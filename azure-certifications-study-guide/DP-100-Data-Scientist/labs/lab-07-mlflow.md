# Lab 07: Track Experiments with MLflow

## 🎯 Lab Goal

Use **MLflow** for experiment tracking in Azure ML:

- Log parameters, metrics, and artifacts
- Compare runs
- Register models from MLflow

This supports the **Train models** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace
- MLflow installed (`pip install mlflow azureml-mlflow`)

---

## Step 1 – Configure MLflow Tracking URI

```python
import mlflow
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Connect to workspace
ml_client = MLClient.from_config(DefaultAzureCredential())

# Get MLflow tracking URI
tracking_uri = ml_client.workspaces.get(ml_client.workspace_name).mlflow_tracking_uri

# Set MLflow tracking
mlflow.set_tracking_uri(tracking_uri)
print(f"Tracking URI: {tracking_uri}")
```

---

## Step 2 – Create an Experiment

```python
experiment_name = "titanic-mlflow"
mlflow.set_experiment(experiment_name)

print(f"Experiment: {mlflow.get_experiment_by_name(experiment_name)}")
```

---

## Step 3 – Log a Training Run

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# Load data
df = pd.read_csv("./data/titanic.csv")
X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].fillna(0)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Start MLflow run
with mlflow.start_run(run_name="rf-baseline"):
    # Log parameters
    n_estimators = 100
    max_depth = 5
    
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("model_type", "RandomForest")
    
    # Train model
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1)
    
    # Log model
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="titanic-rf"
    )
    
    print(f"Accuracy: {accuracy:.4f}, F1: {f1:.4f}")
    print(f"Run ID: {mlflow.active_run().info.run_id}")
```

---

## Step 4 – Log Artifacts

```python
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

with mlflow.start_run(run_name="rf-with-artifacts"):
    # ... training code ...
    
    # Create and log confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(cm)
    disp.plot()
    plt.savefig("confusion_matrix.png")
    mlflow.log_artifact("confusion_matrix.png")
    
    # Log feature importance
    importance_df = pd.DataFrame({
        "feature": X.columns,
        "importance": model.feature_importances_
    })
    importance_df.to_csv("feature_importance.csv", index=False)
    mlflow.log_artifact("feature_importance.csv")
    
    # Log entire folder
    mlflow.log_artifacts("./reports", artifact_path="reports")
```

---

## Step 5 – Use Autologging

```python
# Enable autologging for scikit-learn
mlflow.sklearn.autolog()

with mlflow.start_run(run_name="rf-autolog"):
    model = RandomForestClassifier(n_estimators=100, max_depth=5)
    model.fit(X_train, y_train)
    # Parameters, metrics, and model are logged automatically!
```

### Autolog Support:

| Framework | Command |
|-----------|--------|
| scikit-learn | `mlflow.sklearn.autolog()` |
| TensorFlow/Keras | `mlflow.tensorflow.autolog()` |
| PyTorch | `mlflow.pytorch.autolog()` |
| XGBoost | `mlflow.xgboost.autolog()` |
| LightGBM | `mlflow.lightgbm.autolog()` |

---

## Step 6 – Compare Runs

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Get experiment
experiment = client.get_experiment_by_name("titanic-mlflow")

# Search runs
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.accuracy DESC"],
    max_results=10
)

for run in runs:
    print(f"Run: {run.info.run_name}")
    print(f"  Accuracy: {run.data.metrics.get('accuracy', 'N/A'):.4f}")
    print(f"  Params: {run.data.params}")
```

---

## Step 7 – Register Model from Run

```python
# Register best model
best_run = runs[0]

model_uri = f"runs:/{best_run.info.run_id}/model"

registered_model = mlflow.register_model(
    model_uri=model_uri,
    name="titanic-production"
)

print(f"Registered: {registered_model.name} v{registered_model.version}")
```

---

## Step 8 – Load and Use Registered Model

```python
# Load model by name and version
model_name = "titanic-production"
model_version = 1

model = mlflow.sklearn.load_model(f"models:/{model_name}/{model_version}")

# Make predictions
predictions = model.predict(X_test)
print(f"Predictions: {predictions[:5]}")
```

---

## ✅ Lab Checklist

- [ ] Configured MLflow tracking URI for Azure ML
- [ ] Created and set experiment
- [ ] Logged parameters, metrics, and model
- [ ] Logged artifacts (plots, CSVs)
- [ ] Used autologging for scikit-learn
- [ ] Compared runs and found best model
- [ ] Registered model from MLflow run
