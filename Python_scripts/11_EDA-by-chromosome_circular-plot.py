# ============================================================
# Step 22 — EDA: Circular plot of tissue-level validated peptide genome map
# Fully validated rows only
# Translation-validated + sanity-check-passed mapped peptide projections
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict
from pycirclize import Circos

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

# Step 11 output: translation-validated rows with sanity-check status
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

figure_out = figures_dir / "step22_circos_tissue_validated_peptide_tracks.png"
summary_out = tables_dir / "wheat_circos_tissue_validated_peptide_summary_step22.csv"

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )

if not gff3_features_file.exists():
    raise FileNotFoundError(
        f"GFF3 parsed features file not found:\n{gff3_features_file}"
    )

# -----------------------------
# 2. Parameters
# -----------------------------
chrom_order = [
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D"
]

max_points_per_tissue_chrom = 400
chunksize = 100_000

# -----------------------------
# 3. Helper functions
# -----------------------------
def normalise_chromosome_name(value):
    value = str(value).strip()

    if value.lower() in ["chrunknown", "unknown", "nan"]:
        return "ChrUnknown"

    if value.startswith("Chr"):
        return value

    return "Chr" + value


def clean_tissue_label(value):
    return (
        str(value)
        .replace("-", "_")
        .replace(" ", "_")
        .replace("/", "_")
    )


def source_rank(source):
    """
    Track order from innermost to outermost.

    Desired visual order:
    1. MSV... innermost
    2. PXD004720 / other PXD intermediate
    3. PXD050500 outermost
    """

    source = str(source)

    if source.startswith("MSV"):
        return 0

    if source == "PXD004720":
        return 1

    if source == "PXD050500":
        return 2

    if source.startswith("PXD"):
        return 3

    return 99


def source_tissue_sort_key(source_tissue):
    """
    Sort Source_Tissue labels so that MSV tracks are innermost and
    PXD050500 tracks are outermost.
    """

    source = str(source_tissue).split("_", 1)[0]
    tissue = str(source_tissue).split("_", 1)[1] if "_" in str(source_tissue) else ""

    return (source_rank(source), source, tissue)


# -----------------------------
# 4. Estimate chromosome lengths from GFF3 annotation
# -----------------------------
chrom_lengths = {}

for chunk in pd.read_csv(
    gff3_features_file,
    usecols=lambda col: col in ["SeqID", "End"],
    chunksize=chunksize,
    low_memory=False
):

    chunk["SeqID"] = chunk["SeqID"].apply(normalise_chromosome_name)
    chunk["End"] = pd.to_numeric(chunk["End"], errors="coerce")

    chunk = chunk.dropna(subset=["SeqID", "End"])

    for chrom, group in chunk.groupby("SeqID"):

        if chrom in chrom_order:

            max_end = int(group["End"].max())
            chrom_lengths[chrom] = max(max_end, chrom_lengths.get(chrom, 0))

chrom_lengths = {
    chrom: chrom_lengths[chrom]
    for chrom in chrom_order
    if chrom in chrom_lengths
}

print(f"Chromosomes loaded: {len(chrom_lengths)}")

if len(chrom_lengths) == 0:
    raise ValueError("No chromosome lengths were recovered from the GFF3 feature table.")

# -----------------------------
# 5. Sample validated mapped peptide positions by tissue and chromosome
# -----------------------------
print("\nSampling fully validated mapped peptide positions from Step 11...")

header = pd.read_csv(sanity_file, nrows=0)

required_cols = [
    "Source",
    "Tissue",
    "Chromosome",
    "BED_start_0based",
    "Sanity_check_status"
]

missing_cols = [
    col for col in required_cols
    if col not in header.columns
]

if missing_cols:
    raise KeyError(
        f"Missing required column(s) in Step 11 sanity-check table: {missing_cols}"
    )

tissue_positions = defaultdict(lambda: defaultdict(list))
chrom_counts = defaultdict(lambda: defaultdict(int))

total_rows_read = 0
total_validated_rows_used = 0

