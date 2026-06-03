# ============================================================
# Step 20 — EDA: Protein length vs validated peptide support
# Linear regression by HC/LC with R²
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")

figures_dir.mkdir(parents=True, exist_ok=True)

# Step 15 output: protein/isoform summary built from fully validated rows
protein_summary_file = tables_dir / "wheat_protein_isoform_summary_step15.csv"
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

scatter_out = figures_dir / "step20_validated_protein_length_vs_peptide_support_scatter_regression.png"
step20_summary_out = tables_dir / "wheat_validated_protein_length_vs_peptide_support_summary_step20.csv"

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

if protein_col not in protein_summary.columns:
    raise KeyError(f"Missing '{protein_col}' in protein summary table.")

if protein_col not in protein_mapping.columns:
    raise KeyError(f"Missing '{protein_col}' in protein-gene mapping table.")

if length_col not in protein_mapping.columns:
    raise KeyError(f"Could not find '{length_col}' in protein-gene mapping table.")

if "Unique_peptides" not in protein_summary.columns:
    raise KeyError("Missing 'Unique_peptides' in protein summary table.")

# Use confidence from protein_summary if present, otherwise merge from mapping table
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

# Keep only proteins with at least one validated peptide
plot_data = plot_data[
    plot_data["Unique_peptides"] > 0
].copy()

print(f"Protein isoforms plotted: {len(plot_data):,}")

# -----------------------------
# 7. Regression helper
# -----------------------------
def linear_regression_with_r2(data, x_col, y_col):
    """
    Fit simple linear regression y = slope*x + intercept
    and calculate R² using numpy only.
    """

    clean = data[[x_col, y_col]].dropna().copy()

    x = clean[x_col].astype(float).to_numpy()
    y = clean[y_col].astype(float).to_numpy()

    if len(x) < 2 or np.nanstd(x) == 0 or np.nanstd(y) == 0:
        return {
            "n": len(x),
            "slope": pd.NA,
            "intercept": pd.NA,
            "r2": pd.NA,
            "x_line": None,
            "y_line": None
        }

    slope, intercept = np.polyfit(x, y, 1)

    y_pred = slope * x + intercept

    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)

    r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else pd.NA

    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept

    return {
        "n": len(x),
        "slope": slope,
        "intercept": intercept,
        "r2": r2,
        "x_line": x_line,
        "y_line": y_line
    }

# -----------------------------
# 8. Summary table with regression metrics
# -----------------------------
summary_records = []

regression_results = {}

for confidence in ["HC", "LC"]:

    subset = plot_data[
        plot_data[confidence_col] == confidence
    ].copy()

    regression = linear_regression_with_r2(
        data=subset,
        x_col=length_col,
        y_col="Unique_peptides"
    )

    regression_results[confidence] = regression

    summary_records.append({
        confidence_col: confidence,
        "Protein_isoforms": subset[protein_col].nunique(),
        "Mean_protein_length_aa": subset[length_col].mean(),
        "Median_protein_length_aa": subset[length_col].median(),
        "Max_protein_length_aa": subset[length_col].max(),
        "Mean_unique_validated_peptides": subset["Unique_peptides"].mean(),
        "Median_unique_validated_peptides": subset["Unique_peptides"].median(),
        "Max_unique_validated_peptides": subset["Unique_peptides"].max(),
        "Linear_regression_n": regression["n"],
        "Linear_regression_slope": regression["slope"],
        "Linear_regression_intercept": regression["intercept"],
        "Linear_regression_R2": regression["r2"]
    })

step20_summary = pd.DataFrame(summary_records)

# Round selected numeric columns for readability
for col in [
    "Mean_protein_length_aa",
    "Median_protein_length_aa",
    "Mean_unique_validated_peptides",
    "Median_unique_validated_peptides",
    "Linear_regression_slope",
    "Linear_regression_intercept",
    "Linear_regression_R2"
]:
    if col in step20_summary.columns:
        step20_summary[col] = pd.to_numeric(
            step20_summary[col],
            errors="coerce"
        ).round(4)

step20_summary.to_csv(step20_summary_out, index=False)

# -----------------------------
# 9. Scatterplot with regression lines
# -----------------------------
plt.figure(figsize=(10, 7))

for confidence in ["HC", "LC"]:

    subset = plot_data[
        plot_data[confidence_col] == confidence
    ]

    regression = regression_results[confidence]

    r2_label = (
        f"{confidence} (R²={regression['r2']:.3f})"
        if pd.notna(regression["r2"])
        else f"{confidence} (R²=NA)"
    )

    plt.scatter(
        subset[length_col],
        subset["Unique_peptides"],
        alpha=0.30,
        s=20,
        color=brand_colours[confidence],
        label=r2_label,
        edgecolors="none"
    )

    # Regression line
    if regression["x_line"] is not None:

        plt.plot(
            regression["x_line"],
            regression["y_line"],
            color=brand_colours[confidence],
            linewidth=2.5,
            linestyle="-"
        )

plt.xlabel("Protein length from CDS (amino acids)")
plt.ylabel("Unique validated peptides per protein isoform")

plt.title("Protein length versus validated peptide support")

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
print(f"Step 20 summary saved: {step20_summary_out}")

display(step20_summary)