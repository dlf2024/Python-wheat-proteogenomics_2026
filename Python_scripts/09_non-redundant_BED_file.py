# ============================================================
# Step 13 — Create non-redundant combined validated BED tracks
# Translation-validated + sanity-check-passed projections only
# Uses SQLite for memory-safe aggregation
# ============================================================

import pandas as pd
import sqlite3
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
bed_dir = Path("python_outputs/bed_validated")

bed_dir.mkdir(parents=True, exist_ok=True)
tables_dir.mkdir(parents=True, exist_ok=True)

# Step 11 output: translation-validated rows with sanity-check results
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

combined_table_out = tables_dir / "wheat_all_tissues_nonredundant_validated_peptides.csv"
combined_bed6_out = bed_dir / "wheat_all_tissues_nonredundant_validated_peptides.bed6"
combined_bed12_out = bed_dir / "wheat_all_tissues_nonredundant_validated_peptides.bed12"
step13_summary_out = tables_dir / "wheat_combined_validated_bed_summary_step13.csv"

sqlite_db = tables_dir / "wheat_step13_validated_nonredundant.sqlite"

chunk_size = 100_000

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )

# Clear previous outputs if rerunning
for path in [
    combined_table_out,
    combined_bed6_out,
    combined_bed12_out,
    step13_summary_out,
    sqlite_db
]:
    if path.exists():
        path.unlink()


# -----------------------------
# 2. Helper functions
# -----------------------------
def clean_bed_name(value):
    return (
        str(value)
        .replace(" ", "_")
        .replace(";", "|")
        .replace(",", "|")
        .replace("\t", "_")
        .replace("\n", "_")
    )


def make_bed_score(data):
    """
    Create BED score between 0 and 1000.
    """
    if "Probability" in data.columns:
        score = pd.to_numeric(data["Probability"], errors="coerce") * 1000
        score = score.fillna(1000).clip(0, 1000).round().astype(int)
    else:
        score = pd.Series([1000] * len(data), index=data.index)

    return score


# -----------------------------
# 3. Inspect Step 11 columns
# -----------------------------
header = pd.read_csv(sanity_file, nrows=0)

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
    "Sanity_check_status"
]

missing_required = [
    col for col in required_cols
    if col not in header.columns
]

if missing_required:
    raise KeyError(
        f"Missing required Step 11 column(s): {missing_required}"
    )

# Use best available gene/model label
if "GeneModel" in header.columns:
    gene_label_col = "GeneModel"
elif "GeneID" in header.columns:
    gene_label_col = "GeneID"
else:
    gene_label_col = None

# Use best available peptide display label
if "Peptide_intron_gapped_compact" in header.columns:
    peptide_label_col = "Peptide_intron_gapped_compact"
elif "Peptide_intron_gapped" in header.columns:
    peptide_label_col = "Peptide_intron_gapped"
else:
    peptide_label_col = "Peptide"

optional_cols = []

if "Probability" in header.columns:
    optional_cols.append("Probability")

if gene_label_col is not None:
    optional_cols.append(gene_label_col)

if peptide_label_col not in required_cols:
    optional_cols.append(peptide_label_col)

usecols = list(dict.fromkeys(required_cols + optional_cols))

print("Step 13 input file:")
print(sanity_file)
print(f"Using gene/model label column: {gene_label_col}")
print(f"Using peptide label column: {peptide_label_col}")


# -----------------------------
# 4. Load sanity-passed rows into SQLite
# -----------------------------
conn = sqlite3.connect(sqlite_db)

total_rows_read = 0
total_rows_passed = 0

print("\nLoading sanity-passed rows into SQLite...")

