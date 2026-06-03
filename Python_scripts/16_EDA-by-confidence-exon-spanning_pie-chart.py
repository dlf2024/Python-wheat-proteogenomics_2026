# ============================================================
# Step 23 — EDA: Pie charts of validated peptide evidence by confidence level and exon structure
# Uses all-tissue combined non-redundant validated peptide projections
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
# all-tissue combined, non-redundant, translation-validated + sanity-passed projections
combined_validated_file = tables_dir / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv"

# Protein-to-gene mapping table used to recover HC/LC annotation confidence if needed
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

figure_out = figures_dir / "step23_validated_peptides_confidence_and_exon_structure_pies.png"
summary_out = tables_dir / "wheat_validated_peptides_confidence_and_exon_structure_summary_step23.csv"

if not combined_validated_file.exists():
    raise FileNotFoundError(
        f"Step 13 combined non-redundant validated peptide table not found:\n"
        f"{combined_validated_file}\n\n"
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
    "HC": "#3F007E",              # dark purple
    "LC": "#FF3399",              # pink
    "Within-exon": "#FFC000",     # yellow-gold
    "Exon-spanning": "#E6CDFF"    # soft lavender
}

# -----------------------------
# 3. Load data
# -----------------------------
data = pd.read_csv(combined_validated_file, low_memory=False)

protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    low_memory=False
)

protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

required_combined_cols = [
    "Peptide",
    protein_col,
    "BED_block_count"
]

missing_combined_cols = [
    col for col in required_combined_cols
    if col not in data.columns
]

if missing_combined_cols:
    raise KeyError(
        f"Missing required column(s) in Step 13 combined table: {missing_combined_cols}"
    )

# -----------------------------
# 4. Add annotation confidence if needed
# -----------------------------
if confidence_col not in data.columns:

    if protein_col not in protein_mapping.columns:
        raise KeyError(
            f"Missing '{protein_col}' in protein-gene mapping table."
        )

    if confidence_col not in protein_mapping.columns:
        raise KeyError(
            f"Missing '{confidence_col}' in protein-gene mapping table."
        )

    confidence_lookup = (
        protein_mapping[[protein_col, confidence_col]]
        .dropna(subset=[protein_col, confidence_col])
        .drop_duplicates(subset=[protein_col])
        .copy()
    )

    data = data.merge(
        confidence_lookup,
        on=protein_col,
        how="left"
    )

data[confidence_col] = (
    data[confidence_col]
    .astype(str)
    .str.upper()
)

data = data[
    data[confidence_col].isin(["HC", "LC"])
].copy()

# -----------------------------
# 5. Define exon-structure class
# -----------------------------
data["BED_block_count"] = pd.to_numeric(
    data["BED_block_count"],
    errors="coerce"
)

data = data.dropna(
    subset=["BED_block_count", confidence_col, "Peptide"]
).copy()

data["BED_block_count"] = data["BED_block_count"].astype(int)

data["Exon_structure"] = data["BED_block_count"].apply(
    lambda x: "Exon-spanning" if x > 1 else "Within-exon"
)

print(f"Non-redundant validated peptide projection rows loaded: {len(data):,}")
print("\nAnnotation confidence counts:")
display(data[confidence_col].value_counts().reset_index(name="Rows"))

print("\nExon-structure counts:")
display(data["Exon_structure"].value_counts().reset_index(name="Rows"))

# -----------------------------
# 6. Build summary table
# -----------------------------
summary = (
    data
    .groupby([confidence_col, "Exon_structure"], dropna=False)
    .agg(
        Nonredundant_validated_rows=("Peptide", "size"),
        Unique_peptide_sequences=("Peptide", "nunique"),
        Unique_proteins=("ProteinID", "nunique"),
        Median_BED_block_count=("BED_block_count", "median"),
        Mean_BED_block_count=("BED_block_count", "mean"),
        Max_BED_block_count=("BED_block_count", "max")
    )
    .reset_index()
)

# Add totals and percentages within annotation confidence
confidence_totals = (
    data
    .groupby(confidence_col, dropna=False)
    .agg(
        Total_rows_within_confidence=("Peptide", "size"),
        Total_unique_peptides_within_confidence=("Peptide", "nunique")
    )
    .reset_index()
)

summary = summary.merge(
    confidence_totals,
    on=confidence_col,
    how="left"
)

summary["Percent_rows_within_confidence"] = (
    summary["Nonredundant_validated_rows"] /
    summary["Total_rows_within_confidence"] *
    100
).round(4)

