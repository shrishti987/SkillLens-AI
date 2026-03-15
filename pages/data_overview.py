import streamlit as st
import pandas as pd

with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ## Data Overview
        Understand your dataset at a glance with automated summaries,
data previews, and statistical insights.
        """)

    with col2:
        st.image("assets/data.svg", width=260)

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state["df"]

    # Dataset shape
    st.subheader("Dataset Shape")
    rows, cols = df.shape
    st.write(f"Rows: {rows}")
    st.write(f"Columns: {cols}")

    # Preview dataset
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))

    # Column information
    st.subheader("Column Information")
    col_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.values,
        "Non-Null Count": df.count().values
    })
    st.dataframe(col_info)

    # Missing values
    st.subheader("Missing Values")
    missing_values = df.isnull().sum()
    missing_df = pd.DataFrame({
        "Column": missing_values.index,
        "Missing Values": missing_values.values
    })
    st.dataframe(missing_df)

    # Summary statistics
    st.subheader("Statistical Summary")
    st.dataframe(df.describe())