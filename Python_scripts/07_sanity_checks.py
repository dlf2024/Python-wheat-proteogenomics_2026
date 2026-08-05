# ============================================================
# Step 11 — Sanity checks for translation-validated peptide genome projections
# ============================================================

import pandas as pd
from pathlib import Path


# -----------------------------
# 1. Input / output paths
# -----------------------------

fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = (
    fragpipe_dir
    / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
)

sanity_full_out = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"
)

sanity_failed_out = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_failed_rows_step11.csv"
)

sanity_summary_out = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_summary_step11.csv"
)

manifest = pd.read_csv(
    manifest_file,
    encoding="utf-8-sig"
)

# Step 10 output: full translation-validation table
validation_file = (
    tables_dir
    / "wheat_projection_validation_stratified100percent_step10.csv"
)

if not validation_file.exists():
    raise FileNotFoundError(
        f"Step 10 translation-validation file not found:\n"
        f"{validation_file}\n\n"
        "Please run Step 10 first."
    )


# -----------------------------
# 2. Expected wheat sequence identifiers and valid strands
# -----------------------------

# ChrUnknown is a valid sequence identifier in the
# IWGSC RefSeq v2.1 GFF3 annotation and must therefore
# pass this annotation-consistency check.
valid_chromosomes = {
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D",
    "ChrUnknown"
}

valid_strands = {
    "+",
    "-"
}


# -----------------------------
# 3. Helper functions
# -----------------------------

def parse_bed_list(value):
    """
    Convert comma-separated BED block-size or block-start
    strings into integer lists.

    Empty or missing values return an empty list.
    """

    if pd.isna(value):
        return []

    value = str(value).strip().strip(",")

    if value == "":
        return []

    try:
        return [
            int(item)
            for item in value.split(",")
            if str(item).strip() != ""
        ]

    except ValueError:
        return []


def check_bed_geometry(row):
    """
    Check BED interval and BED12-style block geometry.
    """

    try:
        bed_start = int(
            row["BED_start_0based"]
        )

        bed_end = int(
            row["BED_end_0based_exclusive"]
        )

        block_count = int(
            row["BED_block_count"]
        )

    except Exception:
        return False

    if bed_start < 0:
        return False

    if bed_end <= bed_start:
        return False

    block_sizes = parse_bed_list(
        row["BED_block_sizes"]
    )

    block_starts = parse_bed_list(
        row["BED_block_starts"]
    )

    if block_count <= 0:
        return False

    if len(block_sizes) != block_count:
        return False

    if len(block_starts) != block_count:
        return False

    if any(
        size <= 0
        for size in block_sizes
    ):
        return False

    if any(
        start < 0
        for start in block_starts
    ):
        return False

    interval_length = (
        bed_end
        - bed_start
    )

    # Every block must fit inside the BED interval.
    for block_start, block_size in zip(
        block_starts,
        block_sizes
    ):

        if (
            block_start
            + block_size
            > interval_length
        ):
            return False

    return True


def check_block_nt_length(row):
    """
    Check that the sum of BED block nucleotide lengths
    matches peptide length multiplied by three.
    """

    try:
        peptide_length = int(
            row["Peptide_length_AA"]
        )

    except Exception:
        return False

    block_sizes = parse_bed_list(
        row["BED_block_sizes"]
    )

    if len(block_sizes) == 0:
        return False

    return (
        sum(block_sizes)
        == peptide_length * 3
    )


def check_chromosome_and_strand(row):
    """
    Check that the sequence identifier is represented in the
    IWGSC RefSeq v2.1 annotation and that the strand is valid.

    ChrUnknown is retained because it is a valid GFF3 sequence
    identifier representing unplaced annotated sequence.
    """

    chromosome = str(
        row["Chromosome"]
    ).strip()

    strand = str(
        row["Strand"]
    ).strip()

    return (
        chromosome in valid_chromosomes
        and strand in valid_strands
    )


def check_protein_coordinates(row):
    """
    Check that amino-acid coordinates are internally
    consistent with peptide length.
    """

    try:
        aa_start = int(
            row["AA_start"]
        )

        aa_end = int(
            row["AA_end"]
        )

        peptide_length = int(
            row["Peptide_length_AA"]
        )

    except Exception:
        return False

    if aa_start <= 0:
        return False

    if aa_end < aa_start:
        return False

    if (
        aa_end
        - aa_start
        + 1
        != peptide_length
    ):
        return False

    peptide = str(
        row["Peptide"]
    )

    if len(peptide) != peptide_length:
        return False

    return True


