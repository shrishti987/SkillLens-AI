def generate_ai_insights(df):

    insights = []

    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(include='object').columns


    # -------------------
    # Numeric Insights
    # -------------------
    for col in numeric_cols:

        mean = round(df[col].mean(), 2)
        max_val = df[col].max()
        min_val = df[col].min()

        insights.append(f"{col} average value is {mean}")
        insights.append(f"{col} ranges between {min_val} and {max_val}")


    # -------------------
    # Categorical Insights
    # -------------------
    for col in categorical_cols[:3]:

        if not df[col].value_counts().empty:
            top = df[col].value_counts().idxmax()
            insights.append(f"Most frequent value in {col} is {top}")


    # -------------------
    # Correlation Insight
    # -------------------
    if len(numeric_cols) >= 2:

        corr_matrix = df[numeric_cols].corr().abs()

        # remove self correlation
        corr_matrix.values[[range(len(corr_matrix))]*2] = 0

        max_corr_pair = corr_matrix.unstack().idxmax()
        corr_value = corr_matrix.unstack().max()

        insights.append(
            f"Strong correlation detected between {max_corr_pair[0]} and {max_corr_pair[1]} ({round(corr_value,2)})"
        )


    return insights