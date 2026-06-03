# ============================================================
# Step 16 — EDA: cumulated bar plots of HC/LC coverage by tissue
# Fully validated rows only
# Translation-validated + sanity-check-passed projections
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

# Step 11 output: translation-validated rows with sanity-check status
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

protein_plot_out = figures_dir / "step16_source_tissue_protein_coverage_HC_LC_validated.png"
gene_model_plot_out = figures_dir / "step16_source_tissue_gene_model_coverage_HC_LC_validated.png"
step16_summary_out = tables_dir / "wheat_eda_coverage_HC_LC_validated_step16.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")
protein_gene_mapping = pd.read_csv(protein_gene_mapping_file, low_memory=False)

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399",
    "background": "#E6CDFF"
}

# -----------------------------
# 3. Annotation denominators
# -----------------------------
gene_col = "GeneModel" if "GeneModel" in protein_gene_mapping.columns else "GeneID"
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

required_mapping_cols = [gene_col, protein_col, confidence_col]
missing_mapping_cols = [
    col for col in required_mapping_cols
    if col not in protein_gene_mapping.columns
]

if missing_mapping_cols:
    raise KeyError(
        f"Missing required column(s) in protein-gene mapping table: {missing_mapping_cols}"
    )

all_gene_models = protein_gene_mapping[[gene_col, confidence_col]].drop_duplicates()

total_gene_models = all_gene_models[gene_col].nunique()

total_hc_gene_models = all_gene_models.loc[
    all_gene_models[confidence_col].astype(str).str.upper() == "HC",
    gene_col
].nunique()

total_lc_gene_models = all_gene_models.loc[
    all_gene_models[confidence_col].astype(str).str.upper() == "LC",
    gene_col
].nunique()

total_proteins = protein_gene_mapping[protein_col].nunique()

print("Genome annotation denominators")
print(f"Total gene models: {total_gene_models:,}")
print(f"HC gene models: {total_hc_gene_models:,}")
print(f"LC gene models: {total_lc_gene_models:,}")
print(f"Protein isoforms: {total_proteins:,}")

# -----------------------------
# 4. Load fully validated peptide projection rows
# -----------------------------
print("\nLoading fully validated rows from Step 11...")

header = pd.read_csv(sanity_file, nrows=0)

required_cols = [
    "Source",
    "Species",
    "Tissue",
    "Peptide",
    "ProteinID",
    gene_col,
    confidence_col,
    "Chromosome",
    "BED_block_count",
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

validated_tables = []
chunk_size = 100_000

for chunk_i, chunk in enumerate(
    pd.read_csv(
        sanity_file,
        usecols=required_cols,
        chunksize=chunk_size,
        low_memory=False
    ),
    start=1
):

    chunk = chunk[
        chunk["Sanity_check_status"].astype(str) == "passed"
    ].copy()

    if chunk.empty:
        continue

    chunk["Source_Tissue"] = (
        chunk["Source"].astype(str) + "_" + chunk["Tissue"].astype(str)
    )

    chunk["BED_block_count"] = pd.to_numeric(
        chunk["BED_block_count"],
        errors="coerce"
    )

    validated_tables.append(chunk)

if not validated_tables:
    raise ValueError(
        "No fully validated peptide rows were loaded from Step 11."
    )

validated_all = pd.concat(validated_tables, ignore_index=True)

print(f"Fully validated rows loaded for Step 16: {len(validated_all):,}")

# -----------------------------
# 5. Helper percentage function
# -----------------------------
def pct(numerator, denominator):
    if denominator == 0 or pd.isna(denominator):
        return pd.NA
    return round((numerator / denominator) * 100, 4)

# -----------------------------
# 6. HC/LC coverage metrics by source and tissue
# -----------------------------
records = []

for (source, tissue, source_tissue), group in validated_all.groupby(
    ["Source", "Tissue", "Source_Tissue"],
    dropna=False
):

    hc = group[group[confidence_col].astype(str).str.upper() == "HC"]
    lc = group[group[confidence_col].astype(str).str.upper() == "LC"]

    hc_unique_proteins = hc["ProteinID"].nunique()
    lc_unique_proteins = lc["ProteinID"].nunique()

    hc_unique_genes = hc[gene_col].nunique()
    lc_unique_genes = lc[gene_col].nunique()

    records.append({
        "Source": source,
        "Tissue": tissue,
        "Source_Tissue": source_tissue,

        "HC_unique_proteins": hc_unique_proteins,
        "LC_unique_proteins": lc_unique_proteins,
        "Total_unique_proteins": group["ProteinID"].nunique(),

        "HC_unique_gene_models": hc_unique_genes,
        "LC_unique_gene_models": lc_unique_genes,
        "Total_unique_gene_models": group[gene_col].nunique(),

        "HC_unique_peptides": hc["Peptide"].nunique(),
        "LC_unique_peptides": lc["Peptide"].nunique(),
        "Total_unique_peptides": group["Peptide"].nunique(),

        "Validated_BED_rows": len(group),
        "Multi_exon_peptide_rows": int((group["BED_block_count"] > 1).sum()),
        "Within_exon_peptide_rows": int((group["BED_block_count"] == 1).sum()),

        "Unique_chromosomes": group["Chromosome"].nunique()
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
# 7. Convert counts to coverage percentages
# -----------------------------
coverage["HC_protein_percent"] = (
    coverage["HC_unique_proteins"] / total_proteins
) * 100

coverage["LC_protein_percent"] = (
    coverage["LC_unique_proteins"] / total_proteins
) * 100

coverage["Total_protein_percent"] = (
    coverage["Total_unique_proteins"] / total_proteins
) * 100

coverage["HC_gene_model_percent"] = (
    coverage["HC_unique_gene_models"] / total_hc_gene_models
) * 100

coverage["LC_gene_model_percent"] = (
    coverage["LC_unique_gene_models"] / total_lc_gene_models
) * 100

coverage["Total_gene_model_percent"] = (
    coverage["Total_unique_gene_models"] / total_gene_models
) * 100

# Sort and export
coverage = coverage.sort_values(
    "Total_gene_model_percent",
    ascending=True
)

coverage.to_csv(step16_summary_out, index=False)

print(f"Saved Step 16 validated HC/LC coverage summary: {step16_summary_out}")

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
    ax.legend(title="Annotation confidence", loc="lower right")

    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"Figure saved: {output_path}")

# -----------------------------
# 9. Protein-level plot
# -----------------------------
coverage_protein_sorted = coverage.sort_values(
    "Total_protein_percent",
    ascending=True
)

plot_stacked_horizontal_bar(
    data=coverage_protein_sorted,
    value_cols=["HC_protein_percent", "LC_protein_percent"],
    labels=["HC", "LC"],
    title="Validated protein-level proteogenomic coverage by source and tissue",
    xlabel="Unique protein isoforms as % of total annotated protein isoforms",
    output_path=protein_plot_out
)

# -----------------------------
# 10. Gene-model coverage plot
# -----------------------------
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
    title="Validated gene-model proteogenomic coverage by source and tissue",
    xlabel="Supported gene models as % of annotated HC or LC gene models",
    output_path=gene_model_plot_out
)

display(coverage)