# Add global totals by confidence class
global_confidence_summary = (
    data
    .groupby(confidence_col, dropna=False)
    .agg(
        Nonredundant_validated_rows=("Peptide", "size"),
        Unique_peptide_sequences=("Peptide", "nunique"),
        Unique_proteins=("ProteinID", "nunique")
    )
    .reset_index()
)

global_total_rows = len(data)
global_total_unique_peptides = data["Peptide"].nunique()

global_confidence_summary["Exon_structure"] = "All"
global_confidence_summary["Total_rows_within_confidence"] = global_confidence_summary["Nonredundant_validated_rows"]
global_confidence_summary["Total_unique_peptides_within_confidence"] = global_confidence_summary["Unique_peptide_sequences"]
global_confidence_summary["Percent_rows_within_confidence"] = 100.0
global_confidence_summary["Percent_rows_overall"] = (
    global_confidence_summary["Nonredundant_validated_rows"] /
    global_total_rows *
    100
).round(4)

summary["Percent_rows_overall"] = (
    summary["Nonredundant_validated_rows"] /
    global_total_rows *
    100
).round(4)

# Align columns and combine
for col in ["Median_BED_block_count", "Mean_BED_block_count", "Max_BED_block_count"]:
    if col not in global_confidence_summary.columns:
        global_confidence_summary[col] = pd.NA

# Avoid FutureWarning by removing empty/all-NA columns before concatenation
summary_parts = [
    global_confidence_summary[summary.columns],
    summary
]

summary_parts = [
    df.dropna(axis=1, how="all")
    for df in summary_parts
    if not df.empty
]

summary = pd.concat(
    summary_parts,
    ignore_index=True
)

summary.to_csv(summary_out, index=False)

print(f"\nStep 23 summary saved: {summary_out}")
display(summary)

# -----------------------------
# 7. Pie chart helper
# -----------------------------
def autopct_with_counts(values):
    """
    Return an autopct function that displays percentage and raw count.
    """
    total = sum(values)

    def inner_autopct(pct):
        count = int(round(pct * total / 100.0))
        return f"{pct:.1f}%\n(n={count:,})"

    return inner_autopct


def make_pie(ax, counts, labels, colours, title):
    """
    Create a labelled pie chart.
    """

    values = [counts.get(label, 0) for label in labels]

    if sum(values) == 0:
        ax.text(
            0.5,
            0.5,
            "No data",
            ha="center",
            va="center",
            fontsize=12
        )
        ax.set_title(title, fontsize=13, fontweight="bold")
        ax.axis("off")
        return

    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        colors=colours,
        autopct=autopct_with_counts(values),
        startangle=90,
        counterclock=False,
        wedgeprops={
            "edgecolor": "white",
            "linewidth": 1.5
        },
        textprops={
            "fontsize": 10
        }
    )

    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight("bold")
        autotext.set_color("white")

    ax.set_title(
        title,
        fontsize=13,
        fontweight="bold",
        pad=12
    )

    ax.axis("equal")

# -----------------------------
# 8. Prepare counts for pie charts
# -----------------------------
confidence_counts = (
    data[confidence_col]
    .value_counts()
    .to_dict()
)

hc_exon_counts = (
    data.loc[data[confidence_col] == "HC", "Exon_structure"]
    .value_counts()
    .to_dict()
)

lc_exon_counts = (
    data.loc[data[confidence_col] == "LC", "Exon_structure"]
    .value_counts()
    .to_dict()
)

# -----------------------------
# 9. Plot three pie charts
# -----------------------------
fig, axes = plt.subplots(
    1,
    3,
    figsize=(16, 5)
)

make_pie(
    ax=axes[0],
    counts=confidence_counts,
    labels=["HC", "LC"],
    colours=[brand_colours["HC"], brand_colours["LC"]],
    title="Validated peptide projections\nby annotation confidence"
)

make_pie(
    ax=axes[1],
    counts=hc_exon_counts,
    labels=["Within-exon", "Exon-spanning"],
    colours=[brand_colours["Within-exon"], brand_colours["Exon-spanning"]],
    title="HC projections\nby exon structure"
)

make_pie(
    ax=axes[2],
    counts=lc_exon_counts,
    labels=["Within-exon", "Exon-spanning"],
    colours=[brand_colours["Within-exon"], brand_colours["Exon-spanning"]],
    title="LC projections\nby exon structure"
)

fig.suptitle(
    "Validated non-redundant peptide evidence by confidence level and exon structure",
    fontsize=16,
    fontweight="bold",
    y=1.05
)

plt.tight_layout()

plt.savefig(
    figure_out,
    dpi=300,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"Figure saved: {figure_out}")