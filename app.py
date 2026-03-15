import streamlit as st
import pandas as pd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="InsightAI",
    layout="wide"
)

# ---------------------------
# MODERN UI STYLING
# ---------------------------
st.markdown("""
<style>

/* GLOBAL BACKGROUND */
.stApp {
    background: linear-gradient(135deg,#0f172a,#020617);
}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background: #020617;
    border-right: 1px solid #1e293b;
}

/* TITLES */
h1,h2,h3{
    color:#f8fafc;
}

/* TEXT */
p,label{
    color:#cbd5e1;
}

/* DATAFRAME */
[data-testid="stDataFrame"]{
    border-radius:12px;
}

/* CARD STYLE */
.ai-card{
    background:#020617;
    padding:25px;
    border-radius:14px;
    border:1px solid #1e293b;
    transition:0.25s;
}

.ai-card:hover{
    border:1px solid #3b82f6;
    transform:translateY(-4px);
}

/* BUTTON */
.stButton button{
    background:linear-gradient(90deg,#2563eb,#3b82f6);
    border:none;
    border-radius:8px;
    color:white;
    padding:10px 20px;
}

.stButton button:hover{
    background:linear-gradient(90deg,#1d4ed8,#2563eb);
}

/* KPI METRIC */
[data-testid="metric-container"]{
    background:#020617;
    border:1px solid #1e293b;
    padding:15px;
    border-radius:12px;
}

/* SCROLLBAR */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#334155;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# DATA LOADING FUNCTION
# ---------------------------
@st.cache_data
def load_data(file):
    try:
        df = pd.read_csv(file)
        df = df.loc[:, ~df.columns.duplicated()]

        if df.empty:
            st.error("Uploaded CSV has no data.")
            return None

        return df

    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty or not a valid CSV.")
        return None

    except Exception as e:
        st.error(f"Error reading file: {e}")
        return None


# ---------------------------
# HERO HEADER
# ---------------------------
with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        <h1 style='font-size:48px'>InsightAI – Smart Data Analyzer</h1>

        InsightAI is an AI-powered data analytics platform designed to help you 
        explore, visualize, and understand datasets effortlessly.

        Upload a dataset to generate automated insights, interactive visualizations,
        machine learning predictions, and detailed analytical reports.
        """, unsafe_allow_html=True)

    with col2:
        st.image("assets/main.svg", width=280)

st.divider()


# ---------------------------
# DATASET UPLOAD
# ---------------------------
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)

    if df is not None:
        st.session_state["df"] = df


# ---------------------------
# SIDEBAR DATASET INFO
# ---------------------------
if "df" in st.session_state:

    df = st.session_state["df"]

    st.sidebar.header("Dataset Info")

    st.sidebar.write("Rows:", df.shape[0])
    st.sidebar.write("Columns:", df.shape[1])

    st.sidebar.subheader("Preview")
    st.sidebar.dataframe(df.head())

else:
    st.sidebar.info("Upload a CSV file to begin.")


# ---------------------------
# DASHBOARD METRICS
# ---------------------------
if "df" in st.session_state:

    df = st.session_state["df"]

    st.subheader("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    col4.metric("Numeric Features", len(df.select_dtypes("number").columns))

    st.divider()

    st.subheader("Preview")

    st.dataframe(df.head(20), use_container_width=True)

else:

    st.info("Upload a dataset from the sidebar to begin analysis.")


# ---------------------------
# REAL TIME ANALYSIS
# ---------------------------
st.sidebar.header("Real Time Analysis")

auto_refresh = st.sidebar.checkbox("Enable Live Refresh")

if auto_refresh:
    st.rerun()

