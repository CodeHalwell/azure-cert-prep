# 🧪 DP-100 Practice Resources

## Official Microsoft Practice Assessment

### 📋 Microsoft Practice Assessment

| Resource | Details |
|----------|---------|
| **Link** | [DP-100 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-data-scientist/practice/assessment?assessment-type=practice&assessmentId=62) |
| **Format** | Multiple choice, case studies |
| **Cost** | Free |
| **Questions** | 50+ questions |

---

## ☁️ Hands-On Practice

### Azure Free Account

| Feature | Details |
|---------|---------|
| **Link** | [Create Free Account](https://azure.microsoft.com/free/) |
| **Credit** | $200 for 30 days |
| **ML Compute** | Limited free hours |

### Microsoft Learn Sandbox

| Feature | Details |
|---------|---------|
| **Activation** | Included in Learn modules |
| **Cost** | Free |
| **Duration** | 4 hours per session |

---

## 📚 Hands-On Labs

### Domain 1: Workspace Setup

| Lab | Skills Practiced |
|-----|-----------------|
| Create ML workspace | Resource provisioning |
| Configure compute | Instances and clusters |
| Set up datastores | Data connections |
| Create environments | Custom dependencies |

### Domain 2: Model Training

| Lab | Skills Practiced |
|-----|-----------------|
| Run training script | Command jobs |
| Track with MLflow | Experiment logging |
| AutoML classification | Automated training |
| Hyperparameter tuning | Sweep jobs |

### Domain 3: Model Management

| Lab | Skills Practiced |
|-----|-----------------|
| Register models | Model registry |
| Responsible AI dashboard | Interpretability |
| Compare models | Version comparison |

### Domain 4: Deployment

| Lab | Skills Practiced |
|-----|-----------------|
| Deploy online endpoint | Real-time inference |
| Deploy batch endpoint | Batch scoring |
| Blue-green deployment | Safe rollout |
| Monitor data drift | Model monitoring |

---

## 🔧 Code Practice

### SDK v2 Examples

```python
# Create workspace connection
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="<subscription_id>",
    resource_group_name="<resource_group>",
    workspace_name="<workspace_name>"
)
```

```python
# Submit training job
from azure.ai.ml import command

job = command(
    code="./src",
    command="python train.py --learning-rate ${{inputs.lr}}",
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
    compute="cpu-cluster",
    inputs={"lr": 0.01}
)

ml_client.jobs.create_or_update(job)
```

---

## 📊 Knowledge Check

### Workspace & Compute

1. What are the associated resources for an Azure ML workspace?
2. When should you use compute clusters vs instances?
3. How do you configure auto-shutdown for compute?
4. What is the purpose of environments?

### Training & AutoML

1. How do you track experiments with MLflow?
2. What sampling algorithms are available for hyperparameter tuning?
3. What are the primary metrics for classification tasks?
4. How does cross-validation work in AutoML?

### Deployment

1. What is the difference between online and batch endpoints?
2. How do you implement blue-green deployment?
3. What triggers can be used for retraining pipelines?
4. How do you monitor for data drift?

---

## 🔗 Additional Resources

| Resource | Link |
|----------|------|
| Azure ML Examples | [GitHub](https://github.com/Azure/azureml-examples) |
| SDK Documentation | [Link](https://learn.microsoft.com/en-us/python/api/azure-ai-ml/) |
| Exam Sandbox | [Link](https://aka.ms/examdemo) |

---

*Last updated: November 2025*
