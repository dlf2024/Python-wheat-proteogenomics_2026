# ============================================================
# Step 25 — Sanity checks for annotation-guided peptide genome projections
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

sanity_full_out = tables_dir / "wheat_projection_sanity_checks_full_step25.csv"
sanity_failed_out = tables_dir / "wheat_projection_sanity_checks_failed_rows_step25.csv"
sanity_summary_out = tables_dir / "wheat_projection_sanity_checks_summary_step25.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

# -----------------------------
# 2. Expected wheat chromosomes and valid strands
# -----------------------------
valid_chromosomes = {
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D"
}

valid_strands = {"+", "-"}

# -----------------------------
# 3. Helper functions
# -----------------------------
def parse_bed_list(value):
    """
    Convert comma-separated BED block size/start strings into integer lists.
    Handles empty or missing values.
    """
    if pd.isna(value):
        return []

    value = str(value).strip().strip(",")

    if value == "":
        return []

    try:
        return [int(x) for x in value.split(",") if str(x).strip() != ""]
    except ValueError:
        return []


def check_bed_geometry(row):
    """
    Check BED interval and BED12-style block geometry.
    """
    try:
        bed_start = int(row["BED_start_0based"])
        bed_end = int(row["BED_end_0based_exclusive"])
        block_count = int(row["BED_block_count"])
    except Exception:
        return False

    if bed_start < 0:
        return False

    if bed_end <= bed_start:
        return False

    block_sizes = parse_bed_list(row["BED_block_sizes"])
    block_starts = parse_bed_list(row["BED_block_starts"])

    if block_count <= 0:
        return False

    if len(block_sizes) != block_count:
        return False

    if len(block_starts) != block_count:
        return False

    if any(size <= 0 for size in block_sizes):
        return False

    if any(start < 0 for start in block_starts):
        return False

    interval_length = bed_end - bed_start

    # Every block must fit inside the BED interval
    for block_start, block_size in zip(block_starts, block_sizes):
        if block_start + block_size > interval_length:
            return False

    return True


def check_block_nt_length(row):
    """
    Check that the sum of BED block nucleotide lengths matches peptide length × 3.
    """
    try:
        peptide_len = int(row["Peptide_length_AA"])
    except Exception:
        return False

    block_sizes = parse_bed_list(row["BED_block_sizes"])

    if len(block_sizes) == 0:
        return False

    return sum(block_sizes) == peptide_len * 3


def check_chromosome_and_strand(row):
    """
    Check valid chromosome and strand assignment.
    """
    chrom = str(row["Chromosome"])
    strand = str(row["Strand"])

    return chrom in valid_chromosomes and strand in valid_strands


def check_protein_coordinates(row):
    """
    Check that amino-acid coordinates are internally consistent with peptide length.
    """
    try:
        aa_start = int(row["AA_start"])
        aa_end = int(row["AA_end"])
        peptide_len = int(row["Peptide_length_AA"])
    except Exception:
        return False

    if aa_start <= 0:
        return False

    if aa_end < aa_start:
        return False

    if (aa_end - aa_start + 1) != peptide_len:
        return False

    peptide = str(row["Peptide"])

    if len(peptide) != peptide_len:
        return False

    return True


# -----------------------------
# 4. Run sanity checks across all projected peptide tables
# -----------------------------
all_checked = []
summary_records = []

for _, manifest_row in manifest.iterrows():

    source = manifest_row["Source"]
    species = manifest_row["Species"]
    tissue = manifest_row["Tissue-Raw-Code"]
    batch = manifest_row["Batch"]

    projection_filename = manifest_row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Projection file not found, skipped: {projection_path}")
        continue

    data = pd.read_csv(projection_path, low_memory=False)

    # Keep only successfully projected rows
    projected = data[data["Projection_status"] == "projected"].copy()

    if projected.empty:
        print(f"No projected rows found in: {projection_path}")
        continue

    projected["Source"] = source
    projected["Species"] = species
    projected["Tissue"] = tissue
    projected["Batch"] = batch
    projected["Projection_file"] = projection_filename

    # Sanity checks
    projected["Check_BED_geometry"] = projected.apply(check_bed_geometry, axis=1)
    projected["Check_block_nt_length"] = projected.apply(check_block_nt_length, axis=1)
    projected["Check_chromosome_and_strand"] = projected.apply(check_chromosome_and_strand, axis=1)
    projected["Check_protein_coordinates"] = projected.apply(check_protein_coordinates, axis=1)

    check_cols = [
        "Check_BED_geometry",
        "Check_block_nt_length",
        "Check_chromosome_and_strand",
        "Check_protein_coordinates"
    ]

    projected["All_sanity_checks_passed"] = projected[check_cols].all(axis=1)

    projected["Sanity_check_status"] = projected["All_sanity_checks_passed"].map({
        True: "passed",
        False: "failed"
    })

    failed = projected[~projected["All_sanity_checks_passed"]]

    summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue,
        "Batch": batch,
        "Projection_file": projection_filename,
        "Projected_rows_checked": len(projected),
        "Rows_passing_all_sanity_checks": int(projected["All_sanity_checks_passed"].sum()),
        "Rows_failing_any_sanity_check": int((~projected["All_sanity_checks_passed"]).sum()),
        "Percent_passing_all_sanity_checks": round(
            projected["All_sanity_checks_passed"].mean() * 100, 4
        ),
        "BED_geometry_failures": int((~projected["Check_BED_geometry"]).sum()),
        "Block_nt_length_failures": int((~projected["Check_block_nt_length"]).sum()),
        "Chromosome_strand_failures": int((~projected["Check_chromosome_and_strand"]).sum()),
        "Protein_coordinate_failures": int((~projected["Check_protein_coordinates"]).sum())
    })

    print(
        f"{source} | {tissue}: "
        f"{projected['All_sanity_checks_passed'].sum():,} / {len(projected):,} passed"
    )

    all_checked.append(projected)

# -----------------------------
# 5. Combine and export outputs
# -----------------------------
if len(all_checked) == 0:
    raise ValueError("No projected peptide rows were available for sanity checking.")

sanity_full = pd.concat(all_checked, ignore_index=True)
sanity_summary = pd.DataFrame(summary_records)

sanity_failed = sanity_full[
    sanity_full["Sanity_check_status"] == "failed"
].copy()

sanity_full.to_csv(sanity_full_out, index=False)
sanity_failed.to_csv(sanity_failed_out, index=False)
sanity_summary.to_csv(sanity_summary_out, index=False)

# -----------------------------
# 6. Overall summary
# -----------------------------
overall_checked = len(sanity_full)
overall_passed = int(sanity_full["All_sanity_checks_passed"].sum())
overall_failed = overall_checked - overall_passed
overall_pass_percent = round((overall_passed / overall_checked) * 100, 4)

print("\n===== STEP 25 SANITY CHECK SUMMARY =====")
print(f"Projected rows checked: {overall_checked:,}")
print(f"Rows passing all sanity checks: {overall_passed:,}")
print(f"Rows failing at least one sanity check: {overall_failed:,}")
print(f"Overall pass rate: {overall_pass_percent}%")

print(f"\nFull sanity-check table saved: {sanity_full_out}")
print(f"Failed-row diagnostic table saved: {sanity_failed_out}")
print(f"Tissue-level sanity summary saved: {sanity_summary_out}")

display(sanity_summary)
display(sanity_failed.head(20))