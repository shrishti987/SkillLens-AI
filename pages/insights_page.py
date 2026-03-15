import streamlit as st
import pandas as pd

with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ## AI Generated Insights

        """)

    with col2:
        st.image("assets/ai.svg", width=260)

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state["df"]

    insights = []

    numeric_cols = df.select_dtypes(include="number").columns

    # Basic dataset insight
    insights.append(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

    # Missing values insight
    missing = df.isnull().sum().sum()
    if missing > 0:
        insights.append(f"There are {missing} missing values in the dataset.")
    else:
        insights.append("No missing values detected.")

    # Numeric column insights
    if len(numeric_cols) > 0:

        highest_mean_col = df[numeric_cols].mean().idxmax()
        insights.append(f"{highest_mean_col} has the highest average value.")

        highest_var_col = df[numeric_cols].var().idxmax()
        insights.append(f"{highest_var_col} shows the highest variability.")

    # Correlation insight
    if len(numeric_cols) >= 2:

        corr = df[numeric_cols].corr().abs()

        # remove self correlation
        for i in range(len(corr)):
            corr.iloc[i, i] = 0

        max_corr = corr.max().max()

        if max_corr > 0.7:
            col_pair = corr.stack().idxmax()
            insights.append(f"Strong correlation detected between {col_pair[0]} and {col_pair[1]}.")

    # DISPLAY INSIGHTS
    if len(insights) == 0:
        st.warning("No insights could be generated from the dataset.")
    else:
        for insight in insights:
            st.write("•", insight)