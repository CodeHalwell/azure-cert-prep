"""
Scoring script for model inference.
"""

import json
import joblib
import pandas as pd


def init():
    """Initialize the model."""
    global model
    model_path = "model.pkl"  # Azure ML will provide actual path
    model = joblib.load(model_path)


def run(raw_data: str) -> str:
    """Score input data and return predictions."""
    data = json.loads(raw_data)
    
    # Convert to DataFrame
    df = pd.DataFrame(data if isinstance(data, list) else [data])
    
    # Ensure correct feature order
    feature_columns = [
        'temperature', 'vibration', 'pressure', 'operational_hours',
        'temperature_rolling_mean', 'temperature_rolling_std',
        'vibration_rolling_mean', 'vibration_rolling_std',
        'pressure_rolling_mean', 'pressure_rolling_std',
    ]
    
    # Add missing rolling features with defaults
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0.0
    
    X = df[feature_columns]
    
    # Get predictions and probabilities
    predictions = model.predict(X)
    probabilities = model.predict_proba(X)[:, 1]
    
    results = []
    for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
        risk_level = "high" if prob > 0.7 else "medium" if prob > 0.3 else "low"
        results.append({
            "prediction": int(pred),
            "failure_probability": float(prob),
            "risk_level": risk_level,
        })
    
    return json.dumps(results)


if __name__ == "__main__":
    # Test locally
    init()
    
    test_data = json.dumps([{
        "temperature": 75.0,
        "vibration": 0.45,
        "pressure": 98.0,
        "operational_hours": 2500,
        "temperature_rolling_mean": 73.0,
        "temperature_rolling_std": 2.5,
        "vibration_rolling_mean": 0.42,
        "vibration_rolling_std": 0.05,
        "pressure_rolling_mean": 99.0,
        "pressure_rolling_std": 1.2,
    }])
    
    result = run(test_data)
    print(result)
