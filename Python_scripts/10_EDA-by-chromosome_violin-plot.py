# ============================================================
# Step 21 — EDA: Violin plot of genomic peptide positions by chromosome
# All-tissue combined, non-redundant, fully validated projections only
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

# Step 13 output:
# all-tissue combined, non-redundant, translation-validated + sanity-passed peptide projections
projection_combined_file = tables_dir / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv"

# Protein-to-gene mapping table used to recover HC/LC annotation confidence if needed
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

figure_out = figures_dir / "step21_violinplot_nonredundant_validated_peptide_genomic_start_by_chromosome.png"
summary_out = tables_dir / "wheat_nonredundant_validated_peptide_genomic_start_by_chromosome_summary_step21.csv"

if not projection_combined_file.exists():
    raise FileNotFoundError(
        f"Step 13 combined non-redundant validated peptide table not found:\n"
        f"{projection_combined_file}\n\n"
        "Please run Step 13 first."
    )

if not protein_gene_mapping_file.exists():
    raise FileNotFoundError(
        f"Protein-gene mapping file not found:\n"
        f"{protein_gene_mapping_file}"
    )

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399"
}

# -----------------------------
# 3. Settings
# -----------------------------
chrom_col = "Chromosome"
start_col = "BED_start_0based"
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

max_points_per_group = 50_000
chunksize = 100_000

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

# -----------------------------
# 5. Load ProteinID → Annotation_confidence lookup
# -----------------------------
protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    usecols=lambda col: col in [protein_col, confidence_col],
    low_memory=False
)

if protein_col not in protein_mapping.columns:
    raise KeyError(f"Missing '{protein_col}' in protein-gene mapping table.")

if confidence_col not in protein_mapping.columns:
    raise KeyError(f"Missing '{confidence_col}' in protein-gene mapping table.")

protein_conf_lookup = (
    protein_mapping
    .dropna(subset=[protein_col, confidence_col])
    .drop_duplicates(subset=[protein_col])
    .copy()
)

protein_conf_lookup[confidence_col] = (
    protein_conf_lookup[confidence_col]
    .astype(str)
    .str.upper()
)

# -----------------------------
# 6. Inspect combined non-redundant table columns
# -----------------------------
header = pd.read_csv(projection_combined_file, nrows=0)

required_cols = [
    chrom_col,
    start_col,
    protein_col
]

missing_cols = [
    col for col in required_cols
    if col not in header.columns
]

if missing_cols:
    raise KeyError(
        f"Missing required column(s) in Step 13 combined table: {missing_cols}"
    )

# If Annotation_confidence is already present in the Step 13 table, use it.
# Otherwise merge it from the protein-gene mapping table.
combined_has_confidence = confidence_col in header.columns

projected_needed_cols = [
    chrom_col,
    start_col,
    protein_col
]

if combined_has_confidence:
    projected_needed_cols.append(confidence_col)

# Keep extra useful columns if present
optional_cols = [
    "Peptide",
    "Peptide_label",
    "Gene_label",
    "BED_block_count",
    "Tissue_count",
    "Observation_count"
]

for col in optional_cols:
    if col in header.columns:
        projected_needed_cols.append(col)

projected_needed_cols = list(dict.fromkeys(projected_needed_cols))

print("Step 21 input:")
print(projection_combined_file)
print(f"Using all-tissue non-redundant validated rows from Step 13.")
print(f"Annotation confidence already in Step 13 table: {combined_has_confidence}")

# -----------------------------
# 7. Load combined validated non-redundant data in chunks
# -----------------------------
summary_chunks = []
sample_chunks = []

total_rows_read = 0
total_rows_retained = 0