for chunk_i, chunk in enumerate(
    pd.read_csv(
        sanity_file,
        usecols=required_cols,
        chunksize=chunksize,
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
        print(
            f"Chunk {chunk_i}: read {chunksize:,} rows | "
            f"no validated rows"
        )
        continue

    chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

    chunk = chunk[
        chunk["Chromosome"].isin(chrom_order)
    ].copy()

    chunk["BED_start_0based"] = pd.to_numeric(
        chunk["BED_start_0based"],
        errors="coerce"
    )

    chunk = chunk.dropna(
        subset=[
            "Source",
            "Tissue",
            "Chromosome",
            "BED_start_0based"
        ]
    ).copy()

    if chunk.empty:
        continue

    total_validated_rows_used += len(chunk)

    chunk["Tissue_clean"] = chunk["Tissue"].apply(clean_tissue_label)

    chunk["Source_Tissue"] = (
        chunk["Source"].astype(str) + "_" +
        chunk["Tissue_clean"].astype(str)
    )

    for (source_tissue, chrom), group in chunk.groupby(["Source_Tissue", "Chromosome"]):

        chrom_counts[source_tissue][chrom] += len(group)

        # Sample a small number per chunk to avoid memory overload
        n_sample = min(50, len(group))

        tissue_positions[source_tissue][chrom].extend(
            group["BED_start_0based"]
            .sample(n=n_sample, random_state=42 + chunk_i)
            .astype(int)
            .tolist()
        )

    print(
        f"Chunk {chunk_i}: retained {len(chunk):,} validated mapped rows | "
        f"cumulative validated rows used {total_validated_rows_used:,}"
    )

# -----------------------------
# 6. Final cap per tissue/chromosome and summary table
# -----------------------------
source_tissues = sorted(
    list(tissue_positions.keys()),
    key=source_tissue_sort_key
)

if len(source_tissues) == 0:
    raise ValueError(
        "No validated mapped peptide positions were available for Circos plotting."
    )

summary_records = []

for source_tissue in source_tissues:

    source = source_tissue.split("_", 1)[0]
    tissue = source_tissue.split("_", 1)[1] if "_" in source_tissue else source_tissue

    for chrom in chrom_order:

        positions = tissue_positions[source_tissue][chrom]

        if len(positions) > max_points_per_tissue_chrom:
            positions = (
                pd.Series(positions)
                .sample(n=max_points_per_tissue_chrom, random_state=42)
                .astype(int)
                .tolist()
            )

            tissue_positions[source_tissue][chrom] = positions

        summary_records.append({
            "Source_Tissue": source_tissue,
            "Track_order_inner_to_outer": source_tissues.index(source_tissue) + 1,
            "Source": source,
            "Tissue": tissue,
            "Chromosome": chrom,
            "Total_validated_mapped_peptide_rows": chrom_counts[source_tissue].get(chrom, 0),
            "Sampled_points_plotted": len(tissue_positions[source_tissue][chrom])
        })

summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print(f"\nSummary saved: {summary_out}")
print("\nTrack order, innermost to outermost:")
for i, source_tissue in enumerate(source_tissues, start=1):
    print(f"{i:02d}. {source_tissue}")

# -----------------------------
# 7. Tissue colours
# -----------------------------
cmap = plt.get_cmap("tab20")

tissue_colours = {
    tissue: cmap(i % 20)
    for i, tissue in enumerate(source_tissues)
}

# -----------------------------
# 8. Build Circos plot
# -----------------------------
circos = Circos(chrom_lengths, space=2)

# Outer chromosome track
for sector in circos.sectors:

    outer_track = sector.add_track((96, 100))
    outer_track.axis(fc="#E6CDFF", ec="#3F007E", lw=0.6)

    sector.text(
        sector.name.replace("Chr", ""),
        r=104,
        size=14,
        weight="bold"
    )

# Tissue rings
n_tissues = len(source_tissues)
inner_r = 18
outer_r = 94
ring_height = (outer_r - inner_r) / n_tissues

for i, source_tissue in enumerate(source_tissues):

    # i = 0 is innermost
    # final source_tissue is outermost
    r0 = inner_r + i * ring_height
    r1 = r0 + ring_height * 0.85

    colour = tissue_colours[source_tissue]

    for sector in circos.sectors:

        track = sector.add_track((r0, r1))
        track.axis(fc="white", ec="lightgrey", lw=0.15)

        chrom = sector.name

        positions = tissue_positions[source_tissue].get(chrom, [])

        if len(positions) == 0:
            continue

        y_values = [0.5] * len(positions)

        track.scatter(
            positions,
            y_values,
            s=4,
            color=colour,
            marker="|",
            linewidths=0.5
        )

# -----------------------------
# 9. Plot and legend
# -----------------------------
fig = circos.plotfig(figsize=(12, 12))

# Manual legend outside plot, ordered innermost to outermost
legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="s",
        color="w",
        label=f"{i + 1}. {tissue}",
        markerfacecolor=tissue_colours[tissue],
        markersize=8
    )
    for i, tissue in enumerate(source_tissues)
]

legend = fig.legend(
    handles=legend_handles,
    title="Tissue tracks\n(inner → outer)",
    loc="upper right",
    bbox_to_anchor=(1.30, 0.95),
    frameon=True,
    fontsize=9,
    title_fontsize=12
)

legend.get_title().set_fontweight("bold")
legend.get_frame().set_edgecolor("lightgrey")
legend.get_frame().set_linewidth(1)
legend.get_frame().set_facecolor("white")

fig.suptitle(
    "Circular map of validated mapped wheat peptides by tissue",
    fontsize=16,
    fontweight="bold",
    y=1.02
)

plt.savefig(
    figure_out,
    dpi=600,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"Figure saved: {figure_out}")
display(summary.head())