import streamlit as st

# ---------------------------
# HERO SECTION
# ---------------------------
with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ## Welcome to InsightAI
        
        InsightAI is an AI-powered data analytics platform that helps you explore,
        visualize, and understand datasets effortlessly.

        Upload a CSV dataset to generate automated insights, interactive
        visualizations, machine learning predictions, and analytical reports.
        """)

    with col2:
        st.image("assets/insight.svg", width=260)

st.divider()


# ---------------------------
# HOW TO USE
# ---------------------------
st.subheader("How to Use")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("""
        **Step 1**

        Upload a CSV dataset using the sidebar uploader.
        """)

with col2:
    with st.container(border=True):
        st.markdown("""
        **Step 2**

        Navigate through the analysis pages to explore the dataset.
        """)

with col3:
    with st.container(border=True):
        st.markdown("""
        **Step 3**

        Generate insights, visualizations, and predictions.
        """)

st.divider()


# ---------------------------
# SUPPORTED DATA TYPES
# ---------------------------
st.subheader("Supported Dataset Types")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("""
        **Business Data**

        Sales, revenue, transactions, and operational data.
        """)

with col2:
    with st.container(border=True):
        st.markdown("""
        **Healthcare Data**

        Patient statistics, medical analytics, and health metrics.
        """)

with col3:
    with st.container(border=True):
        st.markdown("""
        **Marketing Data**

        Campaign analytics, customer insights, and performance metrics.
        """)

st.divider()


# ---------------------------
# FEATURES
# ---------------------------
st.subheader("Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("""
        **Exploratory Data Analysis**

        Automatically generate statistical summaries and charts.
        """)

with col2:
    with st.container(border=True):
        st.markdown("""
        **AI Insights**

        Identify patterns, correlations, and key observations.
        """)

with col3:
    with st.container(border=True):
        st.markdown("""
        **Machine Learning**

        Train predictive models directly on your dataset.
        """)

st.divider()

st.info("Upload a dataset from the sidebar to begin analysis.")
