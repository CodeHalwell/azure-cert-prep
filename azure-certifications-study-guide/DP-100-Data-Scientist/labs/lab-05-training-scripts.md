# Lab 05: Train Models with Custom Scripts

## 🎯 Lab Goal

Train models using **custom Python scripts** in Azure ML:

- Create training scripts
- Submit command jobs
- Log metrics and artifacts

This supports the **Train models** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace with compute cluster
- Data asset from Lab 03

---

## Step 1 – Create Training Script

Create `src/train.py`:

```python
import argparse
import os
import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

def main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=5)
    parser.add_argument("--output", type=str, default="./outputs")
    args = parser.parse_args()

    # Enable MLflow autologging
    mlflow.sklearn.autolog()

    # Load data
    print(f"Loading data from: {args.data}")
    df = pd.read_csv(args.data)

    # Prepare features
    X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].fillna(0)
    y = df['Survived']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    print(f"Training with n_estimators={args.n_estimators}, max_depth={args.max_depth}")
    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth,
        random_state=42
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    # Log custom metrics
    mlflow.log_metric("test_accuracy", accuracy)
    mlflow.log_metric("test_precision", precision)
    mlflow.log_metric("test_recall", recall)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

    # Save model
    os.makedirs(args.output, exist_ok=True)
    mlflow.sklearn.save_model(model, os.path.join(args.output, "model"))
    print(f"Model saved to {args.output}")

if __name__ == "__main__":
    main()
```

---

## Step 2 – Submit Command Job

```python
from azure.ai.ml import command, Input

job = command(
    code="./src",
    command="python train.py --data ${{inputs.training_data}} --n-estimators 100 --max-depth 5",
    inputs={
        "training_data": Input(
            type="uri_file",
            path="azureml:titanic-cleaned@latest"
        )
    },
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
    compute="cpu-cluster",
    display_name="titanic-rf-training",
    experiment_name="titanic-classification"
)

returned_job = ml_client.jobs.create_or_update(job)
print(f"Job submitted: {returned_job.studio_url}")
```

---

## Step 3 – Monitor Job in Studio

1. Click the job URL to open in Azure ML Studio.
2. View:
   - **Overview** – Status and duration
   - **Metrics** – Logged metrics and charts
   - **Outputs + logs** – stdout, stderr, model files
   - **Code** – Submitted scripts

---

## Step 4 – Wait for Job Completion

```python
from azure.ai.ml.entities import Job

# Wait for completion
ml_client.jobs.stream(returned_job.name)

# Or poll status
job_status = ml_client.jobs.get(returned_job.name)
print(f"Status: {job_status.status}")
```

---

## Step 5 – Hyperparameter Sweep

```python
from azure.ai.ml.sweep import Choice, Uniform

job_for_sweep = command(
    code="./src",
    command="python train.py --data ${{inputs.training_data}} --n-estimators ${{inputs.n_estimators}} --max-depth ${{inputs.max_depth}}",
    inputs={
        "training_data": Input(type="uri_file", path="azureml:titanic-cleaned@latest"),
        "n_estimators": Choice(values=[50, 100, 200]),
        "max_depth": Choice(values=[3, 5, 10, None])
    },
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
    compute="cpu-cluster"
)

sweep_job = job_for_sweep.sweep(
    sampling_algorithm="random",
    primary_metric="test_accuracy",
    goal="maximize",
    max_total_trials=12,
    max_concurrent_trials=4
)

sweep_job.display_name = "titanic-rf-sweep"
sweep_job.experiment_name = "titanic-classification"

returned_sweep = ml_client.jobs.create_or_update(sweep_job)
print(f"Sweep job: {returned_sweep.studio_url}")
```

---

## Step 6 – Get Best Model from Sweep

```python
# After sweep completes
ml_client.jobs.stream(returned_sweep.name)

# Download best model
ml_client.jobs.download(
    name=returned_sweep.name,
    download_path="./best_model",
    output_name="outputs"
)
```

---

## ✅ Lab Checklist

- [ ] Created training script with argument parsing
- [ ] Used MLflow for metric logging
- [ ] Submitted command job to compute cluster
- [ ] Monitored job in Azure ML Studio
- [ ] Ran hyperparameter sweep
- [ ] Retrieved best model from sweep
