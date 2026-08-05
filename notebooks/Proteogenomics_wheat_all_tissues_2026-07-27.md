# Community Resource: A Genome-Based Extension of Large-Scale Wheat Proteogenomics

---

## Author   
Dr Delphine Vincent  
_website:_ https://dlf2024.github.io/  
_github:_ https://github.com/dlf2024      
_Date:_ 27/07/2026

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
- 10: Translation validation of annotation-guided peptide genome projections (this notebook)
- 11: Sanity Checks for translation-validated peptide Genome Projections (this notebook)
- 12: Export all tissues BED6/BED12 files for JBrowse (this notebook)
- 13: Create a single non-redundant combined BED track (this notebook)
- 14: Prepare BED Files for Apollo/JBrowse Public Upload (this notebook)
- 15: Generate tissue/protein/gene/isoform summary tables (this notebook)
- 16: EDA: Barplot of HC and LC Proteogenomic Coverage by Tissue (this notebook)
- 17: EDA: Tissue Overlap Using UpSet Plots (this notebook)
- 18: EDA: Distributions of Peptide Support per Gene Model (this notebook)
- 19: EDA: Scatterplot of Peptide Length and Probability by Annotation Confidence  (this notebook)
- 20: EDA: Scatterplot of Protein Length versus Peptide Support (this notebook)
- 21: EDA: Violin plot of Chromosomal Distribution of Peptide Genomic Start Positions (this notebook)
- 22: EDA: Circular plot of Tissue-Level Peptide Genome Map (this notebook)
- 23: EDA: Pie chart of HC and LC Proteogenomic Coverage with Within-Exon/Exon-spanning Peptides (this notebook)
- 24: Combine Python workflow Summary Tables at Source/Tissue Level (this notebook)
- 25: Prepare manuscript Table 1 summary statistics (this notebook)

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
├── fragpipe_tissue_reports/    
├── fragpipe_tissue_runtime_logs/    
├── fragpipe_tissue_filter_logs/   
├── fragpipe_tissues_manifests/      
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

## Protein DB entry counts

- HC wheat protein entries:       132,624
- LC wheat protein entries:       163,290
- cRAP contaminant entries:           116
- Total target entries:           296,030
- Reversed decoy entries:         296,030
- Final database entries:         592,060

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

---

## Empirical evaluation of permissive digestion and peptide-size limits

To determine whether the permissive search limits recovered peptide classes that would have been excluded under more conventional settings, the final tissue-specific FragPipe `peptide.tsv` reports were examined across all 32 analyses.

For each filtered peptide identification:

- peptide length was obtained from the FragPipe `Peptide Length` field;
- missed cleavages were calculated from the peptide sequence as the number of   internal lysine or arginine residues, excluding the C-terminal residue, under   the fully enzymatic Trypsin/P search definition;
- decoy and contaminant entries were excluded where present.

Distributions were summarised both across the complete peptide resource and within individual tissues. Particular attention was given to peptides with more than two missed cleavages and peptides longer than 50 amino acids, because these would commonly be excluded by narrower digestion and peptide-length limits.

Both unique-peptide counts and spectral-count-weighted summaries were exported.
The supplementary figure uses unique-peptide counts to avoid disproportionately weighting peptides repeatedly observed across spectra.


```python
# ============================================================
# Step 4 — Evaluate use of permissive missed-cleavage and
# peptide-length search limits across all FragPipe peptide reports
# ============================================================

from pathlib import Path
import re

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


# ------------------------------------------------------------
# 1. Input and output folders
# ------------------------------------------------------------

fragpipe_dir = Path("FragPipe_results")

tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")

tables_dir.mkdir(parents=True, exist_ok=True)
figures_dir.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. Locate tissue-level peptide reports
# ------------------------------------------------------------

peptide_files = sorted(
    path for path in fragpipe_dir.glob("*_peptide.tsv")
    if "combined" not in path.name.lower()
)

if not peptide_files:
    raise FileNotFoundError(
        f"No '*_peptide.tsv' files were found in: {fragpipe_dir.resolve()}"
    )

print(f"Peptide reports found: {len(peptide_files):,}")

for path in peptide_files[:5]:
    print(f"  {path.name}")

if len(peptide_files) > 5:
    print("  ...")


# ------------------------------------------------------------
# 3. Helper functions
# ------------------------------------------------------------

def derive_source_tissue_labels(filename):
    """
    Derive source, tissue and source–tissue labels from a standard
    FragPipe peptide filename.

    Example
    -------
    FragPipe_Duncan_PXD004720_radicle_peptide.tsv

    Source:
        PXD004720

    Tissue:
        radicle

    Source_tissue:
        PXD004720 | radicle
    """
    stem = filename.replace("_peptide.tsv", "")
    parts = stem.split("_")

    # Expected structure:
    # FragPipe_FirstAuthor_Source_Tissue
    if len(parts) >= 4 and parts[0].lower() == "fragpipe":
        source = parts[2]
        tissue = "_".join(parts[3:])
        source_tissue = f"{source} | {tissue}"

        return source, tissue, source_tissue

    # Fallback for an unexpected filename
    return "unknown", stem, f"unknown | {stem}"


def clean_peptide_sequence(sequence):
    """
    Retain uppercase amino-acid letters only.

    This allows the function to remain robust if a peptide field contains
    flanking residues or modification notation, although standard FragPipe
    peptide.tsv files normally contain the unmodified peptide sequence.
    """
    if pd.isna(sequence):
        return ""

    return "".join(
        re.findall(r"[A-Z]", str(sequence).upper())
    )


def count_trypsin_p_missed_cleavages(sequence):
    """
    Count missed Trypsin/P cleavage sites in a fully enzymatic peptide.

    Trypsin/P cleavage was defined after K or R, including before proline.
    For a fully tryptic peptide, every internal K or R represents a missed
    cleavage. A terminal K or R is the expected peptide terminus and is
    therefore excluded from the count.
    """
    peptide = clean_peptide_sequence(sequence)

    if len(peptide) <= 1:
        return 0

    return sum(residue in {"K", "R"} for residue in peptide[:-1])


# ------------------------------------------------------------
# 4. Read and summarise every peptide.tsv file
# ------------------------------------------------------------

all_peptides = []
file_summary_records = []

required_columns = {"Peptide"}

for file_number, peptide_file in enumerate(peptide_files, start=1):

    print(
        f"[{file_number:02d}/{len(peptide_files):02d}] "
        f"Reading {peptide_file.name}"
    )

    peptide_data = pd.read_csv(
        peptide_file,
        sep="\t",
        low_memory=False
    )

    missing = required_columns.difference(peptide_data.columns)

    if missing:
        raise KeyError(
            f"{peptide_file.name} is missing required column(s): "
            f"{sorted(missing)}"
        )

    source, tissue, source_tissue = derive_source_tissue_labels(
        peptide_file.name
    )

    # --------------------------------------------------------
    # Exclude decoys and contaminants where columns are present
    # --------------------------------------------------------

    starting_rows = len(peptide_data)

    if "Is Decoy" in peptide_data.columns:
        peptide_data = peptide_data[
            ~peptide_data["Is Decoy"].fillna(False).astype(bool)
        ].copy()

    if "Is Contaminant" in peptide_data.columns:
        peptide_data = peptide_data[
            ~peptide_data["Is Contaminant"].fillna(False).astype(bool)
        ].copy()

    # --------------------------------------------------------
    # Standardise peptide sequence and length
    # --------------------------------------------------------

    peptide_data["Peptide_clean"] = (
        peptide_data["Peptide"]
        .map(clean_peptide_sequence)
    )

    peptide_data = peptide_data[
        peptide_data["Peptide_clean"].str.len() > 0
    ].copy()

    if "Peptide Length" in peptide_data.columns:
        peptide_data["Peptide_length"] = pd.to_numeric(
            peptide_data["Peptide Length"],
            errors="coerce"
        )
    else:
        peptide_data["Peptide_length"] = (
            peptide_data["Peptide_clean"].str.len()
        )

    # Replace missing reported lengths with sequence-derived lengths
    missing_length = peptide_data["Peptide_length"].isna()

    peptide_data.loc[
        missing_length,
        "Peptide_length"
    ] = peptide_data.loc[
        missing_length,
        "Peptide_clean"
    ].str.len()

    peptide_data["Peptide_length"] = (
        peptide_data["Peptide_length"]
        .astype(int)
    )

    # Confirm reported and sequence-derived lengths agree
    peptide_data["Sequence_length"] = (
        peptide_data["Peptide_clean"].str.len()
    )

    length_disagreement = (
        peptide_data["Peptide_length"]
        != peptide_data["Sequence_length"]
    )

    if length_disagreement.any():
        disagreement_count = int(length_disagreement.sum())

        print(
            f"  Warning: {disagreement_count:,} row(s) had a reported "
            "Peptide Length different from the cleaned sequence length. "
            "The reported FragPipe value was retained."
        )

    # --------------------------------------------------------
    # Calculate missed cleavages
    # --------------------------------------------------------

    peptide_data["Missed_cleavages"] = (
        peptide_data["Peptide_clean"]
        .map(count_trypsin_p_missed_cleavages)
        .astype(int)
    )

    # --------------------------------------------------------
    # Spectral-count field
    # --------------------------------------------------------

    if "Spectral Count" in peptide_data.columns:
        peptide_data["Spectral_count"] = (
            pd.to_numeric(
                peptide_data["Spectral Count"],
                errors="coerce"
            )
            .fillna(0)
        )
    else:
        peptide_data["Spectral_count"] = 1

    # --------------------------------------------------------
    # Add traceability metadata
    # --------------------------------------------------------

    peptide_data["Source"] = source
    peptide_data["Tissue"] = tissue
    peptide_data["Source_tissue"] = source_tissue
    peptide_data["Source_file"] = peptide_file.name

    # Threshold flags of direct relevance to reviewer comment
    peptide_data["More_than_2_missed_cleavages"] = (
        peptide_data["Missed_cleavages"] > 2
    )

    peptide_data["Longer_than_50_AA"] = (
        peptide_data["Peptide_length"] > 50
    )

    peptide_data["More_than_2_MC_and_longer_than_50_AA"] = (
        peptide_data["More_than_2_missed_cleavages"]
        & peptide_data["Longer_than_50_AA"]
    )

    # --------------------------------------------------------
    # Tissue summary
    # --------------------------------------------------------

    retained_rows = len(peptide_data)

    mc_gt2 = int(
        peptide_data["More_than_2_missed_cleavages"].sum()
    )

    length_gt50 = int(
        peptide_data["Longer_than_50_AA"].sum()
    )

    both = int(
        peptide_data[
            "More_than_2_MC_and_longer_than_50_AA"
        ].sum()
    )

    file_summary_records.append({
        "Source": source,
        "Tissue": tissue,
        "Source_tissue": source_tissue,
        "Source_file": peptide_file.name,
        "Input_rows": starting_rows,
        "Retained_nondecoy_noncontaminant_peptides": retained_rows,
        "Peptides_with_more_than_2_missed_cleavages": mc_gt2,
        "Percent_with_more_than_2_missed_cleavages": (
            100 * mc_gt2 / retained_rows if retained_rows else np.nan
        ),
        "Peptides_longer_than_50_AA": length_gt50,
        "Percent_longer_than_50_AA": (
            100 * length_gt50 / retained_rows if retained_rows else np.nan
        ),
        "Peptides_satisfying_both_criteria": both,
        "Percent_satisfying_both_criteria": (
            100 * both / retained_rows if retained_rows else np.nan
        ),
        "Maximum_missed_cleavages": (
            int(peptide_data["Missed_cleavages"].max())
            if retained_rows else np.nan
        ),
        "Maximum_peptide_length_AA": (
            int(peptide_data["Peptide_length"].max())
            if retained_rows else np.nan
        ),
        "Total_spectral_count": peptide_data["Spectral_count"].sum()
    })

    keep_columns = [
        "Source",
        "Tissue",
        "Source_tissue",
        "Source_file",
        "Peptide",
        "Peptide_clean",
        "Peptide_length",
        "Missed_cleavages",
        "Spectral_count",
        "More_than_2_missed_cleavages",
        "Longer_than_50_AA",
        "More_than_2_MC_and_longer_than_50_AA"
    ]

    for optional_column in [
        "Probability",
        "Qvalue",
        "Protein",
        "Mapped Proteins"
    ]:
        if optional_column in peptide_data.columns:
            keep_columns.append(optional_column)

    all_peptides.append(
        peptide_data[keep_columns].copy()
    )


# ------------------------------------------------------------
# 5. Combine all tissues
# ------------------------------------------------------------

combined_peptides = pd.concat(
    all_peptides,
    ignore_index=True
)

tissue_summary = pd.DataFrame(
    file_summary_records
)

print("\n===== COMBINED PEPTIDE SUMMARY =====")
print(
    "Source–tissue analyses: "
    f"{combined_peptides['Source_tissue'].nunique():,}"
)
if combined_peptides["Source_tissue"].nunique() != len(peptide_files):
    raise ValueError(
        "The number of unique source–tissue labels does not match "
        "the number of peptide.tsv files."
    )
print(f"Filtered peptide rows: {len(combined_peptides):,}")
print(
    "Peptides with >2 missed cleavages: "
    f"{combined_peptides['More_than_2_missed_cleavages'].sum():,}"
)
print(
    "Peptides longer than 50 AA: "
    f"{combined_peptides['Longer_than_50_AA'].sum():,}"
)
print(
    "Peptides satisfying both criteria: "
    f"{combined_peptides['More_than_2_MC_and_longer_than_50_AA'].sum():,}"
)
print(
    "Maximum missed cleavages observed: "
    f"{combined_peptides['Missed_cleavages'].max():,}"
)
print(
    "Maximum peptide length observed: "
    f"{combined_peptides['Peptide_length'].max():,} AA"
)


# ------------------------------------------------------------
# 6. Aggregate distributions
# ------------------------------------------------------------

missed_cleavage_distribution = (
    combined_peptides
    .groupby("Missed_cleavages", as_index=False)
    .agg(
        Unique_peptide_rows=("Peptide_clean", "size"),
        Spectral_count=("Spectral_count", "sum"),
        Source_tissue_analyses_with_at_least_one_peptide=(
            "Source_tissue",
            "nunique"
        )
    )
    .sort_values("Missed_cleavages")
)

# Ensure all categories 0–10 are represented
missed_cleavage_distribution = (
    missed_cleavage_distribution
    .set_index("Missed_cleavages")
    .reindex(range(0, 11), fill_value=0)
    .rename_axis("Missed_cleavages")
    .reset_index()
)

peptide_length_distribution = (
    combined_peptides
    .groupby("Peptide_length", as_index=False)
    .agg(
        Unique_peptide_rows=("Peptide_clean", "size"),
        Spectral_count=("Spectral_count", "sum"),
        Source_tissue_analyses_with_at_least_one_peptide=(
            "Source_tissue",
            "nunique"
        )
    )
    .sort_values("Peptide_length")
)


# ------------------------------------------------------------
# 7. Export tables
# ------------------------------------------------------------

combined_out = (
    tables_dir
    / "wheat_fragpipe_peptide_length_missed_cleavage_all_tissues_step4.csv"
)

tissue_summary_out = (
    tables_dir
    / "wheat_fragpipe_peptide_length_missed_cleavage_tissue_summary_step4.csv"
)

mc_distribution_out = (
    tables_dir
    / "wheat_fragpipe_missed_cleavage_distribution_step4.csv"
)

length_distribution_out = (
    tables_dir
    / "wheat_fragpipe_peptide_length_distribution_step4.csv"
)

threshold_peptides_out = (
    tables_dir
    / "wheat_fragpipe_peptides_exceeding_conventional_limits_step4.csv"
)

combined_peptides.to_csv(
    combined_out,
    index=False
)

tissue_summary.to_csv(
    tissue_summary_out,
    index=False
)

missed_cleavage_distribution.to_csv(
    mc_distribution_out,
    index=False
)

peptide_length_distribution.to_csv(
    length_distribution_out,
    index=False
)

combined_peptides.loc[
    combined_peptides["More_than_2_missed_cleavages"]
    | combined_peptides["Longer_than_50_AA"]
].to_csv(
    threshold_peptides_out,
    index=False
)

print("\nExported:")
print(f"  {combined_out}")
print(f"  {tissue_summary_out}")
print(f"  {mc_distribution_out}")
print(f"  {length_distribution_out}")
print(f"  {threshold_peptides_out}")


# ------------------------------------------------------------
# 8. Prepare independent tissue ordering for Panels B and D
# ------------------------------------------------------------

# Panel B: ascending order places the largest horizontal bar at the top
tissue_plot_mc = tissue_summary.sort_values(
    "Peptides_with_more_than_2_missed_cleavages",
    ascending=True
).reset_index(drop=True)

# Panel D: independently sort by number of peptides longer than 50 AA
tissue_plot_length = tissue_summary.sort_values(
    "Peptides_longer_than_50_AA",
    ascending=True
).reset_index(drop=True)

# ------------------------------------------------------------
# Brand colours
# ------------------------------------------------------------

DARK_PURPLE = "#3F007E"
PINK = "#FF3399"
GOLD = "#FFC000"
LIGHT_PURPLE = "#E6CDFF"

# ------------------------------------------------------------
# 9. Create four-panel supplementary figure
# ------------------------------------------------------------

fig, axes = plt.subplots(
    2,
    2,
    figsize=(17, 14)
)

# Panel A — aggregate missed-cleavage distribution
axes[0, 0].bar(
    missed_cleavage_distribution["Missed_cleavages"],
    missed_cleavage_distribution["Unique_peptide_rows"],
    color=DARK_PURPLE,
    edgecolor="black",
    linewidth=0.4
)

axes[0, 0].axvline(
    2.5,
    color=PINK,
    linestyle="--",
    linewidth=1.5
)

axes[0, 0].set_xlabel("Number of missed Trypsin/P cleavages")
axes[0, 0].set_ylabel("Filtered peptide identifications")
axes[0, 0].set_title(
    "A. Missed-cleavage distribution across all source-tissue analyses",
    loc="left",
    fontweight="bold"
)

axes[0, 0].set_xticks(range(0, 11))

# Log scale allows low-frequency high-cleavage categories to remain visible
axes[0, 0].set_yscale("log")

axes[0, 0].text(
    0.98,
    0.95,
    ">2 missed cleavages shown right of dashed line",
    transform=axes[0, 0].transAxes,
    horizontalalignment="right",
    verticalalignment="top",
    fontsize=9
)


# Panel B — tissue-level count with >2 missed cleavages
axes[0, 1].barh(
    tissue_plot_mc["Source_tissue"],
    tissue_plot_mc["Peptides_with_more_than_2_missed_cleavages"],
    color=PINK,
    edgecolor="black",
    linewidth=0.3
)

axes[0, 1].set_xlabel(
    "Filtered peptides with >2 missed cleavages"
)

axes[0, 1].set_ylabel("Source | tissue")

axes[0, 1].set_title(
    "B. Peptides with >2 missed cleavages",
    loc="left",
    fontweight="bold"
)

axes[0, 1].tick_params(
    axis="y",
    labelsize=7
)

axes[0, 1].ticklabel_format(
    axis="x",
    style="plain"
)

axes[0, 1].xaxis.set_major_formatter(
    StrMethodFormatter("{x:,.0f}")
)

# Panel C — aggregate peptide-length distribution
axes[1, 0].bar(
    peptide_length_distribution["Peptide_length"],
    peptide_length_distribution["Unique_peptide_rows"],
    width=0.9,
    color=GOLD,
    edgecolor="black",
    linewidth=0.3
)

axes[1, 0].axvline(
    50.5,
    color=PINK,
    linestyle="--",
    linewidth=1.5
)

axes[1, 0].set_xlabel("Peptide length (amino acids)")
axes[1, 0].set_ylabel("Filtered peptide identifications")

axes[1, 0].set_title(
    "C. Peptide-length distribution across all source–tissue analyses",
    loc="left",
    fontweight="bold"
)

axes[1, 0].set_yscale("log")

axes[1, 0].text(
    0.98,
    0.95,
    ">50 AA shown right of dashed line",
    transform=axes[1, 0].transAxes,
    horizontalalignment="right",
    verticalalignment="top",
    fontsize=9
)


# Panel D — tissue-level count longer than 50 AA
axes[1, 1].barh(
    tissue_plot_length["Source_tissue"],
    tissue_plot_length["Peptides_longer_than_50_AA"],
    color=LIGHT_PURPLE,
    edgecolor="black",
    linewidth=0.3
)

axes[1, 1].set_xlabel(
    "Filtered peptides longer than 50 AA"
)

axes[1, 1].set_ylabel("Source | tissue")

axes[1, 1].set_title(
    "D. Peptides longer than 50 amino acids",
    loc="left",
    fontweight="bold"
)

axes[1, 1].tick_params(
    axis="y",
    labelsize=7
)

axes[1, 1].ticklabel_format(
    axis="x",
    style="plain"
)

axes[1, 1].xaxis.set_major_formatter(
    StrMethodFormatter("{x:,.0f}")
)


# General figure formatting
for axis in axes.flat:
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)

fig.suptitle(
    "Empirical recovery of peptides enabled by permissive "
    "FragPipe digestion and peptide-length limits",
    fontsize=16,
    fontweight="bold",
    y=0.995
)

fig.tight_layout(
    rect=[0, 0, 1, 0.975]
)


# ------------------------------------------------------------
# 10. Save publication-quality figure
# ------------------------------------------------------------

figure_png = (
    figures_dir
    / "step4_FragPipe_missed-cleavage_peptide-length_distributions.png"
)

figure_pdf = (
    figures_dir
    / "step4_FragPipe_missed-cleavage_peptide-length_distributions.pdf"
)

fig.savefig(
    figure_png,
    dpi=600,
    bbox_inches="tight"
)

fig.savefig(
    figure_pdf,
    bbox_inches="tight"
)

plt.show()

print("\nFigure exported:")
print(f"  {figure_png}")
print(f"  {figure_pdf}")


# ------------------------------------------------------------
# 11. Display key summary tables
# ------------------------------------------------------------

display(
    tissue_summary.sort_values(
        "Peptides_with_more_than_2_missed_cleavages",
        ascending=False
    )
)

display(
    missed_cleavage_distribution
)

display(
    peptide_length_distribution.tail(25)
)
```

    Peptide reports found: 32
      FragPipe_Duncan_PXD004720_anther_peptide.tsv
      FragPipe_Duncan_PXD004720_boot_peptide.tsv
      FragPipe_Duncan_PXD004720_coleoptile_peptide.tsv
      FragPipe_Duncan_PXD004720_embryo_peptide.tsv
      FragPipe_Duncan_PXD004720_endosperm_peptide.tsv
      ...
    [01/32] Reading FragPipe_Duncan_PXD004720_anther_peptide.tsv
    [02/32] Reading FragPipe_Duncan_PXD004720_boot_peptide.tsv
    [03/32] Reading FragPipe_Duncan_PXD004720_coleoptile_peptide.tsv
    [04/32] Reading FragPipe_Duncan_PXD004720_embryo_peptide.tsv
    [05/32] Reading FragPipe_Duncan_PXD004720_endosperm_peptide.tsv
    [06/32] Reading FragPipe_Duncan_PXD004720_glume_peptide.tsv
    [07/32] Reading FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide.tsv
    [08/32] Reading FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide.tsv
    [09/32] Reading FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide.tsv
    [10/32] Reading FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide.tsv
    [11/32] Reading FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide.tsv
    [12/32] Reading FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide.tsv
    [13/32] Reading FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide.tsv
    [14/32] Reading FragPipe_Duncan_PXD004720_leaf-flag-young_peptide.tsv
    [15/32] Reading FragPipe_Duncan_PXD004720_lemma_peptide.tsv
    [16/32] Reading FragPipe_Duncan_PXD004720_node-secretion_peptide.tsv
    [17/32] Reading FragPipe_Duncan_PXD004720_node_peptide.tsv
    [18/32] Reading FragPipe_Duncan_PXD004720_palea_peptide.tsv
    [19/32] Reading FragPipe_Duncan_PXD004720_pericarp_peptide.tsv
    [20/32] Reading FragPipe_Duncan_PXD004720_pollen_peptide.tsv
    [21/32] Reading FragPipe_Duncan_PXD004720_rachilla_peptide.tsv
    [22/32] Reading FragPipe_Duncan_PXD004720_radicle_peptide.tsv
    [23/32] Reading FragPipe_Duncan_PXD004720_root-mature_peptide.tsv
    [24/32] Reading FragPipe_Duncan_PXD004720_root-secretion_peptide.tsv
    [25/32] Reading FragPipe_Duncan_PXD004720_root-tip_peptide.tsv
    [26/32] Reading FragPipe_Duncan_PXD004720_root-vasculature_peptide.tsv
    [27/32] Reading FragPipe_Duncan_PXD004720_spike-immature_peptide.tsv
    [28/32] Reading FragPipe_Duncan_PXD004720_stem_peptide.tsv
    [29/32] Reading FragPipe_Liu_PXD050500_coleoptile_peptide.tsv
    [30/32] Reading FragPipe_Liu_PXD050500_node_peptide.tsv
    [31/32] Reading FragPipe_Liu_PXD050500_radicle_peptide.tsv
    [32/32] Reading FragPipe_Vincent_MSV000090572_stored-grain_peptide.tsv
    
    ===== COMBINED PEPTIDE SUMMARY =====
    Source–tissue analyses: 32
    Filtered peptide rows: 2,229,724
    Peptides with >2 missed cleavages: 61,546
    Peptides longer than 50 AA: 1,431
    Peptides satisfying both criteria: 773
    Maximum missed cleavages observed: 10
    Maximum peptide length observed: 87 AA
    
    Exported:
      python_outputs\tables\wheat_fragpipe_peptide_length_missed_cleavage_all_tissues_step4.csv
      python_outputs\tables\wheat_fragpipe_peptide_length_missed_cleavage_tissue_summary_step4.csv
      python_outputs\tables\wheat_fragpipe_missed_cleavage_distribution_step4.csv
      python_outputs\tables\wheat_fragpipe_peptide_length_distribution_step4.csv
      python_outputs\tables\wheat_fragpipe_peptides_exceeding_conventional_limits_step4.csv
    


    
![png](output_5_1.png)
    


    
    Figure exported:
      python_outputs\figures\step4_FragPipe_missed-cleavage_peptide-length_distributions.png
      python_outputs\figures\step4_FragPipe_missed-cleavage_peptide-length_distributions.pdf
    


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
      <th>Source_tissue</th>
      <th>Source_file</th>
      <th>Input_rows</th>
      <th>Retained_nondecoy_noncontaminant_peptides</th>
      <th>Peptides_with_more_than_2_missed_cleavages</th>
      <th>Percent_with_more_than_2_missed_cleavages</th>
      <th>Peptides_longer_than_50_AA</th>
      <th>Percent_longer_than_50_AA</th>
      <th>Peptides_satisfying_both_criteria</th>
      <th>Percent_satisfying_both_criteria</th>
      <th>Maximum_missed_cleavages</th>
      <th>Maximum_peptide_length_AA</th>
      <th>Total_spectral_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>29</th>
      <td>PXD050500</td>
      <td>node</td>
      <td>PXD050500 | node</td>
      <td>FragPipe_Liu_PXD050500_node_peptide.tsv</td>
      <td>596437</td>
      <td>596437</td>
      <td>15804</td>
      <td>2.649735</td>
      <td>301</td>
      <td>0.050466</td>
      <td>137</td>
      <td>0.022970</td>
      <td>10</td>
      <td>73</td>
      <td>3839535</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD050500</td>
      <td>coleoptile</td>
      <td>PXD050500 | coleoptile</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide.tsv</td>
      <td>583184</td>
      <td>583184</td>
      <td>14721</td>
      <td>2.524246</td>
      <td>165</td>
      <td>0.028293</td>
      <td>64</td>
      <td>0.010974</td>
      <td>10</td>
      <td>74</td>
      <td>4407357</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD050500</td>
      <td>radicle</td>
      <td>PXD050500 | radicle</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide.tsv</td>
      <td>333400</td>
      <td>333400</td>
      <td>5371</td>
      <td>1.610978</td>
      <td>142</td>
      <td>0.042591</td>
      <td>59</td>
      <td>0.017696</td>
      <td>10</td>
      <td>75</td>
      <td>2245698</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>spike-immature</td>
      <td>PXD004720 | spike-immature</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>36414</td>
      <td>36414</td>
      <td>3108</td>
      <td>8.535179</td>
      <td>83</td>
      <td>0.227934</td>
      <td>61</td>
      <td>0.167518</td>
      <td>10</td>
      <td>74</td>
      <td>157490</td>
    </tr>
    <tr>
      <th>0</th>
      <td>PXD004720</td>
      <td>anther</td>
      <td>PXD004720 | anther</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide.tsv</td>
      <td>34203</td>
      <td>34203</td>
      <td>2368</td>
      <td>6.923369</td>
      <td>65</td>
      <td>0.190042</td>
      <td>50</td>
      <td>0.146186</td>
      <td>10</td>
      <td>67</td>
      <td>164443</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>palea</td>
      <td>PXD004720 | palea</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide.tsv</td>
      <td>21774</td>
      <td>21774</td>
      <td>2186</td>
      <td>10.039497</td>
      <td>72</td>
      <td>0.330670</td>
      <td>51</td>
      <td>0.234224</td>
      <td>10</td>
      <td>77</td>
      <td>106814</td>
    </tr>
    <tr>
      <th>31</th>
      <td>MSV000090572</td>
      <td>stored-grain</td>
      <td>MSV000090572 | stored-grain</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>9343</td>
      <td>9343</td>
      <td>1801</td>
      <td>19.276464</td>
      <td>62</td>
      <td>0.663598</td>
      <td>47</td>
      <td>0.503050</td>
      <td>10</td>
      <td>65</td>
      <td>33273</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>root-secretion</td>
      <td>PXD004720 | root-secretion</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>21329</td>
      <td>21329</td>
      <td>1757</td>
      <td>8.237611</td>
      <td>26</td>
      <td>0.121900</td>
      <td>20</td>
      <td>0.093769</td>
      <td>10</td>
      <td>64</td>
      <td>37901</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>rachilla</td>
      <td>PXD004720 | rachilla</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide.tsv</td>
      <td>31213</td>
      <td>31213</td>
      <td>1659</td>
      <td>5.315093</td>
      <td>53</td>
      <td>0.169801</td>
      <td>34</td>
      <td>0.108929</td>
      <td>10</td>
      <td>81</td>
      <td>147229</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>radicle</td>
      <td>PXD004720 | radicle</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide.tsv</td>
      <td>39704</td>
      <td>39704</td>
      <td>1486</td>
      <td>3.742696</td>
      <td>39</td>
      <td>0.098227</td>
      <td>18</td>
      <td>0.045335</td>
      <td>9</td>
      <td>66</td>
      <td>152610</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>root-mature</td>
      <td>PXD004720 | root-mature</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide.tsv</td>
      <td>21390</td>
      <td>21390</td>
      <td>1434</td>
      <td>6.704067</td>
      <td>12</td>
      <td>0.056101</td>
      <td>8</td>
      <td>0.037401</td>
      <td>10</td>
      <td>61</td>
      <td>57758</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>root-tip</td>
      <td>PXD004720 | root-tip</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide.tsv</td>
      <td>38681</td>
      <td>38681</td>
      <td>1351</td>
      <td>3.492671</td>
      <td>47</td>
      <td>0.121507</td>
      <td>29</td>
      <td>0.074972</td>
      <td>10</td>
      <td>68</td>
      <td>152978</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>glume</td>
      <td>PXD004720 | glume</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide.tsv</td>
      <td>28683</td>
      <td>28683</td>
      <td>1275</td>
      <td>4.445142</td>
      <td>77</td>
      <td>0.268452</td>
      <td>50</td>
      <td>0.174319</td>
      <td>10</td>
      <td>78</td>
      <td>147049</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>pericarp</td>
      <td>PXD004720 | pericarp</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide.tsv</td>
      <td>28448</td>
      <td>28448</td>
      <td>1081</td>
      <td>3.799916</td>
      <td>70</td>
      <td>0.246063</td>
      <td>35</td>
      <td>0.123031</td>
      <td>10</td>
      <td>74</td>
      <td>122800</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD004720</td>
      <td>coleoptile</td>
      <td>PXD004720 | coleoptile</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide.tsv</td>
      <td>41126</td>
      <td>41126</td>
      <td>885</td>
      <td>2.151923</td>
      <td>30</td>
      <td>0.072947</td>
      <td>18</td>
      <td>0.043768</td>
      <td>9</td>
      <td>65</td>
      <td>159353</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>root-vasculature</td>
      <td>PXD004720 | root-vasculature</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>20911</td>
      <td>20911</td>
      <td>737</td>
      <td>3.524461</td>
      <td>7</td>
      <td>0.033475</td>
      <td>1</td>
      <td>0.004782</td>
      <td>9</td>
      <td>62</td>
      <td>80342</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>lemma</td>
      <td>PXD004720 | lemma</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide.tsv</td>
      <td>29842</td>
      <td>29842</td>
      <td>594</td>
      <td>1.990483</td>
      <td>26</td>
      <td>0.087126</td>
      <td>18</td>
      <td>0.060318</td>
      <td>10</td>
      <td>71</td>
      <td>131599</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>node</td>
      <td>PXD004720 | node</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide.tsv</td>
      <td>21508</td>
      <td>21508</td>
      <td>462</td>
      <td>2.148038</td>
      <td>4</td>
      <td>0.018598</td>
      <td>2</td>
      <td>0.009299</td>
      <td>8</td>
      <td>63</td>
      <td>69197</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720</td>
      <td>boot</td>
      <td>PXD004720 | boot</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide.tsv</td>
      <td>3644</td>
      <td>3644</td>
      <td>326</td>
      <td>8.946213</td>
      <td>19</td>
      <td>0.521405</td>
      <td>11</td>
      <td>0.301866</td>
      <td>9</td>
      <td>78</td>
      <td>6071</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>grain-zadoks-71</td>
      <td>PXD004720 | grain-zadoks-71</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>35990</td>
      <td>35990</td>
      <td>315</td>
      <td>0.875243</td>
      <td>3</td>
      <td>0.008336</td>
      <td>1</td>
      <td>0.002779</td>
      <td>8</td>
      <td>57</td>
      <td>133472</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>grain-zadoks-70</td>
      <td>PXD004720 | grain-zadoks-70</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>26229</td>
      <td>26229</td>
      <td>290</td>
      <td>1.105646</td>
      <td>27</td>
      <td>0.102939</td>
      <td>14</td>
      <td>0.053376</td>
      <td>9</td>
      <td>70</td>
      <td>104545</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>endosperm</td>
      <td>PXD004720 | endosperm</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide.tsv</td>
      <td>20174</td>
      <td>20174</td>
      <td>284</td>
      <td>1.407753</td>
      <td>27</td>
      <td>0.133836</td>
      <td>10</td>
      <td>0.049569</td>
      <td>10</td>
      <td>87</td>
      <td>77601</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>stem</td>
      <td>PXD004720 | stem</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide.tsv</td>
      <td>14389</td>
      <td>14389</td>
      <td>277</td>
      <td>1.925082</td>
      <td>2</td>
      <td>0.013900</td>
      <td>2</td>
      <td>0.013900</td>
      <td>10</td>
      <td>64</td>
      <td>37757</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>grain-zadoks-87</td>
      <td>PXD004720 | grain-zadoks-87</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>24674</td>
      <td>24674</td>
      <td>275</td>
      <td>1.114534</td>
      <td>13</td>
      <td>0.052687</td>
      <td>3</td>
      <td>0.012159</td>
      <td>10</td>
      <td>66</td>
      <td>91205</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>pollen</td>
      <td>PXD004720 | pollen</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide.tsv</td>
      <td>13593</td>
      <td>13593</td>
      <td>259</td>
      <td>1.905392</td>
      <td>27</td>
      <td>0.198632</td>
      <td>9</td>
      <td>0.066211</td>
      <td>10</td>
      <td>78</td>
      <td>61206</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>node-secretion</td>
      <td>PXD004720 | node-secretion</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>34194</td>
      <td>34194</td>
      <td>242</td>
      <td>0.707727</td>
      <td>4</td>
      <td>0.011698</td>
      <td>2</td>
      <td>0.005849</td>
      <td>9</td>
      <td>79</td>
      <td>85168</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>leaf-flag-senescing</td>
      <td>PXD004720 | leaf-flag-senescing</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>11394</td>
      <td>11394</td>
      <td>239</td>
      <td>2.097595</td>
      <td>1</td>
      <td>0.008777</td>
      <td>1</td>
      <td>0.008777</td>
      <td>7</td>
      <td>56</td>
      <td>29276</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>leaf-flag-mature</td>
      <td>PXD004720 | leaf-flag-mature</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>29941</td>
      <td>29941</td>
      <td>218</td>
      <td>0.728099</td>
      <td>3</td>
      <td>0.010020</td>
      <td>2</td>
      <td>0.006680</td>
      <td>7</td>
      <td>66</td>
      <td>79872</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD004720</td>
      <td>embryo</td>
      <td>PXD004720 | embryo</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide.tsv</td>
      <td>2868</td>
      <td>2868</td>
      <td>202</td>
      <td>7.043236</td>
      <td>9</td>
      <td>0.313808</td>
      <td>5</td>
      <td>0.174338</td>
      <td>8</td>
      <td>62</td>
      <td>4603</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>leaf-flag-young</td>
      <td>PXD004720 | leaf-flag-young</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>23441</td>
      <td>23441</td>
      <td>195</td>
      <td>0.831876</td>
      <td>6</td>
      <td>0.025596</td>
      <td>6</td>
      <td>0.025596</td>
      <td>8</td>
      <td>77</td>
      <td>60972</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>grain-zadoks-83</td>
      <td>PXD004720 | grain-zadoks-83</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>24051</td>
      <td>24051</td>
      <td>184</td>
      <td>0.765041</td>
      <td>8</td>
      <td>0.033263</td>
      <td>5</td>
      <td>0.020789</td>
      <td>9</td>
      <td>73</td>
      <td>86569</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>grain-zadoks-75</td>
      <td>PXD004720 | grain-zadoks-75</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>27552</td>
      <td>27552</td>
      <td>160</td>
      <td>0.580720</td>
      <td>1</td>
      <td>0.003630</td>
      <td>0</td>
      <td>0.000000</td>
      <td>9</td>
      <td>51</td>
      <td>93099</td>
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
      <th>Missed_cleavages</th>
      <th>Unique_peptide_rows</th>
      <th>Spectral_count</th>
      <th>Source_tissue_analyses_with_at_least_one_peptide</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1428412</td>
      <td>9559050</td>
      <td>32</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>572901</td>
      <td>2955097</td>
      <td>32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>166865</td>
      <td>507672</td>
      <td>32</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>43528</td>
      <td>106296</td>
      <td>32</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>11362</td>
      <td>26547</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>3649</td>
      <td>6552</td>
      <td>32</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>1486</td>
      <td>1926</td>
      <td>32</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>730</td>
      <td>852</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>435</td>
      <td>474</td>
      <td>29</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>215</td>
      <td>224</td>
      <td>26</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>141</td>
      <td>152</td>
      <td>18</td>
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
      <th>Peptide_length</th>
      <th>Unique_peptide_rows</th>
      <th>Spectral_count</th>
      <th>Source_tissue_analyses_with_at_least_one_peptide</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>57</td>
      <td>85</td>
      <td>290</td>
      <td>21</td>
    </tr>
    <tr>
      <th>51</th>
      <td>58</td>
      <td>59</td>
      <td>270</td>
      <td>15</td>
    </tr>
    <tr>
      <th>52</th>
      <td>59</td>
      <td>47</td>
      <td>97</td>
      <td>12</td>
    </tr>
    <tr>
      <th>53</th>
      <td>60</td>
      <td>42</td>
      <td>98</td>
      <td>18</td>
    </tr>
    <tr>
      <th>54</th>
      <td>61</td>
      <td>54</td>
      <td>1366</td>
      <td>22</td>
    </tr>
    <tr>
      <th>55</th>
      <td>62</td>
      <td>41</td>
      <td>386</td>
      <td>15</td>
    </tr>
    <tr>
      <th>56</th>
      <td>63</td>
      <td>27</td>
      <td>130</td>
      <td>15</td>
    </tr>
    <tr>
      <th>57</th>
      <td>64</td>
      <td>41</td>
      <td>206</td>
      <td>17</td>
    </tr>
    <tr>
      <th>58</th>
      <td>65</td>
      <td>14</td>
      <td>18</td>
      <td>10</td>
    </tr>
    <tr>
      <th>59</th>
      <td>66</td>
      <td>28</td>
      <td>166</td>
      <td>17</td>
    </tr>
    <tr>
      <th>60</th>
      <td>67</td>
      <td>3</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>61</th>
      <td>68</td>
      <td>6</td>
      <td>6</td>
      <td>5</td>
    </tr>
    <tr>
      <th>62</th>
      <td>69</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>63</th>
      <td>70</td>
      <td>3</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>64</th>
      <td>71</td>
      <td>3</td>
      <td>9</td>
      <td>3</td>
    </tr>
    <tr>
      <th>65</th>
      <td>72</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>66</th>
      <td>73</td>
      <td>4</td>
      <td>26</td>
      <td>4</td>
    </tr>
    <tr>
      <th>67</th>
      <td>74</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>68</th>
      <td>75</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>69</th>
      <td>76</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>70</th>
      <td>77</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>71</th>
      <td>78</td>
      <td>3</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>72</th>
      <td>79</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>73</th>
      <td>81</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>74</th>
      <td>87</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>


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


# Step 10 — Translation validation of annotation-guided peptide genome projections

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

- `wheat_projection_validation_stratified100percent_step10.csv`
- `wheat_projection_validation_100%_summary_step10.csv`
- `wheat_projection_validation_100%_tissue_summary_step10.csv`


```python
# # install python library
# !pip install pyfaidx
```


```python
# ============================================================
# Step 10 — Validate peptide genome projections by translation (takes 30 min)
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

sample_fraction = 1 # to test on a portion of the data, lower this number (e.g. 0.1 for 10% of the data)
chunk_size = 30_000 # reduce this for low performance computer
random_seed = 42

validation_out = tables_dir / "wheat_projection_validation_stratified100percent_step10.csv"
summary_out = tables_dir / "wheat_projection_validation_100%_summary_step10.csv"
tissue_summary_out = tables_dir / "wheat_projection_validation_100%_tissue_summary_step10.csv"

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
    "GeneID",
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
    "Projection_status",
    "Probability",
    "Peptide_intron_gapped",
    "Peptide_intron_gapped_compact",
    "Tissues_count"
]

# -----------------------------
# 6. Open genome FASTA
# -----------------------------
print("\nOpening indexed genome FASTA...")

# Use rebuild=True only the first time. Afterwards, rebuild=False is faster.
genome = Fasta(str(genome_fasta), rebuild=False)

print(f"Genome sequences available: {len(genome.keys()):,}")

# -----------------------------
# 7. Validate stratified 100% per projection file
# -----------------------------
rng = np.random.default_rng(random_seed)

overall_records = []
tissue_summary_records = []
header_written = False

print("\nValidating stratified 100% sample per tissue/source...")

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

        # Stratified 100% sample within this file/chunk
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
    {"Metric": "Sampling strategy", "Value": "100% stratified per projection file/source-tissue"},
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
    
    Validating stratified 100% sample per tissue/source...
    
    [1/32] FragPipe_Duncan_PXD004720_anther_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 14,365 | cumulative sampled 164,365
    
    [2/32] FragPipe_Duncan_PXD004720_boot_peptide_genome_projection.csv
      Chunk 1: sampled 13,227 | cumulative sampled 13,227
    
    [3/32] FragPipe_Duncan_PXD004720_coleoptile_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 24,476 | cumulative sampled 204,476
    
    [4/32] FragPipe_Duncan_PXD004720_embryo_peptide_genome_projection.csv
      Chunk 1: sampled 8,852 | cumulative sampled 8,852
    
    [5/32] FragPipe_Duncan_PXD004720_endosperm_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 12,830 | cumulative sampled 102,830
    
    [6/32] FragPipe_Duncan_PXD004720_glume_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 25,133 | cumulative sampled 145,133
    
    [7/32] FragPipe_Duncan_PXD004720_grain-zadoks-70_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 6,195 | cumulative sampled 126,195
    
    [8/32] FragPipe_Duncan_PXD004720_grain-zadoks-71_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 29,725 | cumulative sampled 179,725
    
    [9/32] FragPipe_Duncan_PXD004720_grain-zadoks-75_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 12,701 | cumulative sampled 132,701
    
    [10/32] FragPipe_Duncan_PXD004720_grain-zadoks-83_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 23,203 | cumulative sampled 113,203
    
    [11/32] FragPipe_Duncan_PXD004720_grain-zadoks-87_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 21,792 | cumulative sampled 111,792
    
    [12/32] FragPipe_Duncan_PXD004720_leaf-flag-mature_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 25,632 | cumulative sampled 145,632
    
    [13/32] FragPipe_Duncan_PXD004720_leaf-flag-senescing_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 16,200 | cumulative sampled 46,200
    
    [14/32] FragPipe_Duncan_PXD004720_leaf-flag-young_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 821 | cumulative sampled 120,821
    
    [15/32] FragPipe_Duncan_PXD004720_lemma_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 27,618 | cumulative sampled 147,618
    
    [16/32] FragPipe_Duncan_PXD004720_node-secretion_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 19,675 | cumulative sampled 169,675
    
    [17/32] FragPipe_Duncan_PXD004720_node_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 9,823 | cumulative sampled 99,823
    
    [18/32] FragPipe_Duncan_PXD004720_palea_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 26,936 | cumulative sampled 116,936
    
    [19/32] FragPipe_Duncan_PXD004720_pericarp_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 11,215 | cumulative sampled 131,215
    
    [20/32] FragPipe_Duncan_PXD004720_pollen_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 14,698 | cumulative sampled 74,698
    
    [21/32] FragPipe_Duncan_PXD004720_rachilla_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 10,204 | cumulative sampled 160,204
    
    [22/32] FragPipe_Duncan_PXD004720_radicle_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 14,694 | cumulative sampled 194,694
    
    [23/32] FragPipe_Duncan_PXD004720_root-mature_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 7,188 | cumulative sampled 97,188
    
    [24/32] FragPipe_Duncan_PXD004720_root-secretion_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 10,639 | cumulative sampled 100,639
    
    [25/32] FragPipe_Duncan_PXD004720_root-tip_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 11,943 | cumulative sampled 191,943
    
    [26/32] FragPipe_Duncan_PXD004720_root-vasculature_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 21,831 | cumulative sampled 111,831
    
    [27/32] FragPipe_Duncan_PXD004720_spike-immature_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 8,826 | cumulative sampled 188,826
    
    [28/32] FragPipe_Duncan_PXD004720_stem_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 734 | cumulative sampled 60,734
    
    [29/32] FragPipe_Liu_PXD050500_coleoptile_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 30,000 | cumulative sampled 210,000
      Chunk 8: sampled 30,000 | cumulative sampled 240,000
      Chunk 9: sampled 30,000 | cumulative sampled 270,000
      Chunk 10: sampled 30,000 | cumulative sampled 300,000
      Chunk 11: sampled 30,000 | cumulative sampled 330,000
      Chunk 12: sampled 30,000 | cumulative sampled 360,000
      Chunk 13: sampled 30,000 | cumulative sampled 390,000
      Chunk 14: sampled 30,000 | cumulative sampled 420,000
      Chunk 15: sampled 30,000 | cumulative sampled 450,000
      Chunk 16: sampled 30,000 | cumulative sampled 480,000
      Chunk 17: sampled 30,000 | cumulative sampled 510,000
      Chunk 18: sampled 30,000 | cumulative sampled 540,000
      Chunk 19: sampled 30,000 | cumulative sampled 570,000
      Chunk 20: sampled 30,000 | cumulative sampled 600,000
      Chunk 21: sampled 30,000 | cumulative sampled 630,000
      Chunk 22: sampled 30,000 | cumulative sampled 660,000
      Chunk 23: sampled 30,000 | cumulative sampled 690,000
      Chunk 24: sampled 30,000 | cumulative sampled 720,000
      Chunk 25: sampled 30,000 | cumulative sampled 750,000
      Chunk 26: sampled 30,000 | cumulative sampled 780,000
      Chunk 27: sampled 30,000 | cumulative sampled 810,000
      Chunk 28: sampled 30,000 | cumulative sampled 840,000
      Chunk 29: sampled 30,000 | cumulative sampled 870,000
      Chunk 30: sampled 30,000 | cumulative sampled 900,000
      Chunk 31: sampled 30,000 | cumulative sampled 930,000
      Chunk 32: sampled 30,000 | cumulative sampled 960,000
      Chunk 33: sampled 30,000 | cumulative sampled 990,000
      Chunk 34: sampled 30,000 | cumulative sampled 1,020,000
      Chunk 35: sampled 30,000 | cumulative sampled 1,050,000
      Chunk 36: sampled 30,000 | cumulative sampled 1,080,000
      Chunk 37: sampled 30,000 | cumulative sampled 1,110,000
      Chunk 38: sampled 30,000 | cumulative sampled 1,140,000
      Chunk 39: sampled 30,000 | cumulative sampled 1,170,000
      Chunk 40: sampled 30,000 | cumulative sampled 1,200,000
      Chunk 41: sampled 30,000 | cumulative sampled 1,230,000
      Chunk 42: sampled 30,000 | cumulative sampled 1,260,000
      Chunk 43: sampled 30,000 | cumulative sampled 1,290,000
      Chunk 44: sampled 30,000 | cumulative sampled 1,320,000
      Chunk 45: sampled 30,000 | cumulative sampled 1,350,000
      Chunk 46: sampled 30,000 | cumulative sampled 1,380,000
      Chunk 47: sampled 30,000 | cumulative sampled 1,410,000
      Chunk 48: sampled 30,000 | cumulative sampled 1,440,000
      Chunk 49: sampled 30,000 | cumulative sampled 1,470,000
      Chunk 50: sampled 30,000 | cumulative sampled 1,500,000
      Chunk 51: sampled 30,000 | cumulative sampled 1,530,000
      Chunk 52: sampled 30,000 | cumulative sampled 1,560,000
      Chunk 53: sampled 30,000 | cumulative sampled 1,590,000
      Chunk 54: sampled 30,000 | cumulative sampled 1,620,000
      Chunk 55: sampled 30,000 | cumulative sampled 1,650,000
      Chunk 56: sampled 30,000 | cumulative sampled 1,680,000
      Chunk 57: sampled 30,000 | cumulative sampled 1,710,000
      Chunk 58: sampled 30,000 | cumulative sampled 1,740,000
      Chunk 59: sampled 30,000 | cumulative sampled 1,770,000
      Chunk 60: sampled 30,000 | cumulative sampled 1,800,000
      Chunk 61: sampled 30,000 | cumulative sampled 1,830,000
      Chunk 62: sampled 20,136 | cumulative sampled 1,850,136
    
    [30/32] FragPipe_Liu_PXD050500_node_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 30,000 | cumulative sampled 210,000
      Chunk 8: sampled 30,000 | cumulative sampled 240,000
      Chunk 9: sampled 30,000 | cumulative sampled 270,000
      Chunk 10: sampled 30,000 | cumulative sampled 300,000
      Chunk 11: sampled 30,000 | cumulative sampled 330,000
      Chunk 12: sampled 30,000 | cumulative sampled 360,000
      Chunk 13: sampled 30,000 | cumulative sampled 390,000
      Chunk 14: sampled 30,000 | cumulative sampled 420,000
      Chunk 15: sampled 30,000 | cumulative sampled 450,000
      Chunk 16: sampled 30,000 | cumulative sampled 480,000
      Chunk 17: sampled 30,000 | cumulative sampled 510,000
      Chunk 18: sampled 30,000 | cumulative sampled 540,000
      Chunk 19: sampled 30,000 | cumulative sampled 570,000
      Chunk 20: sampled 30,000 | cumulative sampled 600,000
      Chunk 21: sampled 30,000 | cumulative sampled 630,000
      Chunk 22: sampled 30,000 | cumulative sampled 660,000
      Chunk 23: sampled 30,000 | cumulative sampled 690,000
      Chunk 24: sampled 30,000 | cumulative sampled 720,000
      Chunk 25: sampled 30,000 | cumulative sampled 750,000
      Chunk 26: sampled 30,000 | cumulative sampled 780,000
      Chunk 27: sampled 30,000 | cumulative sampled 810,000
      Chunk 28: sampled 30,000 | cumulative sampled 840,000
      Chunk 29: sampled 30,000 | cumulative sampled 870,000
      Chunk 30: sampled 30,000 | cumulative sampled 900,000
      Chunk 31: sampled 30,000 | cumulative sampled 930,000
      Chunk 32: sampled 30,000 | cumulative sampled 960,000
      Chunk 33: sampled 30,000 | cumulative sampled 990,000
      Chunk 34: sampled 30,000 | cumulative sampled 1,020,000
      Chunk 35: sampled 30,000 | cumulative sampled 1,050,000
      Chunk 36: sampled 30,000 | cumulative sampled 1,080,000
      Chunk 37: sampled 30,000 | cumulative sampled 1,110,000
      Chunk 38: sampled 30,000 | cumulative sampled 1,140,000
      Chunk 39: sampled 30,000 | cumulative sampled 1,170,000
      Chunk 40: sampled 30,000 | cumulative sampled 1,200,000
      Chunk 41: sampled 30,000 | cumulative sampled 1,230,000
      Chunk 42: sampled 30,000 | cumulative sampled 1,260,000
      Chunk 43: sampled 30,000 | cumulative sampled 1,290,000
      Chunk 44: sampled 30,000 | cumulative sampled 1,320,000
      Chunk 45: sampled 30,000 | cumulative sampled 1,350,000
      Chunk 46: sampled 30,000 | cumulative sampled 1,380,000
      Chunk 47: sampled 30,000 | cumulative sampled 1,410,000
      Chunk 48: sampled 30,000 | cumulative sampled 1,440,000
      Chunk 49: sampled 30,000 | cumulative sampled 1,470,000
      Chunk 50: sampled 30,000 | cumulative sampled 1,500,000
      Chunk 51: sampled 30,000 | cumulative sampled 1,530,000
      Chunk 52: sampled 30,000 | cumulative sampled 1,560,000
      Chunk 53: sampled 30,000 | cumulative sampled 1,590,000
      Chunk 54: sampled 30,000 | cumulative sampled 1,620,000
      Chunk 55: sampled 30,000 | cumulative sampled 1,650,000
      Chunk 56: sampled 30,000 | cumulative sampled 1,680,000
      Chunk 57: sampled 30,000 | cumulative sampled 1,710,000
      Chunk 58: sampled 30,000 | cumulative sampled 1,740,000
      Chunk 59: sampled 30,000 | cumulative sampled 1,770,000
      Chunk 60: sampled 30,000 | cumulative sampled 1,800,000
      Chunk 61: sampled 30,000 | cumulative sampled 1,830,000
      Chunk 62: sampled 30,000 | cumulative sampled 1,860,000
      Chunk 63: sampled 26,922 | cumulative sampled 1,886,922
    
    [31/32] FragPipe_Liu_PXD050500_radicle_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 30,000 | cumulative sampled 60,000
      Chunk 3: sampled 30,000 | cumulative sampled 90,000
      Chunk 4: sampled 30,000 | cumulative sampled 120,000
      Chunk 5: sampled 30,000 | cumulative sampled 150,000
      Chunk 6: sampled 30,000 | cumulative sampled 180,000
      Chunk 7: sampled 30,000 | cumulative sampled 210,000
      Chunk 8: sampled 30,000 | cumulative sampled 240,000
      Chunk 9: sampled 30,000 | cumulative sampled 270,000
      Chunk 10: sampled 30,000 | cumulative sampled 300,000
      Chunk 11: sampled 30,000 | cumulative sampled 330,000
      Chunk 12: sampled 30,000 | cumulative sampled 360,000
      Chunk 13: sampled 30,000 | cumulative sampled 390,000
      Chunk 14: sampled 30,000 | cumulative sampled 420,000
      Chunk 15: sampled 30,000 | cumulative sampled 450,000
      Chunk 16: sampled 30,000 | cumulative sampled 480,000
      Chunk 17: sampled 30,000 | cumulative sampled 510,000
      Chunk 18: sampled 30,000 | cumulative sampled 540,000
      Chunk 19: sampled 30,000 | cumulative sampled 570,000
      Chunk 20: sampled 30,000 | cumulative sampled 600,000
      Chunk 21: sampled 30,000 | cumulative sampled 630,000
      Chunk 22: sampled 30,000 | cumulative sampled 660,000
      Chunk 23: sampled 30,000 | cumulative sampled 690,000
      Chunk 24: sampled 30,000 | cumulative sampled 720,000
      Chunk 25: sampled 30,000 | cumulative sampled 750,000
      Chunk 26: sampled 30,000 | cumulative sampled 780,000
      Chunk 27: sampled 30,000 | cumulative sampled 810,000
      Chunk 28: sampled 30,000 | cumulative sampled 840,000
      Chunk 29: sampled 30,000 | cumulative sampled 870,000
      Chunk 30: sampled 30,000 | cumulative sampled 900,000
      Chunk 31: sampled 30,000 | cumulative sampled 930,000
      Chunk 32: sampled 30,000 | cumulative sampled 960,000
      Chunk 33: sampled 30,000 | cumulative sampled 990,000
      Chunk 34: sampled 30,000 | cumulative sampled 1,020,000
      Chunk 35: sampled 30,000 | cumulative sampled 1,050,000
      Chunk 36: sampled 12,508 | cumulative sampled 1,062,508
    
    [32/32] FragPipe_Vincent_MSV000090572_stored-grain_peptide_genome_projection.csv
      Chunk 1: sampled 30,000 | cumulative sampled 30,000
      Chunk 2: sampled 314 | cumulative sampled 30,314
    
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
      <td>100% stratified per projection file/source-tissue</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sample fraction</td>
      <td>1</td>
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
      <td>8291056</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Exact translation matches</td>
      <td>8078586</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Exact translation match rate (%)</td>
      <td>97.44</td>
    </tr>
    <tr>
      <th>7</th>
      <td>I/L-normalised translation matches</td>
      <td>8214230</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I/L-normalised translation match rate (%)</td>
      <td>99.07</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Multi-block peptide projections tested</td>
      <td>1100087</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Negative-strand peptide projections tested</td>
      <td>4236479</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Validation status: validated</td>
      <td>8214230</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Validation status: translation_mismatch</td>
      <td>76811</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Validation status: contains_N</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>


    
    Validation table saved: python_outputs\tables\wheat_projection_validation_stratified100percent_step10.csv
    Tissue-level validation summary saved: python_outputs\tables\wheat_projection_validation_100%_tissue_summary_step10.csv
    Overall validation summary saved: python_outputs\tables\wheat_projection_validation_100%_summary_step10.csv
    

# Step 11 — Sanity Checks for Translation-Validated Peptide Genome Projections

This step performs final quality-control checks on the projected peptide genome coordinates before public upload to Apollo/JBrowse.

The aim is to verify that the annotation-guided peptide projections generated in Step 10 and validated by translation are internally consistent and suitable for genome-browser visualisation.

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
# Step 11A — Sanity checks for translation-validated peptide
# genome projections (takes approximately 30 min)
#
# Corrected to retain valid ChrUnknown projections.
# ============================================================

import pandas as pd
from pathlib import Path


# -----------------------------
# 1. Input / output paths
# -----------------------------

fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = (
    fragpipe_dir
    / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
)

sanity_full_out = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"
)

sanity_failed_out = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_failed_rows_step11.csv"
)

sanity_summary_out = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_summary_step11.csv"
)

manifest = pd.read_csv(
    manifest_file,
    encoding="utf-8-sig"
)

# Step 10 output: full translation-validation table
validation_file = (
    tables_dir
    / "wheat_projection_validation_stratified100percent_step10.csv"
)

if not validation_file.exists():
    raise FileNotFoundError(
        f"Step 10 translation-validation file not found:\n"
        f"{validation_file}\n\n"
        "Please run Step 10 first."
    )


# -----------------------------
# 2. Expected wheat sequence identifiers and valid strands
# -----------------------------

# ChrUnknown is a valid sequence identifier in the
# IWGSC RefSeq v2.1 GFF3 annotation and must therefore
# pass this annotation-consistency check.
valid_chromosomes = {
    "Chr1A", "Chr1B", "Chr1D",
    "Chr2A", "Chr2B", "Chr2D",
    "Chr3A", "Chr3B", "Chr3D",
    "Chr4A", "Chr4B", "Chr4D",
    "Chr5A", "Chr5B", "Chr5D",
    "Chr6A", "Chr6B", "Chr6D",
    "Chr7A", "Chr7B", "Chr7D",
    "ChrUnknown"
}

valid_strands = {
    "+",
    "-"
}


# -----------------------------
# 3. Helper functions
# -----------------------------

def parse_bed_list(value):
    """
    Convert comma-separated BED block-size or block-start
    strings into integer lists.

    Empty or missing values return an empty list.
    """

    if pd.isna(value):
        return []

    value = str(value).strip().strip(",")

    if value == "":
        return []

    try:
        return [
            int(item)
            for item in value.split(",")
            if str(item).strip() != ""
        ]

    except ValueError:
        return []


def check_bed_geometry(row):
    """
    Check BED interval and BED12-style block geometry.
    """

    try:
        bed_start = int(
            row["BED_start_0based"]
        )

        bed_end = int(
            row["BED_end_0based_exclusive"]
        )

        block_count = int(
            row["BED_block_count"]
        )

    except Exception:
        return False

    if bed_start < 0:
        return False

    if bed_end <= bed_start:
        return False

    block_sizes = parse_bed_list(
        row["BED_block_sizes"]
    )

    block_starts = parse_bed_list(
        row["BED_block_starts"]
    )

    if block_count <= 0:
        return False

    if len(block_sizes) != block_count:
        return False

    if len(block_starts) != block_count:
        return False

    if any(
        size <= 0
        for size in block_sizes
    ):
        return False

    if any(
        start < 0
        for start in block_starts
    ):
        return False

    interval_length = (
        bed_end
        - bed_start
    )

    # Every block must fit inside the BED interval.
    for block_start, block_size in zip(
        block_starts,
        block_sizes
    ):

        if (
            block_start
            + block_size
            > interval_length
        ):
            return False

    return True


def check_block_nt_length(row):
    """
    Check that the sum of BED block nucleotide lengths
    matches peptide length multiplied by three.
    """

    try:
        peptide_length = int(
            row["Peptide_length_AA"]
        )

    except Exception:
        return False

    block_sizes = parse_bed_list(
        row["BED_block_sizes"]
    )

    if len(block_sizes) == 0:
        return False

    return (
        sum(block_sizes)
        == peptide_length * 3
    )


def check_chromosome_and_strand(row):
    """
    Check that the sequence identifier is represented in the
    IWGSC RefSeq v2.1 annotation and that the strand is valid.

    ChrUnknown is retained because it is a valid GFF3 sequence
    identifier representing unplaced annotated sequence.
    """

    chromosome = str(
        row["Chromosome"]
    ).strip()

    strand = str(
        row["Strand"]
    ).strip()

    return (
        chromosome in valid_chromosomes
        and strand in valid_strands
    )


def check_protein_coordinates(row):
    """
    Check that amino-acid coordinates are internally
    consistent with peptide length.
    """

    try:
        aa_start = int(
            row["AA_start"]
        )

        aa_end = int(
            row["AA_end"]
        )

        peptide_length = int(
            row["Peptide_length_AA"]
        )

    except Exception:
        return False

    if aa_start <= 0:
        return False

    if aa_end < aa_start:
        return False

    if (
        aa_end
        - aa_start
        + 1
        != peptide_length
    ):
        return False

    peptide = str(
        row["Peptide"]
    )

    if len(peptide) != peptide_length:
        return False

    return True


# -----------------------------
# 4. Run sanity checks across Step 10 output
# -----------------------------

print(
    "\nRunning sanity checks on Step 10 "
    "translation-validated projections..."
)

chunk_size = 100_000

# Overwrite previous Step 11 outputs.
for output_file in [
    sanity_full_out,
    sanity_failed_out,
    sanity_summary_out
]:

    if output_file.exists():
        output_file.unlink()


# Build lookup from Step 9 projection filename
# to manifest metadata.
manifest_lookup = {}

for _, manifest_row in manifest.iterrows():

    projection_filename = (
        manifest_row[
            "FragPipe-Output-Peptide"
        ]
        .replace(
            "_peptide.tsv",
            "_peptide_genome_projection.csv"
        )
    )

    manifest_lookup[
        projection_filename
    ] = {
        "Source":
            manifest_row["Source"],

        "Species":
            manifest_row["Species"],

        "Tissue":
            manifest_row["Tissue-Raw-Code"],

        "Batch":
            manifest_row["Batch"]
    }


def detect_source_file_column(chunk):
    """
    Detect the column containing the original Step 9
    projection filename.

    Step 10 intended to write '_source_file', but pandas
    itertuples() may rename columns beginning with an
    underscore into positional names.

    This function first checks for '_source_file', then
    searches for a column containing values ending in
    '_peptide_genome_projection.csv'.
    """

    if "_source_file" in chunk.columns:
        return "_source_file"

    for column in chunk.columns:

        sample_values = (
            chunk[column]
            .dropna()
            .astype(str)
            .head(20)
        )

        if sample_values.str.contains(
            "_peptide_genome_projection.csv",
            regex=False
        ).any():

            return column

    return None


summary_dict = {}

header_written_full = False
header_written_failed = False

first_failed_examples = []

source_file_column = None

total_rows_read = 0
total_translation_validated = 0
total_translation_excluded = 0


for chunk_number, chunk in enumerate(

    pd.read_csv(
        validation_file,
        chunksize=chunk_size,
        low_memory=False
    ),

    start=1
):

    total_rows_read += len(
        chunk
    )

    # Detect the source-file column once.
    if source_file_column is None:

        source_file_column = (
            detect_source_file_column(
                chunk
            )
        )

        if source_file_column is None:

            raise KeyError(
                "Could not identify the Step 10 source-file "
                "column. Expected '_source_file' or a column "
                "containing values ending with "
                "'_peptide_genome_projection.csv'."
            )

        print(
            "Detected Step 10 source-file column: "
            f"{source_file_column}"
        )

    if "Validation_status" not in chunk.columns:

        raise KeyError(
            "Column 'Validation_status' was not found "
            "in the Step 10 validation table."
        )

    # Count all Step 10 rows by source file
    # and translation-validation status.
    for projection_filename, file_group in chunk.groupby(
        source_file_column
    ):

        projection_filename = str(
            projection_filename
        )

        if projection_filename not in summary_dict:

            metadata = manifest_lookup.get(
                projection_filename,
                {
                    "Source": pd.NA,
                    "Species": pd.NA,
                    "Tissue": pd.NA,
                    "Batch": pd.NA
                }
            )

            summary_dict[
                projection_filename
            ] = {
                "Source":
                    metadata["Source"],

                "Species":
                    metadata["Species"],

                "Tissue":
                    metadata["Tissue"],

                "Batch":
                    metadata["Batch"],

                "Projection_file":
                    projection_filename,

                "Rows_from_step10_validation_table":
                    0,

                "Rows_translation_validated":
                    0,

                "Rows_excluded_by_translation_validation":
                    0,

                "Translation_validated_rows_checked":
                    0,

                "Rows_passing_all_sanity_checks":
                    0,

                "Rows_failing_any_sanity_check":
                    0,

                "BED_geometry_failures":
                    0,

                "Block_nt_length_failures":
                    0,

                "Chromosome_strand_failures":
                    0,

                "Protein_coordinate_failures":
                    0
            }

        summary_dict[
            projection_filename
        ][
            "Rows_from_step10_validation_table"
        ] += len(
            file_group
        )

        number_validated = int(
            (
                file_group[
                    "Validation_status"
                ]
                .astype(str)
                == "validated"
            ).sum()
        )

        number_excluded = (
            len(file_group)
            - number_validated
        )

        summary_dict[
            projection_filename
        ][
            "Rows_translation_validated"
        ] += number_validated

        summary_dict[
            projection_filename
        ][
            "Rows_excluded_by_translation_validation"
        ] += number_excluded


    # Retain only translation-validated rows
    # for Step 11 sanity checking.
    projected = chunk[
        chunk[
            "Validation_status"
        ]
        .astype(str)
        == "validated"
    ].copy()

    total_translation_validated += len(
        projected
    )

    total_translation_excluded += (
        len(chunk)
        - len(projected)
    )

    if projected.empty:

        print(
            f"Chunk {chunk_number}: "
            f"read {len(chunk):,} rows | "
            "no translation-validated rows"
        )

        continue


    # Derive peptide length when not already present.
    if "Peptide_length_AA" not in projected.columns:

        if (
            "Original_peptide_clean"
            in projected.columns
        ):

            projected[
                "Peptide_length_AA"
            ] = (
                projected[
                    "Original_peptide_clean"
                ]
                .astype(str)
                .str.len()
            )

        else:

            projected[
                "Peptide_length_AA"
            ] = (
                projected["Peptide"]
                .astype(str)
                .str.len()
            )


    # Add or standardise projection-file metadata.
    projected[
        "Projection_file"
    ] = (
        projected[
            source_file_column
        ]
        .astype(str)
    )

    projected["Source"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Source",
                pd.NA
            )
        )
    )

    projected["Species"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Species",
                pd.NA
            )
        )
    )

    projected["Tissue"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Tissue",
                pd.NA
            )
        )
    )

    projected["Batch"] = (
        projected[
            "Projection_file"
        ]
        .map(
            lambda value:
            manifest_lookup
            .get(value, {})
            .get(
                "Batch",
                pd.NA
            )
        )
    )


    # Run the four sanity checks.
    projected[
        "Check_BED_geometry"
    ] = projected.apply(
        check_bed_geometry,
        axis=1
    )

    projected[
        "Check_block_nt_length"
    ] = projected.apply(
        check_block_nt_length,
        axis=1
    )

    projected[
        "Check_chromosome_and_strand"
    ] = projected.apply(
        check_chromosome_and_strand,
        axis=1
    )

    projected[
        "Check_protein_coordinates"
    ] = projected.apply(
        check_protein_coordinates,
        axis=1
    )

    check_columns = [
        "Check_BED_geometry",
        "Check_block_nt_length",
        "Check_chromosome_and_strand",
        "Check_protein_coordinates"
    ]

    projected[
        "All_sanity_checks_passed"
    ] = (
        projected[
            check_columns
        ]
        .all(axis=1)
    )

    projected[
        "Sanity_check_status"
    ] = (
        projected[
            "All_sanity_checks_passed"
        ]
        .map({
            True: "passed",
            False: "failed"
        })
    )


    # Update source–tissue summary counts.
    for projection_filename, file_group in projected.groupby(
        "Projection_file"
    ):

        projection_filename = str(
            projection_filename
        )

        if projection_filename not in summary_dict:

            metadata = manifest_lookup.get(
                projection_filename,
                {
                    "Source": pd.NA,
                    "Species": pd.NA,
                    "Tissue": pd.NA,
                    "Batch": pd.NA
                }
            )

            summary_dict[
                projection_filename
            ] = {
                "Source":
                    metadata["Source"],

                "Species":
                    metadata["Species"],

                "Tissue":
                    metadata["Tissue"],

                "Batch":
                    metadata["Batch"],

                "Projection_file":
                    projection_filename,

                "Rows_from_step10_validation_table":
                    0,

                "Rows_translation_validated":
                    0,

                "Rows_excluded_by_translation_validation":
                    0,

                "Translation_validated_rows_checked":
                    0,

                "Rows_passing_all_sanity_checks":
                    0,

                "Rows_failing_any_sanity_check":
                    0,

                "BED_geometry_failures":
                    0,

                "Block_nt_length_failures":
                    0,

                "Chromosome_strand_failures":
                    0,

                "Protein_coordinate_failures":
                    0
            }

        summary_dict[
            projection_filename
        ][
            "Translation_validated_rows_checked"
        ] += len(
            file_group
        )

        summary_dict[
            projection_filename
        ][
            "Rows_passing_all_sanity_checks"
        ] += int(
            file_group[
                "All_sanity_checks_passed"
            ].sum()
        )

        summary_dict[
            projection_filename
        ][
            "Rows_failing_any_sanity_check"
        ] += int(
            (
                ~file_group[
                    "All_sanity_checks_passed"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "BED_geometry_failures"
        ] += int(
            (
                ~file_group[
                    "Check_BED_geometry"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "Block_nt_length_failures"
        ] += int(
            (
                ~file_group[
                    "Check_block_nt_length"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "Chromosome_strand_failures"
        ] += int(
            (
                ~file_group[
                    "Check_chromosome_and_strand"
                ]
            ).sum()
        )

        summary_dict[
            projection_filename
        ][
            "Protein_coordinate_failures"
        ] += int(
            (
                ~file_group[
                    "Check_protein_coordinates"
                ]
            ).sum()
        )


    # Write the complete sanity-check output incrementally.
    projected.to_csv(
        sanity_full_out,
        index=False,
        mode="a",
        header=not header_written_full
    )

    header_written_full = True


    # Write failed rows incrementally.
    failed = projected[
        projected[
            "Sanity_check_status"
        ]
        == "failed"
    ].copy()

    if not failed.empty:

        failed.to_csv(
            sanity_failed_out,
            index=False,
            mode="a",
            header=not header_written_failed
        )

        header_written_failed = True

        if len(first_failed_examples) < 20:

            number_remaining = (
                20
                - len(first_failed_examples)
            )

            first_failed_examples.append(
                failed.head(
                    number_remaining
                )
            )


    print(
        f"Chunk {chunk_number}: "
        f"read {len(chunk):,} rows | "
        f"translation-validated "
        f"{len(projected):,} | "
        f"sanity failed {len(failed):,}"
    )


# -----------------------------
# 5. Build and export summary table
# -----------------------------

if not header_written_full:

    raise ValueError(
        "No translation-validated projected peptide rows "
        "were available for sanity checking."
    )


sanity_summary = pd.DataFrame(
    summary_dict.values()
)


sanity_summary[
    "Percent_translation_validated"
] = (
    sanity_summary[
        "Rows_translation_validated"
    ]
    / sanity_summary[
        "Rows_from_step10_validation_table"
    ]
    * 100
).round(4)


sanity_summary[
    "Percent_passing_all_sanity_checks"
] = (
    sanity_summary[
        "Rows_passing_all_sanity_checks"
    ]
    / sanity_summary[
        "Translation_validated_rows_checked"
    ]
    * 100
).round(4)


sanity_summary.to_csv(
    sanity_summary_out,
    index=False
)


# Build a small failed-row preview for display.
if len(first_failed_examples) > 0:

    sanity_failed_preview = (
        pd.concat(
            first_failed_examples,
            ignore_index=True
        )
        .head(20)
    )

else:

    sanity_failed_preview = pd.DataFrame()


# -----------------------------
# 6. Overall summary
# -----------------------------

overall_checked = int(
    sanity_summary[
        "Translation_validated_rows_checked"
    ].sum()
)

overall_passed = int(
    sanity_summary[
        "Rows_passing_all_sanity_checks"
    ].sum()
)

overall_failed = int(
    sanity_summary[
        "Rows_failing_any_sanity_check"
    ].sum()
)

overall_pass_percent = (
    round(
        overall_passed
        / overall_checked
        * 100,
        4
    )
    if overall_checked > 0
    else pd.NA
)


print(
    "\n===== STEP 11 SANITY CHECK SUMMARY ====="
)

print(
    "Rows read from Step 10 validation table: "
    f"{total_rows_read:,}"
)

print(
    "Rows excluded by translation validation: "
    f"{total_translation_excluded:,}"
)

print(
    "Translation-validated rows checked: "
    f"{overall_checked:,}"
)

print(
    "Rows passing all sanity checks: "
    f"{overall_passed:,}"
)

print(
    "Rows failing at least one sanity check: "
    f"{overall_failed:,}"
)

print(
    "Overall sanity-check pass rate among "
    "translation-validated rows: "
    f"{overall_pass_percent}%"
)

print(
    f"\nFull sanity-check table saved: "
    f"{sanity_full_out}"
)

if sanity_failed_out.exists():

    print(
        f"Failed-row diagnostic table saved: "
        f"{sanity_failed_out}"
    )

else:

    print(
        "No failed-row diagnostic table was created "
        "because all rows passed."
    )

print(
    f"Source–tissue sanity summary saved: "
    f"{sanity_summary_out}"
)


display(
    sanity_summary
)

if not sanity_failed_preview.empty:

    display(
        sanity_failed_preview
    )

else:

    print(
        "\nNo failed sanity-check rows to display."
    )
```

    
    Running sanity checks on Step 10 translation-validated projections...
    Detected Step 10 source-file column: _22
    Chunk 1: read 100,000 rows | translation-validated 99,476 | sanity failed 0
    Chunk 2: read 100,000 rows | translation-validated 99,426 | sanity failed 0
    Chunk 3: read 100,000 rows | translation-validated 99,342 | sanity failed 0
    Chunk 4: read 100,000 rows | translation-validated 99,392 | sanity failed 0
    Chunk 5: read 100,000 rows | translation-validated 99,450 | sanity failed 0
    Chunk 6: read 100,000 rows | translation-validated 99,285 | sanity failed 0
    Chunk 7: read 100,000 rows | translation-validated 99,365 | sanity failed 0
    Chunk 8: read 100,000 rows | translation-validated 99,354 | sanity failed 0
    Chunk 9: read 100,000 rows | translation-validated 99,505 | sanity failed 0
    Chunk 10: read 100,000 rows | translation-validated 99,501 | sanity failed 0
    Chunk 11: read 100,000 rows | translation-validated 99,434 | sanity failed 0
    Chunk 12: read 100,000 rows | translation-validated 99,319 | sanity failed 0
    Chunk 13: read 100,000 rows | translation-validated 99,437 | sanity failed 0
    Chunk 14: read 100,000 rows | translation-validated 99,306 | sanity failed 0
    Chunk 15: read 100,000 rows | translation-validated 99,132 | sanity failed 0
    Chunk 16: read 100,000 rows | translation-validated 99,263 | sanity failed 0
    Chunk 17: read 100,000 rows | translation-validated 99,256 | sanity failed 0
    Chunk 18: read 100,000 rows | translation-validated 99,369 | sanity failed 0
    Chunk 19: read 100,000 rows | translation-validated 99,286 | sanity failed 0
    Chunk 20: read 100,000 rows | translation-validated 98,989 | sanity failed 0
    Chunk 21: read 100,000 rows | translation-validated 99,334 | sanity failed 0
    Chunk 22: read 100,000 rows | translation-validated 99,505 | sanity failed 0
    Chunk 23: read 100,000 rows | translation-validated 99,561 | sanity failed 0
    Chunk 24: read 100,000 rows | translation-validated 99,464 | sanity failed 0
    Chunk 25: read 100,000 rows | translation-validated 99,373 | sanity failed 0
    Chunk 26: read 100,000 rows | translation-validated 99,536 | sanity failed 0
    Chunk 27: read 100,000 rows | translation-validated 99,638 | sanity failed 0
    Chunk 28: read 100,000 rows | translation-validated 99,215 | sanity failed 0
    Chunk 29: read 100,000 rows | translation-validated 99,444 | sanity failed 0
    Chunk 30: read 100,000 rows | translation-validated 99,562 | sanity failed 0
    Chunk 31: read 100,000 rows | translation-validated 99,724 | sanity failed 0
    Chunk 32: read 100,000 rows | translation-validated 99,533 | sanity failed 0
    Chunk 33: read 100,000 rows | translation-validated 99,557 | sanity failed 0
    Chunk 34: read 100,000 rows | translation-validated 99,593 | sanity failed 0
    Chunk 35: read 100,000 rows | translation-validated 99,263 | sanity failed 0
    Chunk 36: read 100,000 rows | translation-validated 99,161 | sanity failed 0
    Chunk 37: read 100,000 rows | translation-validated 98,841 | sanity failed 0
    Chunk 38: read 100,000 rows | translation-validated 98,936 | sanity failed 0
    Chunk 39: read 100,000 rows | translation-validated 98,967 | sanity failed 0
    Chunk 40: read 100,000 rows | translation-validated 98,988 | sanity failed 0
    Chunk 41: read 100,000 rows | translation-validated 98,863 | sanity failed 0
    Chunk 42: read 100,000 rows | translation-validated 98,549 | sanity failed 0
    Chunk 43: read 100,000 rows | translation-validated 98,710 | sanity failed 0
    Chunk 44: read 100,000 rows | translation-validated 98,681 | sanity failed 0
    Chunk 45: read 100,000 rows | translation-validated 99,065 | sanity failed 0
    Chunk 46: read 100,000 rows | translation-validated 98,648 | sanity failed 0
    Chunk 47: read 100,000 rows | translation-validated 98,674 | sanity failed 0
    Chunk 48: read 100,000 rows | translation-validated 98,781 | sanity failed 0
    Chunk 49: read 100,000 rows | translation-validated 98,855 | sanity failed 0
    Chunk 50: read 100,000 rows | translation-validated 98,971 | sanity failed 0
    Chunk 51: read 100,000 rows | translation-validated 99,035 | sanity failed 0
    Chunk 52: read 100,000 rows | translation-validated 99,018 | sanity failed 0
    Chunk 53: read 100,000 rows | translation-validated 98,620 | sanity failed 0
    Chunk 54: read 100,000 rows | translation-validated 99,201 | sanity failed 0
    Chunk 55: read 100,000 rows | translation-validated 98,586 | sanity failed 0
    Chunk 56: read 100,000 rows | translation-validated 98,751 | sanity failed 0
    Chunk 57: read 100,000 rows | translation-validated 98,933 | sanity failed 0
    Chunk 58: read 100,000 rows | translation-validated 99,051 | sanity failed 0
    Chunk 59: read 100,000 rows | translation-validated 98,832 | sanity failed 0
    Chunk 60: read 100,000 rows | translation-validated 98,643 | sanity failed 0
    Chunk 61: read 100,000 rows | translation-validated 98,680 | sanity failed 0
    Chunk 62: read 100,000 rows | translation-validated 98,679 | sanity failed 0
    Chunk 63: read 100,000 rows | translation-validated 98,817 | sanity failed 0
    Chunk 64: read 100,000 rows | translation-validated 98,927 | sanity failed 0
    Chunk 65: read 100,000 rows | translation-validated 98,459 | sanity failed 0
    Chunk 66: read 100,000 rows | translation-validated 98,605 | sanity failed 0
    Chunk 67: read 100,000 rows | translation-validated 98,867 | sanity failed 0
    Chunk 68: read 100,000 rows | translation-validated 98,829 | sanity failed 0
    Chunk 69: read 100,000 rows | translation-validated 98,929 | sanity failed 0
    Chunk 70: read 100,000 rows | translation-validated 98,927 | sanity failed 0
    Chunk 71: read 100,000 rows | translation-validated 98,990 | sanity failed 0
    Chunk 72: read 100,000 rows | translation-validated 98,661 | sanity failed 0
    Chunk 73: read 100,000 rows | translation-validated 99,181 | sanity failed 0
    Chunk 74: read 100,000 rows | translation-validated 98,771 | sanity failed 0
    Chunk 75: read 100,000 rows | translation-validated 98,701 | sanity failed 0
    Chunk 76: read 100,000 rows | translation-validated 98,660 | sanity failed 0
    Chunk 77: read 100,000 rows | translation-validated 98,836 | sanity failed 0
    Chunk 78: read 100,000 rows | translation-validated 98,863 | sanity failed 0
    Chunk 79: read 100,000 rows | translation-validated 98,473 | sanity failed 0
    Chunk 80: read 100,000 rows | translation-validated 98,816 | sanity failed 0
    Chunk 81: read 100,000 rows | translation-validated 98,978 | sanity failed 0
    Chunk 82: read 100,000 rows | translation-validated 99,176 | sanity failed 0
    Chunk 83: read 91,056 rows | translation-validated 89,856 | sanity failed 0
    
    ===== STEP 11 SANITY CHECK SUMMARY =====
    Rows read from Step 10 validation table: 8,291,056
    Rows excluded by translation validation: 76,826
    Translation-validated rows checked: 8,214,230
    Rows passing all sanity checks: 8,214,230
    Rows failing at least one sanity check: 0
    Overall sanity-check pass rate among translation-validated rows: 100.0%
    
    Full sanity-check table saved: python_outputs\tables\wheat_projection_translation_validated_sanity_checks_full_step11.csv
    No failed-row diagnostic table was created because all rows passed.
    Source–tissue sanity summary saved: python_outputs\tables\wheat_projection_translation_validated_sanity_checks_summary_step11.csv
    


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
      <th>Rows_from_step10_validation_table</th>
      <th>Rows_translation_validated</th>
      <th>Rows_excluded_by_translation_validation</th>
      <th>Translation_validated_rows_checked</th>
      <th>Rows_passing_all_sanity_checks</th>
      <th>Rows_failing_any_sanity_check</th>
      <th>BED_geometry_failures</th>
      <th>Block_nt_length_failures</th>
      <th>Chromosome_strand_failures</th>
      <th>Protein_coordinate_failures</th>
      <th>Percent_translation_validated</th>
      <th>Percent_passing_all_sanity_checks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
      <td>164365</td>
      <td>163467</td>
      <td>898</td>
      <td>163467</td>
      <td>163467</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4537</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
      <td>13227</td>
      <td>13137</td>
      <td>90</td>
      <td>13137</td>
      <td>13137</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.3196</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
      <td>204476</td>
      <td>203264</td>
      <td>1212</td>
      <td>203264</td>
      <td>203264</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4073</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
      <td>8852</td>
      <td>8742</td>
      <td>110</td>
      <td>8742</td>
      <td>8742</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.7573</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
      <td>102830</td>
      <td>102289</td>
      <td>541</td>
      <td>102289</td>
      <td>102289</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4739</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
      <td>145133</td>
      <td>144079</td>
      <td>1054</td>
      <td>144079</td>
      <td>144079</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.2738</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>126195</td>
      <td>125355</td>
      <td>840</td>
      <td>125355</td>
      <td>125355</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.3344</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>179725</td>
      <td>178814</td>
      <td>911</td>
      <td>178814</td>
      <td>178814</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4931</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>132701</td>
      <td>132081</td>
      <td>620</td>
      <td>132081</td>
      <td>132081</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.5328</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>113203</td>
      <td>112389</td>
      <td>814</td>
      <td>112389</td>
      <td>112389</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.2809</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>111792</td>
      <td>111156</td>
      <td>636</td>
      <td>111156</td>
      <td>111156</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4311</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>145632</td>
      <td>144641</td>
      <td>991</td>
      <td>144641</td>
      <td>144641</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.3195</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>46200</td>
      <td>45680</td>
      <td>520</td>
      <td>45680</td>
      <td>45680</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.8745</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>120821</td>
      <td>119922</td>
      <td>899</td>
      <td>119922</td>
      <td>119922</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.2559</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
      <td>147618</td>
      <td>146562</td>
      <td>1056</td>
      <td>146562</td>
      <td>146562</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.2846</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>169675</td>
      <td>168564</td>
      <td>1111</td>
      <td>168564</td>
      <td>168564</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.3452</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
      <td>99823</td>
      <td>98731</td>
      <td>1092</td>
      <td>98731</td>
      <td>98731</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.9061</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
      <td>116936</td>
      <td>116285</td>
      <td>651</td>
      <td>116285</td>
      <td>116285</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4433</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
      <td>131215</td>
      <td>130645</td>
      <td>570</td>
      <td>130645</td>
      <td>130645</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.5656</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
      <td>74698</td>
      <td>74334</td>
      <td>364</td>
      <td>74334</td>
      <td>74334</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.5127</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_gen...</td>
      <td>160204</td>
      <td>159219</td>
      <td>985</td>
      <td>159219</td>
      <td>159219</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.3852</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_geno...</td>
      <td>194694</td>
      <td>193938</td>
      <td>756</td>
      <td>193938</td>
      <td>193938</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.6117</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>97188</td>
      <td>96387</td>
      <td>801</td>
      <td>96387</td>
      <td>96387</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.1758</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>100639</td>
      <td>100085</td>
      <td>554</td>
      <td>100085</td>
      <td>100085</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.4495</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_gen...</td>
      <td>191943</td>
      <td>191262</td>
      <td>681</td>
      <td>191262</td>
      <td>191262</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.6452</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>111831</td>
      <td>111315</td>
      <td>516</td>
      <td>111315</td>
      <td>111315</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.5386</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>188826</td>
      <td>188025</td>
      <td>801</td>
      <td>188025</td>
      <td>188025</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.5758</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>60734</td>
      <td>60181</td>
      <td>553</td>
      <td>60181</td>
      <td>60181</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99.0895</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>1850136</td>
      <td>1829196</td>
      <td>20940</td>
      <td>1829196</td>
      <td>1829196</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.8682</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>1886922</td>
      <td>1864415</td>
      <td>22507</td>
      <td>1864415</td>
      <td>1864415</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.8072</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>1062508</td>
      <td>1050178</td>
      <td>12330</td>
      <td>1050178</td>
      <td>1050178</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.8395</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_pep...</td>
      <td>30314</td>
      <td>29892</td>
      <td>422</td>
      <td>29892</td>
      <td>29892</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>98.6079</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
</div>


    
    No failed sanity-check rows to display.
    

# Step 11B — Diagnostic Audit: Fate of ChrUnknown Peptide Projections

This diagnostic step tracks peptide projections assigned to `ChrUnknown` across the validation workflow.

The purpose is to determine whether `ChrUnknown` peptide projections were:

1. present after initial annotation-guided peptide genome projection,
2. retained after translation validation,
3. excluded during sanity checking,
4. absent from the final non-redundant validated peptide set.

This audit was added because final validated BED and EDA outputs no longer contained peptide projections assigned to `ChrUnknown`.

---

## Workflow stages audited

The diagnostic compares `ChrUnknown` counts across:

| Stage | File type | Interpretation |
|---|---|---|
| Step 9 | Tissue-level peptide genome projection files | Initial annotation-guided projected peptide coordinates |
| Step 10 | Full translation-validation table | Rows tested by translation reconstruction |
| Step 11 | Full sanity-check table | Translation-validated rows after BED/chromosome/protein-coordinate checks |
| Step 13 | All-tissue non-redundant validated table | Final non-redundant validated peptide projection set |

---

## Expected outcome

If `ChrUnknown` rows are present in Step 9 and Step 10 but fail Step 11, this indicates that they were removed by the sanity-check layer rather than by peptide-to-genome projection or translation validation.

In particular, rows assigned to `ChrUnknown` are expected to fail the chromosome/strand sanity check when `ChrUnknown` is not included in the accepted chromosome list used for final chromosome-scale BED export.

---

## Output files

### Summary table

```text
wheat_ChrUnknown_validation_fate_summary_step11B.csv


```python
# ============================================================
# Step 11B — Diagnostic audit: fate of ChrUnknown peptide
# projections
#
# Memory-light version for large CSV files.
# ============================================================

import pandas as pd

from pathlib import Path
from collections import defaultdict


# -----------------------------
# 1. Paths
# -----------------------------

fragpipe_dir = Path("FragPipe_results")

tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(
    parents=True,
    exist_ok=True
)

manifest_file = (
    fragpipe_dir
    / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
)

# Existing workflow files
step10_validation_file = (
    tables_dir
    / "wheat_projection_validation_stratified100percent_step10.csv"
)

step11_sanity_file = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"
)

step13_combined_file = (
    tables_dir
    / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv"
)

# Original Step 11B output filenames
summary_out = (
    tables_dir
    / "wheat_ChrUnknown_validation_fate_summary_step11B.csv"
)

failed_examples_out = (
    tables_dir
    / "wheat_ChrUnknown_failed_sanity_examples_step11B.csv"
)

chunksize = 25_000
max_failed_examples = 100


# -----------------------------
# 2. Confirm required inputs
# -----------------------------

if not manifest_file.exists():

    raise FileNotFoundError(
        f"Manifest file not found:\n"
        f"{manifest_file}"
    )


if not step10_validation_file.exists():

    raise FileNotFoundError(
        f"Step 10 file not found:\n"
        f"{step10_validation_file}"
    )


if not step11_sanity_file.exists():

    raise FileNotFoundError(
        f"Step 11 file not found:\n"
        f"{step11_sanity_file}\n\n"
        "Please run the corrected Step 11 first."
    )


manifest = pd.read_csv(
    manifest_file,
    encoding="utf-8-sig"
)


# Overwrite previous Step 11B outputs.
for output_file in [
    summary_out,
    failed_examples_out
]:

    if output_file.exists():
        output_file.unlink()


# -----------------------------
# 3. Helper functions
# -----------------------------

def normalise_chr(value):
    """
    Normalise sequence labels for the ChrUnknown audit.
    """

    if pd.isna(value):
        return "NA"

    value = str(value).strip()

    if value.lower() in [
        "chrunknown",
        "unknown"
    ]:

        return "ChrUnknown"

    if value.lower() in [
        "nan",
        "none",
        "",
        "<na>"
    ]:

        return "NA"

    return value


def build_manifest_lookup(manifest_data):
    """
    Build a lookup from Step 9 projection filename to
    source–tissue metadata.
    """

    lookup = {}

    for _, row in manifest_data.iterrows():

        projection_filename = (
            row[
                "FragPipe-Output-Peptide"
            ]
            .replace(
                "_peptide.tsv",
                "_peptide_genome_projection.csv"
            )
        )

        lookup[
            projection_filename
        ] = {
            "Source":
                row["Source"],

            "Species":
                row["Species"],

            "Tissue":
                row["Tissue-Raw-Code"],

            "Batch":
                row["Batch"]
        }

    return lookup


manifest_lookup = build_manifest_lookup(
    manifest
)


def get_meta_from_projection_file(
    projection_file
):
    """
    Recover source–tissue metadata from a Step 9
    projection filename.
    """

    projection_file = Path(
        str(projection_file)
    ).name

    return manifest_lookup.get(
        projection_file,
        {
            "Source": "UNKNOWN",
            "Species": "bread wheat",
            "Tissue": "UNKNOWN",
            "Batch": "UNKNOWN"
        }
    )


def detect_projection_source_column(
    dataframe
):
    """
    Detect the column containing the original Step 9
    projection filename.

    Step 10 intended to use '_source_file', although pandas
    may rename columns beginning with an underscore.
    """

    preferred_columns = [
        "_source_file",
        "Projection_file",
        "Genome_projection_file",
        "Source_file"
    ]

    for column in preferred_columns:

        if column in dataframe.columns:
            return column

    for column in dataframe.columns:

        sample_values = (
            dataframe[column]
            .dropna()
            .astype(str)
            .head(50)
        )

        if sample_values.str.contains(
            "_peptide_genome_projection.csv",
            regex=False
        ).any():

            return column

    return None


def get_gene_col(columns):
    """
    Return the first available gene-model column.
    """

    for column in [
        "GeneModel",
        "GeneID",
        "Gene_label",
        "Gene_model"
    ]:

        if column in columns:
            return column

    return None


def init_record():
    """
    Initialise one compact ChrUnknown audit record.
    """

    return {
        "Total_rows": 0,
        "ChrUnknown_rows": 0,
        "ChrUnknown_peptides": set(),
        "ChrUnknown_proteins": set(),
        "ChrUnknown_genes": set()
    }


def update_record(
    records,
    key,
    dataframe,
    chrunknown_mask
):
    """
    Update counts for one audit group.

    Only unique identifiers from ChrUnknown rows are retained
    in memory.
    """

    record = records[key]

    record[
        "Total_rows"
    ] += len(
        dataframe
    )

    record[
        "ChrUnknown_rows"
    ] += int(
        chrunknown_mask.sum()
    )

    chrunknown_data = dataframe.loc[
        chrunknown_mask
    ]

    if chrunknown_data.empty:
        return


    if "Peptide" in chrunknown_data.columns:

        record[
            "ChrUnknown_peptides"
        ].update(
            chrunknown_data[
                "Peptide"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


    if "ProteinID" in chrunknown_data.columns:

        record[
            "ChrUnknown_proteins"
        ].update(
            chrunknown_data[
                "ProteinID"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


    gene_column = get_gene_col(
        chrunknown_data.columns
    )

    if gene_column is not None:

        record[
            "ChrUnknown_genes"
        ].update(
            chrunknown_data[
                gene_column
            ]
            .dropna()
            .astype(str)
            .unique()
        )


def records_to_dataframe(records):
    """
    Convert compact audit records to a DataFrame.
    """

    rows = []

    for key, record in records.items():

        (
            stage,
            source,
            species,
            tissue,
            batch,
            projection_file,
            status_detail
        ) = key

        total_rows = record[
            "Total_rows"
        ]

        chrunknown_rows = record[
            "ChrUnknown_rows"
        ]

        rows.append({
            "Stage":
                stage,

            "Source":
                source,

            "Species":
                species,

            "Tissue":
                tissue,

            "Batch":
                batch,

            "Projection_file":
                projection_file,

            "Status_detail":
                status_detail,

            "Total_rows":
                total_rows,

            "ChrUnknown_rows":
                chrunknown_rows,

            "ChrUnknown_percent_rows":
                (
                    round(
                        chrunknown_rows
                        / total_rows
                        * 100,
                        4
                    )
                    if total_rows > 0
                    else 0
                ),

            "ChrUnknown_unique_peptides":
                len(
                    record[
                        "ChrUnknown_peptides"
                    ]
                ),

            "ChrUnknown_unique_proteins":
                len(
                    record[
                        "ChrUnknown_proteins"
                    ]
                ),

            "ChrUnknown_unique_gene_models":
                len(
                    record[
                        "ChrUnknown_genes"
                    ]
                )
        })

    return pd.DataFrame(
        rows
    )


# -----------------------------
# 4. Stage A — Step 9 initial projected rows
# -----------------------------

print(
    "Auditing Step 9 projected rows..."
)

step9_records = defaultdict(
    init_record
)


for _, row in manifest.iterrows():

    projection_filename = (
        row[
            "FragPipe-Output-Peptide"
        ]
        .replace(
            "_peptide.tsv",
            "_peptide_genome_projection.csv"
        )
    )

    projection_path = (
        tables_dir
        / projection_filename
    )

    if not projection_path.exists():

        print(
            "Skipped missing Step 9 file: "
            f"{projection_path}"
        )

        continue


    header = pd.read_csv(
        projection_path,
        nrows=0
    )

    header_columns = list(
        header.columns
    )


    required_columns = [
        "Chromosome",
        "Projection_status"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in header_columns
    ]

    if missing_columns:

        raise KeyError(
            f"Missing required column(s) in "
            f"{projection_filename}: "
            f"{missing_columns}"
        )


    use_columns = [
        column
        for column in [
            "Chromosome",
            "Projection_status",
            "Peptide",
            "ProteinID",
            "GeneModel",
            "GeneID",
            "Gene_label"
        ]
        if column in header_columns
    ]


    key = (
        "Step 9 projected rows",
        row["Source"],
        row["Species"],
        row["Tissue-Raw-Code"],
        row["Batch"],
        projection_filename,
        "Projection_status == projected"
    )


    for chunk in pd.read_csv(
        projection_path,
        usecols=use_columns,
        chunksize=chunksize,
        low_memory=False
    ):

        chunk = chunk[
            chunk[
                "Projection_status"
            ]
            .astype(str)
            .str.strip()
            .eq("projected")
        ].copy()

        if chunk.empty:
            continue


        chromosome_normalised = (
            chunk[
                "Chromosome"
            ]
            .map(
                normalise_chr
            )
        )

        chrunknown_mask = (
            chromosome_normalised
            .eq("ChrUnknown")
        )


        update_record(
            step9_records,
            key,
            chunk,
            chrunknown_mask
        )


step9_summary = records_to_dataframe(
    step9_records
)


# -----------------------------
# 5. Stage B — Step 10 translation validation
# -----------------------------

print(
    "Auditing Step 10 translation-validation rows..."
)


step10_header = pd.read_csv(
    step10_validation_file,
    nrows=0
)

step10_columns = list(
    step10_header.columns
)


required_columns = [
    "Chromosome",
    "Validation_status"
]

missing_columns = [
    column
    for column in required_columns
    if column not in step10_columns
]

if missing_columns:

    raise KeyError(
        "Missing required Step 10 column(s): "
        f"{missing_columns}"
    )


# Read a small sample to detect the projection-source column.
step10_sample = pd.read_csv(
    step10_validation_file,
    nrows=100,
    low_memory=False
)

source_file_column = (
    detect_projection_source_column(
        step10_sample
    )
)


step10_use_columns = [
    column
    for column in [
        source_file_column,
        "Source",
        "Species",
        "Tissue",
        "Batch",
        "Chromosome",
        "Validation_status",
        "Peptide",
        "ProteinID",
        "GeneModel",
        "GeneID",
        "Gene_label"
    ]
    if (
        column is not None
        and column in step10_columns
    )
]


print(
    "Step 10 columns used: "
    f"{step10_use_columns}"
)


if source_file_column is None:

    print(
        "No Step 10 projection-source filename column "
        "was found. Step 10 will be summarised globally "
        "by Validation_status."
    )

else:

    print(
        "Detected Step 10 projection-source column: "
        f"{source_file_column}"
    )


step10_records = defaultdict(
    init_record
)


for chunk_number, chunk in enumerate(

    pd.read_csv(
        step10_validation_file,
        usecols=step10_use_columns,
        chunksize=chunksize,
        low_memory=False
    ),

    start=1
):

    chunk[
        "Chromosome_norm"
    ] = (
        chunk[
            "Chromosome"
        ]
        .map(
            normalise_chr
        )
    )


    metadata_columns = [
        "Source",
        "Species",
        "Tissue",
        "Batch"
    ]


    # Case 1: source–tissue metadata are present.
    if all(
        column in chunk.columns
        for column in metadata_columns
    ):

        for group_values, group in chunk.groupby(
            [
                "Source",
                "Species",
                "Tissue",
                "Batch",
                "Validation_status"
            ],
            dropna=False
        ):

            (
                source,
                species,
                tissue,
                batch,
                validation_status
            ) = group_values


            key = (
                "Step 10 translation validation",
                source,
                species,
                tissue,
                batch,
                "Step10_global_table",
                (
                    "Validation_status == "
                    f"{validation_status}"
                )
            )


            chrunknown_mask = (
                group[
                    "Chromosome_norm"
                ]
                .eq("ChrUnknown")
            )


            update_record(
                step10_records,
                key,
                group,
                chrunknown_mask
            )


    # Case 2: a projection-source filename is available.
    elif source_file_column is not None:

        for group_values, group in chunk.groupby(
            [
                source_file_column,
                "Validation_status"
            ],
            dropna=False
        ):

            (
                projection_file,
                validation_status
            ) = group_values


            projection_file_name = Path(
                str(projection_file)
            ).name


            metadata = (
                get_meta_from_projection_file(
                    projection_file_name
                )
            )


            key = (
                "Step 10 translation validation",
                metadata["Source"],
                metadata["Species"],
                metadata["Tissue"],
                metadata["Batch"],
                projection_file_name,
                (
                    "Validation_status == "
                    f"{validation_status}"
                )
            )


            chrunknown_mask = (
                group[
                    "Chromosome_norm"
                ]
                .eq("ChrUnknown")
            )


            update_record(
                step10_records,
                key,
                group,
                chrunknown_mask
            )


    # Case 3: no source metadata are available.
    else:

        for validation_status, group in chunk.groupby(
            "Validation_status",
            dropna=False
        ):

            key = (
                "Step 10 translation validation",
                "ALL",
                "bread wheat",
                "ALL",
                "ALL",
                step10_validation_file.name,
                (
                    "Validation_status == "
                    f"{validation_status}"
                )
            )


            chrunknown_mask = (
                group[
                    "Chromosome_norm"
                ]
                .eq("ChrUnknown")
            )


            update_record(
                step10_records,
                key,
                group,
                chrunknown_mask
            )


    if chunk_number % 20 == 0:

        print(
            "  Step 10 chunks processed: "
            f"{chunk_number}"
        )


step10_summary = records_to_dataframe(
    step10_records
)


# -----------------------------
# 6. Stage C — Step 11 sanity checks
# -----------------------------

print(
    "Auditing corrected Step 11 sanity-check rows..."
)


step11_header = pd.read_csv(
    step11_sanity_file,
    nrows=0
)

step11_columns = list(
    step11_header.columns
)


required_columns = [
    "Source",
    "Species",
    "Tissue",
    "Batch",
    "Projection_file",
    "Chromosome",
    "Sanity_check_status",
    "Check_chromosome_and_strand"
]

missing_columns = [
    column
    for column in required_columns
    if column not in step11_columns
]

if missing_columns:

    raise KeyError(
        "Missing required Step 11 column(s): "
        f"{missing_columns}\n\n"
        "Confirm that the corrected Step 11 cell "
        "completed successfully."
    )


step11_use_columns = [
    column
    for column in [
        "Source",
        "Species",
        "Tissue",
        "Batch",
        "Projection_file",
        "Chromosome",
        "Sanity_check_status",
        "Validation_status",
        "Peptide",
        "ProteinID",
        "GeneModel",
        "GeneID",
        "Gene_label",
        "Check_BED_geometry",
        "Check_block_nt_length",
        "Check_chromosome_and_strand",
        "Check_protein_coordinates",
        "All_sanity_checks_passed"
    ]
    if column in step11_columns
]


step11_records = defaultdict(
    init_record
)

failed_examples = []


for chunk_number, chunk in enumerate(

    pd.read_csv(
        step11_sanity_file,
        usecols=step11_use_columns,
        chunksize=chunksize,
        low_memory=False
    ),

    start=1
):

    chunk[
        "Chromosome_norm"
    ] = (
        chunk[
            "Chromosome"
        ]
        .map(
            normalise_chr
        )
    )


    grouping_columns = [
        "Source",
        "Species",
        "Tissue",
        "Batch",
        "Projection_file",
        "Sanity_check_status"
    ]


    for group_values, group in chunk.groupby(
        grouping_columns,
        dropna=False
    ):

        (
            source,
            species,
            tissue,
            batch,
            projection_file,
            sanity_status
        ) = group_values


        projection_file_name = Path(
            str(projection_file)
        ).name


        key = (
            "Step 11 sanity checks",
            source,
            species,
            tissue,
            batch,
            projection_file_name,
            (
                "Sanity_check_status == "
                f"{sanity_status}"
            )
        )


        chrunknown_mask = (
            group[
                "Chromosome_norm"
            ]
            .eq("ChrUnknown")
        )


        update_record(
            step11_records,
            key,
            group,
            chrunknown_mask
        )


    # Retain only a limited number of failed ChrUnknown
    # rows for diagnostic inspection.
    if len(
        failed_examples
    ) < max_failed_examples:

        chrunknown_failed = chunk[
            (
                chunk[
                    "Chromosome_norm"
                ]
                .eq("ChrUnknown")
            )
            &
            (
                chunk[
                    "Sanity_check_status"
                ]
                .astype(str)
                .str.strip()
                .eq("failed")
            )
        ].copy()


        if not chrunknown_failed.empty:

            slots_remaining = (
                max_failed_examples
                - len(failed_examples)
            )

            failed_examples.extend(
                chrunknown_failed
                .head(
                    slots_remaining
                )
                .to_dict(
                    "records"
                )
            )


    if chunk_number % 20 == 0:

        print(
            "  Step 11 chunks processed: "
            f"{chunk_number}"
        )


step11_summary = records_to_dataframe(
    step11_records
)


failed_examples_df = pd.DataFrame(
    failed_examples
)


if not failed_examples_df.empty:

    failed_examples_df.to_csv(
        failed_examples_out,
        index=False
    )


# -----------------------------
# 7. Stage D — Step 13 final nonredundant table
# -----------------------------

print(
    "Assessing Step 13 final nonredundant table..."
)


step13_records = defaultdict(
    init_record
)

step13_included = False


if step13_combined_file.exists():

    step11_modification_time = (
        step11_sanity_file
        .stat()
        .st_mtime
    )

    step13_modification_time = (
        step13_combined_file
        .stat()
        .st_mtime
    )


    # Only audit Step 13 when it was regenerated after
    # the corrected Step 11 output.
    if (
        step13_modification_time
        >= step11_modification_time
    ):

        step13_included = True

        print(
            "Step 13 is current and will be included "
            "in the audit."
        )


        step13_header = pd.read_csv(
            step13_combined_file,
            nrows=0
        )

        step13_columns = list(
            step13_header.columns
        )


        if "Chromosome" not in step13_columns:

            raise KeyError(
                "Step 13 combined table lacks "
                "'Chromosome'."
            )


        step13_use_columns = [
            column
            for column in [
                "Chromosome",
                "Peptide",
                "ProteinID",
                "GeneModel",
                "GeneID",
                "Gene_label"
            ]
            if column in step13_columns
        ]


        key = (
            "Step 13 final non-redundant validated table",
            "ALL",
            "bread wheat",
            "ALL",
            "ALL",
            step13_combined_file.name,
            "Final non-redundant validated rows"
        )


        for chunk_number, chunk in enumerate(

            pd.read_csv(
                step13_combined_file,
                usecols=step13_use_columns,
                chunksize=chunksize,
                low_memory=False
            ),

            start=1
        ):

            chromosome_normalised = (
                chunk[
                    "Chromosome"
                ]
                .map(
                    normalise_chr
                )
            )

            chrunknown_mask = (
                chromosome_normalised
                .eq("ChrUnknown")
            )


            update_record(
                step13_records,
                key,
                chunk,
                chrunknown_mask
            )


            if chunk_number % 20 == 0:

                print(
                    "  Step 13 chunks processed: "
                    f"{chunk_number}"
                )


    else:

        print(
            "Existing Step 13 output predates the corrected "
            "Step 11 output and will not be included yet."
        )

        print(
            "Rerun Step 11B after Steps 12 and 13 have "
            "been regenerated."
        )


else:

    print(
        "Step 13 file not found. "
        "Step 13 audit skipped."
    )


step13_summary = records_to_dataframe(
    step13_records
)


# -----------------------------
# 8. Combine, filter and export
# -----------------------------

summary_tables = [
    table
    for table in [
        step9_summary,
        step10_summary,
        step11_summary,
        step13_summary
    ]
    if not table.empty
]


if not summary_tables:

    raise ValueError(
        "No ChrUnknown audit records were generated."
    )


audit_summary = pd.concat(
    summary_tables,
    ignore_index=True
)


# Keep rows containing ChrUnknown evidence.
# Keep Step 13 when a current Step 13 table was audited.
audit_summary = audit_summary[
    (
        audit_summary[
            "ChrUnknown_rows"
        ]
        > 0
    )
    |
    (
        audit_summary[
            "Stage"
        ]
        .str.contains(
            "Step 13",
            regex=False
        )
    )
].copy()


audit_summary = (
    audit_summary
    .sort_values(
        [
            "Stage",
            "Source",
            "Tissue",
            "Projection_file",
            "Status_detail"
        ],
        na_position="last"
    )
    .reset_index(
        drop=True
    )
)


audit_summary.to_csv(
    summary_out,
    index=False
)


# -----------------------------
# 9. Concise stage summary
# -----------------------------

stage_totals = (
    audit_summary
    .groupby(
        [
            "Stage",
            "Status_detail"
        ],
        dropna=False,
        as_index=False
    )
    .agg(
        Total_rows=(
            "Total_rows",
            "sum"
        ),

        ChrUnknown_rows=(
            "ChrUnknown_rows",
            "sum"
        )
    )
)


print(
    "\n===== ChrUnknown VALIDATION FATE SUMMARY ====="
)

print(
    f"Summary saved: "
    f"{summary_out}"
)

if failed_examples_out.exists():

    print(
        f"Failed examples saved: "
        f"{failed_examples_out}"
    )

else:

    print(
        "No failed ChrUnknown example file was created "
        "because no ChrUnknown rows failed Step 11."
    )

print(
    f"Summary rows: "
    f"{len(audit_summary):,}"
)


if not step13_included:

    print(
        "\nStep 13 is not included in this audit yet."
    )


display(
    stage_totals
)

display(
    audit_summary
)


if not failed_examples_df.empty:

    print(
        "\nExample ChrUnknown rows failing "
        "Step 11 sanity checks:"
    )

    display(
        failed_examples_df.head(20)
    )

else:

    print(
        "\nNo ChrUnknown rows failed the corrected "
        "Step 11 sanity checks."
    )
```

    Auditing Step 9 projected rows...
    Auditing Step 10 translation-validation rows...
    Step 10 columns used: ['_22', 'Source', 'Species', 'Tissue', 'Batch', 'Chromosome', 'Validation_status', 'Peptide', 'ProteinID', 'GeneModel']
    Detected Step 10 projection-source column: _22
      Step 10 chunks processed: 20
      Step 10 chunks processed: 40
      Step 10 chunks processed: 60
      Step 10 chunks processed: 80
      Step 10 chunks processed: 100
      Step 10 chunks processed: 120
      Step 10 chunks processed: 140
      Step 10 chunks processed: 160
      Step 10 chunks processed: 180
      Step 10 chunks processed: 200
      Step 10 chunks processed: 220
      Step 10 chunks processed: 240
      Step 10 chunks processed: 260
      Step 10 chunks processed: 280
      Step 10 chunks processed: 300
      Step 10 chunks processed: 320
    Auditing corrected Step 11 sanity-check rows...
      Step 11 chunks processed: 20
      Step 11 chunks processed: 40
      Step 11 chunks processed: 60
      Step 11 chunks processed: 80
      Step 11 chunks processed: 100
      Step 11 chunks processed: 120
      Step 11 chunks processed: 140
      Step 11 chunks processed: 160
      Step 11 chunks processed: 180
      Step 11 chunks processed: 200
      Step 11 chunks processed: 220
      Step 11 chunks processed: 240
      Step 11 chunks processed: 260
      Step 11 chunks processed: 280
      Step 11 chunks processed: 300
      Step 11 chunks processed: 320
    Assessing Step 13 final nonredundant table...
    Step 13 is current and will be included in the audit.
      Step 13 chunks processed: 20
      Step 13 chunks processed: 40
      Step 13 chunks processed: 60
      Step 13 chunks processed: 80
      Step 13 chunks processed: 100
      Step 13 chunks processed: 120
    
    ===== ChrUnknown VALIDATION FATE SUMMARY =====
    Summary saved: python_outputs\tables\wheat_ChrUnknown_validation_fate_summary_step11B.csv
    No failed ChrUnknown example file was created because no ChrUnknown rows failed Step 11.
    Summary rows: 128
    


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
      <th>Stage</th>
      <th>Status_detail</th>
      <th>Total_rows</th>
      <th>ChrUnknown_rows</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Step 10 translation validation</td>
      <td>Validation_status == translation_mismatch</td>
      <td>76721</td>
      <td>2102</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Step 10 translation validation</td>
      <td>Validation_status == validated</td>
      <td>8214230</td>
      <td>77543</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Step 11 sanity checks</td>
      <td>Sanity_check_status == passed</td>
      <td>8214230</td>
      <td>77543</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Step 13 final non-redundant validated table</td>
      <td>Final non-redundant validated rows</td>
      <td>3173811</td>
      <td>34908</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Step 9 projected rows</td>
      <td>Projection_status == projected</td>
      <td>8291056</td>
      <td>79645</td>
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
      <th>Stage</th>
      <th>Source</th>
      <th>Species</th>
      <th>Tissue</th>
      <th>Batch</th>
      <th>Projection_file</th>
      <th>Status_detail</th>
      <th>Total_rows</th>
      <th>ChrUnknown_rows</th>
      <th>ChrUnknown_percent_rows</th>
      <th>ChrUnknown_unique_peptides</th>
      <th>ChrUnknown_unique_proteins</th>
      <th>ChrUnknown_unique_gene_models</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Step 10 translation validation</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>Step10_global_table</td>
      <td>Validation_status == translation_mismatch</td>
      <td>422</td>
      <td>16</td>
      <td>3.7915</td>
      <td>13</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Step 10 translation validation</td>
      <td>MSV000090572</td>
      <td>bread wheat</td>
      <td>stored_grain</td>
      <td>single</td>
      <td>Step10_global_table</td>
      <td>Validation_status == validated</td>
      <td>29892</td>
      <td>462</td>
      <td>1.5456</td>
      <td>209</td>
      <td>291</td>
      <td>273</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Step 10 translation validation</td>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>Step10_global_table</td>
      <td>Validation_status == translation_mismatch</td>
      <td>898</td>
      <td>19</td>
      <td>2.1158</td>
      <td>18</td>
      <td>13</td>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Step 10 translation validation</td>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>Step10_global_table</td>
      <td>Validation_status == validated</td>
      <td>163467</td>
      <td>1512</td>
      <td>0.9250</td>
      <td>696</td>
      <td>467</td>
      <td>437</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Step 10 translation validation</td>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>Step10_global_table</td>
      <td>Validation_status == validated</td>
      <td>13137</td>
      <td>113</td>
      <td>0.8602</td>
      <td>69</td>
      <td>98</td>
      <td>88</td>
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
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Step 9 projected rows</td>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>Projection_status == projected</td>
      <td>188826</td>
      <td>1666</td>
      <td>0.8823</td>
      <td>749</td>
      <td>511</td>
      <td>469</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Step 9 projected rows</td>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>Projection_status == projected</td>
      <td>60734</td>
      <td>572</td>
      <td>0.9418</td>
      <td>304</td>
      <td>349</td>
      <td>329</td>
    </tr>
    <tr>
      <th>125</th>
      <td>Step 9 projected rows</td>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>Projection_status == projected</td>
      <td>1850136</td>
      <td>17731</td>
      <td>0.9584</td>
      <td>10538</td>
      <td>4324</td>
      <td>4180</td>
    </tr>
    <tr>
      <th>126</th>
      <td>Step 9 projected rows</td>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>Projection_status == projected</td>
      <td>1886922</td>
      <td>18421</td>
      <td>0.9762</td>
      <td>10806</td>
      <td>4452</td>
      <td>4309</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Step 9 projected rows</td>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>Projection_status == projected</td>
      <td>1062508</td>
      <td>10116</td>
      <td>0.9521</td>
      <td>5891</td>
      <td>3509</td>
      <td>3379</td>
    </tr>
  </tbody>
</table>
<p>128 rows × 13 columns</p>
</div>


    
    No ChrUnknown rows failed the corrected Step 11 sanity checks.
    

# Step 12 — Export BED6 and BED12 Files for JBrowse

This step converts successfully projected peptide genomic coordinates from Step 10 into BED files for genome browser visualisation.

Both BED6 and BED12 formats were generated for each wheat tissue.

---

## Input files

### Peptide genome projection table from Step 11


```text
wheat_projection_validation_stratified100percent_step10.csv
```

Only rows with translation-validated genomic projection were exported.

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
wheat_bed_export_summary_step12.csv
```

The resulting BED6 and BED12 files can be loaded into JBrowse to visualise peptide evidence aligned to the wheat genome.


```python
# ============================================================
# Step 12 — Export fully validated BED6 and BED12 files
# for JBrowse (takes approximately 30 min)
#
# Translation-validated + sanity-check-passed projections only
# Includes valid ChrUnknown projections.
# ============================================================

import pandas as pd
from pathlib import Path


# -----------------------------
# 1. Input / output paths
# -----------------------------

fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")

# Final BED outputs after both validation layers:
# Step 10 translation validation + Step 11 sanity checks
bed_dir = Path("python_outputs/bed_validated")
bed_dir.mkdir(
    parents=True,
    exist_ok=True
)

manifest_file = (
    fragpipe_dir
    / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"
)

# Corrected Step 11 output
sanity_file = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"
)

# Original Step 12 summary filename
step12_summary_out = (
    tables_dir
    / "wheat_bed_export_validated_summary_step12.csv"
)

chunk_size = 100_000


# -----------------------------
# 2. Load manifest and confirm Step 11 input
# -----------------------------

manifest = pd.read_csv(
    manifest_file,
    encoding="utf-8-sig"
)

if not sanity_file.exists():

    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n"
        f"{sanity_file}\n\n"
        "Please run the corrected Step 11 first."
    )


# Confirm that this is the corrected Step 11 output.
step11_header = pd.read_csv(
    sanity_file,
    nrows=0
)

required_step11_cols = [
    "Projection_file",
    "Chromosome",
    "Sanity_check_status",
    "All_sanity_checks_passed",
    "Check_chromosome_and_strand"
]

missing_step11_cols = [
    col
    for col in required_step11_cols
    if col not in step11_header.columns
]

if missing_step11_cols:

    raise KeyError(
        "Missing required Step 11 column(s): "
        f"{missing_step11_cols}"
    )


# -----------------------------
# 3. Helper functions
# -----------------------------

def make_bed_score(data):
    """
    Create BED score between 0 and 1000.

    Priority:
    1. Probability column scaled to 0–1000, if available
    2. Default score = 1000
    """

    if "Probability" in data.columns:

        score = (
            pd.to_numeric(
                data["Probability"],
                errors="coerce"
            )
            * 1000
        )

        score = (
            score
            .fillna(1000)
            .clip(0, 1000)
            .round()
            .astype(int)
        )

    else:

        score = pd.Series(
            [1000] * len(data),
            index=data.index
        )

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
    1. Peptide_intron_gapped, if present
    2. Peptide_intron_gapped_compact, if present
    3. Peptide

    Final structure:
    peptide|protein|gene|validated=translation+sanity|tissues=X
    """

    if (
        "Peptide_intron_gapped"
        in projected.columns
    ):

        peptide_label = (
            projected[
                "Peptide_intron_gapped"
            ]
            .astype(str)
        )

    elif (
        "Peptide_intron_gapped_compact"
        in projected.columns
    ):

        peptide_label = (
            projected[
                "Peptide_intron_gapped_compact"
            ]
            .astype(str)
        )

    else:

        peptide_label = (
            projected["Peptide"]
            .astype(str)
        )


    if "GeneID" in projected.columns:

        bed_name = (
            peptide_label
            + "|"
            + projected["ProteinID"].astype(str)
            + "|"
            + projected["GeneID"].astype(str)
        )

    elif "GeneModel" in projected.columns:

        bed_name = (
            peptide_label
            + "|"
            + projected["ProteinID"].astype(str)
            + "|"
            + projected["GeneModel"].astype(str)
        )

    else:

        bed_name = (
            peptide_label
            + "|"
            + projected["ProteinID"].astype(str)
        )


    bed_name = (
        bed_name
        + "|validated=translation+sanity"
    )


    if "Tissues_count" in projected.columns:

        bed_name = (
            bed_name
            + "|tissues="
            + projected[
                "Tissues_count"
            ]
            .astype(str)
        )


    return bed_name.apply(
        clean_bed_name
    )


def prepare_bed_rows(projected):
    """
    Prepare a sanity-passed DataFrame for BED6/BED12 export.
    """

    required_cols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "ProteinID",
        "Strand",
        "BED_block_count",
        "BED_block_sizes",
        "BED_block_starts",
        "Peptide",
        "Sanity_check_status",
        "All_sanity_checks_passed"
    ]

    missing_cols = [
        col
        for col in required_cols
        if col not in projected.columns
    ]

    if missing_cols:

        raise KeyError(
            f"Missing required BED column(s): "
            f"{missing_cols}"
        )


    projected = projected.copy()


    # Create BED score and label.
    projected[
        "BED_score"
    ] = make_bed_score(
        projected
    )

    projected[
        "BED_name"
    ] = build_bed_name(
        projected
    )


    # Force integer coordinate types.
    projected[
        "BED_start_0based"
    ] = (
        pd.to_numeric(
            projected[
                "BED_start_0based"
            ],
            errors="coerce"
        )
        .astype("Int64")
    )

    projected[
        "BED_end_0based_exclusive"
    ] = (
        pd.to_numeric(
            projected[
                "BED_end_0based_exclusive"
            ],
            errors="coerce"
        )
        .astype("Int64")
    )

    projected[
        "BED_block_count"
    ] = (
        pd.to_numeric(
            projected[
                "BED_block_count"
            ],
            errors="coerce"
        )
        .astype("Int64")
    )


    # Drop rows with missing essential BED fields,
    # as a final defensive check.
    before_drop = len(
        projected
    )

    projected = projected.dropna(
        subset=[
            "Chromosome",
            "BED_start_0based",
            "BED_end_0based_exclusive",
            "Strand",
            "BED_block_count",
            "BED_block_sizes",
            "BED_block_starts"
        ]
    ).copy()

    dropped_missing_bed_fields = (
        before_drop
        - len(projected)
    )


    projected[
        "BED_start_0based"
    ] = (
        projected[
            "BED_start_0based"
        ]
        .astype(int)
    )

    projected[
        "BED_end_0based_exclusive"
    ] = (
        projected[
            "BED_end_0based_exclusive"
        ]
        .astype(int)
    )

    projected[
        "BED_block_count"
    ] = (
        projected[
            "BED_block_count"
        ]
        .astype(int)
    )


    return (
        projected,
        dropped_missing_bed_fields
    )


def make_bed6(projected):
    """
    Build BED6 DataFrame.
    """

    return projected[[
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_name",
        "BED_score",
        "Strand"
    ]].copy()


def make_bed12(projected):
    """
    Build BED12 DataFrame.
    """

    return pd.DataFrame({

        "chrom":
            projected["Chromosome"],

        "chromStart":
            projected[
                "BED_start_0based"
            ],

        "chromEnd":
            projected[
                "BED_end_0based_exclusive"
            ],

        "name":
            projected["BED_name"],

        "score":
            projected["BED_score"],

        "strand":
            projected["Strand"],

        "thickStart":
            projected[
                "BED_start_0based"
            ],

        "thickEnd":
            projected[
                "BED_end_0based_exclusive"
            ],

        "itemRgb":
            "0",

        "blockCount":
            projected[
                "BED_block_count"
            ],

        "blockSizes":
            projected[
                "BED_block_sizes"
            ],

        "blockStarts":
            projected[
                "BED_block_starts"
            ]
    })


# -----------------------------
# 4. Build manifest lookup and output filenames
# -----------------------------

manifest_lookup = {}

for _, row in manifest.iterrows():

    projection_filename = (
        row[
            "FragPipe-Output-Peptide"
        ]
        .replace(
            "_peptide.tsv",
            "_peptide_genome_projection.csv"
        )
    )


    bed6_filename = (
        projection_filename
        .replace(
            "_peptide_genome_projection.csv",
            "_validated_peptides.bed6"
        )
    )


    bed12_filename = (
        projection_filename
        .replace(
            "_peptide_genome_projection.csv",
            "_validated_peptides.bed12"
        )
    )


    manifest_lookup[
        projection_filename
    ] = {
        "Source":
            row["Source"],

        "Species":
            row["Species"],

        "Tissue":
            row["Tissue-Raw-Code"],

        "Batch":
            row["Batch"],

        "BED6_file":
            bed6_filename,

        "BED12_file":
            bed12_filename,

        "BED6_path":
            bed_dir / bed6_filename,

        "BED12_path":
            bed_dir / bed12_filename
    }


# -----------------------------
# 5. Overwrite previous Step 12 outputs
# -----------------------------

for info in manifest_lookup.values():

    for path_key in [
        "BED6_path",
        "BED12_path"
    ]:

        output_path = info[
            path_key
        ]

        if output_path.exists():
            output_path.unlink()


if step12_summary_out.exists():
    step12_summary_out.unlink()


# -----------------------------
# 6. Initialise summary dictionary
# -----------------------------

summary_dict = {}


for projection_filename, info in manifest_lookup.items():

    summary_dict[
        projection_filename
    ] = {
        "Source":
            info["Source"],

        "Species":
            info["Species"],

        "Tissue":
            info["Tissue"],

        "Batch":
            info["Batch"],

        "Projection_file":
            projection_filename,

        "BED6_file":
            info["BED6_file"],

        "BED12_file":
            info["BED12_file"],

        "Rows_in_step11_sanity_file":
            0,

        "Rows_passing_all_sanity_checks":
            0,

        "Rows_excluded_by_sanity_checks":
            0,

        "Rows_dropped_missing_BED_fields":
            0,

        "BED_rows":
            0,

        "Unique_BED_peptides":
            0,

        "Unique_BED_proteins":
            0,

        "Unique_BED_gene_models":
            0,

        "Multi_block_peptides":
            0,

        "Within_exon_peptides":
            0,

        "Intron_spanning_BED_rows":
            0,

        "Within_exon_BED_rows":
            0,

        "Unique_intron_spanning_peptides":
            0,

        "Unique_within_exon_peptides":
            0,

        "BED_labels_with_introns":
            0
    }


# Unique counts across chunks.
unique_peptides = {
    key: set()
    for key in manifest_lookup
}

unique_proteins = {
    key: set()
    for key in manifest_lookup
}

unique_genes = {
    key: set()
    for key in manifest_lookup
}

unique_intron_spanning_peptides = {
    key: set()
    for key in manifest_lookup
}

unique_within_exon_peptides = {
    key: set()
    for key in manifest_lookup
}


# -----------------------------
# 7. Read corrected Step 11 output in chunks
# -----------------------------

print(
    "\nExporting BED6/BED12 files from corrected "
    "Step 11 sanity-passed rows..."
)


total_rows_read = 0
total_sanity_passed = 0
total_sanity_failed = 0
total_bed_rows = 0
total_rows_dropped_missing_bed_fields = 0
total_chrunknown_bed_rows = 0


for chunk_number, chunk in enumerate(

    pd.read_csv(
        sanity_file,
        chunksize=chunk_size,
        low_memory=False
    ),

    start=1
):

    total_rows_read += len(
        chunk
    )


    # Count sanity status per projection file.
    for projection_filename, file_group in chunk.groupby(
        "Projection_file"
    ):

        projection_filename = str(
            projection_filename
        )

        if projection_filename not in summary_dict:
            continue


        number_rows = len(
            file_group
        )

        number_passed = int(
            (
                file_group[
                    "Sanity_check_status"
                ]
                .astype(str)
                == "passed"
            ).sum()
        )

        number_failed = (
            number_rows
            - number_passed
        )


        summary_dict[
            projection_filename
        ][
            "Rows_in_step11_sanity_file"
        ] += number_rows

        summary_dict[
            projection_filename
        ][
            "Rows_passing_all_sanity_checks"
        ] += number_passed

        summary_dict[
            projection_filename
        ][
            "Rows_excluded_by_sanity_checks"
        ] += number_failed


    # Keep only rows passing all sanity checks.
    passed = chunk[
        chunk[
            "Sanity_check_status"
        ]
        .astype(str)
        == "passed"
    ].copy()


    total_sanity_passed += len(
        passed
    )

    total_sanity_failed += (
        len(chunk)
        - len(passed)
    )


    if passed.empty:

        print(
            f"Chunk {chunk_number}: "
            f"read {len(chunk):,} rows | "
            "no sanity-passed rows"
        )

        continue


    # Export each source–tissue projection file.
    for projection_filename, projected in passed.groupby(
        "Projection_file"
    ):

        projection_filename = str(
            projection_filename
        )


        if projection_filename not in manifest_lookup:

            print(
                "Warning: projection file not found in "
                "manifest, skipped: "
                f"{projection_filename}"
            )

            continue


        info = manifest_lookup[
            projection_filename
        ]


        (
            projected_prepared,
            dropped_missing_bed_fields
        ) = prepare_bed_rows(
            projected
        )


        summary_dict[
            projection_filename
        ][
            "Rows_dropped_missing_BED_fields"
        ] += dropped_missing_bed_fields


        total_rows_dropped_missing_bed_fields += (
            dropped_missing_bed_fields
        )


        if projected_prepared.empty:
            continue


        bed6 = make_bed6(
            projected_prepared
        )

        bed12 = make_bed12(
            projected_prepared
        )


        # Append to BED6.
        bed6.to_csv(
            info["BED6_path"],
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )


        # Append to BED12.
        bed12.to_csv(
            info["BED12_path"],
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )


        # Update summary.
        number_bed_rows = len(
            projected_prepared
        )

        summary_dict[
            projection_filename
        ][
            "BED_rows"
        ] += number_bed_rows


        total_bed_rows += (
            number_bed_rows
        )


        # Count ChrUnknown rows exported.
        number_chrunknown_rows = int(
            (
                projected_prepared[
                    "Chromosome"
                ]
                .astype(str)
                .str.strip()
                == "ChrUnknown"
            ).sum()
        )

        total_chrunknown_bed_rows += (
            number_chrunknown_rows
        )


        if "Peptide" in projected_prepared.columns:

            unique_peptides[
                projection_filename
            ].update(
                projected_prepared[
                    "Peptide"
                ]
                .dropna()
                .astype(str)
                .unique()
            )


        if "ProteinID" in projected_prepared.columns:

            unique_proteins[
                projection_filename
            ].update(
                projected_prepared[
                    "ProteinID"
                ]
                .dropna()
                .astype(str)
                .unique()
            )


        if "GeneID" in projected_prepared.columns:

            unique_genes[
                projection_filename
            ].update(
                projected_prepared[
                    "GeneID"
                ]
                .dropna()
                .astype(str)
                .unique()
            )

        elif "GeneModel" in projected_prepared.columns:

            unique_genes[
                projection_filename
            ].update(
                projected_prepared[
                    "GeneModel"
                ]
                .dropna()
                .astype(str)
                .unique()
            )


        # Count exon structure.
        block_count = pd.to_numeric(
            projected_prepared[
                "BED_block_count"
            ],
            errors="coerce"
        )


        intron_spanning_mask = (
            block_count > 1
        )

        within_exon_mask = (
            block_count == 1
        )


        intron_spanning_rows = int(
            intron_spanning_mask.sum()
        )

        within_exon_rows = int(
            within_exon_mask.sum()
        )


        # Existing legacy-style count retained.
        summary_dict[
            projection_filename
        ][
            "Multi_block_peptides"
        ] += intron_spanning_rows


        summary_dict[
            projection_filename
        ][
            "Within_exon_peptides"
        ] += within_exon_rows


        summary_dict[
            projection_filename
        ][
            "Intron_spanning_BED_rows"
        ] += intron_spanning_rows


        summary_dict[
            projection_filename
        ][
            "Within_exon_BED_rows"
        ] += within_exon_rows


        if "Peptide" in projected_prepared.columns:

            unique_intron_spanning_peptides[
                projection_filename
            ].update(
                projected_prepared.loc[
                    intron_spanning_mask,
                    "Peptide"
                ]
                .dropna()
                .astype(str)
                .unique()
            )


            unique_within_exon_peptides[
                projection_filename
            ].update(
                projected_prepared.loc[
                    within_exon_mask,
                    "Peptide"
                ]
                .dropna()
                .astype(str)
                .unique()
            )


        # BED labels containing dashes remain a visual proxy.
        summary_dict[
            projection_filename
        ][
            "BED_labels_with_introns"
        ] += int(
            projected_prepared[
                "BED_name"
            ]
            .astype(str)
            .str.contains(
                "-",
                regex=False
            )
            .sum()
        )


    print(
        f"Chunk {chunk_number}: "
        f"read {len(chunk):,} rows | "
        f"sanity-passed {len(passed):,} | "
        f"cumulative BED rows {total_bed_rows:,} | "
        f"cumulative ChrUnknown rows "
        f"{total_chrunknown_bed_rows:,}"
    )


# -----------------------------
# 8. Finalise summary table
# -----------------------------

for projection_filename in summary_dict:

    summary_dict[
        projection_filename
    ][
        "Unique_BED_peptides"
    ] = len(
        unique_peptides[
            projection_filename
        ]
    )


    summary_dict[
        projection_filename
    ][
        "Unique_BED_proteins"
    ] = len(
        unique_proteins[
            projection_filename
        ]
    )


    summary_dict[
        projection_filename
    ][
        "Unique_BED_gene_models"
    ] = len(
        unique_genes[
            projection_filename
        ]
    )


    summary_dict[
        projection_filename
    ][
        "Unique_intron_spanning_peptides"
    ] = len(
        unique_intron_spanning_peptides[
            projection_filename
        ]
    )


    summary_dict[
        projection_filename
    ][
        "Unique_within_exon_peptides"
    ] = len(
        unique_within_exon_peptides[
            projection_filename
        ]
    )


step12_summary = pd.DataFrame(
    summary_dict.values()
)


step12_summary[
    "Percent_sanity_passed"
] = (
    step12_summary[
        "Rows_passing_all_sanity_checks"
    ]
    / step12_summary[
        "Rows_in_step11_sanity_file"
    ]
    * 100
).round(4)


step12_summary[
    "Percent_exported_to_BED"
] = (
    step12_summary[
        "BED_rows"
    ]
    / step12_summary[
        "Rows_in_step11_sanity_file"
    ]
    * 100
).round(4)


step12_summary.to_csv(
    step12_summary_out,
    index=False
)


# -----------------------------
# 9. Integrity checks
# -----------------------------

expected_bed_rows = (
    total_sanity_passed
    - total_rows_dropped_missing_bed_fields
)


if total_bed_rows != expected_bed_rows:

    raise ValueError(
        "Step 12 row-accounting mismatch:\n"
        f"Rows passing sanity checks: "
        f"{total_sanity_passed:,}\n"
        f"Rows dropped for missing BED fields: "
        f"{total_rows_dropped_missing_bed_fields:,}\n"
        f"Expected BED rows: "
        f"{expected_bed_rows:,}\n"
        f"Actual BED rows: "
        f"{total_bed_rows:,}"
    )


if total_chrunknown_bed_rows != 77_543:

    print(
        "\nWARNING: expected 77,543 ChrUnknown rows "
        "from corrected Step 11, but Step 12 exported "
        f"{total_chrunknown_bed_rows:,}."
    )

else:

    print(
        "\nChrUnknown export check passed: "
        "77,543 rows exported."
    )


# -----------------------------
# 10. Overall summary
# -----------------------------

overall_bed_files_bed6 = len(
    list(
        bed_dir.glob(
            "*_validated_peptides.bed6"
        )
    )
)

overall_bed_files_bed12 = len(
    list(
        bed_dir.glob(
            "*_validated_peptides.bed12"
        )
    )
)


print(
    "\n===== STEP 12 VALIDATED BED EXPORT SUMMARY ====="
)

print(
    "Rows read from Step 11 sanity-check table: "
    f"{total_rows_read:,}"
)

print(
    "Rows passing all sanity checks: "
    f"{total_sanity_passed:,}"
)

print(
    "Rows excluded by sanity checks: "
    f"{total_sanity_failed:,}"
)

print(
    "Rows dropped for missing essential BED fields: "
    f"{total_rows_dropped_missing_bed_fields:,}"
)

print(
    "Rows exported to BED: "
    f"{total_bed_rows:,}"
)

print(
    "ChrUnknown rows exported to BED: "
    f"{total_chrunknown_bed_rows:,}"
)

print(
    "BED6 files created: "
    f"{overall_bed_files_bed6:,}"
)

print(
    "BED12 files created: "
    f"{overall_bed_files_bed12:,}"
)

print(
    f"\nBED files saved in: "
    f"{bed_dir}"
)

print(
    f"Step 12 summary saved: "
    f"{step12_summary_out}"
)


display(
    step12_summary
)
```

    
    Exporting BED6/BED12 files from corrected Step 11 sanity-passed rows...
    Chunk 1: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 100,000 | cumulative ChrUnknown rows 897
    Chunk 2: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 200,000 | cumulative ChrUnknown rows 1,855
    Chunk 3: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 300,000 | cumulative ChrUnknown rows 2,890
    Chunk 4: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 400,000 | cumulative ChrUnknown rows 3,818
    Chunk 5: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 500,000 | cumulative ChrUnknown rows 4,677
    Chunk 6: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 600,000 | cumulative ChrUnknown rows 5,839
    Chunk 7: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 700,000 | cumulative ChrUnknown rows 6,812
    Chunk 8: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 800,000 | cumulative ChrUnknown rows 7,676
    Chunk 9: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 900,000 | cumulative ChrUnknown rows 8,452
    Chunk 10: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,000,000 | cumulative ChrUnknown rows 9,198
    Chunk 11: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,100,000 | cumulative ChrUnknown rows 10,038
    Chunk 12: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,200,000 | cumulative ChrUnknown rows 10,950
    Chunk 13: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,300,000 | cumulative ChrUnknown rows 11,757
    Chunk 14: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,400,000 | cumulative ChrUnknown rows 12,852
    Chunk 15: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,500,000 | cumulative ChrUnknown rows 14,015
    Chunk 16: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,600,000 | cumulative ChrUnknown rows 15,118
    Chunk 17: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,700,000 | cumulative ChrUnknown rows 16,139
    Chunk 18: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,800,000 | cumulative ChrUnknown rows 17,080
    Chunk 19: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 1,900,000 | cumulative ChrUnknown rows 18,113
    Chunk 20: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,000,000 | cumulative ChrUnknown rows 19,303
    Chunk 21: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,100,000 | cumulative ChrUnknown rows 20,378
    Chunk 22: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,200,000 | cumulative ChrUnknown rows 21,360
    Chunk 23: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,300,000 | cumulative ChrUnknown rows 22,322
    Chunk 24: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,400,000 | cumulative ChrUnknown rows 23,267
    Chunk 25: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,500,000 | cumulative ChrUnknown rows 24,277
    Chunk 26: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,600,000 | cumulative ChrUnknown rows 25,071
    Chunk 27: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,700,000 | cumulative ChrUnknown rows 25,849
    Chunk 28: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,800,000 | cumulative ChrUnknown rows 26,941
    Chunk 29: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 2,900,000 | cumulative ChrUnknown rows 27,865
    Chunk 30: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,000,000 | cumulative ChrUnknown rows 28,572
    Chunk 31: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,100,000 | cumulative ChrUnknown rows 29,252
    Chunk 32: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,200,000 | cumulative ChrUnknown rows 30,167
    Chunk 33: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,300,000 | cumulative ChrUnknown rows 31,031
    Chunk 34: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,400,000 | cumulative ChrUnknown rows 31,934
    Chunk 35: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,500,000 | cumulative ChrUnknown rows 32,786
    Chunk 36: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,600,000 | cumulative ChrUnknown rows 33,617
    Chunk 37: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,700,000 | cumulative ChrUnknown rows 34,503
    Chunk 38: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,800,000 | cumulative ChrUnknown rows 35,321
    Chunk 39: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 3,900,000 | cumulative ChrUnknown rows 36,264
    Chunk 40: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,000,000 | cumulative ChrUnknown rows 37,307
    Chunk 41: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,100,000 | cumulative ChrUnknown rows 38,310
    Chunk 42: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,200,000 | cumulative ChrUnknown rows 39,203
    Chunk 43: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,300,000 | cumulative ChrUnknown rows 40,161
    Chunk 44: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,400,000 | cumulative ChrUnknown rows 41,033
    Chunk 45: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,500,000 | cumulative ChrUnknown rows 42,214
    Chunk 46: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,600,000 | cumulative ChrUnknown rows 43,351
    Chunk 47: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,700,000 | cumulative ChrUnknown rows 44,403
    Chunk 48: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,800,000 | cumulative ChrUnknown rows 45,317
    Chunk 49: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 4,900,000 | cumulative ChrUnknown rows 46,309
    Chunk 50: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,000,000 | cumulative ChrUnknown rows 47,110
    Chunk 51: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,100,000 | cumulative ChrUnknown rows 47,971
    Chunk 52: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,200,000 | cumulative ChrUnknown rows 48,844
    Chunk 53: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,300,000 | cumulative ChrUnknown rows 49,743
    Chunk 54: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,400,000 | cumulative ChrUnknown rows 50,645
    Chunk 55: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,500,000 | cumulative ChrUnknown rows 51,579
    Chunk 56: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,600,000 | cumulative ChrUnknown rows 52,397
    Chunk 57: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,700,000 | cumulative ChrUnknown rows 53,341
    Chunk 58: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,800,000 | cumulative ChrUnknown rows 54,193
    Chunk 59: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 5,900,000 | cumulative ChrUnknown rows 55,253
    Chunk 60: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,000,000 | cumulative ChrUnknown rows 56,293
    Chunk 61: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,100,000 | cumulative ChrUnknown rows 57,296
    Chunk 62: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,200,000 | cumulative ChrUnknown rows 58,220
    Chunk 63: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,300,000 | cumulative ChrUnknown rows 59,274
    Chunk 64: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,400,000 | cumulative ChrUnknown rows 60,564
    Chunk 65: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,500,000 | cumulative ChrUnknown rows 61,584
    Chunk 66: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,600,000 | cumulative ChrUnknown rows 62,587
    Chunk 67: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,700,000 | cumulative ChrUnknown rows 63,549
    Chunk 68: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,800,000 | cumulative ChrUnknown rows 64,390
    Chunk 69: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 6,900,000 | cumulative ChrUnknown rows 65,191
    Chunk 70: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,000,000 | cumulative ChrUnknown rows 66,038
    Chunk 71: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,100,000 | cumulative ChrUnknown rows 66,897
    Chunk 72: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,200,000 | cumulative ChrUnknown rows 67,838
    Chunk 73: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,300,000 | cumulative ChrUnknown rows 68,698
    Chunk 74: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,400,000 | cumulative ChrUnknown rows 69,545
    Chunk 75: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,500,000 | cumulative ChrUnknown rows 70,558
    Chunk 76: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,600,000 | cumulative ChrUnknown rows 71,510
    Chunk 77: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,700,000 | cumulative ChrUnknown rows 72,409
    Chunk 78: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,800,000 | cumulative ChrUnknown rows 73,590
    Chunk 79: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 7,900,000 | cumulative ChrUnknown rows 74,653
    Chunk 80: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 8,000,000 | cumulative ChrUnknown rows 75,436
    Chunk 81: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 8,100,000 | cumulative ChrUnknown rows 76,325
    Chunk 82: read 100,000 rows | sanity-passed 100,000 | cumulative BED rows 8,200,000 | cumulative ChrUnknown rows 77,330
    Chunk 83: read 14,230 rows | sanity-passed 14,230 | cumulative BED rows 8,214,230 | cumulative ChrUnknown rows 77,543
    
    ChrUnknown export check passed: 77,543 rows exported.
    
    ===== STEP 12 VALIDATED BED EXPORT SUMMARY =====
    Rows read from Step 11 sanity-check table: 8,214,230
    Rows passing all sanity checks: 8,214,230
    Rows excluded by sanity checks: 0
    Rows dropped for missing essential BED fields: 0
    Rows exported to BED: 8,214,230
    ChrUnknown rows exported to BED: 77,543
    BED6 files created: 33
    BED12 files created: 33
    
    BED files saved in: python_outputs\bed_validated
    Step 12 summary saved: python_outputs\tables\wheat_bed_export_validated_summary_step12.csv
    


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
      <th>Rows_in_step11_sanity_file</th>
      <th>Rows_passing_all_sanity_checks</th>
      <th>Rows_excluded_by_sanity_checks</th>
      <th>...</th>
      <th>Unique_BED_gene_models</th>
      <th>Multi_block_peptides</th>
      <th>Within_exon_peptides</th>
      <th>Intron_spanning_BED_rows</th>
      <th>Within_exon_BED_rows</th>
      <th>Unique_intron_spanning_peptides</th>
      <th>Unique_within_exon_peptides</th>
      <th>BED_labels_with_introns</th>
      <th>Percent_sanity_passed</th>
      <th>Percent_exported_to_BED</th>
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
      <td>FragPipe_Vincent_MSV000090572_stored-grain_val...</td>
      <td>FragPipe_Vincent_MSV000090572_stored-grain_val...</td>
      <td>29892</td>
      <td>29892</td>
      <td>0</td>
      <td>...</td>
      <td>14536</td>
      <td>3262</td>
      <td>26630</td>
      <td>3262</td>
      <td>26630</td>
      <td>1082</td>
      <td>8075</td>
      <td>1805</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_validated_pe...</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_validated_pe...</td>
      <td>1829196</td>
      <td>1829196</td>
      <td>0</td>
      <td>...</td>
      <td>206142</td>
      <td>227461</td>
      <td>1601735</td>
      <td>227461</td>
      <td>1601735</td>
      <td>65152</td>
      <td>511674</td>
      <td>121858</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>FragPipe_Liu_PXD050500_node_validated_peptides...</td>
      <td>FragPipe_Liu_PXD050500_node_validated_peptides...</td>
      <td>1864415</td>
      <td>1864415</td>
      <td>0</td>
      <td>...</td>
      <td>209468</td>
      <td>234600</td>
      <td>1629815</td>
      <td>234600</td>
      <td>1629815</td>
      <td>66853</td>
      <td>522581</td>
      <td>126430</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>FragPipe_Liu_PXD050500_radicle_validated_pepti...</td>
      <td>FragPipe_Liu_PXD050500_radicle_validated_pepti...</td>
      <td>1050178</td>
      <td>1050178</td>
      <td>0</td>
      <td>...</td>
      <td>175179</td>
      <td>117686</td>
      <td>932492</td>
      <td>117686</td>
      <td>932492</td>
      <td>34041</td>
      <td>295733</td>
      <td>62041</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
      <td>FragPipe_Duncan_PXD004720_anther_validated_pep...</td>
      <td>FragPipe_Duncan_PXD004720_anther_validated_pep...</td>
      <td>163467</td>
      <td>163467</td>
      <td>0</td>
      <td>...</td>
      <td>28845</td>
      <td>27708</td>
      <td>135759</td>
      <td>27708</td>
      <td>135759</td>
      <td>6317</td>
      <td>27896</td>
      <td>16117</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
      <td>FragPipe_Duncan_PXD004720_boot_validated_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_boot_validated_pepti...</td>
      <td>13137</td>
      <td>13137</td>
      <td>0</td>
      <td>...</td>
      <td>7279</td>
      <td>2723</td>
      <td>10414</td>
      <td>2723</td>
      <td>10414</td>
      <td>712</td>
      <td>2899</td>
      <td>1535</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_validated...</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_validated...</td>
      <td>203264</td>
      <td>203264</td>
      <td>0</td>
      <td>...</td>
      <td>36208</td>
      <td>31278</td>
      <td>171986</td>
      <td>31278</td>
      <td>171986</td>
      <td>6794</td>
      <td>34380</td>
      <td>18631</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
      <td>FragPipe_Duncan_PXD004720_embryo_validated_pep...</td>
      <td>FragPipe_Duncan_PXD004720_embryo_validated_pep...</td>
      <td>8742</td>
      <td>8742</td>
      <td>0</td>
      <td>...</td>
      <td>5749</td>
      <td>1407</td>
      <td>7335</td>
      <td>1407</td>
      <td>7335</td>
      <td>385</td>
      <td>2444</td>
      <td>758</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_validated_...</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_validated_...</td>
      <td>102289</td>
      <td>102289</td>
      <td>0</td>
      <td>...</td>
      <td>21529</td>
      <td>14237</td>
      <td>88052</td>
      <td>14237</td>
      <td>88052</td>
      <td>3068</td>
      <td>17038</td>
      <td>7947</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
      <td>FragPipe_Duncan_PXD004720_glume_validated_pept...</td>
      <td>FragPipe_Duncan_PXD004720_glume_validated_pept...</td>
      <td>144079</td>
      <td>144079</td>
      <td>0</td>
      <td>...</td>
      <td>28205</td>
      <td>22077</td>
      <td>122002</td>
      <td>22077</td>
      <td>122002</td>
      <td>5086</td>
      <td>23657</td>
      <td>12720</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_vali...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_vali...</td>
      <td>125355</td>
      <td>125355</td>
      <td>0</td>
      <td>...</td>
      <td>28080</td>
      <td>17442</td>
      <td>107913</td>
      <td>17442</td>
      <td>107913</td>
      <td>3874</td>
      <td>22361</td>
      <td>9870</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_vali...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_vali...</td>
      <td>178814</td>
      <td>178814</td>
      <td>0</td>
      <td>...</td>
      <td>36269</td>
      <td>27602</td>
      <td>151212</td>
      <td>27602</td>
      <td>151212</td>
      <td>5776</td>
      <td>30293</td>
      <td>15938</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_vali...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_vali...</td>
      <td>132081</td>
      <td>132081</td>
      <td>0</td>
      <td>...</td>
      <td>32167</td>
      <td>18607</td>
      <td>113474</td>
      <td>18607</td>
      <td>113474</td>
      <td>3895</td>
      <td>23609</td>
      <td>10479</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_vali...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_vali...</td>
      <td>112389</td>
      <td>112389</td>
      <td>0</td>
      <td>...</td>
      <td>28854</td>
      <td>14700</td>
      <td>97689</td>
      <td>14700</td>
      <td>97689</td>
      <td>3349</td>
      <td>20680</td>
      <td>8431</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_vali...</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_vali...</td>
      <td>111156</td>
      <td>111156</td>
      <td>0</td>
      <td>...</td>
      <td>27624</td>
      <td>14850</td>
      <td>96306</td>
      <td>14850</td>
      <td>96306</td>
      <td>3396</td>
      <td>21262</td>
      <td>8382</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_val...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_val...</td>
      <td>144641</td>
      <td>144641</td>
      <td>0</td>
      <td>...</td>
      <td>29882</td>
      <td>19405</td>
      <td>125236</td>
      <td>19405</td>
      <td>125236</td>
      <td>4500</td>
      <td>25458</td>
      <td>11250</td>
      <td>100.0</td>
      <td>100.0</td>
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
      <td>45680</td>
      <td>45680</td>
      <td>0</td>
      <td>...</td>
      <td>20842</td>
      <td>4552</td>
      <td>41128</td>
      <td>4552</td>
      <td>41128</td>
      <td>1206</td>
      <td>10079</td>
      <td>2399</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_vali...</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_vali...</td>
      <td>119922</td>
      <td>119922</td>
      <td>0</td>
      <td>...</td>
      <td>25809</td>
      <td>15181</td>
      <td>104741</td>
      <td>15181</td>
      <td>104741</td>
      <td>3482</td>
      <td>20011</td>
      <td>8950</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
      <td>FragPipe_Duncan_PXD004720_lemma_validated_pept...</td>
      <td>FragPipe_Duncan_PXD004720_lemma_validated_pept...</td>
      <td>146562</td>
      <td>146562</td>
      <td>0</td>
      <td>...</td>
      <td>29915</td>
      <td>21700</td>
      <td>124862</td>
      <td>21700</td>
      <td>124862</td>
      <td>4945</td>
      <td>24927</td>
      <td>12402</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
      <td>FragPipe_Duncan_PXD004720_node_validated_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_node_validated_pepti...</td>
      <td>98731</td>
      <td>98731</td>
      <td>0</td>
      <td>...</td>
      <td>29228</td>
      <td>12726</td>
      <td>86005</td>
      <td>12726</td>
      <td>86005</td>
      <td>3047</td>
      <td>18416</td>
      <td>7081</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_valid...</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_valid...</td>
      <td>168564</td>
      <td>168564</td>
      <td>0</td>
      <td>...</td>
      <td>33166</td>
      <td>22830</td>
      <td>145734</td>
      <td>22830</td>
      <td>145734</td>
      <td>5106</td>
      <td>29193</td>
      <td>13247</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
      <td>FragPipe_Duncan_PXD004720_palea_validated_pept...</td>
      <td>FragPipe_Duncan_PXD004720_palea_validated_pept...</td>
      <td>116285</td>
      <td>116285</td>
      <td>0</td>
      <td>...</td>
      <td>21503</td>
      <td>20637</td>
      <td>95648</td>
      <td>20637</td>
      <td>95648</td>
      <td>4574</td>
      <td>17224</td>
      <td>12073</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_validated_p...</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_validated_p...</td>
      <td>130645</td>
      <td>130645</td>
      <td>0</td>
      <td>...</td>
      <td>25580</td>
      <td>20924</td>
      <td>109721</td>
      <td>20924</td>
      <td>109721</td>
      <td>4780</td>
      <td>23621</td>
      <td>11925</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
      <td>FragPipe_Duncan_PXD004720_pollen_validated_pep...</td>
      <td>FragPipe_Duncan_PXD004720_pollen_validated_pep...</td>
      <td>74334</td>
      <td>74334</td>
      <td>0</td>
      <td>...</td>
      <td>15866</td>
      <td>9467</td>
      <td>64867</td>
      <td>9467</td>
      <td>64867</td>
      <td>2046</td>
      <td>11506</td>
      <td>5323</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_gen...</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_validated_p...</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_validated_p...</td>
      <td>159219</td>
      <td>159219</td>
      <td>0</td>
      <td>...</td>
      <td>29020</td>
      <td>24725</td>
      <td>134494</td>
      <td>24725</td>
      <td>134494</td>
      <td>5547</td>
      <td>25706</td>
      <td>14419</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_geno...</td>
      <td>FragPipe_Duncan_PXD004720_radicle_validated_pe...</td>
      <td>FragPipe_Duncan_PXD004720_radicle_validated_pe...</td>
      <td>193938</td>
      <td>193938</td>
      <td>0</td>
      <td>...</td>
      <td>33385</td>
      <td>32434</td>
      <td>161504</td>
      <td>32434</td>
      <td>161504</td>
      <td>7023</td>
      <td>32738</td>
      <td>19023</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_validate...</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_validate...</td>
      <td>96387</td>
      <td>96387</td>
      <td>0</td>
      <td>...</td>
      <td>30952</td>
      <td>10853</td>
      <td>85534</td>
      <td>10853</td>
      <td>85534</td>
      <td>2561</td>
      <td>18716</td>
      <td>6101</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_valid...</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_valid...</td>
      <td>100085</td>
      <td>100085</td>
      <td>0</td>
      <td>...</td>
      <td>25126</td>
      <td>15505</td>
      <td>84580</td>
      <td>15505</td>
      <td>84580</td>
      <td>3464</td>
      <td>17786</td>
      <td>8962</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_gen...</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_validated_p...</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_validated_p...</td>
      <td>191262</td>
      <td>191262</td>
      <td>0</td>
      <td>...</td>
      <td>30508</td>
      <td>34992</td>
      <td>156270</td>
      <td>34992</td>
      <td>156270</td>
      <td>7495</td>
      <td>31236</td>
      <td>21029</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_val...</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_val...</td>
      <td>111315</td>
      <td>111315</td>
      <td>0</td>
      <td>...</td>
      <td>23512</td>
      <td>14786</td>
      <td>96529</td>
      <td>14786</td>
      <td>96529</td>
      <td>3150</td>
      <td>17756</td>
      <td>8152</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_valid...</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_valid...</td>
      <td>188025</td>
      <td>188025</td>
      <td>0</td>
      <td>...</td>
      <td>30611</td>
      <td>33123</td>
      <td>154902</td>
      <td>33123</td>
      <td>154902</td>
      <td>7004</td>
      <td>29483</td>
      <td>19325</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>FragPipe_Duncan_PXD004720_stem_validated_pepti...</td>
      <td>FragPipe_Duncan_PXD004720_stem_validated_pepti...</td>
      <td>60181</td>
      <td>60181</td>
      <td>0</td>
      <td>...</td>
      <td>23218</td>
      <td>6927</td>
      <td>53254</td>
      <td>6927</td>
      <td>53254</td>
      <td>1668</td>
      <td>12620</td>
      <td>3963</td>
      <td>100.0</td>
      <td>100.0</td>
    </tr>
  </tbody>
</table>
<p>32 rows × 24 columns</p>
</div>


# Step 13 — Create a Non-Redundant Combined Peptide BED Track

This step generates a single non-redundant genome browser track containing all successfully projected wheat peptides across all tissues.

The purpose of this combined track is to improve the user experience in Apollo/JBrowse by allowing users to display all peptide evidence at once, without needing to manually activate each individual tissue track.

---

## Input files

### Validated peptide genome projection table from Step 11

```text
wheat_projection_translation_validated_sanity_checks_full_step11.csv
```

Only fully validated projected rows were retained.

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
FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed6
```

### Combined BED12 file

```text
FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed12
```

### Output directories

```text
python_outputs/tables/
python_outputs/bed/
```

---

## Summary metrics

A Step 13 summary table was generated.

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
wheat_all_tissues_nonredundant_validated_bed_summary_step13.csv
```

The resulting combined BED files provide a user-friendly genome-wide peptide evidence track for Apollo/JBrowse visualisation.


```python
# ============================================================
# Step 13 — Create non-redundant combined validated BED tracks
# (takes approximately 30 minutes)
#
# Outputs:
# 1. Complete non-redundant track containing all valid
#    sequence identifiers, including ChrUnknown
# 2. Standalone non-redundant ChrUnknown track
#
# Translation-validated + sanity-check-passed projections only
# Uses SQLite for memory-safe aggregation.
#
# Existing Step 13 outputs are overwritten.
# ============================================================

import sqlite3
from pathlib import Path

import pandas as pd


# -----------------------------
# 1. Input / output paths
# -----------------------------

tables_dir = Path("python_outputs/tables")
bed_dir = Path("python_outputs/bed_validated")

bed_dir.mkdir(
    parents=True,
    exist_ok=True
)

tables_dir.mkdir(
    parents=True,
    exist_ok=True
)


# Corrected Step 11 output:
# translation-validated rows with sanity-check results
sanity_file = (
    tables_dir
    / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"
)


# Original complete non-redundant outputs
combined_table_out = (
    tables_dir
    / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv"
)

combined_bed6_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed6"
)

combined_bed12_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed12"
)


# New standalone ChrUnknown non-redundant tracks
chrunknown_bed6_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed6"
)

chrunknown_bed12_out = (
    bed_dir
    / "FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed12"
)


# Original Step 13 summary and SQLite filenames
step13_summary_out = (
    tables_dir
    / "wheat_all_tissues_nonredundant_validated_bed_summary_step13.csv"
)

sqlite_db = (
    tables_dir
    / "wheat_validated_nonredundant_step13.sqlite"
)

chunk_size = 100_000


if not sanity_file.exists():

    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n"
        f"{sanity_file}\n\n"
        "Please run the corrected Step 11 first."
    )


# Overwrite previous Step 13 outputs.
for output_path in [
    combined_table_out,
    combined_bed6_out,
    combined_bed12_out,
    chrunknown_bed6_out,
    chrunknown_bed12_out,
    step13_summary_out,
    sqlite_db
]:

    if output_path.exists():
        output_path.unlink()


# -----------------------------
# 2. Helper functions
# -----------------------------

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
        .replace("\r", "_")
    )


def make_bed_score(data):
    """
    Create BED score between 0 and 1000.

    Priority:
    1. Probability scaled to 0–1000, when available
    2. Default score of 1000
    """

    if "Probability" in data.columns:

        score = (
            pd.to_numeric(
                data["Probability"],
                errors="coerce"
            )
            * 1000
        )

        score = (
            score
            .fillna(1000)
            .clip(0, 1000)
            .round()
            .astype(int)
        )

    else:

        score = pd.Series(
            1000,
            index=data.index,
            dtype="int64"
        )

    return score


def make_bed6(nonredundant):
    """
    Build BED6 DataFrame.
    """

    return pd.DataFrame({
        "chrom":
            nonredundant["Chromosome"],

        "chromStart":
            nonredundant["BED_start_0based"],

        "chromEnd":
            nonredundant["BED_end_0based_exclusive"],

        "name":
            nonredundant["BED_name"],

        "score":
            nonredundant["Max_BED_score"],

        "strand":
            nonredundant["Strand"]
    })


def make_bed12(nonredundant):
    """
    Build BED12 DataFrame.
    """

    return pd.DataFrame({
        "chrom":
            nonredundant["Chromosome"],

        "chromStart":
            nonredundant["BED_start_0based"],

        "chromEnd":
            nonredundant["BED_end_0based_exclusive"],

        "name":
            nonredundant["BED_name"],

        "score":
            nonredundant["Max_BED_score"],

        "strand":
            nonredundant["Strand"],

        "thickStart":
            nonredundant["BED_start_0based"],

        "thickEnd":
            nonredundant["BED_end_0based_exclusive"],

        "itemRgb":
            "0",

        "blockCount":
            nonredundant["BED_block_count"],

        "blockSizes":
            nonredundant["BED_block_sizes"],

        "blockStarts":
            nonredundant["BED_block_starts"]
    })


# -----------------------------
# 3. Inspect corrected Step 11 columns
# -----------------------------

header = pd.read_csv(
    sanity_file,
    nrows=0
)

required_cols = [
    "Chromosome",
    "BED_start_0based",
    "BED_end_0based_exclusive",
    "Strand",
    "Peptide",
    "ProteinID",
    "BED_block_count",
    "BED_block_sizes",
    "BED_block_starts",
    "Source",
    "Tissue",
    "Sanity_check_status",
    "All_sanity_checks_passed",
    "Check_chromosome_and_strand"
]

missing_required = [
    column
    for column in required_cols
    if column not in header.columns
]

if missing_required:

    raise KeyError(
        "Missing required corrected Step 11 column(s): "
        f"{missing_required}"
    )


# Best available gene/model label
if "GeneModel" in header.columns:

    gene_label_col = "GeneModel"

elif "GeneID" in header.columns:

    gene_label_col = "GeneID"

else:

    gene_label_col = None


# Best available peptide display label
if "Peptide_intron_gapped" in header.columns:

    peptide_label_col = "Peptide_intron_gapped"

elif "Peptide_intron_gapped_compact" in header.columns:

    peptide_label_col = "Peptide_intron_gapped_compact"

else:

    peptide_label_col = "Peptide"


optional_cols = []

if "Probability" in header.columns:
    optional_cols.append("Probability")

if gene_label_col is not None:
    optional_cols.append(gene_label_col)

if peptide_label_col not in required_cols:
    optional_cols.append(peptide_label_col)


usecols = list(
    dict.fromkeys(
        required_cols
        + optional_cols
    )
)


print("Step 13 input file:")
print(f"  {sanity_file}")

print(
    "Using gene/model label column: "
    f"{gene_label_col}"
)

print(
    "Using peptide display column: "
    f"{peptide_label_col}"
)


# -----------------------------
# 4. Load sanity-passed rows into SQLite
# -----------------------------

conn = sqlite3.connect(
    sqlite_db
)

total_rows_read = 0
total_rows_passed = 0
total_chrunknown_rows_loaded = 0


print(
    "\nLoading corrected Step 11 sanity-passed rows "
    "into SQLite..."
)


for chunk_number, chunk in enumerate(

    pd.read_csv(
        sanity_file,
        usecols=usecols,
        chunksize=chunk_size,
        low_memory=False
    ),

    start=1
):

    rows_in_chunk = len(
        chunk
    )

    total_rows_read += rows_in_chunk


    # Retain only rows passing both validation layers.
    passed_mask = (
        chunk[
            "Sanity_check_status"
        ]
        .astype(str)
        .str.strip()
        .eq("passed")
        &
        chunk[
            "All_sanity_checks_passed"
        ]
        .fillna(False)
        .astype(bool)
    )

    chunk = chunk[
        passed_mask
    ].copy()


    if chunk.empty:

        print(
            f"Chunk {chunk_number}: "
            f"read {rows_in_chunk:,} rows | "
            "no passed rows"
        )

        continue


    total_rows_passed += len(
        chunk
    )


    # Standardise core text fields.
    chunk["Chromosome"] = (
        chunk["Chromosome"]
        .astype(str)
        .str.strip()
    )

    chunk["Strand"] = (
        chunk["Strand"]
        .astype(str)
        .str.strip()
    )


    total_chrunknown_rows_loaded += int(
        chunk[
            "Chromosome"
        ]
        .eq("ChrUnknown")
        .sum()
    )


    if gene_label_col is None:

        chunk["Gene_label"] = "NA"

    else:

        chunk["Gene_label"] = (
            chunk[
                gene_label_col
            ]
            .fillna("NA")
            .astype(str)
        )


    chunk["Peptide_label"] = (
        chunk[
            peptide_label_col
        ]
        .fillna(
            chunk["Peptide"]
        )
        .astype(str)
    )


    chunk["BED_score"] = (
        make_bed_score(
            chunk
        )
    )


    # Retain only fields required for nonredundant aggregation.
    insert_cols = [
        "Chromosome",
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "Strand",
        "Peptide",
        "Peptide_label",
        "ProteinID",
        "Gene_label",
        "BED_block_count",
        "BED_block_sizes",
        "BED_block_starts",
        "Source",
        "Tissue",
        "BED_score"
    ]

    chunk = chunk[
        insert_cols
    ].copy()


    text_cols = [
        "Chromosome",
        "Strand",
        "Peptide",
        "Peptide_label",
        "ProteinID",
        "Gene_label",
        "BED_block_sizes",
        "BED_block_starts",
        "Source",
        "Tissue"
    ]

    for column in text_cols:

        chunk[column] = (
            chunk[column]
            .astype(str)
        )


    numeric_cols = [
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_block_count",
        "BED_score"
    ]

    for column in numeric_cols:

        chunk[column] = pd.to_numeric(
            chunk[column],
            errors="coerce"
        )


    chunk = chunk.dropna(
        subset=[
            "Chromosome",
            "BED_start_0based",
            "BED_end_0based_exclusive",
            "Strand",
            "BED_block_count",
            "BED_block_sizes",
            "BED_block_starts"
        ]
    ).copy()


    chunk.to_sql(
        "validated_projection_rows",
        conn,
        if_exists="append",
        index=False
    )


    print(
        f"Chunk {chunk_number}: "
        f"cumulative rows read {total_rows_read:,} | "
        f"passed rows loaded {total_rows_passed:,} | "
        f"ChrUnknown rows loaded "
        f"{total_chrunknown_rows_loaded:,}"
    )


if total_rows_passed == 0:

    conn.close()

    raise ValueError(
        "No sanity-passed rows were found in "
        "the corrected Step 11 output."
    )


if total_chrunknown_rows_loaded != 77_543:

    print(
        "\nWARNING: corrected Step 11 was expected to contain "
        "77,543 passed ChrUnknown rows, but "
        f"{total_chrunknown_rows_loaded:,} were loaded."
    )

else:

    print(
        "\nChrUnknown input check passed: "
        "77,543 validated rows loaded into SQLite."
    )


# -----------------------------
# 5. Create SQLite indexes
# -----------------------------

print(
    "\nCreating SQLite indexes..."
)


conn.execute("""
CREATE INDEX IF NOT EXISTS idx_validated_projection_dedup
ON validated_projection_rows (
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    BED_block_count,
    BED_block_sizes,
    BED_block_starts
)
""")


conn.execute("""
CREATE INDEX IF NOT EXISTS idx_validated_projection_chromosome
ON validated_projection_rows (
    Chromosome
)
""")


conn.commit()


# -----------------------------
# 6. Build complete nonredundant table
# -----------------------------

print(
    "\nBuilding complete nonredundant validated "
    "feature table..."
)


conn.execute(
    "DROP TABLE IF EXISTS "
    "nonredundant_validated_peptides"
)


conn.execute("""
CREATE TABLE nonredundant_validated_peptides AS
SELECT
    Chromosome,
    CAST(BED_start_0based AS INTEGER)
        AS BED_start_0based,
    CAST(BED_end_0based_exclusive AS INTEGER)
        AS BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    CAST(BED_block_count AS INTEGER)
        AS BED_block_count,
    BED_block_sizes,
    BED_block_starts,
    GROUP_CONCAT(DISTINCT Source)
        AS Sources,
    GROUP_CONCAT(DISTINCT Tissue)
        AS Tissues,
    COUNT(DISTINCT Source || '|' || Tissue)
        AS Source_tissue_count,
    COUNT(DISTINCT Tissue)
        AS Tissue_count,
    COUNT(*)
        AS Observation_count,
    MAX(CAST(BED_score AS INTEGER))
        AS Max_BED_score
FROM validated_projection_rows
GROUP BY
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    BED_block_count,
    BED_block_sizes,
    BED_block_starts
""")


conn.commit()


# -----------------------------
# 7. Export complete table and both track sets
# -----------------------------

print(
    "\nExporting complete nonredundant table, "
    "complete BED tracks and ChrUnknown-only BED tracks..."
)


combined_header_written = False

total_nonredundant_rows = 0
total_chrunknown_nonredundant_rows = 0

unique_peptides = set()
unique_proteins = set()
unique_genes = set()
unique_sequence_ids = set()

chrunknown_unique_peptides = set()
chrunknown_unique_proteins = set()
chrunknown_unique_genes = set()

multi_block_count = 0
within_exon_count = 0
bed_labels_with_introns = 0

chrunknown_multi_block_count = 0
chrunknown_within_exon_count = 0


sql_query = """
SELECT
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    Peptide_label,
    ProteinID,
    Gene_label,
    BED_block_count,
    BED_block_sizes,
    BED_block_starts,
    Sources,
    Tissues,
    Source_tissue_count,
    Tissue_count,
    Observation_count,
    Max_BED_score
FROM nonredundant_validated_peptides
ORDER BY
    Chromosome,
    BED_start_0based,
    BED_end_0based_exclusive,
    Strand,
    Peptide,
    ProteinID
"""


for chunk_number, nonredundant in enumerate(

    pd.read_sql_query(
        sql_query,
        conn,
        chunksize=chunk_size
    ),

    start=1
):

    number_rows = len(
        nonredundant
    )


    nonredundant.insert(
        0,
        "Index",
        range(
            total_nonredundant_rows + 1,
            total_nonredundant_rows + number_rows + 1
        )
    )


    nonredundant["BED_name"] = (
        nonredundant[
            "Peptide_label"
        ].astype(str)
        + "|"
        + nonredundant[
            "ProteinID"
        ].astype(str)
        + "|"
        + nonredundant[
            "Gene_label"
        ].astype(str)
        + "|validated=translation+sanity"
        + "|source_tissues="
        + nonredundant[
            "Source_tissue_count"
        ].astype(str)
    )


    nonredundant["BED_name"] = (
        nonredundant[
            "BED_name"
        ]
        .apply(
            clean_bed_name
        )
    )


    integer_columns = [
        "BED_start_0based",
        "BED_end_0based_exclusive",
        "BED_block_count",
        "Source_tissue_count",
        "Tissue_count",
        "Observation_count",
        "Max_BED_score"
    ]

    for column in integer_columns:

        nonredundant[column] = (
            pd.to_numeric(
                nonredundant[column],
                errors="raise"
            )
            .astype(int)
        )


    # -----------------------------------------
    # Complete nonredundant CSV table
    # -----------------------------------------

    nonredundant.to_csv(
        combined_table_out,
        index=False,
        mode="a",
        header=not combined_header_written
    )

    combined_header_written = True


    # -----------------------------------------
    # Complete nonredundant BED6/BED12 tracks
    # -----------------------------------------

    complete_bed6 = make_bed6(
        nonredundant
    )

    complete_bed12 = make_bed12(
        nonredundant
    )


    complete_bed6.to_csv(
        combined_bed6_out,
        sep="\t",
        header=False,
        index=False,
        mode="a"
    )


    complete_bed12.to_csv(
        combined_bed12_out,
        sep="\t",
        header=False,
        index=False,
        mode="a"
    )


    # -----------------------------------------
    # Standalone nonredundant ChrUnknown tracks
    # -----------------------------------------

    chrunknown = nonredundant[
        nonredundant[
            "Chromosome"
        ]
        .astype(str)
        .str.strip()
        .eq("ChrUnknown")
    ].copy()


    if not chrunknown.empty:

        chrunknown_bed6 = make_bed6(
            chrunknown
        )

        chrunknown_bed12 = make_bed12(
            chrunknown
        )


        chrunknown_bed6.to_csv(
            chrunknown_bed6_out,
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )


        chrunknown_bed12.to_csv(
            chrunknown_bed12_out,
            sep="\t",
            header=False,
            index=False,
            mode="a"
        )


        total_chrunknown_nonredundant_rows += len(
            chrunknown
        )


        chrunknown_unique_peptides.update(
            chrunknown[
                "Peptide"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


        chrunknown_unique_proteins.update(
            chrunknown[
                "ProteinID"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


        chrunknown_unique_genes.update(
            chrunknown[
                "Gene_label"
            ]
            .dropna()
            .astype(str)
            .unique()
        )


        chrunknown_multi_block_count += int(
            (
                chrunknown[
                    "BED_block_count"
                ]
                > 1
            ).sum()
        )


        chrunknown_within_exon_count += int(
            (
                chrunknown[
                    "BED_block_count"
                ]
                == 1
            ).sum()
        )


    # -----------------------------------------
    # Overall summary counters
    # -----------------------------------------

    total_nonredundant_rows += number_rows


    unique_peptides.update(
        nonredundant[
            "Peptide"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    unique_proteins.update(
        nonredundant[
            "ProteinID"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    unique_genes.update(
        nonredundant[
            "Gene_label"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    unique_sequence_ids.update(
        nonredundant[
            "Chromosome"
        ]
        .dropna()
        .astype(str)
        .unique()
    )


    multi_block_count += int(
        (
            nonredundant[
                "BED_block_count"
            ]
            > 1
        ).sum()
    )


    within_exon_count += int(
        (
            nonredundant[
                "BED_block_count"
            ]
            == 1
        ).sum()
    )


    bed_labels_with_introns += int(
        nonredundant[
            "BED_name"
        ]
        .astype(str)
        .str.contains(
            "-",
            regex=False
        )
        .sum()
    )


    print(
        f"Export chunk {chunk_number}: "
        f"cumulative complete nonredundant rows "
        f"{total_nonredundant_rows:,} | "
        f"ChrUnknown nonredundant rows "
        f"{total_chrunknown_nonredundant_rows:,}"
    )


# -----------------------------
# 8. Integrity checks
# -----------------------------

if not combined_header_written:

    conn.close()

    raise ValueError(
        "No complete nonredundant rows were exported."
    )


if not chrunknown_bed6_out.exists():

    conn.close()

    raise ValueError(
        "No ChrUnknown BED6 track was created. "
        "Check the corrected Step 11 input."
    )


if not chrunknown_bed12_out.exists():

    conn.close()

    raise ValueError(
        "No ChrUnknown BED12 track was created. "
        "Check the corrected Step 11 input."
    )


# Confirm SQLite count agrees with exported ChrUnknown count.
sqlite_chrunknown_count = conn.execute("""
SELECT COUNT(*)
FROM nonredundant_validated_peptides
WHERE Chromosome = 'ChrUnknown'
""").fetchone()[0]


if (
    sqlite_chrunknown_count
    != total_chrunknown_nonredundant_rows
):

    conn.close()

    raise ValueError(
        "ChrUnknown nonredundant row-count mismatch:\n"
        f"SQLite rows: "
        f"{sqlite_chrunknown_count:,}\n"
        f"Exported rows: "
        f"{total_chrunknown_nonredundant_rows:,}"
    )


# -----------------------------
# 9. Summary table
# -----------------------------

step13_summary = pd.DataFrame([{

    "Validated_rows_before_deduplication":
        total_rows_passed,

    "Nonredundant_validated_rows":
        total_nonredundant_rows,

    "Redundant_validated_rows_removed":
        (
            total_rows_passed
            - total_nonredundant_rows
        ),

    "Unique_peptides":
        len(
            unique_peptides
        ),

    "Unique_proteins":
        len(
            unique_proteins
        ),

    "Unique_gene_models":
        len(
            unique_genes
        ),

    # Retain original summary column name for compatibility.
    # This now includes the 21 chromosomes plus ChrUnknown.
    "Unique_chromosomes":
        len(
            unique_sequence_ids
        ),

    "Multi_block_peptides":
        multi_block_count,

    "Within_exon_peptides":
        within_exon_count,

    "BED_labels_with_introns":
        bed_labels_with_introns,

    "ChrUnknown_validated_rows_before_deduplication":
        total_chrunknown_rows_loaded,

    "ChrUnknown_nonredundant_validated_rows":
        total_chrunknown_nonredundant_rows,

    "ChrUnknown_redundant_rows_removed":
        (
            total_chrunknown_rows_loaded
            - total_chrunknown_nonredundant_rows
        ),

    "ChrUnknown_unique_peptides":
        len(
            chrunknown_unique_peptides
        ),

    "ChrUnknown_unique_proteins":
        len(
            chrunknown_unique_proteins
        ),

    "ChrUnknown_unique_gene_models":
        len(
            chrunknown_unique_genes
        ),

    "ChrUnknown_multi_block_peptides":
        chrunknown_multi_block_count,

    "ChrUnknown_within_exon_peptides":
        chrunknown_within_exon_count,

    "Combined_table_file":
        combined_table_out.name,

    "BED6_file":
        combined_bed6_out.name,

    "BED12_file":
        combined_bed12_out.name,

    "ChrUnknown_BED6_file":
        chrunknown_bed6_out.name,

    "ChrUnknown_BED12_file":
        chrunknown_bed12_out.name,

    "SQLite_database":
        sqlite_db.name
}])


step13_summary.to_csv(
    step13_summary_out,
    index=False
)


conn.close()


# -----------------------------
# 10. Final summary
# -----------------------------

print(
    "\n===== STEP 13 COMBINED VALIDATED BED SUMMARY ====="
)

print(
    "Validated rows before deduplication: "
    f"{total_rows_passed:,}"
)

print(
    "Complete nonredundant validated rows: "
    f"{total_nonredundant_rows:,}"
)

print(
    "Redundant validated rows removed: "
    f"{total_rows_passed - total_nonredundant_rows:,}"
)

print(
    "Sequence identifiers represented: "
    f"{len(unique_sequence_ids):,}"
)

print(
    "\n===== ChrUnknown NONREDUNDANT TRACK ====="
)

print(
    "ChrUnknown validated rows before deduplication: "
    f"{total_chrunknown_rows_loaded:,}"
)

print(
    "ChrUnknown nonredundant validated rows: "
    f"{total_chrunknown_nonredundant_rows:,}"
)

print(
    "ChrUnknown redundant rows removed: "
    f"{total_chrunknown_rows_loaded - total_chrunknown_nonredundant_rows:,}"
)

print(
    "ChrUnknown unique peptide sequences: "
    f"{len(chrunknown_unique_peptides):,}"
)

print(
    "ChrUnknown unique protein accessions: "
    f"{len(chrunknown_unique_proteins):,}"
)

print(
    "ChrUnknown unique gene models: "
    f"{len(chrunknown_unique_genes):,}"
)

print(
    "\nComplete nonredundant table saved:"
    f"\n  {combined_table_out}"
)

print(
    "Complete combined BED6 saved:"
    f"\n  {combined_bed6_out}"
)

print(
    "Complete combined BED12 saved:"
    f"\n  {combined_bed12_out}"
)

print(
    "Standalone ChrUnknown BED6 saved:"
    f"\n  {chrunknown_bed6_out}"
)

print(
    "Standalone ChrUnknown BED12 saved:"
    f"\n  {chrunknown_bed12_out}"
)

print(
    "Step 13 summary saved:"
    f"\n  {step13_summary_out}"
)

print(
    "SQLite database saved:"
    f"\n  {sqlite_db}"
)


display(
    step13_summary
)
```

    Step 13 input file:
      python_outputs\tables\wheat_projection_translation_validated_sanity_checks_full_step11.csv
    Using gene/model label column: GeneModel
    Using peptide display column: Peptide_intron_gapped
    
    Loading corrected Step 11 sanity-passed rows into SQLite...
    Chunk 1: cumulative rows read 100,000 | passed rows loaded 100,000 | ChrUnknown rows loaded 897
    Chunk 2: cumulative rows read 200,000 | passed rows loaded 200,000 | ChrUnknown rows loaded 1,855
    Chunk 3: cumulative rows read 300,000 | passed rows loaded 300,000 | ChrUnknown rows loaded 2,890
    Chunk 4: cumulative rows read 400,000 | passed rows loaded 400,000 | ChrUnknown rows loaded 3,818
    Chunk 5: cumulative rows read 500,000 | passed rows loaded 500,000 | ChrUnknown rows loaded 4,677
    Chunk 6: cumulative rows read 600,000 | passed rows loaded 600,000 | ChrUnknown rows loaded 5,839
    Chunk 7: cumulative rows read 700,000 | passed rows loaded 700,000 | ChrUnknown rows loaded 6,812
    Chunk 8: cumulative rows read 800,000 | passed rows loaded 800,000 | ChrUnknown rows loaded 7,676
    Chunk 9: cumulative rows read 900,000 | passed rows loaded 900,000 | ChrUnknown rows loaded 8,452
    Chunk 10: cumulative rows read 1,000,000 | passed rows loaded 1,000,000 | ChrUnknown rows loaded 9,198
    Chunk 11: cumulative rows read 1,100,000 | passed rows loaded 1,100,000 | ChrUnknown rows loaded 10,038
    Chunk 12: cumulative rows read 1,200,000 | passed rows loaded 1,200,000 | ChrUnknown rows loaded 10,950
    Chunk 13: cumulative rows read 1,300,000 | passed rows loaded 1,300,000 | ChrUnknown rows loaded 11,757
    Chunk 14: cumulative rows read 1,400,000 | passed rows loaded 1,400,000 | ChrUnknown rows loaded 12,852
    Chunk 15: cumulative rows read 1,500,000 | passed rows loaded 1,500,000 | ChrUnknown rows loaded 14,015
    Chunk 16: cumulative rows read 1,600,000 | passed rows loaded 1,600,000 | ChrUnknown rows loaded 15,118
    Chunk 17: cumulative rows read 1,700,000 | passed rows loaded 1,700,000 | ChrUnknown rows loaded 16,139
    Chunk 18: cumulative rows read 1,800,000 | passed rows loaded 1,800,000 | ChrUnknown rows loaded 17,080
    Chunk 19: cumulative rows read 1,900,000 | passed rows loaded 1,900,000 | ChrUnknown rows loaded 18,113
    Chunk 20: cumulative rows read 2,000,000 | passed rows loaded 2,000,000 | ChrUnknown rows loaded 19,303
    Chunk 21: cumulative rows read 2,100,000 | passed rows loaded 2,100,000 | ChrUnknown rows loaded 20,378
    Chunk 22: cumulative rows read 2,200,000 | passed rows loaded 2,200,000 | ChrUnknown rows loaded 21,360
    Chunk 23: cumulative rows read 2,300,000 | passed rows loaded 2,300,000 | ChrUnknown rows loaded 22,322
    Chunk 24: cumulative rows read 2,400,000 | passed rows loaded 2,400,000 | ChrUnknown rows loaded 23,267
    Chunk 25: cumulative rows read 2,500,000 | passed rows loaded 2,500,000 | ChrUnknown rows loaded 24,277
    Chunk 26: cumulative rows read 2,600,000 | passed rows loaded 2,600,000 | ChrUnknown rows loaded 25,071
    Chunk 27: cumulative rows read 2,700,000 | passed rows loaded 2,700,000 | ChrUnknown rows loaded 25,849
    Chunk 28: cumulative rows read 2,800,000 | passed rows loaded 2,800,000 | ChrUnknown rows loaded 26,941
    Chunk 29: cumulative rows read 2,900,000 | passed rows loaded 2,900,000 | ChrUnknown rows loaded 27,865
    Chunk 30: cumulative rows read 3,000,000 | passed rows loaded 3,000,000 | ChrUnknown rows loaded 28,572
    Chunk 31: cumulative rows read 3,100,000 | passed rows loaded 3,100,000 | ChrUnknown rows loaded 29,252
    Chunk 32: cumulative rows read 3,200,000 | passed rows loaded 3,200,000 | ChrUnknown rows loaded 30,167
    Chunk 33: cumulative rows read 3,300,000 | passed rows loaded 3,300,000 | ChrUnknown rows loaded 31,031
    Chunk 34: cumulative rows read 3,400,000 | passed rows loaded 3,400,000 | ChrUnknown rows loaded 31,934
    Chunk 35: cumulative rows read 3,500,000 | passed rows loaded 3,500,000 | ChrUnknown rows loaded 32,786
    Chunk 36: cumulative rows read 3,600,000 | passed rows loaded 3,600,000 | ChrUnknown rows loaded 33,617
    Chunk 37: cumulative rows read 3,700,000 | passed rows loaded 3,700,000 | ChrUnknown rows loaded 34,503
    Chunk 38: cumulative rows read 3,800,000 | passed rows loaded 3,800,000 | ChrUnknown rows loaded 35,321
    Chunk 39: cumulative rows read 3,900,000 | passed rows loaded 3,900,000 | ChrUnknown rows loaded 36,264
    Chunk 40: cumulative rows read 4,000,000 | passed rows loaded 4,000,000 | ChrUnknown rows loaded 37,307
    Chunk 41: cumulative rows read 4,100,000 | passed rows loaded 4,100,000 | ChrUnknown rows loaded 38,310
    Chunk 42: cumulative rows read 4,200,000 | passed rows loaded 4,200,000 | ChrUnknown rows loaded 39,203
    Chunk 43: cumulative rows read 4,300,000 | passed rows loaded 4,300,000 | ChrUnknown rows loaded 40,161
    Chunk 44: cumulative rows read 4,400,000 | passed rows loaded 4,400,000 | ChrUnknown rows loaded 41,033
    Chunk 45: cumulative rows read 4,500,000 | passed rows loaded 4,500,000 | ChrUnknown rows loaded 42,214
    Chunk 46: cumulative rows read 4,600,000 | passed rows loaded 4,600,000 | ChrUnknown rows loaded 43,351
    Chunk 47: cumulative rows read 4,700,000 | passed rows loaded 4,700,000 | ChrUnknown rows loaded 44,403
    Chunk 48: cumulative rows read 4,800,000 | passed rows loaded 4,800,000 | ChrUnknown rows loaded 45,317
    Chunk 49: cumulative rows read 4,900,000 | passed rows loaded 4,900,000 | ChrUnknown rows loaded 46,309
    Chunk 50: cumulative rows read 5,000,000 | passed rows loaded 5,000,000 | ChrUnknown rows loaded 47,110
    Chunk 51: cumulative rows read 5,100,000 | passed rows loaded 5,100,000 | ChrUnknown rows loaded 47,971
    Chunk 52: cumulative rows read 5,200,000 | passed rows loaded 5,200,000 | ChrUnknown rows loaded 48,844
    Chunk 53: cumulative rows read 5,300,000 | passed rows loaded 5,300,000 | ChrUnknown rows loaded 49,743
    Chunk 54: cumulative rows read 5,400,000 | passed rows loaded 5,400,000 | ChrUnknown rows loaded 50,645
    Chunk 55: cumulative rows read 5,500,000 | passed rows loaded 5,500,000 | ChrUnknown rows loaded 51,579
    Chunk 56: cumulative rows read 5,600,000 | passed rows loaded 5,600,000 | ChrUnknown rows loaded 52,397
    Chunk 57: cumulative rows read 5,700,000 | passed rows loaded 5,700,000 | ChrUnknown rows loaded 53,341
    Chunk 58: cumulative rows read 5,800,000 | passed rows loaded 5,800,000 | ChrUnknown rows loaded 54,193
    Chunk 59: cumulative rows read 5,900,000 | passed rows loaded 5,900,000 | ChrUnknown rows loaded 55,253
    Chunk 60: cumulative rows read 6,000,000 | passed rows loaded 6,000,000 | ChrUnknown rows loaded 56,293
    Chunk 61: cumulative rows read 6,100,000 | passed rows loaded 6,100,000 | ChrUnknown rows loaded 57,296
    Chunk 62: cumulative rows read 6,200,000 | passed rows loaded 6,200,000 | ChrUnknown rows loaded 58,220
    Chunk 63: cumulative rows read 6,300,000 | passed rows loaded 6,300,000 | ChrUnknown rows loaded 59,274
    Chunk 64: cumulative rows read 6,400,000 | passed rows loaded 6,400,000 | ChrUnknown rows loaded 60,564
    Chunk 65: cumulative rows read 6,500,000 | passed rows loaded 6,500,000 | ChrUnknown rows loaded 61,584
    Chunk 66: cumulative rows read 6,600,000 | passed rows loaded 6,600,000 | ChrUnknown rows loaded 62,587
    Chunk 67: cumulative rows read 6,700,000 | passed rows loaded 6,700,000 | ChrUnknown rows loaded 63,549
    Chunk 68: cumulative rows read 6,800,000 | passed rows loaded 6,800,000 | ChrUnknown rows loaded 64,390
    Chunk 69: cumulative rows read 6,900,000 | passed rows loaded 6,900,000 | ChrUnknown rows loaded 65,191
    Chunk 70: cumulative rows read 7,000,000 | passed rows loaded 7,000,000 | ChrUnknown rows loaded 66,038
    Chunk 71: cumulative rows read 7,100,000 | passed rows loaded 7,100,000 | ChrUnknown rows loaded 66,897
    Chunk 72: cumulative rows read 7,200,000 | passed rows loaded 7,200,000 | ChrUnknown rows loaded 67,838
    Chunk 73: cumulative rows read 7,300,000 | passed rows loaded 7,300,000 | ChrUnknown rows loaded 68,698
    Chunk 74: cumulative rows read 7,400,000 | passed rows loaded 7,400,000 | ChrUnknown rows loaded 69,545
    Chunk 75: cumulative rows read 7,500,000 | passed rows loaded 7,500,000 | ChrUnknown rows loaded 70,558
    Chunk 76: cumulative rows read 7,600,000 | passed rows loaded 7,600,000 | ChrUnknown rows loaded 71,510
    Chunk 77: cumulative rows read 7,700,000 | passed rows loaded 7,700,000 | ChrUnknown rows loaded 72,409
    Chunk 78: cumulative rows read 7,800,000 | passed rows loaded 7,800,000 | ChrUnknown rows loaded 73,590
    Chunk 79: cumulative rows read 7,900,000 | passed rows loaded 7,900,000 | ChrUnknown rows loaded 74,653
    Chunk 80: cumulative rows read 8,000,000 | passed rows loaded 8,000,000 | ChrUnknown rows loaded 75,436
    Chunk 81: cumulative rows read 8,100,000 | passed rows loaded 8,100,000 | ChrUnknown rows loaded 76,325
    Chunk 82: cumulative rows read 8,200,000 | passed rows loaded 8,200,000 | ChrUnknown rows loaded 77,330
    Chunk 83: cumulative rows read 8,214,230 | passed rows loaded 8,214,230 | ChrUnknown rows loaded 77,543
    
    ChrUnknown input check passed: 77,543 validated rows loaded into SQLite.
    
    Creating SQLite indexes...
    
    Building complete nonredundant validated feature table...
    
    Exporting complete nonredundant table, complete BED tracks and ChrUnknown-only BED tracks...
    Export chunk 1: cumulative complete nonredundant rows 100,000 | ChrUnknown nonredundant rows 0
    Export chunk 2: cumulative complete nonredundant rows 200,000 | ChrUnknown nonredundant rows 0
    Export chunk 3: cumulative complete nonredundant rows 300,000 | ChrUnknown nonredundant rows 0
    Export chunk 4: cumulative complete nonredundant rows 400,000 | ChrUnknown nonredundant rows 0
    Export chunk 5: cumulative complete nonredundant rows 500,000 | ChrUnknown nonredundant rows 0
    Export chunk 6: cumulative complete nonredundant rows 600,000 | ChrUnknown nonredundant rows 0
    Export chunk 7: cumulative complete nonredundant rows 700,000 | ChrUnknown nonredundant rows 0
    Export chunk 8: cumulative complete nonredundant rows 800,000 | ChrUnknown nonredundant rows 0
    Export chunk 9: cumulative complete nonredundant rows 900,000 | ChrUnknown nonredundant rows 0
    Export chunk 10: cumulative complete nonredundant rows 1,000,000 | ChrUnknown nonredundant rows 0
    Export chunk 11: cumulative complete nonredundant rows 1,100,000 | ChrUnknown nonredundant rows 0
    Export chunk 12: cumulative complete nonredundant rows 1,200,000 | ChrUnknown nonredundant rows 0
    Export chunk 13: cumulative complete nonredundant rows 1,300,000 | ChrUnknown nonredundant rows 0
    Export chunk 14: cumulative complete nonredundant rows 1,400,000 | ChrUnknown nonredundant rows 0
    Export chunk 15: cumulative complete nonredundant rows 1,500,000 | ChrUnknown nonredundant rows 0
    Export chunk 16: cumulative complete nonredundant rows 1,600,000 | ChrUnknown nonredundant rows 0
    Export chunk 17: cumulative complete nonredundant rows 1,700,000 | ChrUnknown nonredundant rows 0
    Export chunk 18: cumulative complete nonredundant rows 1,800,000 | ChrUnknown nonredundant rows 0
    Export chunk 19: cumulative complete nonredundant rows 1,900,000 | ChrUnknown nonredundant rows 0
    Export chunk 20: cumulative complete nonredundant rows 2,000,000 | ChrUnknown nonredundant rows 0
    Export chunk 21: cumulative complete nonredundant rows 2,100,000 | ChrUnknown nonredundant rows 0
    Export chunk 22: cumulative complete nonredundant rows 2,200,000 | ChrUnknown nonredundant rows 0
    Export chunk 23: cumulative complete nonredundant rows 2,300,000 | ChrUnknown nonredundant rows 0
    Export chunk 24: cumulative complete nonredundant rows 2,400,000 | ChrUnknown nonredundant rows 0
    Export chunk 25: cumulative complete nonredundant rows 2,500,000 | ChrUnknown nonredundant rows 0
    Export chunk 26: cumulative complete nonredundant rows 2,600,000 | ChrUnknown nonredundant rows 0
    Export chunk 27: cumulative complete nonredundant rows 2,700,000 | ChrUnknown nonredundant rows 0
    Export chunk 28: cumulative complete nonredundant rows 2,800,000 | ChrUnknown nonredundant rows 0
    Export chunk 29: cumulative complete nonredundant rows 2,900,000 | ChrUnknown nonredundant rows 0
    Export chunk 30: cumulative complete nonredundant rows 3,000,000 | ChrUnknown nonredundant rows 0
    Export chunk 31: cumulative complete nonredundant rows 3,100,000 | ChrUnknown nonredundant rows 0
    Export chunk 32: cumulative complete nonredundant rows 3,173,811 | ChrUnknown nonredundant rows 34,908
    
    ===== STEP 13 COMBINED VALIDATED BED SUMMARY =====
    Validated rows before deduplication: 8,214,230
    Complete nonredundant validated rows: 3,173,811
    Redundant validated rows removed: 5,040,419
    Sequence identifiers represented: 22
    
    ===== ChrUnknown NONREDUNDANT TRACK =====
    ChrUnknown validated rows before deduplication: 77,543
    ChrUnknown nonredundant validated rows: 34,908
    ChrUnknown redundant rows removed: 42,635
    ChrUnknown unique peptide sequences: 21,184
    ChrUnknown unique protein accessions: 5,132
    ChrUnknown unique gene models: 4,974
    
    Complete nonredundant table saved:
      python_outputs\tables\wheat_all_tissues_nonredundant_validated_peptides_step13.csv
    Complete combined BED6 saved:
      python_outputs\bed_validated\FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed6
    Complete combined BED12 saved:
      python_outputs\bed_validated\FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed12
    Standalone ChrUnknown BED6 saved:
      python_outputs\bed_validated\FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed6
    Standalone ChrUnknown BED12 saved:
      python_outputs\bed_validated\FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed12
    Step 13 summary saved:
      python_outputs\tables\wheat_all_tissues_nonredundant_validated_bed_summary_step13.csv
    SQLite database saved:
      python_outputs\tables\wheat_validated_nonredundant_step13.sqlite
    


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
      <th>Validated_rows_before_deduplication</th>
      <th>Nonredundant_validated_rows</th>
      <th>Redundant_validated_rows_removed</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins</th>
      <th>Unique_gene_models</th>
      <th>Unique_chromosomes</th>
      <th>Multi_block_peptides</th>
      <th>Within_exon_peptides</th>
      <th>BED_labels_with_introns</th>
      <th>...</th>
      <th>ChrUnknown_unique_proteins</th>
      <th>ChrUnknown_unique_gene_models</th>
      <th>ChrUnknown_multi_block_peptides</th>
      <th>ChrUnknown_within_exon_peptides</th>
      <th>Combined_table_file</th>
      <th>BED6_file</th>
      <th>BED12_file</th>
      <th>ChrUnknown_BED6_file</th>
      <th>ChrUnknown_BED12_file</th>
      <th>SQLite_database</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8214230</td>
      <td>3173811</td>
      <td>5040419</td>
      <td>1095523</td>
      <td>272298</td>
      <td>243564</td>
      <td>22</td>
      <td>365259</td>
      <td>2808552</td>
      <td>194538</td>
      <td>...</td>
      <td>5132</td>
      <td>4974</td>
      <td>2027</td>
      <td>32881</td>
      <td>wheat_all_tissues_nonredundant_validated_pepti...</td>
      <td>FragPipe_allauthors_allsources_alltissues_nonr...</td>
      <td>FragPipe_allauthors_allsources_alltissues_nonr...</td>
      <td>FragPipe_allauthors_allsources_alltissues_ChrU...</td>
      <td>FragPipe_allauthors_allsources_alltissues_ChrU...</td>
      <td>wheat_validated_nonredundant_step13.sqlite</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 24 columns</p>
</div>


# Step 14 — Rename BED Files for Apollo/JBrowse Public Upload

This step prepares all BED files generated during the proteogenomics workflow for permanent upload to the public Apollo/JBrowse server.

The BED files include:

```text
validated_peptides
```

---

## Input directories

### Annotation-based proteogenomic BED files

```text
python_outputs/bed_validated/
```

---

## Apollo/JBrowse upload directory

A new output directory was created:

```text
python_outputs/bed_validated_apollo/
```

All BED files were copied into this directory and renamed using a standardised Apollo-compatible nomenclature.

---

## Apollo/JBrowse filename nomenclature

The following naming convention was applied:

```text
Vincent_Source_Tissue_projected-peptides_annotation-proteogenomics_20260602.bed
```

for annotation-projected peptide tracks, and:

### Examples

```text
Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_20260602.bed12
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
# Step 14 — Rename validated BED files for Apollo/JBrowse public upload
# ============================================================

import shutil
from pathlib import Path
import re

# -----------------------------
# 1. Input / output directories
# -----------------------------
bed_dir = Path("python_outputs/bed_validated")

# Final Apollo/JBrowse-ready renamed files
apollo_dir = Path("python_outputs/bed_validated_Apollo")
apollo_dir.mkdir(parents=True, exist_ok=True)

# Date suffix for public upload files
date_suffix = "20260805"

# -----------------------------
# 2. Collect all BED files
# -----------------------------
bed_files = sorted(list(bed_dir.glob("*.bed*")))

print(f"BED files found: {len(bed_files):,}")
print(f"Input directory:  {bed_dir}")
print(f"Output directory: {apollo_dir}")


# -----------------------------
# 3. Helper functions
# -----------------------------
def simplify_tissue_name(tissue):
    """
    Standardise tissue names for Apollo filenames.
    """
    tissue = str(tissue)
    tissue = tissue.replace("-", "_")
    tissue = tissue.replace(" ", "_")
    tissue = re.sub(r"_+", "_", tissue)
    return tissue.strip("_")


def parse_standard_bed_filename(filename):
    """
    Parse validated annotation-projected BED filenames.

    Expected individual examples:
        FragPipe_Duncan_PXD004720_anther_validated_peptides.bed6
        FragPipe_Duncan_PXD004720_anther_validated_peptides.bed12

    Also tolerates older pattern:
        FragPipe_Duncan_PXD004720_anther_peptides.bed6
        FragPipe_Duncan_PXD004720_anther_peptides.bed12

    Expected combined examples:
        FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed6
        FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed12
    """

    # -----------------------------
    # A. Standalone ChrUnknown non-redundant BED files
    # -----------------------------
    chrunknown_combined_match = re.match(
        r"FragPipe_allauthors_allsources_alltissues_ChrUnknown_"
        r"nonredundant_validated_peptides\.bed(?P<BedType>6|12)$",
        filename
    )

    if chrunknown_combined_match is not None:
        return {
            "Author": "Vincent",
            "Source": "allsources",
            "Tissue": "ChrUnknown_nonredundant",
            "TrackType": "annotation_ChrUnknown_nonredundant"
        }
        
    # -----------------------------
    # B. Combined all-authors/all-sources/all-tissues non-redundant BED files
    # -----------------------------
    combined_match = re.match(
        r"FragPipe_allauthors_allsources_alltissues_+nonredundant_validated_peptides\.bed(?P<BedType>6|12)$",
        filename
    )

    if combined_match is not None:
        return {
            "Author": "Vincent",
            "Source": "allsources",
            "Tissue": "alltissues_nonredundant",
            "TrackType": "annotation_nonredundant"
        }

    # -----------------------------
    # C. Individual source/tissue validated BED files
    # -----------------------------
    individual_match = re.match(
        r"FragPipe_(?P<Author>[^_]+)_(?P<Source>MSV\d+|PXD\d+)_(?P<Tissue>.+?)_(?:validated_)?peptides\.bed(?P<BedType>6|12)$",
        filename
    )

    if individual_match is not None:
        return {
            # Use Vincent as the public-facing author/pipeline owner
            "Author": "Vincent",
            "Source": individual_match.group("Source"),
            "Tissue": simplify_tissue_name(individual_match.group("Tissue")),
            "TrackType": "annotation_validated"
        }

    return None


def build_apollo_filename(meta, suffix):
    """
    Build Apollo/JBrowse-compatible BED filename.
    """

    if meta["TrackType"] == "annotation_nonredundant":
        track_label = "nonredundant_projected-peptides_annotation-proteogenomics_validated"

    elif meta["TrackType"] == "annotation_validated":
        track_label = "projected-peptides_annotation-proteogenomics_validated"

    else:
        track_label = "proteogenomics_validated"

    return (
        f"{meta['Author']}_"
        f"{meta['Source']}_"
        f"{meta['Tissue']}_"
        f"{track_label}_"
        f"{date_suffix}."
        f"{suffix}"
    )


# -----------------------------
# 4. Copy and rename BED files
# -----------------------------
copied_count = 0
skipped_count = 0
renaming_records = []

for bed_file in bed_files:

    filename = bed_file.name

    # Detect BED suffix
    if filename.endswith(".bed6"):
        suffix = "bed6"
    elif filename.endswith(".bed12"):
        suffix = "bed12"
    else:
        print(f"Skipped non-BED file: {filename}")
        skipped_count += 1
        continue

    # Parse metadata
    if filename.startswith("FragPipe_"):
        meta = parse_standard_bed_filename(filename)
    else:
        meta = None

    if meta is None:
        print(f"Could not parse filename, skipped: {filename}")
        skipped_count += 1
        continue

    # Build Apollo filename
    apollo_filename = build_apollo_filename(meta, suffix)

    destination = apollo_dir / apollo_filename

    shutil.copy2(bed_file, destination)

    copied_count += 1

    renaming_records.append({
        "Original_file": filename,
        "Apollo_file": apollo_filename,
        "Source": meta["Source"],
        "Tissue": meta["Tissue"],
        "TrackType": meta["TrackType"],
        "Suffix": suffix
    })

    print(f"Copied:")
    print(f"  {filename}")
    print(f"  -> {apollo_filename}")


# -----------------------------
# 5. Export renaming manifest
# -----------------------------
if renaming_records:
    import pandas as pd

    rename_manifest = pd.DataFrame(renaming_records)

    rename_manifest_out = (
        Path("python_outputs/tables") /
        "wheat_bed_Apollo_validated_renaming_manifest_step14.csv"
    )

    rename_manifest.to_csv(rename_manifest_out, index=False)

    print(f"\nRenaming manifest saved: {rename_manifest_out}")


print(f"\nApollo BED files prepared: {copied_count:,}")
print(f"BED files skipped: {skipped_count:,}")
print(f"Output directory: {apollo_dir}")
```

    BED files found: 68
    Input directory:  python_outputs\bed_validated
    Output directory: python_outputs\bed_validated_Apollo
    Copied:
      FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed12
      -> Vincent_allsources_ChrUnknown_nonredundant_proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_allauthors_allsources_alltissues_ChrUnknown_nonredundant_validated_peptides.bed6
      -> Vincent_allsources_ChrUnknown_nonredundant_proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed12
      -> Vincent_allsources_alltissues_nonredundant_nonredundant_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_allauthors_allsources_alltissues_nonredundant_validated_peptides.bed6
      -> Vincent_allsources_alltissues_nonredundant_nonredundant_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_anther_validated_peptides.bed12
      -> Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_anther_validated_peptides.bed6
      -> Vincent_PXD004720_anther_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_boot_validated_peptides.bed12
      -> Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_boot_validated_peptides.bed6
      -> Vincent_PXD004720_boot_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_coleoptile_validated_peptides.bed12
      -> Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_coleoptile_validated_peptides.bed6
      -> Vincent_PXD004720_coleoptile_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_embryo_validated_peptides.bed12
      -> Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_embryo_validated_peptides.bed6
      -> Vincent_PXD004720_embryo_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_endosperm_validated_peptides.bed12
      -> Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_endosperm_validated_peptides.bed6
      -> Vincent_PXD004720_endosperm_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_glume_validated_peptides.bed12
      -> Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_glume_validated_peptides.bed6
      -> Vincent_PXD004720_glume_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-70_validated_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-70_validated_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_70_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-71_validated_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-71_validated_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_71_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-75_validated_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-75_validated_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_75_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-83_validated_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-83_validated_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_83_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-87_validated_peptides.bed12
      -> Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_grain-zadoks-87_validated_peptides.bed6
      -> Vincent_PXD004720_grain_zadoks_87_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-mature_validated_peptides.bed12
      -> Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-mature_validated_peptides.bed6
      -> Vincent_PXD004720_leaf_flag_mature_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-senescing_validated_peptides.bed12
      -> Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-senescing_validated_peptides.bed6
      -> Vincent_PXD004720_leaf_flag_senescing_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-young_validated_peptides.bed12
      -> Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_leaf-flag-young_validated_peptides.bed6
      -> Vincent_PXD004720_leaf_flag_young_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_lemma_validated_peptides.bed12
      -> Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_lemma_validated_peptides.bed6
      -> Vincent_PXD004720_lemma_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_node-secretion_validated_peptides.bed12
      -> Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_node-secretion_validated_peptides.bed6
      -> Vincent_PXD004720_node_secretion_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_node_validated_peptides.bed12
      -> Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_node_validated_peptides.bed6
      -> Vincent_PXD004720_node_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_palea_validated_peptides.bed12
      -> Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_palea_validated_peptides.bed6
      -> Vincent_PXD004720_palea_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_pericarp_validated_peptides.bed12
      -> Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_pericarp_validated_peptides.bed6
      -> Vincent_PXD004720_pericarp_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_pollen_validated_peptides.bed12
      -> Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_pollen_validated_peptides.bed6
      -> Vincent_PXD004720_pollen_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_rachilla_validated_peptides.bed12
      -> Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_rachilla_validated_peptides.bed6
      -> Vincent_PXD004720_rachilla_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_radicle_validated_peptides.bed12
      -> Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_radicle_validated_peptides.bed6
      -> Vincent_PXD004720_radicle_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-mature_validated_peptides.bed12
      -> Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-mature_validated_peptides.bed6
      -> Vincent_PXD004720_root_mature_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-secretion_validated_peptides.bed12
      -> Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-secretion_validated_peptides.bed6
      -> Vincent_PXD004720_root_secretion_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-tip_validated_peptides.bed12
      -> Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-tip_validated_peptides.bed6
      -> Vincent_PXD004720_root_tip_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_root-vasculature_validated_peptides.bed12
      -> Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_root-vasculature_validated_peptides.bed6
      -> Vincent_PXD004720_root_vasculature_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_spike-immature_validated_peptides.bed12
      -> Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_spike-immature_validated_peptides.bed6
      -> Vincent_PXD004720_spike_immature_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Duncan_PXD004720_stem_validated_peptides.bed12
      -> Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Duncan_PXD004720_stem_validated_peptides.bed6
      -> Vincent_PXD004720_stem_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Liu_PXD050500_coleoptile_validated_peptides.bed12
      -> Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Liu_PXD050500_coleoptile_validated_peptides.bed6
      -> Vincent_PXD050500_coleoptile_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Liu_PXD050500_node_validated_peptides.bed12
      -> Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Liu_PXD050500_node_validated_peptides.bed6
      -> Vincent_PXD050500_node_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Liu_PXD050500_radicle_validated_peptides.bed12
      -> Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Liu_PXD050500_radicle_validated_peptides.bed6
      -> Vincent_PXD050500_radicle_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    Copied:
      FragPipe_Vincent_MSV000090572_stored-grain_validated_peptides.bed12
      -> Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_validated_20260805.bed12
    Copied:
      FragPipe_Vincent_MSV000090572_stored-grain_validated_peptides.bed6
      -> Vincent_MSV000090572_stored_grain_projected-peptides_annotation-proteogenomics_validated_20260805.bed6
    
    Renaming manifest saved: python_outputs\tables\wheat_bed_Apollo_validated_renaming_manifest_step14.csv
    
    Apollo BED files prepared: 68
    BED files skipped: 0
    Output directory: python_outputs\bed_validated_Apollo
    

# Step 15 — Generate Tissue, Protein, Gene, and Isoform Summary Tables

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
wheat_tissue_level_summary_step15.csv
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
wheat_gene_model_summary_step14.csv
```

This table captures the number of peptides, protein isoforms, tissues, and sources supporting each gene model.

---

### 3. Protein / isoform summary

One row per detected protein isoform.

```text
wheat_protein_isoform_summary_step15.csv
```

This table captures the number of peptides, tissues, and sources supporting each protein isoform.

---

### 4. Source-level summary

One row per public proteomics repository/source.

```text
wheat_source_level_summary_step15.csv
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
# Step 15 — Tissue, protein, gene, and isoform summary tables (takes 15 min)
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
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )

tissue_summary_out = tables_dir / "wheat_tissue_level_summary_step15.csv"
gene_summary_out = tables_dir / "wheat_gene_model_summary_step15.csv"
protein_summary_out = tables_dir / "wheat_protein_isoform_summary_step15.csv"
source_summary_out = tables_dir / "wheat_source_level_summary_step15.csv"

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
# 4. Load fully validated peptide projection rows
# -----------------------------
# Step 15 now summarises only rows that passed:
# Step 10 translation validation + Step 11 sanity checks

print("\nLoading fully validated peptide projection rows from Step 11...")

usecols_needed = [
    "Source",
    "Species",
    "Tissue",
    "Batch",
    "Peptide",
    "ProteinID",
    gene_col,
    confidence_col,
    "Chromosome",
    "BED_block_count",
    "Sanity_check_status"
]

# Keep only columns that are actually present in the Step 11 file
header = pd.read_csv(sanity_file, nrows=0)
available_usecols = [c for c in usecols_needed if c in header.columns]

missing_core_cols = [
    c for c in [
        "Source",
        "Species",
        "Tissue",
        "Batch",
        "Peptide",
        "ProteinID",
        gene_col,
        confidence_col,
        "Chromosome",
        "BED_block_count",
        "Sanity_check_status"
    ]
    if c not in header.columns
]

if missing_core_cols:
    raise KeyError(
        f"Missing required column(s) in Step 11 sanity-check table: {missing_core_cols}"
    )

all_projected_tables = []

for chunk in pd.read_csv(
    sanity_file,
    usecols=available_usecols,
    chunksize=100_000,
    low_memory=False
):

    chunk = chunk[
        chunk["Sanity_check_status"].astype(str) == "passed"
    ].copy()

    if chunk.empty:
        continue

    chunk["BED_block_count"] = pd.to_numeric(
        chunk["BED_block_count"],
        errors="coerce"
    )

    all_projected_tables.append(chunk)

if not all_projected_tables:
    raise ValueError(
        "No fully validated peptide projection rows were loaded from Step 11."
    )

all_projected = pd.concat(all_projected_tables, ignore_index=True)

print(f"\nFully validated peptide rows loaded: {len(all_projected):,}")


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
        "Validated_peptide_rows": len(group),
        "Unique_peptides": group["Peptide"].nunique(),
        "Unique_proteins_isoforms": group["ProteinID"].nunique(),
        "Unique_gene_models": unique_genes,
        "Unique_HC_gene_models": unique_hc_genes,
        "Unique_LC_gene_models": unique_lc_genes,
        "Percent_total_gene_models_detected": pct(unique_genes, total_gene_models),
        "Percent_HC_gene_models_detected": pct(unique_hc_genes, total_hc_gene_models),
        "Percent_LC_gene_models_detected": pct(unique_lc_genes, total_lc_gene_models),
        "Unique_chromosomes": group["Chromosome"].nunique(),
        "Multi_exon_peptide_rows": int((group["BED_block_count"] > 1).sum()),
        "Within_exon_peptide_rows": int((group["BED_block_count"] == 1).sum()),
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
        Validated_peptide_rows=("Peptide", "size"),
        Unique_peptides=("Peptide", "nunique"),
        Unique_proteins_isoforms=("ProteinID", "nunique"),
        Unique_chromosomes=("Chromosome", "nunique"),
        Multi_exon_peptide_rows=("BED_block_count", lambda x: int((x > 1).sum())),
        Within_exon_peptide_rows=("BED_block_count", lambda x: int((x == 1).sum()))
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
        Validated_peptide_rows=("Peptide", "size"),
        Unique_peptides=("Peptide", "nunique"),
        Unique_chromosomes=("Chromosome", "nunique"),
        Multi_exon_peptide_rows=("BED_block_count", lambda x: int((x > 1).sum())),
        Within_exon_peptide_rows=("BED_block_count", lambda x: int((x == 1).sum()))
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
        "Validated_peptide_rows": len(group),
        "Multi_exon_peptide_rows": int((group["BED_block_count"] > 1).sum()),
        "Within_exon_peptide_rows": int((group["BED_block_count"] == 1).sum()),
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
    
    Loading fully validated peptide projection rows from Step 11...
    
    Fully validated peptide rows loaded: 8,214,230
    
    Tissue-level summary saved: python_outputs\tables\wheat_tissue_level_summary_step15.csv
    Gene model summary saved: python_outputs\tables\wheat_gene_model_summary_step15.csv
    Protein/isoform summary saved: python_outputs\tables\wheat_protein_isoform_summary_step15.csv
    Source-level summary saved: python_outputs\tables\wheat_source_level_summary_step15.csv
    


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
      <th>Validated_peptide_rows</th>
      <th>Unique_peptides</th>
      <th>Unique_proteins_isoforms</th>
      <th>Unique_gene_models</th>
      <th>Unique_HC_gene_models</th>
      <th>Unique_LC_gene_models</th>
      <th>Percent_total_gene_models_detected</th>
      <th>Percent_HC_gene_models_detected</th>
      <th>Percent_LC_gene_models_detected</th>
      <th>Unique_chromosomes</th>
      <th>Multi_exon_peptide_rows</th>
      <th>Within_exon_peptide_rows</th>
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
      <td>29892</td>
      <td>9126</td>
      <td>17110</td>
      <td>14536</td>
      <td>9126</td>
      <td>5410</td>
      <td>5.4493</td>
      <td>8.5358</td>
      <td>3.3847</td>
      <td>22</td>
      <td>3262</td>
      <td>26630</td>
      <td>13795</td>
      <td>3315</td>
      <td>11749</td>
      <td>2787</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>163467</td>
      <td>33982</td>
      <td>36275</td>
      <td>28845</td>
      <td>21409</td>
      <td>7436</td>
      <td>10.8134</td>
      <td>20.0245</td>
      <td>4.6522</td>
      <td>22</td>
      <td>27708</td>
      <td>135759</td>
      <td>19459</td>
      <td>16816</td>
      <td>16079</td>
      <td>12766</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>13137</td>
      <td>3599</td>
      <td>9126</td>
      <td>7279</td>
      <td>5415</td>
      <td>1864</td>
      <td>2.7288</td>
      <td>5.0648</td>
      <td>1.1662</td>
      <td>22</td>
      <td>2723</td>
      <td>10414</td>
      <td>7208</td>
      <td>1918</td>
      <td>5820</td>
      <td>1459</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>203264</td>
      <td>40861</td>
      <td>45819</td>
      <td>36208</td>
      <td>26797</td>
      <td>9411</td>
      <td>13.5737</td>
      <td>25.0641</td>
      <td>5.8878</td>
      <td>22</td>
      <td>31278</td>
      <td>171986</td>
      <td>23052</td>
      <td>22767</td>
      <td>19309</td>
      <td>16899</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>8742</td>
      <td>2815</td>
      <td>7110</td>
      <td>5749</td>
      <td>4204</td>
      <td>1545</td>
      <td>2.1552</td>
      <td>3.9321</td>
      <td>0.9666</td>
      <td>22</td>
      <td>1407</td>
      <td>7335</td>
      <td>6175</td>
      <td>935</td>
      <td>5043</td>
      <td>706</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>102289</td>
      <td>19953</td>
      <td>27099</td>
      <td>21529</td>
      <td>16036</td>
      <td>5493</td>
      <td>8.0708</td>
      <td>14.9990</td>
      <td>3.4366</td>
      <td>22</td>
      <td>14237</td>
      <td>88052</td>
      <td>15563</td>
      <td>11536</td>
      <td>12857</td>
      <td>8672</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>144079</td>
      <td>28512</td>
      <td>35014</td>
      <td>28205</td>
      <td>20534</td>
      <td>7671</td>
      <td>10.5735</td>
      <td>19.2061</td>
      <td>4.7992</td>
      <td>22</td>
      <td>22077</td>
      <td>122002</td>
      <td>19568</td>
      <td>15446</td>
      <td>16269</td>
      <td>11936</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-70</td>
      <td>single</td>
      <td>125355</td>
      <td>26037</td>
      <td>34929</td>
      <td>28080</td>
      <td>20611</td>
      <td>7469</td>
      <td>10.5266</td>
      <td>19.2781</td>
      <td>4.6729</td>
      <td>22</td>
      <td>17442</td>
      <td>107913</td>
      <td>19990</td>
      <td>14939</td>
      <td>16743</td>
      <td>11337</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-71</td>
      <td>single</td>
      <td>178814</td>
      <td>35806</td>
      <td>46422</td>
      <td>36269</td>
      <td>26965</td>
      <td>9304</td>
      <td>13.5965</td>
      <td>25.2212</td>
      <td>5.8209</td>
      <td>22</td>
      <td>27602</td>
      <td>151212</td>
      <td>24143</td>
      <td>22279</td>
      <td>20226</td>
      <td>16043</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-75</td>
      <td>single</td>
      <td>132081</td>
      <td>27293</td>
      <td>40582</td>
      <td>32167</td>
      <td>24243</td>
      <td>7924</td>
      <td>12.0588</td>
      <td>22.6752</td>
      <td>4.9575</td>
      <td>22</td>
      <td>18607</td>
      <td>113474</td>
      <td>22866</td>
      <td>17716</td>
      <td>19091</td>
      <td>13076</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-83</td>
      <td>single</td>
      <td>112389</td>
      <td>23840</td>
      <td>36046</td>
      <td>28854</td>
      <td>21170</td>
      <td>7684</td>
      <td>10.8168</td>
      <td>19.8010</td>
      <td>4.8074</td>
      <td>22</td>
      <td>14700</td>
      <td>97689</td>
      <td>21173</td>
      <td>14873</td>
      <td>17735</td>
      <td>11119</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain-zadoks-87</td>
      <td>single</td>
      <td>111156</td>
      <td>24482</td>
      <td>34405</td>
      <td>27624</td>
      <td>20014</td>
      <td>7610</td>
      <td>10.3557</td>
      <td>18.7197</td>
      <td>4.7611</td>
      <td>22</td>
      <td>14850</td>
      <td>96306</td>
      <td>20841</td>
      <td>13564</td>
      <td>17352</td>
      <td>10272</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-mature</td>
      <td>single</td>
      <td>144641</td>
      <td>29731</td>
      <td>37453</td>
      <td>29882</td>
      <td>22443</td>
      <td>7439</td>
      <td>11.2022</td>
      <td>20.9916</td>
      <td>4.6541</td>
      <td>22</td>
      <td>19405</td>
      <td>125236</td>
      <td>19392</td>
      <td>18061</td>
      <td>16077</td>
      <td>13805</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-senescing</td>
      <td>single</td>
      <td>45680</td>
      <td>11204</td>
      <td>25275</td>
      <td>20842</td>
      <td>14335</td>
      <td>6507</td>
      <td>7.8132</td>
      <td>13.4080</td>
      <td>4.0710</td>
      <td>22</td>
      <td>4552</td>
      <td>41128</td>
      <td>18466</td>
      <td>6809</td>
      <td>15506</td>
      <td>5336</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf-flag-young</td>
      <td>single</td>
      <td>119922</td>
      <td>23296</td>
      <td>32180</td>
      <td>25809</td>
      <td>18864</td>
      <td>6945</td>
      <td>9.6753</td>
      <td>17.6441</td>
      <td>4.3450</td>
      <td>22</td>
      <td>15181</td>
      <td>104741</td>
      <td>17214</td>
      <td>14966</td>
      <td>14228</td>
      <td>11581</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>146562</td>
      <td>29653</td>
      <td>37386</td>
      <td>29915</td>
      <td>21824</td>
      <td>8091</td>
      <td>11.2145</td>
      <td>20.4127</td>
      <td>5.0620</td>
      <td>22</td>
      <td>21700</td>
      <td>124862</td>
      <td>20460</td>
      <td>16926</td>
      <td>16936</td>
      <td>12979</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>98731</td>
      <td>21280</td>
      <td>35794</td>
      <td>29228</td>
      <td>19853</td>
      <td>9375</td>
      <td>10.9570</td>
      <td>18.5691</td>
      <td>5.8653</td>
      <td>22</td>
      <td>12726</td>
      <td>86005</td>
      <td>22750</td>
      <td>13044</td>
      <td>19083</td>
      <td>10145</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>168564</td>
      <td>34026</td>
      <td>41769</td>
      <td>33166</td>
      <td>24936</td>
      <td>8230</td>
      <td>12.4333</td>
      <td>23.3234</td>
      <td>5.1490</td>
      <td>22</td>
      <td>22830</td>
      <td>145734</td>
      <td>20940</td>
      <td>20829</td>
      <td>17524</td>
      <td>15642</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>116285</td>
      <td>21623</td>
      <td>27295</td>
      <td>21503</td>
      <td>16391</td>
      <td>5112</td>
      <td>8.0610</td>
      <td>15.3310</td>
      <td>3.1982</td>
      <td>22</td>
      <td>20637</td>
      <td>95648</td>
      <td>13831</td>
      <td>13464</td>
      <td>11226</td>
      <td>10277</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>130645</td>
      <td>28184</td>
      <td>32281</td>
      <td>25580</td>
      <td>18912</td>
      <td>6668</td>
      <td>9.5894</td>
      <td>17.6890</td>
      <td>4.1717</td>
      <td>22</td>
      <td>20924</td>
      <td>109721</td>
      <td>18276</td>
      <td>14005</td>
      <td>15075</td>
      <td>10505</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>74334</td>
      <td>13446</td>
      <td>19731</td>
      <td>15866</td>
      <td>12172</td>
      <td>3694</td>
      <td>5.9478</td>
      <td>11.3849</td>
      <td>2.3111</td>
      <td>22</td>
      <td>9467</td>
      <td>64867</td>
      <td>10660</td>
      <td>9071</td>
      <td>8746</td>
      <td>7120</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>159219</td>
      <td>31008</td>
      <td>36663</td>
      <td>29020</td>
      <td>21433</td>
      <td>7587</td>
      <td>10.8790</td>
      <td>20.0470</td>
      <td>4.7467</td>
      <td>22</td>
      <td>24725</td>
      <td>134494</td>
      <td>19174</td>
      <td>17489</td>
      <td>15896</td>
      <td>13124</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>193938</td>
      <td>39487</td>
      <td>42476</td>
      <td>33385</td>
      <td>25692</td>
      <td>7693</td>
      <td>12.5154</td>
      <td>24.0305</td>
      <td>4.8130</td>
      <td>22</td>
      <td>32434</td>
      <td>161504</td>
      <td>21978</td>
      <td>20498</td>
      <td>18319</td>
      <td>15066</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-mature</td>
      <td>single</td>
      <td>96387</td>
      <td>21125</td>
      <td>38544</td>
      <td>30952</td>
      <td>22134</td>
      <td>8818</td>
      <td>11.6033</td>
      <td>20.7026</td>
      <td>5.5168</td>
      <td>22</td>
      <td>10853</td>
      <td>85534</td>
      <td>25747</td>
      <td>12797</td>
      <td>21312</td>
      <td>9640</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-secretion</td>
      <td>single</td>
      <td>100085</td>
      <td>21111</td>
      <td>31657</td>
      <td>25126</td>
      <td>18683</td>
      <td>6443</td>
      <td>9.4192</td>
      <td>17.4748</td>
      <td>4.0310</td>
      <td>22</td>
      <td>15505</td>
      <td>84580</td>
      <td>19699</td>
      <td>11958</td>
      <td>16136</td>
      <td>8990</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-tip</td>
      <td>single</td>
      <td>191262</td>
      <td>38496</td>
      <td>39337</td>
      <td>30508</td>
      <td>23693</td>
      <td>6815</td>
      <td>11.4368</td>
      <td>22.1608</td>
      <td>4.2637</td>
      <td>22</td>
      <td>34992</td>
      <td>156270</td>
      <td>18497</td>
      <td>20840</td>
      <td>15314</td>
      <td>15194</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root-vasculature</td>
      <td>single</td>
      <td>111315</td>
      <td>20728</td>
      <td>30323</td>
      <td>23512</td>
      <td>18192</td>
      <td>5320</td>
      <td>8.8142</td>
      <td>17.0155</td>
      <td>3.3284</td>
      <td>22</td>
      <td>14786</td>
      <td>96529</td>
      <td>16436</td>
      <td>13887</td>
      <td>13380</td>
      <td>10132</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike-immature</td>
      <td>single</td>
      <td>188025</td>
      <td>36236</td>
      <td>39779</td>
      <td>30611</td>
      <td>23515</td>
      <td>7096</td>
      <td>11.4755</td>
      <td>21.9943</td>
      <td>4.4395</td>
      <td>22</td>
      <td>33123</td>
      <td>154902</td>
      <td>19526</td>
      <td>20253</td>
      <td>16121</td>
      <td>14490</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>60181</td>
      <td>14177</td>
      <td>28948</td>
      <td>23218</td>
      <td>16618</td>
      <td>6600</td>
      <td>8.7040</td>
      <td>15.5433</td>
      <td>4.1292</td>
      <td>22</td>
      <td>6927</td>
      <td>53254</td>
      <td>19771</td>
      <td>9177</td>
      <td>16359</td>
      <td>6859</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>1829196</td>
      <td>574831</td>
      <td>233744</td>
      <td>206142</td>
      <td>97341</td>
      <td>108801</td>
      <td>77.2785</td>
      <td>91.0461</td>
      <td>68.0695</td>
      <td>22</td>
      <td>227461</td>
      <td>1601735</td>
      <td>58234</td>
      <td>175510</td>
      <td>56145</td>
      <td>149997</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>1864415</td>
      <td>587392</td>
      <td>237191</td>
      <td>209468</td>
      <td>98102</td>
      <td>111366</td>
      <td>78.5254</td>
      <td>91.7579</td>
      <td>69.6743</td>
      <td>22</td>
      <td>234600</td>
      <td>1629815</td>
      <td>56556</td>
      <td>180635</td>
      <td>54455</td>
      <td>155013</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>1050178</td>
      <td>328566</td>
      <td>201263</td>
      <td>175179</td>
      <td>89823</td>
      <td>85356</td>
      <td>65.6711</td>
      <td>84.0143</td>
      <td>53.4016</td>
      <td>22</td>
      <td>117686</td>
      <td>932492</td>
      <td>66435</td>
      <td>134828</td>
      <td>63043</td>
      <td>112136</td>
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
      <th>Validated_peptide_rows</th>
      <th>Multi_exon_peptide_rows</th>
      <th>Within_exon_peptide_rows</th>
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
      <td>29892</td>
      <td>3262</td>
      <td>26630</td>
      <td>1</td>
      <td>9126</td>
      <td>17110</td>
      <td>14536</td>
      <td>9126</td>
      <td>5410</td>
      <td>5.4493</td>
      <td>8.5358</td>
      <td>3.3847</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720</td>
      <td>3440549</td>
      <td>513398</td>
      <td>2927151</td>
      <td>28</td>
      <td>231901</td>
      <td>169983</td>
      <td>146667</td>
      <td>79627</td>
      <td>67040</td>
      <td>54.9825</td>
      <td>74.4776</td>
      <td>41.9425</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>4743789</td>
      <td>579747</td>
      <td>4164042</td>
      <td>3</td>
      <td>976526</td>
      <td>268333</td>
      <td>239699</td>
      <td>103770</td>
      <td>135929</td>
      <td>89.8584</td>
      <td>97.0593</td>
      <td>85.0417</td>
    </tr>
  </tbody>
</table>
</div>


# Step 16 — EDA: Cumulated bar plots of HC and LC Proteogenomic Coverage by Tissue

This exploratory analysis compares proteogenomic evidence across all wheat source–tissue combinations.

The aim is to visualise how much annotation-supported proteomic evidence was obtained from each tissue, separated into:

```text
high-confidence annotation-projected evidence
low-confidence annotation-projected evidence
```

---

## Input files

### Validated peptide genome projection tables from Step 11

```text
wheat_projection_translation_validated_sanity_checks_full_step11.csv
```

Only validated peptide rows were included.

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
step16_source_tissue_protein_coverage_HC_LC.png
```

---

## Output files

### Summary table

```text
wheat_eda_HC_LC_coverage_step16.csv
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
```

    Genome annotation denominators
    Total gene models: 266,752
    HC gene models: 106,914
    LC gene models: 159,838
    Protein isoforms: 295,914
    
    Loading fully validated rows from Step 11...
    Fully validated rows loaded for Step 16: 8,214,230
    Saved Step 16 validated HC/LC coverage summary: python_outputs\tables\wheat_eda_coverage_HC_LC_validated_step16.csv
    


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
      <th>Total_unique_proteins</th>
      <th>HC_unique_gene_models</th>
      <th>LC_unique_gene_models</th>
      <th>Total_unique_gene_models</th>
      <th>HC_unique_peptides</th>
      <th>...</th>
      <th>Validated_BED_rows</th>
      <th>Multi_exon_peptide_rows</th>
      <th>Within_exon_peptide_rows</th>
      <th>Unique_chromosomes</th>
      <th>HC_protein_percent</th>
      <th>LC_protein_percent</th>
      <th>Total_protein_percent</th>
      <th>HC_gene_model_percent</th>
      <th>LC_gene_model_percent</th>
      <th>Total_gene_model_percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>embryo</td>
      <td>PXD004720_embryo</td>
      <td>5534</td>
      <td>1576</td>
      <td>7110</td>
      <td>4204</td>
      <td>1545</td>
      <td>5749</td>
      <td>2160</td>
      <td>...</td>
      <td>8742</td>
      <td>1407</td>
      <td>7335</td>
      <td>22</td>
      <td>1.870138</td>
      <td>0.532587</td>
      <td>2.402725</td>
      <td>3.932132</td>
      <td>0.966604</td>
      <td>2.155185</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>boot</td>
      <td>PXD004720_boot</td>
      <td>7219</td>
      <td>1907</td>
      <td>9126</td>
      <td>5415</td>
      <td>1864</td>
      <td>7279</td>
      <td>2877</td>
      <td>...</td>
      <td>13137</td>
      <td>2723</td>
      <td>10414</td>
      <td>22</td>
      <td>2.439560</td>
      <td>0.644444</td>
      <td>3.084004</td>
      <td>5.064818</td>
      <td>1.166181</td>
      <td>2.728752</td>
    </tr>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>11604</td>
      <td>5506</td>
      <td>17110</td>
      <td>9126</td>
      <td>5410</td>
      <td>14536</td>
      <td>6375</td>
      <td>...</td>
      <td>29892</td>
      <td>3262</td>
      <td>26630</td>
      <td>22</td>
      <td>3.921410</td>
      <td>1.860676</td>
      <td>5.782085</td>
      <td>8.535833</td>
      <td>3.384677</td>
      <td>5.449256</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>pollen</td>
      <td>PXD004720_pollen</td>
      <td>15974</td>
      <td>3757</td>
      <td>19731</td>
      <td>12172</td>
      <td>3694</td>
      <td>15866</td>
      <td>12487</td>
      <td>...</td>
      <td>74334</td>
      <td>9467</td>
      <td>64867</td>
      <td>22</td>
      <td>5.398190</td>
      <td>1.269626</td>
      <td>6.667816</td>
      <td>11.384851</td>
      <td>2.311090</td>
      <td>5.947847</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>leaf-flag-senescing</td>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>18636</td>
      <td>6639</td>
      <td>25275</td>
      <td>14335</td>
      <td>6507</td>
      <td>20842</td>
      <td>8792</td>
      <td>...</td>
      <td>45680</td>
      <td>4552</td>
      <td>41128</td>
      <td>22</td>
      <td>6.297776</td>
      <td>2.243557</td>
      <td>8.541333</td>
      <td>13.407973</td>
      <td>4.070997</td>
      <td>7.813250</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



    
![png](output_33_2.png)
    


    Figure saved: python_outputs\figures\step16_source_tissue_protein_coverage_HC_LC_validated.png
    


    
![png](output_33_4.png)
    


    Figure saved: python_outputs\figures\step16_source_tissue_gene_model_coverage_HC_LC_validated.png
    


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
      <th>Total_unique_proteins</th>
      <th>HC_unique_gene_models</th>
      <th>LC_unique_gene_models</th>
      <th>Total_unique_gene_models</th>
      <th>HC_unique_peptides</th>
      <th>...</th>
      <th>Validated_BED_rows</th>
      <th>Multi_exon_peptide_rows</th>
      <th>Within_exon_peptide_rows</th>
      <th>Unique_chromosomes</th>
      <th>HC_protein_percent</th>
      <th>LC_protein_percent</th>
      <th>Total_protein_percent</th>
      <th>HC_gene_model_percent</th>
      <th>LC_gene_model_percent</th>
      <th>Total_gene_model_percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>embryo</td>
      <td>PXD004720_embryo</td>
      <td>5534</td>
      <td>1576</td>
      <td>7110</td>
      <td>4204</td>
      <td>1545</td>
      <td>5749</td>
      <td>2160</td>
      <td>...</td>
      <td>8742</td>
      <td>1407</td>
      <td>7335</td>
      <td>22</td>
      <td>1.870138</td>
      <td>0.532587</td>
      <td>2.402725</td>
      <td>3.932132</td>
      <td>0.966604</td>
      <td>2.155185</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>boot</td>
      <td>PXD004720_boot</td>
      <td>7219</td>
      <td>1907</td>
      <td>9126</td>
      <td>5415</td>
      <td>1864</td>
      <td>7279</td>
      <td>2877</td>
      <td>...</td>
      <td>13137</td>
      <td>2723</td>
      <td>10414</td>
      <td>22</td>
      <td>2.439560</td>
      <td>0.644444</td>
      <td>3.084004</td>
      <td>5.064818</td>
      <td>1.166181</td>
      <td>2.728752</td>
    </tr>
    <tr>
      <th>0</th>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>MSV000090572_stored_grain</td>
      <td>11604</td>
      <td>5506</td>
      <td>17110</td>
      <td>9126</td>
      <td>5410</td>
      <td>14536</td>
      <td>6375</td>
      <td>...</td>
      <td>29892</td>
      <td>3262</td>
      <td>26630</td>
      <td>22</td>
      <td>3.921410</td>
      <td>1.860676</td>
      <td>5.782085</td>
      <td>8.535833</td>
      <td>3.384677</td>
      <td>5.449256</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>pollen</td>
      <td>PXD004720_pollen</td>
      <td>15974</td>
      <td>3757</td>
      <td>19731</td>
      <td>12172</td>
      <td>3694</td>
      <td>15866</td>
      <td>12487</td>
      <td>...</td>
      <td>74334</td>
      <td>9467</td>
      <td>64867</td>
      <td>22</td>
      <td>5.398190</td>
      <td>1.269626</td>
      <td>6.667816</td>
      <td>11.384851</td>
      <td>2.311090</td>
      <td>5.947847</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>leaf-flag-senescing</td>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>18636</td>
      <td>6639</td>
      <td>25275</td>
      <td>14335</td>
      <td>6507</td>
      <td>20842</td>
      <td>8792</td>
      <td>...</td>
      <td>45680</td>
      <td>4552</td>
      <td>41128</td>
      <td>22</td>
      <td>6.297776</td>
      <td>2.243557</td>
      <td>8.541333</td>
      <td>13.407973</td>
      <td>4.070997</td>
      <td>7.813250</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>palea</td>
      <td>PXD004720_palea</td>
      <td>22101</td>
      <td>5194</td>
      <td>27295</td>
      <td>16391</td>
      <td>5112</td>
      <td>21503</td>
      <td>20177</td>
      <td>...</td>
      <td>116285</td>
      <td>20637</td>
      <td>95648</td>
      <td>22</td>
      <td>7.468724</td>
      <td>1.755240</td>
      <td>9.223964</td>
      <td>15.331014</td>
      <td>3.198238</td>
      <td>8.061045</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>endosperm</td>
      <td>PXD004720_endosperm</td>
      <td>21497</td>
      <td>5602</td>
      <td>27099</td>
      <td>16036</td>
      <td>5493</td>
      <td>21529</td>
      <td>18132</td>
      <td>...</td>
      <td>102289</td>
      <td>14237</td>
      <td>88052</td>
      <td>22</td>
      <td>7.264611</td>
      <td>1.893118</td>
      <td>9.157728</td>
      <td>14.998971</td>
      <td>3.436605</td>
      <td>8.070792</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>stem</td>
      <td>PXD004720_stem</td>
      <td>22190</td>
      <td>6758</td>
      <td>28948</td>
      <td>16618</td>
      <td>6600</td>
      <td>23218</td>
      <td>11554</td>
      <td>...</td>
      <td>60181</td>
      <td>6927</td>
      <td>53254</td>
      <td>22</td>
      <td>7.498800</td>
      <td>2.283772</td>
      <td>9.782572</td>
      <td>15.543334</td>
      <td>4.129181</td>
      <td>8.703965</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>root-vasculature</td>
      <td>PXD004720_root-vasculature</td>
      <td>24874</td>
      <td>5449</td>
      <td>30323</td>
      <td>18192</td>
      <td>5320</td>
      <td>23512</td>
      <td>19168</td>
      <td>...</td>
      <td>111315</td>
      <td>14786</td>
      <td>96529</td>
      <td>22</td>
      <td>8.405821</td>
      <td>1.841413</td>
      <td>10.247234</td>
      <td>17.015545</td>
      <td>3.328370</td>
      <td>8.814179</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>root-secretion</td>
      <td>PXD004720_root-secretion</td>
      <td>25091</td>
      <td>6566</td>
      <td>31657</td>
      <td>18683</td>
      <td>6443</td>
      <td>25126</td>
      <td>18188</td>
      <td>...</td>
      <td>100085</td>
      <td>15505</td>
      <td>84580</td>
      <td>22</td>
      <td>8.479153</td>
      <td>2.218888</td>
      <td>10.698041</td>
      <td>17.474793</td>
      <td>4.030956</td>
      <td>9.419236</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>pericarp</td>
      <td>PXD004720_pericarp</td>
      <td>25476</td>
      <td>6805</td>
      <td>32281</td>
      <td>18912</td>
      <td>6668</td>
      <td>25580</td>
      <td>25757</td>
      <td>...</td>
      <td>130645</td>
      <td>20924</td>
      <td>109721</td>
      <td>22</td>
      <td>8.609258</td>
      <td>2.299655</td>
      <td>10.908913</td>
      <td>17.688984</td>
      <td>4.171724</td>
      <td>9.589431</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>leaf-flag-young</td>
      <td>PXD004720_leaf-flag-young</td>
      <td>25092</td>
      <td>7088</td>
      <td>32180</td>
      <td>18864</td>
      <td>6945</td>
      <td>25809</td>
      <td>21772</td>
      <td>...</td>
      <td>119922</td>
      <td>15181</td>
      <td>104741</td>
      <td>22</td>
      <td>8.479491</td>
      <td>2.395291</td>
      <td>10.874781</td>
      <td>17.644088</td>
      <td>4.345024</td>
      <td>9.675279</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>grain-zadoks-87</td>
      <td>PXD004720_grain-zadoks-87</td>
      <td>26638</td>
      <td>7767</td>
      <td>34405</td>
      <td>20014</td>
      <td>7610</td>
      <td>27624</td>
      <td>21651</td>
      <td>...</td>
      <td>111156</td>
      <td>14850</td>
      <td>96306</td>
      <td>22</td>
      <td>9.001940</td>
      <td>2.624749</td>
      <td>11.626689</td>
      <td>18.719719</td>
      <td>4.761071</td>
      <td>10.355686</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>grain-zadoks-70</td>
      <td>PXD004720_grain-zadoks-70</td>
      <td>27314</td>
      <td>7615</td>
      <td>34929</td>
      <td>20611</td>
      <td>7469</td>
      <td>28080</td>
      <td>23662</td>
      <td>...</td>
      <td>125355</td>
      <td>17442</td>
      <td>107913</td>
      <td>22</td>
      <td>9.230385</td>
      <td>2.573383</td>
      <td>11.803767</td>
      <td>19.278111</td>
      <td>4.672856</td>
      <td>10.526631</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>glume</td>
      <td>PXD004720_glume</td>
      <td>27208</td>
      <td>7806</td>
      <td>35014</td>
      <td>20534</td>
      <td>7671</td>
      <td>28205</td>
      <td>26101</td>
      <td>...</td>
      <td>144079</td>
      <td>22077</td>
      <td>122002</td>
      <td>22</td>
      <td>9.194563</td>
      <td>2.637929</td>
      <td>11.832492</td>
      <td>19.206091</td>
      <td>4.799234</td>
      <td>10.573491</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>anther</td>
      <td>PXD004720_anther</td>
      <td>28669</td>
      <td>7606</td>
      <td>36275</td>
      <td>21409</td>
      <td>7436</td>
      <td>28845</td>
      <td>31552</td>
      <td>...</td>
      <td>163467</td>
      <td>27708</td>
      <td>135759</td>
      <td>22</td>
      <td>9.688288</td>
      <td>2.570341</td>
      <td>12.258629</td>
      <td>20.024506</td>
      <td>4.652210</td>
      <td>10.813415</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>grain-zadoks-83</td>
      <td>PXD004720_grain-zadoks-83</td>
      <td>28200</td>
      <td>7846</td>
      <td>36046</td>
      <td>21170</td>
      <td>7684</td>
      <td>28854</td>
      <td>21217</td>
      <td>...</td>
      <td>112389</td>
      <td>14700</td>
      <td>97689</td>
      <td>22</td>
      <td>9.529796</td>
      <td>2.651446</td>
      <td>12.181242</td>
      <td>19.800962</td>
      <td>4.807367</td>
      <td>10.816789</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>rachilla</td>
      <td>PXD004720_rachilla</td>
      <td>28936</td>
      <td>7727</td>
      <td>36663</td>
      <td>21433</td>
      <td>7587</td>
      <td>29020</td>
      <td>28803</td>
      <td>...</td>
      <td>159219</td>
      <td>24725</td>
      <td>134494</td>
      <td>22</td>
      <td>9.778517</td>
      <td>2.611232</td>
      <td>12.389748</td>
      <td>20.046954</td>
      <td>4.746681</td>
      <td>10.879019</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>node</td>
      <td>PXD004720_node</td>
      <td>26236</td>
      <td>9558</td>
      <td>35794</td>
      <td>19853</td>
      <td>9375</td>
      <td>29228</td>
      <td>18271</td>
      <td>...</td>
      <td>98731</td>
      <td>12726</td>
      <td>86005</td>
      <td>22</td>
      <td>8.866089</td>
      <td>3.229992</td>
      <td>12.096082</td>
      <td>18.569130</td>
      <td>5.865314</td>
      <td>10.956994</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>leaf-flag-mature</td>
      <td>PXD004720_leaf-flag-mature</td>
      <td>29869</td>
      <td>7584</td>
      <td>37453</td>
      <td>22443</td>
      <td>7439</td>
      <td>29882</td>
      <td>27629</td>
      <td>...</td>
      <td>144641</td>
      <td>19405</td>
      <td>125236</td>
      <td>22</td>
      <td>10.093811</td>
      <td>2.562907</td>
      <td>12.656718</td>
      <td>20.991638</td>
      <td>4.654087</td>
      <td>11.202165</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>lemma</td>
      <td>PXD004720_lemma</td>
      <td>29136</td>
      <td>8250</td>
      <td>37386</td>
      <td>21824</td>
      <td>8091</td>
      <td>29915</td>
      <td>27259</td>
      <td>...</td>
      <td>146562</td>
      <td>21700</td>
      <td>124862</td>
      <td>22</td>
      <td>9.846104</td>
      <td>2.787972</td>
      <td>12.634076</td>
      <td>20.412668</td>
      <td>5.062000</td>
      <td>11.214536</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>root-tip</td>
      <td>PXD004720_root-tip</td>
      <td>32368</td>
      <td>6969</td>
      <td>39337</td>
      <td>23693</td>
      <td>6815</td>
      <td>30508</td>
      <td>36423</td>
      <td>...</td>
      <td>191262</td>
      <td>34992</td>
      <td>156270</td>
      <td>22</td>
      <td>10.938313</td>
      <td>2.355076</td>
      <td>13.293389</td>
      <td>22.160802</td>
      <td>4.263692</td>
      <td>11.436840</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>spike-immature</td>
      <td>PXD004720_spike-immature</td>
      <td>32537</td>
      <td>7242</td>
      <td>39779</td>
      <td>23515</td>
      <td>7096</td>
      <td>30611</td>
      <td>33851</td>
      <td>...</td>
      <td>188025</td>
      <td>33123</td>
      <td>154902</td>
      <td>22</td>
      <td>10.995424</td>
      <td>2.447333</td>
      <td>13.442757</td>
      <td>21.994313</td>
      <td>4.439495</td>
      <td>11.475453</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>root-mature</td>
      <td>PXD004720_root-mature</td>
      <td>29545</td>
      <td>8999</td>
      <td>38544</td>
      <td>22134</td>
      <td>8818</td>
      <td>30952</td>
      <td>17366</td>
      <td>...</td>
      <td>96387</td>
      <td>10853</td>
      <td>85534</td>
      <td>22</td>
      <td>9.984320</td>
      <td>3.041086</td>
      <td>13.025406</td>
      <td>20.702621</td>
      <td>5.516836</td>
      <td>11.603287</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>grain-zadoks-75</td>
      <td>PXD004720_grain-zadoks-75</td>
      <td>32477</td>
      <td>8105</td>
      <td>40582</td>
      <td>24243</td>
      <td>7924</td>
      <td>32167</td>
      <td>24606</td>
      <td>...</td>
      <td>132081</td>
      <td>18607</td>
      <td>113474</td>
      <td>22</td>
      <td>10.975148</td>
      <td>2.738971</td>
      <td>13.714120</td>
      <td>22.675234</td>
      <td>4.957519</td>
      <td>12.058766</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>node_secretion</td>
      <td>PXD004720_node_secretion</td>
      <td>33365</td>
      <td>8404</td>
      <td>41769</td>
      <td>24936</td>
      <td>8230</td>
      <td>33166</td>
      <td>31835</td>
      <td>...</td>
      <td>168564</td>
      <td>22830</td>
      <td>145734</td>
      <td>22</td>
      <td>11.275235</td>
      <td>2.840014</td>
      <td>14.115250</td>
      <td>23.323419</td>
      <td>5.148963</td>
      <td>12.433271</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>radicle</td>
      <td>PXD004720_radicle</td>
      <td>34621</td>
      <td>7855</td>
      <td>42476</td>
      <td>25692</td>
      <td>7693</td>
      <td>33385</td>
      <td>36832</td>
      <td>...</td>
      <td>193938</td>
      <td>32434</td>
      <td>161504</td>
      <td>22</td>
      <td>11.699683</td>
      <td>2.654487</td>
      <td>14.354170</td>
      <td>24.030529</td>
      <td>4.812998</td>
      <td>12.515370</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>coleoptile</td>
      <td>PXD004720_coleoptile</td>
      <td>36197</td>
      <td>9622</td>
      <td>45819</td>
      <td>26797</td>
      <td>9411</td>
      <td>36208</td>
      <td>38002</td>
      <td>...</td>
      <td>203264</td>
      <td>31278</td>
      <td>171986</td>
      <td>22</td>
      <td>12.232270</td>
      <td>3.251620</td>
      <td>15.483891</td>
      <td>25.064070</td>
      <td>5.887836</td>
      <td>13.573656</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>grain-zadoks-71</td>
      <td>PXD004720_grain-zadoks-71</td>
      <td>36924</td>
      <td>9498</td>
      <td>46422</td>
      <td>26965</td>
      <td>9304</td>
      <td>36269</td>
      <td>33028</td>
      <td>...</td>
      <td>178814</td>
      <td>27602</td>
      <td>151212</td>
      <td>22</td>
      <td>12.477950</td>
      <td>3.209716</td>
      <td>15.687666</td>
      <td>25.221206</td>
      <td>5.820894</td>
      <td>13.596524</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>radicle</td>
      <td>PXD050500_radicle</td>
      <td>113924</td>
      <td>87339</td>
      <td>201263</td>
      <td>89823</td>
      <td>85356</td>
      <td>175179</td>
      <td>251809</td>
      <td>...</td>
      <td>1050178</td>
      <td>117686</td>
      <td>932492</td>
      <td>22</td>
      <td>38.499023</td>
      <td>29.514994</td>
      <td>68.014018</td>
      <td>84.014254</td>
      <td>53.401569</td>
      <td>65.671110</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>coleoptile</td>
      <td>PXD050500_coleoptile</td>
      <td>122443</td>
      <td>111301</td>
      <td>233744</td>
      <td>97341</td>
      <td>108801</td>
      <td>206142</td>
      <td>445454</td>
      <td>...</td>
      <td>1829196</td>
      <td>227461</td>
      <td>1601735</td>
      <td>22</td>
      <td>41.377900</td>
      <td>37.612617</td>
      <td>78.990518</td>
      <td>91.046074</td>
      <td>68.069545</td>
      <td>77.278521</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>node</td>
      <td>PXD050500_node</td>
      <td>123242</td>
      <td>113949</td>
      <td>237191</td>
      <td>98102</td>
      <td>111366</td>
      <td>209468</td>
      <td>449316</td>
      <td>...</td>
      <td>1864415</td>
      <td>234600</td>
      <td>1629815</td>
      <td>22</td>
      <td>41.647911</td>
      <td>38.507472</td>
      <td>80.155383</td>
      <td>91.757861</td>
      <td>69.674295</td>
      <td>78.525372</td>
    </tr>
  </tbody>
</table>
<p>32 rows × 22 columns</p>
</div>


# Step 17 — EDA: Tissue Overlap Using UpSet Plots

This exploratory analysis investigates the overlap of proteogenomic evidence across wheat tissues using UpSet plots.

Because the study includes a large number of tissues and datasets, traditional Venn diagrams become impractical. UpSet plots provide a scalable alternative for visualising shared and tissue-specific proteogenomic features.

---

## Input files

### Validated peptide genome projection tables from Step 11

```text
wheat_projection_translation_validated_sanity_checks_full_step11.csv
```

Only validated peptide rows were included.

### Filtering rule

```text
Sanity_check_status == "passed"
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
step17_upsetplot_tissue_overlap_proteins.png
```

### Peptide sequence overlap

```text
step17_upsetplot_tissue_overlap_peptides.png
```

### Gene model overlap

```text
step17_upsetplot_tissue_overlap_gene_models.png
```

---

## Output directory

```text
python_outputs/figures/
```

---

## Summary table

A Step 17 summary table was generated.

### Output file

```text
wheat_tissue_overlap_summary_step17.csv
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
```

    
    Loading fully validated rows from Step 11...
    Fully validated rows loaded for Step 17: 8,214,230
    


    
![png](output_35_1.png)
    


    Figure saved: python_outputs\figures\step17_upsetplot_tissue_overlap_validated_proteins.png
    


    
![png](output_35_3.png)
    


    Figure saved: python_outputs\figures\step17_upsetplot_tissue_overlap_validated_peptides.png
    


    
![png](output_35_5.png)
    


    Figure saved: python_outputs\figures\step17_upsetplot_tissue_overlap_validated_gene_models.png
    
    Step 17 summary saved: python_outputs\tables\wheat_tissue_overlap_validated_summary_step17.csv
    


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
      <th>Validated_BED_rows</th>
      <th>Unique_validated_proteins</th>
      <th>Unique_validated_peptides</th>
      <th>Unique_validated_gene_models</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>30</th>
      <td>PXD050500_node</td>
      <td>1864415</td>
      <td>237191</td>
      <td>587392</td>
      <td>209468</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD050500_coleoptile</td>
      <td>1829196</td>
      <td>233744</td>
      <td>574831</td>
      <td>206142</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD050500_radicle</td>
      <td>1050178</td>
      <td>201263</td>
      <td>328566</td>
      <td>175179</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720_grain-zadoks-71</td>
      <td>178814</td>
      <td>46422</td>
      <td>35806</td>
      <td>36269</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD004720_coleoptile</td>
      <td>203264</td>
      <td>45819</td>
      <td>40861</td>
      <td>36208</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720_radicle</td>
      <td>193938</td>
      <td>42476</td>
      <td>39487</td>
      <td>33385</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720_node_secretion</td>
      <td>168564</td>
      <td>41769</td>
      <td>34026</td>
      <td>33166</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720_grain-zadoks-75</td>
      <td>132081</td>
      <td>40582</td>
      <td>27293</td>
      <td>32167</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720_root-mature</td>
      <td>96387</td>
      <td>38544</td>
      <td>21125</td>
      <td>30952</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720_spike-immature</td>
      <td>188025</td>
      <td>39779</td>
      <td>36236</td>
      <td>30611</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720_root-tip</td>
      <td>191262</td>
      <td>39337</td>
      <td>38496</td>
      <td>30508</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720_lemma</td>
      <td>146562</td>
      <td>37386</td>
      <td>29653</td>
      <td>29915</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720_leaf-flag-mature</td>
      <td>144641</td>
      <td>37453</td>
      <td>29731</td>
      <td>29882</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720_node</td>
      <td>98731</td>
      <td>35794</td>
      <td>21280</td>
      <td>29228</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720_rachilla</td>
      <td>159219</td>
      <td>36663</td>
      <td>31008</td>
      <td>29020</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720_grain-zadoks-83</td>
      <td>112389</td>
      <td>36046</td>
      <td>23840</td>
      <td>28854</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD004720_anther</td>
      <td>163467</td>
      <td>36275</td>
      <td>33982</td>
      <td>28845</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720_glume</td>
      <td>144079</td>
      <td>35014</td>
      <td>28512</td>
      <td>28205</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720_grain-zadoks-70</td>
      <td>125355</td>
      <td>34929</td>
      <td>26037</td>
      <td>28080</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720_grain-zadoks-87</td>
      <td>111156</td>
      <td>34405</td>
      <td>24482</td>
      <td>27624</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720_leaf-flag-young</td>
      <td>119922</td>
      <td>32180</td>
      <td>23296</td>
      <td>25809</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720_pericarp</td>
      <td>130645</td>
      <td>32281</td>
      <td>28184</td>
      <td>25580</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720_root-secretion</td>
      <td>100085</td>
      <td>31657</td>
      <td>21111</td>
      <td>25126</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720_root-vasculature</td>
      <td>111315</td>
      <td>30323</td>
      <td>20728</td>
      <td>23512</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720_stem</td>
      <td>60181</td>
      <td>28948</td>
      <td>14177</td>
      <td>23218</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720_endosperm</td>
      <td>102289</td>
      <td>27099</td>
      <td>19953</td>
      <td>21529</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720_palea</td>
      <td>116285</td>
      <td>27295</td>
      <td>21623</td>
      <td>21503</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>45680</td>
      <td>25275</td>
      <td>11204</td>
      <td>20842</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720_pollen</td>
      <td>74334</td>
      <td>19731</td>
      <td>13446</td>
      <td>15866</td>
    </tr>
    <tr>
      <th>0</th>
      <td>MSV000090572_stored_grain</td>
      <td>29892</td>
      <td>17110</td>
      <td>9126</td>
      <td>14536</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD004720_boot</td>
      <td>13137</td>
      <td>9126</td>
      <td>3599</td>
      <td>7279</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720_embryo</td>
      <td>8742</td>
      <td>7110</td>
      <td>2815</td>
      <td>5749</td>
    </tr>
  </tbody>
</table>
</div>


# Step 18 — EDA: Distributions (histogram and box plot) of Peptide Support per Gene Model

This exploratory analysis examines how many unique peptide sequences support each detected wheat gene model.

The aim is to evaluate the strength of proteomics evidence at the gene model level and compare peptide support between high-confidence (HC) and low-confidence (LC) annotations.

---

## Input file

### Gene model summary table from Step 15

```text
wheat_gene_model_summary_step15.csv
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
step18_peptide_support_per_gene_model_histogram.png
```

This plot shows the distribution of unique peptide counts per gene model. A log-scaled x-axis was used because most gene models are expected to be supported by relatively few peptides, while a smaller number may be supported by many peptides.

### 2. HC vs LC boxplot

```text
step18_peptide_support_per_gene_model_HC_LC_boxplot.png
```

This plot compares peptide support between HC and LC gene models. The y-axis was log-scaled to improve visualisation of both low- and high-support gene models.

---

## Summary table

A Step 18 summary table was generated.

### Output file

```text
wheat_peptide_support_per_gene_model_summary_step18.csv
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
# Step 18 — EDA: distributions of peptide support per gene model
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

gene_summary_file = tables_dir / "wheat_gene_model_summary_step15.csv"

histogram_out = figures_dir / "step18_validated_peptide_support_per_gene_model_histogram.png"
boxplot_out = figures_dir / "step18_validated_peptide_support_per_gene_model_HC_LC_boxplot.png"
step18_summary_out = tables_dir / "wheat_validated_peptide_support_per_gene_model_summary_step18.csv"

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

print(f"Gene models with validated peptide support: {gene_summary[gene_col].nunique():,}")

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
step18_summary = (
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

step18_summary = step18_summary.merge(
    total_by_confidence,
    on=confidence_col,
    how="left"
)

step18_summary["Percent_within_confidence_class"] = (
    step18_summary["Gene_model_count"] /
    step18_summary["Total_gene_models_with_peptide_support"] *
    100
).round(4)

bin_order = ["1 peptide", "2–4 peptides", "5–9 peptides", "≥10 peptides"]
step18_summary["Peptide_support_bin"] = pd.Categorical(
    step18_summary["Peptide_support_bin"],
    categories=bin_order,
    ordered=True
)

step18_summary = step18_summary.sort_values(
    [confidence_col, "Peptide_support_bin"]
)

step18_summary.to_csv(step18_summary_out, index=False)

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

plt.xlabel("Unique validated peptides per gene model")
plt.ylabel("Number of gene models")
plt.title("Distribution of validated peptide support per wheat gene model")

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

plt.ylabel("Unique validated peptides per gene model")
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
print(f"Step 18 summary saved: {step18_summary_out}")
display(step18_summary)
```

    Gene models with validated peptide support: 243,564
    


    
![png](output_37_1.png)
    


    Histogram saved: python_outputs\figures\step18_validated_peptide_support_per_gene_model_histogram.png
    


    
![png](output_37_3.png)
    


    Boxplot saved: python_outputs\figures\step18_validated_peptide_support_per_gene_model_HC_LC_boxplot.png
    Step 18 summary saved: python_outputs\tables\wheat_validated_peptide_support_per_gene_model_summary_step18.csv
    


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
      <td>4130</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>104417</td>
      <td>3.9553</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HC</td>
      <td>2–4 peptides</td>
      <td>17259</td>
      <td>3.0</td>
      <td>3.037777</td>
      <td>4</td>
      <td>104417</td>
      <td>16.5289</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HC</td>
      <td>5–9 peptides</td>
      <td>26478</td>
      <td>7.0</td>
      <td>6.866720</td>
      <td>9</td>
      <td>104417</td>
      <td>25.3579</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HC</td>
      <td>≥10 peptides</td>
      <td>56550</td>
      <td>20.0</td>
      <td>26.247303</td>
      <td>318</td>
      <td>104417</td>
      <td>54.1578</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LC</td>
      <td>1 peptide</td>
      <td>24564</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1</td>
      <td>139147</td>
      <td>17.6533</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LC</td>
      <td>2–4 peptides</td>
      <td>59665</td>
      <td>3.0</td>
      <td>2.859784</td>
      <td>4</td>
      <td>139147</td>
      <td>42.8791</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LC</td>
      <td>5–9 peptides</td>
      <td>36992</td>
      <td>6.0</td>
      <td>6.479455</td>
      <td>9</td>
      <td>139147</td>
      <td>26.5848</td>
    </tr>
    <tr>
      <th>7</th>
      <td>LC</td>
      <td>≥10 peptides</td>
      <td>17926</td>
      <td>13.0</td>
      <td>16.557291</td>
      <td>217</td>
      <td>139147</td>
      <td>12.8828</td>
    </tr>
  </tbody>
</table>
</div>


# Step 19 — EDA: Scatterplot of Peptide Length and Probability by Annotation Confidence

This exploratory analysis compares peptide-level identification characteristics between high-confidence (HC) and low-confidence (LC) wheat gene model annotations.

A scatterplot was generated to visualise the relationship between peptide length and peptide identification probability.

---

## Input files

### Validated peptide genome projection tables from Step 11

```text
wheat_projection_translation_validated_sanity_checks_full_step11.csv
```

Only validated peptide rows were included.

### Filtering rule

```text
Sanity_check_status == "passed"
```

---

## Plot design

| Visual element | Variable |
|---|---|
| x-axis | Peptide length in amino acids |
| y-axis | Peptide probability |
| Point colour | Annotation confidence: HC or LC |

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
step19_peptide_length_probability_HC_LC_scatter.png
```

### Summary table

```text
wheat_peptide_length_probability_summary_step19.csv
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
# Step 19 — EDA: Scatterplot of peptide length and probability by HC/LC
# Fully validated rows only
# Translation-validated + sanity-check-passed projections
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
figures_dir = Path("python_outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

# Step 11 output: translation-validated rows with sanity-check status
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

step19_summary_out = tables_dir / "wheat_validated_peptide_length_probability_summary_step19.csv"
scatter_out = figures_dir / "step19_validated_peptide_length_probability_HC_LC_scatter.png"

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

    If multiple charge states are reported, the maximum observed charge is used.
    """
    if pd.isna(value):
        return pd.NA

    values = re.findall(r"\d+", str(value))

    if len(values) == 0:
        return pd.NA

    return max(int(v) for v in values)

# -----------------------------
# 4. Load a random sample from fully validated rows
# -----------------------------
print("\nSampling fully validated rows from Step 11...")

header = pd.read_csv(sanity_file, nrows=0)

confidence_col = "Annotation_confidence"

needed_cols = [
    "Peptide",
    "Peptide_length_AA",
    "Probability",
    confidence_col,
    "Sanity_check_status"
]

required_core_cols = [
    "Peptide",
    "Probability",
    confidence_col,
    "Sanity_check_status"
]

missing_core_cols = [
    col for col in required_core_cols
    if col not in header.columns
]

if missing_core_cols:
    raise KeyError(
        f"Missing required column(s) in Step 11 sanity-check table: {missing_core_cols}"
    )

available_cols = [col for col in needed_cols if col in header.columns]

all_sampled_tables = []

max_points_total = 10_000
chunksize = 100_000
sample_per_chunk = 150

for chunk_i, chunk in enumerate(
    pd.read_csv(
        sanity_file,
        usecols=available_cols,
        chunksize=chunksize,
        low_memory=False
    ),
    start=1
):

    chunk = chunk[
        (chunk["Sanity_check_status"].astype(str) == "passed") &
        (chunk[confidence_col].astype(str).str.upper().isin(["HC", "LC"]))
    ].copy()

    if chunk.empty:
        continue

    # Standardise confidence labels
    chunk[confidence_col] = chunk[confidence_col].astype(str).str.upper()

    n_sample = min(sample_per_chunk, len(chunk))

    all_sampled_tables.append(
        chunk.sample(
            n=n_sample,
            random_state=42 + chunk_i
        )
    )

if len(all_sampled_tables) == 0:
    raise ValueError(
        "No fully validated HC/LC rows were available for Step 19."
    )

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
if "Peptide_length_AA" not in plot_data.columns:
    plot_data["Peptide_length_AA"] = plot_data["Peptide"].astype(str).str.len()

plot_data["Peptide_length_AA"] = pd.to_numeric(
    plot_data["Peptide_length_AA"],
    errors="coerce"
)

plot_data["Probability"] = pd.to_numeric(
    plot_data["Probability"],
    errors="coerce"
)

plot_data = plot_data.dropna(
    subset=["Peptide_length_AA", "Probability"]
).copy()

# Charges were not retained in the validated Step 11 table.
# Use a fixed dot size so the plot remains based only on fully validated rows.
plot_data["Dot_size"] = 30

# -----------------------------
# 6. Summary table
# -----------------------------
# Randomly sampled, memory-friendly dataset
step19_summary = (
    plot_data
    .groupby(confidence_col, dropna=False)
    .agg(
        Sampled_validated_peptide_rows=("Peptide", "size"),
        Unique_validated_peptides=("Peptide", "nunique"),
        Mean_peptide_length=("Peptide_length_AA", "mean"),
        Median_peptide_length=("Peptide_length_AA", "median"),
        Mean_probability=("Probability", "mean"),
        Median_probability=("Probability", "median")
    )
    .reset_index()
)

step19_summary.to_csv(step19_summary_out, index=False)

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
plt.title("Validated peptide length and probability by annotation confidence")

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
print(f"Step 19 summary saved: {step19_summary_out}")

display(step19_summary)
```

    
    Sampling fully validated rows from Step 11...
    Rows used for scatterplot: 10,000
    


    
![png](output_39_1.png)
    


    Scatterplot saved: python_outputs\figures\step19_validated_peptide_length_probability_HC_LC_scatter.png
    Step 19 summary saved: python_outputs\tables\wheat_validated_peptide_length_probability_summary_step19.csv
    


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
      <th>Sampled_validated_peptide_rows</th>
      <th>Unique_validated_peptides</th>
      <th>Mean_peptide_length</th>
      <th>Median_peptide_length</th>
      <th>Mean_probability</th>
      <th>Median_probability</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>8538</td>
      <td>8050</td>
      <td>13.522019</td>
      <td>12.0</td>
      <td>0.847330</td>
      <td>0.9983</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LC</td>
      <td>1462</td>
      <td>1405</td>
      <td>12.855677</td>
      <td>11.0</td>
      <td>0.558524</td>
      <td>0.5663</td>
    </tr>
  </tbody>
</table>
</div>


# Step 20 — EDA: Scatterplot of Protein Length versus Peptide Support

This exploratory analysis investigates the relationship between protein length and peptide support across wheat protein isoforms.

The aim is to determine whether longer proteins tend to accumulate greater peptide evidence and whether this relationship differs between high-confidence (HC) and low-confidence (LC) annotations.

---

## Input files

### Protein isoform summary table from Step 15

```text
wheat_protein_isoform_summary_step15.csv
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
step20_protein_length_vs_peptide_support_scatter.png
```

---

## Summary table

A Step 20 summary table was generated.

### Output file

```text
wheat_protein_length_vs_peptide_support_summary_step20.csv
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
```

    Protein isoforms plotted: 272,298
    


    
![png](output_41_1.png)
    


    Scatterplot saved: python_outputs\figures\step20_validated_protein_length_vs_peptide_support_scatter_regression.png
    Step 20 summary saved: python_outputs\tables\wheat_validated_protein_length_vs_peptide_support_summary_step20.csv
    


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
      <th>Mean_unique_validated_peptides</th>
      <th>Median_unique_validated_peptides</th>
      <th>Max_unique_validated_peptides</th>
      <th>Linear_regression_n</th>
      <th>Linear_regression_slope</th>
      <th>Linear_regression_intercept</th>
      <th>Linear_regression_R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>130006</td>
      <td>450.3988</td>
      <td>383.0</td>
      <td>5366.0</td>
      <td>18.6526</td>
      <td>12.0</td>
      <td>318</td>
      <td>130006</td>
      <td>0.0429</td>
      <td>-0.6836</td>
      <td>0.4559</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LC</td>
      <td>142292</td>
      <td>213.3316</td>
      <td>158.0</td>
      <td>4979.0</td>
      <td>5.2629</td>
      <td>4.0</td>
      <td>217</td>
      <td>142292</td>
      <td>0.0223</td>
      <td>0.5120</td>
      <td>0.4156</td>
    </tr>
  </tbody>
</table>
</div>


# Step 21 — EDA: Violin plot of chromosomal Distribution of Peptide Genomic Start Positions

This exploratory analysis recreates the chromosome-level violin plot used in the 2024 wheat proteogenomics study, updated with the expanded 2026 multi-tissue dataset.

The aim is to visualise where peptide evidence is distributed along each wheat chromosome, including annotation-projected HC and LC peptides.

---

## Input files

### Non-redundant annotation-projected peptide table from Step 13

```text
wheat_all_tissues_nonredundant_validated_peptides_step13.csv
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
step21_violinplot_peptide_genomic_start_by_chromosome.png
```

### Summary table

```text
wheat_peptide_genomic_start_by_chromosome_summary_step21.csv
```

---

## Purpose

This visualisation provides a genome-wide overview of peptide evidence distribution and enables comparison of:

- HC annotation-supported peptide evidence,
- LC annotation-supported peptide evidence.

It is designed to support direct comparison with the chromosome-level proteogenomic distribution figure from the 2024 wheat proteogenomics resource paper.


```python
# ============================================================
# Step 21 — EDA: Violin plot of genomic peptide positions by chromosome
# All-tissue combined, non-redundant, fully validated projections only
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
# all-tissue combined, non-redundant, translation-validated + sanity-passed peptide projections
projection_combined_file = tables_dir / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv"

# Protein-to-gene mapping table used to recover HC/LC annotation confidence if needed
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

figure_out = figures_dir / "step21_violinplot_nonredundant_validated_peptide_genomic_start_by_chromosome.png"
summary_out = tables_dir / "wheat_nonredundant_validated_peptide_genomic_start_by_chromosome_summary_step21.csv"

if not projection_combined_file.exists():
    raise FileNotFoundError(
        f"Step 13 combined non-redundant validated peptide table not found:\n"
        f"{projection_combined_file}\n\n"
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
    "HC": "#3F007E",
    "LC": "#FF3399"
}

# -----------------------------
# 3. Settings
# -----------------------------
chrom_col = "Chromosome"
start_col = "BED_start_0based"
protein_col = "ProteinID"
confidence_col = "Annotation_confidence"

max_points_per_group = 50_000
chunksize = 100_000

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

# -----------------------------
# 5. Load ProteinID → Annotation_confidence lookup
# -----------------------------
protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    usecols=lambda col: col in [protein_col, confidence_col],
    low_memory=False
)

if protein_col not in protein_mapping.columns:
    raise KeyError(f"Missing '{protein_col}' in protein-gene mapping table.")

if confidence_col not in protein_mapping.columns:
    raise KeyError(f"Missing '{confidence_col}' in protein-gene mapping table.")

protein_conf_lookup = (
    protein_mapping
    .dropna(subset=[protein_col, confidence_col])
    .drop_duplicates(subset=[protein_col])
    .copy()
)

protein_conf_lookup[confidence_col] = (
    protein_conf_lookup[confidence_col]
    .astype(str)
    .str.upper()
)

# -----------------------------
# 6. Inspect combined non-redundant table columns
# -----------------------------
header = pd.read_csv(projection_combined_file, nrows=0)

required_cols = [
    chrom_col,
    start_col,
    protein_col
]

missing_cols = [
    col for col in required_cols
    if col not in header.columns
]

if missing_cols:
    raise KeyError(
        f"Missing required column(s) in Step 13 combined table: {missing_cols}"
    )

# If Annotation_confidence is already present in the Step 13 table, use it.
# Otherwise merge it from the protein-gene mapping table.
combined_has_confidence = confidence_col in header.columns

projected_needed_cols = [
    chrom_col,
    start_col,
    protein_col
]

if combined_has_confidence:
    projected_needed_cols.append(confidence_col)

# Keep extra useful columns if present
optional_cols = [
    "Peptide",
    "Peptide_label",
    "Gene_label",
    "BED_block_count",
    "Tissue_count",
    "Observation_count"
]

for col in optional_cols:
    if col in header.columns:
        projected_needed_cols.append(col)

projected_needed_cols = list(dict.fromkeys(projected_needed_cols))

print("Step 21 input:")
print(projection_combined_file)
print(f"Using all-tissue non-redundant validated rows from Step 13.")
print(f"Annotation confidence already in Step 13 table: {combined_has_confidence}")

# -----------------------------
# 7. Load combined validated non-redundant data in chunks
# -----------------------------
summary_chunks = []
sample_chunks = []

total_rows_read = 0
total_rows_retained = 0

for chunk_i, chunk in enumerate(
    pd.read_csv(
        projection_combined_file,
        usecols=lambda col: col in projected_needed_cols,
        chunksize=chunksize,
        low_memory=False
    ),
    start=1
):

    total_rows_read += len(chunk)

    # Add HC/LC annotation confidence if not already present
    if confidence_col not in chunk.columns:

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
    ).copy()

    chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

    chunk = chunk[
        chunk["Chromosome"].isin(chrom_order)
    ].copy()

    if chunk.empty:
        continue

    total_rows_retained += len(chunk)

    # Convert to Mb for easier plotting and interpretation
    chunk["Genomic_start_Mb"] = chunk["Genomic_start"] / 1_000_000

    summary_chunks.append(
        chunk[["Chromosome", "Genomic_start", "Genomic_start_Mb", "Evidence"]]
    )

    # Sample lightly from each chunk for plotting
    if len(chunk) > 3_000:
        chunk_sample = chunk.sample(
            n=3_000,
            random_state=42 + chunk_i
        )
    else:
        chunk_sample = chunk

    sample_chunks.append(
        chunk_sample[["Chromosome", "Genomic_start_Mb", "Evidence"]]
    )

    print(
        f"Chunk {chunk_i}: read {len(chunk):,} retained rows | "
        f"cumulative retained {total_rows_retained:,}"
    )

if not summary_chunks:
    raise ValueError(
        "No valid HC/LC rows were loaded from the Step 13 combined table."
    )

projected_summary_data = pd.concat(summary_chunks, ignore_index=True)
projected_plot_sample = pd.concat(sample_chunks, ignore_index=True)

print(f"\nRows read from Step 13 combined table: {total_rows_read:,}")
print(f"Rows retained for summary: {len(projected_summary_data):,}")
print(f"Sampled rows before group cap: {len(projected_plot_sample):,}")

# -----------------------------
# 8. Build summary table from full non-redundant validated data
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
        Nonredundant_validated_rows=("Genomic_start", "size"),
        Median_genomic_start_bp=("Genomic_start", "median"),
        Mean_genomic_start_bp=("Genomic_start", "mean"),
        Min_genomic_start_bp=("Genomic_start", "min"),
        Max_genomic_start_bp=("Genomic_start", "max"),
        Median_genomic_start_Mb=("Genomic_start_Mb", "median"),
        Mean_genomic_start_Mb=("Genomic_start_Mb", "mean"),
        Min_genomic_start_Mb=("Genomic_start_Mb", "min"),
        Max_genomic_start_Mb=("Genomic_start_Mb", "max")
    )
    .reset_index()
)

summary.to_csv(summary_out, index=False)

# Free memory before plotting
del projected_summary_data
del summary_data
del summary_chunks

# -----------------------------
# 9. Build plot sample and cap per chromosome/evidence group
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
        "Check chromosome names in the input table."
    )

plot_sample = pd.concat(sampled_groups, ignore_index=True)

print(f"Rows used for violin plot: {len(plot_sample):,}")

# -----------------------------
# 10. Violin plot
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
            "Genomic_start_Mb"
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
        body.set_alpha(0.85)

    violin["cmedians"].set_color("white")
    violin["cmedians"].set_linewidth(1.2)

# -----------------------------
# 11. Plot formatting
# -----------------------------
ax.set_xticks(list(positions))

ax.set_xticklabels(
    chrom_order,
    rotation=45,
    ha="right",
    fontsize=12
)

ax.tick_params(
    axis="y",
    labelsize=12
)

ax.set_xlabel(
    "Chromosome",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

ax.set_ylabel(
    "Genomic start position (Mb)",
    fontsize=16,
    fontweight="bold",
    labelpad=10
)

ax.set_title(
    "Genomic distribution of non-redundant validated HC and LC peptide evidence by chromosome",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.grid(axis="y", linestyle="--", alpha=0.3)

# Manual legend
legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="o",
        color="w",
        label=evidence,
        markerfacecolor=brand_colours[evidence],
        markeredgecolor="black",
        markersize=14
    )
    for evidence in ["HC", "LC"]
]

legend = ax.legend(
    handles=legend_handles,
    title="Confidence",
    title_fontsize=12,
    fontsize=14,
    loc="upper right",
    frameon=True
)

legend.get_title().set_fontweight("bold")
legend.get_frame().set_linewidth(1.5)

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

    Step 21 input:
    python_outputs\tables\wheat_all_tissues_nonredundant_validated_peptides_step13.csv
    Using all-tissue non-redundant validated rows from Step 13.
    Annotation confidence already in Step 13 table: False
    Chunk 1: read 100,000 retained rows | cumulative retained 100,000
    Chunk 2: read 100,000 retained rows | cumulative retained 200,000
    Chunk 3: read 100,000 retained rows | cumulative retained 300,000
    Chunk 4: read 100,000 retained rows | cumulative retained 400,000
    Chunk 5: read 100,000 retained rows | cumulative retained 500,000
    Chunk 6: read 100,000 retained rows | cumulative retained 600,000
    Chunk 7: read 100,000 retained rows | cumulative retained 700,000
    Chunk 8: read 100,000 retained rows | cumulative retained 800,000
    Chunk 9: read 100,000 retained rows | cumulative retained 900,000
    Chunk 10: read 100,000 retained rows | cumulative retained 1,000,000
    Chunk 11: read 100,000 retained rows | cumulative retained 1,100,000
    Chunk 12: read 100,000 retained rows | cumulative retained 1,200,000
    Chunk 13: read 100,000 retained rows | cumulative retained 1,300,000
    Chunk 14: read 100,000 retained rows | cumulative retained 1,400,000
    Chunk 15: read 100,000 retained rows | cumulative retained 1,500,000
    Chunk 16: read 100,000 retained rows | cumulative retained 1,600,000
    Chunk 17: read 100,000 retained rows | cumulative retained 1,700,000
    Chunk 18: read 100,000 retained rows | cumulative retained 1,800,000
    Chunk 19: read 100,000 retained rows | cumulative retained 1,900,000
    Chunk 20: read 100,000 retained rows | cumulative retained 2,000,000
    Chunk 21: read 100,000 retained rows | cumulative retained 2,100,000
    Chunk 22: read 100,000 retained rows | cumulative retained 2,200,000
    Chunk 23: read 100,000 retained rows | cumulative retained 2,300,000
    Chunk 24: read 100,000 retained rows | cumulative retained 2,400,000
    Chunk 25: read 100,000 retained rows | cumulative retained 2,500,000
    Chunk 26: read 100,000 retained rows | cumulative retained 2,600,000
    Chunk 27: read 100,000 retained rows | cumulative retained 2,700,000
    Chunk 28: read 100,000 retained rows | cumulative retained 2,800,000
    Chunk 29: read 100,000 retained rows | cumulative retained 2,900,000
    Chunk 30: read 100,000 retained rows | cumulative retained 3,000,000
    Chunk 31: read 100,000 retained rows | cumulative retained 3,100,000
    Chunk 32: read 73,811 retained rows | cumulative retained 3,173,811
    
    Rows read from Step 13 combined table: 3,173,811
    Rows retained for summary: 3,173,811
    Sampled rows before group cap: 96,000
    Rows used for violin plot: 96,000
    


    
![png](output_43_1.png)
    


    Figure saved: python_outputs\figures\step21_violinplot_nonredundant_validated_peptide_genomic_start_by_chromosome.png
    Summary saved: python_outputs\tables\wheat_nonredundant_validated_peptide_genomic_start_by_chromosome_summary_step21.csv
    


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
      <th>Nonredundant_validated_rows</th>
      <th>Median_genomic_start_bp</th>
      <th>Mean_genomic_start_bp</th>
      <th>Min_genomic_start_bp</th>
      <th>Max_genomic_start_bp</th>
      <th>Median_genomic_start_Mb</th>
      <th>Mean_genomic_start_Mb</th>
      <th>Min_genomic_start_Mb</th>
      <th>Max_genomic_start_Mb</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Chr1A</td>
      <td>HC</td>
      <td>102754</td>
      <td>378522004.0</td>
      <td>3.412533e+08</td>
      <td>58543</td>
      <td>598561110</td>
      <td>378.522004</td>
      <td>341.253344</td>
      <td>0.058543</td>
      <td>598.561110</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Chr1A</td>
      <td>LC</td>
      <td>31211</td>
      <td>370878822.0</td>
      <td>3.332435e+08</td>
      <td>41201</td>
      <td>598363879</td>
      <td>370.878822</td>
      <td>333.243481</td>
      <td>0.041201</td>
      <td>598.363879</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Chr1B</td>
      <td>HC</td>
      <td>109319</td>
      <td>416741381.0</td>
      <td>3.837051e+08</td>
      <td>168112</td>
      <td>700379123</td>
      <td>416.741381</td>
      <td>383.705077</td>
      <td>0.168112</td>
      <td>700.379123</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Chr1B</td>
      <td>LC</td>
      <td>36930</td>
      <td>370131610.0</td>
      <td>3.626846e+08</td>
      <td>520312</td>
      <td>700376310</td>
      <td>370.131610</td>
      <td>362.684551</td>
      <td>0.520312</td>
      <td>700.376310</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Chr1D</td>
      <td>HC</td>
      <td>106363</td>
      <td>303328497.0</td>
      <td>2.776298e+08</td>
      <td>20705</td>
      <td>498609718</td>
      <td>303.328497</td>
      <td>277.629766</td>
      <td>0.020705</td>
      <td>498.609718</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Chr1D</td>
      <td>LC</td>
      <td>28367</td>
      <td>268219882.0</td>
      <td>2.673002e+08</td>
      <td>20687</td>
      <td>498498248</td>
      <td>268.219882</td>
      <td>267.300229</td>
      <td>0.020687</td>
      <td>498.498248</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Chr2A</td>
      <td>HC</td>
      <td>130347</td>
      <td>501198336.0</td>
      <td>4.236964e+08</td>
      <td>251216</td>
      <td>787195194</td>
      <td>501.198336</td>
      <td>423.696430</td>
      <td>0.251216</td>
      <td>787.195194</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Chr2A</td>
      <td>LC</td>
      <td>37449</td>
      <td>426674296.0</td>
      <td>4.115439e+08</td>
      <td>249001</td>
      <td>787082048</td>
      <td>426.674296</td>
      <td>411.543887</td>
      <td>0.249001</td>
      <td>787.082048</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Chr2B</td>
      <td>HC</td>
      <td>135074</td>
      <td>444572919.0</td>
      <td>4.146079e+08</td>
      <td>29396</td>
      <td>812720911</td>
      <td>444.572919</td>
      <td>414.607942</td>
      <td>0.029396</td>
      <td>812.720911</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Chr2B</td>
      <td>LC</td>
      <td>44983</td>
      <td>418847767.0</td>
      <td>4.151801e+08</td>
      <td>113609</td>
      <td>812724460</td>
      <td>418.847767</td>
      <td>415.180095</td>
      <td>0.113609</td>
      <td>812.724460</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Chr2D</td>
      <td>HC</td>
      <td>133371</td>
      <td>367806526.0</td>
      <td>3.370559e+08</td>
      <td>81486</td>
      <td>656399532</td>
      <td>367.806526</td>
      <td>337.055877</td>
      <td>0.081486</td>
      <td>656.399532</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Chr2D</td>
      <td>LC</td>
      <td>36389</td>
      <td>372169489.0</td>
      <td>3.473342e+08</td>
      <td>307945</td>
      <td>656397474</td>
      <td>372.169489</td>
      <td>347.334205</td>
      <td>0.307945</td>
      <td>656.397474</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Chr3A</td>
      <td>HC</td>
      <td>121339</td>
      <td>478300580.0</td>
      <td>4.056057e+08</td>
      <td>26772</td>
      <td>754027813</td>
      <td>478.300580</td>
      <td>405.605729</td>
      <td>0.026772</td>
      <td>754.027813</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Chr3A</td>
      <td>LC</td>
      <td>34769</td>
      <td>457330025.0</td>
      <td>4.049209e+08</td>
      <td>109656</td>
      <td>754050779</td>
      <td>457.330025</td>
      <td>404.920906</td>
      <td>0.109656</td>
      <td>754.050779</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Chr3B</td>
      <td>HC</td>
      <td>129973</td>
      <td>479411726.0</td>
      <td>4.405879e+08</td>
      <td>74006</td>
      <td>851873079</td>
      <td>479.411726</td>
      <td>440.587930</td>
      <td>0.074006</td>
      <td>851.873079</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Chr3B</td>
      <td>LC</td>
      <td>44257</td>
      <td>481015226.0</td>
      <td>4.538141e+08</td>
      <td>66880</td>
      <td>851822590</td>
      <td>481.015226</td>
      <td>453.814137</td>
      <td>0.066880</td>
      <td>851.822590</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Chr3D</td>
      <td>HC</td>
      <td>128617</td>
      <td>361377114.0</td>
      <td>3.228180e+08</td>
      <td>110201</td>
      <td>619490011</td>
      <td>361.377114</td>
      <td>322.818018</td>
      <td>0.110201</td>
      <td>619.490011</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Chr3D</td>
      <td>LC</td>
      <td>30483</td>
      <td>338270039.0</td>
      <td>3.215608e+08</td>
      <td>121439</td>
      <td>619441473</td>
      <td>338.270039</td>
      <td>321.560766</td>
      <td>0.121439</td>
      <td>619.441473</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Chr4A</td>
      <td>HC</td>
      <td>114345</td>
      <td>472806758.0</td>
      <td>3.998533e+08</td>
      <td>80753</td>
      <td>754178416</td>
      <td>472.806758</td>
      <td>399.853288</td>
      <td>0.080753</td>
      <td>754.178416</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Chr4A</td>
      <td>LC</td>
      <td>36022</td>
      <td>552511504.5</td>
      <td>4.663150e+08</td>
      <td>189937</td>
      <td>754141599</td>
      <td>552.511505</td>
      <td>466.314989</td>
      <td>0.189937</td>
      <td>754.141599</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Chr4B</td>
      <td>HC</td>
      <td>100161</td>
      <td>395929656.0</td>
      <td>3.453792e+08</td>
      <td>244</td>
      <td>673727718</td>
      <td>395.929656</td>
      <td>345.379207</td>
      <td>0.000244</td>
      <td>673.727718</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Chr4B</td>
      <td>LC</td>
      <td>30139</td>
      <td>366038669.0</td>
      <td>3.507162e+08</td>
      <td>690282</td>
      <td>673722692</td>
      <td>366.038669</td>
      <td>350.716246</td>
      <td>0.690282</td>
      <td>673.722692</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Chr4D</td>
      <td>HC</td>
      <td>97772</td>
      <td>302947272.0</td>
      <td>2.594663e+08</td>
      <td>410358</td>
      <td>514856857</td>
      <td>302.947272</td>
      <td>259.466325</td>
      <td>0.410358</td>
      <td>514.856857</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Chr4D</td>
      <td>LC</td>
      <td>23508</td>
      <td>278453690.5</td>
      <td>2.662943e+08</td>
      <td>464134</td>
      <td>512646336</td>
      <td>278.453690</td>
      <td>266.294279</td>
      <td>0.464134</td>
      <td>512.646336</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Chr5A</td>
      <td>HC</td>
      <td>119968</td>
      <td>464465905.5</td>
      <td>4.172580e+08</td>
      <td>13924</td>
      <td>713330062</td>
      <td>464.465905</td>
      <td>417.258013</td>
      <td>0.013924</td>
      <td>713.330062</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Chr5A</td>
      <td>LC</td>
      <td>36379</td>
      <td>473918962.0</td>
      <td>4.095749e+08</td>
      <td>320159</td>
      <td>713172935</td>
      <td>473.918962</td>
      <td>409.574925</td>
      <td>0.320159</td>
      <td>713.172935</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Chr5B</td>
      <td>HC</td>
      <td>127628</td>
      <td>444708895.0</td>
      <td>4.073457e+08</td>
      <td>16318</td>
      <td>714774033</td>
      <td>444.708895</td>
      <td>407.345684</td>
      <td>0.016318</td>
      <td>714.774033</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Chr5B</td>
      <td>LC</td>
      <td>38289</td>
      <td>430100254.0</td>
      <td>3.920927e+08</td>
      <td>6650</td>
      <td>714795420</td>
      <td>430.100254</td>
      <td>392.092676</td>
      <td>0.006650</td>
      <td>714.795420</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Chr5D</td>
      <td>HC</td>
      <td>128113</td>
      <td>370145315.0</td>
      <td>3.319880e+08</td>
      <td>297066</td>
      <td>569875777</td>
      <td>370.145315</td>
      <td>331.987980</td>
      <td>0.297066</td>
      <td>569.875777</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Chr5D</td>
      <td>LC</td>
      <td>32868</td>
      <td>371195320.5</td>
      <td>3.247128e+08</td>
      <td>291193</td>
      <td>569892303</td>
      <td>371.195320</td>
      <td>324.712839</td>
      <td>0.291193</td>
      <td>569.892303</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Chr6A</td>
      <td>HC</td>
      <td>92529</td>
      <td>405490644.0</td>
      <td>3.354241e+08</td>
      <td>118076</td>
      <td>622585150</td>
      <td>405.490644</td>
      <td>335.424052</td>
      <td>0.118076</td>
      <td>622.585150</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Chr6A</td>
      <td>LC</td>
      <td>29976</td>
      <td>298986599.5</td>
      <td>3.038285e+08</td>
      <td>4145</td>
      <td>622591126</td>
      <td>298.986600</td>
      <td>303.828545</td>
      <td>0.004145</td>
      <td>622.591126</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Chr6B</td>
      <td>HC</td>
      <td>101052</td>
      <td>442599520.0</td>
      <td>3.881085e+08</td>
      <td>4898</td>
      <td>731066437</td>
      <td>442.599520</td>
      <td>388.108530</td>
      <td>0.004898</td>
      <td>731.066437</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Chr6B</td>
      <td>LC</td>
      <td>39067</td>
      <td>386587563.0</td>
      <td>3.770742e+08</td>
      <td>5675</td>
      <td>730950773</td>
      <td>386.587563</td>
      <td>377.074174</td>
      <td>0.005675</td>
      <td>730.950773</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Chr6D</td>
      <td>HC</td>
      <td>91601</td>
      <td>313069947.0</td>
      <td>2.723278e+08</td>
      <td>43504</td>
      <td>495304993</td>
      <td>313.069947</td>
      <td>272.327799</td>
      <td>0.043504</td>
      <td>495.304993</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Chr6D</td>
      <td>LC</td>
      <td>24658</td>
      <td>246942957.5</td>
      <td>2.525414e+08</td>
      <td>27358</td>
      <td>495205351</td>
      <td>246.942958</td>
      <td>252.541357</td>
      <td>0.027358</td>
      <td>495.205351</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Chr7A</td>
      <td>HC</td>
      <td>114156</td>
      <td>320364019.5</td>
      <td>3.544244e+08</td>
      <td>237590</td>
      <td>744483725</td>
      <td>320.364019</td>
      <td>354.424447</td>
      <td>0.237590</td>
      <td>744.483725</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Chr7A</td>
      <td>LC</td>
      <td>38103</td>
      <td>365412944.0</td>
      <td>3.691389e+08</td>
      <td>122054</td>
      <td>744312979</td>
      <td>365.412944</td>
      <td>369.138899</td>
      <td>0.122054</td>
      <td>744.312979</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Chr7B</td>
      <td>HC</td>
      <td>108058</td>
      <td>392793686.0</td>
      <td>3.822149e+08</td>
      <td>33340</td>
      <td>764068236</td>
      <td>392.793686</td>
      <td>382.214876</td>
      <td>0.033340</td>
      <td>764.068236</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Chr7B</td>
      <td>LC</td>
      <td>39929</td>
      <td>438572809.0</td>
      <td>4.101249e+08</td>
      <td>56572</td>
      <td>764067061</td>
      <td>438.572809</td>
      <td>410.124934</td>
      <td>0.056572</td>
      <td>764.067061</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Chr7D</td>
      <td>HC</td>
      <td>116715</td>
      <td>287389395.0</td>
      <td>3.124898e+08</td>
      <td>208449</td>
      <td>642831821</td>
      <td>287.389395</td>
      <td>312.489757</td>
      <td>0.208449</td>
      <td>642.831821</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Chr7D</td>
      <td>LC</td>
      <td>35872</td>
      <td>300215071.5</td>
      <td>3.119092e+08</td>
      <td>173586</td>
      <td>642831014</td>
      <td>300.215072</td>
      <td>311.909188</td>
      <td>0.173586</td>
      <td>642.831014</td>
    </tr>
    <tr>
      <th>42</th>
      <td>ChrUnknown</td>
      <td>HC</td>
      <td>15693</td>
      <td>134767961.0</td>
      <td>1.324406e+08</td>
      <td>7635176</td>
      <td>347551051</td>
      <td>134.767961</td>
      <td>132.440645</td>
      <td>7.635176</td>
      <td>347.551051</td>
    </tr>
    <tr>
      <th>43</th>
      <td>ChrUnknown</td>
      <td>LC</td>
      <td>19215</td>
      <td>215114082.0</td>
      <td>1.893907e+08</td>
      <td>806019</td>
      <td>351238213</td>
      <td>215.114082</td>
      <td>189.390689</td>
      <td>0.806019</td>
      <td>351.238213</td>
    </tr>
  </tbody>
</table>
</div>


# Step 22 — EDA: Circular Tissue-Level Peptide Genome Map

This exploratory analysis generates a Circos-style circular genome map showing projected peptide evidence across wheat chromosomes and tissues.

The figure is inspired by the circular peptide distribution plot generated in the 2024 wheat proteogenomics study, but is produced here directly in Python using `pycirclize`.

---

## Input files

### Validated annotation-projected peptide table from Step 11

```text
"wheat_projection_translation_validated_sanity_checks_full_step11.csv
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
step22_circos_tissue_peptide_tracks.png
```

### Summary table

```text
wheat_circos_tissue_peptide_summary_step22.csv
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
# Step 22 — EDA: Circular plot of tissue-level validated peptide genome map
# Fully validated rows only
# Translation-validated + sanity-check-passed mapped peptide projections
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

gff3_features_file = tables_dir / "wheat_gff3_parsed_features_HC_LC.csv"

# Step 11 output: translation-validated rows with sanity-check status
sanity_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_full_step11.csv"

figure_out = figures_dir / "step22_circos_tissue_validated_peptide_tracks.png"
summary_out = tables_dir / "wheat_circos_tissue_validated_peptide_summary_step22.csv"

if not sanity_file.exists():
    raise FileNotFoundError(
        f"Step 11 sanity-check file not found:\n{sanity_file}\n\n"
        "Please run Step 11 first."
    )

if not gff3_features_file.exists():
    raise FileNotFoundError(
        f"GFF3 parsed features file not found:\n{gff3_features_file}"
    )

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
    "Chr7A", "Chr7B", "Chr7D",
    "ChrUnknown"
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
    return (
        str(value)
        .replace("-", "_")
        .replace(" ", "_")
        .replace("/", "_")
    )


def source_rank(source):
    """
    Track order from innermost to outermost.

    Desired visual order:
    1. MSV... innermost
    2. PXD004720 / other PXD intermediate
    3. PXD050500 outermost
    """

    source = str(source)

    if source.startswith("MSV"):
        return 0

    if source == "PXD004720":
        return 1

    if source == "PXD050500":
        return 2

    if source.startswith("PXD"):
        return 3

    return 99


def source_tissue_sort_key(source_tissue):
    """
    Sort Source_Tissue labels so that MSV tracks are innermost and
    PXD050500 tracks are outermost.
    """

    source = str(source_tissue).split("_", 1)[0]
    tissue = str(source_tissue).split("_", 1)[1] if "_" in str(source_tissue) else ""

    return (source_rank(source), source, tissue)


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

if len(chrom_lengths) == 0:
    raise ValueError("No chromosome lengths were recovered from the GFF3 feature table.")

# -----------------------------
# 5. Sample validated mapped peptide positions by tissue and chromosome
# -----------------------------
print("\nSampling fully validated mapped peptide positions from Step 11...")

header = pd.read_csv(sanity_file, nrows=0)

required_cols = [
    "Source",
    "Tissue",
    "Chromosome",
    "BED_start_0based",
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

tissue_positions = defaultdict(lambda: defaultdict(list))
chrom_counts = defaultdict(lambda: defaultdict(int))

total_rows_read = 0
total_validated_rows_used = 0

for chunk_i, chunk in enumerate(
    pd.read_csv(
        sanity_file,
        usecols=required_cols,
        chunksize=chunksize,
        low_memory=False
    ),
    start=1
):

    total_rows_read += len(chunk)

    # Keep only rows passing both validation layers:
    # Step 10 translation validation + Step 11 sanity checks
    chunk = chunk[
        chunk["Sanity_check_status"].astype(str) == "passed"
    ].copy()

    if chunk.empty:
        print(
            f"Chunk {chunk_i}: read {chunksize:,} rows | "
            f"no validated rows"
        )
        continue

    chunk["Chromosome"] = chunk["Chromosome"].apply(normalise_chromosome_name)

    chunk = chunk[
        chunk["Chromosome"].isin(chrom_order)
    ].copy()

    chunk["BED_start_0based"] = pd.to_numeric(
        chunk["BED_start_0based"],
        errors="coerce"
    )

    chunk = chunk.dropna(
        subset=[
            "Source",
            "Tissue",
            "Chromosome",
            "BED_start_0based"
        ]
    ).copy()

    if chunk.empty:
        continue

    total_validated_rows_used += len(chunk)

    chunk["Tissue_clean"] = chunk["Tissue"].apply(clean_tissue_label)

    chunk["Source_Tissue"] = (
        chunk["Source"].astype(str) + "_" +
        chunk["Tissue_clean"].astype(str)
    )

    for (source_tissue, chrom), group in chunk.groupby(["Source_Tissue", "Chromosome"]):

        chrom_counts[source_tissue][chrom] += len(group)

        # Sample a small number per chunk to avoid memory overload
        n_sample = min(50, len(group))

        tissue_positions[source_tissue][chrom].extend(
            group["BED_start_0based"]
            .sample(n=n_sample, random_state=42 + chunk_i)
            .astype(int)
            .tolist()
        )

    print(
        f"Chunk {chunk_i}: retained {len(chunk):,} validated mapped rows | "
        f"cumulative validated rows used {total_validated_rows_used:,}"
    )

# -----------------------------
# 6. Final cap per tissue/chromosome and summary table
# -----------------------------
source_tissues = sorted(
    list(tissue_positions.keys()),
    key=source_tissue_sort_key
)

if len(source_tissues) == 0:
    raise ValueError(
        "No validated mapped peptide positions were available for Circos plotting."
    )

summary_records = []

for source_tissue in source_tissues:

    source = source_tissue.split("_", 1)[0]
    tissue = source_tissue.split("_", 1)[1] if "_" in source_tissue else source_tissue

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
            "Source_Tissue": source_tissue,
            "Track_order_inner_to_outer": source_tissues.index(source_tissue) + 1,
            "Source": source,
            "Tissue": tissue,
            "Chromosome": chrom,
            "Total_validated_mapped_peptide_rows": chrom_counts[source_tissue].get(chrom, 0),
            "Sampled_points_plotted": len(tissue_positions[source_tissue][chrom])
        })

summary = pd.DataFrame(summary_records)
summary.to_csv(summary_out, index=False)

print(f"\nSummary saved: {summary_out}")
print("\nTrack order, innermost to outermost:")
for i, source_tissue in enumerate(source_tissues, start=1):
    print(f"{i:02d}. {source_tissue}")

# -----------------------------
# 7. Tissue colours
# -----------------------------
cmap = plt.get_cmap("tab20")

tissue_colours = {
    tissue: cmap(i % 20)
    for i, tissue in enumerate(source_tissues)
}

# -----------------------------
# 8. Build Circos plot
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

    # i = 0 is innermost
    # final source_tissue is outermost
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
# 9. Plot and legend
# -----------------------------
fig = circos.plotfig(figsize=(12, 12))

# Manual legend outside plot, ordered innermost to outermost
legend_handles = [
    plt.Line2D(
        [0], [0],
        marker="s",
        color="w",
        label=f"{i + 1}. {tissue}",
        markerfacecolor=tissue_colours[tissue],
        markersize=8
    )
    for i, tissue in enumerate(source_tissues)
]

legend = fig.legend(
    handles=legend_handles,
    title="Tissue tracks\n(inner → outer)",
    loc="upper right",
    bbox_to_anchor=(1.30, 0.95),
    frameon=True,
    fontsize=9,
    title_fontsize=12
)

legend.get_title().set_fontweight("bold")
legend.get_frame().set_edgecolor("lightgrey")
legend.get_frame().set_linewidth(1)
legend.get_frame().set_facecolor("white")

fig.suptitle(
    "Circular map of validated mapped wheat peptides by tissue",
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

    Chromosomes loaded: 22
    
    Sampling fully validated mapped peptide positions from Step 11...
    Chunk 1: retained 100,000 validated mapped rows | cumulative validated rows used 100,000
    Chunk 2: retained 100,000 validated mapped rows | cumulative validated rows used 200,000
    Chunk 3: retained 100,000 validated mapped rows | cumulative validated rows used 300,000
    Chunk 4: retained 100,000 validated mapped rows | cumulative validated rows used 400,000
    Chunk 5: retained 100,000 validated mapped rows | cumulative validated rows used 500,000
    Chunk 6: retained 100,000 validated mapped rows | cumulative validated rows used 600,000
    Chunk 7: retained 100,000 validated mapped rows | cumulative validated rows used 700,000
    Chunk 8: retained 100,000 validated mapped rows | cumulative validated rows used 800,000
    Chunk 9: retained 100,000 validated mapped rows | cumulative validated rows used 900,000
    Chunk 10: retained 100,000 validated mapped rows | cumulative validated rows used 1,000,000
    Chunk 11: retained 100,000 validated mapped rows | cumulative validated rows used 1,100,000
    Chunk 12: retained 100,000 validated mapped rows | cumulative validated rows used 1,200,000
    Chunk 13: retained 100,000 validated mapped rows | cumulative validated rows used 1,300,000
    Chunk 14: retained 100,000 validated mapped rows | cumulative validated rows used 1,400,000
    Chunk 15: retained 100,000 validated mapped rows | cumulative validated rows used 1,500,000
    Chunk 16: retained 100,000 validated mapped rows | cumulative validated rows used 1,600,000
    Chunk 17: retained 100,000 validated mapped rows | cumulative validated rows used 1,700,000
    Chunk 18: retained 100,000 validated mapped rows | cumulative validated rows used 1,800,000
    Chunk 19: retained 100,000 validated mapped rows | cumulative validated rows used 1,900,000
    Chunk 20: retained 100,000 validated mapped rows | cumulative validated rows used 2,000,000
    Chunk 21: retained 100,000 validated mapped rows | cumulative validated rows used 2,100,000
    Chunk 22: retained 100,000 validated mapped rows | cumulative validated rows used 2,200,000
    Chunk 23: retained 100,000 validated mapped rows | cumulative validated rows used 2,300,000
    Chunk 24: retained 100,000 validated mapped rows | cumulative validated rows used 2,400,000
    Chunk 25: retained 100,000 validated mapped rows | cumulative validated rows used 2,500,000
    Chunk 26: retained 100,000 validated mapped rows | cumulative validated rows used 2,600,000
    Chunk 27: retained 100,000 validated mapped rows | cumulative validated rows used 2,700,000
    Chunk 28: retained 100,000 validated mapped rows | cumulative validated rows used 2,800,000
    Chunk 29: retained 100,000 validated mapped rows | cumulative validated rows used 2,900,000
    Chunk 30: retained 100,000 validated mapped rows | cumulative validated rows used 3,000,000
    Chunk 31: retained 100,000 validated mapped rows | cumulative validated rows used 3,100,000
    Chunk 32: retained 100,000 validated mapped rows | cumulative validated rows used 3,200,000
    Chunk 33: retained 100,000 validated mapped rows | cumulative validated rows used 3,300,000
    Chunk 34: retained 100,000 validated mapped rows | cumulative validated rows used 3,400,000
    Chunk 35: retained 100,000 validated mapped rows | cumulative validated rows used 3,500,000
    Chunk 36: retained 100,000 validated mapped rows | cumulative validated rows used 3,600,000
    Chunk 37: retained 100,000 validated mapped rows | cumulative validated rows used 3,700,000
    Chunk 38: retained 100,000 validated mapped rows | cumulative validated rows used 3,800,000
    Chunk 39: retained 100,000 validated mapped rows | cumulative validated rows used 3,900,000
    Chunk 40: retained 100,000 validated mapped rows | cumulative validated rows used 4,000,000
    Chunk 41: retained 100,000 validated mapped rows | cumulative validated rows used 4,100,000
    Chunk 42: retained 100,000 validated mapped rows | cumulative validated rows used 4,200,000
    Chunk 43: retained 100,000 validated mapped rows | cumulative validated rows used 4,300,000
    Chunk 44: retained 100,000 validated mapped rows | cumulative validated rows used 4,400,000
    Chunk 45: retained 100,000 validated mapped rows | cumulative validated rows used 4,500,000
    Chunk 46: retained 100,000 validated mapped rows | cumulative validated rows used 4,600,000
    Chunk 47: retained 100,000 validated mapped rows | cumulative validated rows used 4,700,000
    Chunk 48: retained 100,000 validated mapped rows | cumulative validated rows used 4,800,000
    Chunk 49: retained 100,000 validated mapped rows | cumulative validated rows used 4,900,000
    Chunk 50: retained 100,000 validated mapped rows | cumulative validated rows used 5,000,000
    Chunk 51: retained 100,000 validated mapped rows | cumulative validated rows used 5,100,000
    Chunk 52: retained 100,000 validated mapped rows | cumulative validated rows used 5,200,000
    Chunk 53: retained 100,000 validated mapped rows | cumulative validated rows used 5,300,000
    Chunk 54: retained 100,000 validated mapped rows | cumulative validated rows used 5,400,000
    Chunk 55: retained 100,000 validated mapped rows | cumulative validated rows used 5,500,000
    Chunk 56: retained 100,000 validated mapped rows | cumulative validated rows used 5,600,000
    Chunk 57: retained 100,000 validated mapped rows | cumulative validated rows used 5,700,000
    Chunk 58: retained 100,000 validated mapped rows | cumulative validated rows used 5,800,000
    Chunk 59: retained 100,000 validated mapped rows | cumulative validated rows used 5,900,000
    Chunk 60: retained 100,000 validated mapped rows | cumulative validated rows used 6,000,000
    Chunk 61: retained 100,000 validated mapped rows | cumulative validated rows used 6,100,000
    Chunk 62: retained 100,000 validated mapped rows | cumulative validated rows used 6,200,000
    Chunk 63: retained 100,000 validated mapped rows | cumulative validated rows used 6,300,000
    Chunk 64: retained 100,000 validated mapped rows | cumulative validated rows used 6,400,000
    Chunk 65: retained 100,000 validated mapped rows | cumulative validated rows used 6,500,000
    Chunk 66: retained 100,000 validated mapped rows | cumulative validated rows used 6,600,000
    Chunk 67: retained 100,000 validated mapped rows | cumulative validated rows used 6,700,000
    Chunk 68: retained 100,000 validated mapped rows | cumulative validated rows used 6,800,000
    Chunk 69: retained 100,000 validated mapped rows | cumulative validated rows used 6,900,000
    Chunk 70: retained 100,000 validated mapped rows | cumulative validated rows used 7,000,000
    Chunk 71: retained 100,000 validated mapped rows | cumulative validated rows used 7,100,000
    Chunk 72: retained 100,000 validated mapped rows | cumulative validated rows used 7,200,000
    Chunk 73: retained 100,000 validated mapped rows | cumulative validated rows used 7,300,000
    Chunk 74: retained 100,000 validated mapped rows | cumulative validated rows used 7,400,000
    Chunk 75: retained 100,000 validated mapped rows | cumulative validated rows used 7,500,000
    Chunk 76: retained 100,000 validated mapped rows | cumulative validated rows used 7,600,000
    Chunk 77: retained 100,000 validated mapped rows | cumulative validated rows used 7,700,000
    Chunk 78: retained 100,000 validated mapped rows | cumulative validated rows used 7,800,000
    Chunk 79: retained 100,000 validated mapped rows | cumulative validated rows used 7,900,000
    Chunk 80: retained 100,000 validated mapped rows | cumulative validated rows used 8,000,000
    Chunk 81: retained 100,000 validated mapped rows | cumulative validated rows used 8,100,000
    Chunk 82: retained 100,000 validated mapped rows | cumulative validated rows used 8,200,000
    Chunk 83: retained 14,230 validated mapped rows | cumulative validated rows used 8,214,230
    
    Summary saved: python_outputs\tables\wheat_circos_tissue_validated_peptide_summary_step22.csv
    
    Track order, innermost to outermost:
    01. MSV000090572_stored_grain
    02. PXD004720_anther
    03. PXD004720_boot
    04. PXD004720_coleoptile
    05. PXD004720_embryo
    06. PXD004720_endosperm
    07. PXD004720_glume
    08. PXD004720_grain_zadoks_70
    09. PXD004720_grain_zadoks_71
    10. PXD004720_grain_zadoks_75
    11. PXD004720_grain_zadoks_83
    12. PXD004720_grain_zadoks_87
    13. PXD004720_leaf_flag_mature
    14. PXD004720_leaf_flag_senescing
    15. PXD004720_leaf_flag_young
    16. PXD004720_lemma
    17. PXD004720_node
    18. PXD004720_node_secretion
    19. PXD004720_palea
    20. PXD004720_pericarp
    21. PXD004720_pollen
    22. PXD004720_rachilla
    23. PXD004720_radicle
    24. PXD004720_root_mature
    25. PXD004720_root_secretion
    26. PXD004720_root_tip
    27. PXD004720_root_vasculature
    28. PXD004720_spike_immature
    29. PXD004720_stem
    30. PXD050500_coleoptile
    31. PXD050500_node
    32. PXD050500_radicle
    


    
![png](output_46_1.png)
    


    Figure saved: python_outputs\figures\step22_circos_tissue_validated_peptide_tracks.png
    


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
      <th>Track_order_inner_to_outer</th>
      <th>Source</th>
      <th>Tissue</th>
      <th>Chromosome</th>
      <th>Total_validated_mapped_peptide_rows</th>
      <th>Sampled_points_plotted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MSV000090572_stored_grain</td>
      <td>1</td>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>Chr1A</td>
      <td>1478</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>MSV000090572_stored_grain</td>
      <td>1</td>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>Chr1B</td>
      <td>1648</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>MSV000090572_stored_grain</td>
      <td>1</td>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>Chr1D</td>
      <td>1462</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3</th>
      <td>MSV000090572_stored_grain</td>
      <td>1</td>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>Chr2A</td>
      <td>1239</td>
      <td>100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>MSV000090572_stored_grain</td>
      <td>1</td>
      <td>MSV000090572</td>
      <td>stored_grain</td>
      <td>Chr2B</td>
      <td>1421</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>


# Step 23 — EDA: Pie chart of Validated Peptide Evidence by Annotation Confidence and Exon Structure

This exploratory analysis summarises the final validated peptide evidence according to annotation confidence level and exon structure.

The analysis focuses on the final all-tissue, non-redundant peptide projection set generated after translation validation and sanity checking. It provides a compact visual overview of how validated peptide evidence is distributed between high-confidence (HC) and low-confidence (LC) wheat gene annotations, and whether peptide projections are contained within a single exon or span multiple exons.

---

## Input files

### All-tissue non-redundant validated peptide table from Step 13

```text
wheat_all_tissues_nonredundant_validated_peptides_step13.csv
````

This table contains the final non-redundant set of annotation-guided peptide genome projections after:

```text
Step 10 — translation validation
Step 11 — BED geometry, chromosome/strand, block-length, and protein-coordinate sanity checks
Step 13 — all-tissue non-redundant peptide projection aggregation
```

### Protein-to-gene annotation mapping table from Step 5

```text
wheat_protein_gene_mapping_HC_LC.csv
```

This table was used to recover annotation confidence class (`HC` or `LC`) when this information was not already present in the Step 13 combined table.

---

## Plot design

The output figure contains three pie charts:

| Pie chart                  | Description                                                                                    |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| Overall HC/LC distribution | Proportion of non-redundant validated peptide projection rows assigned to HC or LC annotations |
| HC exon structure          | Proportion of HC peptide projection rows that are within-exon or exon-spanning                 |
| LC exon structure          | Proportion of LC peptide projection rows that are within-exon or exon-spanning                 |

---

## Exon-structure classification

Peptide exon structure was inferred from the BED block structure generated during peptide-to-genome projection.

| Class         | Definition             |
| ------------- | ---------------------- |
| Within-exon   | `BED_block_count == 1` |
| Exon-spanning | `BED_block_count > 1`  |

A within-exon peptide is represented by a single genomic block, whereas an exon-spanning peptide is represented by multiple BED blocks corresponding to peptide sequence split across two or more exons.

---

## Counting strategy

The primary counts are based on **non-redundant validated peptide projection rows**.

This means that each retained row represents a unique peptide/protein/genomic feature after all-tissue redundancy removal, rather than repeated observations across tissues.

The summary table also reports:

* number of non-redundant validated rows,
* number of unique peptide sequences,
* number of unique proteins,
* median, mean, and maximum BED block count,
* percentage of rows within each annotation confidence class,
* and percentage of rows overall.

---

## Output files

### Figure

```text
step23_validated_peptides_confidence_and_exon_structure_pies.png
```

### Summary table

```text
wheat_validated_peptides_confidence_and_exon_structure_summary_step23.csv
```

---

## Purpose

This figure provides a concise overview of the final validated peptide evidence set.

It highlights:

* the relative contribution of HC and LC annotations to validated peptide evidence,
* whether validated peptide projections mostly fall within single exons or span exon junctions,
* whether LC-supported peptide evidence shows similar exon-structure behaviour to HC-supported evidence,
* and the extent to which the workflow preserves exon-resolved peptide mapping information for Apollo/JBrowse interpretation.


```python
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
```

    Non-redundant validated peptide projection rows loaded: 3,173,811
    
    Annotation confidence counts:
    


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
      <th>Rows</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>2424948</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LC</td>
      <td>748863</td>
    </tr>
  </tbody>
</table>
</div>


    
    Exon-structure counts:
    


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
      <th>Exon_structure</th>
      <th>Rows</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Within-exon</td>
      <td>2808552</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Exon-spanning</td>
      <td>365259</td>
    </tr>
  </tbody>
</table>
</div>


    
    Step 23 summary saved: python_outputs\tables\wheat_validated_peptides_confidence_and_exon_structure_summary_step23.csv
    


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
      <th>Exon_structure</th>
      <th>Nonredundant_validated_rows</th>
      <th>Unique_peptide_sequences</th>
      <th>Unique_proteins</th>
      <th>Total_rows_within_confidence</th>
      <th>Total_unique_peptides_within_confidence</th>
      <th>Percent_rows_within_confidence</th>
      <th>Percent_rows_overall</th>
      <th>Median_BED_block_count</th>
      <th>Mean_BED_block_count</th>
      <th>Max_BED_block_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HC</td>
      <td>All</td>
      <td>2424948</td>
      <td>775525</td>
      <td>130006</td>
      <td>2424948</td>
      <td>775525</td>
      <td>100.0000</td>
      <td>76.4049</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>LC</td>
      <td>All</td>
      <td>748863</td>
      <td>381563</td>
      <td>142292</td>
      <td>748863</td>
      <td>381563</td>
      <td>100.0000</td>
      <td>23.5951</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HC</td>
      <td>Exon-spanning</td>
      <td>330367</td>
      <td>94087</td>
      <td>68246</td>
      <td>2424948</td>
      <td>775525</td>
      <td>13.6237</td>
      <td>10.4092</td>
      <td>2.0</td>
      <td>2.018098</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HC</td>
      <td>Within-exon</td>
      <td>2094581</td>
      <td>683809</td>
      <td>129570</td>
      <td>2424948</td>
      <td>775525</td>
      <td>86.3763</td>
      <td>65.9958</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>LC</td>
      <td>Exon-spanning</td>
      <td>34892</td>
      <td>26193</td>
      <td>19391</td>
      <td>748863</td>
      <td>381563</td>
      <td>4.6593</td>
      <td>1.0994</td>
      <td>2.0</td>
      <td>2.020807</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>LC</td>
      <td>Within-exon</td>
      <td>713971</td>
      <td>356427</td>
      <td>141024</td>
      <td>748863</td>
      <td>381563</td>
      <td>95.3407</td>
      <td>22.4957</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



    
![png](output_48_6.png)
    


    Figure saved: python_outputs\figures\step23_validated_peptides_confidence_and_exon_structure_pies.png
    

# Step 24 — Combine Python Workflow Summary Tables at Source/Tissue Level

This step integrates all major workflow summary tables generated throughout the proteogenomics pipeline into a single comprehensive tissue-level summary table. The resulting dataset provides a unified overview of peptide identification, protein mapping, genomic projection, and BED export statistics across all analysed tissues and data sources.

---

The workflow begins by defining the input/output directories and loading the FragPipe tissue manifest, which serves as the backbone for the integrated summary structure. Helper functions are then used to safely load summary files only if they exist and to standardise merge keys (`Source` and `Tissue`) across datasets. Combined “ALL” rows are removed to retain only tissue-level summaries suitable for downstream comparative analyses.

Summary outputs from previous workflow steps are then loaded, including:

- **Step 4:** FragPipe miscleavages and peptidelengths summaries  
- **Step 6:** FragPipe annotation summaries  
- **Step 7:** Peptide–protein evidence summaries  
- **Step 8:** Peptide–protein–gene mapping summaries  
- **Step 9:** Peptide genomic projection summaries  
- **Step 10:** Translation validation  
- **Step 11:** Sanity check validation
- **Step 12:** BED export summaries
- **Step 15:** Tissue-level proteogenomic summaries
- **Step 16:** Confidence-level coevrage summaries
- **Step 17:** Tissue-level overlap summaries

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

`wheat_complete_python_workflow_summary_step24.csv`

This consolidated table provides a high-level overview of the entire computational proteogenomics workflow and serves as a central resource for downstream exploratory data analysis, comparative tissue assessments, manuscript reporting, and reproducibility documentation.


```python
# ============================================================
# Step 24 — Combine Python workflow summary tables at source/tissue level
# Fully revised workflow summary using validated peptide projections
# ============================================================

import pandas as pd
from pathlib import Path
import re

# -----------------------------
# 1. Input / output paths
# -----------------------------
fragpipe_dir = Path("FragPipe_results")
tables_dir = Path("python_outputs/tables")

tables_dir.mkdir(parents=True, exist_ok=True)

manifest_file = fragpipe_dir / "wheat_tissues_FragPipe-result-manifest_2026-05-11.csv"

complete_python_summary_out = tables_dir / "wheat_complete_python_workflow_summary_step24.csv"

if not manifest_file.exists():
    raise FileNotFoundError(
        f"Manifest file not found:\n{manifest_file}"
    )

manifest = pd.read_csv(manifest_file, encoding="utf-8-sig")


# -----------------------------
# 2. Helper functions
# -----------------------------
def load_summary_if_exists(path):
    """
    Load a summary file if present.
    """
    path = Path(path)

    if path.exists():
        print(f"Loaded: {path.name}")
        return pd.read_csv(path, low_memory=False)

    print(f"Summary not found, skipped: {path}")
    return None


def projection_filename_from_manifest_row(row):
    """
    Convert FragPipe peptide TSV filename from the manifest into the corresponding
    Step 9 projection filename.
    """
    return str(row["FragPipe-Output-Peptide"]).replace(
        "_peptide.tsv",
        "_peptide_genome_projection.csv"
    )


def build_projection_manifest_lookup(manifest):
    """
    Build a lookup table linking each projection filename to source/tissue metadata.
    """
    lookup_records = []

    for _, row in manifest.iterrows():

        lookup_records.append({
            "Projection_file": projection_filename_from_manifest_row(row),
            "Source": str(row["Source"]).strip(),
            "Species": row["Species"],
            "Tissue": normalise_tissue_name(row["Tissue-Raw-Code"]),
            "Batch": row["Batch"]
        })

    return pd.DataFrame(lookup_records)



def add_source_tissue_from_projection_file(data):
    """
    Add Source/Tissue metadata to summary files that contain Projection_file
    but do not already contain Source and Tissue.
    """
    if data is None:
        return None

    data = data.copy()

    if "Projection_file" not in data.columns:
        return data

    has_source = "Source" in data.columns
    has_tissue = "Tissue" in data.columns

    if has_source and has_tissue:
        return data

    data = data.merge(
        projection_manifest_lookup,
        on="Projection_file",
        how="left",
        suffixes=("", "_manifest")
    )

    return data


def split_source_tissue(data):
    """
    Some EDA summaries only contain Source_Tissue.
    Split Source_Tissue into Source and Tissue where needed.
    """
    if data is None:
        return None

    data = data.copy()

    if "Source_Tissue" not in data.columns:
        return data

    if "Source" not in data.columns:

        data["Source"] = (
            data["Source_Tissue"]
            .astype(str)
            .str.split("_", n=1)
            .str[0]
        )

    if "Tissue" not in data.columns:

        data["Tissue"] = (
            data["Source_Tissue"]
            .astype(str)
            .str.split("_", n=1)
            .str[1]
        )

    return data

def normalise_tissue_name(value):
    """
    Standardise tissue names for merging across workflow summaries.

    Converts spaces and hyphens to underscores and collapses
    repeated underscores.
    """
    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    value = re.sub(
        r"[\s\-]+",
        "_",
        value
    )

    value = re.sub(
        r"_+",
        "_",
        value
    )

    return value.strip("_")


projection_manifest_lookup = build_projection_manifest_lookup(manifest)

def standardise_tissue_key(data):
    """
    Keep only source/tissue-level rows and standardise merge keys where possible.
    """
    if data is None:
        return None

    data = data.copy()

    data = add_source_tissue_from_projection_file(data)
    data = split_source_tissue(data)

    required_keys = ["Source", "Tissue"]

    if not all(col in data.columns for col in required_keys):
        return None

    # Remove combined/global rows for tissue-level integrated summary
    data = data[
        ~(
            (data["Source"].astype(str).str.upper() == "ALL") |
            (data["Tissue"].astype(str).str.upper() == "ALL")
        )
    ].copy()

    # Standardise as string keys
    data["Source"] = (
        data["Source"]
        .astype(str)
        .str.strip()
    )
    
    data["Tissue"] = (
        data["Tissue"]
        .map(normalise_tissue_name)
    )

    return data


def select_existing_columns(data, cols):
    """
    Return only columns available in data.
    """
    return [col for col in cols if col in data.columns]


def prefix_non_key_columns(data, prefix):
    """
    Prefix non-key columns before merging to avoid duplicate column names.
    """
    rename_cols = {
        col: f"{prefix}_{col}"
        for col in data.columns
        if col not in ["Source", "Tissue"]
    }

    return data.rename(columns=rename_cols)


# -----------------------------
# 3. Summary files from revised workflow
# -----------------------------
summary_files = {
    # Upstream FragPipe and mapping/projection summaries
    "step4_fragpipe_miscleavages": tables_dir / "wheat_fragpipe_peptide_length_missed_cleavage_tissue_summary_step4.csv",
    "step6_fragpipe_annotation": tables_dir / "wheat_fragpipe_annotation_summary_step6.csv",
    "step7_peptide_protein_evidence": tables_dir / "wheat_fragpipe_peptide_protein_evidence_summary_step7.csv",
    "step8_peptide_gene_mapping": tables_dir / "wheat_peptide_protein_gene_mapping_summary_step8.csv",
    "step9_initial_projection": tables_dir / "wheat_peptide_genome_projection_summary_step9.csv",

    # Revised validation workflow
    "step10_translation_validation": tables_dir / "wheat_projection_validation_100%_tissue_summary_step10.csv",
    "step11_sanity_checks": tables_dir / "wheat_projection_translation_validated_sanity_checks_summary_step11.csv",
    "step12_validated_bed_export": tables_dir / "wheat_bed_export_validated_summary_step12.csv",

    # Revised validated summary/EDA outputs
    "step15_validated_tissue_summary": tables_dir / "wheat_tissue_level_summary_step15.csv",
    "step16_validated_HC_LC_coverage": tables_dir / "wheat_eda_coverage_HC_LC_validated_step16.csv",
    "step17_validated_tissue_overlap": tables_dir / "wheat_tissue_overlap_validated_summary_step17.csv"
}

summaries = {
    step: standardise_tissue_key(load_summary_if_exists(path))
    for step, path in summary_files.items()
}


# -----------------------------
# 4. Start from manifest as source/tissue backbone
# -----------------------------
complete_summary = manifest[[
    "Source",
    "Species",
    "Tissue-Raw-Code",
    "Batch"
]].copy()

complete_summary = complete_summary.rename(
    columns={
        "Tissue-Raw-Code": "Tissue"
    }
)

complete_summary["Source"] = (
    complete_summary["Source"]
    .astype(str)
    .str.strip()
)

complete_summary["Tissue"] = (
    complete_summary["Tissue"]
    .map(normalise_tissue_name)
)

# Add projection filename for traceability
complete_summary = complete_summary.merge(
    projection_manifest_lookup[["Source", "Tissue", "Projection_file"]],
    on=["Source", "Tissue"],
    how="left"
)


# -----------------------------
# 5. Merge useful columns from each step
# -----------------------------
merge_specs = {
    "step4_fragpipe_miscleavages": [
        "Source",
        "Tissue",
        "Peptides_with_more_than_2_missed_cleavages",
        "Percent_with_more_than_2_missed_cleavages",
        "Peptides_longer_than_50_AA",
        "Percent_longer_than_50_AA",
        "Peptides_satisfying_both_criteria",
        "Percent_satisfying_both_criteria",
        "Maximum_missed_cleavages",
        "Maximum_peptide_length_AA"
    ],        
    
    "step6_fragpipe_annotation": [
        "Source",
        "Tissue",
        "FragPipe_result",
        "Total_rows",
        "Contaminant_count",
        "Non_contaminant_count"
    ],

    "step7_peptide_protein_evidence": [
        "Source",
        "Tissue",
        "Non_contaminant_peptide_protein_pairs",
        "Unique_peptides",
        "Unique_proteins",
        "Peptides_mapping_to_multiple_proteins",
        "Proteins_supported_by_one_peptide",
        "Proteins_supported_by_two_or_more_peptides"
    ],

    "step8_peptide_gene_mapping": [
        "Source",
        "Tissue",
        "Peptide_protein_pairs",
        "Mapped_peptide_protein_pairs",
        "Unmapped_peptide_protein_pairs",
        "Mapping_rate_percent",
        "Unique_gene_models",
        "Unique_transcripts"
    ],

    "step9_initial_projection": [
        "Source",
        "Tissue",
        "Peptide_protein_gene_rows",
        "Projected_rows",
        "Unprojected_rows",
        "Projection_rate_percent",
        "Unique_projected_peptides",
        "Unique_projected_proteins",
        "Unique_projected_gene_models",
        "Peptides_crossing_CDS_blocks"
    ],

    "step10_translation_validation": [
        "Source",
        "Tissue",
        "Projection_file",
        "Projected_rows_available",
        "Sample_fraction",
        "Rows_validated",
        "Exact_translation_matches",
        "Exact_translation_match_rate_percent",
        "IL_normalised_translation_matches",
        "IL_normalised_translation_match_rate_percent",
        "Multi_block_peptide_projections_tested",
        "Negative_strand_peptide_projections_tested",
        "Validation_status_validated",
        "Validation_status_translation_mismatch",
        "Validation_status_length_mismatch",
        "Validation_status_contains_N",
        "Validation_status_chromosome_not_found_in_genome_fasta"
    ],

    "step11_sanity_checks": [
        "Source",
        "Tissue",
        "Projection_file",
        "Rows_from_step10_validation_table",
        "Rows_translation_validated",
        "Rows_excluded_by_translation_validation",
        "Percent_translation_validated",
        "Translation_validated_rows_checked",
        "Rows_passing_all_sanity_checks",
        "Rows_failing_any_sanity_check",
        "Percent_passing_all_sanity_checks",
        "BED_geometry_failures",
        "Block_nt_length_failures",
        "Chromosome_strand_failures",
        "Protein_coordinate_failures"
    ],

    "step12_validated_bed_export": [
        "Source",
        "Tissue",
        "Projection_file",
        "BED6_file",
        "BED12_file",
        "Rows_in_step11_sanity_file",
        "Rows_passing_all_sanity_checks",
        "Rows_excluded_by_sanity_checks",
        "Rows_dropped_missing_BED_fields",
        "BED_rows",
        "Unique_BED_peptides",
        "Unique_BED_proteins",
        "Unique_BED_gene_models",
        "Multi_block_peptides",
        "Within_exon_peptides",
        "Intron_spanning_BED_rows",
        "Within_exon_BED_rows",
        "Unique_intron_spanning_peptides",
        "Unique_within_exon_peptides",
        "BED_labels_with_introns",
        "Percent_sanity_passed",
        "Percent_exported_to_BED"
    ],

    "step15_validated_tissue_summary": [
        "Source",
        "Tissue",
        "Validated_peptide_rows",
        "Unique_peptides",
        "Unique_proteins_isoforms",
        "Unique_gene_models",
        "Unique_HC_gene_models",
        "Unique_LC_gene_models",
        "Percent_total_gene_models_detected",
        "Percent_HC_gene_models_detected",
        "Percent_LC_gene_models_detected",
        "Unique_chromosomes",
        "Multi_exon_peptide_rows",
        "Within_exon_peptide_rows",
        "Proteins_supported_by_one_peptide",
        "Proteins_supported_by_two_or_more_peptides",
        "Genes_supported_by_one_peptide",
        "Genes_supported_by_two_or_more_peptides"
    ],

    "step16_validated_HC_LC_coverage": [
        "Source",
        "Tissue",
        "Source_Tissue",
        "HC_unique_proteins",
        "LC_unique_proteins",
        "Total_unique_proteins",
        "HC_unique_gene_models",
        "LC_unique_gene_models",
        "Total_unique_gene_models",
        "HC_unique_peptides",
        "LC_unique_peptides",
        "Total_unique_peptides",
        "Validated_BED_rows",
        "Multi_exon_peptide_rows",
        "Within_exon_peptide_rows",
        "HC_protein_percent",
        "LC_protein_percent",
        "Total_protein_percent",
        "HC_gene_model_percent",
        "LC_gene_model_percent",
        "Total_gene_model_percent"
    ],

    "step17_validated_tissue_overlap": [
        "Source",
        "Tissue",
        "Source_Tissue",
        "Validated_BED_rows",
        "Unique_validated_proteins",
        "Unique_validated_peptides",
        "Unique_validated_gene_models"
    ]
}


for step, cols in merge_specs.items():

    data = summaries.get(step)

    if data is None:
        print(f"Skipped merge for {step}: no usable Source/Tissue keys.")
        continue

    available_cols = select_existing_columns(data, cols)

    if "Source" not in available_cols or "Tissue" not in available_cols:
        print(f"Skipped merge for {step}: Source/Tissue not available.")
        continue

    data = data[available_cols].copy()

    # Step 6 has peptide/protein result rows; pivot to avoid duplicate tissue rows
    if step == "step6_fragpipe_annotation" and "FragPipe_result" in data.columns:

        data = data.pivot_table(
            index=["Source", "Tissue"],
            columns="FragPipe_result",
            values=[
                c for c in [
                    "Total_rows",
                    "Contaminant_count",
                    "Non_contaminant_count"
                ]
                if c in data.columns
            ],
            aggfunc="first"
        )

        data.columns = [
            f"{step}_{metric}_{result}"
            for metric, result in data.columns
        ]

        data = data.reset_index()

    else:

        data = prefix_non_key_columns(data, step)

        # Ensure one row per Source/Tissue
        data = data.drop_duplicates(
            subset=["Source", "Tissue"]
        )

    complete_summary = complete_summary.merge(
        data,
        on=["Source", "Tissue"],
        how="left"
    )


# -----------------------------
# 6. Add derived validation/export rates
# -----------------------------
def safe_percent(numerator, denominator):
    numerator = pd.to_numeric(numerator, errors="coerce")
    denominator = pd.to_numeric(denominator, errors="coerce")

    return ((numerator / denominator) * 100).round(4)


if (
    "step10_translation_validation_Validation_status_validated" in complete_summary.columns and
    "step10_translation_validation_Rows_validated" in complete_summary.columns
):

    complete_summary["derived_step10_translation_validated_percent"] = safe_percent(
        complete_summary["step10_translation_validation_Validation_status_validated"],
        complete_summary["step10_translation_validation_Rows_validated"]
    )

if (
    "step12_validated_bed_export_BED_rows" in complete_summary.columns and
    "step10_translation_validation_Projected_rows_available" in complete_summary.columns
):

    complete_summary["derived_final_validated_BED_rows_percent_of_initial_projected_rows"] = safe_percent(
        complete_summary["step12_validated_bed_export_BED_rows"],
        complete_summary["step10_translation_validation_Projected_rows_available"]
    )


# -----------------------------
# 7. Export complete summary
# -----------------------------
complete_summary.to_csv(
    complete_python_summary_out,
    index=False
)

print(f"\nComplete Python workflow summary saved: {complete_python_summary_out}")
print(f"Rows: {complete_summary.shape[0]:,}")
print(f"Columns: {complete_summary.shape[1]:,}")

display(complete_summary)
```

    Loaded: wheat_fragpipe_peptide_length_missed_cleavage_tissue_summary_step4.csv
    Loaded: wheat_fragpipe_annotation_summary_step6.csv
    Loaded: wheat_fragpipe_peptide_protein_evidence_summary_step7.csv
    Loaded: wheat_peptide_protein_gene_mapping_summary_step8.csv
    Loaded: wheat_peptide_genome_projection_summary_step9.csv
    Loaded: wheat_projection_validation_100%_tissue_summary_step10.csv
    Loaded: wheat_projection_translation_validated_sanity_checks_summary_step11.csv
    Loaded: wheat_bed_export_validated_summary_step12.csv
    Loaded: wheat_tissue_level_summary_step15.csv
    Loaded: wheat_eda_coverage_HC_LC_validated_step16.csv
    Loaded: wheat_tissue_overlap_validated_summary_step17.csv
    
    Complete Python workflow summary saved: python_outputs\tables\wheat_complete_python_workflow_summary_step24.csv
    Rows: 32
    Columns: 127
    


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
      <th>step4_fragpipe_miscleavages_Peptides_with_more_than_2_missed_cleavages</th>
      <th>step4_fragpipe_miscleavages_Percent_with_more_than_2_missed_cleavages</th>
      <th>step4_fragpipe_miscleavages_Peptides_longer_than_50_AA</th>
      <th>step4_fragpipe_miscleavages_Percent_longer_than_50_AA</th>
      <th>step4_fragpipe_miscleavages_Peptides_satisfying_both_criteria</th>
      <th>...</th>
      <th>step16_validated_HC_LC_coverage_HC_gene_model_percent</th>
      <th>step16_validated_HC_LC_coverage_LC_gene_model_percent</th>
      <th>step16_validated_HC_LC_coverage_Total_gene_model_percent</th>
      <th>step17_validated_tissue_overlap_Source_Tissue</th>
      <th>step17_validated_tissue_overlap_Validated_BED_rows</th>
      <th>step17_validated_tissue_overlap_Unique_validated_proteins</th>
      <th>step17_validated_tissue_overlap_Unique_validated_peptides</th>
      <th>step17_validated_tissue_overlap_Unique_validated_gene_models</th>
      <th>derived_step10_translation_validated_percent</th>
      <th>derived_final_validated_BED_rows_percent_of_initial_projected_rows</th>
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
      <td>1801</td>
      <td>19.276464</td>
      <td>62</td>
      <td>0.663598</td>
      <td>47</td>
      <td>...</td>
      <td>8.535833</td>
      <td>3.384677</td>
      <td>5.449256</td>
      <td>MSV000090572_stored_grain</td>
      <td>29892</td>
      <td>17110</td>
      <td>9126</td>
      <td>14536</td>
      <td>98.6079</td>
      <td>98.6079</td>
    </tr>
    <tr>
      <th>1</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_coleoptile_peptide_geno...</td>
      <td>14721</td>
      <td>2.524246</td>
      <td>165</td>
      <td>0.028293</td>
      <td>64</td>
      <td>...</td>
      <td>91.046074</td>
      <td>68.069545</td>
      <td>77.278521</td>
      <td>PXD050500_coleoptile</td>
      <td>1829196</td>
      <td>233744</td>
      <td>574831</td>
      <td>206142</td>
      <td>98.8682</td>
      <td>98.8682</td>
    </tr>
    <tr>
      <th>2</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_node_peptide_genome_pro...</td>
      <td>15804</td>
      <td>2.649735</td>
      <td>301</td>
      <td>0.050466</td>
      <td>137</td>
      <td>...</td>
      <td>91.757861</td>
      <td>69.674295</td>
      <td>78.525372</td>
      <td>PXD050500_node</td>
      <td>1864415</td>
      <td>237191</td>
      <td>587392</td>
      <td>209468</td>
      <td>98.8072</td>
      <td>98.8072</td>
    </tr>
    <tr>
      <th>3</th>
      <td>PXD050500</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Liu_PXD050500_radicle_peptide_genome_...</td>
      <td>5371</td>
      <td>1.610978</td>
      <td>142</td>
      <td>0.042591</td>
      <td>59</td>
      <td>...</td>
      <td>84.014254</td>
      <td>53.401569</td>
      <td>65.671110</td>
      <td>PXD050500_radicle</td>
      <td>1050178</td>
      <td>201263</td>
      <td>328566</td>
      <td>175179</td>
      <td>98.8395</td>
      <td>98.8395</td>
    </tr>
    <tr>
      <th>4</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>anther</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_anther_peptide_genom...</td>
      <td>2368</td>
      <td>6.923369</td>
      <td>65</td>
      <td>0.190042</td>
      <td>50</td>
      <td>...</td>
      <td>20.024506</td>
      <td>4.652210</td>
      <td>10.813415</td>
      <td>PXD004720_anther</td>
      <td>163467</td>
      <td>36275</td>
      <td>33982</td>
      <td>28845</td>
      <td>99.4537</td>
      <td>99.4537</td>
    </tr>
    <tr>
      <th>5</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>boot</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_boot_peptide_genome_...</td>
      <td>326</td>
      <td>8.946213</td>
      <td>19</td>
      <td>0.521405</td>
      <td>11</td>
      <td>...</td>
      <td>5.064818</td>
      <td>1.166181</td>
      <td>2.728752</td>
      <td>PXD004720_boot</td>
      <td>13137</td>
      <td>9126</td>
      <td>3599</td>
      <td>7279</td>
      <td>99.3196</td>
      <td>99.3196</td>
    </tr>
    <tr>
      <th>6</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>coleoptile</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_coleoptile_peptide_g...</td>
      <td>885</td>
      <td>2.151923</td>
      <td>30</td>
      <td>0.072947</td>
      <td>18</td>
      <td>...</td>
      <td>25.064070</td>
      <td>5.887836</td>
      <td>13.573656</td>
      <td>PXD004720_coleoptile</td>
      <td>203264</td>
      <td>45819</td>
      <td>40861</td>
      <td>36208</td>
      <td>99.4073</td>
      <td>99.4073</td>
    </tr>
    <tr>
      <th>7</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>embryo</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_embryo_peptide_genom...</td>
      <td>202</td>
      <td>7.043236</td>
      <td>9</td>
      <td>0.313808</td>
      <td>5</td>
      <td>...</td>
      <td>3.932132</td>
      <td>0.966604</td>
      <td>2.155185</td>
      <td>PXD004720_embryo</td>
      <td>8742</td>
      <td>7110</td>
      <td>2815</td>
      <td>5749</td>
      <td>98.7573</td>
      <td>98.7573</td>
    </tr>
    <tr>
      <th>8</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>endosperm</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_endosperm_peptide_ge...</td>
      <td>284</td>
      <td>1.407753</td>
      <td>27</td>
      <td>0.133836</td>
      <td>10</td>
      <td>...</td>
      <td>14.998971</td>
      <td>3.436605</td>
      <td>8.070792</td>
      <td>PXD004720_endosperm</td>
      <td>102289</td>
      <td>27099</td>
      <td>19953</td>
      <td>21529</td>
      <td>99.4739</td>
      <td>99.4739</td>
    </tr>
    <tr>
      <th>9</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>glume</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_glume_peptide_genome...</td>
      <td>1275</td>
      <td>4.445142</td>
      <td>77</td>
      <td>0.268452</td>
      <td>50</td>
      <td>...</td>
      <td>19.206091</td>
      <td>4.799234</td>
      <td>10.573491</td>
      <td>PXD004720_glume</td>
      <td>144079</td>
      <td>35014</td>
      <td>28512</td>
      <td>28205</td>
      <td>99.2738</td>
      <td>99.2738</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain_zadoks_70</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-70_pept...</td>
      <td>290</td>
      <td>1.105646</td>
      <td>27</td>
      <td>0.102939</td>
      <td>14</td>
      <td>...</td>
      <td>19.278111</td>
      <td>4.672856</td>
      <td>10.526631</td>
      <td>PXD004720_grain-zadoks-70</td>
      <td>125355</td>
      <td>34929</td>
      <td>26037</td>
      <td>28080</td>
      <td>99.3344</td>
      <td>99.3344</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain_zadoks_71</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-71_pept...</td>
      <td>315</td>
      <td>0.875243</td>
      <td>3</td>
      <td>0.008336</td>
      <td>1</td>
      <td>...</td>
      <td>25.221206</td>
      <td>5.820894</td>
      <td>13.596524</td>
      <td>PXD004720_grain-zadoks-71</td>
      <td>178814</td>
      <td>46422</td>
      <td>35806</td>
      <td>36269</td>
      <td>99.4931</td>
      <td>99.4931</td>
    </tr>
    <tr>
      <th>12</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain_zadoks_75</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-75_pept...</td>
      <td>160</td>
      <td>0.580720</td>
      <td>1</td>
      <td>0.003630</td>
      <td>0</td>
      <td>...</td>
      <td>22.675234</td>
      <td>4.957519</td>
      <td>12.058766</td>
      <td>PXD004720_grain-zadoks-75</td>
      <td>132081</td>
      <td>40582</td>
      <td>27293</td>
      <td>32167</td>
      <td>99.5328</td>
      <td>99.5328</td>
    </tr>
    <tr>
      <th>13</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain_zadoks_83</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-83_pept...</td>
      <td>184</td>
      <td>0.765041</td>
      <td>8</td>
      <td>0.033263</td>
      <td>5</td>
      <td>...</td>
      <td>19.800962</td>
      <td>4.807367</td>
      <td>10.816789</td>
      <td>PXD004720_grain-zadoks-83</td>
      <td>112389</td>
      <td>36046</td>
      <td>23840</td>
      <td>28854</td>
      <td>99.2809</td>
      <td>99.2809</td>
    </tr>
    <tr>
      <th>14</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>grain_zadoks_87</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_grain-zadoks-87_pept...</td>
      <td>275</td>
      <td>1.114534</td>
      <td>13</td>
      <td>0.052687</td>
      <td>3</td>
      <td>...</td>
      <td>18.719719</td>
      <td>4.761071</td>
      <td>10.355686</td>
      <td>PXD004720_grain-zadoks-87</td>
      <td>111156</td>
      <td>34405</td>
      <td>24482</td>
      <td>27624</td>
      <td>99.4311</td>
      <td>99.4311</td>
    </tr>
    <tr>
      <th>15</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf_flag_mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-mature_pep...</td>
      <td>218</td>
      <td>0.728099</td>
      <td>3</td>
      <td>0.010020</td>
      <td>2</td>
      <td>...</td>
      <td>20.991638</td>
      <td>4.654087</td>
      <td>11.202165</td>
      <td>PXD004720_leaf-flag-mature</td>
      <td>144641</td>
      <td>37453</td>
      <td>29731</td>
      <td>29882</td>
      <td>99.3195</td>
      <td>99.3195</td>
    </tr>
    <tr>
      <th>16</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf_flag_senescing</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-senescing_...</td>
      <td>239</td>
      <td>2.097595</td>
      <td>1</td>
      <td>0.008777</td>
      <td>1</td>
      <td>...</td>
      <td>13.407973</td>
      <td>4.070997</td>
      <td>7.813250</td>
      <td>PXD004720_leaf-flag-senescing</td>
      <td>45680</td>
      <td>25275</td>
      <td>11204</td>
      <td>20842</td>
      <td>98.8745</td>
      <td>98.8745</td>
    </tr>
    <tr>
      <th>17</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>leaf_flag_young</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_leaf-flag-young_pept...</td>
      <td>195</td>
      <td>0.831876</td>
      <td>6</td>
      <td>0.025596</td>
      <td>6</td>
      <td>...</td>
      <td>17.644088</td>
      <td>4.345024</td>
      <td>9.675279</td>
      <td>PXD004720_leaf-flag-young</td>
      <td>119922</td>
      <td>32180</td>
      <td>23296</td>
      <td>25809</td>
      <td>99.2559</td>
      <td>99.2559</td>
    </tr>
    <tr>
      <th>18</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>lemma</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_lemma_peptide_genome...</td>
      <td>594</td>
      <td>1.990483</td>
      <td>26</td>
      <td>0.087126</td>
      <td>18</td>
      <td>...</td>
      <td>20.412668</td>
      <td>5.062000</td>
      <td>11.214536</td>
      <td>PXD004720_lemma</td>
      <td>146562</td>
      <td>37386</td>
      <td>29653</td>
      <td>29915</td>
      <td>99.2846</td>
      <td>99.2846</td>
    </tr>
    <tr>
      <th>19</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node_peptide_genome_...</td>
      <td>462</td>
      <td>2.148038</td>
      <td>4</td>
      <td>0.018598</td>
      <td>2</td>
      <td>...</td>
      <td>18.569130</td>
      <td>5.865314</td>
      <td>10.956994</td>
      <td>PXD004720_node</td>
      <td>98731</td>
      <td>35794</td>
      <td>21280</td>
      <td>29228</td>
      <td>98.9061</td>
      <td>98.9061</td>
    </tr>
    <tr>
      <th>20</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>node_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_node-secretion_pepti...</td>
      <td>242</td>
      <td>0.707727</td>
      <td>4</td>
      <td>0.011698</td>
      <td>2</td>
      <td>...</td>
      <td>23.323419</td>
      <td>5.148963</td>
      <td>12.433271</td>
      <td>PXD004720_node_secretion</td>
      <td>168564</td>
      <td>41769</td>
      <td>34026</td>
      <td>33166</td>
      <td>99.3452</td>
      <td>99.3452</td>
    </tr>
    <tr>
      <th>21</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>palea</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_palea_peptide_genome...</td>
      <td>2186</td>
      <td>10.039497</td>
      <td>72</td>
      <td>0.330670</td>
      <td>51</td>
      <td>...</td>
      <td>15.331014</td>
      <td>3.198238</td>
      <td>8.061045</td>
      <td>PXD004720_palea</td>
      <td>116285</td>
      <td>27295</td>
      <td>21623</td>
      <td>21503</td>
      <td>99.4433</td>
      <td>99.4433</td>
    </tr>
    <tr>
      <th>22</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pericarp</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pericarp_peptide_gen...</td>
      <td>1081</td>
      <td>3.799916</td>
      <td>70</td>
      <td>0.246063</td>
      <td>35</td>
      <td>...</td>
      <td>17.688984</td>
      <td>4.171724</td>
      <td>9.589431</td>
      <td>PXD004720_pericarp</td>
      <td>130645</td>
      <td>32281</td>
      <td>28184</td>
      <td>25580</td>
      <td>99.5656</td>
      <td>99.5656</td>
    </tr>
    <tr>
      <th>23</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>pollen</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_pollen_peptide_genom...</td>
      <td>259</td>
      <td>1.905392</td>
      <td>27</td>
      <td>0.198632</td>
      <td>9</td>
      <td>...</td>
      <td>11.384851</td>
      <td>2.311090</td>
      <td>5.947847</td>
      <td>PXD004720_pollen</td>
      <td>74334</td>
      <td>19731</td>
      <td>13446</td>
      <td>15866</td>
      <td>99.5127</td>
      <td>99.5127</td>
    </tr>
    <tr>
      <th>24</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>rachilla</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_rachilla_peptide_gen...</td>
      <td>1659</td>
      <td>5.315093</td>
      <td>53</td>
      <td>0.169801</td>
      <td>34</td>
      <td>...</td>
      <td>20.046954</td>
      <td>4.746681</td>
      <td>10.879019</td>
      <td>PXD004720_rachilla</td>
      <td>159219</td>
      <td>36663</td>
      <td>31008</td>
      <td>29020</td>
      <td>99.3852</td>
      <td>99.3852</td>
    </tr>
    <tr>
      <th>25</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>radicle</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_radicle_peptide_geno...</td>
      <td>1486</td>
      <td>3.742696</td>
      <td>39</td>
      <td>0.098227</td>
      <td>18</td>
      <td>...</td>
      <td>24.030529</td>
      <td>4.812998</td>
      <td>12.515370</td>
      <td>PXD004720_radicle</td>
      <td>193938</td>
      <td>42476</td>
      <td>39487</td>
      <td>33385</td>
      <td>99.6117</td>
      <td>99.6117</td>
    </tr>
    <tr>
      <th>26</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root_mature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-mature_peptide_...</td>
      <td>1434</td>
      <td>6.704067</td>
      <td>12</td>
      <td>0.056101</td>
      <td>8</td>
      <td>...</td>
      <td>20.702621</td>
      <td>5.516836</td>
      <td>11.603287</td>
      <td>PXD004720_root-mature</td>
      <td>96387</td>
      <td>38544</td>
      <td>21125</td>
      <td>30952</td>
      <td>99.1758</td>
      <td>99.1758</td>
    </tr>
    <tr>
      <th>27</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root_secretion</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-secretion_pepti...</td>
      <td>1757</td>
      <td>8.237611</td>
      <td>26</td>
      <td>0.121900</td>
      <td>20</td>
      <td>...</td>
      <td>17.474793</td>
      <td>4.030956</td>
      <td>9.419236</td>
      <td>PXD004720_root-secretion</td>
      <td>100085</td>
      <td>31657</td>
      <td>21111</td>
      <td>25126</td>
      <td>99.4495</td>
      <td>99.4495</td>
    </tr>
    <tr>
      <th>28</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root_tip</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-tip_peptide_gen...</td>
      <td>1351</td>
      <td>3.492671</td>
      <td>47</td>
      <td>0.121507</td>
      <td>29</td>
      <td>...</td>
      <td>22.160802</td>
      <td>4.263692</td>
      <td>11.436840</td>
      <td>PXD004720_root-tip</td>
      <td>191262</td>
      <td>39337</td>
      <td>38496</td>
      <td>30508</td>
      <td>99.6452</td>
      <td>99.6452</td>
    </tr>
    <tr>
      <th>29</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>root_vasculature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_root-vasculature_pep...</td>
      <td>737</td>
      <td>3.524461</td>
      <td>7</td>
      <td>0.033475</td>
      <td>1</td>
      <td>...</td>
      <td>17.015545</td>
      <td>3.328370</td>
      <td>8.814179</td>
      <td>PXD004720_root-vasculature</td>
      <td>111315</td>
      <td>30323</td>
      <td>20728</td>
      <td>23512</td>
      <td>99.5386</td>
      <td>99.5386</td>
    </tr>
    <tr>
      <th>30</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>spike_immature</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_spike-immature_pepti...</td>
      <td>3108</td>
      <td>8.535179</td>
      <td>83</td>
      <td>0.227934</td>
      <td>61</td>
      <td>...</td>
      <td>21.994313</td>
      <td>4.439495</td>
      <td>11.475453</td>
      <td>PXD004720_spike-immature</td>
      <td>188025</td>
      <td>39779</td>
      <td>36236</td>
      <td>30611</td>
      <td>99.5758</td>
      <td>99.5758</td>
    </tr>
    <tr>
      <th>31</th>
      <td>PXD004720</td>
      <td>bread wheat</td>
      <td>stem</td>
      <td>single</td>
      <td>FragPipe_Duncan_PXD004720_stem_peptide_genome_...</td>
      <td>277</td>
      <td>1.925082</td>
      <td>2</td>
      <td>0.013900</td>
      <td>2</td>
      <td>...</td>
      <td>15.543334</td>
      <td>4.129181</td>
      <td>8.703965</td>
      <td>PXD004720_stem</td>
      <td>60181</td>
      <td>28948</td>
      <td>14177</td>
      <td>23218</td>
      <td>99.0895</td>
      <td>99.0895</td>
    </tr>
  </tbody>
</table>
<p>32 rows × 127 columns</p>
</div>


# Step 25 — Prepare manuscript Table 1 summary statistics

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
# Step 25 — Prepare manuscript Table 1 summary statistics
# ============================================================

import pandas as pd
import numpy as np
from pathlib import Path
import re

# -----------------------------
# 1. Paths
# -----------------------------
tables_dir = Path("python_outputs/tables")
tables_dir.mkdir(parents=True, exist_ok=True)

output_file = tables_dir / "wheat_manuscript_table1_preparatory_step25.csv"

# Main input summary tables
step24_file = tables_dir / "wheat_complete_python_workflow_summary_step24.csv"
step11_file = tables_dir / "wheat_projection_translation_validated_sanity_checks_summary_step11.csv"
gff3_summary_file = tables_dir / "wheat_gff3_parsing_summary_HC_LC.csv"
protein_gene_mapping_file = tables_dir / "wheat_protein_gene_mapping_HC_LC.csv"

# Step 13 combined non-redundant validated table
# The code accepts either filename depending on which version of Step 13 created it.
step13_candidate_files = [
    tables_dir / "wheat_all_tissues_nonredundant_validated_peptides_step13.csv",
    tables_dir / "wheat_all_tissues_nonredundant_validated_peptides.csv"
]

# Optional source-level Step 15 summary
step15_source_candidate_files = [
    tables_dir / "wheat_source_level_summary_step15.csv",
    tables_dir / "wheat_source_summary_step15.csv"
]

# -----------------------------
# 2. Manual dataset metadata
# -----------------------------
dataset_metadata = {
    "MSV000090572": {
        "Total tissues analysed": 1,
        "Total PRIDE/MassIVE datasets": 1,
        "Total raw MS files": 63,
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
        "Total raw MS files": 178,
        "Total raw data size (GB)": 434,
    },
}

sources = ["MSV000090572", "PXD004720", "PXD050500"]

# -----------------------------
# 3. Helper functions
# -----------------------------
def find_existing_file(candidate_paths, label):
    """
    Return the first existing file from a list of candidate paths.
    """
    for path in candidate_paths:
        if Path(path).exists():
            print(f"{label}: {path}")
            return Path(path)

    raise FileNotFoundError(
        f"No file found for {label}. Checked:\n" +
        "\n".join(str(p) for p in candidate_paths)
    )


def find_optional_file(candidate_paths, label):
    """
    Return the first existing file from a list of candidate paths, or None.
    """
    for path in candidate_paths:
        if Path(path).exists():
            print(f"{label}: {path}")
            return Path(path)

    print(f"{label}: not found; continuing without it.")
    return None


def safe_read_csv(path, required=True, **kwargs):
    """
    Read CSV with helpful error handling.
    """
    path = Path(path)

    if not path.exists():
        if required:
            raise FileNotFoundError(f"Required file not found:\n{path}")
        return pd.DataFrame()

    return pd.read_csv(path, low_memory=False, **kwargs)


def first_existing_col(data, candidates):
    """
    Return the first candidate column found in a DataFrame.
    """
    for col in candidates:
        if col in data.columns:
            return col
    return None


def first_existing_col_from_list(columns, candidates):
    """
    Return the first candidate column found in a column list.
    """
    columns = set(columns)
    for col in candidates:
        if col in columns:
            return col
    return None


def normalise_confidence(value):
    """
    Normalise annotation confidence values to HC / LC.
    """
    if pd.isna(value):
        return np.nan

    value = str(value).strip().upper()

    if value in ["HC", "HIGH", "HIGH_CONFIDENCE", "HIGH CONFIDENCE"]:
        return "HC"

    if value in ["LC", "LOW", "LOW_CONFIDENCE", "LOW CONFIDENCE"]:
        return "LC"

    return value


def parse_sources_field(value):
    """
    Parse Step 13 source membership.

    Supports comma-separated and pipe-separated values.
    """
    if pd.isna(value):
        return []

    parts = re.split(r"[,\|;]", str(value))

    return [
        p.strip()
        for p in parts
        if p.strip() != ""
    ]


def source_in_sources_field(value, source):
    """
    Check whether a source is listed in the Step 13 Sources field.
    """
    return source in parse_sources_field(value)


def safe_percent(numerator, denominator, digits=2):
    """
    Safe percentage calculation.
    """
    numerator = pd.to_numeric(numerator, errors="coerce")
    denominator = pd.to_numeric(denominator, errors="coerce")

    if pd.isna(numerator) or pd.isna(denominator) or denominator == 0:
        return np.nan

    return round((float(numerator) / float(denominator)) * 100, digits)


def add_row(rows, order, metric, total=np.nan, source_values=None, note=""):
    """
    Append one manuscript Table 1 row.
    """
    row = {
        "order": order,
        "Metric": metric,
        "Total": total,
        "MSV000090572": np.nan,
        "PXD004720": np.nan,
        "PXD050500": np.nan,
        "Note": note
    }

    if source_values is not None:
        for src in sources:
            row[src] = source_values.get(src, np.nan)

    rows.append(row)


def sum_by_source(data, metric_col):
    """
    Sum a metric by Source.
    """
    if data.empty or "Source" not in data.columns or metric_col not in data.columns:
        return np.nan, {src: np.nan for src in sources}

    tmp = data[["Source", metric_col]].copy()
    tmp["Source"] = tmp["Source"].astype(str)
    tmp[metric_col] = pd.to_numeric(tmp[metric_col], errors="coerce")

    grouped = (
        tmp.groupby("Source", dropna=False)[metric_col]
        .sum()
        .to_dict()
    )

    source_values = {
        src: grouped.get(src, 0)
        for src in sources
    }

    total = np.nansum(list(source_values.values()))

    return total, source_values


def extract_source_from_filename(value):
    """
    Recover Source from common projection/BED filenames if Source column is absent.
    """
    value = str(value)

    for src in sources:
        if src in value:
            return src

    return np.nan


def ensure_source_column(data):
    """
    Ensure a table has a Source column when possible.
    """
    if data.empty:
        return data

    data = data.copy()

    if "Source" in data.columns:
        data["Source"] = data["Source"].astype(str)
        return data

    for candidate in ["Projection_file", "Genome_projection_file", "BED6_file", "BED12_file"]:
        if candidate in data.columns:
            data["Source"] = data[candidate].apply(extract_source_from_filename)
            return data

    return data


def format_table_value(x):
    """
    Format values for display only.
    """
    if pd.isna(x):
        return ""

    try:
        x = float(x)

        if x.is_integer():
            return f"{int(x):,}"

        return f"{x:,.2f}"

    except Exception:
        return str(x)


# -----------------------------
# 4. Resolve files
# -----------------------------
step13_combined_file = find_existing_file(
    step13_candidate_files,
    "Step 13 non-redundant validated table"
)

step15_source_file = find_optional_file(
    step15_source_candidate_files,
    "Step 15 source-level summary"
)

# -----------------------------
# 5. Load small/summary tables
# -----------------------------
step24 = safe_read_csv(step24_file)
step11 = safe_read_csv(step11_file)
gff3_summary = safe_read_csv(gff3_summary_file)

step24 = ensure_source_column(step24)
step11 = ensure_source_column(step11)

if step15_source_file is not None:
    step15_source = safe_read_csv(step15_source_file, required=False)
    step15_source = ensure_source_column(step15_source)
else:
    step15_source = pd.DataFrame()

# -----------------------------
# 6. Load protein-to-gene mapping, using only required columns
# -----------------------------
protein_mapping_header = pd.read_csv(protein_gene_mapping_file, nrows=0)

protein_mapping_usecols = [
    col for col in [
        "ProteinID",
        "GeneModel",
        "GeneID",
        "Annotation_confidence"
    ]
    if col in protein_mapping_header.columns
]

protein_mapping = pd.read_csv(
    protein_gene_mapping_file,
    usecols=protein_mapping_usecols,
    low_memory=False
)

if "ProteinID" not in protein_mapping.columns:
    raise KeyError("ProteinID column missing from protein-to-gene mapping table.")

if "Annotation_confidence" not in protein_mapping.columns:
    raise KeyError("Annotation_confidence column missing from protein-to-gene mapping table.")

if "GeneModel" not in protein_mapping.columns and "GeneID" not in protein_mapping.columns:
    raise KeyError("Neither GeneModel nor GeneID found in protein-to-gene mapping table.")

protein_mapping["Annotation_confidence"] = (
    protein_mapping["Annotation_confidence"]
    .apply(normalise_confidence)
)

mapping_gene_col = "GeneModel" if "GeneModel" in protein_mapping.columns else "GeneID"

# GFF3 denominators: prefer unique gene models from mapping table
gff3_hc_total = int(
    protein_mapping.loc[
        protein_mapping["Annotation_confidence"] == "HC",
        mapping_gene_col
    ].dropna().astype(str).nunique()
)

gff3_lc_total = int(
    protein_mapping.loc[
        protein_mapping["Annotation_confidence"] == "LC",
        mapping_gene_col
    ].dropna().astype(str).nunique()
)

gff3_total = gff3_hc_total + gff3_lc_total

print("\nGFF3 denominator gene-model counts from protein-to-gene mapping:")
print(f"HC gene models: {gff3_hc_total:,}")
print(f"LC gene models: {gff3_lc_total:,}")
print(f"Total gene models: {gff3_total:,}")

# -----------------------------
# 7. Load Step 13 combined table efficiently
# -----------------------------
step13_header = pd.read_csv(step13_combined_file, nrows=0)
step13_columns = list(step13_header.columns)

gene_col_step13 = first_existing_col_from_list(
    step13_columns,
    ["Gene_label", "GeneModel", "GeneID", "Gene_model"]
)

if gene_col_step13 is None:
    # We can recover gene model from protein mapping later
    gene_col_step13 = None

step13_needed_cols = [
    "Peptide",
    "ProteinID",
    "BED_block_count",
    "Sources",
    "Tissues",
    "Tissue_count",
    "Observation_count",
    "Annotation_confidence"
]

if gene_col_step13 is not None:
    step13_needed_cols.append(gene_col_step13)

step13_usecols = [
    col for col in step13_needed_cols
    if col in step13_columns
]

missing_core_step13 = [
    col for col in ["Peptide", "ProteinID", "BED_block_count"]
    if col not in step13_usecols
]

if missing_core_step13:
    raise KeyError(
        f"Missing required column(s) in Step 13 combined table: {missing_core_step13}"
    )

print("\nReading Step 13 combined table using only required columns:")
print(step13_usecols)

step13 = pd.read_csv(
    step13_combined_file,
    usecols=step13_usecols,
    low_memory=False
)

# Add GeneModel and Annotation_confidence from mapping if needed
mapping_lookup_cols = ["ProteinID", mapping_gene_col, "Annotation_confidence"]

mapping_lookup = (
    protein_mapping[mapping_lookup_cols]
    .dropna(subset=["ProteinID"])
    .drop_duplicates(subset=["ProteinID"])
    .copy()
)

mapping_lookup = mapping_lookup.rename(columns={
    mapping_gene_col: "GeneModel_from_mapping",
    "Annotation_confidence": "Annotation_confidence_from_mapping"
})

step13 = step13.merge(
    mapping_lookup,
    on="ProteinID",
    how="left"
)

# Final confidence column
if "Annotation_confidence" in step13.columns:
    step13["Annotation_confidence_final"] = step13["Annotation_confidence"].apply(normalise_confidence)
else:
    step13["Annotation_confidence_final"] = np.nan

step13["Annotation_confidence_final"] = step13["Annotation_confidence_final"].fillna(
    step13["Annotation_confidence_from_mapping"]
)

# Final gene column
if gene_col_step13 is not None:
    step13["GeneModel_final"] = step13[gene_col_step13].astype(str)
    step13.loc[
        step13["GeneModel_final"].isin(["", "nan", "NA", "None", "<NA>"]),
        "GeneModel_final"
    ] = np.nan
else:
    step13["GeneModel_final"] = np.nan

step13["GeneModel_final"] = step13["GeneModel_final"].fillna(
    step13["GeneModel_from_mapping"]
)

# Clean
step13["BED_block_count"] = pd.to_numeric(
    step13["BED_block_count"],
    errors="coerce"
)

step13 = step13.dropna(
    subset=[
        "Peptide",
        "ProteinID",
        "GeneModel_final",
        "Annotation_confidence_final",
        "BED_block_count"
    ]
).copy()

step13["BED_block_count"] = step13["BED_block_count"].astype(int)

step13 = step13[
    step13["Annotation_confidence_final"].isin(["HC", "LC"])
].copy()

print(f"\nStep 13 non-redundant validated rows loaded: {len(step13):,}")

# -----------------------------
# 8. Compute Step 13 non-redundant validated metrics
# -----------------------------
total_nonredundant_validated_rows = int(len(step13))
overall_within_exon_rows = int((step13["BED_block_count"] == 1).sum())
overall_exon_spanning_rows = int((step13["BED_block_count"] > 1).sum())

overall_unique_peptides = int(step13["Peptide"].nunique())
overall_unique_proteins = int(step13["ProteinID"].nunique())
overall_unique_gene_models = int(step13["GeneModel_final"].nunique())

step13_hc = step13[step13["Annotation_confidence_final"] == "HC"].copy()
step13_lc = step13[step13["Annotation_confidence_final"] == "LC"].copy()

overall_gene_counts = {
    "HC": int(step13_hc["GeneModel_final"].nunique()),
    "LC": int(step13_lc["GeneModel_final"].nunique())
}
overall_gene_counts["Total"] = overall_gene_counts["HC"] + overall_gene_counts["LC"]

# Source-specific metrics using Step 13 Sources field, if available.
# These source columns are not mutually exclusive because a non-redundant feature can be observed in multiple sources.
has_sources_field = "Sources" in step13.columns

nonredundant_rows_by_source = {}
within_exon_rows_by_source = {}
exon_spanning_rows_by_source = {}
unique_peptides_by_source = {}
unique_proteins_by_source = {}
gene_counts_by_source = {
    "HC": {},
    "LC": {},
    "Total": {}
}

for src in sources:

    if has_sources_field:
        src_mask = step13["Sources"].apply(
            lambda x: source_in_sources_field(x, src)
        )
    else:
        src_mask = pd.Series([False] * len(step13), index=step13.index)

    if has_sources_field:
        source_subset = step13[src_mask].copy()

        nonredundant_rows_by_source[src] = int(len(source_subset))
        within_exon_rows_by_source[src] = int((source_subset["BED_block_count"] == 1).sum())
        exon_spanning_rows_by_source[src] = int((source_subset["BED_block_count"] > 1).sum())

        unique_peptides_by_source[src] = int(source_subset["Peptide"].nunique())
        unique_proteins_by_source[src] = int(source_subset["ProteinID"].nunique())

        gene_counts_by_source["HC"][src] = int(
            source_subset.loc[
                source_subset["Annotation_confidence_final"] == "HC",
                "GeneModel_final"
            ].nunique()
        )

        gene_counts_by_source["LC"][src] = int(
            source_subset.loc[
                source_subset["Annotation_confidence_final"] == "LC",
                "GeneModel_final"
            ].nunique()
        )

        gene_counts_by_source["Total"][src] = (
            gene_counts_by_source["HC"][src] +
            gene_counts_by_source["LC"][src]
        )

    else:
        nonredundant_rows_by_source[src] = np.nan
        within_exon_rows_by_source[src] = np.nan
        exon_spanning_rows_by_source[src] = np.nan
        unique_peptides_by_source[src] = np.nan
        unique_proteins_by_source[src] = np.nan
        gene_counts_by_source["HC"][src] = np.nan
        gene_counts_by_source["LC"][src] = np.nan
        gene_counts_by_source["Total"][src] = np.nan

# If Sources field was not available, try Step 15 source summary for gene counts
if not has_sources_field and not step15_source.empty and "Source" in step15_source.columns:

    hc_col = first_existing_col(
        step15_source,
        ["Unique_HC_gene_models", "HC_unique_gene_models"]
    )

    lc_col = first_existing_col(
        step15_source,
        ["Unique_LC_gene_models", "LC_unique_gene_models"]
    )

    total_gene_col = first_existing_col(
        step15_source,
        ["Unique_gene_models", "Total_unique_gene_models"]
    )

    for src in sources:

        match = step15_source[step15_source["Source"].astype(str) == src]

        if not match.empty:

            if hc_col is not None:
                gene_counts_by_source["HC"][src] = int(
                    pd.to_numeric(match[hc_col], errors="coerce").sum()
                )

            if lc_col is not None:
                gene_counts_by_source["LC"][src] = int(
                    pd.to_numeric(match[lc_col], errors="coerce").sum()
                )

            if total_gene_col is not None:
                gene_counts_by_source["Total"][src] = int(
                    pd.to_numeric(match[total_gene_col], errors="coerce").sum()
                )

# -----------------------------
# 9. Resolve Step 24 metric columns
# -----------------------------
step24_unique_peptides_col = first_existing_col(
    step24,
    [
        "step7_peptide_protein_evidence_Unique_peptides",
        "step7_Unique_peptides",
        "Unique_peptides"
    ]
)

step24_unique_proteins_col = first_existing_col(
    step24,
    [
        "step7_peptide_protein_evidence_Unique_proteins",
        "step7_Unique_proteins",
        "Unique_proteins"
    ]
)

step24_initial_projected_rows_col = first_existing_col(
    step24,
    [
        "step9_initial_projection_Projected_rows",
        "step9_Projected_rows",
        "Projected_rows"
    ]
)

# -----------------------------
# 10. Resolve Step 11 validation metric columns
# -----------------------------
step11_entering_col = first_existing_col(
    step11,
    [
        "Rows_from_step10_validation_table",
        "Projected_rows_checked",
        "Rows_validated",
        "Translation_validated_rows_checked"
    ]
)

step11_translation_validated_col = first_existing_col(
    step11,
    [
        "Rows_translation_validated",
        "Validation_status_validated",
        "Rows_passing_translation_validation"
    ]
)

step11_translation_excluded_col = first_existing_col(
    step11,
    [
        "Rows_excluded_by_translation_validation",
        "Validation_status_translation_mismatch"
    ]
)

step11_sanity_passed_col = first_existing_col(
    step11,
    [
        "Rows_passing_all_sanity_checks",
        "Translation_validated_rows_passing_all_sanity_checks"
    ]
)

step11_sanity_failed_col = first_existing_col(
    step11,
    [
        "Rows_failing_any_sanity_check",
        "Rows_failing_any_sanity_checks"
    ]
)

# -----------------------------
# 11. Build manuscript Table 1
# -----------------------------
rows = []

# Dataset metadata
for metric, order in [
    ("Total tissues analysed", 1),
    ("Total PRIDE/MassIVE datasets", 2),
    ("Total raw MS files", 3),
    ("Total raw data size (GB)", 4),
]:

    source_values = {
        src: dataset_metadata[src][metric]
        for src in sources
    }

    add_row(
        rows,
        order,
        metric,
        total=sum(source_values.values()),
        source_values=source_values
    )

# FragPipe / projection metrics from Step 24
for col, order, label in [
    (step24_unique_peptides_col, 5, "FragPipe unique peptides"),
    (step24_unique_proteins_col, 6, "FragPipe unique proteins"),
    (step24_initial_projected_rows_col, 7, "Initial annotation-projected peptide rows")
]:

    if col is None:
        add_row(
            rows,
            order,
            label,
            total=np.nan,
            source_values={src: np.nan for src in sources},
            note="Column not found in Step 24 summary"
        )
        continue

    total, source_values = sum_by_source(step24, col)

    add_row(
        rows,
        order,
        label,
        total=int(total) if pd.notna(total) else np.nan,
        source_values={
            src: int(value) if pd.notna(value) else np.nan
            for src, value in source_values.items()
        },
        note=f"From Step 24 column: {col}"
    )

# Validation metrics from Step 11
step11_metric_map = [
    (step11_entering_col, 8, "Rows entering translation validation"),
    (step11_translation_validated_col, 9, "Translation-validated peptide projection rows"),
    (step11_translation_excluded_col, 10, "Rows excluded by translation validation"),
    (step11_sanity_passed_col, 11, "Rows passing all sanity checks"),
    (step11_sanity_failed_col, 12, "Rows failing any sanity check")
]

step11_values = {}

for col, order, label in step11_metric_map:

    if col is None:
        add_row(
            rows,
            order,
            label,
            total=np.nan,
            source_values={src: np.nan for src in sources},
            note="Column not found in Step 11 summary"
        )

        step11_values[label] = {
            "total": np.nan,
            "sources": {src: np.nan for src in sources}
        }

        continue

    total, source_values = sum_by_source(step11, col)

    step11_values[label] = {
        "total": total,
        "sources": source_values
    }

    add_row(
        rows,
        order,
        label,
        total=int(total) if pd.notna(total) else np.nan,
        source_values={
            src: int(value) if pd.notna(value) else np.nan
            for src, value in source_values.items()
        },
        note=f"From Step 11 column: {col}"
    )

# Final validation rate
validation_rate_sources = {}

for src in sources:
    entered = step11_values["Rows entering translation validation"]["sources"].get(src, np.nan)
    passed = step11_values["Rows passing all sanity checks"]["sources"].get(src, np.nan)
    validation_rate_sources[src] = safe_percent(passed, entered)

validation_rate_total = safe_percent(
    step11_values["Rows passing all sanity checks"]["total"],
    step11_values["Rows entering translation validation"]["total"]
)

add_row(
    rows,
    13,
    "Final validation rate (%)",
    total=validation_rate_total,
    source_values=validation_rate_sources,
    note="Rows passing translation validation and all sanity checks / rows entering translation validation × 100"
)

# Final non-redundant validated projection metrics from Step 13
add_row(
    rows,
    14,
    "Non-redundant validated peptide projection rows",
    total=total_nonredundant_validated_rows,
    source_values=nonredundant_rows_by_source,
    note="Computed from Step 13 all-tissue non-redundant validated table; source columns are not mutually exclusive if evidence is shared across sources"
)

add_row(
    rows,
    15,
    "Non-redundant validated within-exon peptide projection rows",
    total=overall_within_exon_rows,
    source_values=within_exon_rows_by_source,
    note="Within-exon defined as BED_block_count == 1"
)

add_row(
    rows,
    16,
    "Non-redundant validated exon-spanning peptide projection rows",
    total=overall_exon_spanning_rows,
    source_values=exon_spanning_rows_by_source,
    note="Exon-spanning defined as BED_block_count > 1"
)

add_row(
    rows,
    17,
    "Non-redundant validated unique peptide sequences",
    total=overall_unique_peptides,
    source_values=unique_peptides_by_source,
    note="Computed from Step 13 all-tissue non-redundant validated table"
)

add_row(
    rows,
    18,
    "Non-redundant validated unique protein isoforms",
    total=overall_unique_proteins,
    source_values=unique_proteins_by_source,
    note="Computed from Step 13 all-tissue non-redundant validated table"
)

# Gene model support
add_row(
    rows,
    19,
    "Non-redundant validated HC gene models",
    total=overall_gene_counts["HC"],
    source_values=gene_counts_by_source["HC"],
    note="Computed from Step 13 all-tissue non-redundant validated table"
)

add_row(
    rows,
    20,
    "Non-redundant validated LC gene models",
    total=overall_gene_counts["LC"],
    source_values=gene_counts_by_source["LC"],
    note="Computed from Step 13 all-tissue non-redundant validated table"
)

add_row(
    rows,
    21,
    "Non-redundant validated total gene models",
    total=overall_gene_counts["Total"],
    source_values=gene_counts_by_source["Total"],
    note="HC + LC non-redundant validated gene models"
)

# GFF3 denominators
add_row(
    rows,
    22,
    "GFF3-parsed HC gene models",
    total=gff3_hc_total,
    source_values={src: np.nan for src in sources},
    note="Reference denominator from unique HC GeneModel counts in protein-to-gene mapping table"
)

add_row(
    rows,
    23,
    "GFF3-parsed LC gene models",
    total=gff3_lc_total,
    source_values={src: np.nan for src in sources},
    note="Reference denominator from unique LC GeneModel counts in protein-to-gene mapping table"
)

add_row(
    rows,
    24,
    "GFF3-parsed total gene models",
    total=gff3_total,
    source_values={src: np.nan for src in sources},
    note="HC + LC unique GFF3-parsed gene models"
)

# Gene model validation rates
hc_rate = safe_percent(overall_gene_counts["HC"], gff3_hc_total)
lc_rate = safe_percent(overall_gene_counts["LC"], gff3_lc_total)
total_rate = safe_percent(overall_gene_counts["Total"], gff3_total)

hc_rate_sources = {
    src: safe_percent(gene_counts_by_source["HC"].get(src, np.nan), gff3_hc_total)
    for src in sources
}

lc_rate_sources = {
    src: safe_percent(gene_counts_by_source["LC"].get(src, np.nan), gff3_lc_total)
    for src in sources
}

total_rate_sources = {
    src: safe_percent(gene_counts_by_source["Total"].get(src, np.nan), gff3_total)
    for src in sources
}

add_row(
    rows,
    25,
    "HC gene model validation rate (%)",
    total=hc_rate,
    source_values=hc_rate_sources,
    note="Non-redundant validated HC gene models / GFF3-parsed HC gene models × 100"
)

add_row(
    rows,
    26,
    "LC gene model validation rate (%)",
    total=lc_rate,
    source_values=lc_rate_sources,
    note="Non-redundant validated LC gene models / GFF3-parsed LC gene models × 100"
)

add_row(
    rows,
    27,
    "Total gene model validation rate (%)",
    total=total_rate,
    source_values=total_rate_sources,
    note="Non-redundant validated total gene models / GFF3-parsed total gene models × 100"
)

# -----------------------------
# 12. Final formatting and export
# -----------------------------
table1_prep = pd.DataFrame(rows)
table1_prep = table1_prep.sort_values("order").reset_index(drop=True)

# Save numeric version
table1_prep.to_csv(output_file, index=False)

# Display-friendly version
display_table = table1_prep.copy()

for col in ["Total", "MSV000090572", "PXD004720", "PXD050500"]:
    display_table[col] = display_table[col].apply(format_table_value)

print("\nPreparatory manuscript Table 1 saved to:")
print(output_file)

print("\nFiles used:")
print(f"Step 24 complete workflow summary: {step24_file}")
print(f"Step 11 validation summary: {step11_file}")
print(f"Step 13 non-redundant validated table: {step13_combined_file}")
print(f"Protein-to-gene mapping table: {protein_gene_mapping_file}")
print(f"GFF3 summary table: {gff3_summary_file}")

print("\nImportant note:")
print(
    "Source-specific counts from the Step 13 non-redundant table are not mutually exclusive "
    "when the same non-redundant peptide/protein/genomic feature was observed in multiple sources."
)

display(display_table)
```

    Step 13 non-redundant validated table: python_outputs\tables\wheat_all_tissues_nonredundant_validated_peptides_step13.csv
    Step 15 source-level summary: python_outputs\tables\wheat_source_level_summary_step15.csv
    
    GFF3 denominator gene-model counts from protein-to-gene mapping:
    HC gene models: 106,914
    LC gene models: 159,838
    Total gene models: 266,752
    
    Reading Step 13 combined table using only required columns:
    ['Peptide', 'ProteinID', 'BED_block_count', 'Sources', 'Tissues', 'Tissue_count', 'Observation_count', 'Gene_label']
    
    Step 13 non-redundant validated rows loaded: 3,173,811
    
    Preparatory manuscript Table 1 saved to:
    python_outputs\tables\wheat_manuscript_table1_preparatory_step25.csv
    
    Files used:
    Step 24 complete workflow summary: python_outputs\tables\wheat_complete_python_workflow_summary_step24.csv
    Step 11 validation summary: python_outputs\tables\wheat_projection_translation_validated_sanity_checks_summary_step11.csv
    Step 13 non-redundant validated table: python_outputs\tables\wheat_all_tissues_nonredundant_validated_peptides_step13.csv
    Protein-to-gene mapping table: python_outputs\tables\wheat_protein_gene_mapping_HC_LC.csv
    GFF3 summary table: python_outputs\tables\wheat_gff3_parsing_summary_HC_LC.csv
    
    Important note:
    Source-specific counts from the Step 13 non-redundant table are not mutually exclusive when the same non-redundant peptide/protein/genomic feature was observed in multiple sources.
    


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
      <td>576</td>
      <td>63</td>
      <td>335</td>
      <td>178</td>
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
      <td>FragPipe unique peptides</td>
      <td>2,226,779</td>
      <td>9,329</td>
      <td>705,663</td>
      <td>1,511,787</td>
      <td>From Step 24 column: step7_peptide_protein_evi...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>FragPipe unique proteins</td>
      <td>1,648,740</td>
      <td>17,481</td>
      <td>942,854</td>
      <td>688,405</td>
      <td>From Step 24 column: step7_peptide_protein_evi...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>Initial annotation-projected peptide rows</td>
      <td>8,291,056</td>
      <td>30,314</td>
      <td>3,461,176</td>
      <td>4,799,566</td>
      <td>From Step 24 column: step9_initial_projection_...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Rows entering translation validation</td>
      <td>8,291,056</td>
      <td>30,314</td>
      <td>3,461,176</td>
      <td>4,799,566</td>
      <td>From Step 11 column: Rows_from_step10_validati...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>Translation-validated peptide projection rows</td>
      <td>8,214,230</td>
      <td>29,892</td>
      <td>3,440,549</td>
      <td>4,743,789</td>
      <td>From Step 11 column: Rows_translation_validated</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>Rows excluded by translation validation</td>
      <td>76,826</td>
      <td>422</td>
      <td>20,627</td>
      <td>55,777</td>
      <td>From Step 11 column: Rows_excluded_by_translat...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Rows passing all sanity checks</td>
      <td>8,214,230</td>
      <td>29,892</td>
      <td>3,440,549</td>
      <td>4,743,789</td>
      <td>From Step 11 column: Rows_passing_all_sanity_c...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>Rows failing any sanity check</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>From Step 11 column: Rows_failing_any_sanity_c...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>Final validation rate (%)</td>
      <td>99.07</td>
      <td>98.61</td>
      <td>99.40</td>
      <td>98.84</td>
      <td>Rows passing translation validation and all sa...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>Non-redundant validated peptide projection rows</td>
      <td>3,173,811</td>
      <td>29,892</td>
      <td>826,257</td>
      <td>2,842,246</td>
      <td>Computed from Step 13 all-tissue non-redundant...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>Non-redundant validated within-exon peptide pr...</td>
      <td>2,808,552</td>
      <td>26,630</td>
      <td>711,151</td>
      <td>2,521,279</td>
      <td>Within-exon defined as BED_block_count == 1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>Non-redundant validated exon-spanning peptide ...</td>
      <td>365,259</td>
      <td>3,262</td>
      <td>115,106</td>
      <td>320,967</td>
      <td>Exon-spanning defined as BED_block_count &gt; 1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>Non-redundant validated unique peptide sequences</td>
      <td>1,095,523</td>
      <td>9,126</td>
      <td>231,901</td>
      <td>976,526</td>
      <td>Computed from Step 13 all-tissue non-redundant...</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>Non-redundant validated unique protein isoforms</td>
      <td>272,298</td>
      <td>17,110</td>
      <td>169,983</td>
      <td>268,333</td>
      <td>Computed from Step 13 all-tissue non-redundant...</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>Non-redundant validated HC gene models</td>
      <td>104,417</td>
      <td>9,126</td>
      <td>79,627</td>
      <td>103,770</td>
      <td>Computed from Step 13 all-tissue non-redundant...</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>Non-redundant validated LC gene models</td>
      <td>139,147</td>
      <td>5,410</td>
      <td>67,040</td>
      <td>135,929</td>
      <td>Computed from Step 13 all-tissue non-redundant...</td>
    </tr>
    <tr>
      <th>20</th>
      <td>21</td>
      <td>Non-redundant validated total gene models</td>
      <td>243,564</td>
      <td>14,536</td>
      <td>146,667</td>
      <td>239,699</td>
      <td>HC + LC non-redundant validated gene models</td>
    </tr>
    <tr>
      <th>21</th>
      <td>22</td>
      <td>GFF3-parsed HC gene models</td>
      <td>106,914</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Reference denominator from unique HC GeneModel...</td>
    </tr>
    <tr>
      <th>22</th>
      <td>23</td>
      <td>GFF3-parsed LC gene models</td>
      <td>159,838</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Reference denominator from unique LC GeneModel...</td>
    </tr>
    <tr>
      <th>23</th>
      <td>24</td>
      <td>GFF3-parsed total gene models</td>
      <td>266,752</td>
      <td></td>
      <td></td>
      <td></td>
      <td>HC + LC unique GFF3-parsed gene models</td>
    </tr>
    <tr>
      <th>24</th>
      <td>25</td>
      <td>HC gene model validation rate (%)</td>
      <td>97.66</td>
      <td>8.54</td>
      <td>74.48</td>
      <td>97.06</td>
      <td>Non-redundant validated HC gene models / GFF3-...</td>
    </tr>
    <tr>
      <th>25</th>
      <td>26</td>
      <td>LC gene model validation rate (%)</td>
      <td>87.06</td>
      <td>3.38</td>
      <td>41.94</td>
      <td>85.04</td>
      <td>Non-redundant validated LC gene models / GFF3-...</td>
    </tr>
    <tr>
      <th>26</th>
      <td>27</td>
      <td>Total gene model validation rate (%)</td>
      <td>91.31</td>
      <td>5.45</td>
      <td>54.98</td>
      <td>89.86</td>
      <td>Non-redundant validated total gene models / GF...</td>
    </tr>
  </tbody>
</table>
</div>


# End of notebook
