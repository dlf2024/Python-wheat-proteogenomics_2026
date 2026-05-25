#################### Wheat genome data ########################

# ============================================================
# Step 5 - Parse HC + LC GFF3 files and build protein-to-gene mapping table
# ============================================================

import pandas as pd
import numpy as np
import re

# -----------------------------
# 1. Input / output file names
# -----------------------------
hc_gff3 = "genome_annotation/iwgsc_refseqv2.1_annotation_200916_HC.gff3"
lc_gff3 = "genome_annotation/iwgsc_refseqv2.1_annotation_200916_LC.gff3"

features_out = "python_outputs/tables/wheat_gff3_parsed_features_HC_LC.csv"
mapping_out  = "python_outputs/tables/wheat_protein_gene_mapping_HC_LC.csv"
summary_out  = "python_outputs/tables/wheat_gff3_parsing_summary_HC_LC.csv"

# -----------------------------
# 2. Helper functions
# -----------------------------
def parse_attributes(attr_text):
    attrs = {}
    if pd.isna(attr_text):
        return attrs

    for item in str(attr_text).strip().split(";"):
        if not item.strip():
            continue
        if "=" in item:
            key, value = item.split("=", 1)
            attrs[key.strip()] = value.strip()
        else:
            attrs[item.strip()] = ""
    return attrs

def strip_prefix(value):
    if value is None or pd.isna(value):
        return np.nan
    value = str(value).strip()
    value = re.sub(r"^[A-Za-z_]+:", "", value)
    return value

def split_multi(value):
    if value is None or pd.isna(value):
        return []
    return [strip_prefix(x.strip()) for x in str(value).split(",") if x.strip()]

def gene_model_from_protein(protein_id):
    if protein_id is None or pd.isna(protein_id):
        return np.nan
    protein_id = str(protein_id).strip()
    return re.sub(r"\.\d+$", "", protein_id)

def normalise_feature_type(ftype):
    ftype = str(ftype)
    if ftype in {"mRNA", "transcript"}:
        return "transcript"
    return ftype

# -----------------------------
# 3. GFF3 parser
# -----------------------------
def parse_gff3(filepath, confidence_label):
    rows = []

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue

            parts = line.rstrip("\n").split("\t")
            if len(parts) != 9:
                continue

            seqid, source, feature_type, start, end, score, strand, phase, attributes = parts
            feature_type = normalise_feature_type(feature_type)
            attrs = parse_attributes(attributes)

            rows.append({
                "SeqID": seqid,
                "Source_gff": source,
                "FeatureType": feature_type,
                "Start": int(start),
                "End": int(end),
                "Score": score if score != "." else np.nan,
                "Strand": strand,
                "Phase": phase if phase != "." else np.nan,
                "Attributes": attributes,
                "Annotation_confidence": confidence_label,
                "ID_raw": attrs.get("ID", np.nan),
                "Parent_raw": attrs.get("Parent", np.nan),
                "Name": attrs.get("Name", np.nan),
                "biotype": attrs.get("biotype", attrs.get("gene_biotype", np.nan)),
                "protein_id_raw": attrs.get("protein_id", np.nan),
                "Derives_from_raw": attrs.get("Derives_from", np.nan),
            })

    df = pd.DataFrame(rows)

    df["ID"] = df["ID_raw"].apply(strip_prefix)
    df["Parent"] = df["Parent_raw"].apply(lambda x: ", ".join(split_multi(x)) if pd.notna(x) else np.nan)
    df["protein_id"] = df["protein_id_raw"].apply(strip_prefix)
    df["Derives_from"] = df["Derives_from_raw"].apply(lambda x: ", ".join(split_multi(x)) if pd.notna(x) else np.nan)

    return df

# -----------------------------
# 4. Parse HC + LC GFF3 files
# -----------------------------
hc_df = parse_gff3(hc_gff3, "HC")
lc_df = parse_gff3(lc_gff3, "LC")
features = pd.concat([hc_df, lc_df], ignore_index=True)

print(f"Parsed HC features: {hc_df.shape[0]:,}")
print(f"Parsed LC features: {lc_df.shape[0]:,}")
print(f"Combined features:  {features.shape[0]:,}")

