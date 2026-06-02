# ============================================================
# Step 12 — Export fully validated BED6 and BED12 files for JBrowse
# Translation-validated + sanity-check-passed projections only
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")

# Final BED outputs after both validation layers:
# Step 10 translation validation + Step 11 sanity checks
bed_dir = Path("python_outputs/bed_validated")
bed_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

# Step 11 output: full sanity-check table built from Step 10 translation-validated rows
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

# Step 12 output summary
step12_summary_out = tables_dir / "wheat_bed_export_validated_summary_step12.csv"

chunk_size = 100_000

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )


# -----------------------------
# 2. Helper functions
# -----------------------------
def make_bed_score(data):
    """
    Create BED score between 0 and 1000.

    Priority:
    1. Probability column scaled to 0–1000, if available
    2. Default score = 1000
    """

    if "Probability" in data.columns:
        score = pd.to_numeric(
            data["Probability"],
            errors="coerce"
        ) * 1000

        score = (
            score
            .fillna(1000)
            .clip(0, 1000)
            .round()
            .astype(int)
        )

    else:
        score = pd.Series([1000] * len(data), index=data.index)

    return score


def clean_bed_name(value):
    """
    Clean BED name field for BED/JBrowse compatibility.
    """

    return (
        str(value)
        .replace(" ", "_")
        .replace(";", "|")
        .replace(",", "|")
        .replace("\t", "_")
        .replace("\n", "_")
    )


def build_bed_name(projected):
    """
    Build informative BED label.

    Priority:
    1. Peptide_intron_gapped_compact, if present
    2. Peptide_intron_gapped, if present
    3. Peptide

    Final structure:
    peptide|protein|gene|validated=translation+sanity|tissues=X
    """

    if "Peptide_intron_gapped_compact" in projected.columns:
        peptide_label = projected["Peptide_intron_gapped_compact"].astype(str)
    elif "Peptide_intron_gapped" in projected.columns:
        peptide_label = projected["Peptide_intron_gapped"].astype(str)
    else:
        peptide_label = projected["Peptide"].astype(str)

    if "GeneID" in projected.columns:
        bed_name = (
            peptide_label + "|" +
            projected["ProteinID"].astype(str) + "|" +
            projected["GeneID"].astype(str)
        )
    else:
        bed_name = (
            peptide_label + "|" +
            projected["ProteinID"].astype(str)
        )

    # Make final BED tracks self-documenting
    bed_name = bed_name + "|validated=translation+sanity"

    # Add tissue count if present
    if "Tissues_count" in projected.columns:
        bed_name = (
            bed_name +
            "|tissues=" +
            projected["Tissues_count"].astype(str)
        )

    return bed_name.apply(clean_bed_name)


def prepare_bed_rows(projected):
    """
    Prepare a sanity-passed DataFrame for BED6/BED12 export.
    """

    required_cols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "ProteinID",
        "Strand",
        "BED_block_count",
        "BED_block_sizes",
        "BED_block_starts",
        "Peptide",
        "Sanity_check_status",
        "All_sanity_checks_passed"
    ]

    missing_cols = [
        col for col in required_cols
        if col not in projected.columns
    ]

    if missing_cols:
        raise KeyError(
            f"Missing required BED column(s): {missing_cols}"
        )

    projected = projected.copy()

    # Create BED score and label
    projected["BED_score"] = make_bed_score(projected)
    projected["BED_name"] = build_bed_name(projected)

    # Force integer coordinate types
    projected["BED_start_0based"] = (
        pd.to_numeric(projected["BED_start_0based"], errors="coerce")
        .astype("Int64")
    )

    projected["BED_end_0based_exclusive"] = (
        pd.to_numeric(projected["BED_end_0based_exclusive"], errors="coerce")
        .astype("Int64")
    )

    projected["BED_block_count"] = (
        pd.to_numeric(projected["BED_block_count"], errors="coerce")
        .astype("Int64")
    )

    # Drop rows with missing essential BED fields, just in case
    before_drop = len(projected)

    projected = projected.dropna(
        subset=[
            "Chromosome",
            "BED_start_0based",
            "BED_end_0based_exclusive",
            "Strand",
            "BED_block_count",
            "BED_block_sizes",
            "BED_block_starts"
        ]
    ).copy()

    dropped_missing_bed_fields = before_drop - len(projected)

    projected["BED_start_0based"] = projected["BED_start_0based"].astype(int)
    projected["BED_end_0based_exclusive"] = projected["BED_end_0based_exclusive"].astype(int)
    projected["BED_block_count"] = projected["BED_block_count"].astype(int)

    return projected, dropped_missing_bed_fields


