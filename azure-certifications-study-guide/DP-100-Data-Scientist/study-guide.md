# 📖 DP-100 Study Guide

## Azure Data Scientist Associate

This comprehensive study guide covers all skills measured in the DP-100 exam.

---

## 📊 Exam Overview

| Attribute | Details |
|-----------|---------|
| **Total Questions** | 40-60 |
| **Duration** | 100 minutes |
| **Passing Score** | 700/1000 |
| **Question Types** | Multiple choice, case studies, drag-and-drop |

---

# Domain 1: Design and Prepare a Machine Learning Solution (20-25%)

## 1.1 Design an Azure Machine Learning Solution

### Workspace Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 Azure Machine Learning Workspace             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   Compute   │  │    Data     │  │   Models    │         │
│  │  Resources  │  │   Assets    │  │  Registry   │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ Experiments │  │  Pipelines  │  │  Endpoints  │         │
│  │             │  │             │  │             │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
├─────────────────────────────────────────────────────────────┤
│  Associated Resources:                                       │
│  - Storage Account (data, models, logs)                     │
│  - Key Vault (secrets, credentials)                         │
│  - Container Registry (Docker images)                       │
│  - Application Insights (monitoring)                        │
└─────────────────────────────────────────────────────────────┘
```

### Compute Options

| Compute Type | Use Case | Scaling |
|--------------|----------|---------|
| **Compute Instance** | Development, notebooks | Single VM |
| **Compute Cluster** | Training jobs | Auto-scale |
| **Serverless Compute** | On-demand training | Fully managed |
| **Kubernetes** | Production inference | Enterprise scale |
| **Attached Compute** | Existing resources | Bring your own |

### Compute Instance vs Cluster

| Aspect | Compute Instance | Compute Cluster |
|--------|-----------------|-----------------|
| Purpose | Development | Training jobs |
| Users | Single user | Multiple jobs |
| Scaling | Fixed size | Auto-scale |
| Idle shutdown | Configurable | Auto-shutdown |
| Cost | Always on (when running) | Pay per job |

---

## 1.2 Manage Workspace Resources

### Data Stores

| Datastore Type | Use Case |
|---------------|----------|
| Azure Blob Storage | Unstructured data, large files |
| Azure Data Lake Gen2 | Enterprise data lake |
| Azure Files | Shared file storage |
| Azure SQL Database | Structured data |

### Data Assets

| Asset Type | Description |
|------------|-------------|
| **URI File** | Single file reference |
| **URI Folder** | Folder reference |
| **MLTable** | Tabular data with schema |

### Environments

```python
# Creating a custom environment
from azure.ai.ml.entities import Environment

env = Environment(
    name="custom-sklearn-env",
    conda_file="./conda.yml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04"
)
ml_client.environments.create_or_update(env)
```

---

# Domain 2: Explore Data and Train Models (25-30%)

## 2.1 Explore Data

### Exploratory Data Analysis (EDA)

| Task | Techniques |
|------|------------|
| **Data profiling** | Summary statistics, data types |
| **Missing values** | Identify patterns, decide handling |
| **Distributions** | Histograms, box plots |
| **Correlations** | Correlation matrix, scatter plots |
| **Outliers** | Z-scores, IQR method |

### Feature Engineering

| Technique | Description |
|-----------|-------------|
| **Encoding** | One-hot, label, target encoding |
| **Scaling** | StandardScaler, MinMaxScaler |
| **Binning** | Continuous to categorical |
| **Polynomial** | Create interaction features |
| **Text features** | TF-IDF, word embeddings |

---

## 2.2 Train Models

### AutoML Configuration

```python
from azure.ai.ml import automl

classification_job = automl.classification(
    compute="cpu-cluster",
    experiment_name="automl-classification",
    training_data=train_data,
    target_column_name="label",
    primary_metric="accuracy",
    n_cross_validations=5,
    enable_model_explainability=True
)
```

### AutoML Task Types

| Task | Primary Metrics |
|------|-----------------|
| **Classification** | Accuracy, AUC, F1, Precision, Recall |
| **Regression** | R2, RMSE, MAE, Spearman |
| **Forecasting** | RMSE, MAE, MAPE |

### Hyperparameter Tuning

```python
from azure.ai.ml.sweep import Choice, Uniform

sweep_job = command_job.sweep(
    compute="gpu-cluster",
    sampling_algorithm="random",
    primary_metric="accuracy",
    goal="maximize",
)

sweep_job.set_limits(max_total_trials=20, max_concurrent_trials=4)

sweep_job.inputs.learning_rate = Uniform(min_value=0.001, max_value=0.1)
sweep_job.inputs.batch_size = Choice(values=[16, 32, 64])
```

### Sampling Algorithms

| Algorithm | Description | Use Case |
|-----------|-------------|----------|
| **Random** | Random selection | Initial exploration |
| **Grid** | Exhaustive search | Small search space |
| **Bayesian** | Probabilistic optimization | Expensive training |

---

## 2.3 Evaluate Models

### Classification Metrics

| Metric | Description | Use When |
|--------|-------------|----------|
| **Accuracy** | Correct predictions / total | Balanced classes |
| **Precision** | TP / (TP + FP) | Cost of FP is high |
| **Recall** | TP / (TP + FN) | Cost of FN is high |
| **F1 Score** | Harmonic mean of P & R | Balance P & R |
| **AUC-ROC** | Area under ROC curve | Threshold selection |

### Regression Metrics

| Metric | Description | Properties |
|--------|-------------|------------|
| **R²** | Variance explained | 0-1 scale |
| **RMSE** | Root mean squared error | Same units as target |
| **MAE** | Mean absolute error | Robust to outliers |
| **MAPE** | Mean absolute percentage | Percentage scale |

---

# Domain 3: Prepare a Model for Deployment (20-25%)

## 3.1 Work with MLflow

### Experiment Tracking

```python
import mlflow

