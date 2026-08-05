# ============================================================
# Step 13 — Create non-redundant combined validated BED tracks
# Translation-validated + sanity-check-passed projections only
# Uses SQLite for memory-safe aggregation
# ============================================================

import sqlite3
from pathlib import Path

import pandas as pd


# -----------------------------
# 1. Input / output paths
# -----------------------------

tables_dir = Path("python_outputs/tables")
bed_dir = Path("python_outputs/bed_validated")

bed_dir.mkdir(
    parents=True,
    exist_ok=True
)

tables_dir.mkdir(
    parents=True,
    exist_ok=True
)


# Corrected Step 11 output:
# translation-validated rows with sanity-check results
sanity_file = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"
)


# Original complete non-redundant outputs
combined_table_out = (
    tables_dir
    / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv"
)

combined_bed6_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed6"
)

combined_bed12_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed12"
)


# New standalone ChrUnknown non-redundant tracks
chrunknown_bed6_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed6"
)

chrunknown_bed12_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed12"
)


# Original Step 13 summary and SQLite filenames
step13_summary_out = (
    tables_dir
    / "wheat_all_tissues_nonredundant_validated_bed_summary_step13.csv"
)

sqlite_db = (
    tables_dir
    / "wheat_validated_nonredundant_step13.sqlite"
)

chunk_size = 100_000


if not sanity_file.exists():

    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n"
        f"{sanity_file}\n\n"
        "Please run the corrected Step 11 first."
    )


# Overwrite previous Step 13 outputs.
for output_path in [
    combined_table_out,
    combined_bed6_out,
    combined_bed12_out,
    chrunknown_bed6_out,
    chrunknown_bed12_out,
    step13_summary_out,
    sqlite_db
]:

    if output_path.exists():
        output_path.unlink()


# -----------------------------
# 2. Helper functions
# -----------------------------

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
        .replace("\r", "_")
    )


def make_bed_score(data):
    """
    Create BED score between 0 and 1000.

    Priority:
    1. Probability scaled to 0–1000, when available
    2. Default score of 1000
    """

    if "Probability" in data.columns:

        score = (
            pd.to_numeric(
                data["Probability"],
                errors="coerce"
            )
            * 1000
        )

        score = (
            score
            .fillna(1000)
            .clip(0, 1000)
            .round()
            .astype(int)
        )

    else:

        score = pd.Series(
            1000,
            index=data.index,
            dtype="int64"
        )

    return score


def make_bed6(nonredundant):
    """
    Build BED6 DataFrame.
    """

    return pd.DataFrame({
        "chrom":
            nonredundant["Chromosome"],

        "chromStart":
            nonredundant["BED_start_0based"],

        "chromEnd":
            nonredundant["BED_end_0based_exclusive"],

        "name":
            nonredundant["BED_name"],

        "score":
            nonredundant["Max_BED_score"],

        "strand":
            nonredundant["Strand"]
    })


def make_bed12(nonredundant):
    """
    Build BED12 DataFrame.
    """

    return pd.DataFrame({
        "chrom":
            nonredundant["Chromosome"],

        "chromStart":
            nonredundant["BED_start_0based"],

        "chromEnd":
            nonredundant["BED_end_0based_exclusive"],

        "name":
            nonredundant["BED_name"],

        "score":
            nonredundant["Max_BED_score"],

        "strand":
            nonredundant["Strand"],

        "thickStart":
            nonredundant["BED_start_0based"],

        "thickEnd":
            nonredundant["BED_end_0based_exclusive"],

        "itemRgb":
            "0",

        "blockCount":
            nonredundant["BED_block_count"],

        "blockSizes":
            nonredundant["BED_block_sizes"],

        "blockStarts":
            nonredundant["BED_block_starts"]
    })


# -----------------------------
# 3. Inspect corrected Step 11 columns
# -----------------------------

header = pd.read_csv(
    sanity_file,
    nrows=0
)

required_cols = [
    "Chromosome",
    "BED_start_0based",
    "BED_end_0based_exclusive",
    "Strand",
    "Peptide",
    "ProteinID",
    "BED_block_count",
    "BED_block_sizes",
    "BED_block_starts",
    "Source",
    "Tissue",
    "Sanity_check_status",
    "All_sanity_checks_passed",
    "Check_chromosome_and_strand"
]

missing_required = [
    column
    for column in required_cols
    if column not in header.columns
]

if missing_required:

    raise KeyError(
        "Missing required corrected Step 11 column(s): "
        f"{missing_required}"
    )


