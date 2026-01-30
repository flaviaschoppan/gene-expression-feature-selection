import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="talk")

def plot_gene_variance_distribution(
    variances: pd.Series,
    outpath: str
):

    """
    Plot the distribution of gene-wise variance.

    Parameters
    -----------
    variances: ps.Series
        Gene-wise variance values.
        Index = gene names
        Values = variance
    
    outpath : str
    Path to save the figure.
    """

    plt.figure(figsize=(7, 6))

    sns.histplot(
        variances,
        bins=30,
        kde=True
    )

    plt.xlabel("Gene-wise variance (log2 CPM)")
    plt. ylabel("Number of genes")
    plt.title("Distribution of gene expression variance")

    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()