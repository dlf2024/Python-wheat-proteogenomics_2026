# ============================================================
# Step 9 — Peptide-to-genome projection with intron-gapped labels
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
fasta_file = Path("protein_database/iwgsc_refseqv2.1_annotation_200916_HC_LC_pep_cRAP_with_DECOY.fasta")
gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

step9_summary_out = tables_dir / "wheat_peptide_genome_projection_summary_step9.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 2. FASTA reader
# -----------------------------
def read_fasta_sequences(fasta_path):
    sequences = {}
    current_id = None
    current_seq = []

    with open(fasta_path, "r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_seq)

                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)

        if current_id is not None:
            sequences[current_id] = "".join(current_seq)

    return sequences


# -----------------------------
# 3. Build CDS dictionary once
# -----------------------------
def build_cds_dictionary(gff3_features_file):
    usecols = [
        "SeqID",
        "FeatureType",
        "Start",
        "End",
        "Strand",
        "Phase",
        "Parent"
    ]

    gff = pd.read_csv(
        gff3_features_file,
        usecols=usecols,
        low_memory=False
    )

    cds = gff[gff["FeatureType"].astype(str).str.lower() == "cds"].copy()

    cds["Start"] = cds["Start"].astype(int)
    cds["End"] = cds["End"].astype(int)
    cds["Phase"] = pd.to_numeric(cds["Phase"], errors="coerce").fillna(0).astype(int)

    cds_dict = {}

    for transcript_id, group in cds.groupby("Parent", sort=False):

        strand = group["Strand"].iloc[0]

        if strand == "+":
            group = group.sort_values(["Start", "End"])
        else:
            group = group.sort_values(["End", "Start"], ascending=[False, False])

        cds_dict[transcript_id] = group[[
            "SeqID",
            "Start",
            "End",
            "Strand",
            "Phase"
        ]].to_dict("records")

    return cds_dict


# -----------------------------
# 4. Projection helpers
# -----------------------------
def locate_peptide_in_protein(peptide, protein_sequence):
    peptide_clean = str(peptide).replace("I", "L")
    protein_clean = str(protein_sequence).replace("I", "L")

    start_0based = protein_clean.find(peptide_clean)

    if start_0based == -1:
        return None, None, 0

    occurrence_count = protein_clean.count(peptide_clean)

    aa_start = start_0based + 1
    aa_end = aa_start + len(peptide_clean) - 1

    return aa_start, aa_end, occurrence_count


def build_coding_position_vector_from_blocks(cds_blocks):
    """
    Build transcript-ordered genomic coding positions from CDS blocks.

    Important:
    The GFF3 Phase field is NOT used to trim CDS coordinates here.
    CDS features already define the coding sequence. Phase describes
    codon continuity across CDS features, but bases should not be removed
    when reconstructing peptide genomic positions.
    """
    coding_positions = []

    for block in cds_blocks:
        start = int(block["Start"])
        end = int(block["End"])
        strand = block["Strand"]

        if strand == "+":
            coding_positions.extend(range(start, end + 1))
        else:
            coding_positions.extend(range(end, start - 1, -1))

    return coding_positions


def collapse_positions_to_blocks(genomic_positions):
    if len(genomic_positions) == 0:
        return []

    sorted_positions = sorted(genomic_positions)

    blocks = []
    block_start = sorted_positions[0]
    previous = sorted_positions[0]

    for pos in sorted_positions[1:]:
        if pos == previous + 1:
            previous = pos
        else:
            blocks.append((block_start, previous))
            block_start = pos
            previous = pos

    blocks.append((block_start, previous))

    return blocks


def build_intron_gapped_peptide_from_nt_positions(
    peptide,
    peptide_nt_positions,
    exact_dash_count=True,
    max_dashes=80
):
    """
    Builds a display peptide sequence with dashes inserted where the peptide
    crosses introns.

    The peptide split is based on the actual nucleotide positions contributing
    to each amino acid codon, so the exon boundary placement is exact at
    amino-acid resolution.

    If exact_dash_count=True:
        number of dashes = intron length in nucleotides.
    If exact_dash_count=False:
        dashes are capped to max_dashes for easier JBrowse display.
    """

    peptide = str(peptide)

    if len(peptide_nt_positions) != len(peptide) * 3:
        return peptide

    parts = []

    for aa_index, aa in enumerate(peptide):
        codon_positions = peptide_nt_positions[aa_index * 3:(aa_index + 1) * 3]
        parts.append(aa)

        if aa_index == len(peptide) - 1:
            continue

        next_codon_positions = peptide_nt_positions[(aa_index + 1) * 3:(aa_index + 2) * 3]

        current_genomic_max = max(codon_positions)
        current_genomic_min = min(codon_positions)
        next_genomic_max = max(next_codon_positions)
        next_genomic_min = min(next_codon_positions)

        # Consecutive codons in the same exon are adjacent in genomic space.
        same_exon_forward = next_genomic_min == current_genomic_max + 1
        same_exon_reverse = current_genomic_min == next_genomic_max + 1

        if not (same_exon_forward or same_exon_reverse):

            if next_genomic_min > current_genomic_max:
                intron_nt_len = next_genomic_min - current_genomic_max - 1
            else:
                intron_nt_len = current_genomic_min - next_genomic_max - 1

            if exact_dash_count:
                dash_n = max(1, int(intron_nt_len))
            else:
                dash_n = min(max(3, int(intron_nt_len)), max_dashes)

            parts.append("-" * dash_n)

    return "".join(parts)


