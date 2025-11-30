# Lab 08: Build a Responsible AI Dashboard

## 🎯 Lab Goal

Create a **Responsible AI dashboard** to analyze model fairness and interpretability:

- Generate model explanations
- Analyze error cohorts
- Evaluate fairness metrics

This supports the **Implement responsible AI** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace with registered model
- Training and test datasets

---

## Step 1 – Understand Responsible AI Components

| Component | Purpose |
|-----------|--------|
| Error Analysis | Identify error patterns in data slices |
| Model Interpretability | Explain feature importance |
| Fairness | Detect bias across sensitive groups |
| Counterfactuals | Show minimal changes for different predictions |
| Causal | Understand causal relationships |

---

## Step 2 – Prepare Data and Model

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load and prepare data
df = pd.read_csv("./data/titanic.csv")

# Create features including sensitive attribute
df['Sex_encoded'] = df['Sex'].map({'male': 0, 'female': 1})
feature_cols = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_encoded']

X = df[feature_cols].fillna(0)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(n_estimators=100, max_depth=5)
model.fit(X_train, y_train)
```

---

## Step 3 – Register Model and Test Data

```python
import mlflow

# Register model
mlflow.sklearn.log_model(model, "model", registered_model_name="titanic-rai")

# Save test data
test_df = X_test.copy()
test_df['Survived'] = y_test.values
test_df.to_parquet("./data/titanic_test.parquet")

# Register as data asset
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

test_data = Data(
    name="titanic-test-rai",
    path="./data/titanic_test.parquet",
    type=AssetTypes.URI_FILE
)
ml_client.data.create_or_update(test_data)
```

---

## Step 4 – Create RAI Insights Dashboard Job

```python
from azure.ai.ml import Input
from azure.ai.ml.entities import (
    Model,
    ResponsibleAiComponentsSet,
    ResponsibleAiInsight
)

# Define RAI components
rai_components = ResponsibleAiComponentsSet(
    error_analysis=True,
    explanation=True,
    counterfactual=True,
    causal=False  # Requires specific configuration
)

# Create RAI insight
rai_insight = ResponsibleAiInsight(
    components=rai_components,
    target_column_name="Survived",
    training_data=Input(type="mltable", path="azureml:titanic-train-rai@latest"),
    test_data=Input(type="mltable", path="azureml:titanic-test-rai@latest")
)
```

---

## Step 5 – Alternative: Use RAI SDK Locally

```bash
pip install raiwidgets responsibleai
```

```python
from responsibleai import RAIInsights

# Create RAI insights
rai_insights = RAIInsights(
    model=model,
    train=X_train.assign(Survived=y_train),
    test=X_test.assign(Survived=y_test),
    target_column="Survived",
    task_type="classification"
)

# Add components
rai_insights.error_analysis.add()
rai_insights.explainer.add()
rai_insights.counterfactual.add(
    total_CFs=10,
    desired_class="opposite"
)

# Compute insights
rai_insights.compute()
```

---

## Step 6 – View Dashboard Locally

```python
from raiwidgets import ResponsibleAIDashboard

ResponsibleAIDashboard(rai_insights)
```

This opens an interactive dashboard to explore:
- Error analysis tree map
- Feature importance
- Individual predictions
- Counterfactual examples

---

## Step 7 – Analyze Fairness

```python
from fairlearn.metrics import MetricFrame
from sklearn.metrics import accuracy_score, precision_score

# Define sensitive feature
sensitive_feature = X_test['Sex_encoded']

# Create metric frame
y_pred = model.predict(X_test)

metrics = {
    "accuracy": accuracy_score,
    "precision": precision_score
}

metric_frame = MetricFrame(
    metrics=metrics,
    y_true=y_test,
    y_pred=y_pred,
    sensitive_features=sensitive_feature
)

print("Overall metrics:")
print(metric_frame.overall)

print("\nMetrics by group:")
print(metric_frame.by_group)

print("\nDifference (disparity):")
print(metric_frame.difference())
```

---

## Step 8 – Save and Share Insights

```python
# Save locally
rai_insights.save("./rai_insights")

# Upload to Azure ML
from azure.ai.ml.entities import Data

rai_data = Data(
    name="titanic-rai-insights",
    path="./rai_insights",
    type=AssetTypes.URI_FOLDER
)
ml_client.data.create_or_update(rai_data)
```

---

## ✅ Lab Checklist

- [ ] Understood Responsible AI components
- [ ] Prepared data with sensitive attributes identified
- [ ] Created RAI insights with error analysis and explanations
- [ ] Viewed interactive Responsible AI dashboard
- [ ] Analyzed fairness metrics across groups
- [ ] Saved and shared insights
