# ============================================================
# Step 19 — EDA: Protein length vs peptide support (scatterplot)
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

protein_summary_file = tables_dir / "wheat_protein_isoform_summary_step13.csv"
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

scatter_out = figures_dir / "step19_protein_length_vs_peptide_support_scatter.png"
step19_summary_out = tables_dir / "wheat_protein_length_vs_peptide_support_summary_step19.csv"

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
# 3. Load tables
# -----------------------------
protein_summary = pd.read_csv(protein_summary_file, low_memory=False)
protein_mapping = pd.read_csv(protein_gene_mapping_file, low_memory=False)

# -----------------------------
# 4. Detect columns
# -----------------------------
protein_col = "ProteinID"

length_col = "Protein_length_aa_from_CDS"

if length_col not in protein_mapping.columns:
    raise KeyError(f"Could not find '{length_col}' in protein mapping table.")

if "Unique_peptides" not in protein_summary.columns:
    raise KeyError("Missing 'Unique_peptides' in protein summary table.")

# Use confidence from protein_summary if present, otherwise from mapping table
if "Annotation_confidence" in protein_summary.columns:
    confidence_col = "Annotation_confidence"
    protein_summary_clean = protein_summary.copy()

elif "Annotation_confidence" in protein_mapping.columns:
    confidence_col = "Annotation_confidence"

    protein_meta_conf = (
        protein_mapping[[protein_col, confidence_col]]
        .drop_duplicates(subset=[protein_col])
        .copy()
    )

    protein_summary_clean = protein_summary.merge(
        protein_meta_conf,
        on=protein_col,
        how="left"
    )

else:
    raise KeyError("Could not find 'Annotation_confidence' in either input table.")

# -----------------------------
# 5. Add protein length
# -----------------------------
protein_length_meta = (
    protein_mapping[[protein_col, length_col]]
    .drop_duplicates(subset=[protein_col])
    .copy()
)

plot_data = protein_summary_clean.merge(
    protein_length_meta,
    on=protein_col,
    how="left"
)

# -----------------------------
# 6. Clean variables
# -----------------------------
plot_data["Unique_peptides"] = pd.to_numeric(
    plot_data["Unique_peptides"],
    errors="coerce"
)

plot_data[length_col] = pd.to_numeric(
    plot_data[length_col],
    errors="coerce"
)

plot_data[confidence_col] = plot_data[confidence_col].astype(str).str.upper()

plot_data = plot_data.dropna(
    subset=["Unique_peptides", length_col, confidence_col]
)

plot_data = plot_data[
    plot_data[confidence_col].isin(["HC", "LC"])
].copy()

print(f"Proteins plotted: {len(plot_data):,}")

# -----------------------------
# 7. Summary table
# -----------------------------
step19_summary = (
    plot_data
    .groupby(confidence_col, dropna=False)
    .agg(
        Protein_isoforms=(protein_col, "nunique"),
        Mean_protein_length_aa=(length_col, "mean"),
        Median_protein_length_aa=(length_col, "median"),
        Max_protein_length_aa=(length_col, "max"),
        Mean_unique_peptides=("Unique_peptides", "mean"),
        Median_unique_peptides=("Unique_peptides", "median"),
        Max_unique_peptides=("Unique_peptides", "max")
    )
    .reset_index()
)

step19_summary.to_csv(step19_summary_out, index=False)

# -----------------------------
# 8. Scatterplot
# -----------------------------
plt.figure(figsize=(10, 7))

for confidence in ["HC", "LC"]:

    subset = plot_data[
        plot_data[confidence_col] == confidence
    ]

    plt.scatter(
        subset[length_col],
        subset["Unique_peptides"],
        alpha=0.35,
        s=20,
        color=brand_colours[confidence],
        label=confidence,
        edgecolors="none"
    )

plt.xlabel("Protein length from CDS (amino acids)")
plt.ylabel("Unique peptides per protein isoform")

plt.title("Protein length versus peptide support")

plt.legend(title="Annotation confidence")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    scatter_out,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Scatterplot saved: {scatter_out}")
print(f"Step 19 summary saved: {step19_summary_out}")

display(step19_summary)