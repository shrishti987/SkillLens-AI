import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def generate_visualizations(df):

    numeric = df.select_dtypes(include="number")

    if numeric.shape[1] > 1:

        st.write("Correlation Heatmap")

        fig, ax = plt.subplots()

        sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", ax=ax)

        st.pyplot(fig)

    for col in numeric.columns:

        st.write(f"Distribution of {col}")

        fig, ax = plt.subplots()

        sns.histplot(df[col], kde=True, ax=ax)

        st.pyplot(fig)