import pandas as pd

def generate_summary(df):

    summary = {}

    summary["shape"] = df.shape
    summary["columns"] = list(df.columns)

    summary["statistics"] = df.describe().to_dict()

    correlation = df.corr(numeric_only=True)

    summary["correlation"] = correlation.to_dict()

    return summary