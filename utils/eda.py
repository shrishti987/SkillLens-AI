import pandas as pd


def generate_summary(df):

    summary = {}

    # Dataset shape
    summary["shape"] = df.shape

    # Column names
    summary["columns"] = list(df.columns)

    # Basic statistics
    try:
        summary["statistics"] = df.describe().to_dict()
    except:
        summary["statistics"] = {}

    # Correlation (only if more than 1 numeric column exists)
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] > 1:
        correlation = numeric_df.corr()
        summary["correlation"] = correlation.to_dict()
    else:
        summary["correlation"] = {}

    return summary