def make_bed6(projected):
    """
    Build BED6 DataFrame.
    """

    return projected[[
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_name",
        "BED_score",
        "Strand"
    ]].copy()


def make_bed12(projected):
    """
    Build BED12 DataFrame.
    """

    return pd.DataFrame({

        "chrom":
            projected["Chromosome"],

        "chromStart":
            projected["BED_start_0based"],

        "chromEnd":
            projected["BED_end_0based_exclusive"],

        "name":
            projected["BED_name"],

        "score":
            projected["BED_score"],

        "strand":
            projected["Strand"],

        "thickStart":
            projected["BED_start_0based"],

        "thickEnd":
            projected["BED_end_0based_exclusive"],

        "itemRgb":
            "0",

        "blockCount":
            projected["BED_block_count"],

        "blockSizes":
            projected["BED_block_sizes"],

        "blockStarts":
            projected["BED_block_starts"]
    })


# -----------------------------
# 3. Build manifest lookup and output file names
# -----------------------------
manifest_lookup = {}

for _, row in manifest.iterrows():

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    bed6_filename = projection_filename.replace(
        "_peptide_genome_projection.csv",
        "_validated_peptides.bed6"
    )

    bed12_filename = projection_filename.replace(
        "_peptide_genome_projection.csv",
        "_validated_peptides.bed12"
    )

    manifest_lookup[projection_filename] = {
        "Source": row["Source"],
        "Species": row["Species"],
        "Tissue": row["Tissue-Raw-Code"],
        "Batch": row["Batch"],
        "BED6_file": bed6_filename,
        "BED12_file": bed12_filename,
        "BED6_path": bed_dir / bed6_filename,
        "BED12_path": bed_dir / bed12_filename
    }


# Clear previous BED outputs if rerunning this step
for info in manifest_lookup.values():
    for path_key in ["BED6_path", "BED12_path"]:
        path = info[path_key]
        if path.exists():
            path.unlink()

if step12_summary_out.exists():
    step12_summary_out.unlink()


# -----------------------------
# 4. Initialise summary dictionary
# -----------------------------
summary_dict = {}

for projection_filename, info in manifest_lookup.items():

    summary_dict[projection_filename] = {
        "Source": info["Source"],
        "Species": info["Species"],
        "Tissue": info["Tissue"],
        "Batch": info["Batch"],
        "Projection_file": projection_filename,
        "BED6_file": info["BED6_file"],
        "BED12_file": info["BED12_file"],

        "Rows_in_step11_sanity_file": 0,
        "Rows_passing_all_sanity_checks": 0,
        "Rows_excluded_by_sanity_checks": 0,
        "Rows_dropped_missing_BED_fields": 0,

        "BED_rows": 0,
        "Unique_BED_peptides": 0,
        "Unique_BED_proteins": 0,
        "Unique_BED_gene_models": 0,
        "Multi_block_peptides": 0,
        "BED_labels_with_introns": 0
    }


# For unique counts across chunks
unique_peptides = {k: set() for k in manifest_lookup}
unique_proteins = {k: set() for k in manifest_lookup}
unique_genes = {k: set() for k in manifest_lookup}

# Track whether each BED file has already been written to
bed_file_written = {
    projection_filename: {
        "bed6": False,
        "bed12": False
    }
    for projection_filename in manifest_lookup
}


# -----------------------------
# 5. Read Step 11 sanity-check output in chunks and export BED files
# -----------------------------
print("\nExporting BED6/BED12 files from Step 11 sanity-passed rows...")

header = pd.read_csv(sanity_file, nrows=0)

required_step11_cols = [
    "Projection_file",
    "Sanity_check_status",
    "All_sanity_checks_passed"
]

missing_step11_cols = [
    col for col in required_step11_cols
    if col not in header.columns
]

if missing_step11_cols:
    raise KeyError(
        f"Missing required Step 11 column(s): {missing_step11_cols}"
    )

total_rows_read = 0
total_sanity_passed = 0
total_sanity_failed = 0
total_bed_rows = 0