for chunk_i, chunk in enumerate(
    pd.read_csv(
        sanity_file,
        usecols=usecols,
        chunksize=chunk_size,
        low_memory=False
    ),
    start=1
):

    total_rows_read += len(chunk)

    # Keep only rows passing both validation layers:
    # Step 10 translation validation + Step 11 sanity checks
    chunk = chunk[
        chunk["Sanity_check_status"].astype(str) == "passed"
    ].copy()

    if chunk.empty:
        print(f"Chunk {chunk_i}: read {chunk_size:,} rows | no passed rows")
        continue

    total_rows_passed += len(chunk)

    # Standardise fields used downstream
    if gene_label_col is None:
        chunk["Gene_label"] = "NA"
    else:
        chunk["Gene_label"] = chunk[gene_label_col].astype(str)

    chunk["Peptide_label"] = chunk[peptide_label_col].astype(str)

    chunk["BED_score"] = make_bed_score(chunk)

    # Keep only columns needed for non-redundant aggregation
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

    chunk = chunk[insert_cols].copy()

    # SQLite is happier with simple string/int/float fields
    for col in [
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
    ]:
        chunk[col] = chunk[col].astype(str)

    numeric_cols = [
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_block_count",
        "BED_score"
    ]

    for col in numeric_cols:
        chunk[col] = pd.to_numeric(chunk[col], errors="coerce")

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
        f"Chunk {chunk_i}: cumulative rows read {total_rows_read:,} | "
        f"cumulative sanity-passed rows loaded {total_rows_passed:,}"
    )

if total_rows_passed == 0:
    conn.close()
    raise ValueError(
        "No sanity-passed rows were found in the Step 11 output."
    )


# -----------------------------
# 5. Create indexes to speed up grouping
# -----------------------------
print("\nCreating SQLite indexes...")

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

conn.commit()


# -----------------------------
# 6. Build non-redundant table in SQLite
# -----------------------------
print("\nBuilding non-redundant validated feature table...")

conn.execute("DROP TABLE IF EXISTS nonredundant_validated_peptides")

