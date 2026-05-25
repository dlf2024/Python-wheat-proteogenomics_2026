# ============================================================
# Step 8 — Link peptide–protein evidence to wheat gene models
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

step8_summary_out = tables_dir / "wheat_peptide_protein_gene_mapping_summary_step8.csv"

# -----------------------------
# 2. Load manifest and protein-to-gene mapping table
# -----------------------------
manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")
protein_gene_mapping = pd.read_csv(protein_gene_mapping_file)

print("Protein-to-gene mapping table loaded:")
print(f"Rows: {protein_gene_mapping.shape[0]:,}")
print(f"Columns: {protein_gene_mapping.shape[1]:,}")

display(protein_gene_mapping.head())


# -----------------------------
# 3. Helper function
# -----------------------------
def map_peptide_protein_to_gene_models(source, tissue_raw_code):
    """
    Merge one tissue-level peptide–protein evidence table with the
    GFF3-derived wheat protein-to-gene mapping table.

    Parameters
    ----------
    source : str
        Proteomics dataset source, e.g. "PXD004720".

    tissue_raw_code : str
        Tissue code as listed in the manifest, e.g. "anther".

    Returns
    -------
    pd.DataFrame
        Peptide–protein–gene evidence table.
    """

    # Find matching manifest row
    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(
            f"No manifest entry found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    if len(match) > 1:
        raise ValueError(
            f"Multiple manifest entries found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    row = match.iloc[0]

    # Input Step 7 evidence file
    evidence_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_evidence.csv"
    )

    evidence_path = tables_dir / evidence_filename

    if not evidence_path.exists():
        raise FileNotFoundError(f"Step 7 evidence file not found: {evidence_path}")

    evidence = pd.read_csv(evidence_path)

    if "ProteinID" not in evidence.columns:
        raise KeyError(f"'ProteinID' column not found in {evidence_filename}")

    if "ProteinID" not in protein_gene_mapping.columns:
        raise KeyError("'ProteinID' column not found in protein-to-gene mapping table.")

    # Merge peptide–protein evidence with GFF3-derived mapping
    mapped = evidence.merge(
        protein_gene_mapping,
        on="ProteinID",
        how="left",
        indicator=True
    )

    mapped["Gene_model_mapping_status"] = mapped["_merge"].map({
        "both": "mapped",
        "left_only": "unmapped",
        "right_only": "mapping_only"
    })

    mapped = mapped.drop(columns=["_merge"])

    # Add sequential index
    if "Index" in mapped.columns:
        mapped = mapped.drop(columns=["Index"])

    mapped.insert(0, "Index", range(1, len(mapped) + 1))

    # Save output
    output_filename = evidence_filename.replace(
        "_peptide_protein_evidence.csv",
        "_peptide_protein_gene_mapping.csv"
    )

    output_path = tables_dir / output_filename
    mapped.to_csv(output_path, index=False)

    # Mapping summary
    total_pairs = len(mapped)
    mapped_pairs = (mapped["Gene_model_mapping_status"] == "mapped").sum()
    unmapped_pairs = (mapped["Gene_model_mapping_status"] == "unmapped").sum()

    print(f"\nSaved peptide–protein–gene mapping table: {output_path}")
    print(f"Rows: {total_pairs:,}")
    print(f"Mapped pairs: {mapped_pairs:,}")
    print(f"Unmapped pairs: {unmapped_pairs:,}")

    return mapped


# -----------------------------
# 4. Run Step 8 for all tissues
# -----------------------------
step8_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    mapped = map_peptide_protein_to_gene_models(
        source=source,
        tissue_raw_code=tissue_raw_code
    )

    output_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_gene_mapping.csv"
    )

    total_pairs = len(mapped)
    mapped_pairs = (mapped["Gene_model_mapping_status"] == "mapped").sum()
    unmapped_pairs = (mapped["Gene_model_mapping_status"] == "unmapped").sum()

    step8_summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue_raw_code,
        "Batch": batch,
        "Gene_mapping_file": output_filename,
        "Peptide_protein_pairs": total_pairs,
        "Mapped_peptide_protein_pairs": mapped_pairs,
        "Unmapped_peptide_protein_pairs": unmapped_pairs,
        "Mapping_rate_percent": round((mapped_pairs / total_pairs) * 100, 2) if total_pairs > 0 else 0,
        "Unique_peptides": mapped["Peptide"].nunique() if "Peptide" in mapped.columns else pd.NA,
        "Unique_proteins": mapped["ProteinID"].nunique() if "ProteinID" in mapped.columns else pd.NA,
        "Mapped_unique_proteins": mapped.loc[
            mapped["Gene_model_mapping_status"] == "mapped", "ProteinID"
        ].nunique(),
        "Unmapped_unique_proteins": mapped.loc[
            mapped["Gene_model_mapping_status"] == "unmapped", "ProteinID"
        ].nunique(),
        "Unique_gene_models": mapped["GeneID"].nunique() if "GeneID" in mapped.columns else pd.NA,
        "Unique_transcripts": mapped["TranscriptID"].nunique() if "TranscriptID" in mapped.columns else pd.NA
    })

step8_summary = pd.DataFrame(step8_summary_records)

# Save Step 8 summary
step8_summary.to_csv(step8_summary_out, index=False)

print(f"\nStep 8 summary saved: {step8_summary_out}")
print(f"Summary rows: {step8_summary.shape[0]:,}")

display(step8_summary)