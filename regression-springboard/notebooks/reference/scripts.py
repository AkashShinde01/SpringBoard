"""Module for listing down additional custom functions required for the notebooks."""

import pandas as pd

def sales_dollar(df):
    """Bin the selling price column using quantiles."""
    return pd.qcut(df["sales_dollars_value"], q=10)