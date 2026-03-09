from sklearn.linear_model import LinearRegression
import numpy as np

def sales_prediction(df):

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) < 2:
        return "Not enough numeric data for prediction"

    X = df[[numeric_cols[0]]]
    y = df[numeric_cols[1]]

    model = LinearRegression()

    model.fit(X,y)

    future = np.array([[X.mean()[0]]])

    prediction = model.predict(future)

    return round(prediction[0],2)

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def auto_ml_prediction(df):

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) < 2:
        return "Not enough numeric columns for prediction"

    target = numeric_cols[-1]

    X = df[numeric_cols].drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)

    return target, score, model.coef_