features.to_csv(features_out, index=False)
print(f"Saved parsed feature table to: {features_out}")

# -----------------------------
# 5. Extract genes
# -----------------------------
genes = features[features["FeatureType"] == "gene"].copy()

genes = genes.rename(columns={
    "ID": "GeneModel",
    "SeqID": "Gene_Chromosome",
    "Start": "Gene_start",
    "End": "Gene_end",
    "Strand": "Gene_strand",
    "Name": "Gene_Name",
    "biotype": "Gene_biotype",
})

gene_cols = [
    "GeneModel", "Gene_Chromosome", "Gene_start", "Gene_end", "Gene_strand",
    "Annotation_confidence", "Gene_Name", "Gene_biotype"
]
genes = genes[gene_cols].drop_duplicates()

print(f"Gene rows: {genes.shape[0]:,}")

# -----------------------------
# 6. Extract transcripts
# -----------------------------
transcripts = features[features["FeatureType"] == "transcript"].copy()

transcripts = transcripts.rename(columns={
    "ID": "TranscriptID",
    "SeqID": "Transcript_Chromosome",
    "Start": "Transcript_start",
    "End": "Transcript_end",
    "Strand": "Transcript_strand",
    "Parent": "GeneModel",
    "Name": "Transcript_Name",
    "biotype": "Transcript_biotype",
})

tx_cols = [
    "TranscriptID", "GeneModel", "Transcript_Chromosome",
    "Transcript_start", "Transcript_end", "Transcript_strand",
    "Annotation_confidence", "Transcript_Name", "Transcript_biotype"
]
transcripts = transcripts[tx_cols].drop_duplicates()

print(f"Transcript rows: {transcripts.shape[0]:,}")

# -----------------------------
# 7. Extract CDS features and summarise by transcript
# -----------------------------
cds = features[features["FeatureType"] == "CDS"].copy()

# Parent of CDS is usually transcript ID
cds["TranscriptID"] = cds["Parent"].apply(
    lambda x: split_multi(x)[0] if pd.notna(x) and len(split_multi(x)) > 0 else np.nan
)

# Ensure compatible dtype before string assignment
cds["ProteinID"] = cds["protein_id"].astype("object")

missing_prot = cds["ProteinID"].isna() | (cds["ProteinID"].astype(str).str.strip() == "")
cds.loc[missing_prot, "ProteinID"] = cds.loc[missing_prot, "TranscriptID"].astype("object")

cds["GeneModel_from_protein"] = cds["ProteinID"].apply(gene_model_from_protein)
cds["CDS_nt_len"] = cds["End"] - cds["Start"] + 1

cds_summary = (
    cds
    .dropna(subset=["TranscriptID"])
    .groupby(["TranscriptID", "ProteinID", "GeneModel_from_protein", "Annotation_confidence"], dropna=False)
    .agg(
        CDS_feature_count=("FeatureType", "size"),
        CDS_start=("Start", "min"),
        CDS_end=("End", "max"),
        CDS_total_nt_length=("CDS_nt_len", "sum"),
        CDS_Chromosome=("SeqID", "first"),
        CDS_strand=("Strand", "first"),
        CDS_phase_values=("Phase", lambda s: "; ".join(sorted({str(x) for x in s if pd.notna(x)}))),
    )
    .reset_index()
)

print(f"CDS summary rows: {cds_summary.shape[0]:,}")

# -----------------------------
# 8. Merge transcript + gene + CDS information
# -----------------------------
mapping = cds_summary.merge(
    transcripts,
    on=["TranscriptID", "Annotation_confidence"],
    how="left"
)

# Prefer transcript-linked GeneModel, fallback to protein-derived GeneModel
mapping["GeneModel"] = np.where(
    mapping["GeneModel"].notna() & (mapping["GeneModel"].astype(str).str.strip() != ""),
    mapping["GeneModel"],
    mapping["GeneModel_from_protein"]
)

mapping = mapping.merge(
    genes,
    on=["GeneModel", "Annotation_confidence"],
    how="left"
)

