import streamlit as st
import pandas as pd

from utils.data_cleaning import clean_data
from utils.insights import generate_ai_insights
from utils.prediction import sales_prediction
from utils.charts import generate_charts

# Page config
st.set_page_config(page_title="InsightAI", layout="wide")

# App title
st.title("InsightAI – Analyst in a Box")
st.write("Upload a dataset and get instant insights.")

# File upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:

    # Read dataset
    df = pd.read_csv(uploaded_file)

    # Sidebar info
    st.sidebar.header("Dataset Info")
    st.sidebar.write("Rows:", df.shape[0])
    st.sidebar.write("Columns:", df.shape[1])

    # Data Cleaning
    df, cleaning_report = clean_data(df)

    # Show cleaning report
    st.sidebar.subheader("Cleaning Report")
    st.sidebar.write(cleaning_report)

    # Dataset preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.write("Dataset Shape:", df.shape)
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    col4.metric("Duplicate Rows", df.duplicated().sum())

    # Exploratory Data Analysis
    st.header("Exploratory Data Analysis")

    if not df.empty:
        generate_charts(df)
    else:
        st.warning("Dataset is empty after cleaning.")

    # AI Insights
    st.header("AI Generated Insights")

    insights = generate_ai_insights(df)

    if insights:
        for i in insights:
            st.write("•", i)
    else:
        st.info("No insights generated.")

    # Predictive Analytics
    st.header("Predictive Analytics")

    prediction = sales_prediction(df)

    st.write("Predicted Future Revenue:", prediction)