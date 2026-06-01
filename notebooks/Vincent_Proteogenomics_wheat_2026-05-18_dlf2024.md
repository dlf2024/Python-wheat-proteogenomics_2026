# Community Resource: A Genome-Guided Extension of Large-Scale Wheat Proteogenomics

---

## Author   
Dr Delphine Vincent  
_website:_ https://dlf2024.github.io/  
_github:_ https://github.com/dlf2024      
_Date:_ 18/05/2026

---

## Rationale  
This project aims at validating gene model annotations in bread wheat (_Triticum aestivum_, IWGSC RefSeq v2.1) using a proteogenomics strategy by identifying peptides/proteins in various wheat tissues from public proteomics experiments and aligning them along the genome.     
This study follows on our previous proteogenomics project from 2024 in which peptides identified in public repositories MSV000090572 and PXD004720 were aligned along the wheat genome using a tBLASTn strategy (Citation: Vincent, D.; Appels, R. (2024) Community Resource: Large-Scale Proteogenomics to Refine Wheat Genome Annotations. Int. J. Mol. Sci. 2024, 25, 8614. https://doi.org/10.3390/ijms25168614).    
The peptide alignments along bread wheat genome are publicly available from the Apollo JBrowse service (https://bread-wheat-um.genome.edu.au/apollo/49826/jbrowse/index.html).   

---

## Steps  
- 1: Data retrieval and extraction (LFTP via Ubuntu Unix outside of this notebook)
- 2: Data conversion (using MSConvert GUI outside of this notebook)
- 3: Protein database creation with decoy (using Galaxy Proteomics platform outside of this notebook)
- 4: Peptide/Protein search (using FragPipe program outside of this notebook)
- 5: Build a protein-to-gene mapping table (this notebook)
- 6: FragPipe Output Annotation and Quality Summary (this notebook)
- 7: Build non-contaminant peptide–protein evidence tables (this notebook)
- 8: Map proteins to gene models using the GFF3-derived mapping table (this notebook)
- 9: Project peptide positions from proteins onto genomic coordinates (this notebook)
- 10: Positional validation of annotation-guided peptide genome projections (this notebook)
- 11: Export all tissues BED6/BED12 files for JBrowse (this notebook)
- 12: Create a single non-redundant combined BED track (this notebook)
- 13: Generate tissue/protein/gene/isoform summary tables (this notebook)
- 14: Prepare BED Files for Apollo/JBrowse Public Upload (this notebook)
- 15: EDA: HC and LC Proteogenomic Coverage by Tissue (this notebook)
- 16: EDA: Tissue Overlap Using UpSet Plots (this notebook)
- 17: EDA: Peptide Support per Gene Model (this notebook)
- 18: EDA: Peptide Length, Probability, and Charge by Annotation Confidence  (this notebook)
- 19: EDA: Protein Length versus Peptide Support (this notebook)
- 20: EDA: Chromosomal Distribution of Peptide Genomic Start Positions (this notebook)
- 21: EDA: Circular Tissue-Level Peptide Genome Map (this notebook)
- 22: EDA: Circular Confidence-Level Peptide Genome Map (this notebook)
- 23: Combine Python workflow Summary Tables at Source/Tissue Level (this notebook)
- 25: Sanity Checks for Annotation-Guided Peptide Genome Projections (this notebook)
- 26: Generate Sanity-Validated BED Files for Apollo/JBrowse Upload (this notebook)
- 27: Create Non-Redundant Combined Validated BED Tracks (this notebook)
- 28: Prepare manuscript Table 1 summary statistics (this notebook)

---

## Wheat Genome Annotation Source  
- Citation: The International Wheat Genome Sequencing Consortium (IWGSC); Appels, R. et al. (2018) Shifting the Limits in Wheat Research and Breeding Using a Fully Annotated Reference Genome. Science, 361, eaar7191. https://doi.org/10.1126/science.aar7191  
- IWGSC URL: https://urgi.versailles.inrae.fr/download/iwgsc/IWGSC_RefSeq_Annotations/v2.1/
- Data files:
  - iwgsc_refseqv2.1_annotation_200916_LC.gff3 (genome annotations of low confidence (LC) gene models)
  - iwgsc_refseqv2.1_annotation_200916_HC.gff3 (genome annotation of high confidence (HC) gene models)
  - iwgsc_refseqv2.1_functional_annotation.csv (gene model functional annotations)
  - iwgsc_refseqv2.1_annotation_200916_HC_pep.fasta (AA sequences of HC gene models)
  - iwgsc_refseqv2.1_annotation_200916_LC_pep.fasta (AA sequences of LC gene models)

---

## MS-Proteomics Raw Data Sources 

### Liu et al 2025 (PXD050500)  
- Citation: Liu S, et al (2025) A telomere-to-telomere genome assembly coupled with multi-omic data provides insights into the evolution of hexaploidy bread wheat. Nature Genetics, 57: 1008-1020. https://doi.org/10.1038/s41588-025-02137-x   
- ProteomeXchange URL: https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD050500   
- PRIDE URL: https://www.ebi.ac.uk/pride/archive/projects/PXD050500    
- FTP URL: https://ftp.pride.ebi.ac.uk/pride/data/archive/2024/12/PXD050500/   
- Data files: 180 .d files (timsTOF Pro mass spectrometer, Bruker Daltonics) - 400 GB
- Tissues: 
  - node (60 fractions)
  - coleoptile (60 fractions)
  - radicle (60 fractions)

### Vincent et al 2023 (MSV000090572)    
- Citation: Vincent, D. et al. (2023) A Community Resource to Mass Explore the Wheat Grain Proteome and Its Application to the Late-Maturity Alpha-Amylase (LMA) Problem. GigaScience, 12, giad084. https://doi.org/10.1093/gigascience/giad084     
- MassIVE URL: https://massive.ucsd.edu/ProteoSAFe/result.jsp?task=9e8c4c3c9d924de8800237e7e828e1d9&view=advanced_view#%7B%7D   
- FTP URL: ftp://massive-ftp.ucsd.edu/v05/MSV000090572/
- Data files: 62 .raw files (LTQ Orbitrap Elite mass analyser, Thermo Scientific) - 12 GB
- Tissues:
  - stored grains (mature, harvested grains stored in optimum conditions)

### Duncan et al 2017 (PXD004720)     
- Citation: Duncan, O. et al (2017) Resource: Mapping the Triticum aestivum Proteome. Plant J., 89, 601-616. https://doi.org/10.1111/tpj.13402      
- ProteomeXchange URL: https://proteomecentral.proteomexchange.org/ui?pxid=PXD004720    
- PRIDE URL: https://www.ebi.ac.uk/pride/archive/projects/PXD004720   
- FTP URL: https://ftp.pride.ebi.ac.uk/pride/data/archive/2016/11/PXD004720/
- Data files: 335 .mzXML files (QTOF, Agilent) - 600 GB
- Tissues:
  - anther (12 fractions)
  - boot (12 fractions)
  - coleoptile (12 fractions)
  - embryo (12 fractions)
  - endosperm (12 fractions)
  - glume (12 fractions)
  - grain-zadoks-70 (12 fractions)
  - grain-zadoks-71 (12 fractions)
  - grain-zadoks-75 (12 fractions)
  - grain-zadoks-83 (12 fractions)
  - grain-zadoks-87 (12 fractions)
  - leaf-flag-mature (12 fractions)
  - leaf-flag-senescing (12 fractions)
  - leaf-flag-young (12 fractions)
  - lemma (12 fractions)
  - node (12 fractions)
  - node_secretion (12 fractions)
  - palea (11 fractions)
  - pericarp (12 fractions)
  - pollen (12 fractions)
  - rachilla (12 fractions)
  - radicle (12 fractions)
  - root-mature (12 fractions)
  - root-secretion (12 fractions)
  - root-tip (12 fractions)
  - root-vasculature (12 fractions)
  - spike-immature (12 fractions)
  - stem (12 fractions)

---

## Computational environment  
- Windows 10
- WSL2 Ubuntu 24.04
- Python 3.12
- JupyterLab 4.3.4
- FragPipe 24.0
- MSFragger 4.4.1
- ProteoWizard MSConvert 3.0
- Galaxy Proteomics platform

---

## Folder architecture  
project/   
├── raw_data/    
├── mzML/    
├── genome_annotation/    
├── protein_database/    
├── fragpipe_results/    
├── tblastn_results/  
├── python_outputs/    
│      ├── bed/    
│      ├── tables/    
│      └── figures/  

---

## AI-assisted workflow development   
Portions of the Python workflow, code optimisation, debugging assistance, and markdown documentation were developed with the assistance of OpenAI ChatGPT (GPT-5 series) under the direction and scientific supervision of the author.   
All computational workflows, parameter selections, biological interpretations, quality control, and final validation were performed and verified by the author.  

---

## Apollo JBrowse Deployment

Projected peptide alignments generated from this workflow are publicly available through the Apollo JBrowse genome browser:  

https://bread-wheat-um.genome.edu.au/apollo/49826/jbrowse/index.html

Tracks include:
- annotation-guided peptide genome projections
- BED6 and BED12 visualisation tracks
- tissue-specific peptide mappings
- non-redundant combined peptide tracks 

# Step 1 — Data Retrieval and Extraction

Large-scale public proteomics datasets were retrieved from the PRIDE and MassIVE repositories using the Linux command-line utility `lftp` executed within a Ubuntu WSL2 environment under Windows 11. Due to the large data volume (>1 TB total), data management and storage optimisation were critical considerations throughout the workflow.

---

## Computational environment

### Operating system
- Windows 11 Pro
- WSL2 Ubuntu Linux

### Software
- `lftp`
- `7zip`
- Windows PowerShell

### Install required Linux utilities

```bash
sudo apt update
sudo apt install lftp p7zip-full
```

---

## Data retrieval using lftp (e.g. PXD050500)

### Create new directory to store files

```bash
mkdir -p /mnt/e/wheat_proteogenomics/PXD050500
cd /mnt/e/wheat_proteogenomics/PXD050500
```

### Connect to public repository (PRIDE)

```bash
lftp ftp.pride.ebi.ac.uk
```

### Inside the `lftp` session, download files

```bash
cd /pride/data/archive/2024/12/PXD050500
mirror --verbose .
exit
```

---

## Monitoring storage usage in WSL2

Large downloads can rapidly consume WSL2 virtual disk space.

### Check Linux folder size

```bash
du -sh /root/wheat_pride/PXD004720
```

### Check available disk space

```bash
df -h
```

### Cleaning temporary files

```bash
rm -rf /tmp/*
```

---

## Archive extraction

### Test archive integrity before extraction

```bash
7z t filename.rar
```

### Extract archive

```bash
7z x filename.rar
```

### Remove extracted archives no longer needed

```bash
rm filename.rar
```

---

## WSL2 disk cleanup

After deleting large datasets, WSL2 virtual disks may still occupy substantial space on the Windows drive.

### Shutdown WSL2

```powershell
wsl --shutdown
```

### Locate the virtual disk

```powershell
Get-ChildItem "$env:LOCALAPPDATA\Packages" -Recurse -Filter ext4.vhdx
```

---

## Notes

- Download times varied from several hours to multiple days depending on repository speed and internet bandwidth.
- Stable internet connection and uninterrupted power supply were strongly recommended.
- External SSD storage substantially improved workflow efficiency compared to mechanical HDD devices.

# Step 2 — Data Conversion using MSConvert

Some raw mass spectrometry files required conversion into the open standard `.mzML` format prior to peptide identification analysis in FragPipe. File conversion was performed using the ProteoWizard software suite (`MSConvert GUI`) under Windows 11.

### Software
- ProteoWizard MSConvert
- URL: https://proteowizard.sourceforge.io/

---

## Input formats

### PXD004720
- Input format: `.mzXML`
- Instrument: Agilent QTOF

### MSV000090572
- Input format: `.raw`
- Instrument: Thermo Orbitrap Elite

### PXD050500
- Input format: `.d`
- Instrument: Bruker timsTOF Pro
- No conversion required for FragPipe analysis

---

## MSConvert GUI workflow

### 1. Launch MSConvert GUI

Open:
```text
ProteoWizard → MSConvert
```

### 2. Select input files

- Click `Browse`
- Select raw data files
- Add files to processing queue

### 3. Select output directory

Choose destination folder for converted files.

Example:
```text
E:\wheat_proteogenomics\PXD004720\mzML\
```

---

## Recommended conversion settings

### Output format
```text
mzML
```

### Binary encoding precision
```text
64-bit
```

### Compression
```text
zlib compression
```

### Peak picking
```text
Vendor peak picking
```

### Use zlib compression
```text
Enabled
```

### Write index
```text
Enabled
```

### TPP compatibility
```text
Enabled
```

---

## Start conversion

Click:
```text
Start
```

Converted `.mzML` files were subsequently used as input for FragPipe peptide identification workflows.

---

## Notes

- File conversion duration depended on instrument type and file size.
- Some Agilent `.mzXML` files from PXD004720 were unreadable by FragPipe and required reconversion using MSConvert.
- Output `.mzML` files substantially increased compatibility and stability during downstream peptide identification analyses.

# Step 3 — FASTA Database Creation

A combined target-decoy protein database was created using Galaxy Proteomics by merging high-confidence (HC) and low-confidence (LC) wheat protein annotations together with the common Repository of Adventitious Proteins (cRAP) contaminant database.

## Wheat protein sequence source

- IWGSC URL:
  https://urgi.versailles.inrae.fr/download/iwgsc/IWGSC_RefSeq_Annotations/v2.1/

### Input FASTA files

```text
iwgsc_refseqv2.1_annotation_200916_HC_pep.fasta
iwgsc_refseqv2.1_annotation_200916_LC_pep.fasta
```

---

## Software

### Galaxy Proteomics platform

- Galaxy URL:
  https://proteomics.usegalaxy.eu/


---

## Upload wheat FASTA files

### Open tool

```text
Upload Data
```

### Workflow

- Click `Choose local file`
- Select HC and LC FASTA files
- Click `Start`

---

## Download cRAP contaminant database

The cRAP database contains common mass spectrometry contaminants such as keratins and trypsin.

### Open tool

```text
Protein Database Downloader
```

### Settings

```text
Database = cRAP (contaminants)
```

### Run tool

Click:

```text
Run Tool
```

---

## Merge FASTA databases and remove duplicate entries

### Open tool

```text
FASTA Merge Files and Filter Unique Sequences
```

### Settings

#### Merge strategy

```text
Merge all FASTAs (always output a single FASTA)
```

#### Input files

```text
HC + LC + cRAP FASTA files
```

#### Duplicate filtering mode

```text
Accession Only
```

#### Parsing rule

```text
^>([^ ]+).*$
```

### Run tool

Click:

```text
Run Tool
```

---

## Create decoy database

A reverse-sequence decoy database was generated for false discovery rate (FDR) estimation during peptide identification.

### Open tool

```text
Create Decoy Database (reverse)
```

### Settings

#### Include original sequences

```text
Yes
```

#### Decoy prefix

```text
decoy_
```

### Run tool

Click:

```text
Run Tool
```

---

## Download final protein database

Download the generated target-decoy FASTA database locally.

### Final database filename

```text
iwgsc_refseqv2.1_annotation_200916_HC_LC_pep_cRAP_with_DECOY.fasta
```

---

## Notes

- HC = high-confidence gene models.
- LC = low-confidence gene models.
- Reverse decoy sequences were used for downstream FDR estimation in FragPipe.
- Inclusion of the cRAP database improved contaminant identification and filtering during peptide searches.

# Step 4 — Peptide and Protein Search using FragPipe

Peptide and protein identification was performed using FragPipe with MSFragger against the combined wheat HC/LC target-decoy protein database containing cRAP contaminant sequences. All tissues were processed using the same FragPipe workflow and search parameters.

---

## Software

### FragPipe workflow version

```text
FragPipe version: 24.0
MSFragger version: 4.4.1
Philosopher version: 5.1.3-RC9
ProteinProphet: enabled
PeptideProphet: enabled
Percolator: disabled
IonQuant: disabled
```

---

## Input files

FragPipe searches were performed on the converted or native mass spectrometry files for each tissue.

### Input formats

```text
PXD050500    Bruker .d folders
MSV000090572 Thermo .raw files
PXD004720    mzML files converted from mzXML
```

---

## Protein database

The following combined target-decoy FASTA database was used:

```text
iwgsc_refseqv2.1_annotation_200916_HC_LC_pep_cRAP_with_DECOY.fasta
```

### Decoy prefix

```text
decoy_
```

---

## Workflow setup

For each tissue, a separate FragPipe run was created.

### Example output directory

```text
C:\Users\Delphine_2026\FragPipe_results\PDX004720_stem_run01
```

### Computational settings

```text
Threads: 4
RAM: 32 GB
Data type: DDA
```

---

## MSFragger search parameters

### Enzyme specificity

```text
Enzyme: Trypsin/P
Cleavage residues: K, R
Cleavage direction: C-terminal
Number of enzymatic termini: 2
Allowed missed cleavages: 10
```

### Peptide length and mass range

```text
Minimum peptide length: 6 aa
Maximum peptide length: 100 aa
Peptide mass range: 300–10,000 Da
```

### Precursor mass tolerance

```text
Precursor mass tolerance: ±10 ppm
True precursor mass tolerance: ±20 ppm
Isotope error: 0/1/2
Precursor mass mode: selected
```

### Fragment mass tolerance

```text
Fragment mass tolerance: ±0.05 Da
Fragment ion series: b, y
Maximum fragment charge: 10
```

### Precursor charge

```text
Charge range: 1–4
Override charge: disabled
```

---

## Modifications

### Fixed modification

```text
Cysteine carbamidomethylation: +57.02146 Da
```

### Variable modifications

```text
Methionine oxidation: +15.9949 Da
Protein N-terminal acetylation: +42.0106 Da
Protein N-terminal methionine clipping: enabled
```

### Variable modification limits

```text
Maximum variable modifications per peptide: 3
Maximum modified forms per peptide: 5
```

---

## Spectrum processing

```text
Deisotoping: enabled
Neutral loss removal: enabled
Remove precursor peak: enabled
Precursor removal range: -1.5 to +1.5 Th
Minimum peaks per spectrum: 15
Top N peaks used: 150
Minimum matched fragments: 4
Minimum fragments for modelling: 2
```

---

## Validation and reporting

### Validation tools

```text
PeptideProphet: enabled
ProteinProphet: enabled
Percolator: disabled
```

### Report settings

```text
Protein FDR: 1%
Sequential filtering: enabled
Peptide-level summary: enabled
Protein-level summary: enabled
Decoys printed in final report: no
Contaminants removed in final report: yes
```

---

## FragPipe outputs used downstream

The main FragPipe output files used for downstream annotation and genome projection were:

```text
psm.tsv
peptide.tsv
protein.tsv
combined_protein.tsv
experiment_annotation.tsv / sdrf.tsv
```

These files were subsequently imported into Python for annotation, contaminant filtering, peptide–protein association, protein-to-gene mapping, and peptide genomic coordinate projection.

---

## Notes

- Each tissue was processed independently to simplify batch management and avoid excessive memory usage.
- The same FragPipe workflow and MSFragger parameters were applied across all 32 tissues.
- The workflow was optimised for peptide/protein identification rather than label-free quantification.
- Matched fragment export was disabled to reduce output size and improve run stability.
- Output files are captured in a file manifest "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

# Step 5 — Build a protein-to-gene mapping table
_inputs:_   
- iwgsc_refseqv2.1_annotation_200916_HC.gff3
- iwgsc_refseqv2.1_annotation_200916_LC.gff3
- iwgsc_refseqv2.1_functional_annotation.csv

__Aim:__  
Map each protein accession / gene model to:  
- chromosome
- gene coordinates
- transcript/CDS model
- HC/LC status
- functional annotation

__Summary:__  
_Parse the wheat GFF3 annotations and build a protein-to-gene mapping table_  
This step parses the high-confidence (HC) and low-confidence (LC) wheat GFF3 annotation files and extracts the structural relationships among genes, transcripts, and CDS features.   
The goal is to create a clean annotation table linking protein accessions and gene models to chromosome, strand, genomic coordinates, and annotation confidence level.   
This table will then be merged into the FASTA-validated peptide–protein evidence in the next step.


```python
#################### Wheat genome data ########################

# ============================================================
# Parse HC + LC GFF3 files and build protein-to-gene mapping table (takes 5 min)
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
```

    Parsed HC features: 1,874,236
    Parsed LC features: 967,070
    Combined features:  2,841,306
    Saved parsed feature table to: python_outputs/tables/wheat_gff3_parsed_features_HC_LC.csv
    Gene rows: 266,760
    Transcript rows: 295,922
    CDS summary rows: 295,914
    Saved protein-to-gene mapping table to: python_outputs/tables/wheat_protein_gene_mapping_HC_LC.csv
    
    ===== GFF3 PARSING SUMMARY =====
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Metric</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Parsed_HC_features</td>
      <td>1874236</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Parsed_LC_features</td>
      <td>967070</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Combined_features</td>
      <td>2841306</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Unique_genes</td>
      <td>266760</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Unique_transcripts</td>
      <td>295922</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Unique_proteins_in_mapping</td>
      <td>295914</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Unique_gene_models_in_mapping</td>
      <td>266752</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Rows_with_gene_coordinates</td>
      <td>295914</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Rows_with_transcript_coordinates</td>
      <td>295914</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Mapping_rows_LC</td>
      <td>163290</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Mapping_rows_HC</td>
      <td>132624</td>
    </tr>
  </tbody>
</table>
</div>


    
    Example protein-to-gene mappings:
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProteinID</th>
      <th>GeneModel</th>
      <th>TranscriptID</th>
      <th>Chromosome</th>
      <th>Strand</th>
      <th>Gene_start</th>
      <th>Gene_end</th>
      <th>Transcript_start</th>
      <th>Transcript_end</th>
      <th>CDS_start</th>
      <th>...</th>
      <th>CDS_phase_values</th>
      <th>Annotation_confidence</th>
      <th>Gene_Name</th>
      <th>Gene_biotype</th>
      <th>Transcript_Name</th>
      <th>Transcript_biotype</th>
      <th>ProteinID_found_in_GFF3</th>
      <th>GeneModel_found_in_GFF3</th>
      <th>Has_gene_coordinates</th>
      <th>Has_transcript_coordinates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TraesCS1A03G0000200.1</td>
      <td>TraesCS1A03G0000200</td>
      <td>TraesCS1A03G0000200.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>40098</td>
      <td>70338</td>
      <td>40098</td>
      <td>70338</td>
      <td>58508</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000200</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000200.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TraesCS1A03G0000400.1</td>
      <td>TraesCS1A03G0000400</td>
      <td>TraesCS1A03G0000400.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>70239</td>
      <td>89245</td>
      <td>70239</td>
      <td>89245</td>
      <td>70239</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000400</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000400.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TraesCS1A03G0000600.1</td>
      <td>TraesCS1A03G0000600</td>
      <td>TraesCS1A03G0000600.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>95906</td>
      <td>104903</td>
      <td>95906</td>
      <td>104903</td>
      <td>104607</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000600</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000600.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TraesCS1A03G0000800.1</td>
      <td>TraesCS1A03G0000800</td>
      <td>TraesCS1A03G0000800.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>102794</td>
      <td>122504</td>
      <td>102794</td>
      <td>122504</td>
      <td>121263</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000800</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000800.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TraesCS1A03G0001000.1</td>
      <td>TraesCS1A03G0001000</td>
      <td>TraesCS1A03G0001000.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>149490</td>
      <td>154559</td>
      <td>149490</td>
      <td>154559</td>
      <td>149490</td>
      <td>...</td>
      <td>0; 2</td>
      <td>HC</td>
      <td>TraesCS1A03G0001000</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001000.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>TraesCS1A03G0001200.1</td>
      <td>TraesCS1A03G0001200</td>
      <td>TraesCS1A03G0001200.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>162313</td>
      <td>162609</td>
      <td>162313</td>
      <td>162609</td>
      <td>162313</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0001200</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001200.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>TraesCS1A03G0001300.1</td>
      <td>TraesCS1A03G0001300</td>
      <td>TraesCS1A03G0001300.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>169592</td>
      <td>169969</td>
      <td>169592</td>
      <td>169969</td>
      <td>169592</td>
      <td>...</td>
      <td>0; 2</td>
      <td>HC</td>
      <td>TraesCS1A03G0001300</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001300.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>TraesCS1A03G0001400.1</td>
      <td>TraesCS1A03G0001400</td>
      <td>TraesCS1A03G0001400.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>180175</td>
      <td>180552</td>
      <td>180175</td>
      <td>180552</td>
      <td>180175</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0001400</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001400.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>8</th>
      <td>TraesCS1A03G0001500.1</td>
      <td>TraesCS1A03G0001500</td>
      <td>TraesCS1A03G0001500.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>233818</td>
      <td>245051</td>
      <td>233818</td>
      <td>245051</td>
      <td>243614</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0001500</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001500.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>9</th>
      <td>TraesCS1A03G0001700.1</td>
      <td>TraesCS1A03G0001700</td>
      <td>TraesCS1A03G0001700.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>269472</td>
      <td>289602</td>
      <td>269472</td>
      <td>289602</td>
      <td>278951</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0001700</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001700.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 24 columns</p>
</div>


    
    Example parsed gene features:
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>GeneModel</th>
      <th>Gene_Chromosome</th>
      <th>Gene_start</th>
      <th>Gene_end</th>
      <th>Gene_strand</th>
      <th>Annotation_confidence</th>
      <th>Gene_Name</th>
      <th>Gene_biotype</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TraesCS1A03G0000200</td>
      <td>Chr1A</td>
      <td>40098</td>
      <td>70338</td>
      <td>-</td>
      <td>HC</td>
      <td>TraesCS1A03G0000200</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>TraesCS1A03G0000400</td>
      <td>Chr1A</td>
      <td>70239</td>
      <td>89245</td>
      <td>+</td>
      <td>HC</td>
      <td>TraesCS1A03G0000400</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>TraesCS1A03G0000600</td>
      <td>Chr1A</td>
      <td>95906</td>
      <td>104903</td>
      <td>+</td>
      <td>HC</td>
      <td>TraesCS1A03G0000600</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>TraesCS1A03G0000800</td>
      <td>Chr1A</td>
      <td>102794</td>
      <td>122504</td>
      <td>+</td>
      <td>HC</td>
      <td>TraesCS1A03G0000800</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>TraesCS1A03G0001000</td>
      <td>Chr1A</td>
      <td>149490</td>
      <td>154559</td>
      <td>-</td>
      <td>HC</td>
      <td>TraesCS1A03G0001000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


    
    Example parsed transcript features:
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TranscriptID</th>
      <th>GeneModel</th>
      <th>Transcript_Chromosome</th>
      <th>Transcript_start</th>
      <th>Transcript_end</th>
      <th>Transcript_strand</th>
      <th>Annotation_confidence</th>
      <th>Transcript_Name</th>
      <th>Transcript_biotype</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>TraesCS1A03G0000200.1</td>
      <td>TraesCS1A03G0000200</td>
      <td>Chr1A</td>
      <td>40098</td>
      <td>70338</td>
      <td>-</td>
      <td>HC</td>
      <td>TraesCS1A03G0000200.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>TraesCS1A03G0000400.1</td>
      <td>TraesCS1A03G0000400</td>
      <td>Chr1A</td>
      <td>70239</td>
      <td>89245</td>
      <td>+</td>
      <td>HC</td>
      <td>TraesCS1A03G0000400.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>TraesCS1A03G0000600.1</td>
      <td>TraesCS1A03G0000600</td>
      <td>Chr1A</td>
      <td>95906</td>
      <td>104903</td>
      <td>+</td>
      <td>HC</td>
      <td>TraesCS1A03G0000600.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>TraesCS1A03G0000800.1</td>
      <td>TraesCS1A03G0000800</td>
      <td>Chr1A</td>
      <td>102794</td>
      <td>122504</td>
      <td>+</td>
      <td>HC</td>
      <td>TraesCS1A03G0000800.1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>TraesCS1A03G0001000.1</td>
      <td>TraesCS1A03G0001000</td>
      <td>Chr1A</td>
      <td>149490</td>
      <td>154559</td>
      <td>-</td>
      <td>HC</td>
      <td>TraesCS1A03G0001000.1</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


    
    Example CDS summary:
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TranscriptID</th>
      <th>ProteinID</th>
      <th>GeneModel_from_protein</th>
      <th>Annotation_confidence</th>
      <th>CDS_feature_count</th>
      <th>CDS_start</th>
      <th>CDS_end</th>
      <th>CDS_total_nt_length</th>
      <th>CDS_Chromosome</th>
      <th>CDS_strand</th>
      <th>CDS_phase_values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TraesCS1A03G0000100LC.1</td>
      <td>TraesCS1A03G0000100LC.1</td>
      <td>TraesCS1A03G0000100LC</td>
      <td>LC</td>
      <td>1</td>
      <td>41202</td>
      <td>41522</td>
      <td>321</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TraesCS1A03G0000200.1</td>
      <td>TraesCS1A03G0000200.1</td>
      <td>TraesCS1A03G0000200</td>
      <td>HC</td>
      <td>1</td>
      <td>58508</td>
      <td>58768</td>
      <td>261</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TraesCS1A03G0000300LC.1</td>
      <td>TraesCS1A03G0000300LC.1</td>
      <td>TraesCS1A03G0000300LC</td>
      <td>LC</td>
      <td>1</td>
      <td>42451</td>
      <td>42645</td>
      <td>195</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TraesCS1A03G0000400.1</td>
      <td>TraesCS1A03G0000400.1</td>
      <td>TraesCS1A03G0000400</td>
      <td>HC</td>
      <td>1</td>
      <td>70239</td>
      <td>70556</td>
      <td>318</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TraesCS1A03G0000500LC.1</td>
      <td>TraesCS1A03G0000500LC.1</td>
      <td>TraesCS1A03G0000500LC</td>
      <td>LC</td>
      <td>3</td>
      <td>94185</td>
      <td>110830</td>
      <td>309</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>0; 1</td>
    </tr>
  </tbody>
</table>
</div>


# Step 6 — FragPipe Output Annotation and Quality Summary

FragPipe peptide and protein identification tables were standardised and annotated in Python to improve traceability, facilitate downstream batch processing, and enable dataset-wide quality assessment across all wheat tissues.

Annotated FragPipe output tables were generated for both peptide- and protein-level results by importing the original `.tsv` files and appending standardised metadata columns derived from the experimental manifest file.

---

## Input files

### FragPipe result tables

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide.tsv
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_protein.tsv
```

### Example

```text
FragPipe_Duncan_PXD004720_anther_peptide.tsv
FragPipe_Duncan_PXD004720_anther_protein.tsv
```

### Manifest file

```text
wheat_tissues_FragPipe-result-manifest_2026-05-11.csv
```

---

## Metadata annotation

The following traceability columns were added to each FragPipe result table:

| Column | Description |
|---|---|
| Index | Sequential row identifier |
| Source | Proteomics repository/project identifier |
| Species | Species name |
| Tissue | Wheat tissue name/code |
| Batch | FragPipe processing batch |
| FragPipe_result | Result type (`peptide` or `protein`) |
| Contaminant | Contaminant assignment (`yes` or `no`) |

---

## Contaminant assignment

Contaminant status was inferred directly from the FragPipe `Protein` column.

### Rule

```text
Protein accession starts with "Traes" → Contaminant = no
Otherwise → Contaminant = yes
```

This strategy enabled rapid separation of wheat-derived peptide/protein identifications from common contaminant proteins originating from keratins, trypsin, laboratory handling, or external contaminant databases.

---

## Output files

Annotated tables were exported as `.csv` files into:

```text
python_outputs/tables/
```

### Example outputs

```text
FragPipe_Duncan_PXD004720_anther_peptide_annotated.csv
FragPipe_Duncan_PXD004720_anther_protein_annotated.csv
```

---

## Batch processing

All wheat tissues were processed automatically using generic Python functions driven by the experimental manifest file.

### Total processed outputs

```text
32 tissues × 2 result types = 64 annotated tables
```

---

## Quality summary table

A global summary table was additionally generated to capture key identification and contaminant statistics for each annotated FragPipe output file.

### Summary metrics

| Metric | Description |
|---|---|
| peptide_count | Number of peptide rows |
| protein_count | Number of protein rows |
| Contaminant_count | Number of contaminant entries |
| Non_contaminant_count | Number of wheat-derived entries |

### Output summary file

```text
wheat_fragpipe_annotation_summary_step6.csv
```

This summary table served as the foundation for subsequent filtering, peptide-to-protein mapping, genome projection, and downstream proteogenomics analyses.


```python
# ============================================================
# Step 6 — Annotate FragPipe peptide/protein output tables
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

output_dir = Path("python_outputs/tables")
output_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 2. Load manifest
# -----------------------------
manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

display(manifest.head())


# -----------------------------
# 3. Helper function
# -----------------------------
def annotate_fragpipe_output(source, tissue_raw_code, result_type):
    """
    Annotate one FragPipe peptide or protein output table with traceability columns.

    Parameters
    ----------
    source : str
        Proteomics dataset source, e.g. "PXD004720", "PXD050500", "MSV000090572".

    tissue_raw_code : str
        Tissue raw code as listed in the manifest, e.g. "anther", "node", "stored-grain".

    result_type : str
        Either "peptide" or "protein".

    Returns
    -------
    pd.DataFrame
        Annotated FragPipe table.
    """

    result_type = result_type.lower()

    if result_type not in ["peptide", "protein"]:
        raise ValueError("result_type must be either 'peptide' or 'protein'.")

    # Find matching manifest row
    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(
            f"No manifest entry found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    if len(match) > 1:
        raise ValueError(
            f"Multiple manifest entries found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    row = match.iloc[0]

    # Retrieve input filename from manifest
    if result_type == "peptide":
        input_filename = row["FragPipe-Output-Peptide"]
        anchor_col = "Peptide"
    else:
        input_filename = row["FragPipe-Output-Protein"]
        anchor_col = "Protein"

    input_path = fragpipe_dir / input_filename

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Read FragPipe TSV file
    data = pd.read_csv(input_path, sep="\t", header=0)

    # Check required Protein column for contaminant assignment
    if "Protein" not in data.columns:
        raise KeyError(f"'Protein' column not found in {input_filename}")

    # Add traceability columns
    data["Index"] = range(1, len(data) + 1)
    data["Source"] = row["Source"]
    data["Species"] = row["Species"]
    data["Tissue"] = row["Tissue-Raw-Code"]
    data["Batch"] = row["Batch"]
    data["FragPipe_result"] = result_type
    data["Contaminant"] = data["Protein"].astype(str).str.startswith("Traes").map(
        {True: "no", False: "yes"}
    )

    new_cols = [
        "Index",
        "Source",
        "Species",
        "Tissue",
        "Batch",
        "FragPipe_result",
        "Contaminant"
    ]

    # Insert metadata columns before Peptide or Protein column when possible
    remaining_cols = [col for col in data.columns if col not in new_cols]

    if anchor_col in remaining_cols:
        anchor_pos = remaining_cols.index(anchor_col)
        ordered_cols = (
            remaining_cols[:anchor_pos] +
            new_cols +
            remaining_cols[anchor_pos:]
        )
    else:
        ordered_cols = new_cols + remaining_cols

    data = data[ordered_cols]

    # Save annotated table
    output_filename = input_filename.replace(".tsv", "_annotated.csv")
    output_path = output_dir / output_filename

    data.to_csv(output_path, index=False)

    print(f"Annotated file saved: {output_path}")
    print(f"Rows: {data.shape[0]:,}")
    print(f"Columns: {data.shape[1]:,}")

    return data


# -----------------------------
# 4. Example usage to check code
# -----------------------------

# Example peptide file
annotated_peptide = annotate_fragpipe_output(
    source="PXD050500",
    tissue_raw_code="radicle",
    result_type="peptide"
)

# Example protein file
annotated_protein = annotate_fragpipe_output(
    source="PXD050500",
    tissue_raw_code="radicle",
    result_type="protein"
)

# -----------------------------
# 5. Annotate all FragPipe TSV files
# -----------------------------

for _, row in manifest.iterrows():
    source = row["Source"]
    tissue_raw_code = row["Tissue-Raw-Code"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    annotate_fragpipe_output(
        source=source,
        tissue_raw_code=tissue_raw_code,
        result_type="peptide"
    )

    annotate_fragpipe_output(
        source=source,
        tissue_raw_code=tissue_raw_code,
        result_type="protein"
    )


# -----------------------------
# 6. Create Step 6 summary table
# -----------------------------

step6_summary_records = []

for _, row in manifest.iterrows():
    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    for result_type in ["peptide", "protein"]:

        if result_type == "peptide":
            input_filename = row["FragPipe-Output-Peptide"]
            count_label = "peptide_count"
        else:
            input_filename = row["FragPipe-Output-Protein"]
            count_label = "protein_count"

        annotated_filename = input_filename.replace(".tsv", "_annotated.csv")
        annotated_path = output_dir / annotated_filename

        if not annotated_path.exists():
            print(f"Warning: annotated file not found, skipped: {annotated_path}")
            continue

        data = pd.read_csv(annotated_path)

        total_count = len(data)
        contaminant_count = (data["Contaminant"] == "yes").sum()
        non_contaminant_count = (data["Contaminant"] == "no").sum()

        step6_summary_records.append({
            "Source": source,
            "Species": species,
            "Tissue": tissue_raw_code,
            "Batch": batch,
            "FragPipe_result": result_type,
            "Annotated_file": annotated_filename,
            count_label: total_count,
            "Contaminant_count": contaminant_count,
            "Non_contaminant_count": non_contaminant_count
        })

step6_summary = pd.DataFrame(step6_summary_records)

# Keep peptide/protein counts in one generic column as well
step6_summary["Total_rows"] = step6_summary[["peptide_count", "protein_count"]].sum(axis=1, skipna=True)

# Reorder columns
summary_cols = [
    "Source",
    "Species",
    "Tissue",
    "Batch",
    "FragPipe_result",
    "Annotated_file",
    "Total_rows",
    "peptide_count",
    "protein_count",
    "Contaminant_count",
    "Non_contaminant_count"
]

step6_summary = step6_summary[summary_cols]

# Save summary table
step6_summary_out = output_dir / "wheat_fragpipe_annotation_summary_step6.csv"
step6_summary.to_csv(step6_summary_out, index=False)

print(f"Step 6 summary saved: {step6_summary_out}")
print(f"Summary rows: {step6_summary.shape[0]:,}")

display(step6_summary)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>First-Author</th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue-Name</th>
      <th>Tissue-Raw-Code</th>
      <th>Tissue-Description</th>
      <th>Batch</th>
      <th>FragPipe-Output-Peptide</th>
      <th>FragPipe-Output-Protein</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Vincent</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>stored_grain</td>
      <td>NaN</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pro...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Liu</td>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>germ</td>
      <td>coleoptile</td>
      <td>The protective, white, tubular sheath that eme...</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide.tsv</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_protein.tsv</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Liu</td>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>node</td>
      <td>The crown area where the seminal roots, advent...</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide.tsv</td>
      <td>FragPipe_Liu_PXD050500_node_protein.tsv</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Liu</td>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>root</td>
      <td>radicle</td>
      <td>The first primary root that emerges from the s...</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide.tsv</td>
      <td>FragPipe_Liu_PXD050500_radicle_protein.tsv</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Duncan</td>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>anther</td>
      <td>NaN</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide.tsv</td>
      <td>FragPipe_Duncan_PXD004720_anther_protein.tsv</td>
    </tr>
  </tbody>
</table>
</div>


    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_peptide_annotated.csv
    Rows: 333,400
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_protein_annotated.csv
    Rows: 105,970
    Columns: 33
    
    Processing MSV000090572 | stored_grain
    Annotated file saved: python_outputs\tables\FragPipe_Vincent_MSV000090572_stored-grain_peptide_annotated.csv
    Rows: 9,343
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Vincent_MSV000090572_stored-grain_protein_annotated.csv
    Rows: 7,074
    Columns: 33
    
    Processing PXD050500 | coleoptile
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_coleoptile_peptide_annotated.csv
    Rows: 583,184
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_coleoptile_protein_annotated.csv
    Rows: 137,841
    Columns: 33
    
    Processing PXD050500 | node
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_node_peptide_annotated.csv
    Rows: 596,437
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_node_protein_annotated.csv
    Rows: 141,772
    Columns: 33
    
    Processing PXD050500 | radicle
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_peptide_annotated.csv
    Rows: 333,400
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_protein_annotated.csv
    Rows: 105,970
    Columns: 33
    
    Processing PXD004720 | anther
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_anther_peptide_annotated.csv
    Rows: 34,203
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_anther_protein_annotated.csv
    Rows: 10,095
    Columns: 33
    
    Processing PXD004720 | boot
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_boot_peptide_annotated.csv
    Rows: 3,644
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_boot_protein_annotated.csv
    Rows: 2,828
    Columns: 33
    
    Processing PXD004720 | coleoptile
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_coleoptile_peptide_annotated.csv
    Rows: 41,126
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_coleoptile_protein_annotated.csv
    Rows: 12,216
    Columns: 33
    
    Processing PXD004720 | embryo
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_embryo_peptide_annotated.csv
    Rows: 2,868
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_embryo_protein_annotated.csv
    Rows: 2,403
    Columns: 33
    
    Processing PXD004720 | endosperm
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_endosperm_peptide_annotated.csv
    Rows: 20,174
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_endosperm_protein_annotated.csv
    Rows: 7,427
    Columns: 33
    
    Processing PXD004720 | glume
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_glume_peptide_annotated.csv
    Rows: 28,683
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_glume_protein_annotated.csv
    Rows: 9,612
    Columns: 33
    
    Processing PXD004720 | grain-zadoks-70
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_annotated.csv
    Rows: 26,229
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-70_protein_annotated.csv
    Rows: 9,821
    Columns: 33
    
    Processing PXD004720 | grain-zadoks-71
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_annotated.csv
    Rows: 35,990
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-71_protein_annotated.csv
    Rows: 12,336
    Columns: 33
    
    Processing PXD004720 | grain-zadoks-75
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_annotated.csv
    Rows: 27,552
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-75_protein_annotated.csv
    Rows: 11,100
    Columns: 33
    
    Processing PXD004720 | grain-zadoks-83
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_annotated.csv
    Rows: 24,051
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-83_protein_annotated.csv
    Rows: 10,194
    Columns: 33
    
    Processing PXD004720 | grain-zadoks-87
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_annotated.csv
    Rows: 24,674
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-87_protein_annotated.csv
    Rows: 10,389
    Columns: 33
    
    Processing PXD004720 | leaf-flag-mature
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_annotated.csv
    Rows: 29,941
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-mature_protein_annotated.csv
    Rows: 9,639
    Columns: 33
    
    Processing PXD004720 | leaf-flag-senescing
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_annotated.csv
    Rows: 11,394
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-senescing_protein_annotated.csv
    Rows: 8,034
    Columns: 33
    
    Processing PXD004720 | leaf-flag-young
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_annotated.csv
    Rows: 23,441
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-young_protein_annotated.csv
    Rows: 7,542
    Columns: 33
    
    Processing PXD004720 | lemma
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_lemma_peptide_annotated.csv
    Rows: 29,842
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_lemma_protein_annotated.csv
    Rows: 9,956
    Columns: 33
    
    Processing PXD004720 | node
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node_peptide_annotated.csv
    Rows: 21,508
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node_protein_annotated.csv
    Rows: 10,530
    Columns: 33
    
    Processing PXD004720 | node_secretion
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node-secretion_peptide_annotated.csv
    Rows: 34,194
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node-secretion_protein_annotated.csv
    Rows: 10,572
    Columns: 33
    
    Processing PXD004720 | palea
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_palea_peptide_annotated.csv
    Rows: 21,774
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_palea_protein_annotated.csv
    Rows: 6,942
    Columns: 33
    
    Processing PXD004720 | pericarp
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pericarp_peptide_annotated.csv
    Rows: 28,448
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pericarp_protein_annotated.csv
    Rows: 9,466
    Columns: 33
    
    Processing PXD004720 | pollen
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pollen_peptide_annotated.csv
    Rows: 13,593
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pollen_protein_annotated.csv
    Rows: 4,676
    Columns: 33
    
    Processing PXD004720 | rachilla
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_rachilla_peptide_annotated.csv
    Rows: 31,213
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_rachilla_protein_annotated.csv
    Rows: 9,717
    Columns: 33
    
    Processing PXD004720 | radicle
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_radicle_peptide_annotated.csv
    Rows: 39,704
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_radicle_protein_annotated.csv
    Rows: 11,752
    Columns: 33
    
    Processing PXD004720 | root-mature
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-mature_peptide_annotated.csv
    Rows: 21,390
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-mature_protein_annotated.csv
    Rows: 12,214
    Columns: 33
    
    Processing PXD004720 | root-secretion
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-secretion_peptide_annotated.csv
    Rows: 21,329
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-secretion_protein_annotated.csv
    Rows: 10,309
    Columns: 33
    
    Processing PXD004720 | root-tip
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-tip_peptide_annotated.csv
    Rows: 38,681
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-tip_protein_annotated.csv
    Rows: 10,344
    Columns: 33
    
    Processing PXD004720 | root-vasculature
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-vasculature_peptide_annotated.csv
    Rows: 20,911
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-vasculature_protein_annotated.csv
    Rows: 7,577
    Columns: 33
    
    Processing PXD004720 | spike-immature
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_spike-immature_peptide_annotated.csv
    Rows: 36,414
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_spike-immature_protein_annotated.csv
    Rows: 10,948
    Columns: 33
    
    Processing PXD004720 | stem
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_stem_peptide_annotated.csv
    Rows: 14,389
    Columns: 30
    Annotated file saved: python_outputs\tables\FragPipe_Duncan_PXD004720_stem_protein_annotated.csv
    Rows: 8,984
    Columns: 33
    Step 6 summary saved: python_outputs\tables\wheat_fragpipe_annotation_summary_step6.csv
    Summary rows: 64
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>FragPipe_result</th>
      <th>Annotated_file</th>
      <th>Total_rows</th>
      <th>peptide_count</th>
      <th>protein_count</th>
      <th>Contaminant_count</th>
      <th>Non_contaminant_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>peptide</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>9343.0</td>
      <td>9343.0</td>
      <td>NaN</td>
      <td>14</td>
      <td>9329</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>protein</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pro...</td>
      <td>7074.0</td>
      <td>NaN</td>
      <td>7074.0</td>
      <td>6</td>
      <td>7068</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>peptide</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_anno...</td>
      <td>583184.0</td>
      <td>583184.0</td>
      <td>NaN</td>
      <td>409</td>
      <td>582775</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>protein</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_protein_anno...</td>
      <td>137841.0</td>
      <td>NaN</td>
      <td>137841.0</td>
      <td>79</td>
      <td>137762</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>peptide</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_annotated.csv</td>
      <td>596437.0</td>
      <td>596437.0</td>
      <td>NaN</td>
      <td>483</td>
      <td>595954</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>protein</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pro...</td>
      <td>7577.0</td>
      <td>NaN</td>
      <td>7577.0</td>
      <td>9</td>
      <td>7568</td>
    </tr>
    <tr>
      <th>60</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>peptide</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>36414.0</td>
      <td>36414.0</td>
      <td>NaN</td>
      <td>44</td>
      <td>36370</td>
    </tr>
    <tr>
      <th>61</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>protein</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_prote...</td>
      <td>10948.0</td>
      <td>NaN</td>
      <td>10948.0</td>
      <td>8</td>
      <td>10940</td>
    </tr>
    <tr>
      <th>62</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>peptide</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_annotat...</td>
      <td>14389.0</td>
      <td>14389.0</td>
      <td>NaN</td>
      <td>51</td>
      <td>14338</td>
    </tr>
    <tr>
      <th>63</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>protein</td>
      <td>FragPipe_Duncan_PXD004720_stem_protein_annotat...</td>
      <td>8984.0</td>
      <td>NaN</td>
      <td>8984.0</td>
      <td>10</td>
      <td>8974</td>
    </tr>
  </tbody>
</table>
<p>64 rows × 11 columns</p>
</div>


# Step 7 — Build Non-Contaminant Peptide–Protein Evidence Tables

This step converts the annotated FragPipe peptide-level outputs into standardised peptide–protein evidence tables for each wheat tissue.

Only wheat-derived identifications were retained for downstream analysis.

### Filtering rule

```text
Contaminant == "no"
```

This removed cRAP contaminants and other non-wheat entries before protein mapping and genome projection.

---

## Purpose

The aim of this step was to create a clean intermediate table linking each identified peptide sequence to its associated wheat protein accession(s).

This table provides the bridge between:

```text
FragPipe peptide identifications
```

and:

```text
protein accession → gene model → genomic coordinates
```

---

## Protein and isoform handling

FragPipe reports a primary protein accession in the `Protein` column and, when available, additional related accessions in the `Mapped Proteins` column.

To preserve protein isoform and shared-peptide information, this step expands the peptide table into peptide–protein pairs.

### Protein mapping categories

| Category | Description |
|---|---|
| primary | Protein accession reported in the FragPipe `Protein` column |
| mapped | Additional protein accession reported in the FragPipe `Mapped Proteins` column |

This avoids prematurely collapsing peptides that may support multiple protein isoforms or closely related wheat gene models.

---

## Output files

One peptide–protein evidence table was exported per tissue.

### Example output

```text
FragPipe_Duncan_PXD004720_anther_peptide_protein_evidence.csv
```

### Output directory

```text
python_outputs/tables/
```

---

## Summary metrics

A Step 7 summary table was generated across all tissues.

### Metrics captured

| Metric | Description |
|---|---|
| Non_contaminant_peptide_protein_pairs | Total number of retained peptide–protein evidence rows |
| Unique_peptides | Number of unique peptide sequences |
| Unique_proteins | Number of unique wheat protein accessions |
| Primary_peptide_protein_pairs | Number of primary peptide–protein associations |
| Mapped_peptide_protein_pairs | Number of additional mapped protein/isoform associations |
| Peptides_mapping_to_multiple_proteins | Number of peptides associated with more than one protein accession |
| Proteins_supported_by_one_peptide | Number of proteins supported by one unique peptide |
| Proteins_supported_by_two_or_more_peptides | Number of proteins supported by at least two unique peptides |

### Output summary file

```text
wheat_fragpipe_peptide_protein_evidence_summary_step7.csv
```

This evidence table is used in the next step to link protein accessions to wheat gene models and genome annotation coordinates.


```python
# ============================================================
# Step 7 — Build non-contaminant peptide–protein evidence tables
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
step6_summary_file = tables_dir / "wheat_fragpipe_annotation_summary_step6.csv"

step7_summary_out = tables_dir / "wheat_fragpipe_peptide_protein_evidence_summary_step7.csv"

# -----------------------------
# 2. Load manifest
# -----------------------------
manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 3. Helper functions
# -----------------------------
def split_mapped_proteins(value):
    """
    Split FragPipe mapped protein accessions into a clean list.

    Handles empty values and common separators used in protein tables.
    """
    if pd.isna(value):
        return []

    value = str(value).strip()

    if value == "" or value.lower() in ["nan", "na", "none"]:
        return []

    for sep in [";", ","]:
        value = value.replace(sep, "|")

    return [x.strip() for x in value.split("|") if x.strip()]


def find_optional_column(data, possible_names):
    """
    Return the first matching column name from a list of possible names.
    """
    for col in possible_names:
        if col in data.columns:
            return col
    return None


def build_peptide_protein_evidence(source, tissue_raw_code):
    """
    Build a non-contaminant peptide–protein evidence table for one tissue.

    Parameters
    ----------
    source : str
        Proteomics dataset source, e.g. "PXD004720".

    tissue_raw_code : str
        Tissue code as listed in the manifest, e.g. "anther".

    Returns
    -------
    pd.DataFrame
        Expanded peptide–protein evidence table.
    """

    # Find matching manifest row
    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(
            f"No manifest entry found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    if len(match) > 1:
        raise ValueError(
            f"Multiple manifest entries found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    row = match.iloc[0]

    # Input annotated peptide file from Step 6
    peptide_filename = row["FragPipe-Output-Peptide"]
    annotated_filename = peptide_filename.replace(".tsv", "_annotated.csv")
    annotated_path = tables_dir / annotated_filename

    if not annotated_path.exists():
        raise FileNotFoundError(f"Annotated peptide file not found: {annotated_path}")

    # Read annotated peptide table
    data = pd.read_csv(annotated_path)

    # Required columns
    required_cols = ["Peptide", "Protein", "Contaminant"]
    missing_cols = [col for col in required_cols if col not in data.columns]

    if missing_cols:
        raise KeyError(
            f"Missing required column(s) in {annotated_filename}: {missing_cols}"
        )

    # Keep wheat-derived identifications only
    data = data[data["Contaminant"] == "no"].copy()

    # Optional FragPipe evidence columns
    mapped_col = find_optional_column(
        data,
        ["Mapped Proteins", "Mapped Protein", "Mapped_Proteins", "Mapped proteins"]
    )

    probability_col = find_optional_column(
        data,
        ["Probability", "PeptideProphet Probability", "Peptide Probability"]
    )

    spectral_count_col = find_optional_column(
        data,
        ["Spectral Count", "Spectral_Count", "SpectralCount"]
    )

    charge_col = find_optional_column(
        data,
        ["Charges", "Charge"]
    )

    records = []

    for _, peptide_row in data.iterrows():

        peptide = peptide_row["Peptide"]
        primary_protein = peptide_row["Protein"]

        # Primary protein evidence
        protein_records = [{
            "ProteinID": primary_protein,
            "Protein_mapping_type": "primary"
        }]

        # Additional mapped proteins / isoforms, when present
        if mapped_col is not None:
            mapped_proteins = split_mapped_proteins(peptide_row[mapped_col])

            for mapped_protein in mapped_proteins:
                if mapped_protein != primary_protein:
                    protein_records.append({
                        "ProteinID": mapped_protein,
                        "Protein_mapping_type": "mapped"
                    })

        for protein_record in protein_records:

            record = {
                "Source": row["Source"],
                "Species": row["Species"],
                "Tissue": row["Tissue-Raw-Code"],
                "Batch": row["Batch"],
                "Peptide": peptide,
                "ProteinID": protein_record["ProteinID"],
                "Protein_mapping_type": protein_record["Protein_mapping_type"],
                "Contaminant": "no"
            }

            if probability_col is not None:
                record["Probability"] = peptide_row[probability_col]

            if spectral_count_col is not None:
                record["Spectral_Count"] = peptide_row[spectral_count_col]

            if charge_col is not None:
                record["Charges"] = peptide_row[charge_col]

            records.append(record)

    evidence = pd.DataFrame(records)

    # Add sequential index
    evidence.insert(0, "Index", range(1, len(evidence) + 1))

    # Remove accidental duplicated peptide–protein rows within a tissue
    # This should usually not be needed, but keeps the output robust.
    evidence = evidence.drop_duplicates(
        subset=["Source", "Tissue", "Peptide", "ProteinID", "Protein_mapping_type"]
    ).reset_index(drop=True)

    evidence["Index"] = range(1, len(evidence) + 1)

    # Save output
    output_filename = peptide_filename.replace(
        "_peptide.tsv",
        "_peptide_protein_evidence.csv"
    )

    output_path = tables_dir / output_filename
    evidence.to_csv(output_path, index=False)

    print(f"Saved peptide–protein evidence table: {output_path}")
    print(f"Rows: {len(evidence):,}")
    print(f"Unique peptides: {evidence['Peptide'].nunique():,}")
    print(f"Unique proteins: {evidence['ProteinID'].nunique():,}")

    return evidence


# -----------------------------
# 4. Run Step 7 for all tissues
# -----------------------------
step7_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    evidence = build_peptide_protein_evidence(
        source=source,
        tissue_raw_code=tissue_raw_code
    )

    output_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_evidence.csv"
    )

    primary_evidence = evidence[evidence["Protein_mapping_type"] == "primary"]
    mapped_evidence = evidence[evidence["Protein_mapping_type"] == "mapped"]

    peptides_per_protein = (
        evidence.groupby("ProteinID")["Peptide"]
        .nunique()
        .reset_index(name="unique_peptides_per_protein")
    )

    proteins_per_peptide = (
        evidence.groupby("Peptide")["ProteinID"]
        .nunique()
        .reset_index(name="protein_isoforms_per_peptide")
    )

    step7_summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue_raw_code,
        "Batch": batch,
        "Evidence_file": output_filename,
        "Non_contaminant_peptide_protein_pairs": len(evidence),
        "Unique_peptides": evidence["Peptide"].nunique(),
        "Unique_proteins": evidence["ProteinID"].nunique(),
        "Primary_peptide_protein_pairs": len(primary_evidence),
        "Mapped_peptide_protein_pairs": len(mapped_evidence),
        "Peptides_mapping_to_multiple_proteins": (
            proteins_per_peptide["protein_isoforms_per_peptide"] > 1
        ).sum(),
        "Proteins_supported_by_one_peptide": (
            peptides_per_protein["unique_peptides_per_protein"] == 1
        ).sum(),
        "Proteins_supported_by_two_or_more_peptides": (
            peptides_per_protein["unique_peptides_per_protein"] >= 2
        ).sum()
    })

step7_summary = pd.DataFrame(step7_summary_records)

# Save Step 7 summary
step7_summary.to_csv(step7_summary_out, index=False)

print(f"\nStep 7 summary saved: {step7_summary_out}")
print(f"Summary rows: {step7_summary.shape[0]:,}")

display(step7_summary)
```

    
    Processing MSV000090572 | stored_grain
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Vincent_MSV000090572_stored-grain_peptide_protein_evidence.csv
    Rows: 30,317
    Unique peptides: 9,329
    Unique proteins: 17,481
    
    Processing PXD050500 | coleoptile
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Liu_PXD050500_coleoptile_peptide_protein_evidence.csv
    Rows: 1,850,247
    Unique peptides: 582,775
    Unique proteins: 239,514
    
    Processing PXD050500 | node
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Liu_PXD050500_node_peptide_protein_evidence.csv
    Rows: 1,887,009
    Unique peptides: 595,954
    Unique proteins: 242,842
    
    Processing PXD050500 | radicle
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_peptide_protein_evidence.csv
    Rows: 1,062,587
    Unique peptides: 333,058
    Unique proteins: 206,049
    
    Processing PXD004720 | anther
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_anther_peptide_protein_evidence.csv
    Rows: 164,397
    Unique peptides: 34,098
    Unique proteins: 36,839
    
    Processing PXD004720 | boot
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_boot_peptide_protein_evidence.csv
    Rows: 13,230
    Unique peptides: 3,643
    Unique proteins: 9,211
    
    Processing PXD004720 | coleoptile
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_coleoptile_peptide_protein_evidence.csv
    Rows: 204,518
    Unique peptides: 41,025
    Unique proteins: 46,513
    
    Processing PXD004720 | embryo
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_embryo_peptide_protein_evidence.csv
    Rows: 8,852
    Unique peptides: 2,867
    Unique proteins: 7,220
    
    Processing PXD004720 | endosperm
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_endosperm_peptide_protein_evidence.csv
    Rows: 102,845
    Unique peptides: 20,081
    Unique proteins: 27,461
    
    Processing PXD004720 | glume
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_glume_peptide_protein_evidence.csv
    Rows: 145,154
    Unique peptides: 28,648
    Unique proteins: 35,551
    
    Processing PXD004720 | grain-zadoks-70
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_protein_evidence.csv
    Rows: 126,227
    Unique peptides: 26,196
    Unique proteins: 35,549
    
    Processing PXD004720 | grain-zadoks-71
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_protein_evidence.csv
    Rows: 179,751
    Unique peptides: 35,960
    Unique proteins: 47,089
    
    Processing PXD004720 | grain-zadoks-75
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_protein_evidence.csv
    Rows: 132,719
    Unique peptides: 27,463
    Unique proteins: 41,042
    
    Processing PXD004720 | grain-zadoks-83
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_protein_evidence.csv
    Rows: 113,236
    Unique peptides: 23,990
    Unique proteins: 36,654
    
    Processing PXD004720 | grain-zadoks-87
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_protein_evidence.csv
    Rows: 111,819
    Unique peptides: 24,636
    Unique proteins: 34,889
    
    Processing PXD004720 | leaf-flag-mature
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_protein_evidence.csv
    Rows: 145,650
    Unique peptides: 29,840
    Unique proteins: 37,963
    
    Processing PXD004720 | leaf-flag-senescing
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_protein_evidence.csv
    Rows: 46,206
    Unique peptides: 11,354
    Unique proteins: 25,701
    
    Processing PXD004720 | leaf-flag-young
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_protein_evidence.csv
    Rows: 120,833
    Unique peptides: 23,373
    Unique proteins: 32,629
    
    Processing PXD004720 | lemma
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_lemma_peptide_protein_evidence.csv
    Rows: 147,650
    Unique peptides: 29,788
    Unique proteins: 37,946
    
    Processing PXD004720 | node
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_node_peptide_protein_evidence.csv
    Rows: 99,844
    Unique peptides: 21,457
    Unique proteins: 36,555
    
    Processing PXD004720 | node_secretion
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_node-secretion_peptide_protein_evidence.csv
    Rows: 169,705
    Unique peptides: 34,124
    Unique proteins: 42,371
    
    Processing PXD004720 | palea
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_palea_peptide_protein_evidence.csv
    Rows: 116,960
    Unique peptides: 21,707
    Unique proteins: 27,591
    
    Processing PXD004720 | pericarp
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_pericarp_peptide_protein_evidence.csv
    Rows: 131,245
    Unique peptides: 28,332
    Unique proteins: 32,676
    
    Processing PXD004720 | pollen
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_pollen_peptide_protein_evidence.csv
    Rows: 74,722
    Unique peptides: 13,502
    Unique proteins: 19,942
    
    Processing PXD004720 | rachilla
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_rachilla_peptide_protein_evidence.csv
    Rows: 160,234
    Unique peptides: 31,145
    Unique proteins: 37,219
    
    Processing PXD004720 | radicle
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_radicle_peptide_protein_evidence.csv
    Rows: 194,730
    Unique peptides: 39,643
    Unique proteins: 42,976
    
    Processing PXD004720 | root-mature
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-mature_peptide_protein_evidence.csv
    Rows: 97,211
    Unique peptides: 21,350
    Unique proteins: 39,165
    
    Processing PXD004720 | root-secretion
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-secretion_peptide_protein_evidence.csv
    Rows: 100,654
    Unique peptides: 21,284
    Unique proteins: 32,049
    
    Processing PXD004720 | root-tip
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-tip_peptide_protein_evidence.csv
    Rows: 191,973
    Unique peptides: 38,634
    Unique proteins: 39,785
    
    Processing PXD004720 | root-vasculature
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-vasculature_peptide_protein_evidence.csv
    Rows: 111,846
    Unique peptides: 20,815
    Unique proteins: 30,631
    
    Processing PXD004720 | spike-immature
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_spike-immature_peptide_protein_evidence.csv
    Rows: 188,868
    Unique peptides: 36,370
    Unique proteins: 40,220
    
    Processing PXD004720 | stem
    Saved peptide–protein evidence table: python_outputs\tables\FragPipe_Duncan_PXD004720_stem_peptide_protein_evidence.csv
    Rows: 60,749
    Unique peptides: 14,338
    Unique proteins: 29,417
    
    Step 7 summary saved: python_outputs\tables\wheat_fragpipe_peptide_protein_evidence_summary_step7.csv
    Summary rows: 32
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Evidence_file</th>
      <th>Non_contaminant_peptide_protein_pairs</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins</th>
      <th>Primary_peptide_protein_pairs</th>
      <th>Mapped_peptide_protein_pairs</th>
      <th>Peptides_mapping_to_multiple_proteins</th>
      <th>Proteins_supported_by_one_peptide</th>
      <th>Proteins_supported_by_two_or_more_peptides</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>30317</td>
      <td>9329</td>
      <td>17481</td>
      <td>9329</td>
      <td>20988</td>
      <td>4290</td>
      <td>14135</td>
      <td>3346</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_prot...</td>
      <td>1850247</td>
      <td>582775</td>
      <td>239514</td>
      <td>582775</td>
      <td>1267472</td>
      <td>338464</td>
      <td>59431</td>
      <td>180083</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_protein_ev...</td>
      <td>1887009</td>
      <td>595954</td>
      <td>242842</td>
      <td>595954</td>
      <td>1291055</td>
      <td>340536</td>
      <td>57486</td>
      <td>185356</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_protein...</td>
      <td>1062587</td>
      <td>333058</td>
      <td>206049</td>
      <td>333058</td>
      <td>729529</td>
      <td>190016</td>
      <td>68213</td>
      <td>137836</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_prote...</td>
      <td>164397</td>
      <td>34098</td>
      <td>36839</td>
      <td>34098</td>
      <td>130299</td>
      <td>27707</td>
      <td>19944</td>
      <td>16895</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_protein...</td>
      <td>13230</td>
      <td>3643</td>
      <td>9211</td>
      <td>3643</td>
      <td>9587</td>
      <td>2302</td>
      <td>7288</td>
      <td>1923</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_p...</td>
      <td>204518</td>
      <td>41025</td>
      <td>46513</td>
      <td>41025</td>
      <td>163493</td>
      <td>34608</td>
      <td>23582</td>
      <td>22931</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_prote...</td>
      <td>8852</td>
      <td>2867</td>
      <td>7220</td>
      <td>2867</td>
      <td>5985</td>
      <td>1581</td>
      <td>6285</td>
      <td>935</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_pr...</td>
      <td>102845</td>
      <td>20081</td>
      <td>27461</td>
      <td>20081</td>
      <td>82764</td>
      <td>15925</td>
      <td>15845</td>
      <td>11616</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_protei...</td>
      <td>145154</td>
      <td>28648</td>
      <td>35551</td>
      <td>28648</td>
      <td>116506</td>
      <td>23601</td>
      <td>19974</td>
      <td>15577</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>126227</td>
      <td>26196</td>
      <td>35549</td>
      <td>26196</td>
      <td>100031</td>
      <td>20748</td>
      <td>20524</td>
      <td>15025</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>179751</td>
      <td>35960</td>
      <td>47089</td>
      <td>35960</td>
      <td>143791</td>
      <td>30079</td>
      <td>24698</td>
      <td>22391</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>132719</td>
      <td>27463</td>
      <td>41042</td>
      <td>27463</td>
      <td>105256</td>
      <td>21885</td>
      <td>23263</td>
      <td>17779</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>113236</td>
      <td>23990</td>
      <td>36654</td>
      <td>23990</td>
      <td>89246</td>
      <td>18722</td>
      <td>21688</td>
      <td>14966</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>111819</td>
      <td>24636</td>
      <td>34889</td>
      <td>24636</td>
      <td>87183</td>
      <td>18599</td>
      <td>21245</td>
      <td>13644</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>145650</td>
      <td>29840</td>
      <td>37963</td>
      <td>29840</td>
      <td>115810</td>
      <td>24930</td>
      <td>19764</td>
      <td>18199</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>46206</td>
      <td>11354</td>
      <td>25701</td>
      <td>11354</td>
      <td>34852</td>
      <td>7264</td>
      <td>18840</td>
      <td>6861</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>120833</td>
      <td>23373</td>
      <td>32629</td>
      <td>23373</td>
      <td>97460</td>
      <td>19862</td>
      <td>17539</td>
      <td>15090</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_protei...</td>
      <td>147650</td>
      <td>29788</td>
      <td>37946</td>
      <td>29788</td>
      <td>117862</td>
      <td>24643</td>
      <td>20871</td>
      <td>17075</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_protein...</td>
      <td>99844</td>
      <td>21457</td>
      <td>36555</td>
      <td>21457</td>
      <td>78387</td>
      <td>15947</td>
      <td>23379</td>
      <td>13176</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>169705</td>
      <td>34124</td>
      <td>42371</td>
      <td>34124</td>
      <td>135581</td>
      <td>28864</td>
      <td>21386</td>
      <td>20985</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_protei...</td>
      <td>116960</td>
      <td>21707</td>
      <td>27591</td>
      <td>21707</td>
      <td>95253</td>
      <td>18324</td>
      <td>14027</td>
      <td>13564</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_pro...</td>
      <td>131245</td>
      <td>28332</td>
      <td>32676</td>
      <td>28332</td>
      <td>102913</td>
      <td>21946</td>
      <td>18600</td>
      <td>14076</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_prote...</td>
      <td>74722</td>
      <td>13502</td>
      <td>19942</td>
      <td>13502</td>
      <td>61220</td>
      <td>11116</td>
      <td>10811</td>
      <td>9131</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_pro...</td>
      <td>160234</td>
      <td>31145</td>
      <td>37219</td>
      <td>31145</td>
      <td>129089</td>
      <td>26163</td>
      <td>19600</td>
      <td>17619</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_prot...</td>
      <td>194730</td>
      <td>39643</td>
      <td>42976</td>
      <td>39643</td>
      <td>155087</td>
      <td>32778</td>
      <td>22396</td>
      <td>20580</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>97211</td>
      <td>21350</td>
      <td>39165</td>
      <td>21350</td>
      <td>75861</td>
      <td>14600</td>
      <td>26303</td>
      <td>12862</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>100654</td>
      <td>21284</td>
      <td>32049</td>
      <td>21284</td>
      <td>79370</td>
      <td>15607</td>
      <td>20041</td>
      <td>12008</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_pro...</td>
      <td>191973</td>
      <td>38634</td>
      <td>39785</td>
      <td>38634</td>
      <td>153339</td>
      <td>33012</td>
      <td>18865</td>
      <td>20920</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>111846</td>
      <td>20815</td>
      <td>30631</td>
      <td>20815</td>
      <td>91031</td>
      <td>17251</td>
      <td>16694</td>
      <td>13937</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>188868</td>
      <td>36370</td>
      <td>40220</td>
      <td>36370</td>
      <td>152498</td>
      <td>30739</td>
      <td>19857</td>
      <td>20363</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_protein...</td>
      <td>60749</td>
      <td>14338</td>
      <td>29417</td>
      <td>14338</td>
      <td>46411</td>
      <td>9710</td>
      <td>20198</td>
      <td>9219</td>
    </tr>
  </tbody>
</table>
</div>


# Step 8 — Link Peptide–Protein Evidence to Wheat Gene Models

This step links the non-contaminant peptide–protein evidence tables generated in Step 7 to wheat gene model annotations derived from the IWGSC RefSeq v2.1 GFF3 files.

The purpose of this step is to connect FragPipe protein accessions to their corresponding wheat gene models, transcripts, and genomic annotation features.

---

## Input files

### Peptide–protein evidence tables from Step 7

One file per tissue:

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_protein_evidence.csv
```

### Protein-to-gene mapping table from Step 5

```text
wheat_protein_gene_mapping_HC_LC.csv
```

This table was generated by parsing the high-confidence and low-confidence wheat GFF3 annotation files.

---

## Mapping strategy

Each peptide–protein evidence row was merged with the protein-to-gene mapping table using:

```text
ProteinID
```

This links each identified protein accession to available gene model annotation fields, including transcript and gene identifiers.

---

## Mapping status

A mapping status column was added to retain unmatched entries for audit purposes.

| Status | Description |
|---|---|
| mapped | ProteinID was found in the GFF3-derived protein-to-gene mapping table |
| unmapped | ProteinID was not found in the protein-to-gene mapping table |

Unmapped proteins were retained rather than discarded so that mapping completeness could be evaluated across tissues.

---

## Output files

One peptide–protein–gene mapping table was exported per tissue.

### Example output

```text
FragPipe_Duncan_PXD004720_anther_peptide_protein_gene_mapping.csv
```

### Output directory

```text
python_outputs/tables/
```

---

## Summary metrics

A Step 8 summary table was generated across all tissues.

### Metrics captured

| Metric | Description |
|---|---|
| Peptide_protein_pairs | Total number of peptide–protein evidence rows |
| Mapped_peptide_protein_pairs | Number of peptide–protein rows successfully linked to gene models |
| Unmapped_peptide_protein_pairs | Number of peptide–protein rows not linked to gene models |
| Mapping_rate_percent | Percentage of peptide–protein rows successfully mapped |
| Unique_peptides | Number of unique peptide sequences |
| Unique_proteins | Number of unique protein accessions |
| Mapped_unique_proteins | Number of unique protein accessions successfully mapped |
| Unmapped_unique_proteins | Number of unique protein accessions not mapped |
| Unique_gene_models | Number of unique gene models identified |
| Unique_transcripts | Number of unique transcripts identified |

### Output summary file

```text
wheat_peptide_protein_gene_mapping_summary_step8.csv
```

This mapped table is used in the next step to project peptide positions from protein coordinates onto wheat genomic coordinates.


```python
# ============================================================
# Step 8 — Link peptide–protein evidence to wheat gene models
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

step8_summary_out = tables_dir / "wheat_peptide_protein_gene_mapping_summary_step8.csv"

# -----------------------------
# 2. Load manifest and protein-to-gene mapping table
# -----------------------------
manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")
protein_gene_mapping = pd.read_csv(protein_gene_mapping_file)

print("Protein-to-gene mapping table loaded:")
print(f"Rows: {protein_gene_mapping.shape[0]:,}")
print(f"Columns: {protein_gene_mapping.shape[1]:,}")

display(protein_gene_mapping.head())


# -----------------------------
# 3. Helper function
# -----------------------------
def map_peptide_protein_to_gene_models(source, tissue_raw_code):
    """
    Merge one tissue-level peptide–protein evidence table with the
    GFF3-derived wheat protein-to-gene mapping table.

    Parameters
    ----------
    source : str
        Proteomics dataset source, e.g. "PXD004720".

    tissue_raw_code : str
        Tissue code as listed in the manifest, e.g. "anther".

    Returns
    -------
    pd.DataFrame
        Peptide–protein–gene evidence table.
    """

    # Find matching manifest row
    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(
            f"No manifest entry found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    if len(match) > 1:
        raise ValueError(
            f"Multiple manifest entries found for Source='{source}' and "
            f"Tissue-Raw-Code='{tissue_raw_code}'."
        )

    row = match.iloc[0]

    # Input Step 7 evidence file
    evidence_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_evidence.csv"
    )

    evidence_path = tables_dir / evidence_filename

    if not evidence_path.exists():
        raise FileNotFoundError(f"Step 7 evidence file not found: {evidence_path}")

    evidence = pd.read_csv(evidence_path)

    if "ProteinID" not in evidence.columns:
        raise KeyError(f"'ProteinID' column not found in {evidence_filename}")

    if "ProteinID" not in protein_gene_mapping.columns:
        raise KeyError("'ProteinID' column not found in protein-to-gene mapping table.")

    # Merge peptide–protein evidence with GFF3-derived mapping
    mapped = evidence.merge(
        protein_gene_mapping,
        on="ProteinID",
        how="left",
        indicator=True
    )

    mapped["Gene_model_mapping_status"] = mapped["_merge"].map({
        "both": "mapped",
        "left_only": "unmapped",
        "right_only": "mapping_only"
    })

    mapped = mapped.drop(columns=["_merge"])

    # Add sequential index
    if "Index" in mapped.columns:
        mapped = mapped.drop(columns=["Index"])

    mapped.insert(0, "Index", range(1, len(mapped) + 1))

    # Save output
    output_filename = evidence_filename.replace(
        "_peptide_protein_evidence.csv",
        "_peptide_protein_gene_mapping.csv"
    )

    output_path = tables_dir / output_filename
    mapped.to_csv(output_path, index=False)

    # Mapping summary
    total_pairs = len(mapped)
    mapped_pairs = (mapped["Gene_model_mapping_status"] == "mapped").sum()
    unmapped_pairs = (mapped["Gene_model_mapping_status"] == "unmapped").sum()

    print(f"\nSaved peptide–protein–gene mapping table: {output_path}")
    print(f"Rows: {total_pairs:,}")
    print(f"Mapped pairs: {mapped_pairs:,}")
    print(f"Unmapped pairs: {unmapped_pairs:,}")

    return mapped


# -----------------------------
# 4. Run Step 8 for all tissues
# -----------------------------
step8_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    mapped = map_peptide_protein_to_gene_models(
        source=source,
        tissue_raw_code=tissue_raw_code
    )

    output_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_gene_mapping.csv"
    )

    total_pairs = len(mapped)
    mapped_pairs = (mapped["Gene_model_mapping_status"] == "mapped").sum()
    unmapped_pairs = (mapped["Gene_model_mapping_status"] == "unmapped").sum()

    step8_summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue_raw_code,
        "Batch": batch,
        "Gene_mapping_file": output_filename,
        "Peptide_protein_pairs": total_pairs,
        "Mapped_peptide_protein_pairs": mapped_pairs,
        "Unmapped_peptide_protein_pairs": unmapped_pairs,
        "Mapping_rate_percent": round((mapped_pairs / total_pairs) * 100, 2) if total_pairs > 0 else 0,
        "Unique_peptides": mapped["Peptide"].nunique() if "Peptide" in mapped.columns else pd.NA,
        "Unique_proteins": mapped["ProteinID"].nunique() if "ProteinID" in mapped.columns else pd.NA,
        "Mapped_unique_proteins": mapped.loc[
            mapped["Gene_model_mapping_status"] == "mapped", "ProteinID"
        ].nunique(),
        "Unmapped_unique_proteins": mapped.loc[
            mapped["Gene_model_mapping_status"] == "unmapped", "ProteinID"
        ].nunique(),
        "Unique_gene_models": mapped["GeneID"].nunique() if "GeneID" in mapped.columns else pd.NA,
        "Unique_transcripts": mapped["TranscriptID"].nunique() if "TranscriptID" in mapped.columns else pd.NA
    })

step8_summary = pd.DataFrame(step8_summary_records)

# Save Step 8 summary
step8_summary.to_csv(step8_summary_out, index=False)

print(f"\nStep 8 summary saved: {step8_summary_out}")
print(f"Summary rows: {step8_summary.shape[0]:,}")

display(step8_summary)
```

    C:\Users\Owner\AppData\Local\Temp\ipykernel_10260\2744825148.py:25: DtypeWarning: Columns (17,19) have mixed types. Specify dtype option on import or set low_memory=False.
      protein_gene_mapping = pd.read_csv(protein_gene_mapping_file)
    

    Protein-to-gene mapping table loaded:
    Rows: 295,914
    Columns: 24
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ProteinID</th>
      <th>GeneModel</th>
      <th>TranscriptID</th>
      <th>Chromosome</th>
      <th>Strand</th>
      <th>Gene_start</th>
      <th>Gene_end</th>
      <th>Transcript_start</th>
      <th>Transcript_end</th>
      <th>CDS_start</th>
      <th>...</th>
      <th>CDS_phase_values</th>
      <th>Annotation_confidence</th>
      <th>Gene_Name</th>
      <th>Gene_biotype</th>
      <th>Transcript_Name</th>
      <th>Transcript_biotype</th>
      <th>ProteinID_found_in_GFF3</th>
      <th>GeneModel_found_in_GFF3</th>
      <th>Has_gene_coordinates</th>
      <th>Has_transcript_coordinates</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>TraesCS1A03G0000200.1</td>
      <td>TraesCS1A03G0000200</td>
      <td>TraesCS1A03G0000200.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>40098</td>
      <td>70338</td>
      <td>40098</td>
      <td>70338</td>
      <td>58508</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000200</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000200.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TraesCS1A03G0000400.1</td>
      <td>TraesCS1A03G0000400</td>
      <td>TraesCS1A03G0000400.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>70239</td>
      <td>89245</td>
      <td>70239</td>
      <td>89245</td>
      <td>70239</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000400</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000400.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>TraesCS1A03G0000600.1</td>
      <td>TraesCS1A03G0000600</td>
      <td>TraesCS1A03G0000600.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>95906</td>
      <td>104903</td>
      <td>95906</td>
      <td>104903</td>
      <td>104607</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000600</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000600.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>TraesCS1A03G0000800.1</td>
      <td>TraesCS1A03G0000800</td>
      <td>TraesCS1A03G0000800.1</td>
      <td>Chr1A</td>
      <td>+</td>
      <td>102794</td>
      <td>122504</td>
      <td>102794</td>
      <td>122504</td>
      <td>121263</td>
      <td>...</td>
      <td>0</td>
      <td>HC</td>
      <td>TraesCS1A03G0000800</td>
      <td>NaN</td>
      <td>TraesCS1A03G0000800.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TraesCS1A03G0001000.1</td>
      <td>TraesCS1A03G0001000</td>
      <td>TraesCS1A03G0001000.1</td>
      <td>Chr1A</td>
      <td>-</td>
      <td>149490</td>
      <td>154559</td>
      <td>149490</td>
      <td>154559</td>
      <td>149490</td>
      <td>...</td>
      <td>0; 2</td>
      <td>HC</td>
      <td>TraesCS1A03G0001000</td>
      <td>NaN</td>
      <td>TraesCS1A03G0001000.1</td>
      <td>NaN</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>


    
    Processing MSV000090572 | stored_grain
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Vincent_MSV000090572_stored-grain_peptide_protein_gene_mapping.csv
    Rows: 30,317
    Mapped pairs: 30,314
    Unmapped pairs: 3
    
    Processing PXD050500 | coleoptile
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Liu_PXD050500_coleoptile_peptide_protein_gene_mapping.csv
    Rows: 1,850,247
    Mapped pairs: 1,850,136
    Unmapped pairs: 111
    
    Processing PXD050500 | node
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Liu_PXD050500_node_peptide_protein_gene_mapping.csv
    Rows: 1,887,009
    Mapped pairs: 1,886,922
    Unmapped pairs: 87
    
    Processing PXD050500 | radicle
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_peptide_protein_gene_mapping.csv
    Rows: 1,062,587
    Mapped pairs: 1,062,508
    Unmapped pairs: 79
    
    Processing PXD004720 | anther
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_anther_peptide_protein_gene_mapping.csv
    Rows: 164,397
    Mapped pairs: 164,365
    Unmapped pairs: 32
    
    Processing PXD004720 | boot
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_boot_peptide_protein_gene_mapping.csv
    Rows: 13,230
    Mapped pairs: 13,227
    Unmapped pairs: 3
    
    Processing PXD004720 | coleoptile
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_coleoptile_peptide_protein_gene_mapping.csv
    Rows: 204,518
    Mapped pairs: 204,476
    Unmapped pairs: 42
    
    Processing PXD004720 | embryo
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_embryo_peptide_protein_gene_mapping.csv
    Rows: 8,852
    Mapped pairs: 8,852
    Unmapped pairs: 0
    
    Processing PXD004720 | endosperm
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_endosperm_peptide_protein_gene_mapping.csv
    Rows: 102,845
    Mapped pairs: 102,830
    Unmapped pairs: 15
    
    Processing PXD004720 | glume
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_glume_peptide_protein_gene_mapping.csv
    Rows: 145,154
    Mapped pairs: 145,133
    Unmapped pairs: 21
    
    Processing PXD004720 | grain-zadoks-70
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_protein_gene_mapping.csv
    Rows: 126,227
    Mapped pairs: 126,195
    Unmapped pairs: 32
    
    Processing PXD004720 | grain-zadoks-71
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_protein_gene_mapping.csv
    Rows: 179,751
    Mapped pairs: 179,725
    Unmapped pairs: 26
    
    Processing PXD004720 | grain-zadoks-75
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_protein_gene_mapping.csv
    Rows: 132,719
    Mapped pairs: 132,701
    Unmapped pairs: 18
    
    Processing PXD004720 | grain-zadoks-83
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_protein_gene_mapping.csv
    Rows: 113,236
    Mapped pairs: 113,203
    Unmapped pairs: 33
    
    Processing PXD004720 | grain-zadoks-87
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_protein_gene_mapping.csv
    Rows: 111,819
    Mapped pairs: 111,792
    Unmapped pairs: 27
    
    Processing PXD004720 | leaf-flag-mature
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_protein_gene_mapping.csv
    Rows: 145,650
    Mapped pairs: 145,632
    Unmapped pairs: 18
    
    Processing PXD004720 | leaf-flag-senescing
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_protein_gene_mapping.csv
    Rows: 46,206
    Mapped pairs: 46,200
    Unmapped pairs: 6
    
    Processing PXD004720 | leaf-flag-young
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_protein_gene_mapping.csv
    Rows: 120,833
    Mapped pairs: 120,821
    Unmapped pairs: 12
    
    Processing PXD004720 | lemma
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_lemma_peptide_protein_gene_mapping.csv
    Rows: 147,650
    Mapped pairs: 147,618
    Unmapped pairs: 32
    
    Processing PXD004720 | node
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_node_peptide_protein_gene_mapping.csv
    Rows: 99,844
    Mapped pairs: 99,823
    Unmapped pairs: 21
    
    Processing PXD004720 | node_secretion
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_node-secretion_peptide_protein_gene_mapping.csv
    Rows: 169,705
    Mapped pairs: 169,675
    Unmapped pairs: 30
    
    Processing PXD004720 | palea
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_palea_peptide_protein_gene_mapping.csv
    Rows: 116,960
    Mapped pairs: 116,936
    Unmapped pairs: 24
    
    Processing PXD004720 | pericarp
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_pericarp_peptide_protein_gene_mapping.csv
    Rows: 131,245
    Mapped pairs: 131,215
    Unmapped pairs: 30
    
    Processing PXD004720 | pollen
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_pollen_peptide_protein_gene_mapping.csv
    Rows: 74,722
    Mapped pairs: 74,698
    Unmapped pairs: 24
    
    Processing PXD004720 | rachilla
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_rachilla_peptide_protein_gene_mapping.csv
    Rows: 160,234
    Mapped pairs: 160,204
    Unmapped pairs: 30
    
    Processing PXD004720 | radicle
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_radicle_peptide_protein_gene_mapping.csv
    Rows: 194,730
    Mapped pairs: 194,694
    Unmapped pairs: 36
    
    Processing PXD004720 | root-mature
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-mature_peptide_protein_gene_mapping.csv
    Rows: 97,211
    Mapped pairs: 97,188
    Unmapped pairs: 23
    
    Processing PXD004720 | root-secretion
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-secretion_peptide_protein_gene_mapping.csv
    Rows: 100,654
    Mapped pairs: 100,639
    Unmapped pairs: 15
    
    Processing PXD004720 | root-tip
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-tip_peptide_protein_gene_mapping.csv
    Rows: 191,973
    Mapped pairs: 191,943
    Unmapped pairs: 30
    
    Processing PXD004720 | root-vasculature
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_root-vasculature_peptide_protein_gene_mapping.csv
    Rows: 111,846
    Mapped pairs: 111,831
    Unmapped pairs: 15
    
    Processing PXD004720 | spike-immature
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_spike-immature_peptide_protein_gene_mapping.csv
    Rows: 188,868
    Mapped pairs: 188,826
    Unmapped pairs: 42
    
    Processing PXD004720 | stem
    
    Saved peptide–protein–gene mapping table: python_outputs\tables\FragPipe_Duncan_PXD004720_stem_peptide_protein_gene_mapping.csv
    Rows: 60,749
    Mapped pairs: 60,734
    Unmapped pairs: 15
    
    Step 8 summary saved: python_outputs\tables\wheat_peptide_protein_gene_mapping_summary_step8.csv
    Summary rows: 32
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Gene_mapping_file</th>
      <th>Peptide_protein_pairs</th>
      <th>Mapped_peptide_protein_pairs</th>
      <th>Unmapped_peptide_protein_pairs</th>
      <th>Mapping_rate_percent</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins</th>
      <th>Mapped_unique_proteins</th>
      <th>Unmapped_unique_proteins</th>
      <th>Unique_gene_models</th>
      <th>Unique_transcripts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>30317</td>
      <td>30314</td>
      <td>3</td>
      <td>99.99</td>
      <td>9329</td>
      <td>17481</td>
      <td>17478</td>
      <td>3</td>
      <td>&lt;NA&gt;</td>
      <td>17478</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_prot...</td>
      <td>1850247</td>
      <td>1850136</td>
      <td>111</td>
      <td>99.99</td>
      <td>582775</td>
      <td>239514</td>
      <td>239461</td>
      <td>53</td>
      <td>&lt;NA&gt;</td>
      <td>239461</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_protein_ge...</td>
      <td>1887009</td>
      <td>1886922</td>
      <td>87</td>
      <td>100.00</td>
      <td>595954</td>
      <td>242842</td>
      <td>242813</td>
      <td>29</td>
      <td>&lt;NA&gt;</td>
      <td>242813</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_protein...</td>
      <td>1062587</td>
      <td>1062508</td>
      <td>79</td>
      <td>99.99</td>
      <td>333058</td>
      <td>206049</td>
      <td>206016</td>
      <td>33</td>
      <td>&lt;NA&gt;</td>
      <td>206016</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_prote...</td>
      <td>164397</td>
      <td>164365</td>
      <td>32</td>
      <td>99.98</td>
      <td>34098</td>
      <td>36839</td>
      <td>36826</td>
      <td>13</td>
      <td>&lt;NA&gt;</td>
      <td>36826</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_protein...</td>
      <td>13230</td>
      <td>13227</td>
      <td>3</td>
      <td>99.98</td>
      <td>3643</td>
      <td>9211</td>
      <td>9208</td>
      <td>3</td>
      <td>&lt;NA&gt;</td>
      <td>9208</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_p...</td>
      <td>204518</td>
      <td>204476</td>
      <td>42</td>
      <td>99.98</td>
      <td>41025</td>
      <td>46513</td>
      <td>46496</td>
      <td>17</td>
      <td>&lt;NA&gt;</td>
      <td>46496</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_prote...</td>
      <td>8852</td>
      <td>8852</td>
      <td>0</td>
      <td>100.00</td>
      <td>2867</td>
      <td>7220</td>
      <td>7220</td>
      <td>0</td>
      <td>&lt;NA&gt;</td>
      <td>7220</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_pr...</td>
      <td>102845</td>
      <td>102830</td>
      <td>15</td>
      <td>99.99</td>
      <td>20081</td>
      <td>27461</td>
      <td>27454</td>
      <td>7</td>
      <td>&lt;NA&gt;</td>
      <td>27454</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_protei...</td>
      <td>145154</td>
      <td>145133</td>
      <td>21</td>
      <td>99.99</td>
      <td>28648</td>
      <td>35551</td>
      <td>35540</td>
      <td>11</td>
      <td>&lt;NA&gt;</td>
      <td>35540</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>126227</td>
      <td>126195</td>
      <td>32</td>
      <td>99.97</td>
      <td>26196</td>
      <td>35549</td>
      <td>35532</td>
      <td>17</td>
      <td>&lt;NA&gt;</td>
      <td>35532</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>179751</td>
      <td>179725</td>
      <td>26</td>
      <td>99.99</td>
      <td>35960</td>
      <td>47089</td>
      <td>47076</td>
      <td>13</td>
      <td>&lt;NA&gt;</td>
      <td>47076</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>132719</td>
      <td>132701</td>
      <td>18</td>
      <td>99.99</td>
      <td>27463</td>
      <td>41042</td>
      <td>41029</td>
      <td>13</td>
      <td>&lt;NA&gt;</td>
      <td>41029</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>113236</td>
      <td>113203</td>
      <td>33</td>
      <td>99.97</td>
      <td>23990</td>
      <td>36654</td>
      <td>36635</td>
      <td>19</td>
      <td>&lt;NA&gt;</td>
      <td>36635</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>111819</td>
      <td>111792</td>
      <td>27</td>
      <td>99.98</td>
      <td>24636</td>
      <td>34889</td>
      <td>34874</td>
      <td>15</td>
      <td>&lt;NA&gt;</td>
      <td>34874</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>145650</td>
      <td>145632</td>
      <td>18</td>
      <td>99.99</td>
      <td>29840</td>
      <td>37963</td>
      <td>37954</td>
      <td>9</td>
      <td>&lt;NA&gt;</td>
      <td>37954</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>46206</td>
      <td>46200</td>
      <td>6</td>
      <td>99.99</td>
      <td>11354</td>
      <td>25701</td>
      <td>25696</td>
      <td>5</td>
      <td>&lt;NA&gt;</td>
      <td>25696</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>120833</td>
      <td>120821</td>
      <td>12</td>
      <td>99.99</td>
      <td>23373</td>
      <td>32629</td>
      <td>32620</td>
      <td>9</td>
      <td>&lt;NA&gt;</td>
      <td>32620</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_protei...</td>
      <td>147650</td>
      <td>147618</td>
      <td>32</td>
      <td>99.98</td>
      <td>29788</td>
      <td>37946</td>
      <td>37927</td>
      <td>19</td>
      <td>&lt;NA&gt;</td>
      <td>37927</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_protein...</td>
      <td>99844</td>
      <td>99823</td>
      <td>21</td>
      <td>99.98</td>
      <td>21457</td>
      <td>36555</td>
      <td>36542</td>
      <td>13</td>
      <td>&lt;NA&gt;</td>
      <td>36542</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>169705</td>
      <td>169675</td>
      <td>30</td>
      <td>99.98</td>
      <td>34124</td>
      <td>42371</td>
      <td>42356</td>
      <td>15</td>
      <td>&lt;NA&gt;</td>
      <td>42356</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_protei...</td>
      <td>116960</td>
      <td>116936</td>
      <td>24</td>
      <td>99.98</td>
      <td>21707</td>
      <td>27591</td>
      <td>27580</td>
      <td>11</td>
      <td>&lt;NA&gt;</td>
      <td>27580</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_pro...</td>
      <td>131245</td>
      <td>131215</td>
      <td>30</td>
      <td>99.98</td>
      <td>28332</td>
      <td>32676</td>
      <td>32667</td>
      <td>9</td>
      <td>&lt;NA&gt;</td>
      <td>32667</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_prote...</td>
      <td>74722</td>
      <td>74698</td>
      <td>24</td>
      <td>99.97</td>
      <td>13502</td>
      <td>19942</td>
      <td>19931</td>
      <td>11</td>
      <td>&lt;NA&gt;</td>
      <td>19931</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_pro...</td>
      <td>160234</td>
      <td>160204</td>
      <td>30</td>
      <td>99.98</td>
      <td>31145</td>
      <td>37219</td>
      <td>37204</td>
      <td>15</td>
      <td>&lt;NA&gt;</td>
      <td>37204</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_prot...</td>
      <td>194730</td>
      <td>194694</td>
      <td>36</td>
      <td>99.98</td>
      <td>39643</td>
      <td>42976</td>
      <td>42965</td>
      <td>11</td>
      <td>&lt;NA&gt;</td>
      <td>42965</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>97211</td>
      <td>97188</td>
      <td>23</td>
      <td>99.98</td>
      <td>21350</td>
      <td>39165</td>
      <td>39156</td>
      <td>9</td>
      <td>&lt;NA&gt;</td>
      <td>39156</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>100654</td>
      <td>100639</td>
      <td>15</td>
      <td>99.99</td>
      <td>21284</td>
      <td>32049</td>
      <td>32046</td>
      <td>3</td>
      <td>&lt;NA&gt;</td>
      <td>32046</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_pro...</td>
      <td>191973</td>
      <td>191943</td>
      <td>30</td>
      <td>99.98</td>
      <td>38634</td>
      <td>39785</td>
      <td>39774</td>
      <td>11</td>
      <td>&lt;NA&gt;</td>
      <td>39774</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>111846</td>
      <td>111831</td>
      <td>15</td>
      <td>99.99</td>
      <td>20815</td>
      <td>30631</td>
      <td>30626</td>
      <td>5</td>
      <td>&lt;NA&gt;</td>
      <td>30626</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>188868</td>
      <td>188826</td>
      <td>42</td>
      <td>99.98</td>
      <td>36370</td>
      <td>40220</td>
      <td>40207</td>
      <td>13</td>
      <td>&lt;NA&gt;</td>
      <td>40207</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_protein...</td>
      <td>60749</td>
      <td>60734</td>
      <td>15</td>
      <td>99.98</td>
      <td>14338</td>
      <td>29417</td>
      <td>29410</td>
      <td>7</td>
      <td>&lt;NA&gt;</td>
      <td>29410</td>
    </tr>
  </tbody>
</table>
</div>


# Step 9 — Project Identified Peptides onto Wheat Genomic Coordinates

This step projects identified non-contaminant peptides from protein coordinates onto wheat genomic coordinates using the IWGSC RefSeq v2.1 genome annotation.

The aim is to convert peptide-level proteomics evidence into genome browser-compatible coordinate information for downstream BED file generation and JBrowse visualisation.

To improve computational efficiency on standard desktop hardware, CDS annotation features were pre-indexed into transcript-level dictionaries prior to peptide projection. This substantially reduced repeated scanning of the large wheat GFF3 annotation table (>2.8 million rows).

---

## Input files

### Peptide–protein–gene mapping tables from Step 8

One file per tissue:

`FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_protein_gene_mapping.csv`

### Protein FASTA database

`iwgsc_refseqv2.1_annotation_200916_HC_LC_pep_cRAP_with_DECOY.fasta`

### Parsed GFF3 feature table from Step 5

`wheat_gff3_parsed_features_HC_LC.csv`

---

## Projection strategy

Genomic coding coordinate vectors were reconstructed directly from ordered CDS intervals extracted from the GFF3 annotation. CDS phase values were retained from the annotation for reference but were not used to trim CDS nucleotide coordinates during peptide projection, because CDS features already define coding sequence boundaries. This ensured continuous exon-aware reconstruction of transcript coding coordinates prior to peptide genomic projection.

For each peptide–protein–transcript entry, the workflow:

1. Locates the peptide amino acid sequence within the corresponding protein sequence.
2. Converts the peptide amino acid interval into coding nucleotide positions.
3. Retrieves the CDS blocks associated with the corresponding transcript.
4. Projects coding nucleotide positions onto genomic coordinates.
5. Collapses projected nucleotide positions into genomic blocks.
6. Generates an intron-aware peptide display label in which exon-spanning junctions are explicitly shown using dash characters.

This allows peptides spanning CDS junctions to be represented as multi-block genomic features and labelled in JBrowse with an explicit visual indication of intron-spanning structure.

---

## Intron-aware peptide labels

For peptides projected across more than one CDS block, an additional display field is generated:

`Peptide_intron_gapped`

This field preserves the original peptide sequence but inserts dash characters at positions where the peptide crosses an intron.

Example:

`AFVVPGLTDADGVGYVAQ--------------------------------------GEGVLTVIENGEKR`

This makes exon-spanning peptides easier to interpret in Apollo/JBrowse, particularly for visualising peptide-supported splice structures across CDS boundaries.

For peptides contained within a single CDS block, `Peptide_intron_gapped` is identical to the original peptide sequence.

---

## Coordinate systems

Both biological and BED-compatible coordinate systems were retained.

| Coordinate field | Description |
|---|---|
| `Genomic_start_1based` | Genomic start coordinate using 1-based inclusive coordinates |
| `Genomic_end_1based` | Genomic end coordinate using 1-based inclusive coordinates |
| `BED_start_0based` | BED-compatible 0-based start coordinate |
| `BED_end_0based_exclusive` | BED-compatible end coordinate |
| `BED_block_count` | Number of genomic blocks covered by the peptide |
| `BED_block_sizes` | BED12-compatible block sizes |
| `BED_block_starts` | BED12-compatible block starts relative to feature start |
| `Peptide_intron_gapped` | Peptide label with dash characters inserted across intron-spanning junctions |

---

## Projection status

A projection status column was added to support quality control and computational validation of peptide genomic projections.

| Status | Description |
|---|---|
| `projected` | Peptide was successfully projected onto genomic coordinates |
| `protein_sequence_not_found` | Protein accession was not found in the FASTA database |
| `peptide_not_found_in_protein` | Peptide sequence could not be located in the protein sequence |
| `cds_blocks_not_found` | CDS features could not be found for the transcript |
| `incomplete_coding_projection` | Peptide coding interval could not be fully projected |

Only successfully projected rows are used for BED file generation in the next step.

---

## Output files

One peptide genome projection table was exported per tissue.

Example output:

`FragPipe_Duncan_PXD004720_anther_peptide_genome_projection.csv`

Output directory:

`python_outputs/tables/`

---

## Summary metrics

A Step 9 summary table was generated across all tissues.

| Metric | Description |
|---|---|
| `Peptide_protein_gene_rows` | Number of mapped peptide–protein–gene rows considered |
| `Projected_rows` | Number of rows successfully projected onto genomic coordinates |
| `Unprojected_rows` | Number of rows not successfully projected |
| `Projection_rate_percent` | Percentage of rows successfully projected |
| `Unique_projected_peptides` | Number of unique projected peptide sequences |
| `Unique_projected_proteins` | Number of unique projected proteins |
| `Unique_projected_gene_models` | Number of unique projected gene models |
| `Peptides_crossing_CDS_blocks` | Number of projected peptide rows spanning more than one CDS block |
| `Peptides_with_intron_gapped_label` | Number of projected peptide rows with dash-containing intron-aware labels |

Output summary file:

`wheat_peptide_genome_projection_summary_step9.csv`

Projection accuracy was subsequently validated computationally (Step 9B) by reconstructing genomic coding sequences from projected peptide coordinates, translating the reconstructed sequences, and comparing them against the original peptide sequences. Validation of 10,000 randomly sampled projected peptides demonstrated >98% peptide reconstruction concordance after I/L normalisation, supporting the accuracy of exon-aware coordinate reconstruction, strand handling, and genomic peptide projection.

The projected genomic coordinate tables are used in the next step to generate BED6 and BED12 files for visualisation in Apollo/JBrowse.


```python
# ============================================================
# Step 9 — Peptide-to-genome projection with intron-gapped labels (takes 60 min)
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
fasta_file = Path("protein_database/iwgsc_refseqv2.1_annotation_200916_HC_LC_pep_cRAP_with_DECOY.fasta")
gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

step9_summary_out = tables_dir / "wheat_peptide_genome_projection_summary_step9.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 2. FASTA reader
# -----------------------------
def read_fasta_sequences(fasta_path):
    sequences = {}
    current_id = None
    current_seq = []

    with open(fasta_path, "r", encoding="utf-8", errors="ignore") as handle:
        for line in handle:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequences[current_id] = "".join(current_seq)

                current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)

        if current_id is not None:
            sequences[current_id] = "".join(current_seq)

    return sequences


# -----------------------------
# 3. Build CDS dictionary once
# -----------------------------
def build_cds_dictionary(gff3_features_file):
    usecols = [
        "SeqID",
        "FeatureType",
        "Start",
        "End",
        "Strand",
        "Phase",
        "Parent"
    ]

    gff = pd.read_csv(
        gff3_features_file,
        usecols=usecols,
        low_memory=False
    )

    cds = gff[gff["FeatureType"].astype(str).str.lower() == "cds"].copy()

    cds["Start"] = cds["Start"].astype(int)
    cds["End"] = cds["End"].astype(int)
    cds["Phase"] = pd.to_numeric(cds["Phase"], errors="coerce").fillna(0).astype(int)

    cds_dict = {}

    for transcript_id, group in cds.groupby("Parent", sort=False):

        strand = group["Strand"].iloc[0]

        if strand == "+":
            group = group.sort_values(["Start", "End"])
        else:
            group = group.sort_values(["End", "Start"], ascending=[False, False])

        cds_dict[transcript_id] = group[[
            "SeqID",
            "Start",
            "End",
            "Strand",
            "Phase"
        ]].to_dict("records")

    return cds_dict


# -----------------------------
# 4. Projection helpers
# -----------------------------
def locate_peptide_in_protein(peptide, protein_sequence):
    peptide_clean = str(peptide).replace("I", "L")
    protein_clean = str(protein_sequence).replace("I", "L")

    start_0based = protein_clean.find(peptide_clean)

    if start_0based == -1:
        return None, None, 0

    occurrence_count = protein_clean.count(peptide_clean)

    aa_start = start_0based + 1
    aa_end = aa_start + len(peptide_clean) - 1

    return aa_start, aa_end, occurrence_count


def build_coding_position_vector_from_blocks(cds_blocks):
    """
    Build transcript-ordered genomic coding positions from CDS blocks.

    Important:
    The GFF3 Phase field is NOT used to trim CDS coordinates here.
    CDS features already define the coding sequence. Phase describes
    codon continuity across CDS features, but bases should not be removed
    when reconstructing peptide genomic positions.
    """
    coding_positions = []

    for block in cds_blocks:
        start = int(block["Start"])
        end = int(block["End"])
        strand = block["Strand"]

        if strand == "+":
            coding_positions.extend(range(start, end + 1))
        else:
            coding_positions.extend(range(end, start - 1, -1))

    return coding_positions


def collapse_positions_to_blocks(genomic_positions):
    if len(genomic_positions) == 0:
        return []

    sorted_positions = sorted(genomic_positions)

    blocks = []
    block_start = sorted_positions[0]
    previous = sorted_positions[0]

    for pos in sorted_positions[1:]:
        if pos == previous + 1:
            previous = pos
        else:
            blocks.append((block_start, previous))
            block_start = pos
            previous = pos

    blocks.append((block_start, previous))

    return blocks


def build_intron_gapped_peptide_from_nt_positions(
    peptide,
    peptide_nt_positions,
    exact_dash_count=True,
    max_dashes=80
):
    """
    Builds a display peptide sequence with dashes inserted where the peptide
    crosses introns.

    The peptide split is based on the actual nucleotide positions contributing
    to each amino acid codon, so the exon boundary placement is exact at
    amino-acid resolution.

    If exact_dash_count=True:
        number of dashes = intron length in nucleotides.
    If exact_dash_count=False:
        dashes are capped to max_dashes for easier JBrowse display.
    """

    peptide = str(peptide)

    if len(peptide_nt_positions) != len(peptide) * 3:
        return peptide

    parts = []

    for aa_index, aa in enumerate(peptide):
        codon_positions = peptide_nt_positions[aa_index * 3:(aa_index + 1) * 3]
        parts.append(aa)

        if aa_index == len(peptide) - 1:
            continue

        next_codon_positions = peptide_nt_positions[(aa_index + 1) * 3:(aa_index + 2) * 3]

        current_genomic_max = max(codon_positions)
        current_genomic_min = min(codon_positions)
        next_genomic_max = max(next_codon_positions)
        next_genomic_min = min(next_codon_positions)

        # Consecutive codons in the same exon are adjacent in genomic space.
        same_exon_forward = next_genomic_min == current_genomic_max + 1
        same_exon_reverse = current_genomic_min == next_genomic_max + 1

        if not (same_exon_forward or same_exon_reverse):

            if next_genomic_min > current_genomic_max:
                intron_nt_len = next_genomic_min - current_genomic_max - 1
            else:
                intron_nt_len = current_genomic_min - next_genomic_max - 1

            if exact_dash_count:
                dash_n = max(1, int(intron_nt_len))
            else:
                dash_n = min(max(3, int(intron_nt_len)), max_dashes)

            parts.append("-" * dash_n)

    return "".join(parts)


# -----------------------------
# 5. Project one tissue
# -----------------------------
def project_one_tissue_peptides_to_genome_fast(source, tissue_raw_code, protein_sequences, cds_dict):

    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(f"No manifest entry found for {source} | {tissue_raw_code}")

    row = match.iloc[0]

    step8_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_protein_gene_mapping.csv"
    )

    step8_path = tables_dir / step8_filename

    mapped = pd.read_csv(step8_path, low_memory=False)

    mapped = mapped[
        mapped["Gene_model_mapping_status"] == "mapped"
    ].copy()

    records = []

    for peptide_row in mapped.itertuples(index=False):

        row_dict = peptide_row._asdict()

        peptide = row_dict["Peptide"]
        protein_id = row_dict["ProteinID"]
        transcript_id = row_dict["TranscriptID"]

        projection_status = "projected"
        peptide_intron_gapped = str(peptide)
        peptide_intron_gapped_compact = str(peptide)

        protein_sequence = protein_sequences.get(protein_id)

        if protein_sequence is None:
            projection_status = "protein_sequence_not_found"
            aa_start = pd.NA
            aa_end = pd.NA
            occurrence_count = pd.NA
            chromosome = pd.NA
            strand = pd.NA
            peptide_blocks = []

        else:
            aa_start, aa_end, occurrence_count = locate_peptide_in_protein(
                peptide,
                protein_sequence
            )

            if aa_start is None:
                projection_status = "peptide_not_found_in_protein"
                aa_start = pd.NA
                aa_end = pd.NA
                chromosome = pd.NA
                strand = pd.NA
                peptide_blocks = []

            else:
                cds_blocks = cds_dict.get(transcript_id)

                if cds_blocks is None:
                    projection_status = "cds_blocks_not_found"
                    chromosome = pd.NA
                    strand = pd.NA
                    peptide_blocks = []

                else:
                    coding_positions = build_coding_position_vector_from_blocks(cds_blocks)

                    nt_start = (int(aa_start) - 1) * 3
                    nt_end = int(aa_end) * 3

                    peptide_nt_positions = coding_positions[nt_start:nt_end]

                    chromosome = cds_blocks[0]["SeqID"]
                    strand = cds_blocks[0]["Strand"]

                    if len(peptide_nt_positions) != len(str(peptide)) * 3:
                        projection_status = "incomplete_coding_projection"
                        peptide_blocks = []
                    else:
                        peptide_blocks = collapse_positions_to_blocks(peptide_nt_positions)

                        # Full-resolution label for BED/JBrowse
                        peptide_intron_gapped = build_intron_gapped_peptide_from_nt_positions(
                            peptide=peptide,
                            peptide_nt_positions=peptide_nt_positions,
                            exact_dash_count=True
                        )
                        
                        # Compact label for CSV storage / downstream loading
                        peptide_intron_gapped_compact = build_intron_gapped_peptide_from_nt_positions(
                            peptide=peptide,
                            peptide_nt_positions=peptide_nt_positions,
                            exact_dash_count=False,
                            max_dashes=10
                        )

        if peptide_blocks:
            genomic_start_1based = min(start for start, end in peptide_blocks)
            genomic_end_1based = max(end for start, end in peptide_blocks)

            bed_start = genomic_start_1based - 1
            bed_end = genomic_end_1based

            block_count = len(peptide_blocks)
            block_sizes = ",".join(str(end - start + 1) for start, end in peptide_blocks)
            block_starts = ",".join(str(start - genomic_start_1based) for start, end in peptide_blocks)

        else:
            genomic_start_1based = pd.NA
            genomic_end_1based = pd.NA
            bed_start = pd.NA
            bed_end = pd.NA
            block_count = 0
            block_sizes = ""
            block_starts = ""

        row_dict.update({
            "AA_start": aa_start,
            "AA_end": aa_end,
            "Peptide_length_AA": len(str(peptide)),
            "Peptide_occurrences_in_protein": occurrence_count,
            "Peptide_intron_gapped": peptide_intron_gapped,
            "Peptide_intron_gapped_compact": peptide_intron_gapped_compact,
            "Chromosome": chromosome,
            "Strand": strand,
            "Genomic_start_1based": genomic_start_1based,
            "Genomic_end_1based": genomic_end_1based,
            "BED_start_0based": bed_start,
            "BED_end_0based_exclusive": bed_end,
            "BED_block_count": block_count,
            "BED_block_sizes": block_sizes,
            "BED_block_starts": block_starts,
            "Projection_status": projection_status
        })

        records.append(row_dict)

    projected = pd.DataFrame(records)

    if "Index" in projected.columns:
        projected = projected.drop(columns=["Index"])

    projected.insert(0, "Index", range(1, len(projected) + 1))

    output_filename = step8_filename.replace(
        "_peptide_protein_gene_mapping.csv",
        "_peptide_genome_projection.csv"
    )

    output_path = tables_dir / output_filename
    projected.to_csv(output_path, index=False)

    print(f"\nSaved: {output_path}")
    print(projected["Projection_status"].value_counts(dropna=False))

    unprojected = projected[
        projected["Projection_status"] != "projected"
    ].copy()

    unprojected_filename = output_filename.replace(
        "_peptide_genome_projection.csv",
        "_unprojected_peptides_for_tblastn.csv"
    )

    unprojected_path = tables_dir / unprojected_filename
    unprojected.to_csv(unprojected_path, index=False)

    print(f"Unprojected peptide table saved: {unprojected_path}")
    print(f"Unprojected rows: {len(unprojected):,}")

    return projected


# -----------------------------
# 6. Pre-load large resources once
# -----------------------------
print("Loading protein FASTA...")
protein_sequences = read_fasta_sequences(fasta_file)
print(f"Protein sequences loaded: {len(protein_sequences):,}")

print("Building CDS dictionary...")
cds_dict = build_cds_dictionary(gff3_features_file)
print(f"Transcript CDS entries loaded: {len(cds_dict):,}")

# # -----------------------------
# # 7-test. Run Step 9 on one tissue only
# # -----------------------------

# test_source = "PXD004720"
# test_tissue = "embryo"

# print(f"\nTEST RUN — Step 9 projection for one tissue only:")
# print(f"Source: {test_source}")
# print(f"Tissue: {test_tissue}")

# test_projection = project_one_tissue_peptides_to_genome_fast(
#     source=test_source,
#     tissue_raw_code=test_tissue,
#     protein_sequences=protein_sequences,
#     cds_dict=cds_dict
# )

# print("\nTest projection completed.")
# print(f"Rows: {len(test_projection):,}")

# display(test_projection.head())
# display(test_projection["Projection_status"].value_counts(dropna=False))

# -----------------------------
# 7. Run all tissues
# -----------------------------
step9_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    species = row["Species"]
    tissue_raw_code = row["Tissue-Raw-Code"]
    batch = row["Batch"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    projected = project_one_tissue_peptides_to_genome_fast(
        source=source,
        tissue_raw_code=tissue_raw_code,
        protein_sequences=protein_sequences,
        cds_dict=cds_dict
    )

    output_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projected_count = (projected["Projection_status"] == "projected").sum()
    unprojected_count = len(projected) - projected_count

    step9_summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue_raw_code,
        "Batch": batch,
        "Genome_projection_file": output_filename,
        "Peptide_protein_gene_rows": len(projected),
        "Projected_rows": projected_count,
        "Unprojected_rows": unprojected_count,
        "Projection_rate_percent": round((projected_count / len(projected)) * 100, 2) if len(projected) > 0 else 0,
        "Unique_projected_peptides": projected.loc[
            projected["Projection_status"] == "projected", "Peptide"
        ].nunique(),
        "Unique_projected_proteins": projected.loc[
            projected["Projection_status"] == "projected", "ProteinID"
        ].nunique(),
        "Unique_projected_gene_models": projected.loc[
            projected["Projection_status"] == "projected", "GeneID"
        ].nunique() if "GeneID" in projected.columns else pd.NA,
        "Peptides_crossing_CDS_blocks": (
            projected.loc[
                projected["Projection_status"] == "projected", "BED_block_count"
            ] > 1
        ).sum(),
        "Peptides_with_intron_gapped_label": (
            projected.loc[
                projected["Projection_status"] == "projected", "Peptide_intron_gapped"
            ].astype(str).str.contains("-", regex=False)
        ).sum()
    })

step9_summary = pd.DataFrame(step9_summary_records)

step9_summary.to_csv(step9_summary_out, index=False)

print(f"\nStep 9 summary saved: {step9_summary_out}")
display(step9_summary)

```

    Loading protein FASTA...
    Protein sequences loaded: 592,060
    Building CDS dictionary...
    Transcript CDS entries loaded: 295,914
    
    Processing MSV000090572 | stored_grain
    
    Saved: python_outputs\tables\FragPipe_Vincent_MSV000090572_stored-grain_peptide_genome_projection.csv
    Projection_status
    projected    30314
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Vincent_MSV000090572_stored-grain_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD050500 | coleoptile
    
    Saved: python_outputs\tables\FragPipe_Liu_PXD050500_coleoptile_peptide_genome_projection.csv
    Projection_status
    projected    1850136
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Liu_PXD050500_coleoptile_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD050500 | node
    
    Saved: python_outputs\tables\FragPipe_Liu_PXD050500_node_peptide_genome_projection.csv
    Projection_status
    projected    1886922
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Liu_PXD050500_node_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD050500 | radicle
    
    Saved: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_peptide_genome_projection.csv
    Projection_status
    projected    1062508
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Liu_PXD050500_radicle_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | anther
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_anther_peptide_genome_projection.csv
    Projection_status
    projected    164365
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_anther_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | boot
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_boot_peptide_genome_projection.csv
    Projection_status
    projected    13227
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_boot_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | coleoptile
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_coleoptile_peptide_genome_projection.csv
    Projection_status
    projected    204476
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_coleoptile_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | embryo
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_embryo_peptide_genome_projection.csv
    Projection_status
    projected    8852
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_embryo_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | endosperm
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_endosperm_peptide_genome_projection.csv
    Projection_status
    projected    102830
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_endosperm_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | glume
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_glume_peptide_genome_projection.csv
    Projection_status
    projected    145133
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_glume_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | grain-zadoks-70
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_genome_projection.csv
    Projection_status
    projected    126195
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-70_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | grain-zadoks-71
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_genome_projection.csv
    Projection_status
    projected    179725
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-71_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | grain-zadoks-75
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_genome_projection.csv
    Projection_status
    projected    132701
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-75_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | grain-zadoks-83
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_genome_projection.csv
    Projection_status
    projected    113203
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-83_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | grain-zadoks-87
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_genome_projection.csv
    Projection_status
    projected    111792
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_grain-zadoks-87_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | leaf-flag-mature
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_genome_projection.csv
    Projection_status
    projected    145632
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-mature_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | leaf-flag-senescing
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_genome_projection.csv
    Projection_status
    projected    46200
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-senescing_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | leaf-flag-young
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_genome_projection.csv
    Projection_status
    projected    120821
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_leaf-flag-young_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | lemma
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_lemma_peptide_genome_projection.csv
    Projection_status
    projected    147618
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_lemma_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | node
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node_peptide_genome_projection.csv
    Projection_status
    projected    99823
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | node_secretion
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node-secretion_peptide_genome_projection.csv
    Projection_status
    projected    169675
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_node-secretion_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | palea
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_palea_peptide_genome_projection.csv
    Projection_status
    projected    116936
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_palea_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | pericarp
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pericarp_peptide_genome_projection.csv
    Projection_status
    projected    131215
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pericarp_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | pollen
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pollen_peptide_genome_projection.csv
    Projection_status
    projected    74698
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_pollen_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | rachilla
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_rachilla_peptide_genome_projection.csv
    Projection_status
    projected    160204
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_rachilla_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | radicle
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_radicle_peptide_genome_projection.csv
    Projection_status
    projected    194694
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_radicle_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | root-mature
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-mature_peptide_genome_projection.csv
    Projection_status
    projected    97188
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-mature_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | root-secretion
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-secretion_peptide_genome_projection.csv
    Projection_status
    projected    100639
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-secretion_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | root-tip
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-tip_peptide_genome_projection.csv
    Projection_status
    projected    191943
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-tip_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | root-vasculature
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-vasculature_peptide_genome_projection.csv
    Projection_status
    projected    111831
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_root-vasculature_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | spike-immature
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_spike-immature_peptide_genome_projection.csv
    Projection_status
    projected    188826
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_spike-immature_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Processing PXD004720 | stem
    
    Saved: python_outputs\tables\FragPipe_Duncan_PXD004720_stem_peptide_genome_projection.csv
    Projection_status
    projected    60734
    Name: count, dtype: int64
    Unprojected peptide table saved: python_outputs\tables\FragPipe_Duncan_PXD004720_stem_unprojected_peptides_for_tblastn.csv
    Unprojected rows: 0
    
    Step 9 summary saved: python_outputs\tables\wheat_peptide_genome_projection_summary_step9.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Genome_projection_file</th>
      <th>Peptide_protein_gene_rows</th>
      <th>Projected_rows</th>
      <th>Unprojected_rows</th>
      <th>Projection_rate_percent</th>
      <th>Unique_projected_peptides</th>
      <th>Unique_projected_proteins</th>
      <th>Unique_projected_gene_models</th>
      <th>Peptides_crossing_CDS_blocks</th>
      <th>Peptides_with_intron_gapped_label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>30314</td>
      <td>30314</td>
      <td>0</td>
      <td>100.0</td>
      <td>9329</td>
      <td>17478</td>
      <td>&lt;NA&gt;</td>
      <td>3291</td>
      <td>1828</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>1850136</td>
      <td>1850136</td>
      <td>0</td>
      <td>100.0</td>
      <td>582775</td>
      <td>239461</td>
      <td>&lt;NA&gt;</td>
      <td>228372</td>
      <td>122385</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>1886922</td>
      <td>1886922</td>
      <td>0</td>
      <td>100.0</td>
      <td>595954</td>
      <td>242813</td>
      <td>&lt;NA&gt;</td>
      <td>235642</td>
      <td>127047</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>1062508</td>
      <td>1062508</td>
      <td>0</td>
      <td>100.0</td>
      <td>333058</td>
      <td>206016</td>
      <td>&lt;NA&gt;</td>
      <td>118195</td>
      <td>62337</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
      <td>164365</td>
      <td>164365</td>
      <td>0</td>
      <td>100.0</td>
      <td>34098</td>
      <td>36826</td>
      <td>&lt;NA&gt;</td>
      <td>27776</td>
      <td>16150</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
      <td>13227</td>
      <td>13227</td>
      <td>0</td>
      <td>100.0</td>
      <td>3643</td>
      <td>9208</td>
      <td>&lt;NA&gt;</td>
      <td>2728</td>
      <td>1537</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
      <td>204476</td>
      <td>204476</td>
      <td>0</td>
      <td>100.0</td>
      <td>41025</td>
      <td>46496</td>
      <td>&lt;NA&gt;</td>
      <td>31344</td>
      <td>18679</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
      <td>8852</td>
      <td>8852</td>
      <td>0</td>
      <td>100.0</td>
      <td>2867</td>
      <td>7220</td>
      <td>&lt;NA&gt;</td>
      <td>1411</td>
      <td>760</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
      <td>102830</td>
      <td>102830</td>
      <td>0</td>
      <td>100.0</td>
      <td>20081</td>
      <td>27454</td>
      <td>&lt;NA&gt;</td>
      <td>14269</td>
      <td>7971</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
      <td>145133</td>
      <td>145133</td>
      <td>0</td>
      <td>100.0</td>
      <td>28648</td>
      <td>35540</td>
      <td>&lt;NA&gt;</td>
      <td>22131</td>
      <td>12759</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>126195</td>
      <td>126195</td>
      <td>0</td>
      <td>100.0</td>
      <td>26196</td>
      <td>35532</td>
      <td>&lt;NA&gt;</td>
      <td>17478</td>
      <td>9892</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>179725</td>
      <td>179725</td>
      <td>0</td>
      <td>100.0</td>
      <td>35960</td>
      <td>47076</td>
      <td>&lt;NA&gt;</td>
      <td>27658</td>
      <td>15967</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>132701</td>
      <td>132701</td>
      <td>0</td>
      <td>100.0</td>
      <td>27463</td>
      <td>41029</td>
      <td>&lt;NA&gt;</td>
      <td>18650</td>
      <td>10504</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>113203</td>
      <td>113203</td>
      <td>0</td>
      <td>100.0</td>
      <td>23990</td>
      <td>36635</td>
      <td>&lt;NA&gt;</td>
      <td>14734</td>
      <td>8452</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>111792</td>
      <td>111792</td>
      <td>0</td>
      <td>100.0</td>
      <td>24636</td>
      <td>34874</td>
      <td>&lt;NA&gt;</td>
      <td>14886</td>
      <td>8402</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>145632</td>
      <td>145632</td>
      <td>0</td>
      <td>100.0</td>
      <td>29840</td>
      <td>37954</td>
      <td>&lt;NA&gt;</td>
      <td>19448</td>
      <td>11285</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>46200</td>
      <td>46200</td>
      <td>0</td>
      <td>100.0</td>
      <td>11354</td>
      <td>25696</td>
      <td>&lt;NA&gt;</td>
      <td>4572</td>
      <td>2415</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>120821</td>
      <td>120821</td>
      <td>0</td>
      <td>100.0</td>
      <td>23373</td>
      <td>32620</td>
      <td>&lt;NA&gt;</td>
      <td>15227</td>
      <td>8981</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
      <td>147618</td>
      <td>147618</td>
      <td>0</td>
      <td>100.0</td>
      <td>29788</td>
      <td>37927</td>
      <td>&lt;NA&gt;</td>
      <td>21753</td>
      <td>12440</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
      <td>99823</td>
      <td>99823</td>
      <td>0</td>
      <td>100.0</td>
      <td>21457</td>
      <td>36542</td>
      <td>&lt;NA&gt;</td>
      <td>12765</td>
      <td>7108</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>169675</td>
      <td>169675</td>
      <td>0</td>
      <td>100.0</td>
      <td>34124</td>
      <td>42356</td>
      <td>&lt;NA&gt;</td>
      <td>22888</td>
      <td>13292</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
      <td>116936</td>
      <td>116936</td>
      <td>0</td>
      <td>100.0</td>
      <td>21707</td>
      <td>27580</td>
      <td>&lt;NA&gt;</td>
      <td>20681</td>
      <td>12105</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
      <td>131215</td>
      <td>131215</td>
      <td>0</td>
      <td>100.0</td>
      <td>28332</td>
      <td>32667</td>
      <td>&lt;NA&gt;</td>
      <td>20964</td>
      <td>11953</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
      <td>74698</td>
      <td>74698</td>
      <td>0</td>
      <td>100.0</td>
      <td>13502</td>
      <td>19931</td>
      <td>&lt;NA&gt;</td>
      <td>9490</td>
      <td>5338</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_gen...</td>
      <td>160204</td>
      <td>160204</td>
      <td>0</td>
      <td>100.0</td>
      <td>31145</td>
      <td>37204</td>
      <td>&lt;NA&gt;</td>
      <td>24784</td>
      <td>14463</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_geno...</td>
      <td>194694</td>
      <td>194694</td>
      <td>0</td>
      <td>100.0</td>
      <td>39643</td>
      <td>42965</td>
      <td>&lt;NA&gt;</td>
      <td>32499</td>
      <td>19061</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>97188</td>
      <td>97188</td>
      <td>0</td>
      <td>100.0</td>
      <td>21350</td>
      <td>39156</td>
      <td>&lt;NA&gt;</td>
      <td>10898</td>
      <td>6135</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>100639</td>
      <td>100639</td>
      <td>0</td>
      <td>100.0</td>
      <td>21284</td>
      <td>32046</td>
      <td>&lt;NA&gt;</td>
      <td>15547</td>
      <td>8991</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_gen...</td>
      <td>191943</td>
      <td>191943</td>
      <td>0</td>
      <td>100.0</td>
      <td>38634</td>
      <td>39774</td>
      <td>&lt;NA&gt;</td>
      <td>35031</td>
      <td>21057</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>111831</td>
      <td>111831</td>
      <td>0</td>
      <td>100.0</td>
      <td>20815</td>
      <td>30626</td>
      <td>&lt;NA&gt;</td>
      <td>14833</td>
      <td>8183</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>188826</td>
      <td>188826</td>
      <td>0</td>
      <td>100.0</td>
      <td>36370</td>
      <td>40207</td>
      <td>&lt;NA&gt;</td>
      <td>33193</td>
      <td>19376</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>60734</td>
      <td>60734</td>
      <td>0</td>
      <td>100.0</td>
      <td>14338</td>
      <td>29410</td>
      <td>&lt;NA&gt;</td>
      <td>6949</td>
      <td>3980</td>
    </tr>
  </tbody>
</table>
</div>



```python
# Testing intron annotation at the peptide level
test_gapped = projected[
    projected["Peptide_intron_gapped"].astype(str).str.contains("-", regex=False)
][["Peptide", "Peptide_intron_gapped", "BED_block_count", "BED_block_sizes", "BED_block_starts"]]

display(test_gapped.head(20))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Peptide</th>
      <th>Peptide_intron_gapped</th>
      <th>BED_block_count</th>
      <th>BED_block_sizes</th>
      <th>BED_block_starts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202</th>
      <td>AAAAAGEPQNGKR</td>
      <td>AAAAAGE------------------PQNGKR</td>
      <td>2</td>
      <td>18,21</td>
      <td>0,36</td>
    </tr>
    <tr>
      <th>309</th>
      <td>AAAAEGDLDLQAK</td>
      <td>AAAAE-----------------------------------------...</td>
      <td>2</td>
      <td>15,24</td>
      <td>0,1904</td>
    </tr>
    <tr>
      <th>310</th>
      <td>AAAAEGDLDLQAK</td>
      <td>AAAAE-----------------------------------------...</td>
      <td>2</td>
      <td>15,24</td>
      <td>0,1120</td>
    </tr>
    <tr>
      <th>311</th>
      <td>AAAAEGDLDLQAK</td>
      <td>AAAAE-----------------------------------------...</td>
      <td>2</td>
      <td>15,24</td>
      <td>0,2111</td>
    </tr>
    <tr>
      <th>314</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,964</td>
    </tr>
    <tr>
      <th>315</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,964</td>
    </tr>
    <tr>
      <th>316</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,964</td>
    </tr>
    <tr>
      <th>317</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,964</td>
    </tr>
    <tr>
      <th>318</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1019</td>
    </tr>
    <tr>
      <th>319</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1019</td>
    </tr>
    <tr>
      <th>320</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1019</td>
    </tr>
    <tr>
      <th>321</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1019</td>
    </tr>
    <tr>
      <th>322</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1019</td>
    </tr>
    <tr>
      <th>323</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1019</td>
    </tr>
    <tr>
      <th>324</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1018</td>
    </tr>
    <tr>
      <th>325</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1018</td>
    </tr>
    <tr>
      <th>326</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1018</td>
    </tr>
    <tr>
      <th>327</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1018</td>
    </tr>
    <tr>
      <th>328</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1018</td>
    </tr>
    <tr>
      <th>329</th>
      <td>AAAAGAAPSGGPVFKSGPLFISSK</td>
      <td>AAAAGAAPSGGP----------------------------------...</td>
      <td>2</td>
      <td>36,36</td>
      <td>0,1018</td>
    </tr>
  </tbody>
</table>
</div>


# Step 10 — Positional validation of annotation-guided peptide genome projections

This step validates a stratified random subset of peptide genome projections generated in Step 9.

---

The validation tests whether projected genomic coordinates can reconstruct the original peptide sequence. For each sampled projected peptide, the workflow:

1. Reads the peptide genomic coordinates from the Step 9 projection tables.
2. Extracts the corresponding genomic DNA sequence from the wheat reference genome.
3. Reconstructs the spliced coding sequence using the BED block structure.
4. Reverse-complements the sequence when the peptide maps to the negative strand.
5. Translates the reconstructed coding DNA sequence.
6. Compares the translated amino acid sequence with the original FragPipe peptide sequence.

This provides a direct validation of the annotation-guided projection logic, including:

- exon-aware block reconstruction,
- splice-junction handling,
- strand-aware sequence recovery,
- peptide-level coordinate accuracy.

Unlike heuristic alignment approaches, this strategy computationally confirms that projected genomic coordinates can regenerate the experimentally observed peptide sequence.

---

Because the complete projection dataset contains millions of peptide–protein associations, a memory-efficient stratified sampling strategy is used to ensure representation across all tissues and data sources while remaining computationally feasible on a standard 8 GB RAM laptop.

For each projection file (source/tissue combination):

- only rows with `Projection_status = projected` are considered,
- a random 10% subset of projected peptide rows is sampled,
- validation is performed independently for each tissue/source dataset.

This ensures that:

- all tissues contribute to the validation,
- small datasets are not overwhelmed by larger datasets,
- validation remains biologically representative across the entire workflow.

---

Two matching criteria are reported:

- `Exact_match`  
  The translated peptide is identical to the original peptide sequence.

- `IL_normalised_match`  
  The translated peptide matches after converting both I and L to L, because tandem mass spectrometry usually cannot distinguish isoleucine from leucine.

The I/L-normalised comparison is considered the biologically relevant validation criterion.

---

The workflow also records:

- reconstructed CDS nucleotide length,
- validation status categories,
- multi-block (exon-spanning) peptide projections,
- negative-strand peptide projections.

This allows independent assessment of complex projection scenarios such as splice-junction peptides and reverse-strand gene models.

---

The output files are:

- `wheat_projection_validation_stratified10percent_step10.csv`
- `wheat_projection_validation_summary_step10.csv`
- `wheat_projection_validation_tissue_summary_step10.csv`


```python
# # install python library
# !pip install pyfaidx
```


```python
# ============================================================
# Step 10 — Validate peptide genome projections by translation (takes 5 min)
# Stratified 10% per tissue/source, memory-light version
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path
import re

# -----------------------------
# 1. User settings
# -----------------------------
tables_dir = Path("python_outputs/tables")
genome_fasta = Path("genome_annotation/iwgsc_refseqv2.1_assembly.fa")

sample_fraction = 0.10
chunk_size = 25_000
random_seed = 42

validation_out = tables_dir / "wheat_projection_validation_stratified10percent_step10.csv"
summary_out = tables_dir / "wheat_projection_validation_summary_step10.csv"
tissue_summary_out = tables_dir / "wheat_projection_validation_tissue_summary_step10.csv"

# Clear previous output if rerunning
if validation_out.exists():
    validation_out.unlink()

# -----------------------------
# 2. Check pyfaidx availability
# -----------------------------
try:
    from pyfaidx import Fasta
except ImportError:
    raise ImportError(
        "Install pyfaidx first:\n\npip install pyfaidx"
    )

# -----------------------------
# 3. Find projection files
# -----------------------------
projection_files = sorted(tables_dir.glob("*_peptide_genome_projection.csv"))

if len(projection_files) == 0:
    raise FileNotFoundError(
        f"No Step 9 projection files found in: {tables_dir}"
    )

print(f"Projection files found: {len(projection_files)}")

if not genome_fasta.exists():
    raise FileNotFoundError(f"Genome FASTA not found:\n{genome_fasta}")

# -----------------------------
# 4. Helper functions
# -----------------------------
def clean_peptide_sequence(seq):
    seq = str(seq).upper()
    seq = re.sub(r"[^ACDEFGHIKLMNPQRSTVWY]", "", seq)
    return seq


def il_normalise(seq):
    return str(seq).upper().replace("I", "L")


def reverse_complement(seq):
    complement = str.maketrans("ACGTNacgtn", "TGCANtgcan")
    return str(seq).translate(complement)[::-1].upper()


genetic_code = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def translate_dna(seq):
    seq = str(seq).upper()
    return "".join(
        genetic_code.get(seq[i:i + 3], "X")
        for i in range(0, len(seq) - 2, 3)
    )


def parse_bed_blocks(row):
    feature_start_1based = int(row["BED_start_0based"]) + 1

    sizes = [
        int(x) for x in str(row["BED_block_sizes"]).strip(",").split(",")
        if str(x).strip() != ""
    ]

    starts = [
        int(x) for x in str(row["BED_block_starts"]).strip(",").split(",")
        if str(x).strip() != ""
    ]

    if len(sizes) != len(starts):
        return []

    return [
        (feature_start_1based + rel_start,
         feature_start_1based + rel_start + size - 1)
        for size, rel_start in zip(sizes, starts)
    ]


def extract_projected_cds(row, genome):
    chrom = str(row["Chromosome"])
    strand = str(row["Strand"])

    blocks = parse_bed_blocks(row)

    if len(blocks) == 0:
        return ""

    seq_parts = []

    for start, end in blocks:
        seq_parts.append(genome[chrom][start - 1:end].seq)

    cds_seq = "".join(seq_parts).upper()

    if strand == "-":
        cds_seq = reverse_complement(cds_seq)

    return cds_seq


def validate_projection_row(row_dict, genome):
    peptide = clean_peptide_sequence(row_dict["Peptide"])
    validation_status = "validated"

    try:
        cds_seq = extract_projected_cds(row_dict, genome)
        translated = translate_dna(cds_seq)

        exact_match = translated == peptide
        il_match = il_normalise(translated) == il_normalise(peptide)

        expected_nt_length = len(peptide) * 3
        observed_nt_length = len(cds_seq)

        if observed_nt_length != expected_nt_length:
            validation_status = "length_mismatch"
        elif "N" in cds_seq:
            validation_status = "contains_N"
        elif not il_match:
            validation_status = "translation_mismatch"

    except KeyError:
        cds_seq = ""
        translated = ""
        exact_match = False
        il_match = False
        expected_nt_length = len(peptide) * 3
        observed_nt_length = 0
        validation_status = "chromosome_not_found_in_genome_fasta"

    except Exception as e:
        cds_seq = ""
        translated = ""
        exact_match = False
        il_match = False
        expected_nt_length = len(peptide) * 3
        observed_nt_length = 0
        validation_status = f"error: {type(e).__name__}"

    row_dict.update({
        "Original_peptide_clean": peptide,
        "Reconstructed_CDS_length_nt": observed_nt_length,
        "Expected_CDS_length_nt": expected_nt_length,
        "Translated_projected_peptide": translated,
        "Exact_match": exact_match,
        "IL_normalised_match": il_match,
        "Validation_status": validation_status
    })

    return row_dict


# -----------------------------
# 5. Required columns
# -----------------------------
required_cols = [
    "Source",
    "Species",
    "Tissue",
    "Batch",
    "Peptide",
    "ProteinID",
    "TranscriptID",
    "GeneModel",
    "Annotation_confidence",
    "Chromosome",
    "Strand",
    "AA_start",
    "AA_end",
    "BED_start_0based",
    "BED_end_0based_exclusive",
    "BED_block_count",
    "BED_block_sizes",
    "BED_block_starts",
    "Projection_status"
]

# -----------------------------
# 6. Open genome FASTA
# -----------------------------
print("\nOpening indexed genome FASTA...")

# Use rebuild=True only the first time. Afterwards, rebuild=False is faster.
genome = Fasta(str(genome_fasta), rebuild=False)

print(f"Genome sequences available: {len(genome.keys()):,}")

# -----------------------------
# 7. Validate stratified 10% per projection file
# -----------------------------
rng = np.random.default_rng(random_seed)

overall_records = []
tissue_summary_records = []
header_written = False

print("\nValidating stratified 10% sample per tissue/source...")

for file_i, projection_file in enumerate(projection_files, start=1):

    print(f"\n[{file_i}/{len(projection_files)}] {projection_file.name}")

    header = pd.read_csv(projection_file, nrows=0)
    available_cols = [c for c in required_cols if c in header.columns]

    file_total_projected = 0
    file_sampled = 0
    file_exact = 0
    file_il = 0
    file_multiblock = 0
    file_negative = 0
    file_status_counts = {}

    for chunk_i, chunk in enumerate(
        pd.read_csv(
            projection_file,
            usecols=available_cols,
            chunksize=chunk_size,
            low_memory=True
        ),
        start=1
    ):

        if "Projection_status" not in chunk.columns:
            continue

        chunk = chunk[chunk["Projection_status"] == "projected"].copy()

        if chunk.empty:
            continue

        file_total_projected += len(chunk)

        # Stratified 10% sample within this file/chunk
        sampled = chunk.sample(
            frac=sample_fraction,
            random_state=random_seed + file_i + chunk_i
        ).copy()

        if sampled.empty:
            continue

        sampled["_source_file"] = projection_file.name

        validation_records = []

        for row in sampled.itertuples(index=False):
            row_dict = row._asdict()
            validation_records.append(validate_projection_row(row_dict, genome))

        validation_chunk = pd.DataFrame(validation_records)

        # Update counters
        file_sampled += len(validation_chunk)
        file_exact += int(validation_chunk["Exact_match"].sum())
        file_il += int(validation_chunk["IL_normalised_match"].sum())
        file_multiblock += int(
            (pd.to_numeric(validation_chunk["BED_block_count"], errors="coerce") > 1).sum()
        )
        file_negative += int((validation_chunk["Strand"].astype(str) == "-").sum())

        for status, count in validation_chunk["Validation_status"].value_counts().items():
            file_status_counts[status] = file_status_counts.get(status, 0) + int(count)

        # Append to CSV immediately
        validation_chunk.to_csv(
            validation_out,
            index=False,
            mode="a",
            header=not header_written
        )

        header_written = True

        print(
            f"  Chunk {chunk_i}: sampled {len(validation_chunk):,} "
            f"| cumulative sampled {file_sampled:,}"
        )

    tissue_summary_records.append({
        "Projection_file": projection_file.name,
        "Projected_rows_available": file_total_projected,
        "Sample_fraction": sample_fraction,
        "Rows_validated": file_sampled,
        "Exact_translation_matches": file_exact,
        "Exact_translation_match_rate_percent": round((file_exact / file_sampled) * 100, 2) if file_sampled > 0 else pd.NA,
        "IL_normalised_translation_matches": file_il,
        "IL_normalised_translation_match_rate_percent": round((file_il / file_sampled) * 100, 2) if file_sampled > 0 else pd.NA,
        "Multi_block_peptide_projections_tested": file_multiblock,
        "Negative_strand_peptide_projections_tested": file_negative,
        **{f"Validation_status_{k}": v for k, v in file_status_counts.items()}
    })

# -----------------------------
# 8. Build final summaries
# -----------------------------
tissue_summary = pd.DataFrame(tissue_summary_records)
tissue_summary.to_csv(tissue_summary_out, index=False)

total_validated = int(tissue_summary["Rows_validated"].sum())
total_exact = int(tissue_summary["Exact_translation_matches"].sum())
total_il = int(tissue_summary["IL_normalised_translation_matches"].sum())
total_multiblock = int(tissue_summary["Multi_block_peptide_projections_tested"].sum())
total_negative = int(tissue_summary["Negative_strand_peptide_projections_tested"].sum())

summary_records = [
    {"Metric": "Sampling strategy", "Value": "10% stratified per projection file/source-tissue"},
    {"Metric": "Sample fraction", "Value": sample_fraction},
    {"Metric": "Projection files validated", "Value": len(tissue_summary)},
    {"Metric": "Projected rows available across files", "Value": int(tissue_summary["Projected_rows_available"].sum())},
    {"Metric": "Projected peptide rows validated", "Value": total_validated},
    {"Metric": "Exact translation matches", "Value": total_exact},
    {"Metric": "Exact translation match rate (%)", "Value": round((total_exact / total_validated) * 100, 2) if total_validated > 0 else pd.NA},
    {"Metric": "I/L-normalised translation matches", "Value": total_il},
    {"Metric": "I/L-normalised translation match rate (%)", "Value": round((total_il / total_validated) * 100, 2) if total_validated > 0 else pd.NA},
    {"Metric": "Multi-block peptide projections tested", "Value": total_multiblock},
    {"Metric": "Negative-strand peptide projections tested", "Value": total_negative}
]

status_cols = [c for c in tissue_summary.columns if c.startswith("Validation_status_")]

for col in status_cols:
    summary_records.append({
        "Metric": col.replace("Validation_status_", "Validation status: "),
        "Value": int(tissue_summary[col].fillna(0).sum())
    })

summary_df = pd.DataFrame(summary_records)
summary_df.to_csv(summary_out, index=False)

print("\n===== STEP 10 STRATIFIED VALIDATION SUMMARY =====")
display(summary_df)

print(f"\nValidation table saved: {validation_out}")
print(f"Tissue-level validation summary saved: {tissue_summary_out}")
print(f"Overall validation summary saved: {summary_out}")
```

    Projection files found: 32
    
    Opening indexed genome FASTA...
    Genome sequences available: 22
    
    Validating stratified 10% sample per tissue/source...
    
    [1/32] FragPipe_Duncan_PXD004720_anther_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 1,436 | cumulative sampled 16,436
    
    [2/32] FragPipe_Duncan_PXD004720_boot_peptide_genome_projection.csv
      Chunk 1: sampled 1,323 | cumulative sampled 1,323
    
    [3/32] FragPipe_Duncan_PXD004720_coleoptile_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 2,500 | cumulative sampled 20,000
      Chunk 9: sampled 448 | cumulative sampled 20,448
    
    [4/32] FragPipe_Duncan_PXD004720_embryo_peptide_genome_projection.csv
      Chunk 1: sampled 885 | cumulative sampled 885
    
    [5/32] FragPipe_Duncan_PXD004720_endosperm_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 283 | cumulative sampled 10,283
    
    [6/32] FragPipe_Duncan_PXD004720_glume_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,013 | cumulative sampled 14,513
    
    [7/32] FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 120 | cumulative sampled 12,620
    
    [8/32] FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 472 | cumulative sampled 17,972
    
    [9/32] FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 770 | cumulative sampled 13,270
    
    [10/32] FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 1,320 | cumulative sampled 11,320
    
    [11/32] FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 1,179 | cumulative sampled 11,179
    
    [12/32] FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,063 | cumulative sampled 14,563
    
    [13/32] FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,120 | cumulative sampled 4,620
    
    [14/32] FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,082 | cumulative sampled 12,082
    
    [15/32] FragPipe_Duncan_PXD004720_lemma_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,262 | cumulative sampled 14,762
    
    [16/32] FragPipe_Duncan_PXD004720_node-secretion_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 1,968 | cumulative sampled 16,968
    
    [17/32] FragPipe_Duncan_PXD004720_node_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,482 | cumulative sampled 9,982
    
    [18/32] FragPipe_Duncan_PXD004720_palea_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 1,694 | cumulative sampled 11,694
    
    [19/32] FragPipe_Duncan_PXD004720_pericarp_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 622 | cumulative sampled 13,122
    
    [20/32] FragPipe_Duncan_PXD004720_pollen_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,470 | cumulative sampled 7,470
    
    [21/32] FragPipe_Duncan_PXD004720_rachilla_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 1,020 | cumulative sampled 16,020
    
    [22/32] FragPipe_Duncan_PXD004720_radicle_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 1,969 | cumulative sampled 19,469
    
    [23/32] FragPipe_Duncan_PXD004720_root-mature_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,219 | cumulative sampled 9,719
    
    [24/32] FragPipe_Duncan_PXD004720_root-secretion_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 64 | cumulative sampled 10,064
    
    [25/32] FragPipe_Duncan_PXD004720_root-tip_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 1,694 | cumulative sampled 19,194
    
    [26/32] FragPipe_Duncan_PXD004720_root-vasculature_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 1,183 | cumulative sampled 11,183
    
    [27/32] FragPipe_Duncan_PXD004720_spike-immature_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 1,383 | cumulative sampled 18,883
    
    [28/32] FragPipe_Duncan_PXD004720_stem_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 1,073 | cumulative sampled 6,073
    
    [29/32] FragPipe_Liu_PXD050500_coleoptile_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 2,500 | cumulative sampled 20,000
      Chunk 9: sampled 2,500 | cumulative sampled 22,500
      Chunk 10: sampled 2,500 | cumulative sampled 25,000
      Chunk 11: sampled 2,500 | cumulative sampled 27,500
      Chunk 12: sampled 2,500 | cumulative sampled 30,000
      Chunk 13: sampled 2,500 | cumulative sampled 32,500
      Chunk 14: sampled 2,500 | cumulative sampled 35,000
      Chunk 15: sampled 2,500 | cumulative sampled 37,500
      Chunk 16: sampled 2,500 | cumulative sampled 40,000
      Chunk 17: sampled 2,500 | cumulative sampled 42,500
      Chunk 18: sampled 2,500 | cumulative sampled 45,000
      Chunk 19: sampled 2,500 | cumulative sampled 47,500
      Chunk 20: sampled 2,500 | cumulative sampled 50,000
      Chunk 21: sampled 2,500 | cumulative sampled 52,500
      Chunk 22: sampled 2,500 | cumulative sampled 55,000
      Chunk 23: sampled 2,500 | cumulative sampled 57,500
      Chunk 24: sampled 2,500 | cumulative sampled 60,000
      Chunk 25: sampled 2,500 | cumulative sampled 62,500
      Chunk 26: sampled 2,500 | cumulative sampled 65,000
      Chunk 27: sampled 2,500 | cumulative sampled 67,500
      Chunk 28: sampled 2,500 | cumulative sampled 70,000
      Chunk 29: sampled 2,500 | cumulative sampled 72,500
      Chunk 30: sampled 2,500 | cumulative sampled 75,000
      Chunk 31: sampled 2,500 | cumulative sampled 77,500
      Chunk 32: sampled 2,500 | cumulative sampled 80,000
      Chunk 33: sampled 2,500 | cumulative sampled 82,500
      Chunk 34: sampled 2,500 | cumulative sampled 85,000
      Chunk 35: sampled 2,500 | cumulative sampled 87,500
      Chunk 36: sampled 2,500 | cumulative sampled 90,000
      Chunk 37: sampled 2,500 | cumulative sampled 92,500
      Chunk 38: sampled 2,500 | cumulative sampled 95,000
      Chunk 39: sampled 2,500 | cumulative sampled 97,500
      Chunk 40: sampled 2,500 | cumulative sampled 100,000
      Chunk 41: sampled 2,500 | cumulative sampled 102,500
      Chunk 42: sampled 2,500 | cumulative sampled 105,000
      Chunk 43: sampled 2,500 | cumulative sampled 107,500
      Chunk 44: sampled 2,500 | cumulative sampled 110,000
      Chunk 45: sampled 2,500 | cumulative sampled 112,500
      Chunk 46: sampled 2,500 | cumulative sampled 115,000
      Chunk 47: sampled 2,500 | cumulative sampled 117,500
      Chunk 48: sampled 2,500 | cumulative sampled 120,000
      Chunk 49: sampled 2,500 | cumulative sampled 122,500
      Chunk 50: sampled 2,500 | cumulative sampled 125,000
      Chunk 51: sampled 2,500 | cumulative sampled 127,500
      Chunk 52: sampled 2,500 | cumulative sampled 130,000
      Chunk 53: sampled 2,500 | cumulative sampled 132,500
      Chunk 54: sampled 2,500 | cumulative sampled 135,000
      Chunk 55: sampled 2,500 | cumulative sampled 137,500
      Chunk 56: sampled 2,500 | cumulative sampled 140,000
      Chunk 57: sampled 2,500 | cumulative sampled 142,500
      Chunk 58: sampled 2,500 | cumulative sampled 145,000
      Chunk 59: sampled 2,500 | cumulative sampled 147,500
      Chunk 60: sampled 2,500 | cumulative sampled 150,000
      Chunk 61: sampled 2,500 | cumulative sampled 152,500
      Chunk 62: sampled 2,500 | cumulative sampled 155,000
      Chunk 63: sampled 2,500 | cumulative sampled 157,500
      Chunk 64: sampled 2,500 | cumulative sampled 160,000
      Chunk 65: sampled 2,500 | cumulative sampled 162,500
      Chunk 66: sampled 2,500 | cumulative sampled 165,000
      Chunk 67: sampled 2,500 | cumulative sampled 167,500
      Chunk 68: sampled 2,500 | cumulative sampled 170,000
      Chunk 69: sampled 2,500 | cumulative sampled 172,500
      Chunk 70: sampled 2,500 | cumulative sampled 175,000
      Chunk 71: sampled 2,500 | cumulative sampled 177,500
      Chunk 72: sampled 2,500 | cumulative sampled 180,000
      Chunk 73: sampled 2,500 | cumulative sampled 182,500
      Chunk 74: sampled 2,500 | cumulative sampled 185,000
      Chunk 75: sampled 14 | cumulative sampled 185,014
    
    [30/32] FragPipe_Liu_PXD050500_node_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 2,500 | cumulative sampled 20,000
      Chunk 9: sampled 2,500 | cumulative sampled 22,500
      Chunk 10: sampled 2,500 | cumulative sampled 25,000
      Chunk 11: sampled 2,500 | cumulative sampled 27,500
      Chunk 12: sampled 2,500 | cumulative sampled 30,000
      Chunk 13: sampled 2,500 | cumulative sampled 32,500
      Chunk 14: sampled 2,500 | cumulative sampled 35,000
      Chunk 15: sampled 2,500 | cumulative sampled 37,500
      Chunk 16: sampled 2,500 | cumulative sampled 40,000
      Chunk 17: sampled 2,500 | cumulative sampled 42,500
      Chunk 18: sampled 2,500 | cumulative sampled 45,000
      Chunk 19: sampled 2,500 | cumulative sampled 47,500
      Chunk 20: sampled 2,500 | cumulative sampled 50,000
      Chunk 21: sampled 2,500 | cumulative sampled 52,500
      Chunk 22: sampled 2,500 | cumulative sampled 55,000
      Chunk 23: sampled 2,500 | cumulative sampled 57,500
      Chunk 24: sampled 2,500 | cumulative sampled 60,000
      Chunk 25: sampled 2,500 | cumulative sampled 62,500
      Chunk 26: sampled 2,500 | cumulative sampled 65,000
      Chunk 27: sampled 2,500 | cumulative sampled 67,500
      Chunk 28: sampled 2,500 | cumulative sampled 70,000
      Chunk 29: sampled 2,500 | cumulative sampled 72,500
      Chunk 30: sampled 2,500 | cumulative sampled 75,000
      Chunk 31: sampled 2,500 | cumulative sampled 77,500
      Chunk 32: sampled 2,500 | cumulative sampled 80,000
      Chunk 33: sampled 2,500 | cumulative sampled 82,500
      Chunk 34: sampled 2,500 | cumulative sampled 85,000
      Chunk 35: sampled 2,500 | cumulative sampled 87,500
      Chunk 36: sampled 2,500 | cumulative sampled 90,000
      Chunk 37: sampled 2,500 | cumulative sampled 92,500
      Chunk 38: sampled 2,500 | cumulative sampled 95,000
      Chunk 39: sampled 2,500 | cumulative sampled 97,500
      Chunk 40: sampled 2,500 | cumulative sampled 100,000
      Chunk 41: sampled 2,500 | cumulative sampled 102,500
      Chunk 42: sampled 2,500 | cumulative sampled 105,000
      Chunk 43: sampled 2,500 | cumulative sampled 107,500
      Chunk 44: sampled 2,500 | cumulative sampled 110,000
      Chunk 45: sampled 2,500 | cumulative sampled 112,500
      Chunk 46: sampled 2,500 | cumulative sampled 115,000
      Chunk 47: sampled 2,500 | cumulative sampled 117,500
      Chunk 48: sampled 2,500 | cumulative sampled 120,000
      Chunk 49: sampled 2,500 | cumulative sampled 122,500
      Chunk 50: sampled 2,500 | cumulative sampled 125,000
      Chunk 51: sampled 2,500 | cumulative sampled 127,500
      Chunk 52: sampled 2,500 | cumulative sampled 130,000
      Chunk 53: sampled 2,500 | cumulative sampled 132,500
      Chunk 54: sampled 2,500 | cumulative sampled 135,000
      Chunk 55: sampled 2,500 | cumulative sampled 137,500
      Chunk 56: sampled 2,500 | cumulative sampled 140,000
      Chunk 57: sampled 2,500 | cumulative sampled 142,500
      Chunk 58: sampled 2,500 | cumulative sampled 145,000
      Chunk 59: sampled 2,500 | cumulative sampled 147,500
      Chunk 60: sampled 2,500 | cumulative sampled 150,000
      Chunk 61: sampled 2,500 | cumulative sampled 152,500
      Chunk 62: sampled 2,500 | cumulative sampled 155,000
      Chunk 63: sampled 2,500 | cumulative sampled 157,500
      Chunk 64: sampled 2,500 | cumulative sampled 160,000
      Chunk 65: sampled 2,500 | cumulative sampled 162,500
      Chunk 66: sampled 2,500 | cumulative sampled 165,000
      Chunk 67: sampled 2,500 | cumulative sampled 167,500
      Chunk 68: sampled 2,500 | cumulative sampled 170,000
      Chunk 69: sampled 2,500 | cumulative sampled 172,500
      Chunk 70: sampled 2,500 | cumulative sampled 175,000
      Chunk 71: sampled 2,500 | cumulative sampled 177,500
      Chunk 72: sampled 2,500 | cumulative sampled 180,000
      Chunk 73: sampled 2,500 | cumulative sampled 182,500
      Chunk 74: sampled 2,500 | cumulative sampled 185,000
      Chunk 75: sampled 2,500 | cumulative sampled 187,500
      Chunk 76: sampled 1,192 | cumulative sampled 188,692
    
    [31/32] FragPipe_Liu_PXD050500_radicle_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 2,500 | cumulative sampled 5,000
      Chunk 3: sampled 2,500 | cumulative sampled 7,500
      Chunk 4: sampled 2,500 | cumulative sampled 10,000
      Chunk 5: sampled 2,500 | cumulative sampled 12,500
      Chunk 6: sampled 2,500 | cumulative sampled 15,000
      Chunk 7: sampled 2,500 | cumulative sampled 17,500
      Chunk 8: sampled 2,500 | cumulative sampled 20,000
      Chunk 9: sampled 2,500 | cumulative sampled 22,500
      Chunk 10: sampled 2,500 | cumulative sampled 25,000
      Chunk 11: sampled 2,500 | cumulative sampled 27,500
      Chunk 12: sampled 2,500 | cumulative sampled 30,000
      Chunk 13: sampled 2,500 | cumulative sampled 32,500
      Chunk 14: sampled 2,500 | cumulative sampled 35,000
      Chunk 15: sampled 2,500 | cumulative sampled 37,500
      Chunk 16: sampled 2,500 | cumulative sampled 40,000
      Chunk 17: sampled 2,500 | cumulative sampled 42,500
      Chunk 18: sampled 2,500 | cumulative sampled 45,000
      Chunk 19: sampled 2,500 | cumulative sampled 47,500
      Chunk 20: sampled 2,500 | cumulative sampled 50,000
      Chunk 21: sampled 2,500 | cumulative sampled 52,500
      Chunk 22: sampled 2,500 | cumulative sampled 55,000
      Chunk 23: sampled 2,500 | cumulative sampled 57,500
      Chunk 24: sampled 2,500 | cumulative sampled 60,000
      Chunk 25: sampled 2,500 | cumulative sampled 62,500
      Chunk 26: sampled 2,500 | cumulative sampled 65,000
      Chunk 27: sampled 2,500 | cumulative sampled 67,500
      Chunk 28: sampled 2,500 | cumulative sampled 70,000
      Chunk 29: sampled 2,500 | cumulative sampled 72,500
      Chunk 30: sampled 2,500 | cumulative sampled 75,000
      Chunk 31: sampled 2,500 | cumulative sampled 77,500
      Chunk 32: sampled 2,500 | cumulative sampled 80,000
      Chunk 33: sampled 2,500 | cumulative sampled 82,500
      Chunk 34: sampled 2,500 | cumulative sampled 85,000
      Chunk 35: sampled 2,500 | cumulative sampled 87,500
      Chunk 36: sampled 2,500 | cumulative sampled 90,000
      Chunk 37: sampled 2,500 | cumulative sampled 92,500
      Chunk 38: sampled 2,500 | cumulative sampled 95,000
      Chunk 39: sampled 2,500 | cumulative sampled 97,500
      Chunk 40: sampled 2,500 | cumulative sampled 100,000
      Chunk 41: sampled 2,500 | cumulative sampled 102,500
      Chunk 42: sampled 2,500 | cumulative sampled 105,000
      Chunk 43: sampled 1,251 | cumulative sampled 106,251
    
    [32/32] FragPipe_Vincent_MSV000090572_stored-grain_peptide_genome_projection.csv
      Chunk 1: sampled 2,500 | cumulative sampled 2,500
      Chunk 2: sampled 531 | cumulative sampled 3,031
    
    ===== STEP 10 STRATIFIED VALIDATION SUMMARY =====
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Metric</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sampling strategy</td>
      <td>10% stratified per projection file/source-tissue</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sample fraction</td>
      <td>0.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Projection files validated</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Projected rows available across files</td>
      <td>8291056</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Projected peptide rows validated</td>
      <td>829105</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Exact translation matches</td>
      <td>807879</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Exact translation match rate (%)</td>
      <td>97.44</td>
    </tr>
    <tr>
      <th>7</th>
      <td>I/L-normalised translation matches</td>
      <td>821474</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I/L-normalised translation match rate (%)</td>
      <td>99.08</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Multi-block peptide projections tested</td>
      <td>110390</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Negative-strand peptide projections tested</td>
      <td>423254</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Validation status: validated</td>
      <td>821474</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Validation status: translation_mismatch</td>
      <td>7631</td>
    </tr>
  </tbody>
</table>
</div>


    
    Validation table saved: python_outputs\tables\wheat_projection_validation_stratified10percent_step10.csv
    Tissue-level validation summary saved: python_outputs\tables\wheat_projection_validation_tissue_summary_step10.csv
    Overall validation summary saved: python_outputs\tables\wheat_projection_validation_summary_step10.csv
    

# Step 11 — Export BED6 and BED12 Files for JBrowse

This step converts successfully projected peptide genomic coordinates from Step 9 into BED files for genome browser visualisation.

Both BED6 and BED12 formats were generated for each wheat tissue.

---

## Input files

### Peptide genome projection tables from Step 9

One file per tissue:

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only rows with successful genomic projection were exported.

### Filtering rule

```text
Projection_status == "projected"
```

---

## BED output formats

### BED6

BED6 provides a compact representation of each peptide genomic interval.

| BED6 field | Description |
|---|---|
| chrom | Chromosome or genome sequence ID |
| chromStart | 0-based genomic start coordinate |
| chromEnd | 0-based exclusive genomic end coordinate |
| name | Peptide, protein, and gene identifier |
| score | BED score scaled from peptide probability where available |
| strand | Genomic strand |

---

### BED12

BED12 provides a block-aware representation of peptide genomic coordinates.

This is particularly important for peptides spanning CDS junctions, because such peptides need to be displayed as multi-block genomic features.

| BED12 field | Description |
|---|---|
| chrom | Chromosome or genome sequence ID |
| chromStart | 0-based genomic start coordinate |
| chromEnd | 0-based exclusive genomic end coordinate |
| name | Peptide, protein, and gene identifier |
| score | BED score scaled from peptide probability where available |
| strand | Genomic strand |
| thickStart | Start of displayed feature |
| thickEnd | End of displayed feature |
| itemRgb | RGB colour field |
| blockCount | Number of genomic blocks |
| blockSizes | Comma-separated block sizes |
| blockStarts | Comma-separated block starts relative to chromStart |

---

## BED score

The BED score field was generated as follows:

```text
Probability × 1000
```

where peptide probability was available.

If no probability column was present, a default score of `1000` was assigned.

---

## Output files

BED files were exported into:

```text
python_outputs/bed/
```

### Example BED6 output

```text
FragPipe_Duncan_PXD004720_anther_peptides.bed6
```

### Example BED12 output

```text
FragPipe_Duncan_PXD004720_anther_peptides.bed12
```

---

## Summary metrics

A Step 10 summary table was generated across all tissues.

### Metrics captured

| Metric | Description |
|---|---|
| BED_rows | Number of peptide genomic features exported |
| Unique_BED_peptides | Number of unique peptide sequences exported |
| Unique_BED_proteins | Number of unique protein accessions represented |
| Unique_BED_gene_models | Number of unique gene models represented |
| Multi_block_peptides | Number of peptide features spanning more than one genomic block |

### Output summary file

```text
wheat_bed_export_summary_step11.csv
```

The resulting BED6 and BED12 files can be loaded into JBrowse to visualise peptide evidence aligned to the wheat genome.


```python
# ============================================================
# Step 11 — Export BED6 and BED12 files for JBrowse (takes 15 min)
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
bed_dir = Path("python_outputs/bed")

bed_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
step11_summary_out = tables_dir / "wheat_bed_export_summary_step11.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 2. Helper functions
# -----------------------------
def make_bed_score(data):
    """
    Create BED score between 0 and 1000.

    Priority:
    1. Probability column scaled to 0–1000
    2. Default score = 1000
    """

    if "Probability" in data.columns:
        score = pd.to_numeric(
            data["Probability"],
            errors="coerce"
        ) * 1000

        score = (
            score
            .fillna(1000)
            .clip(0, 1000)
            .round()
            .astype(int)
        )

    else:
        score = pd.Series([1000] * len(data), index=data.index)

    return score


def clean_bed_name(value):
    """
    Clean BED name field for BED/JBrowse compatibility.
    """

    return (
        str(value)
        .replace(" ", "_")
        .replace(";", "|")
        .replace(",", "|")
        .replace("\t", "_")
        .replace("\n", "_")
    )


def build_bed_name(projected):
    """
    Build informative BED label.

    Priority:
    1. Peptide_intron_gapped
    2. Peptide

    Final structure:
    peptide|protein|gene|tissues=X
    """

    if "Peptide_intron_gapped" in projected.columns:
        peptide_label = projected["Peptide_intron_gapped_compact"].astype(str)
    else:
        peptide_label = projected["Peptide"].astype(str)

    if "GeneID" in projected.columns:

        bed_name = (
            peptide_label + "|" +
            projected["ProteinID"].astype(str) + "|" +
            projected["GeneID"].astype(str)
        )

    else:

        bed_name = (
            peptide_label + "|" +
            projected["ProteinID"].astype(str)
        )

    # Add tissue count if present
    if "Tissues_count" in projected.columns:
        bed_name = (
            bed_name +
            "|tissues=" +
            projected["Tissues_count"].astype(str)
        )

    return bed_name.apply(clean_bed_name)


# -----------------------------
# 3. Export BED files
# -----------------------------
def export_bed_files_for_tissue(source, tissue_raw_code):

    match = manifest[
        (manifest["Source"] == source) &
        (manifest["Tissue-Raw-Code"] == tissue_raw_code)
    ]

    if match.empty:
        raise ValueError(
            f"No manifest entry found for {source} | {tissue_raw_code}"
        )

    row = match.iloc[0]

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        raise FileNotFoundError(
            f"Step 9 projection file not found: {projection_path}"
        )

    data = pd.read_csv(
        projection_path,
        low_memory=False
    )

    projected = data[
        data["Projection_status"] == "projected"
    ].copy()

    required_cols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "ProteinID",
        "Strand",
        "BED_block_count",
        "BED_block_sizes",
        "BED_block_starts"
    ]

    missing_cols = [
        col for col in required_cols
        if col not in projected.columns
    ]

    if missing_cols:
        raise KeyError(
            f"Missing required BED column(s): {missing_cols}"
        )

    # -----------------------------
    # Create BED score
    # -----------------------------
    projected["BED_score"] = make_bed_score(projected)

    # -----------------------------
    # Create BED label
    # -----------------------------
    projected["BED_name"] = build_bed_name(projected)

    # -----------------------------
    # Force integer coordinate types
    # -----------------------------
    projected["BED_start_0based"] = (
        projected["BED_start_0based"]
        .astype(int)
    )

    projected["BED_end_0based_exclusive"] = (
        projected["BED_end_0based_exclusive"]
        .astype(int)
    )

    projected["BED_block_count"] = (
        projected["BED_block_count"]
        .astype(int)
    )

    # -----------------------------
    # BED6 export
    # -----------------------------
    bed6 = projected[[
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_name",
        "BED_score",
        "Strand"
    ]].copy()

    bed6_filename = projection_filename.replace(
        "_peptide_genome_projection.csv",
        "_peptides.bed6"
    )

    bed6_path = bed_dir / bed6_filename

    bed6.to_csv(
        bed6_path,
        sep="\t",
        header=False,
        index=False
    )

    # -----------------------------
    # BED12 export
    # -----------------------------
    bed12 = pd.DataFrame({

        "chrom":
            projected["Chromosome"],

        "chromStart":
            projected["BED_start_0based"],

        "chromEnd":
            projected["BED_end_0based_exclusive"],

        "name":
            projected["BED_name"],

        "score":
            projected["BED_score"],

        "strand":
            projected["Strand"],

        "thickStart":
            projected["BED_start_0based"],

        "thickEnd":
            projected["BED_end_0based_exclusive"],

        "itemRgb":
            "0",

        "blockCount":
            projected["BED_block_count"],

        "blockSizes":
            projected["BED_block_sizes"],

        "blockStarts":
            projected["BED_block_starts"]

    })

    bed12_filename = projection_filename.replace(
        "_peptide_genome_projection.csv",
        "_peptides.bed12"
    )

    bed12_path = bed_dir / bed12_filename

    bed12.to_csv(
        bed12_path,
        sep="\t",
        header=False,
        index=False
    )

    print(f"\nSaved BED6:  {bed6_path}")
    print(f"Saved BED12: {bed12_path}")
    print(f"BED rows: {len(projected):,}")

    # -----------------------------
    # Summary metrics
    # -----------------------------
    multi_block_count = (
        projected["BED_block_count"] > 1
    ).sum()

    intron_gapped_count = (
        projected["BED_name"]
        .astype(str)
        .str.contains("-", regex=False)
    ).sum()

    return {

        "Source":
            source,

        "Species":
            row["Species"],

        "Tissue":
            tissue_raw_code,

        "Batch":
            row["Batch"],

        "Projection_file":
            projection_filename,

        "BED6_file":
            bed6_filename,

        "BED12_file":
            bed12_filename,

        "BED_rows":
            len(projected),

        "Unique_BED_peptides":
            projected["Peptide"].nunique(),

        "Unique_BED_proteins":
            projected["ProteinID"].nunique(),

        "Unique_BED_gene_models":
            projected["GeneID"].nunique()
            if "GeneID" in projected.columns
            else pd.NA,

        "Multi_block_peptides":
            multi_block_count,

        "BED_labels_with_introns":
            intron_gapped_count
    }


# -----------------------------
# 4. Run Step 11 for all tissues
# -----------------------------
step11_summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    tissue_raw_code = row["Tissue-Raw-Code"]

    print(f"\nProcessing {source} | {tissue_raw_code}")

    summary_record = export_bed_files_for_tissue(
        source=source,
        tissue_raw_code=tissue_raw_code
    )

    step11_summary_records.append(summary_record)

step11_summary = pd.DataFrame(step11_summary_records)

step11_summary.to_csv(
    step11_summary_out,
    index=False
)

print(f"\nStep 11 summary saved: {step11_summary_out}")
print(f"Summary rows: {step11_summary.shape[0]:,}")

display(step11_summary)
```

    
    Processing MSV000090572 | stored_grain
    
    Saved BED6:  python_outputs\bed\FragPipe_Vincent_MSV000090572_stored-grain_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Vincent_MSV000090572_stored-grain_peptides.bed12
    BED rows: 30,314
    
    Processing PXD050500 | coleoptile
    
    Saved BED6:  python_outputs\bed\FragPipe_Liu_PXD050500_coleoptile_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Liu_PXD050500_coleoptile_peptides.bed12
    BED rows: 1,850,136
    
    Processing PXD050500 | node
    
    Saved BED6:  python_outputs\bed\FragPipe_Liu_PXD050500_node_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Liu_PXD050500_node_peptides.bed12
    BED rows: 1,886,922
    
    Processing PXD050500 | radicle
    
    Saved BED6:  python_outputs\bed\FragPipe_Liu_PXD050500_radicle_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Liu_PXD050500_radicle_peptides.bed12
    BED rows: 1,062,508
    
    Processing PXD004720 | anther
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_anther_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_anther_peptides.bed12
    BED rows: 164,365
    
    Processing PXD004720 | boot
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_boot_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_boot_peptides.bed12
    BED rows: 13,227
    
    Processing PXD004720 | coleoptile
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_coleoptile_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_coleoptile_peptides.bed12
    BED rows: 204,476
    
    Processing PXD004720 | embryo
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_embryo_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_embryo_peptides.bed12
    BED rows: 8,852
    
    Processing PXD004720 | endosperm
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_endosperm_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_endosperm_peptides.bed12
    BED rows: 102,830
    
    Processing PXD004720 | glume
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_glume_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_glume_peptides.bed12
    BED rows: 145,133
    
    Processing PXD004720 | grain-zadoks-70
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-70_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-70_peptides.bed12
    BED rows: 126,195
    
    Processing PXD004720 | grain-zadoks-71
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-71_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-71_peptides.bed12
    BED rows: 179,725
    
    Processing PXD004720 | grain-zadoks-75
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-75_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-75_peptides.bed12
    BED rows: 132,701
    
    Processing PXD004720 | grain-zadoks-83
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-83_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-83_peptides.bed12
    BED rows: 113,203
    
    Processing PXD004720 | grain-zadoks-87
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-87_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_grain-zadoks-87_peptides.bed12
    BED rows: 111,792
    
    Processing PXD004720 | leaf-flag-mature
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_leaf-flag-mature_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_leaf-flag-mature_peptides.bed12
    BED rows: 145,632
    
    Processing PXD004720 | leaf-flag-senescing
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptides.bed12
    BED rows: 46,200
    
    Processing PXD004720 | leaf-flag-young
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_leaf-flag-young_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_leaf-flag-young_peptides.bed12
    BED rows: 120,821
    
    Processing PXD004720 | lemma
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_lemma_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_lemma_peptides.bed12
    BED rows: 147,618
    
    Processing PXD004720 | node
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_node_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_node_peptides.bed12
    BED rows: 99,823
    
    Processing PXD004720 | node_secretion
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_node-secretion_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_node-secretion_peptides.bed12
    BED rows: 169,675
    
    Processing PXD004720 | palea
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_palea_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_palea_peptides.bed12
    BED rows: 116,936
    
    Processing PXD004720 | pericarp
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_pericarp_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_pericarp_peptides.bed12
    BED rows: 131,215
    
    Processing PXD004720 | pollen
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_pollen_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_pollen_peptides.bed12
    BED rows: 74,698
    
    Processing PXD004720 | rachilla
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_rachilla_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_rachilla_peptides.bed12
    BED rows: 160,204
    
    Processing PXD004720 | radicle
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_radicle_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_radicle_peptides.bed12
    BED rows: 194,694
    
    Processing PXD004720 | root-mature
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_root-mature_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_root-mature_peptides.bed12
    BED rows: 97,188
    
    Processing PXD004720 | root-secretion
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_root-secretion_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_root-secretion_peptides.bed12
    BED rows: 100,639
    
    Processing PXD004720 | root-tip
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_root-tip_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_root-tip_peptides.bed12
    BED rows: 191,943
    
    Processing PXD004720 | root-vasculature
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_root-vasculature_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_root-vasculature_peptides.bed12
    BED rows: 111,831
    
    Processing PXD004720 | spike-immature
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_spike-immature_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_spike-immature_peptides.bed12
    BED rows: 188,826
    
    Processing PXD004720 | stem
    
    Saved BED6:  python_outputs\bed\FragPipe_Duncan_PXD004720_stem_peptides.bed6
    Saved BED12: python_outputs\bed\FragPipe_Duncan_PXD004720_stem_peptides.bed12
    BED rows: 60,734
    
    Step 11 summary saved: python_outputs\tables\wheat_bed_export_summary_step11.csv
    Summary rows: 32
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Projection_file</th>
      <th>BED6_file</th>
      <th>BED12_file</th>
      <th>BED_rows</th>
      <th>Unique_BED_peptides</th>
      <th>Unique_BED_proteins</th>
      <th>Unique_BED_gene_models</th>
      <th>Multi_block_peptides</th>
      <th>BED_labels_with_introns</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>30314</td>
      <td>9329</td>
      <td>17478</td>
      <td>&lt;NA&gt;</td>
      <td>3291</td>
      <td>1828</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptides.bed6</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptides.bed12</td>
      <td>1850136</td>
      <td>582775</td>
      <td>239461</td>
      <td>&lt;NA&gt;</td>
      <td>228372</td>
      <td>122385</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>FragPipe_Liu_PXD050500_node_peptides.bed6</td>
      <td>FragPipe_Liu_PXD050500_node_peptides.bed12</td>
      <td>1886922</td>
      <td>595954</td>
      <td>242813</td>
      <td>&lt;NA&gt;</td>
      <td>235642</td>
      <td>127047</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptides.bed6</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptides.bed12</td>
      <td>1062508</td>
      <td>333058</td>
      <td>206016</td>
      <td>&lt;NA&gt;</td>
      <td>118195</td>
      <td>62337</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptides.bed12</td>
      <td>164365</td>
      <td>34098</td>
      <td>36826</td>
      <td>&lt;NA&gt;</td>
      <td>27776</td>
      <td>16150</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptides.bed12</td>
      <td>13227</td>
      <td>3643</td>
      <td>9208</td>
      <td>&lt;NA&gt;</td>
      <td>2728</td>
      <td>1537</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptides....</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptides....</td>
      <td>204476</td>
      <td>41025</td>
      <td>46496</td>
      <td>&lt;NA&gt;</td>
      <td>31344</td>
      <td>18679</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptides.bed12</td>
      <td>8852</td>
      <td>2867</td>
      <td>7220</td>
      <td>&lt;NA&gt;</td>
      <td>1411</td>
      <td>760</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptides.b...</td>
      <td>102830</td>
      <td>20081</td>
      <td>27454</td>
      <td>&lt;NA&gt;</td>
      <td>14269</td>
      <td>7971</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptides.bed12</td>
      <td>145133</td>
      <td>28648</td>
      <td>35540</td>
      <td>&lt;NA&gt;</td>
      <td>22131</td>
      <td>12759</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>126195</td>
      <td>26196</td>
      <td>35532</td>
      <td>&lt;NA&gt;</td>
      <td>17478</td>
      <td>9892</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>179725</td>
      <td>35960</td>
      <td>47076</td>
      <td>&lt;NA&gt;</td>
      <td>27658</td>
      <td>15967</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>132701</td>
      <td>27463</td>
      <td>41029</td>
      <td>&lt;NA&gt;</td>
      <td>18650</td>
      <td>10504</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>113203</td>
      <td>23990</td>
      <td>36635</td>
      <td>&lt;NA&gt;</td>
      <td>14734</td>
      <td>8452</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>111792</td>
      <td>24636</td>
      <td>34874</td>
      <td>&lt;NA&gt;</td>
      <td>14886</td>
      <td>8402</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>145632</td>
      <td>29840</td>
      <td>37954</td>
      <td>&lt;NA&gt;</td>
      <td>19448</td>
      <td>11285</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>46200</td>
      <td>11354</td>
      <td>25696</td>
      <td>&lt;NA&gt;</td>
      <td>4572</td>
      <td>2415</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>120821</td>
      <td>23373</td>
      <td>32620</td>
      <td>&lt;NA&gt;</td>
      <td>15227</td>
      <td>8981</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptides.bed12</td>
      <td>147618</td>
      <td>29788</td>
      <td>37927</td>
      <td>&lt;NA&gt;</td>
      <td>21753</td>
      <td>12440</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
      <td>FragPipe_Duncan_PXD004720_node_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_node_peptides.bed12</td>
      <td>99823</td>
      <td>21457</td>
      <td>36542</td>
      <td>&lt;NA&gt;</td>
      <td>12765</td>
      <td>7108</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>169675</td>
      <td>34124</td>
      <td>42356</td>
      <td>&lt;NA&gt;</td>
      <td>22888</td>
      <td>13292</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptides.bed12</td>
      <td>116936</td>
      <td>21707</td>
      <td>27580</td>
      <td>&lt;NA&gt;</td>
      <td>20681</td>
      <td>12105</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptides.bed12</td>
      <td>131215</td>
      <td>28332</td>
      <td>32667</td>
      <td>&lt;NA&gt;</td>
      <td>20964</td>
      <td>11953</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptides.bed12</td>
      <td>74698</td>
      <td>13502</td>
      <td>19931</td>
      <td>&lt;NA&gt;</td>
      <td>9490</td>
      <td>5338</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_gen...</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptides.bed12</td>
      <td>160204</td>
      <td>31145</td>
      <td>37204</td>
      <td>&lt;NA&gt;</td>
      <td>24784</td>
      <td>14463</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_geno...</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptides.bed12</td>
      <td>194694</td>
      <td>39643</td>
      <td>42965</td>
      <td>&lt;NA&gt;</td>
      <td>32499</td>
      <td>19061</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptides...</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptides...</td>
      <td>97188</td>
      <td>21350</td>
      <td>39156</td>
      <td>&lt;NA&gt;</td>
      <td>10898</td>
      <td>6135</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>100639</td>
      <td>21284</td>
      <td>32046</td>
      <td>&lt;NA&gt;</td>
      <td>15547</td>
      <td>8991</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_gen...</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptides.bed12</td>
      <td>191943</td>
      <td>38634</td>
      <td>39774</td>
      <td>&lt;NA&gt;</td>
      <td>35031</td>
      <td>21057</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>111831</td>
      <td>20815</td>
      <td>30626</td>
      <td>&lt;NA&gt;</td>
      <td>14833</td>
      <td>8183</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>188826</td>
      <td>36370</td>
      <td>40207</td>
      <td>&lt;NA&gt;</td>
      <td>33193</td>
      <td>19376</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptides.bed6</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptides.bed12</td>
      <td>60734</td>
      <td>14338</td>
      <td>29410</td>
      <td>&lt;NA&gt;</td>
      <td>6949</td>
      <td>3980</td>
    </tr>
  </tbody>
</table>
</div>


# Step 12 — Create a Non-Redundant Combined Peptide BED Track

This step generates a single non-redundant genome browser track containing all successfully projected wheat peptides across all tissues.

The purpose of this combined track is to improve the user experience in Apollo/JBrowse by allowing users to display all peptide evidence at once, without needing to manually activate each individual tissue track.

---

## Input files

### Peptide genome projection tables from Step 9

One file per tissue:

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only successfully projected rows were retained.

### Filtering rule

```text
Projection_status == "projected"
```

---

## Redundancy removal strategy

This step does not simply concatenate all tissue-level BED files.

Instead, redundancy was removed at the peptide–protein–genome feature level.

A feature was considered redundant when it had the same:

```text
Chromosome
BED_start_0based
BED_end_0based_exclusive
Strand
Peptide
ProteinID
GeneID
BED_block_count
BED_block_sizes
BED_block_starts
```

This means that the same peptide/protein/genomic feature detected in multiple tissues is represented only once in the combined BED track.

---

## Tissue support retention

Although redundant features were collapsed, tissue-level evidence was retained in the combined output table.

The following support metrics were added:

| Metric | Description |
|---|---|
| Sources | Proteomics source datasets in which the feature was observed |
| Tissues | Wheat tissues in which the feature was observed |
| Tissue_count | Number of tissues supporting the feature |
| Observation_count | Number of tissue-level observations collapsed into the feature |
| Max_BED_score | Maximum BED score observed for the feature |

---

## Output files

### Combined non-redundant evidence table

```text
wheat_all_tissues_nonredundant_projected_peptides.csv
```

### Combined BED6 file

```text
wheat_all_tissues_nonredundant_projected_peptides.bed6
```

### Combined BED12 file

```text
wheat_all_tissues_nonredundant_projected_peptides.bed12
```

### Output directories

```text
python_outputs/tables/
python_outputs/bed/
```

---

## Summary metrics

A Step 12 summary table was generated.

### Metrics captured

| Metric | Description |
|---|---|
| Total_projected_rows_before_deduplication | Number of projected rows across all tissue-level files |
| Nonredundant_projected_rows | Number of unique peptide/protein/genome features retained |
| Redundant_rows_removed | Number of redundant tissue-level observations collapsed |
| Unique_peptides | Number of unique peptide sequences |
| Unique_proteins | Number of unique protein accessions |
| Unique_gene_models | Number of unique gene models |
| Unique_chromosomes | Number of chromosomes or genomic sequences represented |
| Multi_block_peptides | Number of features spanning more than one genomic block |

### Output summary file

```text
wheat_combined_bed_summary_step12.csv
```

The resulting combined BED files provide a user-friendly genome-wide peptide evidence track for Apollo/JBrowse visualisation.


```python
# ============================================================
# Step 12 — Create non-redundant combined BED tracks (takes 20 min)
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
bed_dir = Path("python_outputs/bed")

bed_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

combined_table_out = tables_dir / "wheat_all_tissues_nonredundant_projected_peptides.csv"
combined_bed6_out = bed_dir / "wheat_all_tissues_nonredundant_projected_peptides.bed6"
combined_bed12_out = bed_dir / "wheat_all_tissues_nonredundant_projected_peptides.bed12"
step12_summary_out = tables_dir / "wheat_combined_bed_summary_step12.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 2. Helper functions
# -----------------------------
def make_bed_score(data):
    if "Probability" in data.columns:
        score = pd.to_numeric(data["Probability"], errors="coerce") * 1000
        score = score.fillna(1000).clip(0, 1000).round().astype(int)
    else:
        score = pd.Series([1000] * len(data), index=data.index)

    return score


def clean_bed_name(value):
    return (
        str(value)
        .replace(" ", "_")
        .replace(";", "|")
        .replace(",", "|")
        .replace("\t", "_")
        .replace("\n", "_")
    )


def collapse_unique_values(values):
    values = sorted(set(str(v) for v in values if pd.notna(v)))
    return "|".join(values)


# -----------------------------
# 3. Load all projected peptide tables
# -----------------------------
all_projected_tables = []

for _, row in manifest.iterrows():

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Warning: missing projection file, skipped: {projection_path}")
        continue

    data = pd.read_csv(projection_path, low_memory=False)

    data = data[data["Projection_status"] == "projected"].copy()

    data["Source"] = row["Source"]
    data["Species"] = row["Species"]
    data["Tissue"] = row["Tissue-Raw-Code"]
    data["Batch"] = row["Batch"]

    # Fallback for older Step 9 outputs
    if "Peptide_intron_gapped" not in data.columns:
        data["Peptide_intron_gapped"] = data["Peptide"].astype(str)

    all_projected_tables.append(data)

if not all_projected_tables:
    raise ValueError("No projected peptide tables were loaded. Please check Step 9 outputs.")

all_projected = pd.concat(all_projected_tables, ignore_index=True)

print(f"Total projected rows before redundancy removal: {len(all_projected):,}")


# -----------------------------
# 4. Define non-redundant peptide/protein/genome feature
# -----------------------------
dedup_cols = [
    "Chromosome",
    "BED_start_0based",
    "BED_end_0based_exclusive",
    "Strand",
    "Peptide",
    "Peptide_intron_gapped_compact",
    "ProteinID",
    "GeneModel",
    "BED_block_count",
    "BED_block_sizes",
    "BED_block_starts"
]

missing_cols = [col for col in dedup_cols if col not in all_projected.columns]

if missing_cols:
    raise KeyError(f"Missing required column(s): {missing_cols}")

all_projected["BED_score"] = make_bed_score(all_projected)


# -----------------------------
# 5. Collapse redundant tissue-level observations
# -----------------------------
agg_dict = {
    "Sources": ("Source", collapse_unique_values),
    "Tissues": ("Tissue", collapse_unique_values),
    "Tissue_count": ("Tissue", lambda x: len(set(x))),
    "Observation_count": ("Peptide", "size"),
    "Max_BED_score": ("BED_score", "max")
}

if "Probability" in all_projected.columns:
    agg_dict["Max_probability"] = ("Probability", "max")
else:
    agg_dict["Max_probability"] = ("BED_score", "max")

nonredundant = (
    all_projected
    .groupby(dedup_cols, dropna=False)
    .agg(**agg_dict)
    .reset_index()
)

nonredundant.insert(0, "Index", range(1, len(nonredundant) + 1))

print(f"Non-redundant projected peptide/protein/genome rows: {len(nonredundant):,}")


# -----------------------------
# 6. Create BED names with intron-gapped peptide labels
# -----------------------------
nonredundant["BED_name"] = (
    nonredundant["Peptide_intron_gapped_compact"].astype(str) + "|" +
    nonredundant["ProteinID"].astype(str) + "|" +
    nonredundant["GeneModel"].astype(str) + "|" +
    "tissues=" + nonredundant["Tissue_count"].astype(str)
)

nonredundant["BED_name"] = nonredundant["BED_name"].apply(clean_bed_name)

nonredundant["BED_start_0based"] = nonredundant["BED_start_0based"].astype(int)
nonredundant["BED_end_0based_exclusive"] = nonredundant["BED_end_0based_exclusive"].astype(int)
nonredundant["BED_block_count"] = nonredundant["BED_block_count"].astype(int)
nonredundant["Max_BED_score"] = nonredundant["Max_BED_score"].astype(int)

# Save combined non-redundant table
nonredundant.to_csv(combined_table_out, index=False)


# -----------------------------
# 7. Export combined BED6
# -----------------------------
bed6 = nonredundant[[
    "Chromosome",
    "BED_start_0based",
    "BED_end_0based_exclusive",
    "BED_name",
    "Max_BED_score",
    "Strand"
]].copy()

bed6.to_csv(
    combined_bed6_out,
    sep="\t",
    header=False,
    index=False
)


# -----------------------------
# 8. Export combined BED12
# -----------------------------
bed12 = pd.DataFrame({
    "chrom": nonredundant["Chromosome"],
    "chromStart": nonredundant["BED_start_0based"],
    "chromEnd": nonredundant["BED_end_0based_exclusive"],
    "name": nonredundant["BED_name"],
    "score": nonredundant["Max_BED_score"],
    "strand": nonredundant["Strand"],
    "thickStart": nonredundant["BED_start_0based"],
    "thickEnd": nonredundant["BED_end_0based_exclusive"],
    "itemRgb": "0",
    "blockCount": nonredundant["BED_block_count"],
    "blockSizes": nonredundant["BED_block_sizes"],
    "blockStarts": nonredundant["BED_block_starts"]
})

bed12.to_csv(
    combined_bed12_out,
    sep="\t",
    header=False,
    index=False
)


# -----------------------------
# 9. Summary table
# -----------------------------
step12_summary = pd.DataFrame([{
    "Total_projected_rows_before_deduplication": len(all_projected),
    "Nonredundant_projected_rows": len(nonredundant),
    "Redundant_rows_removed": len(all_projected) - len(nonredundant),
    "Unique_peptides": nonredundant["Peptide"].nunique(),
    "Unique_proteins": nonredundant["ProteinID"].nunique(),
    "Unique_gene_models": nonredundant["GeneModel"].nunique(),
    "Unique_chromosomes": nonredundant["Chromosome"].nunique(),
    "Multi_block_peptides": (nonredundant["BED_block_count"] > 1).sum(),
    "BED_labels_with_introns": nonredundant["BED_name"].astype(str).str.contains("-", regex=False).sum(),
    "BED6_file": combined_bed6_out.name,
    "BED12_file": combined_bed12_out.name
}])

step12_summary.to_csv(step12_summary_out, index=False)

print(f"\nCombined non-redundant table saved: {combined_table_out}")
print(f"Combined BED6 saved: {combined_bed6_out}")
print(f"Combined BED12 saved: {combined_bed12_out}")
print(f"Step 12 summary saved: {step12_summary_out}")

display(step12_summary)
```

    Total projected rows before redundancy removal: 8,291,056
    Non-redundant projected peptide/protein/genome rows: 3,224,488
    
    Combined non-redundant table saved: python_outputs\tables\wheat_all_tissues_nonredundant_projected_peptides.csv
    Combined BED6 saved: python_outputs\bed\wheat_all_tissues_nonredundant_projected_peptides.bed6
    Combined BED12 saved: python_outputs\bed\wheat_all_tissues_nonredundant_projected_peptides.bed12
    Step 12 summary saved: python_outputs\tables\wheat_combined_bed_summary_step12.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total_projected_rows_before_deduplication</th>
      <th>Nonredundant_projected_rows</th>
      <th>Redundant_rows_removed</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins</th>
      <th>Unique_gene_models</th>
      <th>Unique_chromosomes</th>
      <th>Multi_block_peptides</th>
      <th>BED_labels_with_introns</th>
      <th>BED6_file</th>
      <th>BED12_file</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8291056</td>
      <td>3224488</td>
      <td>5066568</td>
      <td>1115869</td>
      <td>277852</td>
      <td>249082</td>
      <td>22</td>
      <td>367521</td>
      <td>195832</td>
      <td>wheat_all_tissues_nonredundant_projected_pepti...</td>
      <td>wheat_all_tissues_nonredundant_projected_pepti...</td>
    </tr>
  </tbody>
</table>
</div>



```python
# checking dashed peptide annotations
display(
    nonredundant[
        nonredundant["BED_name"].astype(str).str.contains("-", regex=False)
    ][["Peptide", "Peptide_intron_gapped_compact", "BED_name", "BED_block_count"]].head(20)
)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Peptide</th>
      <th>Peptide_intron_gapped_compact</th>
      <th>BED_name</th>
      <th>BED_block_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18</th>
      <td>MVGVLALSTQCIR</td>
      <td>MVGVLALSTQ----------CIR</td>
      <td>MVGVLALSTQ----------CIR|TraesCS1A03G0000500LC....</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>MVGVLALSTQCIRRAAGMMASK</td>
      <td>MVGVLALSTQ----------CIRRAAGMMASK</td>
      <td>MVGVLALSTQ----------CIRRAAGMMASK|TraesCS1A03G0...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>294</th>
      <td>SSGTKALEMLQHAEQK</td>
      <td>SSGTK----------ALEMLQHAEQK</td>
      <td>SSGTK----------ALEMLQHAEQK|TraesCS1A03G0004200...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>295</th>
      <td>SSGTKALEMLQHAEQK</td>
      <td>SSGTK----------ALEMLQHAEQK</td>
      <td>SSGTK----------ALEMLQHAEQK|TraesCS1A03G0004200...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>296</th>
      <td>SYVEQTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR|TraesCS1A03G0004200.10...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>297</th>
      <td>SYVEQTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR|TraesCS1A03G0004200.3|...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>298</th>
      <td>SYVEQTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR|TraesCS1A03G0004200.4|...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>299</th>
      <td>SYVEQTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR|TraesCS1A03G0004200.6|...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>300</th>
      <td>SYVEQTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR|TraesCS1A03G0004200.7|...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>301</th>
      <td>SYVEQTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR</td>
      <td>SYVE----------QTVQRGDNR|TraesCS1A03G0004200.8|...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>302</th>
      <td>SYVEQTVQR</td>
      <td>SYVE----------QTVQR</td>
      <td>SYVE----------QTVQR|TraesCS1A03G0004200.10|Tra...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>303</th>
      <td>SYVEQTVQR</td>
      <td>SYVE----------QTVQR</td>
      <td>SYVE----------QTVQR|TraesCS1A03G0004200.3|Trae...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>304</th>
      <td>SYVEQTVQR</td>
      <td>SYVE----------QTVQR</td>
      <td>SYVE----------QTVQR|TraesCS1A03G0004200.4|Trae...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>305</th>
      <td>SYVEQTVQR</td>
      <td>SYVE----------QTVQR</td>
      <td>SYVE----------QTVQR|TraesCS1A03G0004200.6|Trae...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>306</th>
      <td>SYVEQTVQR</td>
      <td>SYVE----------QTVQR</td>
      <td>SYVE----------QTVQR|TraesCS1A03G0004200.7|Trae...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>307</th>
      <td>SYVEQTVQR</td>
      <td>SYVE----------QTVQR</td>
      <td>SYVE----------QTVQR|TraesCS1A03G0004200.8|Trae...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>308</th>
      <td>SYVETVQR</td>
      <td>SYVE----------TVQR</td>
      <td>SYVE----------TVQR|TraesCS1A03G0004200.1|Traes...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>309</th>
      <td>SYVETVQR</td>
      <td>SYVE----------TVQR</td>
      <td>SYVE----------TVQR|TraesCS1A03G0004200.2|Traes...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>310</th>
      <td>SYVETVQR</td>
      <td>SYVE----------TVQR</td>
      <td>SYVE----------TVQR|TraesCS1A03G0004200.5|Traes...</td>
      <td>2</td>
    </tr>
    <tr>
      <th>311</th>
      <td>SYVETVQR</td>
      <td>SYVE----------TVQR</td>
      <td>SYVE----------TVQR|TraesCS1A03G0004200.9|Traes...</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>


# Step 13 — Generate Tissue, Protein, Gene, and Isoform Summary Tables

This step generates publication-ready summary tables describing peptide evidence across wheat tissues, protein isoforms, and gene models.

The summaries are based on successfully projected peptide evidence from Step 9 and use the GFF3-derived protein-to-gene mapping table from Step 5 to distinguish high-confidence (HC) and low-confidence (LC) gene models.

---

## Input files

### Peptide genome projection tables from Step 9

One file per tissue:

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only successfully projected peptide rows were included.

### Filtering rule

```text
Projection_status == "projected"
```

### Protein-to-gene mapping table from Step 5

```text
wheat_protein_gene_mapping_HC_LC.csv
```

This table provides the full set of wheat protein isoforms, gene models, and annotation-confidence categories used as denominators for percentage calculations.

---

## Genome annotation denominators

The following global annotation counts were calculated from the GFF3-derived protein-to-gene mapping table:

| Denominator | Description |
|---|---|
| Total gene models | Number of unique HC + LC wheat gene models |
| HC gene models | Number of high-confidence wheat gene models |
| LC gene models | Number of low-confidence wheat gene models |
| Protein isoforms | Number of unique annotated protein accessions |

These values were used to express proteomics coverage as a percentage of the annotated wheat gene model space.

---

## Summary tables generated

### 1. Tissue-level summary

One row per tissue.

```text
wheat_tissue_level_summary_step13.csv
```

Main metrics include:

| Metric | Description |
|---|---|
| Projected_peptide_rows | Number of projected peptide evidence rows |
| Unique_peptides | Number of unique peptide sequences |
| Unique_proteins_isoforms | Number of unique protein isoforms |
| Unique_gene_models | Number of unique gene models detected |
| Unique_HC_gene_models | Number of detected HC gene models |
| Unique_LC_gene_models | Number of detected LC gene models |
| Percent_total_gene_models_detected | Percentage of all annotated gene models detected |
| Percent_HC_gene_models_detected | Percentage of HC gene models detected |
| Percent_LC_gene_models_detected | Percentage of LC gene models detected |
| Multi_block_peptide_rows | Number of peptide rows spanning more than one CDS block |
| Proteins_supported_by_one_peptide | Number of protein isoforms supported by one unique peptide |
| Proteins_supported_by_two_or_more_peptides | Number of protein isoforms supported by at least two unique peptides |
| Genes_supported_by_one_peptide | Number of gene models supported by one unique peptide |
| Genes_supported_by_two_or_more_peptides | Number of gene models supported by at least two unique peptides |

---

### 2. Gene model summary

One row per detected gene model.

```text
wheat_gene_model_summary_step13.csv
```

This table captures the number of peptides, protein isoforms, tissues, and sources supporting each gene model.

---

### 3. Protein / isoform summary

One row per detected protein isoform.

```text
wheat_protein_isoform_summary_step12.csv
```

This table captures the number of peptides, tissues, and sources supporting each protein isoform.

---

### 4. Source-level summary

One row per public proteomics repository/source.

```text
wheat_source_level_summary_step13.csv
```

This table summarises proteomics coverage at the dataset level and reports the proportion of total, HC, and LC gene models detected from each source.

---

## Purpose

These summary tables provide a high-level overview of proteomics evidence across tissues and public datasets.

They also quantify the extent to which the identified peptides support:

```text
protein isoforms
gene models
HC annotations
LC annotations
multi-tissue evidence
```

These outputs are intended for downstream reporting, manuscript tables, supplementary files, and global interpretation of wheat proteogenomic coverage.


```python
# ============================================================
# Step 13 — Tissue, protein, gene, and isoform summary tables (takes 15 min)
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

tissue_summary_out = tables_dir / "wheat_tissue_level_summary_step13.csv"
gene_summary_out = tables_dir / "wheat_gene_model_summary_step13.csv"
protein_summary_out = tables_dir / "wheat_protein_isoform_summary_step13.csv"
source_summary_out = tables_dir / "wheat_source_level_summary_step13.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")
protein_gene_mapping = pd.read_csv(protein_gene_mapping_file, low_memory=False)

# -----------------------------
# 2. Detect key columns
# -----------------------------
gene_col = "GeneModel" if "GeneModel" in protein_gene_mapping.columns else "GeneID"
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

required_mapping_cols = [gene_col, protein_col, confidence_col]
missing = [col for col in required_mapping_cols if col not in protein_gene_mapping.columns]

if missing:
    raise KeyError(f"Missing required column(s) in protein-gene mapping table: {missing}")

# -----------------------------
# 3. Genome annotation denominators
# -----------------------------
all_gene_models = protein_gene_mapping[[gene_col, confidence_col]].drop_duplicates()

total_gene_models = all_gene_models[gene_col].nunique()
total_hc_gene_models = all_gene_models.loc[
    all_gene_models[confidence_col].astype(str).str.upper() == "HC", gene_col
].nunique()
total_lc_gene_models = all_gene_models.loc[
    all_gene_models[confidence_col].astype(str).str.upper() == "LC", gene_col
].nunique()

total_proteins = protein_gene_mapping[protein_col].nunique()

print("Genome annotation denominators")
print(f"Total gene models: {total_gene_models:,}")
print(f"HC gene models: {total_hc_gene_models:,}")
print(f"LC gene models: {total_lc_gene_models:,}")
print(f"Protein isoforms: {total_proteins:,}")


# -----------------------------
# 4. Load all projected peptide tables
# -----------------------------
all_projected_tables = []

for _, row in manifest.iterrows():

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Warning: missing projection file, skipped: {projection_path}")
        continue

    data = pd.read_csv(projection_path, low_memory=False)

    data = data[data["Projection_status"] == "projected"].copy()

    data["Source"] = row["Source"]
    data["Species"] = row["Species"]
    data["Tissue"] = row["Tissue-Raw-Code"]
    data["Batch"] = row["Batch"]

    all_projected_tables.append(data)

all_projected = pd.concat(all_projected_tables, ignore_index=True)

if gene_col not in all_projected.columns:
    raise KeyError(
        f"'{gene_col}' was found in the mapping table but not in Step 9 projection files. "
        "Please check the Step 8/9 merged column names."
    )

print(f"\nProjected peptide rows loaded: {len(all_projected):,}")


# -----------------------------
# 5. Helper percentage function
# -----------------------------
def pct(numerator, denominator):
    if denominator == 0 or pd.isna(denominator):
        return pd.NA
    return round((numerator / denominator) * 100, 4)


# -----------------------------
# 6. Tissue-level summary
# -----------------------------
tissue_records = []

for (source, species, tissue, batch), group in all_projected.groupby(
    ["Source", "Species", "Tissue", "Batch"],
    dropna=False
):

    hc = group[group[confidence_col].astype(str).str.upper() == "HC"]
    lc = group[group[confidence_col].astype(str).str.upper() == "LC"]

    unique_genes = group[gene_col].nunique()
    unique_hc_genes = hc[gene_col].nunique()
    unique_lc_genes = lc[gene_col].nunique()

    tissue_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue,
        "Batch": batch,
        "Projected_peptide_rows": len(group),
        "Unique_peptides": group["Peptide"].nunique(),
        "Unique_proteins_isoforms": group["ProteinID"].nunique(),
        "Unique_gene_models": unique_genes,
        "Unique_HC_gene_models": unique_hc_genes,
        "Unique_LC_gene_models": unique_lc_genes,
        "Percent_total_gene_models_detected": pct(unique_genes, total_gene_models),
        "Percent_HC_gene_models_detected": pct(unique_hc_genes, total_hc_gene_models),
        "Percent_LC_gene_models_detected": pct(unique_lc_genes, total_lc_gene_models),
        "Unique_chromosomes": group["Chromosome"].nunique(),
        "Multi_block_peptide_rows": (group["BED_block_count"] > 1).sum(),
        "Proteins_supported_by_one_peptide": (
            group.groupby("ProteinID")["Peptide"].nunique() == 1
        ).sum(),
        "Proteins_supported_by_two_or_more_peptides": (
            group.groupby("ProteinID")["Peptide"].nunique() >= 2
        ).sum(),
        "Genes_supported_by_one_peptide": (
            group.groupby(gene_col)["Peptide"].nunique() == 1
        ).sum(),
        "Genes_supported_by_two_or_more_peptides": (
            group.groupby(gene_col)["Peptide"].nunique() >= 2
        ).sum()
    })

tissue_summary = pd.DataFrame(tissue_records)
tissue_summary.to_csv(tissue_summary_out, index=False)


# -----------------------------
# 7. Gene model summary across all tissues
# -----------------------------
gene_summary = (
    all_projected
    .groupby([gene_col, confidence_col], dropna=False)
    .agg(
        Sources=("Source", lambda x: "|".join(sorted(set(map(str, x))))),
        Tissues=("Tissue", lambda x: "|".join(sorted(set(map(str, x))))),
        Tissue_count=("Tissue", lambda x: len(set(x))),
        Projected_peptide_rows=("Peptide", "size"),
        Unique_peptides=("Peptide", "nunique"),
        Unique_proteins_isoforms=("ProteinID", "nunique"),
        Unique_chromosomes=("Chromosome", "nunique"),
        Multi_block_peptide_rows=("BED_block_count", lambda x: (x > 1).sum())
    )
    .reset_index()
)

gene_summary.insert(0, "Index", range(1, len(gene_summary) + 1))
gene_summary.to_csv(gene_summary_out, index=False)


# -----------------------------
# 8. Protein / isoform summary across all tissues
# -----------------------------
protein_summary = (
    all_projected
    .groupby(["ProteinID", gene_col, confidence_col], dropna=False)
    .agg(
        Sources=("Source", lambda x: "|".join(sorted(set(map(str, x))))),
        Tissues=("Tissue", lambda x: "|".join(sorted(set(map(str, x))))),
        Tissue_count=("Tissue", lambda x: len(set(x))),
        Projected_peptide_rows=("Peptide", "size"),
        Unique_peptides=("Peptide", "nunique"),
        Unique_chromosomes=("Chromosome", "nunique"),
        Multi_block_peptide_rows=("BED_block_count", lambda x: (x > 1).sum())
    )
    .reset_index()
)

protein_summary.insert(0, "Index", range(1, len(protein_summary) + 1))
protein_summary.to_csv(protein_summary_out, index=False)


# -----------------------------
# 9. Source-level summary
# -----------------------------
source_records = []

for source, group in all_projected.groupby("Source", dropna=False):

    hc = group[group[confidence_col].astype(str).str.upper() == "HC"]
    lc = group[group[confidence_col].astype(str).str.upper() == "LC"]

    unique_genes = group[gene_col].nunique()
    unique_hc_genes = hc[gene_col].nunique()
    unique_lc_genes = lc[gene_col].nunique()

    source_records.append({
        "Source": source,
        "Projected_peptide_rows": len(group),
        "Unique_tissues": group["Tissue"].nunique(),
        "Unique_peptides": group["Peptide"].nunique(),
        "Unique_proteins_isoforms": group["ProteinID"].nunique(),
        "Unique_gene_models": unique_genes,
        "Unique_HC_gene_models": unique_hc_genes,
        "Unique_LC_gene_models": unique_lc_genes,
        "Percent_total_gene_models_detected": pct(unique_genes, total_gene_models),
        "Percent_HC_gene_models_detected": pct(unique_hc_genes, total_hc_gene_models),
        "Percent_LC_gene_models_detected": pct(unique_lc_genes, total_lc_gene_models)
    })

source_summary = pd.DataFrame(source_records)
source_summary.to_csv(source_summary_out, index=False)


# -----------------------------
# 10. Display outputs
# -----------------------------
print(f"\nTissue-level summary saved: {tissue_summary_out}")
print(f"Gene model summary saved: {gene_summary_out}")
print(f"Protein/isoform summary saved: {protein_summary_out}")
print(f"Source-level summary saved: {source_summary_out}")

display(tissue_summary)
display(source_summary)
```

    Genome annotation denominators
    Total gene models: 266,752
    HC gene models: 106,914
    LC gene models: 159,838
    Protein isoforms: 295,914
    
    Projected peptide rows loaded: 8,291,056
    
    Tissue-level summary saved: python_outputs\tables\wheat_tissue_level_summary_step13.csv
    Gene model summary saved: python_outputs\tables\wheat_gene_model_summary_step13.csv
    Protein/isoform summary saved: python_outputs\tables\wheat_protein_isoform_summary_step13.csv
    Source-level summary saved: python_outputs\tables\wheat_source_level_summary_step13.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Projected_peptide_rows</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins_isoforms</th>
      <th>Unique_gene_models</th>
      <th>Unique_HC_gene_models</th>
      <th>Unique_LC_gene_models</th>
      <th>Percent_total_gene_models_detected</th>
      <th>Percent_HC_gene_models_detected</th>
      <th>Percent_LC_gene_models_detected</th>
      <th>Unique_chromosomes</th>
      <th>Multi_block_peptide_rows</th>
      <th>Proteins_supported_by_one_peptide</th>
      <th>Proteins_supported_by_two_or_more_peptides</th>
      <th>Genes_supported_by_one_peptide</th>
      <th>Genes_supported_by_two_or_more_peptides</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>30314</td>
      <td>9329</td>
      <td>17478</td>
      <td>14903</td>
      <td>9169</td>
      <td>5734</td>
      <td>5.5868</td>
      <td>8.5761</td>
      <td>3.5874</td>
      <td>22</td>
      <td>3291</td>
      <td>14132</td>
      <td>3346</td>
      <td>12085</td>
      <td>2818</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>164365</td>
      <td>34098</td>
      <td>36826</td>
      <td>29384</td>
      <td>21425</td>
      <td>7959</td>
      <td>11.0155</td>
      <td>20.0395</td>
      <td>4.9794</td>
      <td>22</td>
      <td>27776</td>
      <td>19936</td>
      <td>16890</td>
      <td>16541</td>
      <td>12843</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>13227</td>
      <td>3643</td>
      <td>9208</td>
      <td>7361</td>
      <td>5420</td>
      <td>1941</td>
      <td>2.7595</td>
      <td>5.0695</td>
      <td>1.2144</td>
      <td>22</td>
      <td>2728</td>
      <td>7285</td>
      <td>1923</td>
      <td>5897</td>
      <td>1464</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>204476</td>
      <td>41025</td>
      <td>46496</td>
      <td>36872</td>
      <td>26825</td>
      <td>10047</td>
      <td>13.8226</td>
      <td>25.0903</td>
      <td>6.2857</td>
      <td>22</td>
      <td>31344</td>
      <td>23572</td>
      <td>22924</td>
      <td>19818</td>
      <td>17054</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>8852</td>
      <td>2867</td>
      <td>7220</td>
      <td>5858</td>
      <td>4214</td>
      <td>1644</td>
      <td>2.1960</td>
      <td>3.9415</td>
      <td>1.0285</td>
      <td>22</td>
      <td>1411</td>
      <td>6285</td>
      <td>935</td>
      <td>5152</td>
      <td>706</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>102830</td>
      <td>20081</td>
      <td>27454</td>
      <td>21878</td>
      <td>16070</td>
      <td>5808</td>
      <td>8.2016</td>
      <td>15.0308</td>
      <td>3.6337</td>
      <td>22</td>
      <td>14269</td>
      <td>15841</td>
      <td>11613</td>
      <td>13128</td>
      <td>8750</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>145133</td>
      <td>28648</td>
      <td>35540</td>
      <td>28724</td>
      <td>20555</td>
      <td>8169</td>
      <td>10.7681</td>
      <td>19.2257</td>
      <td>5.1108</td>
      <td>22</td>
      <td>22131</td>
      <td>19968</td>
      <td>15572</td>
      <td>16662</td>
      <td>12062</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>126195</td>
      <td>26196</td>
      <td>35532</td>
      <td>28677</td>
      <td>20658</td>
      <td>8019</td>
      <td>10.7504</td>
      <td>19.3221</td>
      <td>5.0170</td>
      <td>22</td>
      <td>17478</td>
      <td>20510</td>
      <td>15022</td>
      <td>17259</td>
      <td>11418</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>179725</td>
      <td>35960</td>
      <td>47076</td>
      <td>36918</td>
      <td>26989</td>
      <td>9929</td>
      <td>13.8398</td>
      <td>25.2437</td>
      <td>6.2119</td>
      <td>22</td>
      <td>27658</td>
      <td>24690</td>
      <td>22386</td>
      <td>20769</td>
      <td>16149</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>132701</td>
      <td>27463</td>
      <td>41029</td>
      <td>32610</td>
      <td>24271</td>
      <td>8339</td>
      <td>12.2248</td>
      <td>22.7014</td>
      <td>5.2172</td>
      <td>22</td>
      <td>18650</td>
      <td>23251</td>
      <td>17778</td>
      <td>19474</td>
      <td>13136</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>113203</td>
      <td>23990</td>
      <td>36635</td>
      <td>29435</td>
      <td>21216</td>
      <td>8219</td>
      <td>11.0346</td>
      <td>19.8440</td>
      <td>5.1421</td>
      <td>22</td>
      <td>14734</td>
      <td>21674</td>
      <td>14961</td>
      <td>18228</td>
      <td>11207</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>111792</td>
      <td>24636</td>
      <td>34874</td>
      <td>28087</td>
      <td>20047</td>
      <td>8040</td>
      <td>10.5293</td>
      <td>18.7506</td>
      <td>5.0301</td>
      <td>22</td>
      <td>14886</td>
      <td>21235</td>
      <td>13639</td>
      <td>17740</td>
      <td>10347</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>145632</td>
      <td>29840</td>
      <td>37954</td>
      <td>30373</td>
      <td>22463</td>
      <td>7910</td>
      <td>11.3862</td>
      <td>21.0103</td>
      <td>4.9488</td>
      <td>22</td>
      <td>19448</td>
      <td>19758</td>
      <td>18196</td>
      <td>16433</td>
      <td>13940</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>46200</td>
      <td>11354</td>
      <td>25696</td>
      <td>21261</td>
      <td>14354</td>
      <td>6907</td>
      <td>7.9703</td>
      <td>13.4257</td>
      <td>4.3213</td>
      <td>22</td>
      <td>4572</td>
      <td>18836</td>
      <td>6860</td>
      <td>15872</td>
      <td>5389</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>120821</td>
      <td>23373</td>
      <td>32620</td>
      <td>26238</td>
      <td>18878</td>
      <td>7360</td>
      <td>9.8361</td>
      <td>17.6572</td>
      <td>4.6047</td>
      <td>22</td>
      <td>15227</td>
      <td>17531</td>
      <td>15089</td>
      <td>14534</td>
      <td>11704</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>147618</td>
      <td>29788</td>
      <td>37927</td>
      <td>30445</td>
      <td>21851</td>
      <td>8594</td>
      <td>11.4132</td>
      <td>20.4379</td>
      <td>5.3767</td>
      <td>22</td>
      <td>21753</td>
      <td>20855</td>
      <td>17072</td>
      <td>17320</td>
      <td>13125</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>99823</td>
      <td>21457</td>
      <td>36542</td>
      <td>29969</td>
      <td>19881</td>
      <td>10088</td>
      <td>11.2348</td>
      <td>18.5953</td>
      <td>6.3114</td>
      <td>22</td>
      <td>12765</td>
      <td>23369</td>
      <td>13173</td>
      <td>19696</td>
      <td>10273</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>169675</td>
      <td>34124</td>
      <td>42356</td>
      <td>33736</td>
      <td>24960</td>
      <td>8776</td>
      <td>12.6470</td>
      <td>23.3459</td>
      <td>5.4906</td>
      <td>22</td>
      <td>22888</td>
      <td>21374</td>
      <td>20982</td>
      <td>17945</td>
      <td>15791</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>116936</td>
      <td>21707</td>
      <td>27580</td>
      <td>21779</td>
      <td>16403</td>
      <td>5376</td>
      <td>8.1645</td>
      <td>15.3422</td>
      <td>3.3634</td>
      <td>22</td>
      <td>20681</td>
      <td>14019</td>
      <td>13561</td>
      <td>11405</td>
      <td>10374</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>131215</td>
      <td>28332</td>
      <td>32667</td>
      <td>25960</td>
      <td>18944</td>
      <td>7016</td>
      <td>9.7319</td>
      <td>17.7189</td>
      <td>4.3894</td>
      <td>22</td>
      <td>20964</td>
      <td>18598</td>
      <td>14069</td>
      <td>15393</td>
      <td>10567</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>74698</td>
      <td>13502</td>
      <td>19931</td>
      <td>16058</td>
      <td>12178</td>
      <td>3880</td>
      <td>6.0198</td>
      <td>11.3905</td>
      <td>2.4275</td>
      <td>22</td>
      <td>9490</td>
      <td>10805</td>
      <td>9126</td>
      <td>8883</td>
      <td>7175</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>160204</td>
      <td>31145</td>
      <td>37204</td>
      <td>29549</td>
      <td>21454</td>
      <td>8095</td>
      <td>11.0773</td>
      <td>20.0666</td>
      <td>5.0645</td>
      <td>22</td>
      <td>24784</td>
      <td>19588</td>
      <td>17616</td>
      <td>16297</td>
      <td>13252</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>194694</td>
      <td>39643</td>
      <td>42965</td>
      <td>33865</td>
      <td>25722</td>
      <td>8143</td>
      <td>12.6953</td>
      <td>24.0586</td>
      <td>5.0945</td>
      <td>22</td>
      <td>32499</td>
      <td>22390</td>
      <td>20575</td>
      <td>18724</td>
      <td>15141</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>97188</td>
      <td>21350</td>
      <td>39156</td>
      <td>31553</td>
      <td>22163</td>
      <td>9390</td>
      <td>11.8286</td>
      <td>20.7297</td>
      <td>5.8747</td>
      <td>22</td>
      <td>10898</td>
      <td>26297</td>
      <td>12859</td>
      <td>21852</td>
      <td>9701</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>100639</td>
      <td>21284</td>
      <td>32046</td>
      <td>25509</td>
      <td>18705</td>
      <td>6804</td>
      <td>9.5628</td>
      <td>17.4954</td>
      <td>4.2568</td>
      <td>22</td>
      <td>15547</td>
      <td>20041</td>
      <td>12005</td>
      <td>16472</td>
      <td>9037</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>191943</td>
      <td>38634</td>
      <td>39774</td>
      <td>30937</td>
      <td>23718</td>
      <td>7219</td>
      <td>11.5977</td>
      <td>22.1842</td>
      <td>4.5164</td>
      <td>22</td>
      <td>35031</td>
      <td>18861</td>
      <td>20913</td>
      <td>15675</td>
      <td>15262</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>111831</td>
      <td>20815</td>
      <td>30626</td>
      <td>23808</td>
      <td>18214</td>
      <td>5594</td>
      <td>8.9251</td>
      <td>17.0361</td>
      <td>3.4998</td>
      <td>22</td>
      <td>14833</td>
      <td>16692</td>
      <td>13934</td>
      <td>13630</td>
      <td>10178</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>188826</td>
      <td>36370</td>
      <td>40207</td>
      <td>31027</td>
      <td>23528</td>
      <td>7499</td>
      <td>11.6314</td>
      <td>22.0065</td>
      <td>4.6916</td>
      <td>22</td>
      <td>33193</td>
      <td>19851</td>
      <td>20356</td>
      <td>16433</td>
      <td>14594</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>60734</td>
      <td>14338</td>
      <td>29410</td>
      <td>23675</td>
      <td>16641</td>
      <td>7034</td>
      <td>8.8753</td>
      <td>15.5648</td>
      <td>4.4007</td>
      <td>22</td>
      <td>6949</td>
      <td>20194</td>
      <td>9216</td>
      <td>16775</td>
      <td>6900</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>1850136</td>
      <td>582775</td>
      <td>239461</td>
      <td>211806</td>
      <td>97522</td>
      <td>114284</td>
      <td>79.4018</td>
      <td>91.2154</td>
      <td>71.4999</td>
      <td>22</td>
      <td>228372</td>
      <td>59391</td>
      <td>180070</td>
      <td>57302</td>
      <td>154504</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>1886922</td>
      <td>595954</td>
      <td>242813</td>
      <td>215038</td>
      <td>98279</td>
      <td>116759</td>
      <td>80.6135</td>
      <td>91.9234</td>
      <td>73.0483</td>
      <td>22</td>
      <td>235642</td>
      <td>57470</td>
      <td>185343</td>
      <td>55363</td>
      <td>159675</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>1062508</td>
      <td>333058</td>
      <td>206016</td>
      <td>179884</td>
      <td>89997</td>
      <td>89887</td>
      <td>67.4349</td>
      <td>84.1770</td>
      <td>56.2363</td>
      <td>22</td>
      <td>118195</td>
      <td>68189</td>
      <td>137827</td>
      <td>64784</td>
      <td>115100</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Projected_peptide_rows</th>
      <th>Unique_tissues</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins_isoforms</th>
      <th>Unique_gene_models</th>
      <th>Unique_HC_gene_models</th>
      <th>Unique_LC_gene_models</th>
      <th>Percent_total_gene_models_detected</th>
      <th>Percent_HC_gene_models_detected</th>
      <th>Percent_LC_gene_models_detected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>30314</td>
      <td>1</td>
      <td>9329</td>
      <td>17478</td>
      <td>14903</td>
      <td>9169</td>
      <td>5734</td>
      <td>5.5868</td>
      <td>8.5761</td>
      <td>3.5874</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720</td>
      <td>3461176</td>
      <td>28</td>
      <td>234920</td>
      <td>174207</td>
      <td>150849</td>
      <td>79808</td>
      <td>71041</td>
      <td>56.5503</td>
      <td>74.6469</td>
      <td>44.4456</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>4799566</td>
      <td>3</td>
      <td>994270</td>
      <td>274010</td>
      <td>245338</td>
      <td>103930</td>
      <td>141408</td>
      <td>91.9723</td>
      <td>97.2090</td>
      <td>88.4696</td>
    </tr>
  </tbody>
</table>
</div>


# Step 14 — Prepare BED Files for Apollo/JBrowse Public Upload

This step prepares all BED files generated during the proteogenomics workflow for permanent upload to the public Apollo/JBrowse server.

The BED files include:

```text
annotation-projected peptide evidence
```

---

## Input directories

### Annotation-based proteogenomic BED files

```text
python_outputs/bed/
```

---

## Apollo/JBrowse upload directory

A new output directory was created:

```text
python_outputs/bed_apollo/
```

All BED files were copied into this directory and renamed using a standardised Apollo-compatible nomenclature.

---

## Apollo/JBrowse filename nomenclature

The following naming convention was applied:

```text
Vincent_Source_Tissue_projected-peptides_annotation-proteogenomics_20260518.bed
```

for annotation-projected peptide tracks, and:

### Examples

```text
Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed12
```

---

## Purpose

These BED tracks are intended for permanent upload and public visualisation on the Apollo/JBrowse wheat genome browser server:

```text
https://bread-wheat-um.genome.edu.au/apollo/49826/jbrowse/
```

The resulting tracks provide genome-wide visualisation of:

- experimentally identified wheat peptides,
- peptide-supported gene models,
- peptides spanning CDS junctions.

This creates a public proteogenomics resource supporting wheat genome annotation refinement and community exploration.


```python
# ============================================================
# Step 14 — Prepare Apollo/JBrowse BED files for public upload
# ============================================================

import shutil
from pathlib import Path
import re

# -----------------------------
# 1. Input / output directories
# -----------------------------
bed_dir = Path("python_outputs/bed")

apollo_dir = Path("python_outputs/bed_apollo")
apollo_dir.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 2. Collect all BED files
# -----------------------------
bed_files = list(bed_dir.glob("*.bed*"))

print(f"BED files found: {len(bed_files):,}")

# -----------------------------
# 3. Helper functions
# -----------------------------
def simplify_tissue_name(tissue):
    """
    Standardise tissue names for Apollo filenames.
    """
    tissue = tissue.replace("-", "_")
    tissue = tissue.replace(" ", "_")
    tissue = re.sub(r"_+", "_", tissue)
    return tissue.strip("_")


def parse_standard_bed_filename(filename):
    """
    Parse standard annotation-projected BED filenames.

    Example:
    FragPipe_Duncan_PXD004720_anther_peptides.bed6
    """

    match = re.match(
        r"FragPipe_(?P<Author>[^_]+)_(?P<Source>MSV\d+|PXD\d+)_(?P<Tissue>.+?)_peptides\.bed(6|12)",
        filename
    )

    if match is None:
        return None

    return {
        "Author": "Vincent",
        "Source": match.group("Source"),
        "Tissue": simplify_tissue_name(match.group("Tissue")),
        "TrackType": "annotation"
    }


def build_apollo_filename(meta, suffix):
    """
    Build Apollo-compatible BED filename.
    """

    if meta["TrackType"] == "annotation":
        track_label = "projected-peptides_annotation-proteogenomics"

    else:
        track_label = "proteogenomics"

    return (
        f"{meta['Author']}_"
        f"{meta['Source']}_"
        f"{meta['Tissue']}_"
        f"{track_label}_"
        f"20260518."
        f"{suffix}"
    )

# -----------------------------
# 4. Copy and rename BED files
# -----------------------------
copied_count = 0

for bed_file in bed_files:

    filename = bed_file.name

    # Detect BED suffix
    if filename.endswith(".bed6"):
        suffix = "bed6"
    elif filename.endswith(".bed12"):
        suffix = "bed12"
    else:
        print(f"Skipped non-BED file: {filename}")
        continue

    # Parse metadata
    if filename.startswith("FragPipe_"):
        meta = parse_standard_bed_filename(filename)

    else:
        print(f"Skipped unrecognised BED filename: {filename}")
        continue

    if meta is None:
        print(f"Could not parse filename: {filename}")
        continue

    # Build Apollo filename
    apollo_filename = build_apollo_filename(meta, suffix)

    destination = apollo_dir / apollo_filename

    shutil.copy2(bed_file, destination)

    copied_count += 1

    print(f"Copied:")
    print(f"  {filename}")
    print(f"  -> {apollo_filename}")

print(f"\nApollo BED files prepared: {copied_count:,}")
print(f"Output directory: {apollo_dir}")
```

    BED files found: 66
    Copied:
      FragPipe_Duncan_PXD004720_anther_peptides.bed12
      -> Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_anther_peptides.bed6
      -> Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_boot_peptides.bed12
      -> Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_boot_peptides.bed6
      -> Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_coleoptile_peptides.bed12
      -> Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_coleoptile_peptides.bed6
      -> Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_embryo_peptides.bed12
      -> Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_embryo_peptides.bed6
      -> Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_endosperm_peptides.bed12
      -> Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_endosperm_peptides.bed6
      -> Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_glume_peptides.bed12
      -> Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_glume_peptides.bed6
      -> Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-70_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-70_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-71_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-71_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-75_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-75_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-83_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-83_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-87_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-87_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-mature_peptides.bed12
      -> Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-mature_peptides.bed6
      -> Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptides.bed12
      -> Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptides.bed6
      -> Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-young_peptides.bed12
      -> Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-young_peptides.bed6
      -> Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_lemma_peptides.bed12
      -> Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_lemma_peptides.bed6
      -> Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_node-secretion_peptides.bed12
      -> Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_node-secretion_peptides.bed6
      -> Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_node_peptides.bed12
      -> Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_node_peptides.bed6
      -> Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_palea_peptides.bed12
      -> Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_palea_peptides.bed6
      -> Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_pericarp_peptides.bed12
      -> Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_pericarp_peptides.bed6
      -> Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_pollen_peptides.bed12
      -> Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_pollen_peptides.bed6
      -> Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_rachilla_peptides.bed12
      -> Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_rachilla_peptides.bed6
      -> Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_radicle_peptides.bed12
      -> Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_radicle_peptides.bed6
      -> Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-mature_peptides.bed12
      -> Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-mature_peptides.bed6
      -> Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-secretion_peptides.bed12
      -> Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-secretion_peptides.bed6
      -> Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-tip_peptides.bed12
      -> Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-tip_peptides.bed6
      -> Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-vasculature_peptides.bed12
      -> Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-vasculature_peptides.bed6
      -> Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_spike-immature_peptides.bed12
      -> Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_spike-immature_peptides.bed6
      -> Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Duncan_PXD004720_stem_peptides.bed12
      -> Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Duncan_PXD004720_stem_peptides.bed6
      -> Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Liu_PXD050500_coleoptile_peptides.bed12
      -> Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Liu_PXD050500_coleoptile_peptides.bed6
      -> Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Liu_PXD050500_node_peptides.bed12
      -> Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Liu_PXD050500_node_peptides.bed6
      -> Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Liu_PXD050500_radicle_peptides.bed12
      -> Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Liu_PXD050500_radicle_peptides.bed6
      -> Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    Copied:
      FragPipe_Vincent_MSV000090572_stored-grain_peptides.bed12
      -> Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed12
    Copied:
      FragPipe_Vincent_MSV000090572_stored-grain_peptides.bed6
      -> Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed6
    Skipped unrecognised BED filename: wheat_all_tissues_nonredundant_projected_peptides.bed12
    Skipped unrecognised BED filename: wheat_all_tissues_nonredundant_projected_peptides.bed6
    
    Apollo BED files prepared: 64
    Output directory: python_outputs\bed_apollo
    

# Step 15 — EDA: HC and LC Proteogenomic Coverage by Tissue

This exploratory analysis compares proteogenomic evidence across all wheat source–tissue combinations.

The aim is to visualise how much annotation-supported proteomic evidence was obtained from each tissue, separated into:

```text
high-confidence annotation-projected evidence
low-confidence annotation-projected evidence
```

---

## Input files

### Peptide genome projection tables from Step 9

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only successfully projected peptide rows were included.

### Protein-to-gene mapping table from Step 5

```text
wheat_protein_gene_mapping_HC_LC.csv
```

This table was used to define the total number of annotated wheat gene models used as the denominator for percentage calculations.

---

## Percentage denominator

All percentages were calculated relative to:

```text
total number of annotated wheat gene models
```

This provides a common denominator across HC and LC evidence categories.

---

## Evidence categories

| Category | Description |
|---|---|
| HC | Proteins projected through high-confidence wheat gene models |
| LC | Proteins projected through low-confidence wheat gene models |

---

## Metrics calculated

### 1. Unique proteins

The number of non-redundant protein accessions supported by projected peptides within each source–tissue combination.

### 2. Unique peptides

The number of non-redundant peptide sequences associated with projected proteins within each source–tissue combination.

### 3. Protein-level coverage percentages

Protein coverage was calculated as:

```text
unique projected proteins / total annotated gene models × 100
```

Peptide percentages were intentionally not calculated because multiple peptides can support a single gene model, which can generate biologically misleading values exceeding 100%.

---

## Plots generated

### Protein-level proteogenomic coverage plot

This plot shows unique projected protein accessions separated into HC and LC evidence categories.

```text
step15_source_tissue_protein_coverage_HC_LC.png
```

---

## Output files

### Summary table

```text
wheat_eda_HC_LC_coverage_step15.csv
```

### Figures

```text
python_outputs/figures/
```

---

## Colour scheme

The plots use the project brand colours:

| Evidence category | Colour |
|---|---|
| HC | Dark purple |
| LC | Pink |

These figures provide an overview of tissue-level annotation-supported proteogenomic coverage and highlight the relative contribution of HC and LC wheat gene models across tissues.


```python
# ============================================================
# Step 15 — EDA: HC/LC coverage by tissue
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
```

    Total annotated gene models used as denominator: 266,752
    Projected rows loaded for Step 15: 8,291,056
    Saved corrected Step 15 summary: python_outputs\tables\wheat_eda_coverage_HC_LC_step15.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Tissue</th>
      <th>Source_Tissue</th>
      <th>HC_unique_proteins</th>
      <th>LC_unique_proteins</th>
      <th>HC_unique_peptides</th>
      <th>LC_unique_peptides</th>
      <th>HC_protein_percent</th>
      <th>LC_protein_percent</th>
      <th>Total_protein_percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>embryo</td>
      <td>PXD004720_embryo</td>
      <td>5544</td>
      <td>1676</td>
      <td>2166</td>
      <td>914</td>
      <td>2.078335</td>
      <td>0.628299</td>
      <td>2.706634</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>boot</td>
      <td>PXD004720_boot</td>
      <td>7224</td>
      <td>1984</td>
      <td>2881</td>
      <td>1050</td>
      <td>2.708133</td>
      <td>0.743762</td>
      <td>3.451895</td>
    </tr>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>11648</td>
      <td>5830</td>
      <td>6395</td>
      <td>3580</td>
      <td>4.366603</td>
      <td>2.185551</td>
      <td>6.552153</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>pollen</td>
      <td>PXD004720_pollen</td>
      <td>15984</td>
      <td>3947</td>
      <td>12494</td>
      <td>2799</td>
      <td>5.992083</td>
      <td>1.479652</td>
      <td>7.471734</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>leaf-flag-senescing</td>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>18655</td>
      <td>7041</td>
      <td>8807</td>
      <td>3707</td>
      <td>6.993387</td>
      <td>2.639530</td>
      <td>9.632917</td>
    </tr>
  </tbody>
</table>
</div>



    
![png](output_29_2.png)
    


    Figure saved: python_outputs\figures\step15_source_tissue_protein_coverage_HC_LC.png
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Tissue</th>
      <th>Source_Tissue</th>
      <th>HC_unique_proteins</th>
      <th>LC_unique_proteins</th>
      <th>HC_unique_peptides</th>
      <th>LC_unique_peptides</th>
      <th>HC_protein_percent</th>
      <th>LC_protein_percent</th>
      <th>Total_protein_percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>embryo</td>
      <td>PXD004720_embryo</td>
      <td>5544</td>
      <td>1676</td>
      <td>2166</td>
      <td>914</td>
      <td>2.078335</td>
      <td>0.628299</td>
      <td>2.706634</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>boot</td>
      <td>PXD004720_boot</td>
      <td>7224</td>
      <td>1984</td>
      <td>2881</td>
      <td>1050</td>
      <td>2.708133</td>
      <td>0.743762</td>
      <td>3.451895</td>
    </tr>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>11648</td>
      <td>5830</td>
      <td>6395</td>
      <td>3580</td>
      <td>4.366603</td>
      <td>2.185551</td>
      <td>6.552153</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>pollen</td>
      <td>PXD004720_pollen</td>
      <td>15984</td>
      <td>3947</td>
      <td>12494</td>
      <td>2799</td>
      <td>5.992083</td>
      <td>1.479652</td>
      <td>7.471734</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>leaf-flag-senescing</td>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>18655</td>
      <td>7041</td>
      <td>8807</td>
      <td>3707</td>
      <td>6.993387</td>
      <td>2.639530</td>
      <td>9.632917</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>endosperm</td>
      <td>PXD004720_endosperm</td>
      <td>21535</td>
      <td>5919</td>
      <td>18150</td>
      <td>4153</td>
      <td>8.073042</td>
      <td>2.218915</td>
      <td>10.291957</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>palea</td>
      <td>PXD004720_palea</td>
      <td>22119</td>
      <td>5461</td>
      <td>20187</td>
      <td>4039</td>
      <td>8.291972</td>
      <td>2.047220</td>
      <td>10.339191</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>stem</td>
      <td>PXD004720_stem</td>
      <td>22217</td>
      <td>7193</td>
      <td>11574</td>
      <td>4207</td>
      <td>8.328710</td>
      <td>2.696512</td>
      <td>11.025222</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>root-vasculature</td>
      <td>PXD004720_root-vasculature</td>
      <td>24900</td>
      <td>5726</td>
      <td>19182</td>
      <td>3879</td>
      <td>9.334513</td>
      <td>2.146563</td>
      <td>11.481076</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>root-secretion</td>
      <td>PXD004720_root-secretion</td>
      <td>25118</td>
      <td>6928</td>
      <td>18206</td>
      <td>5146</td>
      <td>9.416237</td>
      <td>2.597169</td>
      <td>12.013406</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>leaf-flag-young</td>
      <td>PXD004720_leaf-flag-young</td>
      <td>25112</td>
      <td>7508</td>
      <td>21785</td>
      <td>4346</td>
      <td>9.413988</td>
      <td>2.814599</td>
      <td>12.228587</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>pericarp</td>
      <td>PXD004720_pericarp</td>
      <td>25512</td>
      <td>7155</td>
      <td>25772</td>
      <td>5337</td>
      <td>9.563940</td>
      <td>2.682267</td>
      <td>12.246206</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>grain-zadoks-87</td>
      <td>PXD004720_grain-zadoks-87</td>
      <td>26675</td>
      <td>8199</td>
      <td>21667</td>
      <td>5519</td>
      <td>9.999925</td>
      <td>3.073641</td>
      <td>13.073566</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>grain-zadoks-70</td>
      <td>PXD004720_grain-zadoks-70</td>
      <td>27365</td>
      <td>8167</td>
      <td>23686</td>
      <td>5313</td>
      <td>10.258592</td>
      <td>3.061645</td>
      <td>13.320238</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>glume</td>
      <td>PXD004720_glume</td>
      <td>27234</td>
      <td>8306</td>
      <td>26117</td>
      <td>5865</td>
      <td>10.209483</td>
      <td>3.113754</td>
      <td>13.323237</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>node</td>
      <td>PXD004720_node</td>
      <td>26266</td>
      <td>10276</td>
      <td>18293</td>
      <td>5608</td>
      <td>9.846599</td>
      <td>3.852267</td>
      <td>13.698866</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>grain-zadoks-83</td>
      <td>PXD004720_grain-zadoks-83</td>
      <td>28248</td>
      <td>8387</td>
      <td>21239</td>
      <td>5315</td>
      <td>10.589611</td>
      <td>3.144119</td>
      <td>13.733730</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>anther</td>
      <td>PXD004720_anther</td>
      <td>28693</td>
      <td>8133</td>
      <td>31564</td>
      <td>6057</td>
      <td>10.756433</td>
      <td>3.048899</td>
      <td>13.805332</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>rachilla</td>
      <td>PXD004720_rachilla</td>
      <td>28965</td>
      <td>8239</td>
      <td>28819</td>
      <td>5720</td>
      <td>10.858400</td>
      <td>3.088637</td>
      <td>13.947037</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>lemma</td>
      <td>PXD004720_lemma</td>
      <td>29169</td>
      <td>8758</td>
      <td>27278</td>
      <td>5895</td>
      <td>10.934876</td>
      <td>3.283199</td>
      <td>14.218075</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>leaf-flag-mature</td>
      <td>PXD004720_leaf-flag-mature</td>
      <td>29893</td>
      <td>8061</td>
      <td>27643</td>
      <td>5529</td>
      <td>11.206289</td>
      <td>3.021908</td>
      <td>14.228197</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>root-mature</td>
      <td>PXD004720_root-mature</td>
      <td>29580</td>
      <td>9576</td>
      <td>17386</td>
      <td>6111</td>
      <td>11.088952</td>
      <td>3.589851</td>
      <td>14.678803</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>root-tip</td>
      <td>PXD004720_root-tip</td>
      <td>32397</td>
      <td>7377</td>
      <td>36440</td>
      <td>5770</td>
      <td>12.144989</td>
      <td>2.765490</td>
      <td>14.910479</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>spike-immature</td>
      <td>PXD004720_spike-immature</td>
      <td>32554</td>
      <td>7653</td>
      <td>33863</td>
      <td>6236</td>
      <td>12.203845</td>
      <td>2.868957</td>
      <td>15.072802</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>grain-zadoks-75</td>
      <td>PXD004720_grain-zadoks-75</td>
      <td>32506</td>
      <td>8523</td>
      <td>24629</td>
      <td>5801</td>
      <td>12.185851</td>
      <td>3.195103</td>
      <td>15.380953</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>node_secretion</td>
      <td>PXD004720_node_secretion</td>
      <td>33400</td>
      <td>8956</td>
      <td>31855</td>
      <td>6047</td>
      <td>12.520993</td>
      <td>3.357426</td>
      <td>15.878419</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>radicle</td>
      <td>PXD004720_radicle</td>
      <td>34656</td>
      <td>8309</td>
      <td>36848</td>
      <td>6649</td>
      <td>12.991843</td>
      <td>3.114878</td>
      <td>16.106721</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>coleoptile</td>
      <td>PXD004720_coleoptile</td>
      <td>36231</td>
      <td>10265</td>
      <td>38024</td>
      <td>7336</td>
      <td>13.582279</td>
      <td>3.848144</td>
      <td>17.430422</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>grain-zadoks-71</td>
      <td>PXD004720_grain-zadoks-71</td>
      <td>36950</td>
      <td>10126</td>
      <td>33041</td>
      <td>6524</td>
      <td>13.851817</td>
      <td>3.796035</td>
      <td>17.647853</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>radicle</td>
      <td>PXD050500_radicle</td>
      <td>114118</td>
      <td>91898</td>
      <td>252340</td>
      <td>100268</td>
      <td>42.780560</td>
      <td>34.450726</td>
      <td>77.231286</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>coleoptile</td>
      <td>PXD050500_coleoptile</td>
      <td>122649</td>
      <td>116812</td>
      <td>446378</td>
      <td>169664</td>
      <td>45.978662</td>
      <td>43.790487</td>
      <td>89.769149</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>node</td>
      <td>PXD050500_node</td>
      <td>123444</td>
      <td>119369</td>
      <td>450326</td>
      <td>179930</td>
      <td>46.276691</td>
      <td>44.749055</td>
      <td>91.025747</td>
    </tr>
  </tbody>
</table>
</div>


# Step 16 — EDA: Tissue Overlap Using UpSet Plots

This exploratory analysis investigates the overlap of proteogenomic evidence across wheat tissues using UpSet plots.

Because the study includes a large number of tissues and datasets, traditional Venn diagrams become impractical. UpSet plots provide a scalable alternative for visualising shared and tissue-specific proteogenomic features.

---

## Input files

### Peptide genome projection tables from Step 9

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only successfully projected peptide rows were included.

### Filtering rule

```text
Projection_status == "projected"
```

---

## Tissue grouping strategy

Each tissue was represented using a combined identifier:

```text
Source_Tissue
```

### Example

```text
PXD004720_anther
MSV000090572_stored_grain
```

This allows tissue-specific overlap analysis while preserving the origin of the proteomics dataset.

---

## Overlap categories analysed

Three independent UpSet analyses were performed:

| Analysis | Feature type |
|---|---|
| Protein overlap | Protein isoforms |
| Peptide overlap | Peptide sequences |
| Gene model overlap | Wheat gene models |

---

## UpSet plot interpretation

The UpSet plots visualise:

- tissue-specific features,
- shared features across tissues,
- and the frequency of different tissue-overlap combinations.

### Main components

| Component | Meaning |
|---|---|
| Horizontal bars | Total feature count per tissue |
| Vertical bars | Size of feature intersections |
| Connected dots | Tissue combinations contributing to each intersection |

---

## Figures generated

### Protein isoform overlap

```text
step16_upsetplot_tissue_overlap_proteins.png
```

### Peptide sequence overlap

```text
step16_upsetplot_tissue_overlap_peptides.png
```

### Gene model overlap

```text
step16_upsetplot_tissue_overlap_gene_models.png
```

---

## Output directory

```text
python_outputs/figures/
```

---

## Summary table

A Step 16 summary table was generated.

### Output file

```text
wheat_tissue_overlap_summary_step16.csv
```

### Metrics captured

| Metric | Description |
|---|---|
| Unique_projected_proteins | Number of unique projected protein isoforms |
| Unique_projected_peptides | Number of unique projected peptide sequences |
| Unique_projected_gene_models | Number of unique projected wheat gene models |

---

## Purpose

These analyses help identify:

- highly tissue-specific proteogenomic signatures,
- broadly shared wheat proteins and peptides,
- and tissues contributing the greatest diversity of proteogenomic evidence.

The UpSet plots also provide a global overview of tissue complementarity within the proteogenomics workflow.


```python
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
```

    Projected rows loaded: 8,291,056
    


    
![png](output_31_1.png)
    


    Figure saved: python_outputs\figures\step16_upsetplot_tissue_overlap_proteins.png
    


    
![png](output_31_3.png)
    


    Figure saved: python_outputs\figures\step16_upsetplot_tissue_overlap_peptides.png
    


    
![png](output_31_5.png)
    


    Figure saved: python_outputs\figures\step16_upsetplot_tissue_overlap_gene_models.png
    
    Step 16 summary saved: python_outputs\tables\wheat_tissue_overlap_summary_step16.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source_Tissue</th>
      <th>Unique_projected_proteins</th>
      <th>Unique_projected_peptides</th>
      <th>Unique_projected_gene_models</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>PXD050500_node</td>
      <td>242813</td>
      <td>595954</td>
      <td>215038</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD050500_coleoptile</td>
      <td>239461</td>
      <td>582775</td>
      <td>211806</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD050500_radicle</td>
      <td>206016</td>
      <td>333058</td>
      <td>179884</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720_grain-zadoks-71</td>
      <td>47076</td>
      <td>35960</td>
      <td>36918</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD004720_coleoptile</td>
      <td>46496</td>
      <td>41025</td>
      <td>36872</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720_radicle</td>
      <td>42965</td>
      <td>39643</td>
      <td>33865</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720_node_secretion</td>
      <td>42356</td>
      <td>34124</td>
      <td>33736</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720_grain-zadoks-75</td>
      <td>41029</td>
      <td>27463</td>
      <td>32610</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720_root-mature</td>
      <td>39156</td>
      <td>21350</td>
      <td>31553</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720_spike-immature</td>
      <td>40207</td>
      <td>36370</td>
      <td>31027</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720_root-tip</td>
      <td>39774</td>
      <td>38634</td>
      <td>30937</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720_lemma</td>
      <td>37927</td>
      <td>29788</td>
      <td>30445</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720_leaf-flag-mature</td>
      <td>37954</td>
      <td>29840</td>
      <td>30373</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720_node</td>
      <td>36542</td>
      <td>21457</td>
      <td>29969</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720_rachilla</td>
      <td>37204</td>
      <td>31145</td>
      <td>29549</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720_grain-zadoks-83</td>
      <td>36635</td>
      <td>23990</td>
      <td>29435</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720_anther</td>
      <td>36826</td>
      <td>34098</td>
      <td>29384</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720_glume</td>
      <td>35540</td>
      <td>28648</td>
      <td>28724</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720_grain-zadoks-70</td>
      <td>35532</td>
      <td>26196</td>
      <td>28677</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720_grain-zadoks-87</td>
      <td>34874</td>
      <td>24636</td>
      <td>28087</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720_leaf-flag-young</td>
      <td>32620</td>
      <td>23373</td>
      <td>26238</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720_pericarp</td>
      <td>32667</td>
      <td>28332</td>
      <td>25960</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720_root-secretion</td>
      <td>32046</td>
      <td>21284</td>
      <td>25509</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720_root-vasculature</td>
      <td>30626</td>
      <td>20815</td>
      <td>23808</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720_stem</td>
      <td>29410</td>
      <td>14338</td>
      <td>23675</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720_endosperm</td>
      <td>27454</td>
      <td>20081</td>
      <td>21878</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720_palea</td>
      <td>27580</td>
      <td>21707</td>
      <td>21779</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>25696</td>
      <td>11354</td>
      <td>21261</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720_pollen</td>
      <td>19931</td>
      <td>13502</td>
      <td>16058</td>
    </tr>
    <tr>
      <th>0</th>
      <td>MSV000090572_stored_grain</td>
      <td>17478</td>
      <td>9329</td>
      <td>14903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD004720_boot</td>
      <td>9208</td>
      <td>3643</td>
      <td>7361</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720_embryo</td>
      <td>7220</td>
      <td>2867</td>
      <td>5858</td>
    </tr>
  </tbody>
</table>
</div>


# Step 17 — EDA: Peptide Support per Gene Model

This exploratory analysis examines how many unique peptide sequences support each detected wheat gene model.

The aim is to evaluate the strength of proteomics evidence at the gene model level and compare peptide support between high-confidence (HC) and low-confidence (LC) annotations.

---

## Input file

### Gene model summary table from Step 13

```text
wheat_gene_model_summary_step13.csv
```

This table contains one row per detected gene model and includes the number of unique peptides, protein isoforms, tissues, and sources supporting each gene model.

---

## Analysis strategy

For each detected gene model, the number of unique supporting peptide sequences was extracted.

The analysis was stratified by annotation confidence:

```text
HC = high-confidence gene model
LC = low-confidence gene model
```

---

## Peptide support categories

Gene models were grouped into peptide-support classes:

| Category | Description |
|---|---|
| 1 peptide | Gene model supported by one unique peptide |
| 2–4 peptides | Gene model supported by two to four unique peptides |
| 5–9 peptides | Gene model supported by five to nine unique peptides |
| ≥10 peptides | Gene model supported by ten or more unique peptides |

---

## Figures generated

### 1. Histogram of peptide support per gene model

```text
step17_peptide_support_per_gene_model_histogram.png
```

This plot shows the distribution of unique peptide counts per gene model. A log-scaled x-axis was used because most gene models are expected to be supported by relatively few peptides, while a smaller number may be supported by many peptides.

### 2. HC vs LC boxplot

```text
step17_peptide_support_per_gene_model_HC_LC_boxplot.png
```

This plot compares peptide support between HC and LC gene models. The y-axis was log-scaled to improve visualisation of both low- and high-support gene models.

---

## Summary table

A Step 17 summary table was generated.

### Output file

```text
wheat_peptide_support_per_gene_model_summary_step17.csv
```

### Metrics captured

| Metric | Description |
|---|---|
| Gene_model_count | Number of gene models in each peptide-support category |
| Median_unique_peptides | Median number of unique peptides per gene model |
| Mean_unique_peptides | Mean number of unique peptides per gene model |
| Max_unique_peptides | Maximum number of unique peptides observed |
| Total_gene_models_with_peptide_support | Total detected gene models within each annotation class |
| Percent_within_confidence_class | Percentage of detected HC or LC gene models in each support category |

---

## Purpose

This analysis provides an overview of the strength of peptide evidence supporting wheat gene model annotations.

It helps identify:

- gene models supported by minimal peptide evidence,
- gene models with strong multi-peptide support,
- differences in evidence strength between HC and LC annotations,
- and highly supported gene models that may represent abundant or broadly detected proteins.


```python
# ============================================================
# Step 17 — EDA: Peptide support per gene model
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
```

    Gene models with peptide support: 249,082
    


    
![png](output_33_1.png)
    


    Histogram saved: python_outputs\figures\step17_peptide_support_per_gene_model_histogram.png
    


    
![png](output_33_3.png)
    


    Boxplot saved: python_outputs\figures\step17_peptide_support_per_gene_model_HC_LC_boxplot.png
    Step 17 summary saved: python_outputs\tables\wheat_peptide_support_per_gene_model_summary_step17.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Annotation_confidence</th>
      <th>Peptide_support_bin</th>
      <th>Gene_model_count</th>
      <th>Median_unique_peptides</th>
      <th>Mean_unique_peptides</th>
      <th>Max_unique_peptides</th>
      <th>Total_gene_models_with_peptide_support</th>
      <th>Percent_within_confidence_class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>1 peptide</td>
      <td>4088</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>104576</td>
      <td>3.9091</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HC</td>
      <td>2–4 peptides</td>
      <td>17236</td>
      <td>3.0</td>
      <td>3.038698</td>
      <td>4</td>
      <td>104576</td>
      <td>16.4818</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HC</td>
      <td>5–9 peptides</td>
      <td>26541</td>
      <td>7.0</td>
      <td>6.868430</td>
      <td>9</td>
      <td>104576</td>
      <td>25.3796</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HC</td>
      <td>≥10 peptides</td>
      <td>56711</td>
      <td>20.0</td>
      <td>26.219622</td>
      <td>318</td>
      <td>104576</td>
      <td>54.2295</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LC</td>
      <td>1 peptide</td>
      <td>23596</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>144506</td>
      <td>16.3287</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LC</td>
      <td>2–4 peptides</td>
      <td>61744</td>
      <td>3.0</td>
      <td>2.870400</td>
      <td>4</td>
      <td>144506</td>
      <td>42.7276</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LC</td>
      <td>5–9 peptides</td>
      <td>39752</td>
      <td>6.0</td>
      <td>6.490466</td>
      <td>9</td>
      <td>144506</td>
      <td>27.5089</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LC</td>
      <td>≥10 peptides</td>
      <td>19414</td>
      <td>13.0</td>
      <td>16.487792</td>
      <td>217</td>
      <td>144506</td>
      <td>13.4347</td>
    </tr>
  </tbody>
</table>
</div>


# Step 18 — EDA: Peptide Length, Probability, and Charge by Annotation Confidence

This exploratory analysis compares peptide-level identification characteristics between high-confidence (HC) and low-confidence (LC) wheat gene model annotations.

A scatterplot was generated to visualise the relationship between peptide length and peptide identification probability, with charge state represented by point size.

---

## Input files

### Peptide genome projection tables from Step 9

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only successfully projected peptide rows were included.

### Filtering rule

```text
Projection_status == "projected"
```

---

## Plot design

| Visual element | Variable |
|---|---|
| x-axis | Peptide length in amino acids |
| y-axis | Peptide probability |
| Point colour | Annotation confidence: HC or LC |
| Point size | Peptide charge state |

---

## Charge handling

FragPipe may report one or multiple charge states for a peptide.

When multiple charge states were present, the maximum reported charge state was used for point size representation.

---

## Downsampling

Because the full projected peptide table contains millions of rows, a random sample was used for plotting to improve readability and computational performance.

The summary statistics were calculated from the full dataset.

---

## Output files

### Figure

```text
step18_peptide_length_probability_charge_HC_LC_scatter.png
```

### Summary table

```text
wheat_peptide_length_charge_probability_summary_step18.csv
```

---

## Purpose

This plot helps assess whether peptides supporting HC and LC annotations differ in:

- peptide length,
- identification probability,
- charge state distribution,
- or overall peptide evidence quality.


```python
# ============================================================
# Step 18 — EDA: Peptide length, probability, and charge by HC/LC
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re

# -----------------------------
# 1. Paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

step18_summary_out = tables_dir / "wheat_peptide_length_charge_probability_summary_step18.csv"
scatter_out = figures_dir / "step18_peptide_length_probability_charge_HC_LC_scatter.png"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399",
    "gold": "#FFC000",
    "lavender": "#E6CDFF"
}

# -----------------------------
# 3. Helper function
# -----------------------------
def parse_charge(value):
    """
    Convert FragPipe charge values into one numeric value.
    Handles values such as:
    2
    2,3
    2;3
    2|3
    """
    if pd.isna(value):
        return pd.NA

    values = re.findall(r"\d+", str(value))

    if len(values) == 0:
        return pd.NA

    # Use maximum observed charge state when multiple are reported
    return max(int(v) for v in values)

# -----------------------------
# 4. Load a small random sample from projected peptide tables
# -----------------------------
all_sampled_tables = []

max_points_total = 10000
n_files = len(manifest)
sample_per_file = max(200, max_points_total // n_files)

needed_cols = [
    "Projection_status",
    "Peptide",
    "Peptide_length_AA",
    "Probability",
    "Charges",
    "Annotation_confidence"
]

chunksize = 100_000

for _, row in manifest.iterrows():

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Warning: missing file, skipped: {projection_path}")
        continue

    print(f"Sampling from: {projection_filename}")

    file_samples = []

    for chunk in pd.read_csv(
        projection_path,
        usecols=lambda col: col in needed_cols,
        chunksize=chunksize,
        low_memory=False
    ):

        chunk = chunk[
            (chunk["Projection_status"] == "projected") &
            (chunk["Annotation_confidence"].isin(["HC", "LC"]))
        ]

        if chunk.empty:
            continue

        n_sample = min(50, len(chunk))

        file_samples.append(
            chunk.sample(
                n=n_sample,
                random_state=42
            )
        )

    if len(file_samples) == 0:
        continue

    file_sample = pd.concat(file_samples, ignore_index=True)

    if len(file_sample) > sample_per_file:
        file_sample = file_sample.sample(
            n=sample_per_file,
            random_state=42
        )

    all_sampled_tables.append(file_sample)

plot_data = pd.concat(all_sampled_tables, ignore_index=True)

if len(plot_data) > max_points_total:
    plot_data = plot_data.sample(
        n=max_points_total,
        random_state=42
    ).copy()

print(f"Rows used for scatterplot: {len(plot_data):,}")

# -----------------------------
# 5. Prepare plotting variables
# -----------------------------
confidence_col = "Annotation_confidence"

if "Peptide_length_AA" not in plot_data.columns:
    plot_data["Peptide_length_AA"] = plot_data["Peptide"].astype(str).str.len()

plot_data["Probability"] = pd.to_numeric(
    plot_data["Probability"],
    errors="coerce"
)

plot_data["Charge_numeric"] = plot_data["Charges"].apply(parse_charge)

plot_data = plot_data.dropna(
    subset=["Peptide_length_AA", "Probability", "Charge_numeric"]
).copy()

plot_data["Dot_size"] = plot_data["Charge_numeric"] * 12

# -----------------------------
# 6. Summary table
# -----------------------------
# randomly sampled dataset (memory friendly)
step18_summary = (
    plot_data
    .groupby(confidence_col, dropna=False)
    .agg(
        Sampled_peptide_rows=("Peptide", "size"),
        Unique_peptides=("Peptide", "nunique"),
        Mean_peptide_length=("Peptide_length_AA", "mean"),
        Median_peptide_length=("Peptide_length_AA", "median"),
        Mean_probability=("Probability", "mean"),
        Median_probability=("Probability", "median"),
        Mean_charge=("Charge_numeric", "mean"),
        Median_charge=("Charge_numeric", "median")
    )
    .reset_index()
)

step18_summary.to_csv(step18_summary_out, index=False)

# -----------------------------
# 7. Scatterplot
# -----------------------------
plt.figure(figsize=(10, 7))

for confidence in ["HC", "LC"]:

    subset = plot_data[plot_data[confidence_col] == confidence]

    plt.scatter(
        subset["Peptide_length_AA"],
        subset["Probability"],
        s=subset["Dot_size"],
        alpha=0.25,
        color=brand_colours[confidence],
        label=confidence,
        edgecolors="none"
    )

plt.xlabel("Peptide length (amino acids)")
plt.ylabel("Peptide probability")
plt.title("Peptide length, probability, and charge state by annotation confidence")

plt.legend(
    title="Annotation confidence",
    markerscale=1.5
)

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    scatter_out,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Scatterplot saved: {scatter_out}")
print(f"Step 18 summary saved: {step18_summary_out}")

display(step18_summary)
```

    Sampling from: FragPipe_Vincent_MSV000090572_stored-grain_peptide_genome_projection.csv
    Sampling from: FragPipe_Liu_PXD050500_coleoptile_peptide_genome_projection.csv
    Sampling from: FragPipe_Liu_PXD050500_node_peptide_genome_projection.csv
    Sampling from: FragPipe_Liu_PXD050500_radicle_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_anther_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_boot_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_coleoptile_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_embryo_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_endosperm_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_glume_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_lemma_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_node_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_node-secretion_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_palea_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_pericarp_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_pollen_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_rachilla_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_radicle_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_root-mature_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_root-secretion_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_root-tip_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_root-vasculature_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_spike-immature_peptide_genome_projection.csv
    Sampling from: FragPipe_Duncan_PXD004720_stem_peptide_genome_projection.csv
    Rows used for scatterplot: 3,486
    


    
![png](output_35_1.png)
    


    Scatterplot saved: python_outputs\figures\step18_peptide_length_probability_charge_HC_LC_scatter.png
    Step 18 summary saved: python_outputs\tables\wheat_peptide_length_charge_probability_summary_step18.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Annotation_confidence</th>
      <th>Sampled_peptide_rows</th>
      <th>Unique_peptides</th>
      <th>Mean_peptide_length</th>
      <th>Median_peptide_length</th>
      <th>Mean_probability</th>
      <th>Median_probability</th>
      <th>Mean_charge</th>
      <th>Median_charge</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>3064</td>
      <td>2891</td>
      <td>13.698433</td>
      <td>12.0</td>
      <td>0.855652</td>
      <td>0.9989</td>
      <td>2.458551</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LC</td>
      <td>422</td>
      <td>408</td>
      <td>12.457346</td>
      <td>11.0</td>
      <td>0.586741</td>
      <td>0.6620</td>
      <td>2.319905</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>


# Step 19 — EDA: Protein Length versus Peptide Support

This exploratory analysis investigates the relationship between protein length and peptide support across wheat protein isoforms.

The aim is to determine whether longer proteins tend to accumulate greater peptide evidence and whether this relationship differs between high-confidence (HC) and low-confidence (LC) annotations.

---

## Input files

### Protein isoform summary table from Step 13

```text
wheat_protein_isoform_summary_step13.csv
```

### Protein-to-gene mapping table from Step 5

```text
wheat_protein_gene_mapping_HC_LC.csv
```

---

## Plot design

| Visual element | Variable |
|---|---|
| x-axis | Protein length derived from CDS annotation |
| y-axis | Number of unique supporting peptides |
| Point colour | Annotation confidence (HC or LC) |

---

## Variables used

### Protein length

```text
Protein_length_aa_from_CDS
```

Protein length corresponds to the amino acid length inferred from CDS annotations in the wheat genome annotation.

### Peptide support

```text
Unique_peptides
```

This corresponds to the number of unique peptide sequences supporting each protein isoform.

---

## Figure generated

```text
step19_protein_length_vs_peptide_support_scatter.png
```

---

## Summary table

A Step 22 summary table was generated.

### Output file

```text
wheat_protein_length_vs_peptide_support_summary_step19.csv
```

### Metrics captured

| Metric | Description |
|---|---|
| Protein_isoforms | Number of detected protein isoforms |
| Mean_protein_length_aa | Mean protein length |
| Median_protein_length_aa | Median protein length |
| Max_protein_length_aa | Maximum protein length |
| Mean_unique_peptides | Mean number of unique peptides |
| Median_unique_peptides | Median number of unique peptides |
| Max_unique_peptides | Maximum number of unique peptides observed |

---

## Purpose

This analysis helps evaluate whether peptide support scales with protein length and whether HC and LC annotations display different peptide-support characteristics.

The plot also highlights highly supported protein isoforms and potential outliers within the wheat proteogenomics dataset.


```python
# ============================================================
# Step 19 — EDA: Protein length vs peptide support
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
```

    Proteins plotted: 277,852
    


    
![png](output_37_1.png)
    


    Scatterplot saved: python_outputs\figures\step19_protein_length_vs_peptide_support_scatter.png
    Step 19 summary saved: python_outputs\tables\wheat_protein_length_vs_peptide_support_summary_step19.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Annotation_confidence</th>
      <th>Protein_isoforms</th>
      <th>Mean_protein_length_aa</th>
      <th>Median_protein_length_aa</th>
      <th>Max_protein_length_aa</th>
      <th>Mean_unique_peptides</th>
      <th>Median_unique_peptides</th>
      <th>Max_unique_peptides</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>130182</td>
      <td>450.447317</td>
      <td>383.0</td>
      <td>5366.0</td>
      <td>18.652425</td>
      <td>12.0</td>
      <td>318</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LC</td>
      <td>147670</td>
      <td>211.899793</td>
      <td>158.0</td>
      <td>4979.0</td>
      <td>5.392280</td>
      <td>4.0</td>
      <td>217</td>
    </tr>
  </tbody>
</table>
</div>


# Step 20 — EDA: Chromosomal Distribution of Peptide Genomic Start Positions

This exploratory analysis recreates the chromosome-level violin plot used in the 2024 wheat proteogenomics study, updated with the expanded 2026 multi-tissue dataset.

The aim is to visualise where peptide evidence is distributed along each wheat chromosome, including annotation-projected HC and LC peptides.

---

## Input files

### Non-redundant annotation-projected peptide table from Step 11

```text
wheat_all_tissues_nonredundant_projected_peptides.csv
```
---

## Evidence categories

| Category | Description |
|---|---|
| HC peptide | Peptide projected through a high-confidence wheat gene model |
| LC peptide | Peptide projected through a low-confidence wheat gene model |

---

## Plot design

| Plot element | Variable |
|---|---|
| x-axis | Wheat chromosome |
| y-axis | Peptide genomic start position |
| Colour | Evidence category: HC, LC |

The plot includes the 21 wheat chromosomes plus:

```text
ChrUnknown
```

so that all chromosome categories represented in the dataset can be visualised.

---

## Sampling strategy

Because the full peptide projection table contains millions of rows, values were sampled within each chromosome/evidence group for plotting efficiency.

The summary table was calculated from the full dataset.

---

## Output files

### Figure

```text
step20_violinplot_peptide_genomic_start_by_chromosome.png
```

### Summary table

```text
wheat_peptide_genomic_start_by_chromosome_summary_step20.csv
```

---

## Purpose

This visualisation provides a genome-wide overview of peptide evidence distribution and enables comparison of:

- HC annotation-supported peptide evidence,
- LC annotation-supported peptide evidence.

It is designed to support direct comparison with the chromosome-level proteogenomic distribution figure from the 2024 wheat proteogenomics resource paper.


```python
# ============================================================
# Step 20 — EDA: Chromosome distribution of peptide genomic positions
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

projection_combined_file = tables_dir / "wheat_all_tissues_nonredundant_projected_peptides.csv"

figure_out = figures_dir / "step20_violinplot_peptide_genomic_start_by_chromosome.png"
summary_out = tables_dir / "wheat_peptide_genomic_start_by_chromosome_summary_step20.csv"

# -----------------------------
# 2. Brand colours
# -----------------------------
brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399"
}

# -----------------------------
# 3. Load annotation-projected peptide data in chunks
# -----------------------------
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

chrom_col = "Chromosome"
start_col = "BED_start_0based"
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

# Load ProteinID → Annotation_confidence lookup
protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    usecols=lambda col: col in [protein_col, confidence_col],
    low_memory=False
)

protein_conf_lookup = (
    protein_mapping
    .dropna(subset=[protein_col, confidence_col])
    .drop_duplicates(subset=[protein_col])
)

projected_needed_cols = [
    chrom_col,
    start_col,
    protein_col
]

max_points_per_group = 50000
chunksize = 100_000

summary_chunks = []
sample_chunks = []

for chunk in pd.read_csv(
    projection_combined_file,
    usecols=lambda col: col in projected_needed_cols,
    chunksize=chunksize,
    low_memory=False
):

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
    )

    chunk["Chromosome"] = chunk["Chromosome"].astype(str)

    summary_chunks.append(
        chunk[["Chromosome", "Genomic_start", "Evidence"]]
    )

    # Sample lightly from each chunk for plotting
    if len(chunk) > 3000:
        chunk_sample = chunk.sample(
            n=3000,
            random_state=42
        )
    else:
        chunk_sample = chunk

    sample_chunks.append(
        chunk_sample[["Chromosome", "Genomic_start", "Evidence"]]
    )

projected_summary_data = pd.concat(summary_chunks, ignore_index=True)
projected_plot_sample = pd.concat(sample_chunks, ignore_index=True)

print(f"Projected rows for summary: {len(projected_summary_data):,}")
print(f"Projected sampled rows before group cap: {len(projected_plot_sample):,}")

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

projected_summary_data["Chromosome"] = projected_summary_data["Chromosome"].apply(normalise_chromosome_name)
projected_plot_sample["Chromosome"] = projected_plot_sample["Chromosome"].apply(normalise_chromosome_name)

projected_summary_data = projected_summary_data[
    projected_summary_data["Chromosome"].isin(chrom_order)
].copy()

projected_plot_sample = projected_plot_sample[
    projected_plot_sample["Chromosome"].isin(chrom_order)
].copy()

# -----------------------------
# 5. Build summary table from full projected data
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
        Peptide_rows=("Genomic_start", "size"),
        Median_genomic_start=("Genomic_start", "median"),
        Mean_genomic_start=("Genomic_start", "mean"),
        Min_genomic_start=("Genomic_start", "min"),
        Max_genomic_start=("Genomic_start", "max")
    )
    .reset_index()
)

summary.to_csv(summary_out, index=False)

# Free memory before plotting
del projected_summary_data
del summary_data
del summary_chunks

# -----------------------------
# 6. Build plot sample and cap per chromosome/evidence group
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
        "Check chromosome names in the input tables."
    )

plot_sample = pd.concat(sampled_groups, ignore_index=True)

print(f"Rows used for violin plot: {len(plot_sample):,}")


# -----------------------------
# 7. Violin plot
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
            "Genomic_start"
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
        body.set_alpha(1)

    violin["cmedians"].set_color("white")
    violin["cmedians"].set_linewidth(1.2)

# -----------------------------
# 8. Plot formatting
# -----------------------------

ax.set_xticks(list(positions))

ax.set_xticklabels(
    chrom_order,
    rotation=45,
    ha="right",
    fontsize=12
)

# Y-axis tick labels
ax.tick_params(
    axis="y",
    labelsize=12
)

# Axis labels
ax.set_xlabel(
    "Chromosome",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

ax.set_ylabel(
    "Peptide genomic start position",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

# Title
ax.set_title(
    "Genomic distribution of HC and LC peptide evidence by chromosome",
    fontsize=20,
    fontweight="bold",
    pad=20
)

# Grid
ax.grid(axis="y", linestyle="--", alpha=0.3)

# Manual legend
legend_labels = {
    "HC": "HC",
    "LC": "LC"
}

legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="o",
        color="w",
        label=legend_labels[label],
        markerfacecolor=colour,
        markeredgecolor="black",
        markersize=14
    )
    for label, colour in brand_colours.items()
]

legend = ax.legend(
    handles=legend_handles,
    title="Legend",
    title_fontsize=14,
    fontsize=14,
    loc="upper right",
    frameon=True
)

# Bold legend title
legend.get_title().set_fontweight("bold")

# Optional: thicker legend border
legend.get_frame().set_linewidth(1.5)

# Tight layout
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
```

    Projected rows for summary: 3,224,488
    Projected sampled rows before group cap: 99,000
    Rows used for violin plot: 99,000
    


    
![png](output_39_1.png)
    


    Figure saved: python_outputs\figures\step20_violinplot_peptide_genomic_start_by_chromosome.png
    Summary saved: python_outputs\tables\wheat_peptide_genomic_start_by_chromosome_summary_step20.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Chromosome</th>
      <th>Evidence</th>
      <th>Peptide_rows</th>
      <th>Median_genomic_start</th>
      <th>Mean_genomic_start</th>
      <th>Min_genomic_start</th>
      <th>Max_genomic_start</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Chr1A</td>
      <td>HC</td>
      <td>102785</td>
      <td>378520882.0</td>
      <td>3.411754e+08</td>
      <td>58543</td>
      <td>598561110</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chr1A</td>
      <td>LC</td>
      <td>33210</td>
      <td>370919131.5</td>
      <td>3.332170e+08</td>
      <td>41201</td>
      <td>598363879</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chr1B</td>
      <td>HC</td>
      <td>109468</td>
      <td>416739307.0</td>
      <td>3.834039e+08</td>
      <td>168112</td>
      <td>700379123</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Chr1B</td>
      <td>LC</td>
      <td>39263</td>
      <td>370917562.0</td>
      <td>3.624798e+08</td>
      <td>520312</td>
      <td>700376310</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Chr1D</td>
      <td>HC</td>
      <td>106460</td>
      <td>303287708.0</td>
      <td>2.775585e+08</td>
      <td>20705</td>
      <td>498609718</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Chr1D</td>
      <td>LC</td>
      <td>30206</td>
      <td>266404424.0</td>
      <td>2.672430e+08</td>
      <td>20687</td>
      <td>498498248</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Chr2A</td>
      <td>HC</td>
      <td>130632</td>
      <td>501782804.5</td>
      <td>4.238702e+08</td>
      <td>251216</td>
      <td>787195194</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Chr2A</td>
      <td>LC</td>
      <td>39713</td>
      <td>428628820.0</td>
      <td>4.121603e+08</td>
      <td>249001</td>
      <td>787082048</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Chr2B</td>
      <td>HC</td>
      <td>135400</td>
      <td>444573110.0</td>
      <td>4.146318e+08</td>
      <td>29396</td>
      <td>812720911</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Chr2B</td>
      <td>LC</td>
      <td>47911</td>
      <td>418945614.0</td>
      <td>4.155830e+08</td>
      <td>113609</td>
      <td>812724460</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Chr2D</td>
      <td>HC</td>
      <td>133488</td>
      <td>367807133.0</td>
      <td>3.371833e+08</td>
      <td>81486</td>
      <td>656399532</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Chr2D</td>
      <td>LC</td>
      <td>38368</td>
      <td>368739264.0</td>
      <td>3.468261e+08</td>
      <td>307945</td>
      <td>656397474</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Chr3A</td>
      <td>HC</td>
      <td>121656</td>
      <td>478300732.0</td>
      <td>4.055248e+08</td>
      <td>26772</td>
      <td>754027813</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Chr3A</td>
      <td>LC</td>
      <td>37100</td>
      <td>459791785.0</td>
      <td>4.058733e+08</td>
      <td>109656</td>
      <td>754051399</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Chr3B</td>
      <td>HC</td>
      <td>130121</td>
      <td>479411014.0</td>
      <td>4.405457e+08</td>
      <td>74006</td>
      <td>851873079</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Chr3B</td>
      <td>LC</td>
      <td>47080</td>
      <td>482879192.0</td>
      <td>4.544109e+08</td>
      <td>66880</td>
      <td>851822590</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Chr3D</td>
      <td>HC</td>
      <td>128866</td>
      <td>361378248.0</td>
      <td>3.227838e+08</td>
      <td>110201</td>
      <td>619490011</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Chr3D</td>
      <td>LC</td>
      <td>32356</td>
      <td>339257020.0</td>
      <td>3.218520e+08</td>
      <td>121439</td>
      <td>619441473</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Chr4A</td>
      <td>HC</td>
      <td>114425</td>
      <td>473058367.0</td>
      <td>4.000253e+08</td>
      <td>80753</td>
      <td>754178416</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Chr4A</td>
      <td>LC</td>
      <td>38542</td>
      <td>550173980.5</td>
      <td>4.651186e+08</td>
      <td>189937</td>
      <td>754141599</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Chr4B</td>
      <td>HC</td>
      <td>100213</td>
      <td>396066887.0</td>
      <td>3.454357e+08</td>
      <td>244</td>
      <td>673727718</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Chr4B</td>
      <td>LC</td>
      <td>32078</td>
      <td>366237711.5</td>
      <td>3.506044e+08</td>
      <td>690282</td>
      <td>673722692</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Chr4D</td>
      <td>HC</td>
      <td>97823</td>
      <td>302669143.0</td>
      <td>2.594031e+08</td>
      <td>410358</td>
      <td>514856857</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Chr4D</td>
      <td>LC</td>
      <td>25021</td>
      <td>277337249.0</td>
      <td>2.654539e+08</td>
      <td>464134</td>
      <td>512646336</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Chr5A</td>
      <td>HC</td>
      <td>120079</td>
      <td>464663231.0</td>
      <td>4.173051e+08</td>
      <td>13924</td>
      <td>713330062</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Chr5A</td>
      <td>LC</td>
      <td>38594</td>
      <td>472175707.0</td>
      <td>4.084900e+08</td>
      <td>216418</td>
      <td>713172935</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Chr5B</td>
      <td>HC</td>
      <td>127808</td>
      <td>444708895.0</td>
      <td>4.072841e+08</td>
      <td>16318</td>
      <td>714774033</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Chr5B</td>
      <td>LC</td>
      <td>40874</td>
      <td>429771729.0</td>
      <td>3.916751e+08</td>
      <td>6650</td>
      <td>714795420</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Chr5D</td>
      <td>HC</td>
      <td>128275</td>
      <td>370144516.0</td>
      <td>3.319864e+08</td>
      <td>297066</td>
      <td>569875777</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Chr5D</td>
      <td>LC</td>
      <td>34704</td>
      <td>368267723.5</td>
      <td>3.236685e+08</td>
      <td>140015</td>
      <td>569892303</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Chr6A</td>
      <td>HC</td>
      <td>92603</td>
      <td>405490196.0</td>
      <td>3.353303e+08</td>
      <td>118076</td>
      <td>622585150</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Chr6A</td>
      <td>LC</td>
      <td>31922</td>
      <td>300300761.5</td>
      <td>3.039192e+08</td>
      <td>4145</td>
      <td>622591126</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Chr6B</td>
      <td>HC</td>
      <td>101277</td>
      <td>442599367.0</td>
      <td>3.880181e+08</td>
      <td>4898</td>
      <td>731066437</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Chr6B</td>
      <td>LC</td>
      <td>41642</td>
      <td>387024324.0</td>
      <td>3.775135e+08</td>
      <td>5675</td>
      <td>730950773</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Chr6D</td>
      <td>HC</td>
      <td>91764</td>
      <td>312591135.0</td>
      <td>2.720982e+08</td>
      <td>43504</td>
      <td>495304993</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Chr6D</td>
      <td>LC</td>
      <td>26041</td>
      <td>247341006.0</td>
      <td>2.525238e+08</td>
      <td>27358</td>
      <td>495205351</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Chr7A</td>
      <td>HC</td>
      <td>114245</td>
      <td>320363391.0</td>
      <td>3.543689e+08</td>
      <td>237590</td>
      <td>744483725</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Chr7A</td>
      <td>LC</td>
      <td>40572</td>
      <td>364887518.0</td>
      <td>3.689063e+08</td>
      <td>122054</td>
      <td>744312979</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Chr7B</td>
      <td>HC</td>
      <td>108202</td>
      <td>392793308.5</td>
      <td>3.822092e+08</td>
      <td>33340</td>
      <td>764068236</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Chr7B</td>
      <td>LC</td>
      <td>42639</td>
      <td>438208974.0</td>
      <td>4.094903e+08</td>
      <td>56572</td>
      <td>764067061</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Chr7D</td>
      <td>HC</td>
      <td>116863</td>
      <td>287389395.0</td>
      <td>3.124912e+08</td>
      <td>208449</td>
      <td>642831821</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Chr7D</td>
      <td>LC</td>
      <td>37946</td>
      <td>305180074.5</td>
      <td>3.121796e+08</td>
      <td>173586</td>
      <td>642831014</td>
    </tr>
    <tr>
      <th>42</th>
      <td>ChrUnknown</td>
      <td>HC</td>
      <td>15757</td>
      <td>134768042.0</td>
      <td>1.323768e+08</td>
      <td>7635176</td>
      <td>347551051</td>
    </tr>
    <tr>
      <th>43</th>
      <td>ChrUnknown</td>
      <td>LC</td>
      <td>20496</td>
      <td>214922270.5</td>
      <td>1.885482e+08</td>
      <td>806019</td>
      <td>351238213</td>
    </tr>
  </tbody>
</table>
</div>


# Step 21 — EDA: Circular Tissue-Level Peptide Genome Map

This final exploratory analysis generates a Circos-style circular genome map showing projected peptide evidence across wheat chromosomes and tissues.

The figure is inspired by the circular peptide distribution plot generated in the 2024 wheat proteogenomics study, but is produced here directly in Python using `pycirclize`.

---

## Input files

### Peptide genome projection tables from Step 9

One file per tissue:

```text
FragPipe_FirstAuthor_Source_Tissue-Raw-Code_peptide_genome_projection.csv
```

Only successfully projected peptide rows were included.

### Filtering rule

```text
Projection_status == "projected"
```

### Parsed GFF3 annotation table from Step 5

```text
wheat_gff3_parsed_features_HC_LC.csv
```

This table was used to estimate chromosome lengths for circular plotting.

---

## Plot design

The circular plot contains:

| Plot element | Description |
|---|---|
| Outer sectors | Wheat chromosomes |
| Inner rings | Individual source–tissue peptide tracks |
| Tick marks | Projected peptide genomic start positions |
| Colour | Tissue track identity |

Each tissue is represented as a separate ring, similar to the 2024 Galaxy Circos visualisation.

---

## Memory-light plotting strategy

Because the full projected peptide dataset contains millions of rows, the plotting procedure was designed to be memory efficient.

The workflow:

1. Reads each tissue projection file in chunks.
2. Keeps only projected peptide rows.
3. Samples peptide positions within each tissue/chromosome group.
4. Caps the number of plotted points per tissue and chromosome.

The summary table retains total projected peptide counts and sampled plotted counts.

---

## Chromosomes included

The plot includes the 21 assembled wheat chromosomes:

```text
Chr1A–Chr7D
```

`ChrUnknown` was excluded from the circular plot to preserve chromosome-scale interpretability.

---

## Output files

### Figure

```text
step21_circos_tissue_peptide_tracks.png
```

### Summary table

```text
wheat_circos_tissue_peptide_summary_step21.csv
```

---

## Purpose

This figure provides a genome-wide overview of peptide evidence across wheat tissues.

It highlights:

- chromosome-level peptide distribution,
- tissue-specific peptide evidence patterns,
- broad proteogenomic coverage across the wheat genome,
- and the suitability of the generated peptide tracks for public Apollo/JBrowse exploration.


```python
# # install library
# !pip install pycirclize
```


```python
# ============================================================
# Step 21 — EDA: Circular tissue-level peptide genome map
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict
from pycirclize import Circos

# -----------------------------
# 1. Paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

figure_out = figures_dir / "step21_circos_tissue_peptide_tracks.png"
summary_out = tables_dir / "wheat_circos_tissue_peptide_summary_step21.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

# -----------------------------
# 2. Parameters
# -----------------------------
chrom_order = [
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D"
]

max_points_per_tissue_chrom = 400
chunksize = 100_000

# -----------------------------
# 3. Helper functions
# -----------------------------
def normalise_chromosome_name(value):
    value = str(value).strip()

    if value.lower() in ["chrunknown", "unknown", "nan"]:
        return "ChrUnknown"

    if value.startswith("Chr"):
        return value

    return "Chr" + value


def clean_tissue_label(value):
    return str(value).replace("-", "_").replace(" ", "_")


# -----------------------------
# 4. Estimate chromosome lengths from GFF3 annotation
# -----------------------------
chrom_lengths = {}

for chunk in pd.read_csv(
    gff3_features_file,
    usecols=lambda col: col in ["SeqID", "End"],
    chunksize=chunksize,
    low_memory=False
):

    chunk["SeqID"] = chunk["SeqID"].apply(normalise_chromosome_name)
    chunk["End"] = pd.to_numeric(chunk["End"], errors="coerce")

    chunk = chunk.dropna(subset=["SeqID", "End"])

    for chrom, group in chunk.groupby("SeqID"):
        if chrom in chrom_order:
            max_end = int(group["End"].max())
            chrom_lengths[chrom] = max(max_end, chrom_lengths.get(chrom, 0))

chrom_lengths = {
    chrom: chrom_lengths[chrom]
    for chrom in chrom_order
    if chrom in chrom_lengths
}

print(f"Chromosomes loaded: {len(chrom_lengths)}")

# -----------------------------
# 5. Sample projected peptide positions by tissue and chromosome
# -----------------------------
tissue_positions = defaultdict(lambda: defaultdict(list))
summary_records = []

for _, row in manifest.iterrows():

    source = row["Source"]
    tissue = clean_tissue_label(row["Tissue-Raw-Code"])
    source_tissue = f"{source}_{tissue}"

    projection_filename = row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Warning: missing projection file, skipped: {projection_path}")
        continue

    print(f"Sampling: {source_tissue}")

    chrom_counts = defaultdict(int)

    for chunk in pd.read_csv(
        projection_path,
        usecols=lambda col: col in [
            "Projection_status",
            "Chromosome",
            "BED_start_0based"
        ],
        chunksize=chunksize,
        low_memory=False
    ):

        chunk = chunk[chunk["Projection_status"] == "projected"].copy()

        if chunk.empty:
            continue

        chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

        chunk = chunk[chunk["Chromosome"].isin(chrom_order)].copy()

        chunk["BED_start_0based"] = pd.to_numeric(
            chunk["BED_start_0based"],
            errors="coerce"
        )

        chunk = chunk.dropna(subset=["Chromosome", "BED_start_0based"])

        for chrom, group in chunk.groupby("Chromosome"):

            chrom_counts[chrom] += len(group)

            # Sample small number per chunk to avoid memory overload
            n_sample = min(50, len(group))

            tissue_positions[source_tissue][chrom].extend(
                group["BED_start_0based"]
                .sample(n=n_sample, random_state=42)
                .astype(int)
                .tolist()
            )

    # Final cap per tissue/chromosome
    for chrom in chrom_order:
        positions = tissue_positions[source_tissue][chrom]

        if len(positions) > max_points_per_tissue_chrom:
            positions = (
                pd.Series(positions)
                .sample(n=max_points_per_tissue_chrom, random_state=42)
                .astype(int)
                .tolist()
            )
            tissue_positions[source_tissue][chrom] = positions

        summary_records.append({
            "Source": source,
            "Tissue": tissue,
            "Source_Tissue": source_tissue,
            "Chromosome": chrom,
            "Total_projected_peptide_rows": chrom_counts.get(chrom, 0),
            "Sampled_points_plotted": len(tissue_positions[source_tissue][chrom])
        })

summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print(f"Summary saved: {summary_out}")

# -----------------------------
# 6. Tissue colours
# -----------------------------
source_tissues = list(tissue_positions.keys())

cmap = plt.get_cmap("tab20")
tissue_colours = {
    tissue: cmap(i % 20)
    for i, tissue in enumerate(source_tissues)
}

# -----------------------------
# 7. Build Circos plot
# -----------------------------
circos = Circos(chrom_lengths, space=2)

# Outer chromosome track
for sector in circos.sectors:
    outer_track = sector.add_track((96, 100))
    outer_track.axis(fc="#E6CDFF", ec="#3F007E", lw=0.6)

    sector.text(
        sector.name.replace("Chr", ""),
        r=104,
        size=14,
        weight="bold"
    )

# Tissue rings
n_tissues = len(source_tissues)
inner_r = 18
outer_r = 94
ring_height = (outer_r - inner_r) / n_tissues

for i, source_tissue in enumerate(source_tissues):

    r0 = inner_r + i * ring_height
    r1 = r0 + ring_height * 0.85

    colour = tissue_colours[source_tissue]

    for sector in circos.sectors:

        track = sector.add_track((r0, r1))
        track.axis(fc="white", ec="lightgrey", lw=0.15)

        chrom = sector.name
        positions = tissue_positions[source_tissue].get(chrom, [])

        if len(positions) == 0:
            continue

        y_values = [0.5] * len(positions)

        track.scatter(
            positions,
            y_values,
            s=4,
            color=colour,
            marker="|",
            linewidths=0.5
        )

# -----------------------------
# 8. Plot and legend
# -----------------------------
fig = circos.plotfig(figsize=(12, 12))

# Manual legend outside plot
legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="s",
        color="w",
        label=tissue,
        markerfacecolor=tissue_colours[tissue],
        markersize=8
    )
    for tissue in source_tissues
]

fig.legend(
    handles=legend_handles,
    title="Tissue tracks",
    loc="upper right",
    bbox_to_anchor=(1.25, 0.95),
    frameon=True,
    fontsize=10,
    title_fontsize=14
)

legend.get_title().set_fontweight("bold")
legend.get_frame().set_edgecolor("lightgrey")
legend.get_frame().set_linewidth(1)
legend.get_frame().set_facecolor("white")

fig.suptitle(
    "Circular map of projected wheat peptides by tissue",
    fontsize=16,
    fontweight="bold",
    y=1.02
)

plt.savefig(
    figure_out,
    dpi=600,
    bbox_inches="tight",
    facecolor="white"
)

plt.show()

print(f"Figure saved: {figure_out}")
display(summary.head())
```

    Chromosomes loaded: 21
    Sampling: MSV000090572_stored_grain
    Sampling: PXD050500_coleoptile
    Sampling: PXD050500_node
    Sampling: PXD050500_radicle
    Sampling: PXD004720_anther
    Sampling: PXD004720_boot
    Sampling: PXD004720_coleoptile
    Sampling: PXD004720_embryo
    Sampling: PXD004720_endosperm
    Sampling: PXD004720_glume
    Sampling: PXD004720_grain_zadoks_70
    Sampling: PXD004720_grain_zadoks_71
    Sampling: PXD004720_grain_zadoks_75
    Sampling: PXD004720_grain_zadoks_83
    Sampling: PXD004720_grain_zadoks_87
    Sampling: PXD004720_leaf_flag_mature
    Sampling: PXD004720_leaf_flag_senescing
    Sampling: PXD004720_leaf_flag_young
    Sampling: PXD004720_lemma
    Sampling: PXD004720_node
    Sampling: PXD004720_node_secretion
    Sampling: PXD004720_palea
    Sampling: PXD004720_pericarp
    Sampling: PXD004720_pollen
    Sampling: PXD004720_rachilla
    Sampling: PXD004720_radicle
    Sampling: PXD004720_root_mature
    Sampling: PXD004720_root_secretion
    Sampling: PXD004720_root_tip
    Sampling: PXD004720_root_vasculature
    Sampling: PXD004720_spike_immature
    Sampling: PXD004720_stem
    Summary saved: python_outputs\tables\wheat_circos_tissue_peptide_summary_step21.csv
    


    
![png](output_42_1.png)
    


    Figure saved: python_outputs\figures\step21_circos_tissue_peptide_tracks.png
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Tissue</th>
      <th>Source_Tissue</th>
      <th>Chromosome</th>
      <th>Total_projected_peptide_rows</th>
      <th>Sampled_points_plotted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>Chr1A</td>
      <td>1498</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>Chr1B</td>
      <td>1676</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>Chr1D</td>
      <td>1477</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>Chr2A</td>
      <td>1264</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>Chr2B</td>
      <td>1444</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>


# Step 22 — EDA: Circular Confidence-Level Peptide Genome Map

This exploratory analysis generates a Circos-style circular genome map showing peptide evidence by annotation-confidence category across the wheat genome.

Unlike the tissue-ring Circos plot in Step 21, this plot groups peptide evidence into three biologically meaningful classes:

```text
HC projected peptides
LC projected peptides
```

---

## Input files

### Non-redundant annotation-projected peptide table from Step 11

```text
wheat_all_tissues_nonredundant_projected_peptides.csv
```

### Protein-to-gene mapping table from Step 5

```text
wheat_protein_gene_mapping_HC_LC.csv
```

### Parsed GFF3 annotation table from Step 5

```text
wheat_gff3_parsed_features_HC_LC.csv
```

The GFF3-derived table was used to estimate chromosome lengths for the circular genome layout.

---

## Plot design

The circular plot contains:

| Ring | Evidence class |
|---|---|
| Inner ring | LC annotation-projected peptides |
| Outer ring | HC annotation-projected peptides |

Each tick mark represents a sampled peptide genomic start position.

---

## Memory-light plotting strategy

Because the full peptide dataset contains millions of mapped positions, the workflow was designed to run on standard desktop hardware.

The code:

1. Reads the projected peptide table in chunks.
2. Keeps only required columns.
3. Maps protein IDs to HC/LC confidence.
4. Samples peptide positions per chromosome and evidence class.
5. Caps the number of plotted points per chromosome/evidence class.

The full counts and sampled counts are retained in the summary table.

---

## Chromosomes included

The plot includes the 21 assembled wheat chromosomes:

```text
Chr1A–Chr7D
```

`ChrUnknown` was excluded to preserve chromosome-scale interpretability.

---

## Output files

### Figure

```text
step22_circos_confidence_level_peptide_map.png
```

### Summary table

```text
wheat_circos_confidence_level_peptide_summary_step22.csv
```

---

## Purpose

This figure provides a compact genome-wide overview of peptide evidence stratified by annotation confidence.



```python
# ============================================================
# Step 22 — EDA: Circular confidence-level peptide genome map
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict
from pycirclize import Circos

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

projection_combined_file = tables_dir / "wheat_all_tissues_nonredundant_projected_peptides.csv"
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"
gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

figure_out = figures_dir / "step22_circos_confidence_level_peptide_map.png"
summary_out = tables_dir / "wheat_circos_confidence_level_peptide_summary_step22.csv"

# -----------------------------
# 2. Parameters
# -----------------------------
chrom_order = [
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D"
]

chunksize = 100_000
max_points_per_chrom_confidence = 800

brand_colours = {
    "HC": "#3F007E",
    "LC": "#FF3399",
    "lavender": "#E6CDFF"
}

track_ranges = {
    "LC": (80, 85),
    "HC": (89, 94)
}

# -----------------------------
# 3. Helper functions
# -----------------------------
def normalise_chromosome_name(value):
    value = str(value).strip()

    if value.lower() in ["chrunknown", "unknown", "nan"]:
        return "ChrUnknown"

    if value.startswith("Chr"):
        return value

    return "Chr" + value


# -----------------------------
# 4. Estimate chromosome lengths from GFF3 annotation
# -----------------------------
chrom_lengths = {}

for chunk in pd.read_csv(
    gff3_features_file,
    usecols=lambda col: col in ["SeqID", "End"],
    chunksize=chunksize,
    low_memory=False
):

    chunk["SeqID"] = chunk["SeqID"].apply(normalise_chromosome_name)
    chunk["End"] = pd.to_numeric(chunk["End"], errors="coerce")

    chunk = chunk.dropna(subset=["SeqID", "End"])

    for chrom, group in chunk.groupby("SeqID"):
        if chrom in chrom_order:
            max_end = int(group["End"].max())
            chrom_lengths[chrom] = max(max_end, chrom_lengths.get(chrom, 0))

chrom_lengths = {
    chrom: chrom_lengths[chrom]
    for chrom in chrom_order
    if chrom in chrom_lengths
}

print(f"Chromosomes loaded: {len(chrom_lengths)}")

# -----------------------------
# 5. Load ProteinID → HC/LC lookup
# -----------------------------
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    usecols=lambda col: col in [protein_col, confidence_col],
    low_memory=False
)

protein_conf_lookup = (
    protein_mapping
    .dropna(subset=[protein_col, confidence_col])
    .drop_duplicates(subset=[protein_col])
)

# -----------------------------
# 6. Sample projected HC/LC peptide positions
# -----------------------------
confidence_positions = defaultdict(lambda: defaultdict(list))
summary_counts = defaultdict(lambda: defaultdict(int))

projected_needed_cols = [
    "Chromosome",
    "BED_start_0based",
    "ProteinID"
]

for chunk in pd.read_csv(
    projection_combined_file,
    usecols=lambda col: col in projected_needed_cols,
    chunksize=chunksize,
    low_memory=False
):

    chunk = chunk.merge(
        protein_conf_lookup,
        on="ProteinID",
        how="left"
    )

    chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

    chunk = chunk[
        chunk["Chromosome"].isin(chrom_order)
    ].copy()

    chunk["BED_start_0based"] = pd.to_numeric(
        chunk["BED_start_0based"],
        errors="coerce"
    )

    chunk["Annotation_confidence"] = (
        chunk["Annotation_confidence"]
        .astype(str)
        .str.upper()
    )

    chunk = chunk.dropna(
        subset=["Chromosome", "BED_start_0based", "Annotation_confidence"]
    )

    chunk = chunk[
        chunk["Annotation_confidence"].isin(["HC", "LC"])
    ].copy()

    if chunk.empty:
        continue

    for (confidence, chrom), group in chunk.groupby(
        ["Annotation_confidence", "Chromosome"]
    ):

        summary_counts[confidence][chrom] += len(group)

        n_sample = min(80, len(group))

        confidence_positions[confidence][chrom].extend(
            group["BED_start_0based"]
            .sample(n=n_sample, random_state=42)
            .astype(int)
            .tolist()
        )

# Final cap per chromosome/confidence
for confidence in ["HC", "LC"]:
    for chrom in chrom_order:
        positions = confidence_positions[confidence][chrom]

        if len(positions) > max_points_per_chrom_confidence:
            positions = (
                pd.Series(positions)
                .sample(
                    n=max_points_per_chrom_confidence,
                    random_state=42
                )
                .astype(int)
                .tolist()
            )

            confidence_positions[confidence][chrom] = positions

# -----------------------------
# 7. Save summary table
# -----------------------------
summary_records = []

for confidence in ["HC", "LC"]:
    for chrom in chrom_order:
        summary_records.append({
            "Evidence_class": confidence,
            "Chromosome": chrom,
            "Total_peptide_rows_or_loci": summary_counts[confidence].get(chrom, 0),
            "Sampled_points_plotted": len(confidence_positions[confidence][chrom])
        })

summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print(f"Summary saved: {summary_out}")

# -----------------------------
# 8. Build Circos plot
# -----------------------------
def filter_positions_within_chromosome(positions, chrom, chrom_lengths):
    chrom_len = chrom_lengths.get(chrom)

    if chrom_len is None:
        return []

    return [
        int(pos)
        for pos in positions
        if pd.notna(pos) and 0 <= int(pos) <= chrom_len
    ]

circos = Circos(chrom_lengths, space=2)

# Outer chromosome track
for sector in circos.sectors:
    outer_track = sector.add_track((96, 100))
    outer_track.axis(fc="#E6CDFF", ec="#3F007E", lw=0.6)

    sector.text(
        sector.name.replace("Chr", ""),
        r=103,
        size=10
    )

# Confidence rings: LC centre, HC outside
for evidence_class in ["LC", "HC"]:

    r0, r1 = track_ranges[evidence_class]
    colour = brand_colours[evidence_class]

    for sector in circos.sectors:

        track = sector.add_track((r0, r1))
        track.axis(fc="white", ec="lightgrey", lw=0.2)

        chrom = sector.name
        positions = confidence_positions[evidence_class].get(chrom, [])
        
        positions = filter_positions_within_chromosome(
            positions,
            chrom,
            chrom_lengths
        )
        
        if len(positions) == 0:
            continue

        y_values = [0.5] * len(positions)

        track.scatter(
            positions,
            y_values,
            s=14,
            color=colour,
            marker=".",
            linewidths=1.2
        )

# -----------------------------
# 9. Plot and legend
# -----------------------------
fig = circos.plotfig(figsize=(8.5, 8.5))

legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="s",
        color="w",
        label="HC projected peptide",
        markerfacecolor=brand_colours["HC"],
        markersize=9
    ),
    plt.Line2D(
        [0], [0],
        marker="s",
        color="w",
        label="LC projected peptide",
        markerfacecolor=brand_colours["LC"],
        markersize=9
    )
]

fig.legend(
    handles=legend_handles,
    title="Legend",
    loc="upper right",
    bbox_to_anchor=(1.05, 0.92),
    frameon=True,
    facecolor="white",
    edgecolor="black"
)

fig.suptitle(
    "Circular confidence-level peptide genome map",
    fontsize=15,
    fontweight="bold",
    y=0.98
)

plt.savefig(
    figure_out,
    dpi=300,
    bbox_inches="tight",
    pad_inches=0.1,
    facecolor="white"
)

plt.show()

print(f"Figure saved: {figure_out}")
display(summary.head())
```

    Chromosomes loaded: 21
    Summary saved: python_outputs\tables\wheat_circos_confidence_level_peptide_summary_step22.csv
    


    
![png](output_44_1.png)
    


    Figure saved: python_outputs\figures\step22_circos_confidence_level_peptide_map.png
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Evidence_class</th>
      <th>Chromosome</th>
      <th>Total_peptide_rows_or_loci</th>
      <th>Sampled_points_plotted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>Chr1A</td>
      <td>102785</td>
      <td>160</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HC</td>
      <td>Chr1B</td>
      <td>109468</td>
      <td>160</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HC</td>
      <td>Chr1D</td>
      <td>106460</td>
      <td>240</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HC</td>
      <td>Chr2A</td>
      <td>130632</td>
      <td>160</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HC</td>
      <td>Chr2B</td>
      <td>135400</td>
      <td>240</td>
    </tr>
  </tbody>
</table>
</div>


# Step 23 — Combine Python Workflow Summary Tables at Source/Tissue Level

This step integrates all major workflow summary tables generated throughout the proteogenomics pipeline into a single comprehensive tissue-level summary table. The resulting dataset provides a unified overview of peptide identification, protein mapping, genomic projection, and BED export statistics across all analysed tissues and data sources.

---

The workflow begins by defining the input/output directories and loading the FragPipe tissue manifest, which serves as the backbone for the integrated summary structure. Helper functions are then used to safely load summary files only if they exist and to standardise merge keys (`Source` and `Tissue`) across datasets. Combined “ALL” rows are removed to retain only tissue-level summaries suitable for downstream comparative analyses.

Summary outputs from previous workflow steps are then loaded, including:

- **Step 6:** FragPipe annotation summaries  
- **Step 7:** Peptide–protein evidence summaries  
- **Step 8:** Peptide–protein–gene mapping summaries  
- **Step 9:** Peptide genomic projection summaries  
- **Step 11:** BED export summaries  
- **Step 13:** Tissue-level proteogenomic summaries  

To minimise redundancy and avoid excessively wide tables, only biologically informative and technically relevant columns are retained from each step. Step 6 data are pivoted to separate peptide and protein statistics into distinct columns while preserving one row per source/tissue combination.

---

All summary tables are sequentially merged into a single integrated dataframe using `Source` and `Tissue` as common merge keys. The final combined summary contains metrics spanning the entire workflow, including:

- total peptide/protein identifications,
- contaminant filtering statistics,
- peptide-to-protein mapping performance,
- gene model coverage,
- peptide genomic projection success,
- BED track export statistics,
- chromosome coverage,
- exon-spanning peptide evidence,
- HC/LC gene model representation.

---

The completed integrated summary table is exported as:

`wheat_complete_python_workflow_summary_step23.csv`

This consolidated table provides a high-level overview of the entire computational proteogenomics workflow and serves as a central resource for downstream exploratory data analysis, comparative tissue assessments, manuscript reporting, and reproducibility documentation.


```python
# ============================================================
# Step 23. Combine Python workflow summary tables at source/tissue level
# ============================================================

import pandas as pd
from pathlib import Path
import re

# -----------------------------
# 1. Input / output paths
# -----------------------------
tables_dir = Path("python_outputs/tables")

tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

complete_python_summary_out = tables_dir / "wheat_complete_python_workflow_summary_step23.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

# -----------------------------
# 2. Helper functions
# -----------------------------

def load_summary_if_exists(path):
    if Path(path).exists():
        return pd.read_csv(path, low_memory=False)
    print(f"Summary not found, skipped: {path}")
    return None


def standardise_tissue_key(data):
    """
    Keep only tissue-level rows and standardise merge keys where possible.
    """
    if data is None:
        return None

    data = data.copy()

    required_keys = ["Source", "Tissue"]
    if not all(col in data.columns for col in required_keys):
        return None

    # Remove combined ALL rows for tissue-level integrated summary
    data = data[
        ~((data["Source"].astype(str) == "ALL") | (data["Tissue"].astype(str) == "ALL"))
    ].copy()

    return data


# -----------------------------
# 3. Combine all summary outputs
# -----------------------------

summary_files = {
    "step6": tables_dir / "wheat_fragpipe_annotation_summary_step6.csv",
    "step7": tables_dir / "wheat_fragpipe_peptide_protein_evidence_summary_step7.csv",
    "step8": tables_dir / "wheat_peptide_protein_gene_mapping_summary_step8.csv",
    "step9": tables_dir / "wheat_peptide_genome_projection_summary_step9.csv",
    "step11": tables_dir / "wheat_bed_export_summary_step11.csv",
    "step13": tables_dir / "wheat_tissue_level_summary_step13.csv"
}

summaries = {
    step: standardise_tissue_key(load_summary_if_exists(path))
    for step, path in summary_files.items()
}

# Start from manifest as the backbone
complete_summary = manifest[[
    "Source",
    "Species",
    "Tissue-Raw-Code",
    "Batch"
]].copy()

complete_summary = complete_summary.rename(columns={"Tissue-Raw-Code": "Tissue"})

# Select useful columns from each step to avoid very wide duplicated tables
merge_specs = {
    "step6": [
        "Source", "Tissue", "FragPipe_result", "Total_rows",
        "Contaminant_count", "Non_contaminant_count"
    ],
    "step7": [
        "Source", "Tissue", "Non_contaminant_peptide_protein_pairs",
        "Unique_peptides", "Unique_proteins",
        "Peptides_mapping_to_multiple_proteins",
        "Proteins_supported_by_one_peptide",
        "Proteins_supported_by_two_or_more_peptides"
    ],
    "step8": [
        "Source", "Tissue", "Peptide_protein_pairs",
        "Mapped_peptide_protein_pairs",
        "Unmapped_peptide_protein_pairs",
        "Mapping_rate_percent",
        "Unique_gene_models",
        "Unique_transcripts"
    ],
    "step9": [
        "Source", "Tissue", "Peptide_protein_gene_rows",
        "Projected_rows", "Unprojected_rows",
        "Projection_rate_percent",
        "Unique_projected_peptides",
        "Unique_projected_proteins",
        "Unique_projected_gene_models",
        "Peptides_crossing_CDS_blocks"
    ],
    "step11": [
        "Source", "Tissue", "Projection_file",
        "BED_rows", "Unique_BED_peptides",
        "Unique_BED_proteins",
        "Unique_BED_gene_models",
        "Multi_block_peptides",
        "BED_labels_with_introns"
    ],
    "step13": [
        "Source", "Tissue", "Projected_peptide_rows",
        "Unique_peptides",	"Unique_proteins_isoforms",
        "Unique_gene_models",	"Unique_HC_gene_models",
        "Unique_LC_gene_models",	"Percent_total_gene_models_detected",
        "Percent_HC_gene_models_detected",	"Percent_LC_gene_models_detected",
        "Unique_chromosomes",	"Multi_block_peptide_rows",
        "Proteins_supported_by_one_peptide",	"Proteins_supported_by_two_or_more_peptides",
        "Genes_supported_by_one_peptide",	"Genes_supported_by_two_or_more_peptides"
    ]
}

for step, cols in merge_specs.items():

    data = summaries.get(step)

    if data is None:
        continue

    available_cols = [col for col in cols if col in data.columns]

    if "Source" not in available_cols or "Tissue" not in available_cols:
        continue

    data = data[available_cols].copy()

    # Step 6 has peptide and protein rows, so pivot to avoid duplicate tissue rows
    if step == "step6" and "FragPipe_result" in data.columns:
        data = data.pivot_table(
            index=["Source", "Tissue"],
            columns="FragPipe_result",
            values=["Total_rows", "Contaminant_count", "Non_contaminant_count"],
            aggfunc="first"
        )

        data.columns = [
            f"step6_{metric}_{result}"
            for metric, result in data.columns
        ]

        data = data.reset_index()

    else:
        # Avoid duplicated column names after merging
        rename_cols = {
            col: f"{step}_{col}"
            for col in data.columns
            if col not in ["Source", "Tissue"]
        }

        data = data.rename(columns=rename_cols)

        # Ensure one row per Source/Tissue
        data = data.drop_duplicates(subset=["Source", "Tissue"])

    complete_summary = complete_summary.merge(
        data,
        on=["Source", "Tissue"],
        how="left"
    )

complete_summary.to_csv(complete_python_summary_out, index=False)

print(f"\nComplete Python workflow summary saved: {complete_python_summary_out}")
display(complete_summary)
```

    
    Complete Python workflow summary saved: python_outputs\tables\wheat_complete_python_workflow_summary_step23.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>step6_Contaminant_count_peptide</th>
      <th>step6_Contaminant_count_protein</th>
      <th>step6_Non_contaminant_count_peptide</th>
      <th>step6_Non_contaminant_count_protein</th>
      <th>step6_Total_rows_peptide</th>
      <th>step6_Total_rows_protein</th>
      <th>...</th>
      <th>step13_Unique_LC_gene_models</th>
      <th>step13_Percent_total_gene_models_detected</th>
      <th>step13_Percent_HC_gene_models_detected</th>
      <th>step13_Percent_LC_gene_models_detected</th>
      <th>step13_Unique_chromosomes</th>
      <th>step13_Multi_block_peptide_rows</th>
      <th>step13_Proteins_supported_by_one_peptide</th>
      <th>step13_Proteins_supported_by_two_or_more_peptides</th>
      <th>step13_Genes_supported_by_one_peptide</th>
      <th>step13_Genes_supported_by_two_or_more_peptides</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>14</td>
      <td>6</td>
      <td>9329</td>
      <td>7068</td>
      <td>9343.0</td>
      <td>7074.0</td>
      <td>...</td>
      <td>5734</td>
      <td>5.5868</td>
      <td>8.5761</td>
      <td>3.5874</td>
      <td>22</td>
      <td>3291</td>
      <td>14132</td>
      <td>3346</td>
      <td>12085</td>
      <td>2818</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>409</td>
      <td>79</td>
      <td>582775</td>
      <td>137762</td>
      <td>583184.0</td>
      <td>137841.0</td>
      <td>...</td>
      <td>114284</td>
      <td>79.4018</td>
      <td>91.2154</td>
      <td>71.4999</td>
      <td>22</td>
      <td>228372</td>
      <td>59391</td>
      <td>180070</td>
      <td>57302</td>
      <td>154504</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>483</td>
      <td>94</td>
      <td>595954</td>
      <td>141678</td>
      <td>596437.0</td>
      <td>141772.0</td>
      <td>...</td>
      <td>116759</td>
      <td>80.6135</td>
      <td>91.9234</td>
      <td>73.0483</td>
      <td>22</td>
      <td>235642</td>
      <td>57470</td>
      <td>185343</td>
      <td>55363</td>
      <td>159675</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>342</td>
      <td>67</td>
      <td>333058</td>
      <td>105903</td>
      <td>333400.0</td>
      <td>105970.0</td>
      <td>...</td>
      <td>89887</td>
      <td>67.4349</td>
      <td>84.1770</td>
      <td>56.2363</td>
      <td>22</td>
      <td>118195</td>
      <td>68189</td>
      <td>137827</td>
      <td>64784</td>
      <td>115100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>105</td>
      <td>10</td>
      <td>34098</td>
      <td>10085</td>
      <td>34203.0</td>
      <td>10095.0</td>
      <td>...</td>
      <td>7959</td>
      <td>11.0155</td>
      <td>20.0395</td>
      <td>4.9794</td>
      <td>22</td>
      <td>27776</td>
      <td>19936</td>
      <td>16890</td>
      <td>16541</td>
      <td>12843</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>1</td>
      <td>1</td>
      <td>3643</td>
      <td>2827</td>
      <td>3644.0</td>
      <td>2828.0</td>
      <td>...</td>
      <td>1941</td>
      <td>2.7595</td>
      <td>5.0695</td>
      <td>1.2144</td>
      <td>22</td>
      <td>2728</td>
      <td>7285</td>
      <td>1923</td>
      <td>5897</td>
      <td>1464</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>101</td>
      <td>11</td>
      <td>41025</td>
      <td>12205</td>
      <td>41126.0</td>
      <td>12216.0</td>
      <td>...</td>
      <td>10047</td>
      <td>13.8226</td>
      <td>25.0903</td>
      <td>6.2857</td>
      <td>22</td>
      <td>31344</td>
      <td>23572</td>
      <td>22924</td>
      <td>19818</td>
      <td>17054</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>1</td>
      <td>1</td>
      <td>2867</td>
      <td>2402</td>
      <td>2868.0</td>
      <td>2403.0</td>
      <td>...</td>
      <td>1644</td>
      <td>2.1960</td>
      <td>3.9415</td>
      <td>1.0285</td>
      <td>22</td>
      <td>1411</td>
      <td>6285</td>
      <td>935</td>
      <td>5152</td>
      <td>706</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>93</td>
      <td>11</td>
      <td>20081</td>
      <td>7416</td>
      <td>20174.0</td>
      <td>7427.0</td>
      <td>...</td>
      <td>5808</td>
      <td>8.2016</td>
      <td>15.0308</td>
      <td>3.6337</td>
      <td>22</td>
      <td>14269</td>
      <td>15841</td>
      <td>11613</td>
      <td>13128</td>
      <td>8750</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>35</td>
      <td>8</td>
      <td>28648</td>
      <td>9604</td>
      <td>28683.0</td>
      <td>9612.0</td>
      <td>...</td>
      <td>8169</td>
      <td>10.7681</td>
      <td>19.2257</td>
      <td>5.1108</td>
      <td>22</td>
      <td>22131</td>
      <td>19968</td>
      <td>15572</td>
      <td>16662</td>
      <td>12062</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>33</td>
      <td>9</td>
      <td>26196</td>
      <td>9812</td>
      <td>26229.0</td>
      <td>9821.0</td>
      <td>...</td>
      <td>8019</td>
      <td>10.7504</td>
      <td>19.3221</td>
      <td>5.0170</td>
      <td>22</td>
      <td>17478</td>
      <td>20510</td>
      <td>15022</td>
      <td>17259</td>
      <td>11418</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>30</td>
      <td>10</td>
      <td>35960</td>
      <td>12326</td>
      <td>35990.0</td>
      <td>12336.0</td>
      <td>...</td>
      <td>9929</td>
      <td>13.8398</td>
      <td>25.2437</td>
      <td>6.2119</td>
      <td>22</td>
      <td>27658</td>
      <td>24690</td>
      <td>22386</td>
      <td>20769</td>
      <td>16149</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>89</td>
      <td>11</td>
      <td>27463</td>
      <td>11089</td>
      <td>27552.0</td>
      <td>11100.0</td>
      <td>...</td>
      <td>8339</td>
      <td>12.2248</td>
      <td>22.7014</td>
      <td>5.2172</td>
      <td>22</td>
      <td>18650</td>
      <td>23251</td>
      <td>17778</td>
      <td>19474</td>
      <td>13136</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>61</td>
      <td>9</td>
      <td>23990</td>
      <td>10185</td>
      <td>24051.0</td>
      <td>10194.0</td>
      <td>...</td>
      <td>8219</td>
      <td>11.0346</td>
      <td>19.8440</td>
      <td>5.1421</td>
      <td>22</td>
      <td>14734</td>
      <td>21674</td>
      <td>14961</td>
      <td>18228</td>
      <td>11207</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>38</td>
      <td>9</td>
      <td>24636</td>
      <td>10380</td>
      <td>24674.0</td>
      <td>10389.0</td>
      <td>...</td>
      <td>8040</td>
      <td>10.5293</td>
      <td>18.7506</td>
      <td>5.0301</td>
      <td>22</td>
      <td>14886</td>
      <td>21235</td>
      <td>13639</td>
      <td>17740</td>
      <td>10347</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>101</td>
      <td>13</td>
      <td>29840</td>
      <td>9626</td>
      <td>29941.0</td>
      <td>9639.0</td>
      <td>...</td>
      <td>7910</td>
      <td>11.3862</td>
      <td>21.0103</td>
      <td>4.9488</td>
      <td>22</td>
      <td>19448</td>
      <td>19758</td>
      <td>18196</td>
      <td>16433</td>
      <td>13940</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>40</td>
      <td>12</td>
      <td>11354</td>
      <td>8022</td>
      <td>11394.0</td>
      <td>8034.0</td>
      <td>...</td>
      <td>6907</td>
      <td>7.9703</td>
      <td>13.4257</td>
      <td>4.3213</td>
      <td>22</td>
      <td>4572</td>
      <td>18836</td>
      <td>6860</td>
      <td>15872</td>
      <td>5389</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>68</td>
      <td>10</td>
      <td>23373</td>
      <td>7532</td>
      <td>23441.0</td>
      <td>7542.0</td>
      <td>...</td>
      <td>7360</td>
      <td>9.8361</td>
      <td>17.6572</td>
      <td>4.6047</td>
      <td>22</td>
      <td>15227</td>
      <td>17531</td>
      <td>15089</td>
      <td>14534</td>
      <td>11704</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>54</td>
      <td>8</td>
      <td>29788</td>
      <td>9948</td>
      <td>29842.0</td>
      <td>9956.0</td>
      <td>...</td>
      <td>8594</td>
      <td>11.4132</td>
      <td>20.4379</td>
      <td>5.3767</td>
      <td>22</td>
      <td>21753</td>
      <td>20855</td>
      <td>17072</td>
      <td>17320</td>
      <td>13125</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>51</td>
      <td>9</td>
      <td>21457</td>
      <td>10521</td>
      <td>21508.0</td>
      <td>10530.0</td>
      <td>...</td>
      <td>10088</td>
      <td>11.2348</td>
      <td>18.5953</td>
      <td>6.3114</td>
      <td>22</td>
      <td>12765</td>
      <td>23369</td>
      <td>13173</td>
      <td>19696</td>
      <td>10273</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>70</td>
      <td>12</td>
      <td>34124</td>
      <td>10560</td>
      <td>34194.0</td>
      <td>10572.0</td>
      <td>...</td>
      <td>8776</td>
      <td>12.6470</td>
      <td>23.3459</td>
      <td>5.4906</td>
      <td>22</td>
      <td>22888</td>
      <td>21374</td>
      <td>20982</td>
      <td>17945</td>
      <td>15791</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>67</td>
      <td>8</td>
      <td>21707</td>
      <td>6934</td>
      <td>21774.0</td>
      <td>6942.0</td>
      <td>...</td>
      <td>5376</td>
      <td>8.1645</td>
      <td>15.3422</td>
      <td>3.3634</td>
      <td>22</td>
      <td>20681</td>
      <td>14019</td>
      <td>13561</td>
      <td>11405</td>
      <td>10374</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>116</td>
      <td>13</td>
      <td>28332</td>
      <td>9453</td>
      <td>28448.0</td>
      <td>9466.0</td>
      <td>...</td>
      <td>7016</td>
      <td>9.7319</td>
      <td>17.7189</td>
      <td>4.3894</td>
      <td>22</td>
      <td>20964</td>
      <td>18598</td>
      <td>14069</td>
      <td>15393</td>
      <td>10567</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>91</td>
      <td>9</td>
      <td>13502</td>
      <td>4667</td>
      <td>13593.0</td>
      <td>4676.0</td>
      <td>...</td>
      <td>3880</td>
      <td>6.0198</td>
      <td>11.3905</td>
      <td>2.4275</td>
      <td>22</td>
      <td>9490</td>
      <td>10805</td>
      <td>9126</td>
      <td>8883</td>
      <td>7175</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>68</td>
      <td>7</td>
      <td>31145</td>
      <td>9710</td>
      <td>31213.0</td>
      <td>9717.0</td>
      <td>...</td>
      <td>8095</td>
      <td>11.0773</td>
      <td>20.0666</td>
      <td>5.0645</td>
      <td>22</td>
      <td>24784</td>
      <td>19588</td>
      <td>17616</td>
      <td>16297</td>
      <td>13252</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>61</td>
      <td>11</td>
      <td>39643</td>
      <td>11741</td>
      <td>39704.0</td>
      <td>11752.0</td>
      <td>...</td>
      <td>8143</td>
      <td>12.6953</td>
      <td>24.0586</td>
      <td>5.0945</td>
      <td>22</td>
      <td>32499</td>
      <td>22390</td>
      <td>20575</td>
      <td>18724</td>
      <td>15141</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>40</td>
      <td>11</td>
      <td>21350</td>
      <td>12203</td>
      <td>21390.0</td>
      <td>12214.0</td>
      <td>...</td>
      <td>9390</td>
      <td>11.8286</td>
      <td>20.7297</td>
      <td>5.8747</td>
      <td>22</td>
      <td>10898</td>
      <td>26297</td>
      <td>12859</td>
      <td>21852</td>
      <td>9701</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>45</td>
      <td>11</td>
      <td>21284</td>
      <td>10298</td>
      <td>21329.0</td>
      <td>10309.0</td>
      <td>...</td>
      <td>6804</td>
      <td>9.5628</td>
      <td>17.4954</td>
      <td>4.2568</td>
      <td>22</td>
      <td>15547</td>
      <td>20041</td>
      <td>12005</td>
      <td>16472</td>
      <td>9037</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>47</td>
      <td>8</td>
      <td>38634</td>
      <td>10336</td>
      <td>38681.0</td>
      <td>10344.0</td>
      <td>...</td>
      <td>7219</td>
      <td>11.5977</td>
      <td>22.1842</td>
      <td>4.5164</td>
      <td>22</td>
      <td>35031</td>
      <td>18861</td>
      <td>20913</td>
      <td>15675</td>
      <td>15262</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>96</td>
      <td>9</td>
      <td>20815</td>
      <td>7568</td>
      <td>20911.0</td>
      <td>7577.0</td>
      <td>...</td>
      <td>5594</td>
      <td>8.9251</td>
      <td>17.0361</td>
      <td>3.4998</td>
      <td>22</td>
      <td>14833</td>
      <td>16692</td>
      <td>13934</td>
      <td>13630</td>
      <td>10178</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>44</td>
      <td>8</td>
      <td>36370</td>
      <td>10940</td>
      <td>36414.0</td>
      <td>10948.0</td>
      <td>...</td>
      <td>7499</td>
      <td>11.6314</td>
      <td>22.0065</td>
      <td>4.6916</td>
      <td>22</td>
      <td>33193</td>
      <td>19851</td>
      <td>20356</td>
      <td>16433</td>
      <td>14594</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>51</td>
      <td>10</td>
      <td>14338</td>
      <td>8974</td>
      <td>14389.0</td>
      <td>8984.0</td>
      <td>...</td>
      <td>7034</td>
      <td>8.8753</td>
      <td>15.5648</td>
      <td>4.4007</td>
      <td>22</td>
      <td>6949</td>
      <td>20194</td>
      <td>9216</td>
      <td>16775</td>
      <td>6900</td>
    </tr>
  </tbody>
</table>
<p>32 rows × 52 columns</p>
</div>


# Step 25 — Sanity Checks for Annotation-Guided Peptide Genome Projections

This step performs final quality-control checks on the projected peptide genome coordinates before public upload to Apollo/JBrowse.

The aim is to verify that the annotation-guided peptide projections generated in Step 9 are internally consistent and suitable for genome-browser visualisation.

---

Three independent sanity checks are performed:

1. **BED geometry check**  
   Confirms that BED coordinates are valid, that start coordinates are smaller than end coordinates, and that BED block sizes and block starts are consistent with each peptide genomic interval.

2. **Chromosome and strand check**  
   Confirms that projected peptides are assigned only to expected wheat chromosomes and valid strand values (`+` or `-`).

3. **Protein-coordinate consistency check**  
   Confirms that each peptide projection has coherent amino-acid coordinates, including matching peptide length and valid protein coordinate intervals.

For each projected peptide row, the workflow records pass/fail flags for each check and assigns an overall sanity-check status.

---

The outputs include:

- a full sanity-check table for all projected peptide rows,
- a failed-row diagnostic table,
- a tissue-level sanity-check summary table.

---

These checks provide an additional safeguard before sharing the BED tracks as a public genome-browser resource.


```python
# ============================================================
# Step 25 — Sanity checks for annotation-guided peptide genome projections (takes 30 min)
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

sanity_full_out = tables_dir / "wheat_projection_sanity_checks_full_step25.csv"
sanity_failed_out = tables_dir / "wheat_projection_sanity_checks_failed_rows_step25.csv"
sanity_summary_out = tables_dir / "wheat_projection_sanity_checks_summary_step25.csv"

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")

# -----------------------------
# 2. Expected wheat chromosomes and valid strands
# -----------------------------
valid_chromosomes = {
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D"
}

valid_strands = {"+", "-"}

# -----------------------------
# 3. Helper functions
# -----------------------------
def parse_bed_list(value):
    """
    Convert comma-separated BED block size/start strings into integer lists.
    Handles empty or missing values.
    """
    if pd.isna(value):
        return []

    value = str(value).strip().strip(",")

    if value == "":
        return []

    try:
        return [int(x) for x in value.split(",") if str(x).strip() != ""]
    except ValueError:
        return []


def check_bed_geometry(row):
    """
    Check BED interval and BED12-style block geometry.
    """
    try:
        bed_start = int(row["BED_start_0based"])
        bed_end = int(row["BED_end_0based_exclusive"])
        block_count = int(row["BED_block_count"])
    except Exception:
        return False

    if bed_start < 0:
        return False

    if bed_end <= bed_start:
        return False

    block_sizes = parse_bed_list(row["BED_block_sizes"])
    block_starts = parse_bed_list(row["BED_block_starts"])

    if block_count <= 0:
        return False

    if len(block_sizes) != block_count:
        return False

    if len(block_starts) != block_count:
        return False

    if any(size <= 0 for size in block_sizes):
        return False

    if any(start < 0 for start in block_starts):
        return False

    interval_length = bed_end - bed_start

    # Every block must fit inside the BED interval
    for block_start, block_size in zip(block_starts, block_sizes):
        if block_start + block_size > interval_length:
            return False

    return True


def check_block_nt_length(row):
    """
    Check that the sum of BED block nucleotide lengths matches peptide length × 3.
    """
    try:
        peptide_len = int(row["Peptide_length_AA"])
    except Exception:
        return False

    block_sizes = parse_bed_list(row["BED_block_sizes"])

    if len(block_sizes) == 0:
        return False

    return sum(block_sizes) == peptide_len * 3


def check_chromosome_and_strand(row):
    """
    Check valid chromosome and strand assignment.
    """
    chrom = str(row["Chromosome"])
    strand = str(row["Strand"])

    return chrom in valid_chromosomes and strand in valid_strands


def check_protein_coordinates(row):
    """
    Check that amino-acid coordinates are internally consistent with peptide length.
    """
    try:
        aa_start = int(row["AA_start"])
        aa_end = int(row["AA_end"])
        peptide_len = int(row["Peptide_length_AA"])
    except Exception:
        return False

    if aa_start <= 0:
        return False

    if aa_end < aa_start:
        return False

    if (aa_end - aa_start + 1) != peptide_len:
        return False

    peptide = str(row["Peptide"])

    if len(peptide) != peptide_len:
        return False

    return True


# -----------------------------
# 4. Run sanity checks across all projected peptide tables
# -----------------------------
all_checked = []
summary_records = []

for _, manifest_row in manifest.iterrows():

    source = manifest_row["Source"]
    species = manifest_row["Species"]
    tissue = manifest_row["Tissue-Raw-Code"]
    batch = manifest_row["Batch"]

    projection_filename = manifest_row["FragPipe-Output-Peptide"].replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )

    projection_path = tables_dir / projection_filename

    if not projection_path.exists():
        print(f"Projection file not found, skipped: {projection_path}")
        continue

    data = pd.read_csv(projection_path, low_memory=False)

    # Keep only successfully projected rows
    projected = data[data["Projection_status"] == "projected"].copy()

    if projected.empty:
        print(f"No projected rows found in: {projection_path}")
        continue

    projected["Source"] = source
    projected["Species"] = species
    projected["Tissue"] = tissue
    projected["Batch"] = batch
    projected["Projection_file"] = projection_filename

    # Sanity checks
    projected["Check_BED_geometry"] = projected.apply(check_bed_geometry, axis=1)
    projected["Check_block_nt_length"] = projected.apply(check_block_nt_length, axis=1)
    projected["Check_chromosome_and_strand"] = projected.apply(check_chromosome_and_strand, axis=1)
    projected["Check_protein_coordinates"] = projected.apply(check_protein_coordinates, axis=1)

    check_cols = [
        "Check_BED_geometry",
        "Check_block_nt_length",
        "Check_chromosome_and_strand",
        "Check_protein_coordinates"
    ]

    projected["All_sanity_checks_passed"] = projected[check_cols].all(axis=1)

    projected["Sanity_check_status"] = projected["All_sanity_checks_passed"].map({
        True: "passed",
        False: "failed"
    })

    failed = projected[~projected["All_sanity_checks_passed"]]

    summary_records.append({
        "Source": source,
        "Species": species,
        "Tissue": tissue,
        "Batch": batch,
        "Projection_file": projection_filename,
        "Projected_rows_checked": len(projected),
        "Rows_passing_all_sanity_checks": int(projected["All_sanity_checks_passed"].sum()),
        "Rows_failing_any_sanity_check": int((~projected["All_sanity_checks_passed"]).sum()),
        "Percent_passing_all_sanity_checks": round(
            projected["All_sanity_checks_passed"].mean() * 100, 4
        ),
        "BED_geometry_failures": int((~projected["Check_BED_geometry"]).sum()),
        "Block_nt_length_failures": int((~projected["Check_block_nt_length"]).sum()),
        "Chromosome_strand_failures": int((~projected["Check_chromosome_and_strand"]).sum()),
        "Protein_coordinate_failures": int((~projected["Check_protein_coordinates"]).sum())
    })

    print(
        f"{source} | {tissue}: "
        f"{projected['All_sanity_checks_passed'].sum():,} / {len(projected):,} passed"
    )

    all_checked.append(projected)

# -----------------------------
# 5. Combine and export outputs
# -----------------------------
if len(all_checked) == 0:
    raise ValueError("No projected peptide rows were available for sanity checking.")

sanity_full = pd.concat(all_checked, ignore_index=True)
sanity_summary = pd.DataFrame(summary_records)

sanity_failed = sanity_full[
    sanity_full["Sanity_check_status"] == "failed"
].copy()

sanity_full.to_csv(sanity_full_out, index=False)
sanity_failed.to_csv(sanity_failed_out, index=False)
sanity_summary.to_csv(sanity_summary_out, index=False)

# -----------------------------
# 6. Overall summary
# -----------------------------
overall_checked = len(sanity_full)
overall_passed = int(sanity_full["All_sanity_checks_passed"].sum())
overall_failed = overall_checked - overall_passed
overall_pass_percent = round((overall_passed / overall_checked) * 100, 4)

print("\n===== STEP 25 SANITY CHECK SUMMARY =====")
print(f"Projected rows checked: {overall_checked:,}")
print(f"Rows passing all sanity checks: {overall_passed:,}")
print(f"Rows failing at least one sanity check: {overall_failed:,}")
print(f"Overall pass rate: {overall_pass_percent}%")

print(f"\nFull sanity-check table saved: {sanity_full_out}")
print(f"Failed-row diagnostic table saved: {sanity_failed_out}")
print(f"Tissue-level sanity summary saved: {sanity_summary_out}")

display(sanity_summary)
display(sanity_failed.head(20))
```

    MSV000090572 | stored_grain: 29,836 / 30,314 passed
    PXD050500 | coleoptile: 1,832,405 / 1,850,136 passed
    PXD050500 | node: 1,868,501 / 1,886,922 passed
    PXD050500 | radicle: 1,052,392 / 1,062,508 passed
    PXD004720 | anther: 162,834 / 164,365 passed
    PXD004720 | boot: 13,114 / 13,227 passed
    PXD004720 | coleoptile: 202,433 / 204,476 passed
    PXD004720 | embryo: 8,769 / 8,852 passed
    PXD004720 | endosperm: 101,946 / 102,830 passed
    PXD004720 | glume: 143,464 / 145,133 passed
    PXD004720 | grain-zadoks-70: 125,070 / 126,195 passed
    PXD004720 | grain-zadoks-71: 178,286 / 179,725 passed
    PXD004720 | grain-zadoks-75: 131,666 / 132,701 passed
    PXD004720 | grain-zadoks-83: 112,128 / 113,203 passed
    PXD004720 | grain-zadoks-87: 110,874 / 111,792 passed
    PXD004720 | leaf-flag-mature: 144,063 / 145,632 passed
    PXD004720 | leaf-flag-senescing: 45,551 / 46,200 passed
    PXD004720 | leaf-flag-young: 119,463 / 120,821 passed
    PXD004720 | lemma: 146,124 / 147,618 passed
    PXD004720 | node: 98,604 / 99,823 passed
    PXD004720 | node_secretion: 167,975 / 169,675 passed
    PXD004720 | palea: 115,679 / 116,936 passed
    PXD004720 | pericarp: 129,960 / 131,215 passed
    PXD004720 | pollen: 73,946 / 74,698 passed
    PXD004720 | rachilla: 158,608 / 160,204 passed
    PXD004720 | radicle: 193,172 / 194,694 passed
    PXD004720 | root-mature: 96,110 / 97,188 passed
    PXD004720 | root-secretion: 99,670 / 100,639 passed
    PXD004720 | root-tip: 190,638 / 191,943 passed
    PXD004720 | root-vasculature: 110,808 / 111,831 passed
    PXD004720 | spike-immature: 187,160 / 188,826 passed
    PXD004720 | stem: 60,162 / 60,734 passed
    
    ===== STEP 25 SANITY CHECK SUMMARY =====
    Projected rows checked: 8,291,056
    Rows passing all sanity checks: 8,211,411
    Rows failing at least one sanity check: 79,645
    Overall pass rate: 99.0394%
    
    Full sanity-check table saved: python_outputs\tables\wheat_projection_sanity_checks_full_step25.csv
    Failed-row diagnostic table saved: python_outputs\tables\wheat_projection_sanity_checks_failed_rows_step25.csv
    Tissue-level sanity summary saved: python_outputs\tables\wheat_projection_sanity_checks_summary_step25.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Projection_file</th>
      <th>Projected_rows_checked</th>
      <th>Rows_passing_all_sanity_checks</th>
      <th>Rows_failing_any_sanity_check</th>
      <th>Percent_passing_all_sanity_checks</th>
      <th>BED_geometry_failures</th>
      <th>Block_nt_length_failures</th>
      <th>Chromosome_strand_failures</th>
      <th>Protein_coordinate_failures</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>30314</td>
      <td>29836</td>
      <td>478</td>
      <td>98.4232</td>
      <td>0</td>
      <td>0</td>
      <td>478</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>1850136</td>
      <td>1832405</td>
      <td>17731</td>
      <td>99.0416</td>
      <td>0</td>
      <td>0</td>
      <td>17731</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>1886922</td>
      <td>1868501</td>
      <td>18421</td>
      <td>99.0238</td>
      <td>0</td>
      <td>0</td>
      <td>18421</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>1062508</td>
      <td>1052392</td>
      <td>10116</td>
      <td>99.0479</td>
      <td>0</td>
      <td>0</td>
      <td>10116</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
      <td>164365</td>
      <td>162834</td>
      <td>1531</td>
      <td>99.0685</td>
      <td>0</td>
      <td>0</td>
      <td>1531</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
      <td>13227</td>
      <td>13114</td>
      <td>113</td>
      <td>99.1457</td>
      <td>0</td>
      <td>0</td>
      <td>113</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
      <td>204476</td>
      <td>202433</td>
      <td>2043</td>
      <td>99.0009</td>
      <td>0</td>
      <td>0</td>
      <td>2043</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
      <td>8852</td>
      <td>8769</td>
      <td>83</td>
      <td>99.0624</td>
      <td>0</td>
      <td>0</td>
      <td>83</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
      <td>102830</td>
      <td>101946</td>
      <td>884</td>
      <td>99.1403</td>
      <td>0</td>
      <td>0</td>
      <td>884</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
      <td>145133</td>
      <td>143464</td>
      <td>1669</td>
      <td>98.8500</td>
      <td>0</td>
      <td>0</td>
      <td>1669</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>126195</td>
      <td>125070</td>
      <td>1125</td>
      <td>99.1085</td>
      <td>0</td>
      <td>0</td>
      <td>1125</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>179725</td>
      <td>178286</td>
      <td>1439</td>
      <td>99.1993</td>
      <td>0</td>
      <td>0</td>
      <td>1439</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>132701</td>
      <td>131666</td>
      <td>1035</td>
      <td>99.2201</td>
      <td>0</td>
      <td>0</td>
      <td>1035</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>113203</td>
      <td>112128</td>
      <td>1075</td>
      <td>99.0504</td>
      <td>0</td>
      <td>0</td>
      <td>1075</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>111792</td>
      <td>110874</td>
      <td>918</td>
      <td>99.1788</td>
      <td>0</td>
      <td>0</td>
      <td>918</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>145632</td>
      <td>144063</td>
      <td>1569</td>
      <td>98.9226</td>
      <td>0</td>
      <td>0</td>
      <td>1569</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>46200</td>
      <td>45551</td>
      <td>649</td>
      <td>98.5952</td>
      <td>0</td>
      <td>0</td>
      <td>649</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>120821</td>
      <td>119463</td>
      <td>1358</td>
      <td>98.8760</td>
      <td>0</td>
      <td>0</td>
      <td>1358</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
      <td>147618</td>
      <td>146124</td>
      <td>1494</td>
      <td>98.9879</td>
      <td>0</td>
      <td>0</td>
      <td>1494</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
      <td>99823</td>
      <td>98604</td>
      <td>1219</td>
      <td>98.7788</td>
      <td>0</td>
      <td>0</td>
      <td>1219</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>169675</td>
      <td>167975</td>
      <td>1700</td>
      <td>98.9981</td>
      <td>0</td>
      <td>0</td>
      <td>1700</td>
      <td>0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
      <td>116936</td>
      <td>115679</td>
      <td>1257</td>
      <td>98.9251</td>
      <td>0</td>
      <td>0</td>
      <td>1257</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
      <td>131215</td>
      <td>129960</td>
      <td>1255</td>
      <td>99.0436</td>
      <td>0</td>
      <td>0</td>
      <td>1255</td>
      <td>0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
      <td>74698</td>
      <td>73946</td>
      <td>752</td>
      <td>98.9933</td>
      <td>0</td>
      <td>0</td>
      <td>752</td>
      <td>0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_gen...</td>
      <td>160204</td>
      <td>158608</td>
      <td>1596</td>
      <td>99.0038</td>
      <td>0</td>
      <td>0</td>
      <td>1596</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_geno...</td>
      <td>194694</td>
      <td>193172</td>
      <td>1522</td>
      <td>99.2183</td>
      <td>0</td>
      <td>0</td>
      <td>1522</td>
      <td>0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>97188</td>
      <td>96110</td>
      <td>1078</td>
      <td>98.8908</td>
      <td>0</td>
      <td>0</td>
      <td>1078</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>100639</td>
      <td>99670</td>
      <td>969</td>
      <td>99.0372</td>
      <td>0</td>
      <td>0</td>
      <td>969</td>
      <td>0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_gen...</td>
      <td>191943</td>
      <td>190638</td>
      <td>1305</td>
      <td>99.3201</td>
      <td>0</td>
      <td>0</td>
      <td>1305</td>
      <td>0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>111831</td>
      <td>110808</td>
      <td>1023</td>
      <td>99.0852</td>
      <td>0</td>
      <td>0</td>
      <td>1023</td>
      <td>0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>188826</td>
      <td>187160</td>
      <td>1666</td>
      <td>99.1177</td>
      <td>0</td>
      <td>0</td>
      <td>1666</td>
      <td>0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>60734</td>
      <td>60162</td>
      <td>572</td>
      <td>99.0582</td>
      <td>0</td>
      <td>0</td>
      <td>572</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Index</th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Peptide</th>
      <th>ProteinID</th>
      <th>Protein_mapping_type</th>
      <th>Contaminant</th>
      <th>Probability</th>
      <th>...</th>
      <th>BED_block_sizes</th>
      <th>BED_block_starts</th>
      <th>Projection_status</th>
      <th>Projection_file</th>
      <th>Check_BED_geometry</th>
      <th>Check_block_nt_length</th>
      <th>Check_chromosome_and_strand</th>
      <th>Check_protein_coordinates</th>
      <th>All_sanity_checks_passed</th>
      <th>Sanity_check_status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>354</th>
      <td>355</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AAVFRWIHGLLKEMK</td>
      <td>TraesCSU03G0412800LC.1</td>
      <td>primary</td>
      <td>no</td>
      <td>0.0598</td>
      <td>...</td>
      <td>45</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>485</th>
      <td>486</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>ADIMESSTDQNF</td>
      <td>TraesCSU03G0471100LC.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9703</td>
      <td>...</td>
      <td>36</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>520</th>
      <td>521</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>ADNLYWEGFK</td>
      <td>TraesCSU03G0261100.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9970</td>
      <td>...</td>
      <td>30</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>521</th>
      <td>522</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>ADNLYWEGFK</td>
      <td>TraesCSU03G0261300.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9970</td>
      <td>...</td>
      <td>30</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>561</th>
      <td>562</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>ADVEAPDDDAEAEVRVDVETGDAAVKGGAPVMKR</td>
      <td>TraesCSU03G0110900.1</td>
      <td>primary</td>
      <td>no</td>
      <td>0.3168</td>
      <td>...</td>
      <td>102</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>641</th>
      <td>642</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AEHLASIFGTEK</td>
      <td>TraesCSU03G0077400LC.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.1075</td>
      <td>...</td>
      <td>36</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>642</th>
      <td>643</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AEHLASIFGTEK</td>
      <td>TraesCSU03G0540200LC.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.1075</td>
      <td>...</td>
      <td>36</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>643</th>
      <td>644</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AEHLASIFGTEK</td>
      <td>TraesCSU03G0553300LC.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.1075</td>
      <td>...</td>
      <td>36</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>929</th>
      <td>930</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLASARELR</td>
      <td>TraesCSU03G0085200.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.6766</td>
      <td>...</td>
      <td>30</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>930</th>
      <td>931</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLASARELR</td>
      <td>TraesCSU03G0085200.2</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.6766</td>
      <td>...</td>
      <td>30</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>931</th>
      <td>932</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLASARELR</td>
      <td>TraesCSU03G0085200.3</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.6766</td>
      <td>...</td>
      <td>30</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>948</th>
      <td>949</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLENGVLTVTVPK</td>
      <td>TraesCSU03G0040500.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9970</td>
      <td>...</td>
      <td>42</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>949</th>
      <td>950</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLENGVLTVTVPK</td>
      <td>TraesCSU03G0197500.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9970</td>
      <td>...</td>
      <td>42</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>950</th>
      <td>951</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLENGVLTVTVPK</td>
      <td>TraesCSU03G0235000.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9970</td>
      <td>...</td>
      <td>42</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>951</th>
      <td>952</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGLENGVLTVTVPK</td>
      <td>TraesCSU03G0289800.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.9970</td>
      <td>...</td>
      <td>42</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>1135</th>
      <td>1136</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AGTVVSMARSMLGAVISVAASAAATEMSLLMGVR</td>
      <td>TraesCSU03G0059700.1</td>
      <td>primary</td>
      <td>no</td>
      <td>0.1794</td>
      <td>...</td>
      <td>102</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>1154</th>
      <td>1155</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AHALVRSVRRLLAAILAIR</td>
      <td>TraesCSU03G0252900LC.1</td>
      <td>primary</td>
      <td>no</td>
      <td>0.7872</td>
      <td>...</td>
      <td>57</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>1398</th>
      <td>1399</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AKQDGQITGVVP</td>
      <td>TraesCSU03G0002700LC.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.3900</td>
      <td>...</td>
      <td>36</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>1399</th>
      <td>1400</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>AKQDGQITGVVP</td>
      <td>TraesCSU03G0132700LC.1</td>
      <td>mapped</td>
      <td>no</td>
      <td>0.3900</td>
      <td>...</td>
      <td>36</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
    <tr>
      <th>1639</th>
      <td>1640</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>ALWLLKLKPAK</td>
      <td>TraesCSU03G0106700.1</td>
      <td>primary</td>
      <td>no</td>
      <td>0.0878</td>
      <td>...</td>
      <td>33</td>
      <td>0</td>
      <td>projected</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>failed</td>
    </tr>
  </tbody>
</table>
<p>20 rows × 57 columns</p>
</div>


# Step 26 — Generate Sanity-Validated BED Files for Apollo/JBrowse Upload

This step creates a final set of Apollo/JBrowse BED files containing only peptide genome projections that passed the Step 25 sanity checks.

---

Rows failing any of the following checks are excluded:

- BED geometry validity
- BED block nucleotide length consistency
- chromosome and strand validity
- protein-coordinate consistency

---

The original BED files are preserved unchanged. Filtered versions are written to a new upload-ready directory:

`python_outputs/bed_Apollo_validated/`

---

These validated BED files should be used for public upload to Apollo/JBrowse.


```python
# ============================================================
# Step 26 — Generate sanity-validated BED files for Apollo/JBrowse upload (takes 7 min)
# Memory-light version using failed-row exclusion
# ============================================================

import pandas as pd
from pathlib import Path
import re

# -----------------------------
# 1. Input / output paths
# -----------------------------
bed_apollo_dir = Path("python_outputs/bed_Apollo")
validated_bed_dir = Path("python_outputs/bed_Apollo_validated")
tables_dir = Path("python_outputs/tables")

validated_bed_dir.mkdir(parents=True, exist_ok=True)

sanity_failed_file = tables_dir / "wheat_projection_sanity_checks_failed_rows_step25.csv"

summary_out = tables_dir / "wheat_validated_bed_filtering_summary_step26.csv"

# -----------------------------
# 2. Helper functions
# -----------------------------
def clean_peptide_from_bed_name(name):
    name = str(name)
    peptide = name.split("|")[0]
    peptide = peptide.replace("-", "")
    peptide = re.sub(r"[^A-Z]", "", peptide.upper())
    peptide = peptide.replace("I", "L")
    return peptide


def make_key(chrom, start, end, strand, peptide):
    return (
        chrom.astype(str) + "|" +
        start.astype(str) + "|" +
        end.astype(str) + "|" +
        strand.astype(str) + "|" +
        peptide.astype(str)
    )


# -----------------------------
# 3. Build failed-key set from Step 25 failed rows only
# -----------------------------
failed_keys = set()

if sanity_failed_file.exists():

    failed_usecols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "Strand",
        "Peptide"
    ]

    for chunk in pd.read_csv(
        sanity_failed_file,
        usecols=lambda col: col in failed_usecols,
        chunksize=100_000,
        low_memory=True
    ):

        chunk = chunk.dropna(
            subset=[
                "Chromosome",
                "BED_start_0based",
                "BED_end_0based_exclusive",
                "Strand",
                "Peptide"
            ]
        ).copy()

        chunk["BED_start_0based"] = pd.to_numeric(
            chunk["BED_start_0based"],
            errors="coerce"
        )

        chunk["BED_end_0based_exclusive"] = pd.to_numeric(
            chunk["BED_end_0based_exclusive"],
            errors="coerce"
        )

        chunk = chunk.dropna(
            subset=["BED_start_0based", "BED_end_0based_exclusive"]
        ).copy()

        chunk["BED_start_0based"] = chunk["BED_start_0based"].astype(int)
        chunk["BED_end_0based_exclusive"] = chunk["BED_end_0based_exclusive"].astype(int)

        chunk["peptide_clean"] = (
            chunk["Peptide"]
            .astype(str)
            .str.replace("-", "", regex=False)
            .str.upper()
            .str.replace("I", "L", regex=False)
        )

        keys = make_key(
            chunk["Chromosome"],
            chunk["BED_start_0based"],
            chunk["BED_end_0based_exclusive"],
            chunk["Strand"],
            chunk["peptide_clean"]
        )

        failed_keys.update(keys.tolist())

else:
    print(f"No failed-row file found: {sanity_failed_file}")
    print("Proceeding with no failed keys.")

print(f"Failed projection keys loaded: {len(failed_keys):,}")

# -----------------------------
# 4. Find Apollo BED files without duplicates
# -----------------------------
bed_extensions = {".bed", ".bed6", ".bed12"}

bed_files = sorted({
    path.resolve()
    for path in bed_apollo_dir.iterdir()
    if path.is_file() and path.suffix.lower() in bed_extensions
})

bed_files = [Path(path) for path in bed_files]

if len(bed_files) == 0:
    raise FileNotFoundError(
        f"No BED files found in {bed_apollo_dir}. "
        "Check the Apollo BED output folder name."
    )

print(f"Unique BED files found: {len(bed_files)}")

# -----------------------------
# 5. Filter BED files in chunks
# -----------------------------
summary_records = []

for bed_file in bed_files:

    print(f"\nFiltering: {bed_file.name}")

    output_file = validated_bed_dir / bed_file.name

    # Clear existing output if rerunning
    if output_file.exists():
        output_file.unlink()

    original_rows_total = 0
    retained_rows_total = 0
    removed_rows_total = 0

    chunk_iter = pd.read_csv(
        bed_file,
        sep="\t",
        header=None,
        comment="#",
        dtype=str,
        chunksize=100_000,
        low_memory=True
    )

    for chunk_i, chunk in enumerate(chunk_iter, start=1):

        original_rows_total += len(chunk)

        if chunk.shape[1] < 6:
            print(f"Skipped chunk {chunk_i}: fewer than 6 BED columns.")
            continue

        chunk = chunk.rename(columns={
            0: "chrom",
            1: "start",
            2: "end",
            3: "name",
            4: "score",
            5: "strand"
        })

        chunk["start"] = pd.to_numeric(chunk["start"], errors="coerce")
        chunk["end"] = pd.to_numeric(chunk["end"], errors="coerce")

        chunk = chunk.dropna(
            subset=["chrom", "start", "end", "name", "strand"]
        ).copy()

        chunk["start"] = chunk["start"].astype(int)
        chunk["end"] = chunk["end"].astype(int)

        chunk["peptide_clean"] = chunk["name"].apply(clean_peptide_from_bed_name)

        chunk["validation_key"] = make_key(
            chunk["chrom"],
            chunk["start"],
            chunk["end"],
            chunk["strand"],
            chunk["peptide_clean"]
        )

        filtered = chunk[
            ~chunk["validation_key"].isin(failed_keys)
        ].copy()

        retained_rows_total += len(filtered)
        removed_rows_total += len(chunk) - len(filtered)

        filtered = filtered.drop(columns=["peptide_clean", "validation_key"])

        filtered = filtered.rename(columns={
            "chrom": 0,
            "start": 1,
            "end": 2,
            "name": 3,
            "score": 4,
            "strand": 5
        })

        filtered.to_csv(
            output_file,
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )

    summary_records.append({
        "Input_BED_file": bed_file.name,
        "Original_rows": original_rows_total,
        "Retained_validated_rows": retained_rows_total,
        "Removed_failed_rows": removed_rows_total,
        "Percent_retained": round(
            (retained_rows_total / original_rows_total) * 100,
            4
        ) if original_rows_total > 0 else 0,
        "Output_BED_file": output_file.name
    })

    print(f"Original rows: {original_rows_total:,}")
    print(f"Retained rows: {retained_rows_total:,}")
    print(f"Removed failed rows: {removed_rows_total:,}")
    print(f"Saved: {output_file}")

# -----------------------------
# 6. Save summary
# -----------------------------
summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print("\n===== STEP 26 BED FILTERING SUMMARY =====")
print(f"BED files processed: {len(summary):,}")
print(f"Total original rows: {summary['Original_rows'].sum():,}")
print(f"Total retained rows: {summary['Retained_validated_rows'].sum():,}")
print(f"Total removed rows: {summary['Removed_failed_rows'].sum():,}")

print(f"\nValidated BED files saved in: {validated_bed_dir}")
print(f"Filtering summary saved: {summary_out}")

display(summary)
```

    Failed projection keys loaded: 32,845
    Unique BED files found: 64
    
    Filtering: Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 30,314
    Retained rows: 29,836
    Removed failed rows: 478
    Saved: python_outputs\bed_Apollo_validated\Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 30,314
    Retained rows: 29,836
    Removed failed rows: 478
    Saved: python_outputs\bed_Apollo_validated\Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 164,365
    Retained rows: 162,834
    Removed failed rows: 1,531
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 164,365
    Retained rows: 162,834
    Removed failed rows: 1,531
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 13,227
    Retained rows: 13,114
    Removed failed rows: 113
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 13,227
    Retained rows: 13,114
    Removed failed rows: 113
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 204,476
    Retained rows: 202,433
    Removed failed rows: 2,043
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 204,476
    Retained rows: 202,433
    Removed failed rows: 2,043
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 8,852
    Retained rows: 8,769
    Removed failed rows: 83
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 8,852
    Retained rows: 8,769
    Removed failed rows: 83
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 102,830
    Retained rows: 101,946
    Removed failed rows: 884
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 102,830
    Retained rows: 101,946
    Removed failed rows: 884
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 145,133
    Retained rows: 143,464
    Removed failed rows: 1,669
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 145,133
    Retained rows: 143,464
    Removed failed rows: 1,669
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 126,195
    Retained rows: 125,070
    Removed failed rows: 1,125
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 126,195
    Retained rows: 125,070
    Removed failed rows: 1,125
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 179,725
    Retained rows: 178,286
    Removed failed rows: 1,439
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 179,725
    Retained rows: 178,286
    Removed failed rows: 1,439
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 132,701
    Retained rows: 131,666
    Removed failed rows: 1,035
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 132,701
    Retained rows: 131,666
    Removed failed rows: 1,035
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 113,203
    Retained rows: 112,128
    Removed failed rows: 1,075
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 113,203
    Retained rows: 112,128
    Removed failed rows: 1,075
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 111,792
    Retained rows: 110,874
    Removed failed rows: 918
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 111,792
    Retained rows: 110,874
    Removed failed rows: 918
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 145,632
    Retained rows: 144,063
    Removed failed rows: 1,569
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 145,632
    Retained rows: 144,063
    Removed failed rows: 1,569
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 46,200
    Retained rows: 45,551
    Removed failed rows: 649
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 46,200
    Retained rows: 45,551
    Removed failed rows: 649
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 120,821
    Retained rows: 119,463
    Removed failed rows: 1,358
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 120,821
    Retained rows: 119,463
    Removed failed rows: 1,358
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 147,618
    Retained rows: 146,124
    Removed failed rows: 1,494
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 147,618
    Retained rows: 146,124
    Removed failed rows: 1,494
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 99,823
    Retained rows: 98,604
    Removed failed rows: 1,219
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 99,823
    Retained rows: 98,604
    Removed failed rows: 1,219
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 169,675
    Retained rows: 167,975
    Removed failed rows: 1,700
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 169,675
    Retained rows: 167,975
    Removed failed rows: 1,700
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 116,936
    Retained rows: 115,679
    Removed failed rows: 1,257
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 116,936
    Retained rows: 115,679
    Removed failed rows: 1,257
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 131,215
    Retained rows: 129,960
    Removed failed rows: 1,255
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 131,215
    Retained rows: 129,960
    Removed failed rows: 1,255
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 74,698
    Retained rows: 73,946
    Removed failed rows: 752
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 74,698
    Retained rows: 73,946
    Removed failed rows: 752
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 160,204
    Retained rows: 158,608
    Removed failed rows: 1,596
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 160,204
    Retained rows: 158,608
    Removed failed rows: 1,596
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 194,694
    Retained rows: 193,172
    Removed failed rows: 1,522
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 194,694
    Retained rows: 193,172
    Removed failed rows: 1,522
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 97,188
    Retained rows: 96,110
    Removed failed rows: 1,078
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 97,188
    Retained rows: 96,110
    Removed failed rows: 1,078
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 100,639
    Retained rows: 99,670
    Removed failed rows: 969
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 100,639
    Retained rows: 99,670
    Removed failed rows: 969
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 191,943
    Retained rows: 190,638
    Removed failed rows: 1,305
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 191,943
    Retained rows: 190,638
    Removed failed rows: 1,305
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 111,831
    Retained rows: 110,808
    Removed failed rows: 1,023
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 111,831
    Retained rows: 110,808
    Removed failed rows: 1,023
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 188,826
    Retained rows: 187,160
    Removed failed rows: 1,666
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 188,826
    Retained rows: 187,160
    Removed failed rows: 1,666
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 60,734
    Retained rows: 60,162
    Removed failed rows: 572
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 60,734
    Retained rows: 60,162
    Removed failed rows: 572
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 1,850,136
    Retained rows: 1,832,405
    Removed failed rows: 17,731
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 1,850,136
    Retained rows: 1,832,405
    Removed failed rows: 17,731
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 1,886,922
    Retained rows: 1,868,501
    Removed failed rows: 18,421
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 1,886,922
    Retained rows: 1,868,501
    Removed failed rows: 18,421
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    Filtering: Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    Original rows: 1,062,508
    Retained rows: 1,052,392
    Removed failed rows: 10,116
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    Filtering: Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    Original rows: 1,062,508
    Retained rows: 1,052,392
    Removed failed rows: 10,116
    Saved: python_outputs\bed_Apollo_validated\Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    
    ===== STEP 26 BED FILTERING SUMMARY =====
    BED files processed: 64
    Total original rows: 16,582,112
    Total retained rows: 16,422,822
    Total removed rows: 159,290
    
    Validated BED files saved in: python_outputs\bed_Apollo_validated
    Filtering summary saved: python_outputs\tables\wheat_validated_bed_filtering_summary_step26.csv
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input_BED_file</th>
      <th>Original_rows</th>
      <th>Retained_validated_rows</th>
      <th>Removed_failed_rows</th>
      <th>Percent_retained</th>
      <th>Output_BED_file</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Vincent_MSV000090572_stored_grain_projected-pe...</td>
      <td>30314</td>
      <td>29836</td>
      <td>478</td>
      <td>98.4232</td>
      <td>Vincent_MSV000090572_stored_grain_projected-pe...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Vincent_MSV000090572_stored_grain_projected-pe...</td>
      <td>30314</td>
      <td>29836</td>
      <td>478</td>
      <td>98.4232</td>
      <td>Vincent_MSV000090572_stored_grain_projected-pe...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Vincent_PXD004720_anther_projected-peptides_an...</td>
      <td>164365</td>
      <td>162834</td>
      <td>1531</td>
      <td>99.0685</td>
      <td>Vincent_PXD004720_anther_projected-peptides_an...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Vincent_PXD004720_anther_projected-peptides_an...</td>
      <td>164365</td>
      <td>162834</td>
      <td>1531</td>
      <td>99.0685</td>
      <td>Vincent_PXD004720_anther_projected-peptides_an...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Vincent_PXD004720_boot_projected-peptides_anno...</td>
      <td>13227</td>
      <td>13114</td>
      <td>113</td>
      <td>99.1457</td>
      <td>Vincent_PXD004720_boot_projected-peptides_anno...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Vincent_PXD050500_coleoptile_projected-peptide...</td>
      <td>1850136</td>
      <td>1832405</td>
      <td>17731</td>
      <td>99.0416</td>
      <td>Vincent_PXD050500_coleoptile_projected-peptide...</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Vincent_PXD050500_node_projected-peptides_anno...</td>
      <td>1886922</td>
      <td>1868501</td>
      <td>18421</td>
      <td>99.0238</td>
      <td>Vincent_PXD050500_node_projected-peptides_anno...</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Vincent_PXD050500_node_projected-peptides_anno...</td>
      <td>1886922</td>
      <td>1868501</td>
      <td>18421</td>
      <td>99.0238</td>
      <td>Vincent_PXD050500_node_projected-peptides_anno...</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Vincent_PXD050500_radicle_projected-peptides_a...</td>
      <td>1062508</td>
      <td>1052392</td>
      <td>10116</td>
      <td>99.0479</td>
      <td>Vincent_PXD050500_radicle_projected-peptides_a...</td>
    </tr>
    <tr>
      <th>63</th>
      <td>Vincent_PXD050500_radicle_projected-peptides_a...</td>
      <td>1062508</td>
      <td>1052392</td>
      <td>10116</td>
      <td>99.0479</td>
      <td>Vincent_PXD050500_radicle_projected-peptides_a...</td>
    </tr>
  </tbody>
</table>
<p>64 rows × 6 columns</p>
</div>


# Step 27 — Create Non-Redundant Combined Validated BED Tracks

This step combines all sanity-validated Apollo/JBrowse BED files generated in Step 26 into single all-tissue BED6 and BED12 tracks.

Unlike simple exact-row deduplication, this version collapses visually identical BED features that differ only by BED score. This is important because the same peptide projection can be observed in multiple tissues or source datasets with different peptide probabilities, producing otherwise identical browser features with different scores.

For each duplicate visual feature, the maximum BED score is retained.

---

BED6 features are collapsed using:

- chromosome
- start
- end
- name
- strand

---

BED12 features are collapsed using:

- chromosome
- start
- end
- name
- strand
- thickStart
- thickEnd
- itemRgb
- blockCount
- blockSizes
- blockStarts

---

The resulting files provide compact non-redundant all-tissue tracks suitable for Apollo/JBrowse upload.


```python
# ============================================================
# Step 27 — Create non-redundant combined validated BED tracks
# ============================================================

import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Input / output paths
# -----------------------------
validated_bed_dir = Path("python_outputs/bed_Apollo_validated")
tables_dir = Path("python_outputs/tables")

tables_dir.mkdir(parents=True, exist_ok=True)

combined_bed6_out = validated_bed_dir / "Vincent_all-tissues_validated_projected-peptides_annotation-proteogenomics_20260518.bed6"
combined_bed12_out = validated_bed_dir / "Vincent_all-tissues_validated_projected-peptides_annotation-proteogenomics_20260518.bed12"

summary_out = tables_dir / "wheat_combined_validated_bed_summary_step27.csv"

# -----------------------------
# 2. Find validated BED files
# -----------------------------
bed_files = sorted({
    path.resolve()
    for path in validated_bed_dir.iterdir()
    if path.is_file() and path.suffix.lower() in {".bed6", ".bed12"}
})

bed_files = [Path(path) for path in bed_files]

# Exclude previous combined outputs if rerunning
bed_files = [
    path for path in bed_files
    if not path.name.startswith("Vincent_all-tissues_validated_projected-peptides")
]

if len(bed_files) == 0:
    raise FileNotFoundError(
        f"No validated BED6/BED12 files found in: {validated_bed_dir}"
    )

bed6_files = [path for path in bed_files if path.suffix.lower() == ".bed6"]
bed12_files = [path for path in bed_files if path.suffix.lower() == ".bed12"]

print(f"Validated BED6 files found: {len(bed6_files)}")
print(f"Validated BED12 files found: {len(bed12_files)}")

# -----------------------------
# 3. Helper function
# -----------------------------
def combine_bed_files_nonredundant(bed_file_list, output_file, expected_min_cols):
    """
    Combine BED files and remove visually duplicated BED features.

    Unlike exact row deduplication, this collapses rows that represent the
    same browser feature but have different BED scores, keeping the highest score.
    """

    combined_chunks = []
    input_row_count = 0

    for bed_file in bed_file_list:
        print(f"Reading: {bed_file.name}")

        data = pd.read_csv(
            bed_file,
            sep="\t",
            header=None,
            comment="#",
            low_memory=False
        )

        if data.shape[1] < expected_min_cols:
            print(f"  Skipped: fewer than {expected_min_cols} columns")
            continue

        data = data.iloc[:, :expected_min_cols].copy()
        input_row_count += len(data)
        combined_chunks.append(data)

    if len(combined_chunks) == 0:
        raise ValueError(f"No valid BED files available for: {output_file.name}")

    combined = pd.concat(combined_chunks, ignore_index=True)
    rows_before_dedup = len(combined)

    # Ensure coordinates and score are numeric
    combined[1] = pd.to_numeric(combined[1], errors="coerce")
    combined[2] = pd.to_numeric(combined[2], errors="coerce")
    combined[4] = pd.to_numeric(combined[4], errors="coerce").fillna(1000).astype(int)

    if expected_min_cols == 6:
        # BED6: chrom, start, end, name, score, strand
        dedup_cols = [0, 1, 2, 3, 5]

        combined = (
            combined
            .groupby(dedup_cols, dropna=False, as_index=False)
            .agg({4: "max"})
        )

        combined = combined[[0, 1, 2, 3, 4, 5]]

    elif expected_min_cols == 12:
        # BED12: collapse same feature/block structure, keep max score
        dedup_cols = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

        combined = (
            combined
            .groupby(dedup_cols, dropna=False, as_index=False)
            .agg({4: "max"})
        )

        combined = combined[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]

    else:
        raise ValueError("Only BED6 and BED12 are supported.")

    rows_after_dedup = len(combined)

    combined = (
        combined
        .sort_values(by=[0, 1, 2])
        .reset_index(drop=True)
    )

    # Restore integer coordinate display
    for col in [1, 2, 4]:
        combined[col] = combined[col].astype("Int64").astype(str)

    if expected_min_cols == 12:
        for col in [6, 7, 9]:
            combined[col] = pd.to_numeric(combined[col], errors="coerce").astype("Int64").astype(str)

    combined.to_csv(
        output_file,
        sep="\t",
        header=False,
        index=False
    )

    return {
        "Output_file": output_file.name,
        "Input_files": len(bed_file_list),
        "Input_rows_total": input_row_count,
        "Rows_before_deduplication": rows_before_dedup,
        "Rows_after_deduplication": rows_after_dedup,
        "Duplicate_rows_removed": rows_before_dedup - rows_after_dedup
    }

# -----------------------------
# 4. Combine BED6 files
# -----------------------------
summary_records = []

if len(bed6_files) > 0:
    bed6_summary = combine_bed_files_nonredundant(
        bed_file_list=bed6_files,
        output_file=combined_bed6_out,
        expected_min_cols=6
    )
    bed6_summary["BED_format"] = "BED6"
    summary_records.append(bed6_summary)

# -----------------------------
# 5. Combine BED12 files
# -----------------------------
if len(bed12_files) > 0:
    bed12_summary = combine_bed_files_nonredundant(
        bed_file_list=bed12_files,
        output_file=combined_bed12_out,
        expected_min_cols=12
    )
    bed12_summary["BED_format"] = "BED12"
    summary_records.append(bed12_summary)

# -----------------------------
# 6. Save summary
# -----------------------------
summary = pd.DataFrame(summary_records)

summary = summary[
    [
        "BED_format",
        "Output_file",
        "Input_files",
        "Input_rows_total",
        "Rows_before_deduplication",
        "Rows_after_deduplication",
        "Duplicate_rows_removed"
    ]
]

summary.to_csv(summary_out, index=False)

print("\n===== STEP 27 COMBINED VALIDATED BED SUMMARY =====")
display(summary)

print(f"\nCombined BED6 saved: {combined_bed6_out}")
print(f"Combined BED12 saved: {combined_bed12_out}")
print(f"Summary saved: {summary_out}")
```

    Validated BED6 files found: 32
    Validated BED12 files found: 32
    Reading: Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed6
    Reading: Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_20260518.bed12
    Reading: Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_20260518.bed12
    
    ===== STEP 27 COMBINED VALIDATED BED SUMMARY =====
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BED_format</th>
      <th>Output_file</th>
      <th>Input_files</th>
      <th>Input_rows_total</th>
      <th>Rows_before_deduplication</th>
      <th>Rows_after_deduplication</th>
      <th>Duplicate_rows_removed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BED6</td>
      <td>Vincent_all-tissues_validated_projected-peptid...</td>
      <td>32</td>
      <td>8211411</td>
      <td>8211411</td>
      <td>3188235</td>
      <td>5023176</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BED12</td>
      <td>Vincent_all-tissues_validated_projected-peptid...</td>
      <td>32</td>
      <td>8211411</td>
      <td>8211411</td>
      <td>3188235</td>
      <td>5023176</td>
    </tr>
  </tbody>
</table>
</div>


    
    Combined BED6 saved: python_outputs\bed_Apollo_validated\Vincent_all-tissues_validated_projected-peptides_annotation-proteogenomics_20260518.bed6
    Combined BED12 saved: python_outputs\bed_Apollo_validated\Vincent_all-tissues_validated_projected-peptides_annotation-proteogenomics_20260518.bed12
    Summary saved: python_outputs\tables\wheat_combined_validated_bed_summary_step27.csv
    

# Step 28 — Prepare manuscript Table 1 summary statistics

This step prepares a manuscript-oriented summary table for Table 1 by combining selected workflow metrics across previous summary tables.

The table reports dataset-scale, proteomics-scale, projection-scale, validation-scale, and genome-annotation support metrics for each public data source and for the complete study.

Importantly, gene-model mapping rates are calculated from non-redundant projected gene models, not from tissue-level summed counts. This avoids double-counting gene models detected in multiple tissues or sources.

---

Mapping rates are calculated as:

- HC mapping rate = unique projected HC gene models / total GFF3-parsed HC gene models × 100
- LC mapping rate = unique projected LC gene models / total GFF3-parsed LC gene models × 100
- Total mapping rate = unique projected HC+LC gene models / total GFF3-parsed HC+LC gene models × 100
---

The output table is intended as a preparatory version of manuscript Table 1 and can be edited further for publication formatting.


```python
# ============================================================
# Step 28 — Prepare manuscript Table 1 summary statistics
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path
import re

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
output_file = tables_dir / "wheat_manuscript_table1_preparatory_step28.csv"

# Main input summary tables
step23_file = tables_dir / "wheat_complete_python_workflow_summary_step23.csv"
step25_file = tables_dir / "wheat_projection_sanity_checks_summary_step25.csv"
gff3_summary_file = tables_dir / "wheat_gff3_parsing_summary_HC_LC.csv"

# Row-level projection files are needed for non-redundant gene-model counts.
# Edit this pattern only if your final projected/validated row-level CSV files have a different name.
projection_file_patterns = [
    "*projected*peptide*.csv",
    "*projection*.csv",
    "*peptide*genome*.csv",
]

# -----------------------------
# 2. Manual dataset metadata
# -----------------------------
# These are study-level metadata, not derived from previous summary tables.
dataset_metadata = {
    "MSV000090572": {
        "Total tissues analysed": 1,
        "Total PRIDE/MassIVE datasets": 1,
        "Total raw MS files": 62,
        "Total raw data size (GB)": 12,
    },
    "PXD004720": {
        "Total tissues analysed": 28,
        "Total PRIDE/MassIVE datasets": 1,
        "Total raw MS files": 335,
        "Total raw data size (GB)": 563,
    },
    "PXD050500": {
        "Total tissues analysed": 3,
        "Total PRIDE/MassIVE datasets": 1,
        "Total raw MS files": 180,
        "Total raw data size (GB)": 434,
    },
}

sources = ["MSV000090572", "PXD004720", "PXD050500"]


# -----------------------------
# 3. Helper functions
# -----------------------------
def safe_read_csv(path, **kwargs):
    """Read CSV with a helpful error message."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found:\n{path}")
    return pd.read_csv(path, low_memory=False, **kwargs)


def clean_number(x):
    """Convert values to numeric where possible."""
    return pd.to_numeric(x, errors="coerce")


def add_row(rows, order, metric, total=np.nan, source_values=None, note=""):
    """Append one formatted row to the Table 1 preparatory output."""
    row = {
        "order": order,
        "Metric": metric,
        "Total": total,
        "MSV000090572": np.nan,
        "PXD004720": np.nan,
        "PXD050500": np.nan,
        "Note": note,
    }

    if source_values is not None:
        for src in sources:
            row[src] = source_values.get(src, np.nan)

    rows.append(row)


def sum_by_source(df, metric_col):
    """
    Sum a metric by Source.
    Requires columns: Source and metric_col.
    """
    if metric_col not in df.columns:
        raise KeyError(f"Column not found: {metric_col}")

    out = (
        df.groupby("Source", dropna=False)[metric_col]
        .sum()
        .to_dict()
    )

    total = sum(v for v in out.values() if pd.notna(v))
    return total, out


def find_source_column(df):
    """Find a likely source column."""
    for col in ["Source", "source", "Dataset", "dataset"]:
        if col in df.columns:
            return col
    return None


def find_gene_column(df):
    """Find a likely gene model column."""
    candidate_cols = [
        "GeneModel", "Gene_model", "GeneID", "Gene_ID",
        "gene_model", "gene_id", "Gene"
    ]
    for col in candidate_cols:
        if col in df.columns:
            return col
    return None


def find_confidence_column(df):
    """Find a likely HC/LC annotation confidence column."""
    candidate_cols = [
        "Annotation_confidence", "AnnotationConfidence",
        "Confidence", "annotation_confidence",
        "HC_LC", "Evidence_category"
    ]
    for col in candidate_cols:
        if col in df.columns:
            return col
    return None


def normalise_confidence(value):
    """Normalise annotation confidence values to HC / LC where possible."""
    if pd.isna(value):
        return np.nan

    value = str(value).strip().upper()

    if value in ["HC", "HIGH", "HIGH_CONFIDENCE", "HIGH CONFIDENCE"]:
        return "HC"

    if value in ["LC", "LOW", "LOW_CONFIDENCE", "LOW CONFIDENCE"]:
        return "LC"

    return value


def collect_projection_row_level_tables():
    """
    Locate and load row-level projection tables that contain Source, GeneModel,
    and Annotation_confidence columns.

    This is required for non-redundant gene-model mapping rates.
    """
    candidate_files = []

    for pattern in projection_file_patterns:
        candidate_files.extend(sorted(tables_dir.glob(pattern)))

    # Remove duplicates while preserving order
    candidate_files = list(dict.fromkeys(candidate_files))

    usable_tables = []

    for file in candidate_files:
        try:
            df = pd.read_csv(file, low_memory=False)
        except Exception:
            continue

        source_col = find_source_column(df)
        gene_col = find_gene_column(df)
        conf_col = find_confidence_column(df)

        if source_col is not None and gene_col is not None and conf_col is not None:
            tmp = df[[source_col, gene_col, conf_col]].copy()
            tmp.columns = ["Source", "GeneModel", "Annotation_confidence"]
            tmp["Annotation_confidence"] = tmp["Annotation_confidence"].apply(normalise_confidence)
            tmp["Input_file"] = file.name

            usable_tables.append(tmp)

    if len(usable_tables) == 0:
        print("No row-level projection table with Source, GeneModel and Annotation_confidence was found.")
        print("Candidate files inspected:")
        for f in candidate_files[:30]:
            print(f"  - {f.name}")
        print("\nPlease update projection_file_patterns or provide the correct row-level projection CSV filename.")
        return pd.DataFrame()

    projected_genes = pd.concat(usable_tables, ignore_index=True)

    # Keep only valid HC/LC gene model rows
    projected_genes = projected_genes[
        projected_genes["Annotation_confidence"].isin(["HC", "LC"])
    ].copy()

    projected_genes = projected_genes.dropna(subset=["Source", "GeneModel"])

    return projected_genes


# -----------------------------
# 4. Load summary tables
# -----------------------------
step23 = safe_read_csv(step23_file)
step25 = safe_read_csv(step25_file)
gff3_summary = safe_read_csv(gff3_summary_file)

# Ensure numeric columns are numeric where needed
for df in [step23, step25]:
    for col in df.columns:
        if col != "Source":
            try:
                df[col] = pd.to_numeric(df[col])
            except (ValueError, TypeError):
                pass


# -----------------------------
# 5. Extract GFF3 denominator values
# -----------------------------
# Expected file structure:
# Metric, Value
if {"Metric", "Value"}.issubset(gff3_summary.columns):
    gff3_dict = dict(zip(gff3_summary["Metric"], gff3_summary["Value"]))
else:
    raise KeyError("GFF3 summary file must contain columns 'Metric' and 'Value'.")

# In Step 5 output:
# Mapping_rows_HC = number of HC protein/transcript mapping rows
# Mapping_rows_LC = number of LC protein/transcript mapping rows
gff3_hc_total = int(gff3_dict.get("Mapping_rows_HC", np.nan))
gff3_lc_total = int(gff3_dict.get("Mapping_rows_LC", np.nan))
gff3_total = gff3_hc_total + gff3_lc_total


# -----------------------------
# 6. Compute non-redundant projected gene-model support
# -----------------------------
projected_genes = collect_projection_row_level_tables()

if projected_genes.empty:
    unique_gene_counts_by_source = pd.DataFrame()
    overall_gene_counts = {"HC": np.nan, "LC": np.nan, "Total": np.nan}
else:
    # Non-redundant within each source
    unique_by_source_conf = (
        projected_genes
        .drop_duplicates(["Source", "Annotation_confidence", "GeneModel"])
        .groupby(["Source", "Annotation_confidence"])["GeneModel"]
        .nunique()
        .unstack(fill_value=0)
    )

    for col in ["HC", "LC"]:
        if col not in unique_by_source_conf.columns:
            unique_by_source_conf[col] = 0

    unique_by_source_conf["Total"] = (
        unique_by_source_conf["HC"] + unique_by_source_conf["LC"]
    )

    unique_gene_counts_by_source = unique_by_source_conf.reset_index()

    # Non-redundant across the complete study
    overall_gene_counts_series = (
        projected_genes
        .drop_duplicates(["Annotation_confidence", "GeneModel"])
        .groupby("Annotation_confidence")["GeneModel"]
        .nunique()
    )

    overall_gene_counts = {
        "HC": int(overall_gene_counts_series.get("HC", 0)),
        "LC": int(overall_gene_counts_series.get("LC", 0)),
    }
    overall_gene_counts["Total"] = overall_gene_counts["HC"] + overall_gene_counts["LC"]


def get_gene_count_source_dict(conf):
    """Return source-level non-redundant gene counts for HC, LC or Total."""
    if unique_gene_counts_by_source.empty:
        return {src: np.nan for src in sources}

    out = {}
    for src in sources:
        match = unique_gene_counts_by_source[unique_gene_counts_by_source["Source"] == src]
        if match.empty:
            out[src] = 0
        else:
            out[src] = int(match.iloc[0][conf])
    return out


# -----------------------------
# 7. Build preparatory Table 1
# -----------------------------
rows = []

# Dataset metadata
for metric, order in [
    ("Total tissues analysed", 1),
    ("Total PRIDE/MassIVE datasets", 2),
    ("Total raw MS files", 3),
    ("Total raw data size (GB)", 4),
]:
    source_values = {src: dataset_metadata[src][metric] for src in sources}
    total = sum(source_values.values())
    add_row(rows, order, metric, total=total, source_values=source_values)

# Proteomics outputs from Step 23
metric_map_step23 = [
    ("step7_Unique_peptides", 5, "Unique peptides"),
    ("step7_Unique_proteins", 6, "Unique proteins"),
    ("step9_Projected_rows", 7, "Projected peptide rows"),
]

for col, order, label in metric_map_step23:
    total, source_values = sum_by_source(step23, col)
    add_row(rows, order, label, total=int(total), source_values={k: int(v) for k, v in source_values.items()})

# Projection sanity checks from Step 25
metric_map_step25 = [
    ("Projected_rows_checked", 8, "Total projected rows"),
    ("Rows_passing_all_sanity_checks", 9, "Validation-passing projected rows"),
    ("Rows_failing_any_sanity_check", 10, "Validation-failing projected rows"),
]

step25_values = {}

for col, order, label in metric_map_step25:
    total, source_values = sum_by_source(step25, col)
    step25_values[col] = {"total": total, "sources": source_values}
    add_row(rows, order, label, total=int(total), source_values={k: int(v) for k, v in source_values.items()})

# Validation rate
validation_rate_sources = {}
for src in sources:
    checked = step25_values["Projected_rows_checked"]["sources"].get(src, np.nan)
    passed = step25_values["Rows_passing_all_sanity_checks"]["sources"].get(src, np.nan)
    validation_rate_sources[src] = round((passed / checked) * 100, 2) if checked else np.nan

validation_rate_total = round(
    (step25_values["Rows_passing_all_sanity_checks"]["total"] /
     step25_values["Projected_rows_checked"]["total"]) * 100,
    2
)

add_row(
    rows,
    11,
    "Validation rate (%)",
    total=validation_rate_total,
    source_values=validation_rate_sources,
    note="Rows passing all projection sanity checks / projected rows checked × 100"
)

# Non-redundant gene-model support
add_row(
    rows,
    12,
    "Non-redundant projected HC gene models",
    total=overall_gene_counts["HC"],
    source_values=get_gene_count_source_dict("HC"),
    note="Computed from row-level projection tables using unique GeneModel counts"
)

add_row(
    rows,
    13,
    "Non-redundant projected LC gene models",
    total=overall_gene_counts["LC"],
    source_values=get_gene_count_source_dict("LC"),
    note="Computed from row-level projection tables using unique GeneModel counts"
)

add_row(
    rows,
    14,
    "Non-redundant projected total gene models",
    total=overall_gene_counts["Total"],
    source_values=get_gene_count_source_dict("Total"),
    note="HC + LC non-redundant projected gene models"
)

# GFF3 denominators
add_row(
    rows,
    15,
    "GFF3-parsed HC gene models",
    total=gff3_hc_total,
    source_values={src: np.nan for src in sources},
    note="Reference denominator from IWGSC RefSeq v2.1 GFF3 parsing"
)

add_row(
    rows,
    16,
    "GFF3-parsed LC gene models",
    total=gff3_lc_total,
    source_values={src: np.nan for src in sources},
    note="Reference denominator from IWGSC RefSeq v2.1 GFF3 parsing"
)

add_row(
    rows,
    17,
    "GFF3-parsed total gene models",
    total=gff3_total,
    source_values={src: np.nan for src in sources},
    note="HC + LC GFF3-parsed gene models"
)

# Mapping rates
hc_rate = round((overall_gene_counts["HC"] / gff3_hc_total) * 100, 2) if gff3_hc_total else np.nan
lc_rate = round((overall_gene_counts["LC"] / gff3_lc_total) * 100, 2) if gff3_lc_total else np.nan
total_rate = round((overall_gene_counts["Total"] / gff3_total) * 100, 2) if gff3_total else np.nan

hc_rate_sources = {
    src: round((get_gene_count_source_dict("HC")[src] / gff3_hc_total) * 100, 2)
    if gff3_hc_total else np.nan
    for src in sources
}

lc_rate_sources = {
    src: round((get_gene_count_source_dict("LC")[src] / gff3_lc_total) * 100, 2)
    if gff3_lc_total else np.nan
    for src in sources
}

total_rate_sources = {
    src: round((get_gene_count_source_dict("Total")[src] / gff3_total) * 100, 2)
    if gff3_total else np.nan
    for src in sources
}

add_row(
    rows,
    18,
    "HC gene model projection rate (%)",
    total=hc_rate,
    source_values=hc_rate_sources,
    note="Non-redundant projected HC gene models / GFF3-parsed HC gene models × 100"
)

add_row(
    rows,
    19,
    "LC gene model projection rate (%)",
    total=lc_rate,
    source_values=lc_rate_sources,
    note="Non-redundant projected LC gene models / GFF3-parsed LC gene models × 100"
)

add_row(
    rows,
    20,
    "Total gene model projection rate (%)",
    total=total_rate,
    source_values=total_rate_sources,
    note="Non-redundant projected total gene models / GFF3-parsed total gene models × 100"
)

# -----------------------------
# 8. Final formatting
# -----------------------------
table1_prep = pd.DataFrame(rows)
table1_prep = table1_prep.sort_values("order").reset_index(drop=True)

# Add formatted display columns while keeping numeric values exportable
display_table = table1_prep.copy()

for col in ["Total", "MSV000090572", "PXD004720", "PXD050500"]:
    display_table[col] = display_table[col].apply(
        lambda x: "" if pd.isna(x) else f"{x:,.2f}" if isinstance(x, float) and not x.is_integer() else f"{int(x):,}"
    )

# Save numeric version
table1_prep.to_csv(output_file, index=False)

print(f"Preparatory manuscript Table 1 saved to:\n{output_file}")
print("\nNon-redundant gene-model counts were computed from:")
if not projected_genes.empty:
    display(projected_genes[["Input_file"]].drop_duplicates().head(20))
else:
    print("No suitable row-level projection files detected.")

display(display_table)
```

    Preparatory manuscript Table 1 saved to:
    python_outputs\tables\wheat_manuscript_table1_preparatory_step28.csv
    
    Non-redundant gene-model counts were computed from:
    


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input_file</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
    </tr>
    <tr>
      <th>164365</th>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
    </tr>
    <tr>
      <th>177592</th>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
    </tr>
    <tr>
      <th>382068</th>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
    </tr>
    <tr>
      <th>390920</th>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
    </tr>
    <tr>
      <th>493750</th>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
    </tr>
    <tr>
      <th>638883</th>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
    </tr>
    <tr>
      <th>765078</th>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
    </tr>
    <tr>
      <th>944803</th>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
    </tr>
    <tr>
      <th>1077504</th>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
    </tr>
    <tr>
      <th>1190707</th>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
    </tr>
    <tr>
      <th>1302499</th>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
    </tr>
    <tr>
      <th>1448131</th>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
    </tr>
    <tr>
      <th>1494331</th>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
    </tr>
    <tr>
      <th>1615152</th>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
    </tr>
    <tr>
      <th>1762770</th>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
    </tr>
    <tr>
      <th>1932445</th>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
    </tr>
    <tr>
      <th>2032268</th>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
    </tr>
    <tr>
      <th>2149204</th>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
    </tr>
    <tr>
      <th>2280419</th>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>order</th>
      <th>Metric</th>
      <th>Total</th>
      <th>MSV000090572</th>
      <th>PXD004720</th>
      <th>PXD050500</th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Total tissues analysed</td>
      <td>32</td>
      <td>1</td>
      <td>28</td>
      <td>3</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Total PRIDE/MassIVE datasets</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Total raw MS files</td>
      <td>577</td>
      <td>62</td>
      <td>335</td>
      <td>180</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Total raw data size (GB)</td>
      <td>1,009</td>
      <td>12</td>
      <td>563</td>
      <td>434</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Unique peptides</td>
      <td>2,226,779</td>
      <td>9,329</td>
      <td>705,663</td>
      <td>1,511,787</td>
      <td></td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Unique proteins</td>
      <td>1,648,740</td>
      <td>17,481</td>
      <td>942,854</td>
      <td>688,405</td>
      <td></td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Projected peptide rows</td>
      <td>8,291,056</td>
      <td>30,314</td>
      <td>3,461,176</td>
      <td>4,799,566</td>
      <td></td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Total projected rows</td>
      <td>8,291,056</td>
      <td>30,314</td>
      <td>3,461,176</td>
      <td>4,799,566</td>
      <td></td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Validation-passing projected rows</td>
      <td>8,211,411</td>
      <td>29,836</td>
      <td>3,428,277</td>
      <td>4,753,298</td>
      <td></td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Validation-failing projected rows</td>
      <td>79,645</td>
      <td>478</td>
      <td>32,899</td>
      <td>46,268</td>
      <td></td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Validation rate (%)</td>
      <td>99.04</td>
      <td>98.42</td>
      <td>99.05</td>
      <td>99.04</td>
      <td>Rows passing all projection sanity checks / pr...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Non-redundant projected HC gene models</td>
      <td>104,576</td>
      <td>9,169</td>
      <td>79,808</td>
      <td>103,930</td>
      <td>Computed from row-level projection tables usin...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Non-redundant projected LC gene models</td>
      <td>144,506</td>
      <td>5,734</td>
      <td>71,041</td>
      <td>141,408</td>
      <td>Computed from row-level projection tables usin...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Non-redundant projected total gene models</td>
      <td>249,082</td>
      <td>14,903</td>
      <td>150,849</td>
      <td>245,338</td>
      <td>HC + LC non-redundant projected gene models</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>GFF3-parsed HC gene models</td>
      <td>132,624</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Reference denominator from IWGSC RefSeq v2.1 G...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>GFF3-parsed LC gene models</td>
      <td>163,290</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Reference denominator from IWGSC RefSeq v2.1 G...</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>GFF3-parsed total gene models</td>
      <td>295,914</td>
      <td></td>
      <td></td>
      <td></td>
      <td>HC + LC GFF3-parsed gene models</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>HC gene model projection rate (%)</td>
      <td>78.85</td>
      <td>6.91</td>
      <td>60.18</td>
      <td>78.36</td>
      <td>Non-redundant projected HC gene models / GFF3-...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>LC gene model projection rate (%)</td>
      <td>88.50</td>
      <td>3.51</td>
      <td>43.51</td>
      <td>86.60</td>
      <td>Non-redundant projected LC gene models / GFF3-...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>Total gene model projection rate (%)</td>
      <td>84.17</td>
      <td>5.04</td>
      <td>50.98</td>
      <td>82.91</td>
      <td>Non-redundant projected total gene models / GF...</td>
    </tr>
  </tbody>
</table>
</div>


# End of notebook
