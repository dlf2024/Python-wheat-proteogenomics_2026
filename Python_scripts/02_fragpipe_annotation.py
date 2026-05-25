# ============================================================
# Step 6 — Annotate FragPipe peptide/protein output tables
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

output_dir = Path("python_outputs/tables")
output_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 2. Load manifest
# -----------------------------
manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

display(manifest.head())


# -----------------------------
# 3. Helper function
# -----------------------------
def annotate_fragpipe_output(source, tissue_raw_code, result_type):
    """
    Annotate one FragPipe peptide or protein output table with traceability columns.

    Parameters
    ----------
    source : str
        Proteomics dataset source, e.g. "PXD004720", "PXD050500", "MSV000090572".

    tissue_raw_code : str
        Tissue raw code as listed in the manifest, e.g. "anther", "node", "stored-grain".

    result_type : str
        Either "peptide" or "protein".

    Returns
    -------
    pd.DataFrame
        Annotated FragPipe table.
    """

    result_type = result_type.lower()

    if result_type not in ["peptide", "protein"]:
        raise ValueError("result_type must be either 'peptide' or 'protein'.")

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

    # Retrieve input filename from manifest
    if result_type == "peptide":
        input_filename = row["FragPipe-Output-Peptide"]
        anchor_col = "Peptide"
    else:
        input_filename = row["FragPipe-Output-Protein"]
        anchor_col = "Protein"

    input_path = fragpipe_dir / input_filename

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Read FragPipe TSV file
    data = pd.read_csv(input_path, sep="\t", header=0)

    # Check required Protein column for contaminant assignment
    if "Protein" not in data.columns:
        raise KeyError(f"'Protein' column not found in {input_filename}")

    # Add traceability columns
    data["Index"] = range(1, len(data) + 1)
    data["Source"] = row["Source"]
    data["Species"] = row["Species"]
    data["Tissue"] = row["Tissue-Raw-Code"]
    data["Batch"] = row["Batch"]
    data["FragPipe_result"] = result_type
    data["Contaminant"] = data["Protein"].astype(str).str.startswith("Traes").map(
        {True: "no", False: "yes"}
    )

    new_cols = [
        "Index",
        "Source",
        "Species",
        "Tissue",
        "Batch",
        "FragPipe_result",
        "Contaminant"
    ]

    # Insert metadata columns before Peptide or Protein column when possible
    remaining_cols = [col for col in data.columns if col not in new_cols]

    if anchor_col in remaining_cols:
        anchor_pos = remaining_cols.index(anchor_col)
        ordered_cols = (
            remaining_cols[:anchor_pos] +
            new_cols +
            remaining_cols[anchor_pos:]
        )
    else:
        ordered_cols = new_cols + remaining_cols

    data = data[ordered_cols]

    # Save annotated table
    output_filename = input_filename.replace(".tsv", "_annotated.csv")
    output_path = output_dir / output_filename

    data.to_csv(output_path, index=False)

    print(f"Annotated file saved: {output_path}")
    print(f"Rows: {data.shape[0]:,}")
    print(f"Columns: {data.shape[1]:,}")

    return data


# -----------------------------
# 4. Example usage to check code
# -----------------------------

# Example peptide file
annotated_peptide = annotate_fragpipe_output(
    source="PXD050500",
    tissue_raw_code="radicle",
    result_type="peptide"
)

# Example protein file
annotated_protein = annotate_fragpipe_output(
    source="PXD050500",
    tissue_raw_code="radicle",
    result_type="protein"
)

# -----------------------------
# 5. Annotate all FragPipe TSV files
# -----------------------------

for _, row in manifest.iterrows():
    source = row["Source"]
    tissue_raw_code = row["Tissue-Raw-Code"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    annotate_fragpipe_output(
        source=source,
        tissue_raw_code=tissue_raw_code,
        result_type="peptide"
    )

    annotate_fragpipe_output(
        source=source,
        tissue_raw_code=tissue_raw_code,
        result_type="protein"
    )


# -----------------------------
# 6. Create Step 6 summary table
# -----------------------------

step6_summary_records = []

for _, row in manifest.iterrows():
    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    for result_type in ["peptide", "protein"]:

        if result_type == "peptide":
            input_filename = row["FragPipe-Output-Peptide"]
            count_label = "peptide_count"
        else:
            input_filename = row["FragPipe-Output-Protein"]
            count_label = "protein_count"

        annotated_filename = input_filename.replace(".tsv", "_annotated.csv")
        annotated_path = output_dir / annotated_filename

        if not annotated_path.exists():
            print(f"Warning: annotated file not found, skipped: {annotated_path}")
            continue

        data = pd.read_csv(annotated_path)

        total_count = len(data)
        contaminant_count = (data["Contaminant"] == "yes").sum()
        non_contaminant_count = (data["Contaminant"] == "no").sum()

        step6_summary_records.append({
            "Source": source,
            "Species": species,
            "Tissue": tissue_raw_code,
            "Batch": batch,
            "FragPipe_result": result_type,
            "Annotated_file": annotated_filename,
            count_label: total_count,
            "Contaminant_count": contaminant_count,
            "Non_contaminant_count": non_contaminant_count
        })

step6_summary = pd.DataFrame(step6_summary_records)

# Keep peptide/protein counts in one generic column as well
step6_summary["Total_rows"] = step6_summary[["peptide_count", "protein_count"]].sum(axis=1, skipna=True)

# Reorder columns
summary_cols = [
    "Source",
    "Species",
    "Tissue",
    "Batch",
    "FragPipe_result",
    "Annotated_file",
    "Total_rows",
    "peptide_count",
    "protein_count",
    "Contaminant_count",
    "Non_contaminant_count"
]

step6_summary = step6_summary[summary_cols]

# Save summary table
step6_summary_out = output_dir / "wheat_fragpipe_annotation_summary_step6.csv"
step6_summary.to_csv(step6_summary_out, index=False)

print(f"Step 6 summary saved: {step6_summary_out}")
print(f"Summary rows: {step6_summary.shape[0]:,}")

display(step6_summary)