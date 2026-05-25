# ============================================================
# Step 15 — EDA: HC/LC coverage by tissue (barplot)
# Memory-safe version: does not load long BED/peptide label columns
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# 1. Paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

protein_plot_out = figures_dir / "step15_source_tissue_protein_coverage_HC_LC.png"
gene_model_plot_out = figures_dir / "step15_source_tissue_gene_model_coverage_HC_LC.png"
step15_summary_out = tables_dir / "wheat_eda_coverage_HC_LC_step15.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")
protein_gene_mapping = pd.read_csv(protein_gene_mapping_file, low_memory=False)

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399",
    "background": "#E6CDFF"
}

# -----------------------------
# 3. Annotation denominator
# -----------------------------
gene_col = "GeneModel" if "GeneModel" in protein_gene_mapping.columns else "GeneID"
confidence_col = "Annotation_confidence"

total_gene_models = protein_gene_mapping[gene_col].nunique()

print(f"Total annotated gene models used as denominator: {total_gene_models:,}")

# -----------------------------
# 4. Load projected peptide tables from Step 9
# Only load columns required for this EDA step
# -----------------------------
projected_tables = []

projection_usecols = [
    "Projection_status",
    "ProteinID",
    "Peptide",
    confidence_col
]

for _, row in manifest.iterrows():

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Warning: missing projection file, skipped: {projection_path}")
        continue

    data = pd.read_csv(
        projection_path,
        usecols=lambda col: col in projection_usecols,
        low_memory=False
    )

    data = data[data["Projection_status"] == "projected"].copy()

    data["Source"] = row["Source"]
    data["Species"] = row["Species"]
    data["Tissue"] = row["Tissue-Raw-Code"]
    data["Source_Tissue"] = (
        data["Source"].astype(str) + "_" + data["Tissue"].astype(str)
    )

    projected_tables.append(data)

if not projected_tables:
    raise ValueError("No projected peptide tables were loaded. Please check Step 9 outputs.")

projected_all = pd.concat(projected_tables, ignore_index=True)

print(f"Projected rows loaded for Step 15: {len(projected_all):,}")

# -----------------------------
# 5. Annotation-projected HC/LC metrics
# -----------------------------
records = []

for (source, tissue, source_tissue), group in projected_all.groupby(
    ["Source", "Tissue", "Source_Tissue"],
    dropna=False
):

    hc = group[group[confidence_col].astype(str).str.upper() == "HC"]
    lc = group[group[confidence_col].astype(str).str.upper() == "LC"]

    records.append({
        "Source": source,
        "Tissue": tissue,
        "Source_Tissue": source_tissue,
        "HC_unique_proteins": hc["ProteinID"].nunique(),
        "LC_unique_proteins": lc["ProteinID"].nunique(),
        "HC_unique_peptides": hc["Peptide"].nunique(),
        "LC_unique_peptides": lc["Peptide"].nunique()
    })

coverage = pd.DataFrame(records)

# Ensure all manifest tissues are present
all_tissues = manifest[["Source", "Tissue-Raw-Code"]].copy()
all_tissues = all_tissues.rename(columns={"Tissue-Raw-Code": "Tissue"})
all_tissues["Source_Tissue"] = (
    all_tissues["Source"].astype(str) + "_" + all_tissues["Tissue"].astype(str)
)

coverage = all_tissues.merge(
    coverage,
    on=["Source", "Tissue", "Source_Tissue"],
    how="left"
).fillna(0)


# -----------------------------
# 6. Convert counts to percentage of total annotated gene models
# -----------------------------

# Total annotated gene models from Step 5
# (266,752 unique mapped gene models)
# total_gene_models = 266752

# Protein-level coverage percentages
coverage["HC_protein_percent"] = (
    coverage["HC_unique_proteins"] / total_gene_models
) * 100

coverage["LC_protein_percent"] = (
    coverage["LC_unique_proteins"] / total_gene_models
) * 100

# Total protein coverage
coverage["Total_protein_percent"] = (
    coverage["HC_protein_percent"] +
    coverage["LC_protein_percent"]
)

# -----------------------------
# Remove peptide percentage columns
# (biologically misleading and can exceed 100%)
# -----------------------------
cols_to_remove = [
    "HC_peptide_percent",
    "LC_peptide_percent",
    "Total_peptide_percent"
]

coverage = coverage.drop(
    columns=[c for c in cols_to_remove if c in coverage.columns],
    errors="ignore"
)

# -----------------------------
# Sort and export
# -----------------------------
coverage = coverage.sort_values(
    "Total_protein_percent",
    ascending=True
)

coverage.to_csv(step15_summary_out, index=False)

print(f"Saved corrected Step 15 summary: {step15_summary_out}")

display(coverage.head())

# -----------------------------
# 8. Plotting helper
# -----------------------------
def plot_stacked_horizontal_bar(data, value_cols, labels, title, xlabel, output_path):

    plot_data = data.copy()
    y = plot_data["Source_Tissue"]

    fig_height = max(8, len(plot_data) * 0.35)

    fig, ax = plt.subplots(figsize=(12, fig_height))

    left = pd.Series([0] * len(plot_data), index=plot_data.index)

    for col, label in zip(value_cols, labels):
        ax.barh(
            y,
            plot_data[col],
            left=left,
            label=label,
            color=brand_colours[label]
        )
        left = left + plot_data[col]

    ax.set_xlabel(xlabel)
    ax.set_ylabel("Source_Tissue")
    ax.set_title(title)
    ax.legend(title="Evidence category", loc="lower right")

    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"Figure saved: {output_path}")

# -----------------------------
# 9. Protein-level plot
# -----------------------------
plot_stacked_horizontal_bar(
    data=coverage,
    value_cols=["HC_protein_percent", "LC_protein_percent"],
    labels=["HC", "LC"],
    title="Protein-level proteogenomic coverage by source and tissue",
    xlabel="Unique protein accessions as % of total annotated gene models",
    output_path=protein_plot_out
)

display(coverage)

# -----------------------------
# 10. Gene-model coverage plot
# -----------------------------
if (
    "HC_gene_model_percent" in coverage.columns and
    "LC_gene_model_percent" in coverage.columns
):

    coverage_gene_sorted = coverage.sort_values(
        "Total_gene_model_percent",
        ascending=True
    )

    plot_stacked_horizontal_bar(
        data=coverage_gene_sorted,
        value_cols=[
            "HC_gene_model_percent",
            "LC_gene_model_percent"
        ],
        labels=["HC", "LC"],
        title="Gene-model proteogenomic coverage by source and tissue",
        xlabel="Supported gene models as % of total annotated gene models",
        output_path=peptide_plot_out
    )