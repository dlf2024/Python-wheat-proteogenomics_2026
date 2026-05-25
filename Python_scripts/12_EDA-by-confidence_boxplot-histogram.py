# ============================================================
# Step 17 — EDA: Peptide distribution by confidence level (boxplot & histogram)
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

gene_summary_file = tables_dir / "wheat_gene_model_summary_step13.csv"

histogram_out = figures_dir / "step17_peptide_support_per_gene_model_histogram.png"
boxplot_out = figures_dir / "step17_peptide_support_per_gene_model_HC_LC_boxplot.png"
step17_summary_out = tables_dir / "wheat_peptide_support_per_gene_model_summary_step17.csv"

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",      # dark purple
    "LC": "#FF3399",      # pink
    "gold": "#FFC000",
    "lavender": "#E6CDFF"
}

# -----------------------------
# 3. Load gene model summary
# -----------------------------
gene_summary = pd.read_csv(gene_summary_file, low_memory=False)

gene_col = "GeneModel" if "GeneModel" in gene_summary.columns else "GeneID"
confidence_col = "Annotation_confidence"

required_cols = [gene_col, confidence_col, "Unique_peptides"]
missing_cols = [col for col in required_cols if col not in gene_summary.columns]

if missing_cols:
    raise KeyError(f"Missing required column(s): {missing_cols}")

gene_summary["Unique_peptides"] = pd.to_numeric(
    gene_summary["Unique_peptides"],
    errors="coerce"
).fillna(0)

gene_summary = gene_summary[gene_summary["Unique_peptides"] > 0].copy()

gene_summary[confidence_col] = gene_summary[confidence_col].astype(str).str.upper()

print(f"Gene models with peptide support: {gene_summary[gene_col].nunique():,}")

# -----------------------------
# 4. Peptide support bins
# -----------------------------
def peptide_support_bin(value):
    if value == 1:
        return "1 peptide"
    elif 2 <= value <= 4:
        return "2–4 peptides"
    elif 5 <= value <= 9:
        return "5–9 peptides"
    else:
        return "≥10 peptides"

gene_summary["Peptide_support_bin"] = gene_summary["Unique_peptides"].apply(peptide_support_bin)

# -----------------------------
# 5. Summary table
# -----------------------------
step17_summary = (
    gene_summary
    .groupby([confidence_col, "Peptide_support_bin"], dropna=False)
    .agg(
        Gene_model_count=(gene_col, "nunique"),
        Median_unique_peptides=("Unique_peptides", "median"),
        Mean_unique_peptides=("Unique_peptides", "mean"),
        Max_unique_peptides=("Unique_peptides", "max")
    )
    .reset_index()
)

total_by_confidence = (
    gene_summary
    .groupby(confidence_col)[gene_col]
    .nunique()
    .reset_index(name="Total_gene_models_with_peptide_support")
)

step17_summary = step17_summary.merge(
    total_by_confidence,
    on=confidence_col,
    how="left"
)

step17_summary["Percent_within_confidence_class"] = (
    step17_summary["Gene_model_count"] /
    step17_summary["Total_gene_models_with_peptide_support"] *
    100
).round(4)

bin_order = ["1 peptide", "2–4 peptides", "5–9 peptides", "≥10 peptides"]
step17_summary["Peptide_support_bin"] = pd.Categorical(
    step17_summary["Peptide_support_bin"],
    categories=bin_order,
    ordered=True
)

step17_summary = step17_summary.sort_values(
    [confidence_col, "Peptide_support_bin"]
)

step17_summary.to_csv(step17_summary_out, index=False)

# -----------------------------
# 6. Histogram: unique peptide support per gene model
# -----------------------------
plt.figure(figsize=(10, 6))

for confidence, colour in [("HC", brand_colours["HC"]), ("LC", brand_colours["LC"])]:

    subset = gene_summary[
        gene_summary[confidence_col] == confidence
    ]

    if len(subset) > 0:

        plt.hist(
            subset["Unique_peptides"],
            bins=50,
            alpha=0.65,
            label=confidence,
            color=colour
        )

plt.xlabel("Unique peptides per gene model")
plt.ylabel("Number of gene models")
plt.title("Distribution of peptide support per wheat gene model")

plt.legend(title="Annotation confidence")

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig(
    histogram_out,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Histogram saved: {histogram_out}")

# -----------------------------
# 7. HC vs LC boxplot
# -----------------------------
hc_values = gene_summary.loc[
    gene_summary[confidence_col] == "HC",
    "Unique_peptides"
]

lc_values = gene_summary.loc[
    gene_summary[confidence_col] == "LC",
    "Unique_peptides"
]

plt.figure(figsize=(4, 6))

box = plt.boxplot(
    [hc_values, lc_values],
    tick_labels=["HC", "LC"],   # updated Matplotlib syntax
    patch_artist=True,
    showfliers=False
)

box["boxes"][0].set_facecolor(brand_colours["HC"])
box["boxes"][1].set_facecolor(brand_colours["LC"])

for median in box["medians"]:
    median.set_color("white")
    median.set_linewidth(2)

plt.ylabel("Unique peptides per gene model")
plt.xlabel("Annotation confidence")

plt.title("Peptide support per gene model")

plt.grid(axis="y", linestyle="--", alpha=0.3)

plt.tight_layout()

plt.savefig(
    boxplot_out,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Boxplot saved: {boxplot_out}")

# -----------------------------
# 8. Display summary
# -----------------------------
print(f"Step 17 summary saved: {step17_summary_out}")
display(step17_summary)