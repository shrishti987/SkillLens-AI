from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import pandas as pd


# -------------------------------
# PDF REPORT GENERATOR
# -------------------------------
def create_pdf_report(summary, cleaning_report):

    buffer = io.BytesIO()

    c = canvas.Canvas(buffer, pagesize=letter)

    y = 750

    c.drawString(200, y, "InsightAI Analysis Report")

    y -= 40
    c.drawString(50, y, "Data Cleaning Summary:")
    y -= 20

    for item in cleaning_report:
        c.drawString(60, y, str(item))
        y -= 20

    y -= 20
    c.drawString(50, y, "Dataset Information")
    y -= 20

    c.drawString(60, y, f"Rows: {summary['shape'][0]}")
    y -= 20
    c.drawString(60, y, f"Columns: {summary['shape'][1]}")

    y -= 40
    c.drawString(50, y, "Columns Detected:")
    y -= 20

    for col in summary["columns"]:
        c.drawString(60, y, str(col))
        y -= 20

    c.save()

    buffer.seek(0)

    return buffer


# -------------------------------
# AI SUMMARY REPORT (NEW FEATURE)
# -------------------------------
def generate_report(df):

    report = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum(),
        "Numeric Columns": len(df.select_dtypes(include="number").columns),
        "Categorical Columns": len(df.select_dtypes(include="object").columns)
    }

    report_df = pd.DataFrame(
        list(report.items()),
        columns=["Metric", "Value"]
    )

    return report_df