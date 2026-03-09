import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

def detect_target(df):

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) == 0:
        return None

    # assume last numeric column is target
    return numeric_cols[-1]

def generate_charts(df):

    if df is None or df.empty:
        st.warning("Dataset is empty. No charts to display.")
        return

    st.subheader("Exploratory Data Analysis")

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

    # -----------------------------
    # 1 Histogram for numeric cols
    # -----------------------------
    if numeric_cols:

        st.markdown("### Numeric Distributions")

        for col in numeric_cols:

            try:
                fig = px.histogram(df, x=col, title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)

            except Exception as e:
                st.warning(f"Could not generate histogram for {col}")

    # -----------------------------
    # 2 Boxplots for outliers
    # -----------------------------
    if numeric_cols:

        st.markdown("### Outlier Detection")

        for col in numeric_cols:

            try:
                fig = px.box(df, y=col, title=f"Outliers in {col}")
                st.plotly_chart(fig, use_container_width=True)

            except:
                st.warning(f"Could not generate boxplot for {col}")

    # -----------------------------
    # 3 Correlation Heatmap
    # -----------------------------
    if len(numeric_cols) > 1:

        try:
            st.markdown("### Correlation Heatmap")

            fig, ax = plt.subplots()

            corr = df[numeric_cols].corr()

            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

            st.pyplot(fig)

        except:
            st.warning("Could not generate correlation heatmap.")

    # -----------------------------
# Missing Value Heatmap
# -----------------------------

    if df.isnull().sum().sum() > 0:

        st.markdown("### Missing Values Heatmap")

        fig, ax = plt.subplots()

        sns.heatmap(df.isnull(), cbar=False, cmap="viridis")

        st.pyplot(fig)

    # -----------------------------
    # 4 Bar charts for categorical
    # -----------------------------
    if categorical_cols:

        st.markdown("### Categorical Distributions")

        for col in categorical_cols[:4]:  # limit to avoid overload

            try:

                counts = df[col].value_counts().reset_index()
                counts.columns = [col, "count"]

                # limit categories if too many
                counts = counts.head(20)

                fig = px.bar(
                    counts,
                    x=col,
                    y="count",
                    title=f"Count of {col}"
                )

                st.plotly_chart(fig, use_container_width=True)

            except:
                st.warning(f"Could not generate bar chart for {col}")

    # -----------------------------
    # 5 Scatter plots relationships
    # -----------------------------
    if len(numeric_cols) >= 2:

        try:

            st.markdown("### Variable Relationships")

            fig = px.scatter(
                df,
                x=numeric_cols[0],
                y=numeric_cols[1],
                title=f"{numeric_cols[0]} vs {numeric_cols[1]}"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            st.warning("Could not generate scatter plot.")

        # -----------------------------
    # 5 Scatter plots relationships
    # -----------------------------
    if len(numeric_cols) >= 2:

        try:

            st.markdown("### Variable Relationships")

            fig = px.scatter(
                df,
                x=numeric_cols[0],
                y=numeric_cols[1],
                title=f"{numeric_cols[0]} vs {numeric_cols[1]}"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            st.warning("Could not generate scatter plot.")


    # -----------------------------
    # Feature Importance
    # -----------------------------
    if len(numeric_cols) >= 2:

        try:

            st.markdown("### Feature Importance")

            target = numeric_cols[-1]

            X = df[numeric_cols].drop(columns=[target])
            y = df[target]

            model = RandomForestRegressor()

            model.fit(X, y)

            importance = pd.DataFrame({
                "Feature": X.columns,
                "Importance": model.feature_importances_
            })

            fig = px.bar(
                importance,
                x="Feature",
                y="Importance",
                title="Feature Importance"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            st.warning("Feature importance could not be generated.")


    # -----------------------------
    # 6 Pairplot (advanced EDA)
    # -----------------------------
    if len(numeric_cols) >= 3 and len(df) < 2000:

        try:

            st.markdown("### Pairwise Relationships")

            pairplot = sns.pairplot(df[numeric_cols[:4]])

            st.pyplot(pairplot)

        except:
            st.warning("Pairplot could not be generated.")
