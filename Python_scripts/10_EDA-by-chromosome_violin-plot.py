# ============================================================
# Step 20 — EDA: Violin plot of chromosome distribution of peptide genomic positions
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

projection_combined_file = tables_dir / "wheat_all_tissues_nonredundant_projected_peptides.csv"

figure_out = figures_dir / "step20_violinplot_peptide_genomic_start_by_chromosome.png"
summary_out = tables_dir / "wheat_peptide_genomic_start_by_chromosome_summary_step20.csv"

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399"
}

# -----------------------------
# 3. Load annotation-projected peptide data in chunks
# -----------------------------
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

chrom_col = "Chromosome"
start_col = "BED_start_0based"
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

# Load ProteinID → Annotation_confidence lookup
protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    usecols=lambda col: col in [protein_col, confidence_col],
    low_memory=False
)

protein_conf_lookup = (
    protein_mapping
    .dropna(subset=[protein_col, confidence_col])
    .drop_duplicates(subset=[protein_col])
)

projected_needed_cols = [
    chrom_col,
    start_col,
    protein_col
]

max_points_per_group = 50000
chunksize = 100_000

summary_chunks = []
sample_chunks = []

for chunk in pd.read_csv(
    projection_combined_file,
    usecols=lambda col: col in projected_needed_cols,
    chunksize=chunksize,
    low_memory=False
):

    chunk = chunk.merge(
        protein_conf_lookup,
        on=protein_col,
        how="left"
    )

    chunk = chunk.rename(columns={
        chrom_col: "Chromosome",
        start_col: "Genomic_start",
        confidence_col: "Evidence"
    })

    chunk["Evidence"] = chunk["Evidence"].astype(str).str.upper()
    chunk["Evidence"] = chunk["Evidence"].map({
        "HC": "HC",
        "LC": "LC"
    })

    chunk["Genomic_start"] = pd.to_numeric(
        chunk["Genomic_start"],
        errors="coerce"
    )

    chunk = chunk.dropna(
        subset=["Chromosome", "Genomic_start", "Evidence"]
    )

    chunk["Chromosome"] = chunk["Chromosome"].astype(str)

    summary_chunks.append(
        chunk[["Chromosome", "Genomic_start", "Evidence"]]
    )

    # Sample lightly from each chunk for plotting
    if len(chunk) > 3000:
        chunk_sample = chunk.sample(
            n=3000,
            random_state=42
        )
    else:
        chunk_sample = chunk

    sample_chunks.append(
        chunk_sample[["Chromosome", "Genomic_start", "Evidence"]]
    )

projected_summary_data = pd.concat(summary_chunks, ignore_index=True)
projected_plot_sample = pd.concat(sample_chunks, ignore_index=True)

print(f"Projected rows for summary: {len(projected_summary_data):,}")
print(f"Projected sampled rows before group cap: {len(projected_plot_sample):,}")

# -----------------------------
# 4. Chromosome ordering
# -----------------------------
def normalise_chromosome_name(value):
    value = str(value).strip()

    if value.lower() in ["chrunknown", "unknown", "nan"]:
        return "ChrUnknown"

    if value.startswith("Chr"):
        return value

    return "Chr" + value

chrom_order = [
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D",
    "ChrUnknown"
]

projected_summary_data["Chromosome"] = projected_summary_data["Chromosome"].apply(normalise_chromosome_name)
projected_plot_sample["Chromosome"] = projected_plot_sample["Chromosome"].apply(normalise_chromosome_name)

projected_summary_data = projected_summary_data[
    projected_summary_data["Chromosome"].isin(chrom_order)
].copy()

projected_plot_sample = projected_plot_sample[
    projected_plot_sample["Chromosome"].isin(chrom_order)
].copy()

# -----------------------------
# 5. Build summary table from full projected data
# -----------------------------
summary_data = projected_summary_data.copy()

summary_data["Chromosome"] = pd.Categorical(
    summary_data["Chromosome"],
    categories=chrom_order,
    ordered=True
)

