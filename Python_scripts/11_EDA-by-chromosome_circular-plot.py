# ============================================================
# Step 21 — EDA: Circular tissue-level peptide genome map
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict
from pycirclize import Circos

# -----------------------------
# 1. Paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

figure_out = figures_dir / "step21_circos_tissue_peptide_tracks.png"
summary_out = tables_dir / "wheat_circos_tissue_peptide_summary_step21.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

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
    return str(value).replace("-", "_").replace(" ", "_")


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

# -----------------------------
# 5. Sample projected peptide positions by tissue and chromosome
# -----------------------------
tissue_positions = defaultdict(lambda: defaultdict(list))
summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    tissue = clean_tissue_label(row["Tissue-Raw-Code"])
    source_tissue = f"{source}_{tissue}"

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Warning: missing projection file, skipped: {projection_path}")
        continue

    print(f"Sampling: {source_tissue}")

    chrom_counts = defaultdict(int)

    for chunk in pd.read_csv(
        projection_path,
        usecols=lambda col: col in [
            "Projection_status",
            "Chromosome",
            "BED_start_0based"
        ],
        chunksize=chunksize,
        low_memory=False
    ):

        chunk = chunk[chunk["Projection_status"] == "projected"].copy()

        if chunk.empty:
            continue

        chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

        chunk = chunk[chunk["Chromosome"].isin(chrom_order)].copy()

        chunk["BED_start_0based"] = pd.to_numeric(
            chunk["BED_start_0based"],
            errors="coerce"
        )

        chunk = chunk.dropna(subset=["Chromosome", "BED_start_0based"])

        for chrom, group in chunk.groupby("Chromosome"):

            chrom_counts[chrom] += len(group)

            # Sample small number per chunk to avoid memory overload
            n_sample = min(50, len(group))

            tissue_positions[source_tissue][chrom].extend(
                group["BED_start_0based"]
                .sample(n=n_sample, random_state=42)
                .astype(int)
                .tolist()
            )

    # Final cap per tissue/chromosome
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
            "Source": source,
            "Tissue": tissue,
            "Source_Tissue": source_tissue,
            "Chromosome": chrom,
            "Total_projected_peptide_rows": chrom_counts.get(chrom, 0),
            "Sampled_points_plotted": len(tissue_positions[source_tissue][chrom])
        })

summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print(f"Summary saved: {summary_out}")

# -----------------------------
# 6. Tissue colours
# -----------------------------
source_tissues = list(tissue_positions.keys())

cmap = plt.get_cmap("tab20")
tissue_colours = {
    tissue: cmap(i % 20)
    for i, tissue in enumerate(source_tissues)
}

# -----------------------------
# 7. Build Circos plot
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
# 8. Plot and legend
# -----------------------------
fig = circos.plotfig(figsize=(12, 12))

# Manual legend outside plot
legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="s",
        color="w",
        label=tissue,
        markerfacecolor=tissue_colours[tissue],
        markersize=8
    )
    for tissue in source_tissues
]

fig.legend(
    handles=legend_handles,
    title="Tissue tracks",
    loc="upper right",
    bbox_to_anchor=(1.25, 0.95),
    frameon=True,
    fontsize=10,
    title_fontsize=14
)

legend.get_title().set_fontweight("bold")
legend.get_frame().set_edgecolor("lightgrey")
legend.get_frame().set_linewidth(1)
legend.get_frame().set_facecolor("white")

fig.suptitle(
    "Circular map of projected wheat peptides by tissue",
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