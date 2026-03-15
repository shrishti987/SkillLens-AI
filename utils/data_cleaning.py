def clean_data(df):

    report = []

    if df.isnull().sum().sum() > 0:

        num_cols = df.select_dtypes(include="number").columns
        cat_cols = df.select_dtypes(exclude="number").columns

        df[num_cols] = df[num_cols].fillna(df[num_cols].median())
        df[cat_cols] = df[cat_cols].fillna("Unknown")

        report.append("Missing values handled")

    if df.duplicated().sum() > 0:

        df = df.drop_duplicates()
        report.append("Duplicate rows removed")

    return df, report