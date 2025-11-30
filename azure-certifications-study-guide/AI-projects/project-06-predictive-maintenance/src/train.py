"""
Machine learning model training for predictive maintenance.
"""

import argparse
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import joblib
import mlflow
import mlflow.sklearn


def load_data(data_path: str) -> pd.DataFrame:
    """Load and prepare training data."""
    df = pd.read_csv(data_path)
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create features for the model."""
    # Sort by device and time
    df = df.sort_values(['device_id', 'timestamp'])
    
    # Rolling statistics (by device)
    for col in ['temperature', 'vibration', 'pressure']:
        df[f'{col}_rolling_mean'] = df.groupby('device_id')[col].transform(
            lambda x: x.rolling(window=10, min_periods=1).mean()
        )
        df[f'{col}_rolling_std'] = df.groupby('device_id')[col].transform(
            lambda x: x.rolling(window=10, min_periods=1).std()
        )
    
    # Fill NaN from rolling calculations
    df = df.fillna(0)
    
    return df


def train_model(X: pd.DataFrame, y: pd.Series) -> RandomForestClassifier:
    """Train a Random Forest classifier."""
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X, y)
    return model


def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Evaluate model performance."""
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    
    report = classification_report(y_test, predictions, output_dict=True)
    roc_auc = roc_auc_score(y_test, probabilities)
    
    return {
        "accuracy": report["accuracy"],
        "precision": report["1"]["precision"],
        "recall": report["1"]["recall"],
        "f1_score": report["1"]["f1-score"],
        "roc_auc": roc_auc,
    }


def main(data_path: str, output_path: str):
    """Main training pipeline."""
    
    # Start MLflow run
    with mlflow.start_run():
        # Load and prepare data
        print("Loading data...")
        df = load_data(data_path)
        df = engineer_features(df)
        
        # Define features and target
        feature_columns = [
            'temperature', 'vibration', 'pressure', 'operational_hours',
            'temperature_rolling_mean', 'temperature_rolling_std',
            'vibration_rolling_mean', 'vibration_rolling_std',
            'pressure_rolling_mean', 'pressure_rolling_std',
        ]
        
        X = df[feature_columns]
        y = df['failure']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Train model
        print("Training model...")
        model = train_model(X_train, y_train)
        
        # Evaluate
        print("Evaluating model...")
        metrics = evaluate_model(model, X_test, y_test)
        
        # Log to MLflow
        mlflow.log_params({
            "n_estimators": 100,
            "max_depth": 10,
        })
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, "model")
        
        # Save locally
        joblib.dump(model, output_path)
        print(f"Model saved to {output_path}")
        
        print("Metrics:")
        for name, value in metrics.items():
            print(f"  {name}: {value:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-path", required=True, help="Path to training data CSV")
    parser.add_argument("--output-path", default="model.pkl", help="Output model path")
    
    args = parser.parse_args()
    main(args.data_path, args.output_path)
