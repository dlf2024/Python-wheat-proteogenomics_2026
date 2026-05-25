# Software Versions

This document summarises the primary software tools, packages, and computational environment used in the wheat proteogenomics workflow.

---

## Operating System

- Windows 11 Pro
- WSL2 Ubuntu

---

## Python Environment

- Python 3.11
- JupyterLab 4+

---

## Python Packages

Key packages used throughout the workflow:

| Package | Purpose |
|---|---|
| pandas | Data manipulation |
| numpy | Numerical analysis |
| scipy | Statistical calculations |
| scikit-learn | Machine learning and clustering |
| matplotlib | Static visualisation |
| seaborn | Statistical plotting |
| plotly | Interactive visualisation |
| upsetplot | UpSet overlap visualisation |
| biopython | FASTA and sequence handling |
| pysam | Genomic coordinate processing |
| pybedtools | BED file operations |
| gffutils | GFF3 parsing |
| tqdm | Progress tracking |

---

## Proteomics Software

### FragPipe

Used for peptide identification and protein inference.

Key integrated tools:
- MSFragger
- Philosopher
- IonQuant

Typical workflow:
- DDA timsTOF-PASEF searches
- Semi-tryptic peptide identification
- Variable PTM searches

---

## Mass Spectrometry Utilities

### ProteoWizard MSConvert

Used for:
- RAW conversion
- mzML generation
- mzXML compatibility handling

---

## Genome and Annotation Resources

### Wheat Reference Genome

- IWGSC RefSeq v2.1

### Annotation Files

- HC GFF3 annotation
- LC GFF3 annotation
- HC peptide FASTA
- LC peptide FASTA

---

## Proteogenomics Utilities

### BLAST+

Used for:
- tblastn peptide-to-genome rescue searches

### Galaxy Proteomics

Used for:
- tblastn execution
- large-scale peptide rescue workflows

https://proteomics.usegalaxy.eu

---

## Visualisation Platforms

### Apollo JBrowse

Used for:
- peptide genome coordinate visualisation
- BED6/BED12 track rendering

https://bread-wheat-um.genome.edu.au/apollo/49826/jbrowse/index.html

---

## Version Notes

Exact minor package versions may vary slightly across executions due to ongoing development and workflow optimisation.

The provided `environment.yml` file contains the recommended reproducible computational environment for rerunning the workflow.