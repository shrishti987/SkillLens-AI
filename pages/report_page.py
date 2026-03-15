import streamlit as st
from utils.report_generator import generate_report

with st.container(border=True):

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ## 📄 AI Generated Report
        
        Generate a complete AI-powered report from your dataset.
        Export insights, statistics, and findings in one place.
        """)

    with col2:
        st.image("assets/report.svg", width=260)

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state["df"]

    if df is None or df.empty:
        st.warning("Uploaded dataset is empty.")
    else:
        st.write("Generate a complete AI analysis report for your dataset.")

        st.divider()

        # Generate report
        report = generate_report(df)

        st.subheader("Report Preview")

        st.dataframe(report)

        st.divider()

        # Convert to CSV for download
        csv = report.to_csv(index=False).encode()

        st.download_button(
            label="⬇ Download AI Report",
            data=csv,
            file_name="ai_report.csv",
            mime="text/csv"
        )