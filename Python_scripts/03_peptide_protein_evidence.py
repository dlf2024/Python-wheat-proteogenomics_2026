# ============================================================
# Step 7 — Build non-contaminant peptide–protein evidence tables
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
step6_summary_file = tables_dir / "wheat_fragpipe_annotation_summary_step6.csv"

step7_summary_out = tables_dir / "wheat_fragpipe_peptide_protein_evidence_summary_step7.csv"

# -----------------------------
# 2. Load manifest
# -----------------------------
manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 3. Helper functions
# -----------------------------
def split_mapped_proteins(value):
    """
    Split FragPipe mapped protein accessions into a clean list.

    Handles empty values and common separators used in protein tables.
    """
    if pd.isna(value):
        return []

    value = str(value).strip()

    if value == "" or value.lower() in ["nan", "na", "none"]:
        return []

    for sep in [";", ","]:
        value = value.replace(sep, "|")

    return [x.strip() for x in value.split("|") if x.strip()]


def find_optional_column(data, possible_names):
    """
    Return the first matching column name from a list of possible names.
    """
    for col in possible_names:
        if col in data.columns:
            return col
    return None


def build_peptide_protein_evidence(source, tissue_raw_code):
    """
    Build a non-contaminant peptide–protein evidence table for one tissue.

    Parameters
    ----------
    source : str
        Proteomics dataset source, e.g. "PXD004720".

    tissue_raw_code : str
        Tissue code as listed in the manifest, e.g. "anther".

    Returns
    -------
    pd.DataFrame
        Expanded peptide–protein evidence table.
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

    # Input annotated peptide file from Step 6
    peptide_filename = row["FragPipe-Output-Peptide"]
    annotated_filename = peptide_filename.replace(".tsv", "_annotated.csv")
    annotated_path = tables_dir / annotated_filename

    if not annotated_path.exists():
        raise FileNotFoundError(f"Annotated peptide file not found: {annotated_path}")

    # Read annotated peptide table
    data = pd.read_csv(annotated_path)

    # Required columns
    required_cols = ["Peptide", "Protein", "Contaminant"]
    missing_cols = [col for col in required_cols if col not in data.columns]

    if missing_cols:
        raise KeyError(
            f"Missing required column(s) in {annotated_filename}: {missing_cols}"
        )

    # Keep wheat-derived identifications only
    data = data[data["Contaminant"] == "no"].copy()

    # Optional FragPipe evidence columns
    mapped_col = find_optional_column(
        data,
        ["Mapped Proteins", "Mapped Protein", "Mapped_Proteins", "Mapped proteins"]
    )

    probability_col = find_optional_column(
        data,
        ["Probability", "PeptideProphet Probability", "Peptide Probability"]
    )

    spectral_count_col = find_optional_column(
        data,
        ["Spectral Count", "Spectral_Count", "SpectralCount"]
    )

    charge_col = find_optional_column(
        data,
        ["Charges", "Charge"]
    )

    records = []

    for _, peptide_row in data.iterrows():

        peptide = peptide_row["Peptide"]
        primary_protein = peptide_row["Protein"]

        # Primary protein evidence
        protein_records = [{
            "ProteinID": primary_protein,
            "Protein_mapping_type": "primary"
        }]

        # Additional mapped proteins / isoforms, when present
        if mapped_col is not None:
            mapped_proteins = split_mapped_proteins(peptide_row[mapped_col])

            for mapped_protein in mapped_proteins:
                if mapped_protein != primary_protein:
                    protein_records.append({
                        "ProteinID": mapped_protein,
                        "Protein_mapping_type": "mapped"
                    })

        for protein_record in protein_records:

            record = {
                "Source": row["Source"],
                "Species": row["Species"],
                "Tissue": row["Tissue-Raw-Code"],
                "Batch": row["Batch"],
                "Peptide": peptide,
                "ProteinID": protein_record["ProteinID"],
                "Protein_mapping_type": protein_record["Protein_mapping_type"],
                "Contaminant": "no"
            }

            if probability_col is not None:
                record["Probability"] = peptide_row[probability_col]

            if spectral_count_col is not None:
                record["Spectral_Count"] = peptide_row[spectral_count_col]

            if charge_col is not None:
                record["Charges"] = peptide_row[charge_col]

            records.append(record)

    evidence = pd.DataFrame(records)

    # Add sequential index
    evidence.insert(0, "Index", range(1, len(evidence) + 1))

    # Remove accidental duplicated peptide–protein rows within a tissue
    # This should usually not be needed, but keeps the output robust.
    evidence = evidence.drop_duplicates(
        subset=["Source", "Tissue", "Peptide", "ProteinID", "Protein_mapping_type"]
    ).reset_index(drop=True)

    evidence["Index"] = range(1, len(evidence) + 1)

    # Save output
    output_filename = peptide_filename.replace(
        "_peptide.tsv",
        "_peptide_protein_evidence.csv"
    )

    output_path = tables_dir / output_filename
    evidence.to_csv(output_path, index=False)

    print(f"Saved peptide–protein evidence table: {output_path}")
    print(f"Rows: {len(evidence):,}")
    print(f"Unique peptides: {evidence['Peptide'].nunique():,}")
    print(f"Unique proteins: {evidence['ProteinID'].nunique():,}")

    return evidence


# -----------------------------
# 4. Run Step 7 for all tissues
# -----------------------------
step7_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    evidence = build_peptide_protein_evidence(
        source=source,
        tissue_raw_code=tissue_raw_code
    )

    output_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_evidence.csv"
    )

    primary_evidence = evidence[evidence["Protein_mapping_type"] == "primary"]
    mapped_evidence = evidence[evidence["Protein_mapping_type"] == "mapped"]

    peptides_per_protein = (
        evidence.groupby("ProteinID")["Peptide"]
        .nunique()
        .reset_index(name="unique_peptides_per_protein")
    )

    proteins_per_peptide = (
        evidence.groupby("Peptide")["ProteinID"]
        .nunique()
        .reset_index(name="protein_isoforms_per_peptide")
    )

    step7_summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue_raw_code,
        "Batch": batch,
        "Evidence_file": output_filename,
        "Non_contaminant_peptide_protein_pairs": len(evidence),
        "Unique_peptides": evidence["Peptide"].nunique(),
        "Unique_proteins": evidence["ProteinID"].nunique(),
        "Primary_peptide_protein_pairs": len(primary_evidence),
        "Mapped_peptide_protein_pairs": len(mapped_evidence),
        "Peptides_mapping_to_multiple_proteins": (
            proteins_per_peptide["protein_isoforms_per_peptide"] > 1
        ).sum(),
        "Proteins_supported_by_one_peptide": (
            peptides_per_protein["unique_peptides_per_protein"] == 1
        ).sum(),
        "Proteins_supported_by_two_or_more_peptides": (
            peptides_per_protein["unique_peptides_per_protein"] >= 2
        ).sum()
    })

step7_summary = pd.DataFrame(step7_summary_records)

# Save Step 7 summary
step7_summary.to_csv(step7_summary_out, index=False)

print(f"\nStep 7 summary saved: {step7_summary_out}")
print(f"Summary rows: {step7_summary.shape[0]:,}")

display(step7_summary)