import pandas as pd

def cpm(counts: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize raw counts to counts per million (CPM).

    Parameters
    -----------
    counts : pd.DataFrame
        Raw count matrix.
        Rows = genes, columns = samples.
    
    Returns
    ----------
    pd.DataFrame
        CPM-normalized matrix.
    """

    lib_sizes = counts.sum(axis=0)
    cpm_matrix = (counts / lib_sizes) * 1e6

    return cpm_matrix 