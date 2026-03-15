import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

def run_automl(df):

    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) < 2:
        return "Not enough numeric columns"

    target = numeric_cols[-1]

    X = df[numeric_cols].drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        "Decision Tree": DecisionTreeRegressor(random_state=42)
    }

    scores = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        scores[name] = r2_score(y_test, pred)

    best_model = max(scores, key=scores.get)

    return best_model, scores