for chunk_i, chunk in enumerate(
    pd.read_csv(
        projection_combined_file,
        usecols=lambda col: col in projected_needed_cols,
        chunksize=chunksize,
        low_memory=False
    ),
    start=1
):

    total_rows_read += len(chunk)

    # Add HC/LC annotation confidence if not already present
    if confidence_col not in chunk.columns:

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
    ).copy()

    chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

    chunk = chunk[
        chunk["Chromosome"].isin(chrom_order)
    ].copy()

    if chunk.empty:
        continue

    total_rows_retained += len(chunk)

    # Convert to Mb for easier plotting and interpretation
    chunk["Genomic_start_Mb"] = chunk["Genomic_start"] / 1_000_000

    summary_chunks.append(
        chunk[["Chromosome", "Genomic_start", "Genomic_start_Mb", "Evidence"]]
    )

    # Sample lightly from each chunk for plotting
    if len(chunk) > 3_000:
        chunk_sample = chunk.sample(
            n=3_000,
            random_state=42 + chunk_i
        )
    else:
        chunk_sample = chunk

    sample_chunks.append(
        chunk_sample[["Chromosome", "Genomic_start_Mb", "Evidence"]]
    )

    print(
        f"Chunk {chunk_i}: read {len(chunk):,} retained rows | "
        f"cumulative retained {total_rows_retained:,}"
    )

if not summary_chunks:
    raise ValueError(
        "No valid HC/LC rows were loaded from the Step 13 combined table."
    )

projected_summary_data = pd.concat(summary_chunks, ignore_index=True)
projected_plot_sample = pd.concat(sample_chunks, ignore_index=True)

print(f"\nRows read from Step 13 combined table: {total_rows_read:,}")
print(f"Rows retained for summary: {len(projected_summary_data):,}")
print(f"Sampled rows before group cap: {len(projected_plot_sample):,}")

# -----------------------------
# 8. Build summary table from full non-redundant validated data
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
        Nonredundant_validated_rows=("Genomic_start", "size"),
        Median_genomic_start_bp=("Genomic_start", "median"),
        Mean_genomic_start_bp=("Genomic_start", "mean"),
        Min_genomic_start_bp=("Genomic_start", "min"),
        Max_genomic_start_bp=("Genomic_start", "max"),
        Median_genomic_start_Mb=("Genomic_start_Mb", "median"),
        Mean_genomic_start_Mb=("Genomic_start_Mb", "mean"),
        Min_genomic_start_Mb=("Genomic_start_Mb", "min"),
        Max_genomic_start_Mb=("Genomic_start_Mb", "max")
    )
    .reset_index()
)

summary.to_csv(summary_out, index=False)

# Free memory before plotting
del projected_summary_data
del summary_data
del summary_chunks

# -----------------------------
# 9. Build plot sample and cap per chromosome/evidence group
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
        "Check chromosome names in the input table."
    )

plot_sample = pd.concat(sampled_groups, ignore_index=True)

print(f"Rows used for violin plot: {len(plot_sample):,}")

# -----------------------------
# 10. Violin plot
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
            "Genomic_start_Mb"
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
        body.set_alpha(0.85)

    violin["cmedians"].set_color("white")
    violin["cmedians"].set_linewidth(1.2)

# -----------------------------
# 11. Plot formatting
# -----------------------------
ax.set_xticks(list(positions))

ax.set_xticklabels(
    chrom_order,
    rotation=45,
    ha="right",
    fontsize=12
)

ax.tick_params(
    axis="y",
    labelsize=12
)

ax.set_xlabel(
    "Chromosome",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

ax.set_ylabel(
    "Genomic start position (Mb)",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

ax.set_title(
    "Genomic distribution of non-redundant validated HC and LC peptide evidence by chromosome",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.grid(axis="y", linestyle="--", alpha=0.3)

# Manual legend
legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="o",
        color="w",
        label=evidence,
        markerfacecolor=brand_colours[evidence],
        markeredgecolor="black",
        markersize=14
    )
    for evidence in ["HC", "LC"]
]

legend = ax.legend(
    handles=legend_handles,
    title="Annotation confidence",
    title_fontsize=14,
    fontsize=14,
    loc="upper right",
    frameon=True
)

legend.get_title().set_fontweight("bold")
legend.get_frame().set_linewidth(1.5)

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