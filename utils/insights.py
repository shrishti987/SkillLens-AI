def generate_ai_insights(df):

    insights = []

    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(include='object').columns

    # numeric insights
    for col in numeric_cols:

        mean = round(df[col].mean(),2)
        max_val = df[col].max()
        min_val = df[col].min()

        insights.append(f"{col} average value is {mean}")
        insights.append(f"{col} ranges between {min_val} and {max_val}")

    # categorical insights
    for col in categorical_cols[:3]:

        top = df[col].value_counts().idxmax()

        insights.append(f"Most frequent value in {col} is {top}")

    # correlations
    if len(numeric_cols) >= 2:

        corr = df[numeric_cols].corr().iloc[0,1]

        insights.append(f"There is a correlation of {round(corr,2)} between {numeric_cols[0]} and {numeric_cols[1]}")

    return insights