summary = (
    summary_data
    .groupby(["Chromosome", "Evidence"], observed=True)
    .agg(
        Peptide_rows=("Genomic_start", "size"),
        Median_genomic_start=("Genomic_start", "median"),
        Mean_genomic_start=("Genomic_start", "mean"),
        Min_genomic_start=("Genomic_start", "min"),
        Max_genomic_start=("Genomic_start", "max")
    )
    .reset_index()
)

summary.to_csv(summary_out, index=False)

# Free memory before plotting
del projected_summary_data
del summary_data
del summary_chunks

# -----------------------------
# 6. Build plot sample and cap per chromosome/evidence group
# -----------------------------
plot_data = projected_plot_sample.copy()

plot_data["Chromosome"] = pd.Categorical(
    plot_data["Chromosome"],
    categories=chrom_order,
    ordered=True
)

sampled_groups = []

for (chrom, evidence), group in plot_data.groupby(
    ["Chromosome", "Evidence"],
    observed=True
):

    if len(group) > max_points_per_group:
        group = group.sample(
            n=max_points_per_group,
            random_state=42
        )

    sampled_groups.append(group)

if len(sampled_groups) == 0:
    raise ValueError(
        "No chromosome/evidence groups remained after filtering. "
        "Check chromosome names in the input tables."
    )

plot_sample = pd.concat(sampled_groups, ignore_index=True)

print(f"Rows used for violin plot: {len(plot_sample):,}")


# -----------------------------
# 7. Violin plot
# -----------------------------
fig, ax = plt.subplots(figsize=(16, 7))

positions = range(len(chrom_order))
offsets = {
    "HC": -0.25,
    "LC": 0.25
}

width = 0.22

for evidence in ["HC", "LC"]:

    data_by_chrom = []
    pos_by_chrom = []

    for i, chrom in enumerate(chrom_order):

        values = plot_sample.loc[
            (plot_sample["Chromosome"] == chrom) &
            (plot_sample["Evidence"] == evidence),
            "Genomic_start"
        ].dropna()

        if len(values) > 0:
            data_by_chrom.append(values)
            pos_by_chrom.append(i + offsets[evidence])

    if len(data_by_chrom) == 0:
        continue

    violin = ax.violinplot(
        data_by_chrom,
        positions=pos_by_chrom,
        widths=width,
        showmeans=False,
        showmedians=True,
        showextrema=False
    )

    for body in violin["bodies"]:
        body.set_facecolor(brand_colours[evidence])
        body.set_edgecolor("black")
        body.set_alpha(1)

    violin["cmedians"].set_color("white")
    violin["cmedians"].set_linewidth(1.2)

# -----------------------------
# 8. Plot formatting
# -----------------------------

ax.set_xticks(list(positions))

ax.set_xticklabels(
    chrom_order,
    rotation=45,
    ha="right",
    fontsize=12
)

# Y-axis tick labels
ax.tick_params(
    axis="y",
    labelsize=12
)

# Axis labels
ax.set_xlabel(
    "Chromosome",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

ax.set_ylabel(
    "Peptide genomic start position",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

# Title
ax.set_title(
    "Genomic distribution of HC and LC peptide evidence by chromosome",
    fontsize=20,
    fontweight="bold",
    pad=20
)

# Grid
ax.grid(axis="y", linestyle="--", alpha=0.3)

# Manual legend
legend_labels = {
    "HC": "HC",
    "LC": "LC"
}

legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="o",
        color="w",
        label=legend_labels[label],
        markerfacecolor=colour,
        markeredgecolor="black",
        markersize=14
    )
    for label, colour in brand_colours.items()
]

legend = ax.legend(
    handles=legend_handles,
    title="Legend",
    title_fontsize=14,
    fontsize=14,
    loc="upper right",
    frameon=True
)

# Bold legend title
legend.get_title().set_fontweight("bold")

# Optional: thicker legend border
legend.get_frame().set_linewidth(1.5)

# Tight layout
plt.tight_layout()

plt.savefig(
    figure_out,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Figure saved: {figure_out}")
print(f"Summary saved: {summary_out}")

display(summary)