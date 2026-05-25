# ============================================================
# Step 26 — Generate sanity-validated BED files for Apollo/JBrowse upload
# Memory-light version using failed-row exclusion
# ============================================================

import pandas as pd
from pathlib import Path
import re

# -----------------------------
# 1. Input / output paths
# -----------------------------
bed_apollo_dir = Path("python_outputs/bed_Apollo")
validated_bed_dir = Path("python_outputs/bed_Apollo_validated")
tables_dir = Path("python_outputs/tables")

validated_bed_dir.mkdir(parents=True, exist_ok=True)

sanity_failed_file = tables_dir / "wheat_projection_sanity_checks_failed_rows_step25.csv"

summary_out = tables_dir / "wheat_validated_bed_filtering_summary_step26.csv"

# -----------------------------
# 2. Helper functions
# -----------------------------
def clean_peptide_from_bed_name(name):
    name = str(name)
    peptide = name.split("|")[0]
    peptide = peptide.replace("-", "")
    peptide = re.sub(r"[^A-Z]", "", peptide.upper())
    peptide = peptide.replace("I", "L")
    return peptide


def make_key(chrom, start, end, strand, peptide):
    return (
        chrom.astype(str) + "|" +
        start.astype(str) + "|" +
        end.astype(str) + "|" +
        strand.astype(str) + "|" +
        peptide.astype(str)
    )


# -----------------------------
# 3. Build failed-key set from Step 25 failed rows only
# -----------------------------
failed_keys = set()

if sanity_failed_file.exists():

    failed_usecols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "Strand",
        "Peptide"
    ]

    for chunk in pd.read_csv(
        sanity_failed_file,
        usecols=lambda col: col in failed_usecols,
        chunksize=100_000,
        low_memory=True
    ):

        chunk = chunk.dropna(
            subset=[
                "Chromosome",
                "BED_start_0based",
                "BED_end_0based_exclusive",
                "Strand",
                "Peptide"
            ]
        ).copy()

        chunk["BED_start_0based"] = pd.to_numeric(
            chunk["BED_start_0based"],
            errors="coerce"
        )

        chunk["BED_end_0based_exclusive"] = pd.to_numeric(
            chunk["BED_end_0based_exclusive"],
            errors="coerce"
        )

        chunk = chunk.dropna(
            subset=["BED_start_0based", "BED_end_0based_exclusive"]
        ).copy()

        chunk["BED_start_0based"] = chunk["BED_start_0based"].astype(int)
        chunk["BED_end_0based_exclusive"] = chunk["BED_end_0based_exclusive"].astype(int)

        chunk["peptide_clean"] = (
            chunk["Peptide"]
            .astype(str)
            .str.replace("-", "", regex=False)
            .str.upper()
            .str.replace("I", "L", regex=False)
        )

        keys = make_key(
            chunk["Chromosome"],
            chunk["BED_start_0based"],
            chunk["BED_end_0based_exclusive"],
            chunk["Strand"],
            chunk["peptide_clean"]
        )

        failed_keys.update(keys.tolist())

else:
    print(f"No failed-row file found: {sanity_failed_file}")
    print("Proceeding with no failed keys.")

print(f"Failed projection keys loaded: {len(failed_keys):,}")

# -----------------------------
# 4. Find Apollo BED files without duplicates
# -----------------------------
bed_extensions = {".bed", ".bed6", ".bed12"}

bed_files = sorted({
    path.resolve()
    for path in bed_apollo_dir.iterdir()
    if path.is_file() and path.suffix.lower() in bed_extensions
})

bed_files = [Path(path) for path in bed_files]

if len(bed_files) == 0:
    raise FileNotFoundError(
        f"No BED files found in {bed_apollo_dir}. "
        "Check the Apollo BED output folder name."
    )

print(f"Unique BED files found: {len(bed_files)}")

# -----------------------------
# 5. Filter BED files in chunks
# -----------------------------
summary_records = []

for bed_file in bed_files:

    print(f"\nFiltering: {bed_file.name}")

    output_file = validated_bed_dir / bed_file.name

    # Clear existing output if rerunning
    if output_file.exists():
        output_file.unlink()

    original_rows_total = 0
    retained_rows_total = 0
    removed_rows_total = 0

    chunk_iter = pd.read_csv(
        bed_file,
        sep="\t",
        header=None,
        comment="#",
        dtype=str,
        chunksize=100_000,
        low_memory=True
    )

    for chunk_i, chunk in enumerate(chunk_iter, start=1):

        original_rows_total += len(chunk)

        if chunk.shape[1] < 6:
            print(f"Skipped chunk {chunk_i}: fewer than 6 BED columns.")
            continue

        chunk = chunk.rename(columns={
            0: "chrom",
            1: "start",
            2: "end",
            3: "name",
            4: "score",
            5: "strand"
        })

        chunk["start"] = pd.to_numeric(chunk["start"], errors="coerce")
        chunk["end"] = pd.to_numeric(chunk["end"], errors="coerce")

        chunk = chunk.dropna(
            subset=["chrom", "start", "end", "name", "strand"]
        ).copy()

        chunk["start"] = chunk["start"].astype(int)
        chunk["end"] = chunk["end"].astype(int)

        chunk["peptide_clean"] = chunk["name"].apply(clean_peptide_from_bed_name)

        chunk["validation_key"] = make_key(
            chunk["chrom"],
            chunk["start"],
            chunk["end"],
            chunk["strand"],
            chunk["peptide_clean"]
        )

        filtered = chunk[
            ~chunk["validation_key"].isin(failed_keys)
        ].copy()

        retained_rows_total += len(filtered)
        removed_rows_total += len(chunk) - len(filtered)

        filtered = filtered.drop(columns=["peptide_clean", "validation_key"])

        filtered = filtered.rename(columns={
            "chrom": 0,
            "start": 1,
            "end": 2,
            "name": 3,
            "score": 4,
            "strand": 5
        })

        filtered.to_csv(
            output_file,
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )

    summary_records.append({
        "Input_BED_file": bed_file.name,
        "Original_rows": original_rows_total,
        "Retained_validated_rows": retained_rows_total,
        "Removed_failed_rows": removed_rows_total,
        "Percent_retained": round(
            (retained_rows_total / original_rows_total) * 100,
            4
        ) if original_rows_total > 0 else 0,
        "Output_BED_file": output_file.name
    })

    print(f"Original rows: {original_rows_total:,}")
    print(f"Retained rows: {retained_rows_total:,}")
    print(f"Removed failed rows: {removed_rows_total:,}")
    print(f"Saved: {output_file}")

# -----------------------------
# 6. Save summary
# -----------------------------
summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print("\n===== STEP 26 BED FILTERING SUMMARY =====")
print(f"BED files processed: {len(summary):,}")
print(f"Total original rows: {summary['Original_rows'].sum():,}")
print(f"Total retained rows: {summary['Retained_validated_rows'].sum():,}")
print(f"Total removed rows: {summary['Removed_failed_rows'].sum():,}")

print(f"\nValidated BED files saved in: {validated_bed_dir}")
print(f"Filtering summary saved: {summary_out}")

display(summary)