conn.execute("""
CREATE TABLE nonredundant_validated_peptides AS
SELECT
    Chromosome,
    CAST(BED_start_0based AS INTEGER) AS BED_start_0based,
    CAST(BED_end_0based_exclusive AS INTEGER) AS BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    CAST(BED_block_count AS INTEGER) AS BED_block_count,
    BED_block_sizes,
    BED_block_starts,
    GROUP_CONCAT(DISTINCT Source) AS Sources,
    GROUP_CONCAT(DISTINCT Tissue) AS Tissues,
    COUNT(DISTINCT Tissue) AS Tissue_count,
    COUNT(*) AS Observation_count,
    MAX(CAST(BED_score AS INTEGER)) AS Max_BED_score
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
# 7. Export combined table and BED files in chunks
# -----------------------------
print("\nExporting combined non-redundant table and BED files...")

combined_header_written = False
bed6_header_written = False
bed12_header_written = False

total_nonredundant_rows = 0
unique_peptides = set()
unique_proteins = set()
unique_genes = set()
unique_chromosomes = set()
multi_block_count = 0
bed_labels_with_introns = 0

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

for chunk_i, nonredundant in enumerate(
    pd.read_sql_query(sql_query, conn, chunksize=chunk_size),
    start=1
):

    nonredundant.insert(
        0,
        "Index",
        range(total_nonredundant_rows + 1, total_nonredundant_rows + len(nonredundant) + 1)
    )

    nonredundant["BED_name"] = (
        nonredundant["Peptide_label"].astype(str) + "|" +
        nonredundant["ProteinID"].astype(str) + "|" +
        nonredundant["Gene_label"].astype(str) + "|" +
        "validated=translation+sanity" + "|" +
        "tissues=" + nonredundant["Tissue_count"].astype(str)
    )

    nonredundant["BED_name"] = nonredundant["BED_name"].apply(clean_bed_name)

    nonredundant["BED_start_0based"] = nonredundant["BED_start_0based"].astype(int)
    nonredundant["BED_end_0based_exclusive"] = nonredundant["BED_end_0based_exclusive"].astype(int)
    nonredundant["BED_block_count"] = nonredundant["BED_block_count"].astype(int)
    nonredundant["Max_BED_score"] = nonredundant["Max_BED_score"].astype(int)

    # Save combined table incrementally
    nonredundant.to_csv(
        combined_table_out,
        index=False,
        mode="a",
        header=not combined_header_written
    )

    combined_header_written = True

    # BED6
    bed6 = nonredundant[[
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_name",
        "Max_BED_score",
        "Strand"
    ]].copy()

    bed6.to_csv(
        combined_bed6_out,
        sep="\t",
        header=False,
        index=False,
        mode="a"
    )

    # BED12
    bed12 = pd.DataFrame({
        "chrom": nonredundant["Chromosome"],
        "chromStart": nonredundant["BED_start_0based"],
        "chromEnd": nonredundant["BED_end_0based_exclusive"],
        "name": nonredundant["BED_name"],
        "score": nonredundant["Max_BED_score"],
        "strand": nonredundant["Strand"],
        "thickStart": nonredundant["BED_start_0based"],
        "thickEnd": nonredundant["BED_end_0based_exclusive"],
        "itemRgb": "0",
        "blockCount": nonredundant["BED_block_count"],
        "blockSizes": nonredundant["BED_block_sizes"],
        "blockStarts": nonredundant["BED_block_starts"]
    })

    bed12.to_csv(
        combined_bed12_out,
        sep="\t",
        header=False,
        index=False,
        mode="a"
    )

    # Summary counters
    total_nonredundant_rows += len(nonredundant)

    unique_peptides.update(nonredundant["Peptide"].dropna().astype(str).unique())
    unique_proteins.update(nonredundant["ProteinID"].dropna().astype(str).unique())
    unique_genes.update(nonredundant["Gene_label"].dropna().astype(str).unique())
    unique_chromosomes.update(nonredundant["Chromosome"].dropna().astype(str).unique())

    multi_block_count += int((nonredundant["BED_block_count"] > 1).sum())

    bed_labels_with_introns += int(
        nonredundant["BED_name"]
        .astype(str)
        .str.contains("-", regex=False)
        .sum()
    )

    print(
        f"Export chunk {chunk_i}: cumulative non-redundant rows "
        f"{total_nonredundant_rows:,}"
    )


# -----------------------------
# 8. Summary table
# -----------------------------
step13_summary = pd.DataFrame([{
    "Validated_rows_before_deduplication": total_rows_passed,
    "Nonredundant_validated_rows": total_nonredundant_rows,
    "Redundant_validated_rows_removed": total_rows_passed - total_nonredundant_rows,
    "Unique_peptides": len(unique_peptides),
    "Unique_proteins": len(unique_proteins),
    "Unique_gene_models": len(unique_genes),
    "Unique_chromosomes": len(unique_chromosomes),
    "Multi_block_peptides": multi_block_count,
    "BED_labels_with_introns": bed_labels_with_introns,
    "Combined_table_file": combined_table_out.name,
    "BED6_file": combined_bed6_out.name,
    "BED12_file": combined_bed12_out.name,
    "SQLite_database": sqlite_db.name
}])

step13_summary.to_csv(step13_summary_out, index=False)

conn.close()

print("\n===== STEP 13 COMBINED VALIDATED BED SUMMARY =====")
print(f"Validated rows before deduplication: {total_rows_passed:,}")
print(f"Non-redundant validated rows: {total_nonredundant_rows:,}")
print(f"Redundant validated rows removed: {total_rows_passed - total_nonredundant_rows:,}")

print(f"\nCombined non-redundant table saved: {combined_table_out}")
print(f"Combined BED6 saved: {combined_bed6_out}")
print(f"Combined BED12 saved: {combined_bed12_out}")
print(f"Step 13 summary saved: {step13_summary_out}")
print(f"Temporary SQLite database saved: {sqlite_db}")

display(step13_summary)