import streamlit as st
import pandas as pd
import plotly.express as px

with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ## Smart Visualizations
        
        Explore interative charts and uncover patterns in your dataset.
        """)

    with col2:
        st.image("assets/visualization.svg", width=260)

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state["df"]

    if df is None or df.empty:
        st.warning("Uploaded dataset is empty.")
    else:
        chart_type = st.selectbox(
            "Select Visualization Type",
            ["Scatter Plot", "Histogram", "Box Plot", "Correlation Heatmap"]
        )
        numeric_cols = df.select_dtypes(include="number").columns.tolist()

# Remove ID columns
        numeric_cols = [col for col in numeric_cols if "id" not in col.lower()]

        if len(numeric_cols) == 0:
            st.warning("No numeric columns available for visualization.")
        else:

            # ----------------------
            # Scatter Plot
            # ----------------------
            if chart_type == "Scatter Plot":

                st.subheader("Scatter Plot")

                if len(numeric_cols) < 2:
                    st.warning("Need at least 2 numeric columns for scatter plot.")
                else:
                    x_col = st.selectbox("Select X axis", numeric_cols)
                    y_col = st.selectbox("Select Y axis", numeric_cols)

                    scatter_df = df[[x_col, y_col]].dropna()

                    if scatter_df.empty:
                        st.warning("Not enough valid data.")
                    else:
                        fig = px.scatter(
                            scatter_df,
                            x=x_col,
                            y=y_col,
                            color_discrete_sequence=["#4F8BF9"]
                        )

                        with st.container(border=True):
                            st.plotly_chart(fig, use_container_width=True)

            # ----------------------
            # Histogram
            # ----------------------
            elif chart_type == "Histogram":

                st.subheader("Histogram")

                col = st.selectbox("Select Column", numeric_cols)

                fig = px.histogram(
                    df,
                    x=col,
                    nbins=30,
                    color_discrete_sequence=["#ff4d4d"]
                )

                with st.container(border=True):
                    st.plotly_chart(fig, use_container_width=True)

            # ----------------------
            # Box Plot
            # ----------------------
            elif chart_type == "Box Plot":

                st.subheader("Box Plot")

                col = st.selectbox("Select Column", numeric_cols)

                fig = px.box(
                    df,
                    y=col,
                    color_discrete_sequence=["#4F8BF9"]
                )

                with st.container(border=True):
                    st.plotly_chart(fig, use_container_width=True)

            # ----------------------
            # Correlation Heatmap
            # ----------------------
            elif chart_type == "Correlation Heatmap":

                st.subheader("Correlation Heatmap")

                if len(numeric_cols) < 2:
                    st.warning("Need at least 2 numeric columns.")
                else:
                    corr = df[numeric_cols].corr()

                    fig = px.imshow(
                        corr,
                        text_auto=True,
                        color_continuous_scale="RdBu"
                    )

                    with st.container(border=True):
                        st.plotly_chart(fig, use_container_width=True)