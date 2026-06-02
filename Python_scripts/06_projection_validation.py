# ============================================================
# Step 10 — Validate peptide genome projections by translation
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path
import re

# -----------------------------
# 1. User settings
# -----------------------------
tables_dir = Path("python_outputs/tables")
genome_fasta = Path("genome_annotation/iwgsc_refseqv2.1_assembly.fa")

sample_fraction = 1 # to test on a portion of the data, lower this number (e.g. 0.1 for 10% of the data)
chunk_size = 30_000 # reduce this for low performance computer
random_seed = 42

validation_out = tables_dir / "wheat_projection_validation_stratified100percent_step10.csv"
summary_out = tables_dir / "wheat_projection_validation_100%_summary_step10.csv"
tissue_summary_out = tables_dir / "wheat_projection_validation_100%_tissue_summary_step10.csv"

# Clear previous output if rerunning
if validation_out.exists():
    validation_out.unlink()

# -----------------------------
# 2. Check pyfaidx availability
# -----------------------------
try:
    from pyfaidx import Fasta
except ImportError:
    raise ImportError(
        "Install pyfaidx first:\n\npip install pyfaidx"
    )

# -----------------------------
# 3. Find projection files
# -----------------------------
projection_files = sorted(tables_dir.glob("*_peptide_genome_projection.csv"))

if len(projection_files) == 0:
    raise FileNotFoundError(
        f"No Step 9 projection files found in: {tables_dir}"
    )

print(f"Projection files found: {len(projection_files)}")

if not genome_fasta.exists():
    raise FileNotFoundError(f"Genome FASTA not found:\n{genome_fasta}")

# -----------------------------
# 4. Helper functions
# -----------------------------
def clean_peptide_sequence(seq):
    seq = str(seq).upper()
    seq = re.sub(r"[^ACDEFGHIKLMNPQRSTVWY]", "", seq)
    return seq


def il_normalise(seq):
    return str(seq).upper().replace("I", "L")


def reverse_complement(seq):
    complement = str.maketrans("ACGTNacgtn", "TGCANtgcan")
    return str(seq).translate(complement)[::-1].upper()


genetic_code = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def translate_dna(seq):
    seq = str(seq).upper()
    return "".join(
        genetic_code.get(seq[i:i + 3], "X")
        for i in range(0, len(seq) - 2, 3)
    )


def parse_bed_blocks(row):
    feature_start_1based = int(row["BED_start_0based"]) + 1

    sizes = [
        int(x) for x in str(row["BED_block_sizes"]).strip(",").split(",")
        if str(x).strip() != ""
    ]

    starts = [
        int(x) for x in str(row["BED_block_starts"]).strip(",").split(",")
        if str(x).strip() != ""
    ]

    if len(sizes) != len(starts):
        return []

    return [
        (feature_start_1based + rel_start,
         feature_start_1based + rel_start + size - 1)
        for size, rel_start in zip(sizes, starts)
    ]


def extract_projected_cds(row, genome):
    chrom = str(row["Chromosome"])
    strand = str(row["Strand"])

    blocks = parse_bed_blocks(row)

    if len(blocks) == 0:
        return ""

    seq_parts = []

    for start, end in blocks:
        seq_parts.append(genome[chrom][start - 1:end].seq)

    cds_seq = "".join(seq_parts).upper()

    if strand == "-":
        cds_seq = reverse_complement(cds_seq)

    return cds_seq


def validate_projection_row(row_dict, genome):
    peptide = clean_peptide_sequence(row_dict["Peptide"])
    validation_status = "validated"

    try:
        cds_seq = extract_projected_cds(row_dict, genome)
        translated = translate_dna(cds_seq)

        exact_match = translated == peptide
        il_match = il_normalise(translated) == il_normalise(peptide)

        expected_nt_length = len(peptide) * 3
        observed_nt_length = len(cds_seq)

        if observed_nt_length != expected_nt_length:
            validation_status = "length_mismatch"
        elif "N" in cds_seq:
            validation_status = "contains_N"
        elif not il_match:
            validation_status = "translation_mismatch"

    except KeyError:
        cds_seq = ""
        translated = ""
        exact_match = False
        il_match = False
        expected_nt_length = len(peptide) * 3
        observed_nt_length = 0
        validation_status = "chromosome_not_found_in_genome_fasta"

    except Exception as e:
        cds_seq = ""
        translated = ""
        exact_match = False
        il_match = False
        expected_nt_length = len(peptide) * 3
        observed_nt_length = 0
        validation_status = f"error: {type(e).__name__}"

    row_dict.update({
        "Original_peptide_clean": peptide,
        "Reconstructed_CDS_length_nt": observed_nt_length,
        "Expected_CDS_length_nt": expected_nt_length,
        "Translated_projected_peptide": translated,
        "Exact_match": exact_match,
        "IL_normalised_match": il_match,
        "Validation_status": validation_status
    })

    return row_dict


# -----------------------------
# 5. Required columns
# -----------------------------
required_cols = [
    "Source",
    "Species",
    "Tissue",
    "Batch",
    "Peptide",
    "ProteinID",
    "TranscriptID",
    "GeneModel",
    "GeneID",
    "Annotation_confidence",
    "Chromosome",
    "Strand",
    "AA_start",
    "AA_end",
    "BED_start_0based",
    "BED_end_0based_exclusive",
    "BED_block_count",
    "BED_block_sizes",
    "BED_block_starts",
    "Projection_status",
    "Probability",
    "Peptide_intron_gapped",
    "Peptide_intron_gapped_compact",
    "Tissues_count"
]

# -----------------------------
# 6. Open genome FASTA
# -----------------------------
print("\nOpening indexed genome FASTA...")

