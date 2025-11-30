# Lab 10: Build and Run Training Pipelines

## 🎯 Lab Goal

Create **ML pipelines** for reproducible workflows:

- Build multi-step pipelines
- Pass data between steps
- Schedule and reuse pipelines

This supports the **Orchestrate ML workflows** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace with compute cluster
- Data assets and environments configured

---

## Step 1 – Understand Pipeline Concepts

| Concept | Description |
|---------|------------|
| Component | Reusable step with defined inputs/outputs |
| Pipeline | DAG of connected components |
| Pipeline Job | Single execution of a pipeline |
| Schedule | Automated pipeline triggering |

---

## Step 2 – Create Pipeline Components

### Data Preparation Component:

Create `components/prep_data.yml`:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
name: prep_data
version: 1
type: command

display_name: Prepare Data
description: Clean and prepare data for training

inputs:
  raw_data:
    type: uri_file

outputs:
  prepared_data:
    type: uri_folder

code: ../src/prep
command: python prep.py --raw_data ${{inputs.raw_data}} --output ${{outputs.prepared_data}}

environment:
  azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
```

### prep.py:

```python
import argparse
import pandas as pd
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw_data", type=str)
    parser.add_argument("--output", type=str)
    args = parser.parse_args()
    
    # Load and clean data
    df = pd.read_csv(args.raw_data)
    df = df.dropna(subset=['Age', 'Fare'])
    df['Age'].fillna(df['Age'].median(), inplace=True)
    
    # Save prepared data
    os.makedirs(args.output, exist_ok=True)
    df.to_csv(os.path.join(args.output, "prepared.csv"), index=False)
    print(f"Prepared {len(df)} rows")

if __name__ == "__main__":
    main()
```

### Training Component:

Create `components/train.yml`:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
name: train_model
version: 1
type: command

display_name: Train Model

inputs:
  training_data:
    type: uri_folder
  n_estimators:
    type: integer
    default: 100

outputs:
  model_output:
    type: uri_folder

code: ../src/train
command: >-
  python train.py 
  --data ${{inputs.training_data}} 
  --n_estimators ${{inputs.n_estimators}}
  --output ${{outputs.model_output}}

environment:
  azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
```

---

## Step 3 – Load Components

```python
from azure.ai.ml import load_component

prep_component = load_component(source="./components/prep_data.yml")
train_component = load_component(source="./components/train.yml")

# Register components (optional)
ml_client.components.create_or_update(prep_component)
ml_client.components.create_or_update(train_component)
```

---

## Step 4 – Build the Pipeline

```python
from azure.ai.ml import dsl, Input

@dsl.pipeline(
    compute="cpu-cluster",
    description="Titanic training pipeline"
)
def titanic_pipeline(raw_data: Input, n_estimators: int = 100):
    # Step 1: Prepare data
    prep_step = prep_component(raw_data=raw_data)
    
    # Step 2: Train model
    train_step = train_component(
        training_data=prep_step.outputs.prepared_data,
        n_estimators=n_estimators
    )
    
    return {
        "prepared_data": prep_step.outputs.prepared_data,
        "model": train_step.outputs.model_output
    }

# Instantiate pipeline
pipeline = titanic_pipeline(
    raw_data=Input(type="uri_file", path="azureml:titanic-data@latest"),
    n_estimators=100
)
```

---

## Step 5 – Submit Pipeline Job

```python
pipeline_job = ml_client.jobs.create_or_update(
    pipeline,
    experiment_name="titanic-pipeline"
)

print(f"Pipeline job: {pipeline_job.studio_url}")

# Wait for completion
ml_client.jobs.stream(pipeline_job.name)
```

---

## Step 6 – View Pipeline in Studio

1. Open the job URL in Azure ML Studio.
2. Explore:
   - **Graph view** – Pipeline DAG visualization
   - **Outputs + logs** – Each step's outputs
   - **Metrics** – Logged metrics per step

---

## Step 7 – Schedule the Pipeline

```python
from azure.ai.ml.entities import (
    RecurrenceTrigger,
    JobSchedule
)

schedule = JobSchedule(
    name="titanic-weekly-training",
    trigger=RecurrenceTrigger(
        frequency="week",
        interval=1,
        schedule=RecurrencePattern(
            week_days=["Monday"],
            hours=[8],
            minutes=[0]
        )
    ),
    create_job=pipeline
)

ml_client.schedules.begin_create_or_update(schedule).result()
print("Schedule created")
```

### List and Manage Schedules:

```python
# List schedules
for s in ml_client.schedules.list():
    print(f"{s.name}: {s.is_enabled}")

# Disable schedule
schedule.is_enabled = False
ml_client.schedules.begin_create_or_update(schedule).result()
```

---

## Step 8 – Reuse Pipeline Outputs

```python
# Get outputs from completed pipeline
completed_job = ml_client.jobs.get(pipeline_job.name)

# Download outputs
ml_client.jobs.download(
    name=pipeline_job.name,
    download_path="./outputs",
    output_name="model"
)
```

---

## ✅ Lab Checklist

- [ ] Created reusable pipeline components
- [ ] Loaded and registered components
- [ ] Built multi-step pipeline using @dsl.pipeline
- [ ] Passed data between pipeline steps
- [ ] Submitted and monitored pipeline job
- [ ] Created schedule for automated runs
- [ ] Downloaded pipeline outputs
