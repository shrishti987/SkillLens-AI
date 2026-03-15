def recommend_analysis(df):

    columns = [c.lower() for c in df.columns]
    if any("revenue" in c or "sales" in c for c in columns):
        return "Sales dataset detected. Revenue trend and forecasting recommended."

    if any("age" in c or "patient" in c for c in columns):
        return "Healthcare dataset detected. Patient demographics analysis recommended."

    if any("price" in c or "stock" in c for c in columns):
        return "Finance dataset detected. Risk and price trend analysis recommended."

    return "General dataset detected. Standard EDA recommended."