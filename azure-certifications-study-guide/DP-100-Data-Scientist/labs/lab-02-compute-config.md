# Lab 02: Configure Compute Targets for Azure ML

## 🎯 Lab Goal

Configure **compute targets** for Azure ML workloads:

- Create compute instances for development
- Create compute clusters for training
- Understand compute options

This supports the **Manage Azure Machine Learning resources** domain of DP‑100.

---

## ✅ Prerequisites

- Azure ML workspace from Lab 01
- Azure ML Python SDK installed

---

## Step 1 – Understand Compute Types

| Type | Use Case | Scaling |
|------|----------|--------|
| Compute Instance | Development, notebooks | Single VM |
| Compute Cluster | Training jobs | Auto-scale (0-N nodes) |
| Kubernetes Cluster | Production inference | Manual |
| Serverless Compute | On-demand training | Automatic |

---

## Step 2 – Create Compute Instance

### Via Python SDK:

```python
from azure.ai.ml.entities import ComputeInstance

ci = ComputeInstance(
    name="ci-dp100-dev",
    size="Standard_DS3_v2",
    idle_time_before_shutdown_minutes=60  # Auto-shutdown
)

ml_client.compute.begin_create_or_update(ci).result()
print("Compute instance created")
```

### Via CLI:

```bash
az ml compute create \
  --name ci-dp100-dev \
  --type ComputeInstance \
  --size Standard_DS3_v2 \
  --resource-group rg-dp100 \
  --workspace-name mlw-dp100-lab
```

---

## Step 3 – Create Compute Cluster

### Via Python SDK:

```python
from azure.ai.ml.entities import AmlCompute

cluster = AmlCompute(
    name="cpu-cluster",
    size="Standard_DS3_v2",
    min_instances=0,
    max_instances=4,
    idle_time_before_scale_down=300,  # 5 minutes
    tier="Dedicated"  # or "LowPriority" for cost savings
)

ml_client.compute.begin_create_or_update(cluster).result()
print("Compute cluster created")
```

### GPU Cluster for Deep Learning:

```python
gpu_cluster = AmlCompute(
    name="gpu-cluster",
    size="Standard_NC6s_v3",  # NVIDIA V100
    min_instances=0,
    max_instances=2,
    idle_time_before_scale_down=300
)

ml_client.compute.begin_create_or_update(gpu_cluster).result()
```

---

## Step 4 – Use Serverless Compute

Serverless compute doesn't require pre-creation:

```python
from azure.ai.ml import command
from azure.ai.ml.entities import ResourceConfiguration

job = command(
    code="./src",
    command="python train.py",
    environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
    compute="serverless",
    resources=ResourceConfiguration(
        instance_type="Standard_DS3_v2",
        instance_count=1
    )
)
```

---

## Step 5 – List and Manage Compute

```python
# List all compute targets
for compute in ml_client.compute.list():
    print(f"{compute.name}: {compute.type} - {compute.provisioning_state}")

# Get specific compute
cluster = ml_client.compute.get("cpu-cluster")
print(f"Cluster size: {cluster.size}")
print(f"Current nodes: {cluster.current_node_count}")

# Start/stop compute instance
ml_client.compute.begin_start("ci-dp100-dev").result()
ml_client.compute.begin_stop("ci-dp100-dev").result()
```

---

## Step 6 – Configure Auto-Shutdown

### Compute Instance Schedule:

```python
from azure.ai.ml.entities import ComputeSchedules, ComputeStartStopSchedule, ScheduleState
from datetime import time

schedule = ComputeStartStopSchedule(
    trigger=RecurrenceTrigger(
        frequency="day",
        schedule=RecurrencePattern(hours=[18], minutes=[0])
    ),
    action="Stop",
    state=ScheduleState.ENABLED
)
```

---

## Cost Optimization Tips

| Strategy | Savings |
|----------|--------|
| Use min_instances=0 | No idle cost |
| Low-priority VMs | Up to 80% |
| Auto-shutdown schedules | Avoid overnight running |
| Right-size VMs | Match workload needs |

---

## Cleanup

```python
ml_client.compute.begin_delete("ci-dp100-dev").result()
ml_client.compute.begin_delete("cpu-cluster").result()
```

---

## ✅ Lab Checklist

- [ ] Created a compute instance for development
- [ ] Created a compute cluster for training
- [ ] Understood serverless compute option
- [ ] Listed and managed compute targets
- [ ] Configured auto-shutdown for cost savings
