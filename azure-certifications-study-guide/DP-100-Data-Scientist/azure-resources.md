# 🔧 DP-100 Azure Resources Reference

Data science–oriented reference for all core Azure resources in DP-100.

---

## 📋 Table of Contents

1. Azure Machine Learning
   - Workspaces
   - Compute (Compute Instances, Clusters, Attached Compute)
   - Datastores & Datasets
   - Environments & Pipelines
   - Managed Online/Batch Endpoints
2. Data Storage & Access
   - Azure Storage (Blob / ADLS Gen2)
   - Azure SQL / Synapse / Fabric (high-level)
3. Experimentation & MLOps
   - MLflow Tracking
   - Model Registry
   - Responsible AI tools

---

# 1. Azure Machine Learning

## 1.1 Workspace

### What It Is

- Logical container for all ML assets: experiments, runs, models, data, compute, endpoints

### Built-in

- Integration with Azure Key Vault, Storage, Container Registry
- Role-based access control at workspace level

### Requires Customization

- Network topology (public vs private, VNet isolation)
- RBAC and data access model (data scientist vs operator)

---

## 1.2 Compute

### Types

| Type | Purpose |
|------|---------|
| Compute Instance | Dev notebooks, interactive work |
| Compute Cluster | Scalable training jobs |
| Attached Compute | Bring your own Kubernetes, HDInsight, etc. |

### Built-in

- Auto-scale for clusters based on job queue
- Spot/low-priority VMs for cost savings

### Requires Customization

- VM size selection (CPU vs GPU, memory requirements)
- Idle timeouts and min/max nodes
- Node setup scripts and environments

---

## 1.3 Datastores & Datasets

### Datastores

- Abstract connection to storage (Blob/ADLS/SQL/etc.)
- Store **credentials securely**, often via managed identity or Key Vault

### Datasets (v1) / Data assets (v2)

- Versioned references to data in datastores
- Support for tabular and file data

### Requires Customization

- Data partitioning strategy (by date, by customer, etc.)
- Read/write access via managed identities

---

## 1.4 Environments & Pipelines

### Environments

- Define **conda/pip dependencies, base image**
- Ensure reproducible runs

### Pipelines

- Multi-step ML workflows (prepare → train → evaluate → register → deploy)

### Built-in

- CLI/SDK/Studio support for authoring
- Caching of pipeline steps

### Requires Customization

- Componentization of steps for reuse
- CI/CD integration (GitHub Actions/Azure DevOps)

---

## 1.5 Managed Endpoints (Online & Batch)

### What They Do

- Online endpoints: real-time scoring
- Batch endpoints: offline/bulk scoring

### Built-in

- Multi-model deployments with traffic split
- Auto-scaling and revision management

### Requires Customization

- Request/response contracts (schemas)
- Scaling rules (concurrency, instance counts)
- Canary deployments and A/B testing

---

# 2. Data Storage & Access

## 2.1 Azure Storage / ADLS Gen2

- Primary data lake for training and scoring data
- Use hierarchical namespace for **ADLS Gen2 features** (directories, ACLs)

### Built-in

- Integration with Azure ML datastores
- RBAC and POSIX-style ACLs (ADLS Gen2)

### Requires Customization

- Folder structure for raw / curated / feature / model outputs
- Access patterns (read-optimized vs write-optimized)

---

## 2.2 Other Data Services (High Level)

- Azure SQL / Synapse / Fabric items appear in exam as **data sources/targets**
- DP-100 focuses on **ML workflows**, not deep data warehousing design

---

# 3. Experimentation & MLOps

## 3.1 MLflow Tracking

- Native support in Azure ML
- Track parameters, metrics, artifacts, and model versions

## 3.2 Model Registry

- Central store for model versions with metadata and stage transitions (Dev/Test/Prod)

## 3.3 Responsible AI Tools

- Model interpretability (feature importance, SHAP)
- Error analysis, fairness dashboards

---

*Last updated: November 2025*