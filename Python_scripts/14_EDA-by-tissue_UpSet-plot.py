# ============================================================
# Step 16 — EDA: Tissue overlap using UpSet plots
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from upsetplot import UpSet, from_contents
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="upsetplot")

# -----------------------------
# 1. Paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")

figures_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

protein_upset_out = figures_dir / "step16_upsetplot_tissue_overlap_proteins.png"
peptide_upset_out = figures_dir / "step16_upsetplot_tissue_overlap_peptides.png"
gene_upset_out = figures_dir / "step16_upsetplot_tissue_overlap_gene_models.png"

step16_summary_out = tables_dir / "wheat_tissue_overlap_summary_step16.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "dark_purple": "#3F007E",
    "pink": "#FF3399",
    "gold": "#FFC000",
    "lavender": "#E6CDFF"
}

# -----------------------------
# 3. Load projected peptide tables
# Memory-safe: only load columns required for Step 16
# -----------------------------
projected_tables = []

usecols_needed = [
    "Projection_status",
    "ProteinID",
    "Peptide",
    "GeneModel",
    "GeneID"
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
        usecols=lambda col: col in usecols_needed,
        low_memory=False
    )

    data = data[data["Projection_status"] == "projected"].copy()

    data["Source"] = row["Source"]
    data["Species"] = row["Species"]
    data["Tissue"] = row["Tissue-Raw-Code"]
    data["Source_Tissue"] = (
        data["Source"].astype(str) + "_" +
        data["Tissue"].astype(str)
    )

    projected_tables.append(data)

projected_all = pd.concat(projected_tables, ignore_index=True)

print(f"Projected rows loaded: {len(projected_all):,}")

# -----------------------------
# 4. Build overlap dictionaries
# -----------------------------
gene_col = "GeneModel" if "GeneModel" in projected_all.columns else "GeneID"

protein_contents = {}
peptide_contents = {}
gene_contents = {}

for tissue, group in projected_all.groupby("Source_Tissue", dropna=False):

    protein_contents[tissue] = set(
        group["ProteinID"].dropna().astype(str)
    )

    peptide_contents[tissue] = set(
        group["Peptide"].dropna().astype(str)
    )

    gene_contents[tissue] = set(
        group[gene_col].dropna().astype(str)
    )

# -----------------------------
# 5. Create UpSet-compatible data
# -----------------------------
protein_upset_data = from_contents(protein_contents)
peptide_upset_data = from_contents(peptide_contents)
gene_upset_data = from_contents(gene_contents)

# -----------------------------
# 6. Plot helper function
# -----------------------------
def create_upset_plot(
    upset_data,
    title,
    output_path,
    facecolor,
    max_subset_rank=40,
    min_subset_size=50
):
    """
    Create a manageable UpSet plot by showing only the largest intersections.
    This avoids excessively large figures when many tissues are included.
    """

    fig = plt.figure(figsize=(16, 8))

    upset = UpSet(
        upset_data,
        subset_size="count",
        show_counts=True,
        sort_by="cardinality",
        facecolor=facecolor,
        min_subset_size=min_subset_size,
        max_subset_rank=max_subset_rank
    )

    upset.plot(fig=fig)

    plt.suptitle(title, fontsize=14, fontweight="bold")

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close(fig)

    print(f"Figure saved: {output_path}")
    
# -----------------------------
# 7. Protein overlap UpSet plot
# -----------------------------
create_upset_plot(
    upset_data=protein_upset_data,
    title="Top tissue intersections of projected protein isoforms",
    output_path=protein_upset_out,
    facecolor=brand_colours["dark_purple"],
    max_subset_rank=40,
    min_subset_size=50
)

# -----------------------------
# 8. Peptide overlap UpSet plot
# -----------------------------
create_upset_plot(
    upset_data=peptide_upset_data,
    title="Top tissue intersections of projected peptide sequences",
    output_path=peptide_upset_out,
    facecolor=brand_colours["pink"],
    max_subset_rank=40,
    min_subset_size=50
)

# -----------------------------
# 9. Gene model overlap UpSet plot
# -----------------------------
create_upset_plot(
    upset_data=gene_upset_data,
    title="Top tissue intersections of projected gene models",
    output_path=gene_upset_out,
    facecolor=brand_colours["gold"],
    max_subset_rank=40,
    min_subset_size=50
)

# -----------------------------
# 10. Generate overlap summary table
# -----------------------------
summary_records = []

for tissue, group in projected_all.groupby("Source_Tissue", dropna=False):

    summary_records.append({
        "Source_Tissue": tissue,
        "Unique_projected_proteins": group["ProteinID"].nunique(),
        "Unique_projected_peptides": group["Peptide"].nunique(),
        "Unique_projected_gene_models": group[gene_col].nunique()
    })

step16_summary = pd.DataFrame(summary_records)

step16_summary = step16_summary.sort_values(
    "Unique_projected_gene_models",
    ascending=False
)

step16_summary.to_csv(step16_summary_out, index=False)

print(f"\nStep 16 summary saved: {step16_summary_out}")

display(step16_summary)