mlflow.set_experiment("my-experiment")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 100)
    
    # Training code...
    
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_metric("loss", 0.05)
    
    mlflow.sklearn.log_model(model, "model")
```

### Model Registry

| Operation | Description |
|-----------|-------------|
| **Register** | Add model to registry |
| **Version** | Track model versions |
| **Stage** | None, Staging, Production, Archived |
| **Transition** | Move between stages |

### Model Registration

```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

model = Model(
    path="./model",
    type=AssetTypes.MLFLOW_MODEL,
    name="my-model",
    description="Classification model"
)

ml_client.models.create_or_update(model)
```

---

## 3.2 Responsible AI

### Responsible AI Dashboard

| Component | Purpose |
|-----------|---------|
| **Error Analysis** | Understand failure patterns |
| **Model Interpretability** | Feature importance, explanations |
| **Fairness** | Assess demographic disparities |
| **Counterfactuals** | What-if analysis |
| **Causal Inference** | Treatment effects |

### Fairness Metrics

| Metric | Description |
|--------|-------------|
| **Demographic Parity** | Equal positive rates across groups |
| **Equalized Odds** | Equal TPR and FPR across groups |
| **Equal Opportunity** | Equal TPR across groups |

---

# Domain 4: Deploy and Retrain a Model (25-30%)

## 4.1 Deploy Models

### Online Endpoints

```python
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment
)

endpoint = ManagedOnlineEndpoint(
    name="my-endpoint",
    auth_mode="key"
)

ml_client.online_endpoints.begin_create_or_update(endpoint)

deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name="my-endpoint",
    model=model,
    instance_type="Standard_DS3_v2",
    instance_count=1
)

ml_client.online_deployments.begin_create_or_update(deployment)
```

### Endpoint Types

| Type | Use Case | Scaling |
|------|----------|---------|
| **Managed Online** | Real-time, managed | Autoscale |
| **Kubernetes** | Enterprise, existing K8s | Manual/auto |
| **Batch** | Large-scale batch scoring | Parallel processing |

### Blue-Green Deployment

```
┌─────────────────────────────────────────────────────────────┐
│                        Endpoint                              │
│                    "my-endpoint"                             │
└───────────────────────────┬─────────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            │ Traffic Split                  │
            │ Blue: 90% | Green: 10%         │
            └───────────────┬───────────────┘
                            │
        ┌───────────────────┴───────────────────┐
        │                                       │
┌───────▼───────┐                       ┌───────▼───────┐
│ Blue Deployment│                       │Green Deployment│
│   (v1 model)   │                       │   (v2 model)   │
└────────────────┘                       └────────────────┘
```

---

## 4.2 Create Pipelines

### Pipeline Components

```python
from azure.ai.ml import command
from azure.ai.ml.dsl import pipeline

@pipeline()
def training_pipeline(input_data):
    prep_step = prep_component(data=input_data)
    train_step = train_component(data=prep_step.outputs.output_data)
    eval_step = eval_component(model=train_step.outputs.model)
    return {"model": eval_step.outputs.model}
```

### Pipeline Triggers

| Trigger Type | Use Case |
|--------------|----------|
| **Schedule** | Regular retraining |
| **Event-based** | New data arrival |
| **Manual** | On-demand execution |

---

## 4.3 Monitor Models

### Data Drift Monitoring

| Metric | Description |
|--------|-------------|
| **Statistical distance** | Distribution difference |
| **Feature drift** | Individual feature changes |
| **Target drift** | Label distribution changes |

### Setting Up Monitoring

```python
from azure.ai.ml.entities import (
    MonitoringTarget,
    MonitorSchedule,
    DataDriftSignal
)

monitoring = MonitorSchedule(
    name="model-monitor",
    trigger=RecurrenceTrigger(frequency="week", interval=1),
    create_monitor=MonitorDefinition(
        signals={
            "data_drift": DataDriftSignal(
                production_data=production_data,
                reference_data=reference_data,
                features=["feature1", "feature2"]
            )
        }
    )
)
```

---

## ✅ Study Checklist

### Domain 1: Design & Prepare
- [ ] Understand workspace components
- [ ] Know compute options and use cases
- [ ] Configure datastores and data assets
- [ ] Create and manage environments

### Domain 2: Explore & Train
- [ ] Perform exploratory data analysis
- [ ] Apply feature engineering techniques
- [ ] Configure and run AutoML
- [ ] Implement hyperparameter tuning
- [ ] Evaluate models with appropriate metrics

### Domain 3: Prepare for Deployment
- [ ] Use MLflow for experiment tracking
- [ ] Register and manage models
- [ ] Implement Responsible AI dashboard
- [ ] Understand fairness metrics

### Domain 4: Deploy & Retrain
- [ ] Deploy to online endpoints
- [ ] Configure batch endpoints
- [ ] Create training pipelines
- [ ] Set up model monitoring
- [ ] Implement retraining automation

---

*Last updated: November 2025*