# Best available gene/model label
if "GeneModel" in header.columns:

    gene_label_col = "GeneModel"

elif "GeneID" in header.columns:

    gene_label_col = "GeneID"

else:

    gene_label_col = None


# Best available peptide display label
if "Peptide_intron_gapped" in header.columns:

    peptide_label_col = "Peptide_intron_gapped"

elif "Peptide_intron_gapped_compact" in header.columns:

    peptide_label_col = "Peptide_intron_gapped_compact"

else:

    peptide_label_col = "Peptide"


optional_cols = []

if "Probability" in header.columns:
    optional_cols.append("Probability")

if gene_label_col is not None:
    optional_cols.append(gene_label_col)

if peptide_label_col not in required_cols:
    optional_cols.append(peptide_label_col)


usecols = list(
    dict.fromkeys(
        required_cols
        + optional_cols
    )
)


print("Step 13 input file:")
print(f"  {sanity_file}")

print(
    "Using gene/model label column: "
    f"{gene_label_col}"
)

print(
    "Using peptide display column: "
    f"{peptide_label_col}"
)


# -----------------------------
# 4. Load sanity-passed rows into SQLite
# -----------------------------

conn = sqlite3.connect(
    sqlite_db
)

total_rows_read = 0
total_rows_passed = 0
total_chrunknown_rows_loaded = 0


print(
    "\nLoading corrected Step 11 sanity-passed rows "
    "into SQLite..."
)


