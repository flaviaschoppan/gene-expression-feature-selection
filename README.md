# Gene Expression Feature Selection Pipeline

---

## Overview

This repository implements a minimal, explicit, and reproducible pipeline to compute and inspect gene-wise variance in gene expression data.

The pipeline formalizes an intermediate analytical stage commonly used in transcriptomics workflows: quantifying variability across genes before any feature filtering, clustering, or dimensionality reduction is applied.

The focus of this project is strictly on variance computation and inspection, treating gene-wise variability as an explicit analytical object.

---

## What this pipeline does

1. Loads a raw gene expression count matrix
2. Normalizes counts to CPM (Counts Per Million)
3. Applies log2(x + 1) transformation
4. Computes gene-wise variance across samples
5. Saves the variance table as a versioned artifact
6. Generates a distribution plot of gene-wise variance

---

## Why this matters

Many downstream transcriptomics analyses rely implicitly on variance-based assumptions, such as:

• Low-variance genes being uninformative
• High-variance genes contributing disproportionately to structure and signal

Despite this, the global distribution of gene-wise variance is often not inspected explicitly, and filtering thresholds are frequently chosen without quantitative justification.

This pipeline makes variance computation and inspection explicit, enabling informed decisions about subsequent feature selection steps.

---

## What this project is NOT

• This is not a differential expression analysis
• This is not a clustering pipeline
• This is not a dimensionality reduction pipeline

No genes are filtered or removed in this stage.
The pipeline deliberately stops before feature selection.

---

## Conceptual focus

> Variance computation and inspection should precede any feature filtering or dimensionality reduction.

This project isolates gene-wise variance as a standalone analytical step.

---

## Project structure

gene-expression-feature-selection/
├── data/
│   └── raw/
│       └── counts.csv
├── pipeline/
│   ├── __init__.py
│   ├── io.py
│   ├── normalization.py
│   ├── transform.py
│   ├── feature_selection.py
│   └── plots.py
├── outputs/
│   ├── matrices/
│   └── figures/
├── run_pipeline.py
├── requirements.txt
├── README.md
└── LICENSE

---

## Outputs

The pipeline produces the following versionable artifacts:
```
outputs/matrices/gene_variances.csv
outputs/figures/gene_variance_distribution.png
```
• The CSV contains per-gene variance values computed on log2 CPM data
• The PNG visualizes the global distribution of gene-wise variance

---

## How to run

1. Install dependencies: ```pip install -r requirements.txt```

2. Run the pipeline: ```python run_pipeline.py```

All outputs will be written to the ```outputs/``` folder.

---

## Reproducibility

All steps in this pipeline are:
• Explicit
• Deterministic
• Scripted
• And produce versionable artifacts

The pipeline is designed to be inspectable, auditable, and easily extensible.

---

## Data note

The data used in this repository are synthetic and intended solely to demonstrate:

• The numerical behavior of variance computation
• The structure of a feature inspection workflow

They are not intended for biological interpretation.

---

## License

This project is released under the MIT License.