# -----------------------------
# 5. Project one tissue
# -----------------------------
def project_one_tissue_peptides_to_genome_fast(source, tissue_raw_code, protein_sequences, cds_dict):

    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(f"No manifest entry found for {source} | {tissue_raw_code}")

    row = match.iloc[0]

    step8_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_gene_mapping.csv"
    )

    step8_path = tables_dir / step8_filename

    mapped = pd.read_csv(step8_path, low_memory=False)

    mapped = mapped[
        mapped["Gene_model_mapping_status"] == "mapped"
    ].copy()

    records = []

    for peptide_row in mapped.itertuples(index=False):

        row_dict = peptide_row._asdict()

        peptide = row_dict["Peptide"]
        protein_id = row_dict["ProteinID"]
        transcript_id = row_dict["TranscriptID"]

        projection_status = "projected"
        peptide_intron_gapped = str(peptide)
        peptide_intron_gapped_compact = str(peptide)

        protein_sequence = protein_sequences.get(protein_id)

        if protein_sequence is None:
            projection_status = "protein_sequence_not_found"
            aa_start = pd.NA
            aa_end = pd.NA
            occurrence_count = pd.NA
            chromosome = pd.NA
            strand = pd.NA
            peptide_blocks = []

        else:
            aa_start, aa_end, occurrence_count = locate_peptide_in_protein(
                peptide,
                protein_sequence
            )

            if aa_start is None:
                projection_status = "peptide_not_found_in_protein"
                aa_start = pd.NA
                aa_end = pd.NA
                chromosome = pd.NA
                strand = pd.NA
                peptide_blocks = []

            else:
                cds_blocks = cds_dict.get(transcript_id)

                if cds_blocks is None:
                    projection_status = "cds_blocks_not_found"
                    chromosome = pd.NA
                    strand = pd.NA
                    peptide_blocks = []

                else:
                    coding_positions = build_coding_position_vector_from_blocks(cds_blocks)

                    nt_start = (int(aa_start) - 1) * 3
                    nt_end = int(aa_end) * 3

                    peptide_nt_positions = coding_positions[nt_start:nt_end]

                    chromosome = cds_blocks[0]["SeqID"]
                    strand = cds_blocks[0]["Strand"]

                    if len(peptide_nt_positions) != len(str(peptide)) * 3:
                        projection_status = "incomplete_coding_projection"
                        peptide_blocks = []
                    else:
                        peptide_blocks = collapse_positions_to_blocks(peptide_nt_positions)

                        # Full-resolution label for BED/JBrowse
                        peptide_intron_gapped = build_intron_gapped_peptide_from_nt_positions(
                            peptide=peptide,
                            peptide_nt_positions=peptide_nt_positions,
                            exact_dash_count=True
                        )
                        
                        # Compact label for CSV storage / downstream loading
                        peptide_intron_gapped_compact = build_intron_gapped_peptide_from_nt_positions(
                            peptide=peptide,
                            peptide_nt_positions=peptide_nt_positions,
                            exact_dash_count=False,
                            max_dashes=10
                        )

        if peptide_blocks:
            genomic_start_1based = min(start for start, end in peptide_blocks)
            genomic_end_1based = max(end for start, end in peptide_blocks)

            bed_start = genomic_start_1based - 1
            bed_end = genomic_end_1based

            block_count = len(peptide_blocks)
            block_sizes = ",".join(str(end - start + 1) for start, end in peptide_blocks)
            block_starts = ",".join(str(start - genomic_start_1based) for start, end in peptide_blocks)

        else:
            genomic_start_1based = pd.NA
            genomic_end_1based = pd.NA
            bed_start = pd.NA
            bed_end = pd.NA
            block_count = 0
            block_sizes = ""
            block_starts = ""

        row_dict.update({
            "AA_start": aa_start,
            "AA_end": aa_end,
            "Peptide_length_AA": len(str(peptide)),
            "Peptide_occurrences_in_protein": occurrence_count,
            "Peptide_intron_gapped": peptide_intron_gapped,
            "Peptide_intron_gapped_compact": peptide_intron_gapped_compact,
            "Chromosome": chromosome,
            "Strand": strand,
            "Genomic_start_1based": genomic_start_1based,
            "Genomic_end_1based": genomic_end_1based,
            "BED_start_0based": bed_start,
            "BED_end_0based_exclusive": bed_end,
            "BED_block_count": block_count,
            "BED_block_sizes": block_sizes,
            "BED_block_starts": block_starts,
            "Projection_status": projection_status
        })

        records.append(row_dict)

    projected = pd.DataFrame(records)

    if "Index" in projected.columns:
        projected = projected.drop(columns=["Index"])

    projected.insert(0, "Index", range(1, len(projected) + 1))

    output_filename = step8_filename.replace(
        "_peptide_protein_gene_mapping.csv",
        "_peptide_genome_projection.csv"
    )

    output_path = tables_dir / output_filename
    projected.to_csv(output_path, index=False)

    print(f"\nSaved: {output_path}")
    print(projected["Projection_status"].value_counts(dropna=False))

    unprojected = projected[
        projected["Projection_status"] != "projected"
    ].copy()

    unprojected_filename = output_filename.replace(
        "_peptide_genome_projection.csv",
        "_unprojected_peptides_for_tblastn.csv"
    )

    unprojected_path = tables_dir / unprojected_filename
    unprojected.to_csv(unprojected_path, index=False)

    print(f"Unprojected peptide table saved: {unprojected_path}")
    print(f"Unprojected rows: {len(unprojected):,}")

    return projected


