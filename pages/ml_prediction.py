import streamlit as st
from utils.prediction import sales_prediction
from utils.automl import run_automl
from utils.deep_learning import run_deep_learning

with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ##  Machine Learning Predictions
        
        Train predictive models on your dataset and discover patterns using AI.
        InsightAI automatically prepares data and runs machine learning models.
        """)

    with col2:
        st.image("assets/ml.svg", width=260)

# Check dataset
if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state["df"]

    if df is None or df.empty:
        st.warning("Uploaded dataset is empty.")
    else:
        st.write("Run machine learning models on your dataset to generate predictions.")

        st.divider()

        # -----------------------
        # Basic Prediction
        # -----------------------
        st.subheader("📈 Sales / Value Prediction")

        prediction = sales_prediction(df)

        st.success(f"Predicted Future Revenue: {prediction}")

        st.divider()

        # -----------------------
        # AutoML Model Selection
        # -----------------------
        st.subheader("⚙️ AutoML Model Selection")

        best_model, scores = run_automl(df)

        st.write("Best Model Selected:", best_model)

        st.write("Model Performance Scores")
        st.dataframe(scores)

        st.divider()

        # -----------------------
        # Deep Learning Model
        # -----------------------
        st.subheader("🧠 Deep Learning Model")

        dl_result = run_deep_learning(df)

        st.write("Neural Network Loss:", dl_result)

        st.info("Lower loss indicates better model performance.")