# -----------------------------
# 4. Run sanity checks across Step 10 output
# -----------------------------

print(
    "\nRunning sanity checks on Step 10 "
    "translation-validated projections..."
)

chunk_size = 100_000

# Overwrite previous Step 11 outputs.
for output_file in [
    sanity_full_out,
    sanity_failed_out,
    sanity_summary_out
]:

    if output_file.exists():
        output_file.unlink()


# Build lookup from Step 9 projection filename
# to manifest metadata.
manifest_lookup = {}

for _, manifest_row in manifest.iterrows():

    projection_filename = (
        manifest_row[
            "FragPipe-Output-Peptide"
        ]
        .replace(
            "_peptide.tsv",
            "_peptide_genome_projection.csv"
        )
    )

    manifest_lookup[
        projection_filename
    ] = {
        "Source":
            manifest_row["Source"],

        "Species":
            manifest_row["Species"],

        "Tissue":
            manifest_row["Tissue-Raw-Code"],

        "Batch":
            manifest_row["Batch"]
    }


def detect_source_file_column(chunk):
    """
    Detect the column containing the original Step 9
    projection filename.

    Step 10 intended to write '_source_file', but pandas
    itertuples() may rename columns beginning with an
    underscore into positional names.

    This function first checks for '_source_file', then
    searches for a column containing values ending in
    '_peptide_genome_projection.csv'.
    """

    if "_source_file" in chunk.columns:
        return "_source_file"

    for column in chunk.columns:

        sample_values = (
            chunk[column]
            .dropna()
            .astype(str)
            .head(20)
        )

        if sample_values.str.contains(
            "_peptide_genome_projection.csv",
            regex=False
        ).any():

            return column

    return None


summary_dict = {}

header_written_full = False
header_written_failed = False

first_failed_examples = []

source_file_column = None

total_rows_read = 0
total_translation_validated = 0
total_translation_excluded = 0


