# Lab 09: Deploy a Model to a Managed Online Endpoint

## 🎯 Lab Goal

Deploy a model to a **managed online endpoint** for real-time inference:

- Create managed endpoint
- Deploy model with scoring script
- Test and manage deployments

This supports the **Deploy and operationalize models** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace
- Registered model (from Lab 06 or 07)

---

## Step 1 – Understand Endpoint Types

| Type | Use Case | Scaling |
|------|----------|--------|
| Managed Online | Real-time, managed infra | Auto-scale |
| Kubernetes Online | Real-time, bring your own K8s | Manual |
| Batch Endpoint | Large-scale batch scoring | Job-based |

---

## Step 2 – Create Managed Online Endpoint

```python
from azure.ai.ml.entities import ManagedOnlineEndpoint
import datetime

# Create unique endpoint name
endpoint_name = f"titanic-endpoint-{datetime.datetime.now().strftime('%m%d%H%M')}"

endpoint = ManagedOnlineEndpoint(
    name=endpoint_name,
    description="Titanic survival prediction endpoint",
    auth_mode="key"  # or "aml_token"
)

ml_client.online_endpoints.begin_create_or_update(endpoint).result()
print(f"Endpoint created: {endpoint_name}")
```

---

## Step 3 – Create Scoring Script

Create `score.py`:

```python
import json
import logging
import os
import mlflow

def init():
    global model
    
    # Get model path from environment
    model_path = os.path.join(
        os.environ["AZUREML_MODEL_DIR"], 
        "model"
    )
    
    # Load MLflow model
    model = mlflow.sklearn.load_model(model_path)
    logging.info("Model loaded successfully")

def run(raw_data):
    try:
        # Parse input
        data = json.loads(raw_data)
        
        # Handle single or batch predictions
        if isinstance(data, dict):
            data = [data]
        
        # Extract features
        import pandas as pd
        df = pd.DataFrame(data)
        
        # Make predictions
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)
        
        # Return results
        result = {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist()
        }
        
        return json.dumps(result)
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return json.dumps({"error": str(e)})
```

---

## Step 4 – Create Deployment

```python
from azure.ai.ml.entities import (
    ManagedOnlineDeployment,
    Model,
    Environment,
    CodeConfiguration
)

# Get registered model
model = ml_client.models.get(name="titanic-rf", version="1")

# Use curated environment or create custom
environment = Environment(
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
    conda_file="./environment.yml"
)

# Create deployment
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint_name,
    model=model,
    environment=environment,
    code_configuration=CodeConfiguration(
        code="./src",
        scoring_script="score.py"
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1
)

ml_client.online_deployments.begin_create_or_update(deployment).result()
print("Deployment created")
```

### Environment.yml:

```yaml
name: scoring-env
channels:
  - conda-forge
dependencies:
  - python=3.9
  - pip
  - pip:
    - mlflow
    - scikit-learn
    - pandas
```

---

## Step 5 – Route Traffic to Deployment

```python
# Set 100% traffic to blue deployment
endpoint.traffic = {"blue": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```

---

## Step 6 – Test the Endpoint

```python
# Test with sample data
test_data = {
    "Pclass": 1,
    "Age": 35,
    "SibSp": 0,
    "Parch": 0,
    "Fare": 100.0
}

response = ml_client.online_endpoints.invoke(
    endpoint_name=endpoint_name,
    request_file="./sample_request.json"  # Or use deployment_name for specific
)

print(response)
```

### Using REST API:

```python
import requests

# Get scoring URI and key
endpoint = ml_client.online_endpoints.get(endpoint_name)
scoring_uri = endpoint.scoring_uri
keys = ml_client.online_endpoints.get_keys(endpoint_name)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {keys.primary_key}"
}

response = requests.post(
    scoring_uri,
    headers=headers,
    json=test_data
)

print(response.json())
```

---

## Step 7 – Blue-Green Deployment

```python
# Create green deployment with new model
green_deployment = ManagedOnlineDeployment(
    name="green",
    endpoint_name=endpoint_name,
    model=ml_client.models.get(name="titanic-rf", version="2"),
    environment=environment,
    code_configuration=CodeConfiguration(
        code="./src",
        scoring_script="score.py"
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1
)

ml_client.online_deployments.begin_create_or_update(green_deployment).result()

# Gradually shift traffic
endpoint.traffic = {"blue": 90, "green": 10}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Full cutover
endpoint.traffic = {"blue": 0, "green": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Delete old deployment
ml_client.online_deployments.begin_delete(
    name="blue",
    endpoint_name=endpoint_name
).result()
```

---

## Cleanup

```python
ml_client.online_endpoints.begin_delete(endpoint_name).result()
```

---

## ✅ Lab Checklist

- [ ] Created managed online endpoint
- [ ] Created scoring script for inference
- [ ] Deployed model with environment and code configuration
- [ ] Routed traffic to deployment
- [ ] Tested endpoint via SDK and REST API
- [ ] Implemented blue-green deployment pattern