for chunk_number, chunk in enumerate(

    pd.read_csv(
        sanity_file,
        usecols=usecols,
        chunksize=chunk_size,
        low_memory=False
    ),

    start=1
):

    rows_in_chunk = len(
        chunk
    )

    total_rows_read += rows_in_chunk


    # Retain only rows passing both validation layers.
    passed_mask = (
        chunk[
            "Sanity_check_status"
        ]
        .astype(str)
        .str.strip()
        .eq("passed")
        &
        chunk[
            "All_sanity_checks_passed"
        ]
        .fillna(False)
        .astype(bool)
    )

    chunk = chunk[
        passed_mask
    ].copy()


    if chunk.empty:

        print(
            f"Chunk {chunk_number}: "
            f"read {rows_in_chunk:,} rows | "
            "no passed rows"
        )

        continue


    total_rows_passed += len(
        chunk
    )


    # Standardise core text fields.
    chunk["Chromosome"] = (
        chunk["Chromosome"]
        .astype(str)
        .str.strip()
    )

    chunk["Strand"] = (
        chunk["Strand"]
        .astype(str)
        .str.strip()
    )


    total_chrunknown_rows_loaded += int(
        chunk[
            "Chromosome"
        ]
        .eq("ChrUnknown")
        .sum()
    )


    if gene_label_col is None:

        chunk["Gene_label"] = "NA"

    else:

        chunk["Gene_label"] = (
            chunk[
                gene_label_col
            ]
            .fillna("NA")
            .astype(str)
        )


    chunk["Peptide_label"] = (
        chunk[
            peptide_label_col
        ]
        .fillna(
            chunk["Peptide"]
        )
        .astype(str)
    )


    chunk["BED_score"] = (
        make_bed_score(
            chunk
        )
    )


    # Retain only fields required for nonredundant aggregation.
    insert_cols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "Strand",
        "Peptide",
        "Peptide_label",
        "ProteinID",
        "Gene_label",
        "BED_block_count",
        "BED_block_sizes",
        "BED_block_starts",
        "Source",
        "Tissue",
        "BED_score"
    ]

    chunk = chunk[
        insert_cols
    ].copy()


    text_cols = [
        "Chromosome",
        "Strand",
        "Peptide",
        "Peptide_label",
        "ProteinID",
        "Gene_label",
        "BED_block_sizes",
        "BED_block_starts",
        "Source",
        "Tissue"
    ]

    for column in text_cols:

        chunk[column] = (
            chunk[column]
            .astype(str)
        )


    numeric_cols = [
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_block_count",
        "BED_score"
    ]

    for column in numeric_cols:

        chunk[column] = pd.to_numeric(
            chunk[column],
            errors="coerce"
        )


    chunk = chunk.dropna(
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


    chunk.to_sql(
        "validated_projection_rows",
        conn,
        if_exists="append",
        index=False
    )


    print(
        f"Chunk {chunk_number}: "
        f"cumulative rows read {total_rows_read:,} | "
        f"passed rows loaded {total_rows_passed:,} | "
        f"ChrUnknown rows loaded "
        f"{total_chrunknown_rows_loaded:,}"
    )


if total_rows_passed == 0:

    conn.close()

    raise ValueError(
        "No sanity-passed rows were found in "
        "the corrected Step 11 output."
    )


if total_chrunknown_rows_loaded != 77_543:

    print(
        "\nWARNING: corrected Step 11 was expected to contain "
        "77,543 passed ChrUnknown rows, but "
        f"{total_chrunknown_rows_loaded:,} were loaded."
    )

else:

    print(
        "\nChrUnknown input check passed: "
        "77,543 validated rows loaded into SQLite."
    )


# -----------------------------
# 5. Create SQLite indexes
# -----------------------------

print(
    "\nCreating SQLite indexes..."
)


conn.execute("""
CREATE INDEX IF NOT EXISTS idx_validated_projection_dedup
ON validated_projection_rows (
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    BED_block_count,
    BED_block_sizes,
    BED_block_starts
)
""")


conn.execute("""
CREATE INDEX IF NOT EXISTS idx_validated_projection_chromosome
ON validated_projection_rows (
    Chromosome
)
""")


conn.commit()


# -----------------------------
# 6. Build complete nonredundant table
# -----------------------------

print(
    "\nBuilding complete nonredundant validated "
    "feature table..."
)


conn.execute(
    "DROP TABLE IF EXISTS "
    "nonredundant_validated_peptides"
)


conn.execute("""
CREATE TABLE nonredundant_validated_peptides AS
SELECT
    Chromosome,
    CAST(BED_start_0based AS INTEGER)
        AS BED_start_0based,
    CAST(BED_end_0based_exclusive AS INTEGER)
        AS BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    CAST(BED_block_count AS INTEGER)
        AS BED_block_count,
    BED_block_sizes,
    BED_block_starts,
    GROUP_CONCAT(DISTINCT Source)
        AS Sources,
    GROUP_CONCAT(DISTINCT Tissue)
        AS Tissues,
    COUNT(DISTINCT Source || '|' || Tissue)
        AS Source_tissue_count,
    COUNT(DISTINCT Tissue)
        AS Tissue_count,
    COUNT(*)
        AS Observation_count,
    MAX(CAST(BED_score AS INTEGER))
        AS Max_BED_score
FROM validated_projection_rows
GROUP BY
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    BED_block_count,
    BED_block_sizes,
    BED_block_starts
""")


conn.commit()


# -----------------------------
# 7. Export complete table and both track sets
# -----------------------------

print(
    "\nExporting complete nonredundant table, "
    "complete BED tracks and ChrUnknown-only BED tracks..."
)


combined_header_written = False

total_nonredundant_rows = 0
total_chrunknown_nonredundant_rows = 0

unique_peptides = set()
unique_proteins = set()
unique_genes = set()
unique_sequence_ids = set()

chrunknown_unique_peptides = set()
chrunknown_unique_proteins = set()
chrunknown_unique_genes = set()

multi_block_count = 0
within_exon_count = 0
bed_labels_with_introns = 0

chrunknown_multi_block_count = 0
chrunknown_within_exon_count = 0


sql_query = """
SELECT
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    BED_block_count,
    BED_block_sizes,
    BED_block_starts,
    Sources,
    Tissues,
    Source_tissue_count,
    Tissue_count,
    Observation_count,
    Max_BED_score
FROM nonredundant_validated_peptides
ORDER BY
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    ProteinID
"""


for chunk_number, nonredundant in enumerate(

    pd.read_sql_query(
        sql_query,
        conn,
        chunksize=chunk_size
    ),

    start=1
):

    number_rows = len(
        nonredundant
    )


    nonredundant.insert(
        0,
        "Index",
        range(
            total_nonredundant_rows + 1,
            total_nonredundant_rows + number_rows + 1
        )
    )


    nonredundant["BED_name"] = (
        nonredundant[
            "Peptide_label"
        ].astype(str)
        + "|"
        + nonredundant[
            "ProteinID"
        ].astype(str)
        + "|"
        + nonredundant[
            "Gene_label"
        ].astype(str)
        + "|validated=translation+sanity"
        + "|source_tissues="
        + nonredundant[
            "Source_tissue_count"
        ].astype(str)
    )


    nonredundant["BED_name"] = (
        nonredundant[
            "BED_name"
        ]
        .apply(
            clean_bed_name
        )
    )


    integer_columns = [
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_block_count",
        "Source_tissue_count",
        "Tissue_count",
        "Observation_count",
        "Max_BED_score"
    ]

    for column in integer_columns:

        nonredundant[column] = (
            pd.to_numeric(
                nonredundant[column],
                errors="raise"
            )
            .astype(int)
        )


    # -----------------------------------------
    # Complete nonredundant CSV table
    # -----------------------------------------

    nonredundant.to_csv(
        combined_table_out,
        index=False,
        mode="a",
        header=not combined_header_written
    )

    combined_header_written = True


    # -----------------------------------------
    # Complete nonredundant BED6/BED12 tracks
    # -----------------------------------------

    complete_bed6 = make_bed6(
        nonredundant
    )

    complete_bed12 = make_bed12(
        nonredundant
    )


    complete_bed6.to_csv(
        combined_bed6_out,
        sep="\t",
        header=False,
        index=False,
        mode="a"
    )


    complete_bed12.to_csv(
        combined_bed12_out,
        sep="\t",
        header=False,
        index=False,
        mode="a"
    )


    # -----------------------------------------
    # Standalone nonredundant ChrUnknown tracks
    # -----------------------------------------

    chrunknown = nonredundant[
        nonredundant[
            "Chromosome"
        ]
        .astype(str)
        .str.strip()
        .eq("ChrUnknown")
    ].copy()


    if not chrunknown.empty:

        chrunknown_bed6 = make_bed6(
            chrunknown
        )

        chrunknown_bed12 = make_bed12(
            chrunknown
        )


        chrunknown_bed6.to_csv(
            chrunknown_bed6_out,
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )


        chrunknown_bed12.to_csv(
            chrunknown_bed12_out,
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )


        total_chrunknown_nonredundant_rows += len(
            chrunknown
        )


        chrunknown_unique_peptides.update(
            chrunknown[
                "Peptide"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


        chrunknown_unique_proteins.update(
            chrunknown[
                "ProteinID"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


        chrunknown_unique_genes.update(
            chrunknown[
                "Gene_label"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


        chrunknown_multi_block_count += int(
            (
                chrunknown[
                    "BED_block_count"
                ]
                > 1
            ).sum()
        )


        chrunknown_within_exon_count += int(
            (
                chrunknown[
                    "BED_block_count"
                ]
                == 1
            ).sum()
        )


    # -----------------------------------------
    # Overall summary counters
    # -----------------------------------------

    total_nonredundant_rows += number_rows


    unique_peptides.update(
        nonredundant[
            "Peptide"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    unique_proteins.update(
        nonredundant[
            "ProteinID"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    unique_genes.update(
        nonredundant[
            "Gene_label"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    unique_sequence_ids.update(
        nonredundant[
            "Chromosome"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    multi_block_count += int(
        (
            nonredundant[
                "BED_block_count"
            ]
            > 1
        ).sum()
    )


    within_exon_count += int(
        (
            nonredundant[
                "BED_block_count"
            ]
            == 1
        ).sum()
    )


    bed_labels_with_introns += int(
        nonredundant[
            "BED_name"
        ]
        .astype(str)
        .str.contains(
            "-",
            regex=False
        )
        .sum()
    )


    print(
        f"Export chunk {chunk_number}: "
        f"cumulative complete nonredundant rows "
        f"{total_nonredundant_rows:,} | "
        f"ChrUnknown nonredundant rows "
        f"{total_chrunknown_nonredundant_rows:,}"
    )


# -----------------------------
# 8. Integrity checks
# -----------------------------

if not combined_header_written:

    conn.close()

    raise ValueError(
        "No complete nonredundant rows were exported."
    )


if not chrunknown_bed6_out.exists():

    conn.close()

    raise ValueError(
        "No ChrUnknown BED6 track was created. "
        "Check the corrected Step 11 input."
    )


if not chrunknown_bed12_out.exists():

    conn.close()

    raise ValueError(
        "No ChrUnknown BED12 track was created. "
        "Check the corrected Step 11 input."
    )


# Confirm SQLite count agrees with exported ChrUnknown count.
sqlite_chrunknown_count = conn.execute("""
SELECT COUNT(*)
FROM nonredundant_validated_peptides
WHERE Chromosome = 'ChrUnknown'
""").fetchone()[0]


if (
    sqlite_chrunknown_count
    != total_chrunknown_nonredundant_rows
):

    conn.close()

    raise ValueError(
        "ChrUnknown nonredundant row-count mismatch:\n"
        f"SQLite rows: "
        f"{sqlite_chrunknown_count:,}\n"
        f"Exported rows: "
        f"{total_chrunknown_nonredundant_rows:,}"
    )


# -----------------------------
# 9. Summary table
# -----------------------------

step13_summary = pd.DataFrame([{

    "Validated_rows_before_deduplication":
        total_rows_passed,

    "Nonredundant_validated_rows":
        total_nonredundant_rows,

    "Redundant_validated_rows_removed":
        (
            total_rows_passed
            - total_nonredundant_rows
        ),

    "Unique_peptides":
        len(
            unique_peptides
        ),

    "Unique_proteins":
        len(
            unique_proteins
        ),

    "Unique_gene_models":
        len(
            unique_genes
        ),

    # Retain original summary column name for compatibility.
    # This now includes the 21 chromosomes plus ChrUnknown.
    "Unique_chromosomes":
        len(
            unique_sequence_ids
        ),

    "Multi_block_peptides":
        multi_block_count,

    "Within_exon_peptides":
        within_exon_count,

    "BED_labels_with_introns":
        bed_labels_with_introns,

    "ChrUnknown_validated_rows_before_deduplication":
        total_chrunknown_rows_loaded,

    "ChrUnknown_nonredundant_validated_rows":
        total_chrunknown_nonredundant_rows,

    "ChrUnknown_redundant_rows_removed":
        (
            total_chrunknown_rows_loaded
            - total_chrunknown_nonredundant_rows
        ),

    "ChrUnknown_unique_peptides":
        len(
            chrunknown_unique_peptides
        ),

    "ChrUnknown_unique_proteins":
        len(
            chrunknown_unique_proteins
        ),

    "ChrUnknown_unique_gene_models":
        len(
            chrunknown_unique_genes
        ),

    "ChrUnknown_multi_block_peptides":
        chrunknown_multi_block_count,

    "ChrUnknown_within_exon_peptides":
        chrunknown_within_exon_count,

    "Combined_table_file":
        combined_table_out.name,

    "BED6_file":
        combined_bed6_out.name,

    "BED12_file":
        combined_bed12_out.name,

    "ChrUnknown_BED6_file":
        chrunknown_bed6_out.name,

    "ChrUnknown_BED12_file":
        chrunknown_bed12_out.name,

    "SQLite_database":
        sqlite_db.name
}])


step13_summary.to_csv(
    step13_summary_out,
    index=False
)


conn.close()


# -----------------------------
# 10. Final summary
# -----------------------------

print(
    "\n===== STEP 13 COMBINED VALIDATED BED SUMMARY ====="
)

print(
    "Validated rows before deduplication: "
    f"{total_rows_passed:,}"
)

print(
    "Complete nonredundant validated rows: "
    f"{total_nonredundant_rows:,}"
)

print(
    "Redundant validated rows removed: "
    f"{total_rows_passed - total_nonredundant_rows:,}"
)

print(
    "Sequence identifiers represented: "
    f"{len(unique_sequence_ids):,}"
)

print(
    "\n===== ChrUnknown NONREDUNDANT TRACK ====="
)

print(
    "ChrUnknown validated rows before deduplication: "
    f"{total_chrunknown_rows_loaded:,}"
)

print(
    "ChrUnknown nonredundant validated rows: "
    f"{total_chrunknown_nonredundant_rows:,}"
)

print(
    "ChrUnknown redundant rows removed: "
    f"{total_chrunknown_rows_loaded - total_chrunknown_nonredundant_rows:,}"
)

print(
    "ChrUnknown unique peptide sequences: "
    f"{len(chrunknown_unique_peptides):,}"
)

print(
    "ChrUnknown unique protein accessions: "
    f"{len(chrunknown_unique_proteins):,}"
)

print(
    "ChrUnknown unique gene models: "
    f"{len(chrunknown_unique_genes):,}"
)

print(
    "\nComplete nonredundant table saved:"
    f"\n  {combined_table_out}"
)

print(
    "Complete combined BED6 saved:"
    f"\n  {combined_bed6_out}"
)

print(
    "Complete combined BED12 saved:"
    f"\n  {combined_bed12_out}"
)

print(
    "Standalone ChrUnknown BED6 saved:"
    f"\n  {chrunknown_bed6_out}"
)

print(
    "Standalone ChrUnknown BED12 saved:"
    f"\n  {chrunknown_bed12_out}"
)

print(
    "Step 13 summary saved:"
    f"\n  {step13_summary_out}"
)

print(
    "SQLite database saved:"
    f"\n  {sqlite_db}"
)


display(
    step13_summary
)