# Build final chromosome/strand columns explicitly
mapping["Chromosome"] = np.where(
    mapping["Gene_Chromosome"].notna(),
    mapping["Gene_Chromosome"],
    np.where(
        mapping["Transcript_Chromosome"].notna(),
        mapping["Transcript_Chromosome"],
        mapping["CDS_Chromosome"]
    )
)

mapping["Strand"] = np.where(
    mapping["Gene_strand"].notna(),
    mapping["Gene_strand"],
    np.where(
        mapping["Transcript_strand"].notna(),
        mapping["Transcript_strand"],
        mapping["CDS_strand"]
    )
)

mapping["Protein_length_aa_from_CDS"] = np.where(
    pd.to_numeric(mapping["CDS_total_nt_length"], errors="coerce").notna(),
    (pd.to_numeric(mapping["CDS_total_nt_length"], errors="coerce") / 3).round(2),
    np.nan
)

final_cols = [
    "ProteinID",
    "GeneModel",
    "TranscriptID",
    "Chromosome",
    "Strand",
    "Gene_start",
    "Gene_end",
    "Transcript_start",
    "Transcript_end",
    "CDS_start",
    "CDS_end",
    "CDS_feature_count",
    "CDS_total_nt_length",
    "Protein_length_aa_from_CDS",
    "CDS_phase_values",
    "Annotation_confidence",
    "Gene_Name",
    "Gene_biotype",
    "Transcript_Name",
    "Transcript_biotype",
]
mapping = mapping[final_cols].drop_duplicates()

# -----------------------------
# 9. Add mapping status flags
# -----------------------------
mapping["ProteinID_found_in_GFF3"] = mapping["ProteinID"].notna()
mapping["GeneModel_found_in_GFF3"] = mapping["GeneModel"].notna()
mapping["Has_gene_coordinates"] = mapping["Gene_start"].notna() & mapping["Gene_end"].notna()
mapping["Has_transcript_coordinates"] = mapping["Transcript_start"].notna() & mapping["Transcript_end"].notna()

sort_cols = [c for c in ["Annotation_confidence", "Chromosome", "Gene_start", "ProteinID"] if c in mapping.columns]
mapping = mapping.sort_values(sort_cols).reset_index(drop=True)

mapping.to_csv(mapping_out, index=False)
print(f"Saved protein-to-gene mapping table to: {mapping_out}")

# -----------------------------
# 10. Summary tables
# -----------------------------
summary_rows = [
    {"Metric": "Parsed_HC_features", "Value": int(hc_df.shape[0])},
    {"Metric": "Parsed_LC_features", "Value": int(lc_df.shape[0])},
    {"Metric": "Combined_features", "Value": int(features.shape[0])},
    {"Metric": "Unique_genes", "Value": int(genes["GeneModel"].nunique())},
    {"Metric": "Unique_transcripts", "Value": int(transcripts["TranscriptID"].nunique())},
    {"Metric": "Unique_proteins_in_mapping", "Value": int(mapping["ProteinID"].nunique())},
    {"Metric": "Unique_gene_models_in_mapping", "Value": int(mapping["GeneModel"].nunique())},
    {"Metric": "Rows_with_gene_coordinates", "Value": int(mapping["Has_gene_coordinates"].sum())},
    {"Metric": "Rows_with_transcript_coordinates", "Value": int(mapping["Has_transcript_coordinates"].sum())},
]

if "Annotation_confidence" in mapping.columns:
    conf_counts = mapping["Annotation_confidence"].value_counts(dropna=False).to_dict()
    for k, v in conf_counts.items():
        summary_rows.append({"Metric": f"Mapping_rows_{k}", "Value": int(v)})

summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(summary_out, index=False)

# -----------------------------
# 11. Print summary
# -----------------------------
print("\n===== GFF3 PARSING SUMMARY =====")
display(summary_df)

print("\nExample protein-to-gene mappings:")
display(mapping.head(10))

print("\nExample parsed gene features:")
display(genes.head(5))

print("\nExample parsed transcript features:")
display(transcripts.head(5))

print("\nExample CDS summary:")
display(cds_summary.head(5))