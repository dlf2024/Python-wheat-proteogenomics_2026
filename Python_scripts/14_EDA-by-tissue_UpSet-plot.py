# ============================================================
# Step 17 — EDA: Tissue overlap using UpSet plots
# Fully validated rows only
# Translation-validated + sanity-check-passed projections
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
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

# Step 11 output: translation-validated rows with sanity-check status
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

protein_upset_out = figures_dir / "step17_upsetplot_tissue_overlap_validated_proteins.png"
peptide_upset_out = figures_dir / "step17_upsetplot_tissue_overlap_validated_peptides.png"
gene_upset_out = figures_dir / "step17_upsetplot_tissue_overlap_validated_gene_models.png"

step17_summary_out = tables_dir / "wheat_tissue_overlap_validated_summary_step17.csv"

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )

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
# 3. Load fully validated peptide projection rows
# -----------------------------
print("\nLoading fully validated rows from Step 11...")

header = pd.read_csv(sanity_file, nrows=0)

gene_col = "GeneModel" if "GeneModel" in header.columns else "GeneID"

usecols_needed = [
    "Source",
    "Tissue",
    "ProteinID",
    "Peptide",
    gene_col,
    "Sanity_check_status"
]

missing_cols = [
    col for col in usecols_needed
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
        usecols=usecols_needed,
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
        chunk["Source"].astype(str) + "_" +
        chunk["Tissue"].astype(str)
    )

    validated_tables.append(chunk)

if not validated_tables:
    raise ValueError(
        "No fully validated peptide rows were loaded from Step 11."
    )

validated_all = pd.concat(validated_tables, ignore_index=True)

print(f"Fully validated rows loaded for Step 17: {len(validated_all):,}")

# -----------------------------
# 4. Build overlap dictionaries
# -----------------------------
protein_contents = {}
peptide_contents = {}
gene_contents = {}

for tissue, group in validated_all.groupby("Source_Tissue", dropna=False):

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
    title="Top tissue intersections of validated protein isoforms",
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
    title="Top tissue intersections of validated peptide sequences",
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
    title="Top tissue intersections of validated gene models",
    output_path=gene_upset_out,
    facecolor=brand_colours["gold"],
    max_subset_rank=40,
    min_subset_size=50
)

# -----------------------------
# 10. Generate overlap summary table
# -----------------------------
summary_records = []

for tissue, group in validated_all.groupby("Source_Tissue", dropna=False):

    summary_records.append({
        "Source_Tissue": tissue,
        "Validated_BED_rows": len(group),
        "Unique_validated_proteins": group["ProteinID"].nunique(),
        "Unique_validated_peptides": group["Peptide"].nunique(),
        "Unique_validated_gene_models": group[gene_col].nunique()
    })

step17_summary = pd.DataFrame(summary_records)

step17_summary = step17_summary.sort_values(
    "Unique_validated_gene_models",
    ascending=False
)

step17_summary.to_csv(step17_summary_out, index=False)

print(f"\nStep 17 summary saved: {step17_summary_out}")

display(step17_summary)