for chunk_number, chunk in enumerate(

    pd.read_csv(
        validation_file,
        chunksize=chunk_size,
        low_memory=False
    ),

    start=1
):

    total_rows_read += len(
        chunk
    )

    # Detect the source-file column once.
    if source_file_column is None:

        source_file_column = (
            detect_source_file_column(
                chunk
            )
        )

        if source_file_column is None:

            raise KeyError(
                "Could not identify the Step 10 source-file "
                "column. Expected '_source_file' or a column "
                "containing values ending with "
                "'_peptide_genome_projection.csv'."
            )

        print(
            "Detected Step 10 source-file column: "
            f"{source_file_column}"
        )

    if "Validation_status" not in chunk.columns:

        raise KeyError(
            "Column 'Validation_status' was not found "
            "in the Step 10 validation table."
        )

    # Count all Step 10 rows by source file
    # and translation-validation status.
    for projection_filename, file_group in chunk.groupby(
        source_file_column
    ):

        projection_filename = str(
            projection_filename
        )

        if projection_filename not in summary_dict:

            metadata = manifest_lookup.get(
                projection_filename,
                {
                    "Source": pd.NA,
                    "Species": pd.NA,
                    "Tissue": pd.NA,
                    "Batch": pd.NA
                }
            )

            summary_dict[
                projection_filename
            ] = {
                "Source":
                    metadata["Source"],

                "Species":
                    metadata["Species"],

                "Tissue":
                    metadata["Tissue"],

                "Batch":
                    metadata["Batch"],

                "Projection_file":
                    projection_filename,

                "Rows_from_step10_validation_table":
                    0,

                "Rows_translation_validated":
                    0,

                "Rows_excluded_by_translation_validation":
                    0,

                "Translation_validated_rows_checked":
                    0,

                "Rows_passing_all_sanity_checks":
                    0,

                "Rows_failing_any_sanity_check":
                    0,

                "BED_geometry_failures":
                    0,

                "Block_nt_length_failures":
                    0,

                "Chromosome_strand_failures":
                    0,

                "Protein_coordinate_failures":
                    0
            }

        summary_dict[
            projection_filename
        ][
            "Rows_from_step10_validation_table"
        ] += len(
            file_group
        )

        number_validated = int(
            (
                file_group[
                    "Validation_status"
                ]
                .astype(str)
                == "validated"
            ).sum()
        )

        number_excluded = (
            len(file_group)
            - number_validated
        )

        summary_dict[
            projection_filename
        ][
            "Rows_translation_validated"
        ] += number_validated

        summary_dict[
            projection_filename
        ][
            "Rows_excluded_by_translation_validation"
        ] += number_excluded


    # Retain only translation-validated rows
    # for Step 11 sanity checking.
    projected = chunk[
        chunk[
            "Validation_status"
        ]
        .astype(str)
        == "validated"
    ].copy()

    total_translation_validated += len(
        projected
    )

    total_translation_excluded += (
        len(chunk)
        - len(projected)
    )

    if projected.empty:

        print(
            f"Chunk {chunk_number}: "
            f"read {len(chunk):,} rows | "
            "no translation-validated rows"
        )

        continue


    # Derive peptide length when not already present.
    if "Peptide_length_AA" not in projected.columns:

        if (
            "Original_peptide_clean"
            in projected.columns
        ):

            projected[
                "Peptide_length_AA"
            ] = (
                projected[
                    "Original_peptide_clean"
                ]
                .astype(str)
                .str.len()
            )

        else:

            projected[
                "Peptide_length_AA"
            ] = (
                projected["Peptide"]
                .astype(str)
                .str.len()
            )


    # Add or standardise projection-file metadata.
    projected[
        "Projection_file"
    ] = (
        projected[
            source_file_column
        ]
        .astype(str)
    )

    projected["Source"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Source",
                pd.NA
            )
        )
    )

    projected["Species"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Species",
                pd.NA
            )
        )
    )

    projected["Tissue"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Tissue",
                pd.NA
            )
        )
    )

    projected["Batch"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Batch",
                pd.NA
            )
        )
    )


    # Run the four sanity checks.
    projected[
        "Check_BED_geometry"
    ] = projected.apply(
        check_bed_geometry,
        axis=1
    )

    projected[
        "Check_block_nt_length"
    ] = projected.apply(
        check_block_nt_length,
        axis=1
    )

    projected[
        "Check_chromosome_and_strand"
    ] = projected.apply(
        check_chromosome_and_strand,
        axis=1
    )

    projected[
        "Check_protein_coordinates"
    ] = projected.apply(
        check_protein_coordinates,
        axis=1
    )

    check_columns = [
        "Check_BED_geometry",
        "Check_block_nt_length",
        "Check_chromosome_and_strand",
        "Check_protein_coordinates"
    ]

    projected[
        "All_sanity_checks_passed"
    ] = (
        projected[
            check_columns
        ]
        .all(axis=1)
    )

    projected[
        "Sanity_check_status"
    ] = (
        projected[
            "All_sanity_checks_passed"
        ]
        .map({
            True: "passed",
            False: "failed"
        })
    )


    # Update source–tissue summary counts.
    for projection_filename, file_group in projected.groupby(
        "Projection_file"
    ):

        projection_filename = str(
            projection_filename
        )

        if projection_filename not in summary_dict:

            metadata = manifest_lookup.get(
                projection_filename,
                {
                    "Source": pd.NA,
                    "Species": pd.NA,
                    "Tissue": pd.NA,
                    "Batch": pd.NA
                }
            )

            summary_dict[
                projection_filename
            ] = {
                "Source":
                    metadata["Source"],

                "Species":
                    metadata["Species"],

                "Tissue":
                    metadata["Tissue"],

                "Batch":
                    metadata["Batch"],

                "Projection_file":
                    projection_filename,

                "Rows_from_step10_validation_table":
                    0,

                "Rows_translation_validated":
                    0,

                "Rows_excluded_by_translation_validation":
                    0,

                "Translation_validated_rows_checked":
                    0,

                "Rows_passing_all_sanity_checks":
                    0,

                "Rows_failing_any_sanity_check":
                    0,

                "BED_geometry_failures":
                    0,

                "Block_nt_length_failures":
                    0,

                "Chromosome_strand_failures":
                    0,

                "Protein_coordinate_failures":
                    0
            }

        summary_dict[
            projection_filename
        ][
            "Translation_validated_rows_checked"
        ] += len(
            file_group
        )

        summary_dict[
            projection_filename
        ][
            "Rows_passing_all_sanity_checks"
        ] += int(
            file_group[
                "All_sanity_checks_passed"
            ].sum()
        )

        summary_dict[
            projection_filename
        ][
            "Rows_failing_any_sanity_check"
        ] += int(
            (
                ~file_group[
                    "All_sanity_checks_passed"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "BED_geometry_failures"
        ] += int(
            (
                ~file_group[
                    "Check_BED_geometry"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "Block_nt_length_failures"
        ] += int(
            (
                ~file_group[
                    "Check_block_nt_length"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "Chromosome_strand_failures"
        ] += int(
            (
                ~file_group[
                    "Check_chromosome_and_strand"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "Protein_coordinate_failures"
        ] += int(
            (
                ~file_group[
                    "Check_protein_coordinates"
                ]
            ).sum()
        )


    # Write the complete sanity-check output incrementally.
    projected.to_csv(
        sanity_full_out,
        index=False,
        mode="a",
        header=not header_written_full
    )

    header_written_full = True


    # Write failed rows incrementally.
    failed = projected[
        projected[
            "Sanity_check_status"
        ]
        == "failed"
    ].copy()

    if not failed.empty:

        failed.to_csv(
            sanity_failed_out,
            index=False,
            mode="a",
            header=not header_written_failed
        )

        header_written_failed = True

        if len(first_failed_examples) < 20:

            number_remaining = (
                20
                - len(first_failed_examples)
            )

            first_failed_examples.append(
                failed.head(
                    number_remaining
                )
            )


    print(
        f"Chunk {chunk_number}: "
        f"read {len(chunk):,} rows | "
        f"translation-validated "
        f"{len(projected):,} | "
        f"sanity failed {len(failed):,}"
    )


# -----------------------------
# 5. Build and export summary table
# -----------------------------

if not header_written_full:

    raise ValueError(
        "No translation-validated projected peptide rows "
        "were available for sanity checking."
    )


sanity_summary = pd.DataFrame(
    summary_dict.values()
)


sanity_summary[
    "Percent_translation_validated"
] = (
    sanity_summary[
        "Rows_translation_validated"
    ]
    / sanity_summary[
        "Rows_from_step10_validation_table"
    ]
    * 100
).round(4)


sanity_summary[
    "Percent_passing_all_sanity_checks"
] = (
    sanity_summary[
        "Rows_passing_all_sanity_checks"
    ]
    / sanity_summary[
        "Translation_validated_rows_checked"
    ]
    * 100
).round(4)


sanity_summary.to_csv(
    sanity_summary_out,
    index=False
)


# Build a small failed-row preview for display.
if len(first_failed_examples) > 0:

    sanity_failed_preview = (
        pd.concat(
            first_failed_examples,
            ignore_index=True
        )
        .head(20)
    )

else:

    sanity_failed_preview = pd.DataFrame()


# -----------------------------
# 6. Overall summary
# -----------------------------

overall_checked = int(
    sanity_summary[
        "Translation_validated_rows_checked"
    ].sum()
)

overall_passed = int(
    sanity_summary[
        "Rows_passing_all_sanity_checks"
    ].sum()
)

overall_failed = int(
    sanity_summary[
        "Rows_failing_any_sanity_check"
    ].sum()
)

overall_pass_percent = (
    round(
        overall_passed
        / overall_checked
        * 100,
        4
    )
    if overall_checked > 0
    else pd.NA
)


print(
    "\n===== STEP 11 SANITY CHECK SUMMARY ====="
)

print(
    "Rows read from Step 10 validation table: "
    f"{total_rows_read:,}"
)

print(
    "Rows excluded by translation validation: "
    f"{total_translation_excluded:,}"
)

print(
    "Translation-validated rows checked: "
    f"{overall_checked:,}"
)

print(
    "Rows passing all sanity checks: "
    f"{overall_passed:,}"
)

print(
    "Rows failing at least one sanity check: "
    f"{overall_failed:,}"
)

print(
    "Overall sanity-check pass rate among "
    "translation-validated rows: "
    f"{overall_pass_percent}%"
)

print(
    f"\nFull sanity-check table saved: "
    f"{sanity_full_out}"
)

if sanity_failed_out.exists():

    print(
        f"Failed-row diagnostic table saved: "
        f"{sanity_failed_out}"
    )

else:

    print(
        "No failed-row diagnostic table was created "
        "because all rows passed."
    )

print(
    f"Source–tissue sanity summary saved: "
    f"{sanity_summary_out}"
)


display(
    sanity_summary
)

if not sanity_failed_preview.empty:

    display(
        sanity_failed_preview
    )

else:

    print(
        "\nNo failed sanity-check rows to display."
    )