for chunk_i, chunk in enumerate(
    pd.read_csv(
        sanity_file,
        chunksize=chunk_size,
        low_memory=False
    ),
    start=1
):

    total_rows_read += len(chunk)

    # Count sanity status per projection file
    for projection_filename, file_group in chunk.groupby("Projection_file"):

        projection_filename = str(projection_filename)

        if projection_filename not in summary_dict:
            continue

        n_rows = len(file_group)
        n_passed = int((file_group["Sanity_check_status"].astype(str) == "passed").sum())
        n_failed = n_rows - n_passed

        summary_dict[projection_filename]["Rows_in_step11_sanity_file"] += n_rows
        summary_dict[projection_filename]["Rows_passing_all_sanity_checks"] += n_passed
        summary_dict[projection_filename]["Rows_excluded_by_sanity_checks"] += n_failed

    # Keep only rows passing all sanity checks
    passed = chunk[
        chunk["Sanity_check_status"].astype(str) == "passed"
    ].copy()

    total_sanity_passed += len(passed)
    total_sanity_failed += len(chunk) - len(passed)

    if passed.empty:
        print(
            f"Chunk {chunk_i}: read {len(chunk):,} rows | "
            f"no sanity-passed rows"
        )
        continue

    # Export per projection/source-tissue file
    for projection_filename, projected in passed.groupby("Projection_file"):

        projection_filename = str(projection_filename)

        if projection_filename not in manifest_lookup:
            print(f"  Warning: projection file not found in manifest, skipped: {projection_filename}")
            continue

        info = manifest_lookup[projection_filename]

        projected_prepared, dropped_missing_bed_fields = prepare_bed_rows(projected)

        if projected_prepared.empty:
            summary_dict[projection_filename]["Rows_dropped_missing_BED_fields"] += dropped_missing_bed_fields
            continue

        bed6 = make_bed6(projected_prepared)
        bed12 = make_bed12(projected_prepared)

        # Append to BED6
        bed6.to_csv(
            info["BED6_path"],
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )

        # Append to BED12
        bed12.to_csv(
            info["BED12_path"],
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )

        # Update summary
        n_bed = len(projected_prepared)

        summary_dict[projection_filename]["BED_rows"] += n_bed
        summary_dict[projection_filename]["Rows_dropped_missing_BED_fields"] += dropped_missing_bed_fields

        if "Peptide" in projected_prepared.columns:
            unique_peptides[projection_filename].update(
                projected_prepared["Peptide"].dropna().astype(str).unique()
            )

        if "ProteinID" in projected_prepared.columns:
            unique_proteins[projection_filename].update(
                projected_prepared["ProteinID"].dropna().astype(str).unique()
            )

        if "GeneID" in projected_prepared.columns:
            unique_genes[projection_filename].update(
                projected_prepared["GeneID"].dropna().astype(str).unique()
            )

        summary_dict[projection_filename]["Multi_block_peptides"] += int(
            (pd.to_numeric(projected_prepared["BED_block_count"], errors="coerce") > 1).sum()
        )

        summary_dict[projection_filename]["BED_labels_with_introns"] += int(
            projected_prepared["BED_name"]
            .astype(str)
            .str.contains("-", regex=False)
            .sum()
        )

        total_bed_rows += n_bed

    print(
        f"Chunk {chunk_i}: read {len(chunk):,} rows | "
        f"sanity-passed {len(passed):,} | "
        f"cumulative BED rows {total_bed_rows:,}"
    )


# -----------------------------
# 6. Finalise summary table
# -----------------------------
for projection_filename in summary_dict:

    summary_dict[projection_filename]["Unique_BED_peptides"] = len(
        unique_peptides[projection_filename]
    )

    summary_dict[projection_filename]["Unique_BED_proteins"] = len(
        unique_proteins[projection_filename]
    )

    summary_dict[projection_filename]["Unique_BED_gene_models"] = len(
        unique_genes[projection_filename]
    )

step12_summary = pd.DataFrame(summary_dict.values())

step12_summary["Percent_sanity_passed"] = (
    step12_summary["Rows_passing_all_sanity_checks"] /
    step12_summary["Rows_in_step11_sanity_file"] *
    100
).round(4)

step12_summary["Percent_exported_to_BED"] = (
    step12_summary["BED_rows"] /
    step12_summary["Rows_in_step11_sanity_file"] *
    100
).round(4)

step12_summary.to_csv(
    step12_summary_out,
    index=False
)


# -----------------------------
# 7. Overall summary
# -----------------------------
overall_bed_files_bed6 = len(list(bed_dir.glob("*_validated_peptides.bed6")))
overall_bed_files_bed12 = len(list(bed_dir.glob("*_validated_peptides.bed12")))

print("\n===== STEP 12 VALIDATED BED EXPORT SUMMARY =====")
print(f"Rows read from Step 11 sanity-check table: {total_rows_read:,}")
print(f"Rows passing all sanity checks: {total_sanity_passed:,}")
print(f"Rows excluded by sanity checks: {total_sanity_failed:,}")
print(f"Rows exported to BED: {total_bed_rows:,}")
print(f"BED6 files created: {overall_bed_files_bed6:,}")
print(f"BED12 files created: {overall_bed_files_bed12:,}")

print(f"\nBED files saved in: {bed_dir}")
print(f"Step 12 summary saved: {step12_summary_out}")

display(step12_summary)