# -----------------------------
# 6. Pre-load large resources once
# -----------------------------
print("Loading protein FASTA...")
protein_sequences = read_fasta_sequences(fasta_file)
print(f"Protein sequences loaded: {len(protein_sequences):,}")

print("Building CDS dictionary...")
cds_dict = build_cds_dictionary(gff3_features_file)
print(f"Transcript CDS entries loaded: {len(cds_dict):,}")

# # -----------------------------
# # 7-test. Run Step 9 on one tissue only
# # -----------------------------

# test_source = "PXD004720"
# test_tissue = "embryo"

# print(f"\nTEST RUN — Step 9 projection for one tissue only:")
# print(f"Source: {test_source}")
# print(f"Tissue: {test_tissue}")

# test_projection = project_one_tissue_peptides_to_genome_fast(
#     source=test_source,
#     tissue_raw_code=test_tissue,
#     protein_sequences=protein_sequences,
#     cds_dict=cds_dict
# )

# print("\nTest projection completed.")
# print(f"Rows: {len(test_projection):,}")

# display(test_projection.head())
# display(test_projection["Projection_status"].value_counts(dropna=False))

# -----------------------------
# 7. Run all tissues
# -----------------------------
step9_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    projected = project_one_tissue_peptides_to_genome_fast(
        source=source,
        tissue_raw_code=tissue_raw_code,
        protein_sequences=protein_sequences,
        cds_dict=cds_dict
    )

    output_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projected_count = (projected["Projection_status"] == "projected").sum()
    unprojected_count = len(projected) - projected_count

    step9_summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue_raw_code,
        "Batch": batch,
        "Genome_projection_file": output_filename,
        "Peptide_protein_gene_rows": len(projected),
        "Projected_rows": projected_count,
        "Unprojected_rows": unprojected_count,
        "Projection_rate_percent": round((projected_count / len(projected)) * 100, 2) if len(projected) > 0 else 0,
        "Unique_projected_peptides": projected.loc[
            projected["Projection_status"] == "projected", "Peptide"
        ].nunique(),
        "Unique_projected_proteins": projected.loc[
            projected["Projection_status"] == "projected", "ProteinID"
        ].nunique(),
        "Unique_projected_gene_models": projected.loc[
            projected["Projection_status"] == "projected", "GeneID"
        ].nunique() if "GeneID" in projected.columns else pd.NA,
        "Peptides_crossing_CDS_blocks": (
            projected.loc[
                projected["Projection_status"] == "projected", "BED_block_count"
            ] > 1
        ).sum(),
        "Peptides_with_intron_gapped_label": (
            projected.loc[
                projected["Projection_status"] == "projected", "Peptide_intron_gapped"
            ].astype(str).str.contains("-", regex=False)
        ).sum()
    })

step9_summary = pd.DataFrame(step9_summary_records)

step9_summary.to_csv(step9_summary_out, index=False)

print(f"\nStep 9 summary saved: {step9_summary_out}")
display(step9_summary)