# Use rebuild=True only the first time. Afterwards, rebuild=False is faster.
genome = Fasta(str(genome_fasta), rebuild=False)

print(f"Genome sequences available: {len(genome.keys()):,}")

# -----------------------------
# 7. Validate stratified 100% per projection file
# -----------------------------
rng = np.random.default_rng(random_seed)

overall_records = []
tissue_summary_records = []
header_written = False

print("\nValidating stratified 100% sample per tissue/source...")

for file_i, projection_file in enumerate(projection_files, start=1):

    print(f"\n[{file_i}/{len(projection_files)}] {projection_file.name}")

    header = pd.read_csv(projection_file, nrows=0)
    available_cols = [c for c in required_cols if c in header.columns]

    file_total_projected = 0
    file_sampled = 0
    file_exact = 0
    file_il = 0
    file_multiblock = 0
    file_negative = 0
    file_status_counts = {}

    for chunk_i, chunk in enumerate(
        pd.read_csv(
            projection_file,
            usecols=available_cols,
            chunksize=chunk_size,
            low_memory=True
        ),
        start=1
    ):

        if "Projection_status" not in chunk.columns:
            continue

        chunk = chunk[chunk["Projection_status"] == "projected"].copy()

        if chunk.empty:
            continue

        file_total_projected += len(chunk)

        # Stratified 100% sample within this file/chunk
        sampled = chunk.sample(
            frac=sample_fraction,
            random_state=random_seed + file_i + chunk_i
        ).copy()

        if sampled.empty:
            continue

        sampled["_source_file"] = projection_file.name

        validation_records = []

        for row in sampled.itertuples(index=False):
            row_dict = row._asdict()
            validation_records.append(validate_projection_row(row_dict, genome))

        validation_chunk = pd.DataFrame(validation_records)

        # Update counters
        file_sampled += len(validation_chunk)
        file_exact += int(validation_chunk["Exact_match"].sum())
        file_il += int(validation_chunk["IL_normalised_match"].sum())
        file_multiblock += int(
            (pd.to_numeric(validation_chunk["BED_block_count"], errors="coerce") > 1).sum()
        )
        file_negative += int((validation_chunk["Strand"].astype(str) == "-").sum())

        for status, count in validation_chunk["Validation_status"].value_counts().items():
            file_status_counts[status] = file_status_counts.get(status, 0) + int(count)

        # Append to CSV immediately
        validation_chunk.to_csv(
            validation_out,
            index=False,
            mode="a",
            header=not header_written
        )

        header_written = True

        print(
            f"  Chunk {chunk_i}: sampled {len(validation_chunk):,} "
            f"| cumulative sampled {file_sampled:,}"
        )

    tissue_summary_records.append({
        "Projection_file": projection_file.name,
        "Projected_rows_available": file_total_projected,
        "Sample_fraction": sample_fraction,
        "Rows_validated": file_sampled,
        "Exact_translation_matches": file_exact,
        "Exact_translation_match_rate_percent": round((file_exact / file_sampled) * 100, 2) if file_sampled > 0 else pd.NA,
        "IL_normalised_translation_matches": file_il,
        "IL_normalised_translation_match_rate_percent": round((file_il / file_sampled) * 100, 2) if file_sampled > 0 else pd.NA,
        "Multi_block_peptide_projections_tested": file_multiblock,
        "Negative_strand_peptide_projections_tested": file_negative,
        **{f"Validation_status_{k}": v for k, v in file_status_counts.items()}
    })

# -----------------------------
# 8. Build final summaries
# -----------------------------
tissue_summary = pd.DataFrame(tissue_summary_records)
tissue_summary.to_csv(tissue_summary_out, index=False)

total_validated = int(tissue_summary["Rows_validated"].sum())
total_exact = int(tissue_summary["Exact_translation_matches"].sum())
total_il = int(tissue_summary["IL_normalised_translation_matches"].sum())
total_multiblock = int(tissue_summary["Multi_block_peptide_projections_tested"].sum())
total_negative = int(tissue_summary["Negative_strand_peptide_projections_tested"].sum())

summary_records = [
    {"Metric": "Sampling strategy", "Value": "100% stratified per projection file/source-tissue"},
    {"Metric": "Sample fraction", "Value": sample_fraction},
    {"Metric": "Projection files validated", "Value": len(tissue_summary)},
    {"Metric": "Projected rows available across files", "Value": int(tissue_summary["Projected_rows_available"].sum())},
    {"Metric": "Projected peptide rows validated", "Value": total_validated},
    {"Metric": "Exact translation matches", "Value": total_exact},
    {"Metric": "Exact translation match rate (%)", "Value": round((total_exact / total_validated) * 100, 2) if total_validated > 0 else pd.NA},
    {"Metric": "I/L-normalised translation matches", "Value": total_il},
    {"Metric": "I/L-normalised translation match rate (%)", "Value": round((total_il / total_validated) * 100, 2) if total_validated > 0 else pd.NA},
    {"Metric": "Multi-block peptide projections tested", "Value": total_multiblock},
    {"Metric": "Negative-strand peptide projections tested", "Value": total_negative}
]

status_cols = [c for c in tissue_summary.columns if c.startswith("Validation_status_")]

for col in status_cols:
    summary_records.append({
        "Metric": col.replace("Validation_status_", "Validation status: "),
        "Value": int(tissue_summary[col].fillna(0).sum())
    })

summary_df = pd.DataFrame(summary_records)
summary_df.to_csv(summary_out, index=False)

print("\n===== STEP 10 STRATIFIED VALIDATION SUMMARY =====")
display(summary_df)

print(f"\nValidation table saved: {validation_out}")
print(f"Tissue-level validation summary saved: {tissue_summary_out}")
print(f"Overall validation summary saved: {summary_out}")