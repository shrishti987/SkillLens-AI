import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def run_deep_learning(df):

    # Select only numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    # Check if dataset has enough numeric columns
    if len(numeric_cols) < 2:
        return "Not enough numeric data for deep learning"

    # Select target column (last numeric column)
    target = numeric_cols[-1]

    # Features and target
    X = df[numeric_cols].drop(columns=[target])
    y = df[target]

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    # Feature scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Build Neural Network
    model = Sequential()

    model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1))

    # Compile model
    model.compile(
        optimizer='adam',
        loss='mse'
    )

    # Train model
    model.fit(
        X_train,
        y_train,
        epochs=25,
        batch_size=32,
        verbose=0
    )

    # Evaluate model
    loss = model.evaluate(
        X_test,
        y_test,
        verbose=0
    )

    return target, round(loss, 4)