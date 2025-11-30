# Lab 06: Run AutoML Experiments

## 🎯 Lab Goal

Use **Automated Machine Learning (AutoML)** to find the best model:

- Configure AutoML jobs
- Analyze results and model explanations
- Register the best model

This supports the **Train models using AutoML** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace with compute cluster
- MLTable data asset

---

## Step 1 – Prepare Data as MLTable

AutoML requires MLTable format:

```python
import mltable
from mltable import MLTableHeaders, MLTableFileEncoding

# Create MLTable from CSV
paths = [{"file": "./data/titanic.csv"}]

table = mltable.from_delimited_files(
    paths,
    delimiter=",",
    header=MLTableHeaders.all_files_same_headers,
    encoding=MLTableFileEncoding.utf8
)

# Save MLTable artifact
table.save("./data/titanic-mltable")
```

---

## Step 2 – Register MLTable Data Asset

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

training_data = Data(
    name="titanic-automl",
    path="./data/titanic-mltable",
    type=AssetTypes.MLTABLE
)

ml_client.data.create_or_update(training_data)
```

---

## Step 3 – Configure Classification AutoML Job

```python
from azure.ai.ml import automl, Input

classification_job = automl.classification(
    compute="cpu-cluster",
    experiment_name="titanic-automl",
    training_data=Input(type="mltable", path="azureml:titanic-automl@latest"),
    target_column_name="Survived",
    primary_metric="accuracy",
    n_cross_validations=5,
    enable_model_explainability=True
)

# Set limits
classification_job.set_limits(
    timeout_minutes=60,
    trial_timeout_minutes=10,
    max_trials=20,
    max_concurrent_trials=4,
    enable_early_termination=True
)

# Set training options
classification_job.set_training(
    enable_onnx_compatible_models=True
)
```

---

## Step 4 – Configure Featurization

```python
from azure.ai.ml.automl import ColumnTransformer

classification_job.set_featurization(
    mode="auto",  # or "custom"
    blocked_transformers=["LabelEncoder"],
    column_name_and_types={
        "Pclass": "Categorical",
        "Sex": "Categorical",
        "Age": "Numerical",
        "Embarked": "Categorical"
    }
)
```

---

## Step 5 – Submit AutoML Job

```python
returned_job = ml_client.jobs.create_or_update(classification_job)
print(f"AutoML job: {returned_job.studio_url}")

# Wait for completion
ml_client.jobs.stream(returned_job.name)
```

---

## Step 6 – Analyze Results in Studio

1. Open the job in Azure ML Studio.
2. Explore:
   - **Models** tab – All trained models ranked by metric
   - **Data guardrails** – Data quality checks
   - **Metrics** – Comparison charts
3. Select the best model:
   - **Explanations** – Feature importance
   - **Metrics** – Confusion matrix, ROC curve

---

## Step 7 – Get Best Model Programmatically

```python
from azure.ai.ml.entities import Model

# Get best child run
best_run = ml_client.jobs.get(returned_job.name)
print(f"Best model: {best_run.properties.get('best_child_run_id')}")

# Download best model
ml_client.jobs.download(
    name=returned_job.name,
    download_path="./best_automl_model",
    output_name="best_model"
)
```

---

## Step 8 – Register Best Model

```python
model = Model(
    path="./best_automl_model/model",
    name="titanic-automl-best",
    description="Best model from AutoML classification",
    type="mlflow_model"
)

registered_model = ml_client.models.create_or_update(model)
print(f"Registered: {registered_model.name} v{registered_model.version}")
```

---

## AutoML for Other Tasks

### Regression:

```python
from azure.ai.ml import automl

regression_job = automl.regression(
    compute="cpu-cluster",
    training_data=Input(type="mltable", path="azureml:housing-data@latest"),
    target_column_name="price",
    primary_metric="r2_score"
)
```

### Forecasting:

```python
forecasting_job = automl.forecasting(
    compute="cpu-cluster",
    training_data=Input(type="mltable", path="azureml:sales-data@latest"),
    target_column_name="sales",
    primary_metric="normalized_root_mean_squared_error"
)

forecasting_job.set_forecast_settings(
    time_column_name="date",
    forecast_horizon=14
)
```

---

## ✅ Lab Checklist

- [ ] Prepared data as MLTable format
- [ ] Configured classification AutoML job
- [ ] Set limits and featurization options
- [ ] Submitted and monitored AutoML job
- [ ] Analyzed models and explanations in Studio
- [ ] Retrieved and registered the best model
