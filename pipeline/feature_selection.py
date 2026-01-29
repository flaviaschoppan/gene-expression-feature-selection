import pandas as pd

def compute_gene_variance(matrix: pd.DataFrame) -> pd.Series:
    """
    Compute variance of each gene across samples.

    Input:
        matrix: pd.DataFrame
            • rows = genes
            • columns = samples
    
    Output:
        variances: pd.Series
            • index = gene names
            • values = variance across samples
    """

    variances = matrix.var(axis=1)
    return variances

def select_top_variable_genes(matrix: pd.DataFrame, n_genes: int) -> pd.DataFrame:
    """
    Select the top N most variable genes.

    Input:
        matrix: pd.DataFrame
            • rows = genes
            • columns = samples
        n_genes: int
            • Number of genes to keep
    
    Output:
        Filtered matrix with only the top variable genes.
    """

    variances = compute_gene_variance(matrix)
    top_genes = variances.sort_values(ascending=False).head(n_genes).index
    filtered_matrix = matrix.loc[top_genes]
    return filtered_matrix