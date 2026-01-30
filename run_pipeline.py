"""
Gene Expression Feature Selection Pipeline

This script implements a minimal and explicit pipeline to compute
gene-wise variance from a gene expression matrix.

Steps:
1. Load raw counts
2. CPM normalization
3. Log2 transformation
4. Compute per-gene variance
5. Save variance table
6. Plot variance distribution

The goal is to prepare the ground for feature selection,
not to perform filtering yet.
"""

from pipeline.io import load_counts
from pipeline.normalization import cpm
from pipeline.transform import log2_transform
from pipeline.feature_selection import compute_gene_variance
from pipeline.plots import plot_gene_variance_distribution


def main():
    # ---------------------------------------------------
    # Step 1 - Load data
    # ---------------------------------------------------
    print("Loading raw counts...")
    counts = load_counts("data/raw/counts.csv")
    print("✓ Step 1 finished: data loaded\n")

    # ---------------------------------------------------
    # Step 2 - Normalize
    # ---------------------------------------------------
    print("Applying CPM normalization...")
    cpm_matrix = cpm(counts)
    print("✓ Step 2 finished: CPM normalization applied\n")

    # ---------------------------------------------------
    # Step 3 - Log transform
    # ---------------------------------------------------
    print("Applying log2 transformation...")
    log_matrix = log2_transform(cpm_matrix)
    print("✓ Step 3 finished: log2 transformation applied\n")

    # ---------------------------------------------------
    # Step 4 - Compute gene-wise variance
    # ---------------------------------------------------
    print("Computing gene-wise variance...")
    variances = compute_gene_variance(log_matrix)
    print("✓ Step 4 finished: gene-wise variance computed\n")

    # ---------------------------------------------------
    # Step 5 - Save results
    # ---------------------------------------------------
    print("Saving variance table...")
    variances.to_csv("outputs/matrices/gene_variances.csv")
    print("✓ Step 5 finished: variance table saved\n")

    # ---------------------------------------------------
    # Step 6 - Plot variance distribution
    # ---------------------------------------------------
    print("Plotting variance distribution...")
    plot_gene_variance_distribution(
        variances,
        outpath="outputs/figures/gene_variance_distribution.png"
    )
    print("✓ Step 6 finished: variance distribution plotted\n")

    print("Pipeline finished successfully.")


if __name__ == "__main__":
    main()