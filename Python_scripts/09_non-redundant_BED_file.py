# ============================================================
# Step 27 — Create non-redundant combined validated BED tracks
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
validated_bed_dir = Path("python_outputs/bed_Apollo_validated")
tables_dir = Path("python_outputs/tables")

tables_dir.mkdir(parents=True, exist_ok=True)

combined_bed6_out = validated_bed_dir / "Vincent_all-tissues_validated_projected-peptides_annotation-proteogenomics_20260518.bed6"
combined_bed12_out = validated_bed_dir / "Vincent_all-tissues_validated_projected-peptides_annotation-proteogenomics_20260518.bed12"

summary_out = tables_dir / "wheat_combined_validated_bed_summary_step27.csv"

# -----------------------------
# 2. Find validated BED files
# -----------------------------
bed_files = sorted({
    path.resolve()
    for path in validated_bed_dir.iterdir()
    if path.is_file() and path.suffix.lower() in {".bed6", ".bed12"}
})

bed_files = [Path(path) for path in bed_files]

# Exclude previous combined outputs if rerunning
bed_files = [
    path for path in bed_files
    if not path.name.startswith("Vincent_all-tissues_validated_projected-peptides")
]

if len(bed_files) == 0:
    raise FileNotFoundError(
        f"No validated BED6/BED12 files found in: {validated_bed_dir}"
    )

bed6_files = [path for path in bed_files if path.suffix.lower() == ".bed6"]
bed12_files = [path for path in bed_files if path.suffix.lower() == ".bed12"]

print(f"Validated BED6 files found: {len(bed6_files)}")
print(f"Validated BED12 files found: {len(bed12_files)}")

# -----------------------------
# 3. Helper function
# -----------------------------
def combine_bed_files_nonredundant(bed_file_list, output_file, expected_min_cols):
    """
    Combine BED files and remove visually duplicated BED features.

    Unlike exact row deduplication, this collapses rows that represent the
    same browser feature but have different BED scores, keeping the highest score.
    """

    combined_chunks = []
    input_row_count = 0

    for bed_file in bed_file_list:
        print(f"Reading: {bed_file.name}")

        data = pd.read_csv(
            bed_file,
            sep="\t",
            header=None,
            comment="#",
            low_memory=False
        )

        if data.shape[1] < expected_min_cols:
            print(f"  Skipped: fewer than {expected_min_cols} columns")
            continue

        data = data.iloc[:, :expected_min_cols].copy()
        input_row_count += len(data)
        combined_chunks.append(data)

    if len(combined_chunks) == 0:
        raise ValueError(f"No valid BED files available for: {output_file.name}")

    combined = pd.concat(combined_chunks, ignore_index=True)
    rows_before_dedup = len(combined)

    # Ensure coordinates and score are numeric
    combined[1] = pd.to_numeric(combined[1], errors="coerce")
    combined[2] = pd.to_numeric(combined[2], errors="coerce")
    combined[4] = pd.to_numeric(combined[4], errors="coerce").fillna(1000).astype(int)

    if expected_min_cols == 6:
        # BED6: chrom, start, end, name, score, strand
        dedup_cols = [0, 1, 2, 3, 5]

        combined = (
            combined
            .groupby(dedup_cols, dropna=False, as_index=False)
            .agg({4: "max"})
        )

        combined = combined[[0, 1, 2, 3, 4, 5]]

    elif expected_min_cols == 12:
        # BED12: collapse same feature/block structure, keep max score
        dedup_cols = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

        combined = (
            combined
            .groupby(dedup_cols, dropna=False, as_index=False)
            .agg({4: "max"})
        )

        combined = combined[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

    else:
        raise ValueError("Only BED6 and BED12 are supported.")

    rows_after_dedup = len(combined)

    combined = (
        combined
        .sort_values(by=[0, 1, 2])
        .reset_index(drop=True)
    )

    # Restore integer coordinate display
    for col in [1, 2, 4]:
        combined[col] = combined[col].astype("Int64").astype(str)

    if expected_min_cols == 12:
        for col in [6, 7, 9]:
            combined[col] = pd.to_numeric(combined[col], errors="coerce").astype("Int64").astype(str)

    combined.to_csv(
        output_file,
        sep="\t",
        header=False,
        index=False
    )

    return {
        "Output_file": output_file.name,
        "Input_files": len(bed_file_list),
        "Input_rows_total": input_row_count,
        "Rows_before_deduplication": rows_before_dedup,
        "Rows_after_deduplication": rows_after_dedup,
        "Duplicate_rows_removed": rows_before_dedup - rows_after_dedup
    }

# -----------------------------
# 4. Combine BED6 files
# -----------------------------
summary_records = []

if len(bed6_files) > 0:
    bed6_summary = combine_bed_files_nonredundant(
        bed_file_list=bed6_files,
        output_file=combined_bed6_out,
        expected_min_cols=6
    )
    bed6_summary["BED_format"] = "BED6"
    summary_records.append(bed6_summary)

# -----------------------------
# 5. Combine BED12 files
# -----------------------------
if len(bed12_files) > 0:
    bed12_summary = combine_bed_files_nonredundant(
        bed_file_list=bed12_files,
        output_file=combined_bed12_out,
        expected_min_cols=12
    )
    bed12_summary["BED_format"] = "BED12"
    summary_records.append(bed12_summary)

# -----------------------------
# 6. Save summary
# -----------------------------
summary = pd.DataFrame(summary_records)

summary = summary[
    [
        "BED_format",
        "Output_file",
        "Input_files",
        "Input_rows_total",
        "Rows_before_deduplication",
        "Rows_after_deduplication",
        "Duplicate_rows_removed"
    ]
]

summary.to_csv(summary_out, index=False)

print("\n===== STEP 27 COMBINED VALIDATED BED SUMMARY =====")
display(summary)

print(f"\nCombined BED6 saved: {combined_bed6_out}")
print(f"Combined BED12 saved: {combined_bed12_out}")
print(f"Summary saved: {summary_out}")