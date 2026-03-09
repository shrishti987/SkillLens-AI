def clean_data(df):

    report = []

    missing = df.isnull().sum().sum()

    if missing > 0:
        df = df.fillna(df.median(numeric_only=True))
        report.append("Missing values filled")

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        df = df.drop_duplicates()
        report.append("Duplicates removed")

    return df, report