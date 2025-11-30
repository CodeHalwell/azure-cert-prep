# Lab 07: Design Compute Architecture

## 🎯 Lab Goal

Design **compute architecture** for various workloads:

- Select appropriate compute services
- Design for scalability and cost optimization
- Evaluate containers vs. VMs vs. serverless

This supports the **Design infrastructure solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of Azure compute services

---

## Scenario

Contoso needs compute for:
- Web application (variable traffic, 100-10,000 users)
- Batch processing (nightly, CPU-intensive)
- Microservices (10 services, independent scaling)
- Legacy application (Windows Server, requires IIS)

---

## Step 1 – Evaluate Compute Options

### Decision Matrix:

| Requirement | VMs | App Service | Container Apps | Functions |
|-------------|-----|-------------|----------------|----------|
| Full OS control | ✓ | | | |
| Web apps | ✓ | ✓ | ✓ | ✓ |
| Microservices | | | ✓ | |
| Event-driven | | | | ✓ |
| Legacy apps | ✓ | | | |
| Auto-scaling | Manual | ✓ | ✓ | ✓ |

### Contoso Selections:

| Workload | Service | Justification |
|----------|---------|---------------|
| Web app | App Service | Managed, auto-scale |
| Batch | Azure Batch | Optimized for HPC |
| Microservices | Container Apps | Dapr, KEDA scaling |
| Legacy | Virtual Machines | Full control needed |

---

## Step 2 – Design App Service Architecture

### Tier Selection:

| Tier | Use Case | Features |
|------|----------|----------|
| Free/Shared | Dev/Test | Limited, shared |
| Basic | Light production | Dedicated, no auto-scale |
| Standard | Production | Auto-scale, slots |
| Premium | High-scale, VNet | Zone redundancy |

### Scaling Strategy:

```bash
az monitor autoscale create \
  --resource-group rg-webapp \
  --resource webapp-contoso \
  --resource-type Microsoft.Web/sites \
  --min-count 2 \
  --max-count 10 \
  --count 2

az monitor autoscale rule create \
  --resource-group rg-webapp \
  --autoscale-name webapp-autoscale \
  --condition "CpuPercentage > 70 avg 5m" \
  --scale out 2
```

---

## Step 3 – Design Container Architecture

### AKS vs. Container Apps:

| Factor | AKS | Container Apps |
|--------|-----|----------------|
| Complexity | High | Low |
| Control | Full K8s | Managed |
| Scaling | HPA, KEDA | Built-in KEDA |
| Use case | Large enterprise | Microservices, APIs |

### Container Apps Design:

```
Container Apps Environment
├── orders-api (scale on HTTP, 1-20 replicas)
├── inventory-service (scale on queue, 0-10 replicas)
├── notification-service (scale on events)
└── frontend (scale on HTTP, 2-50 replicas)
```

```bash
az containerapp create \
  --name orders-api \
  --resource-group rg-containers \
  --environment cae-contoso \
  --image contoso.azurecr.io/orders:latest \
  --min-replicas 1 \
  --max-replicas 20 \
  --ingress external
```

---

## Step 4 – Design VM Architecture

### VM Size Selection:

| Series | Use Case |
|--------|----------|
| B-series | Burstable, dev/test |
| D-series | General purpose |
| E-series | Memory-optimized |
| F-series | CPU-optimized |
| N-series | GPU workloads |

### Cost Optimization:

| Strategy | Savings |
|----------|--------|
| Reserved Instances | Up to 72% |
| Spot VMs | Up to 90% |
| Hybrid Benefit | Up to 40% |
| Right-sizing | Variable |

---

## Step 5 – Design Document

```markdown
# Compute Architecture – Contoso Ltd.

## 1. Service Selection
| Workload | Service | SKU |
|----------|---------|-----|
| Web App | App Service | Premium v3 P1V3 |
| Batch | Azure Batch | D4s_v3 (spot) |
| Microservices | Container Apps | Consumption |
| Legacy | VMs | D4s_v3 |

## 2. Scaling Strategy
- App Service: CPU-based autoscale (2-10)
- Container Apps: HTTP + queue-based KEDA
- VMs: VMSS with schedule-based scaling

## 3. Cost Optimization
- 3-year reserved instances for VMs
- Spot VMs for batch processing
- Azure Hybrid Benefit for Windows
- Consumption plan for dev environments

## 4. Security
- VNet integration for all services
- Managed identities for authentication
- Private endpoints where supported
```

---

## ✅ Lab Checklist

- [ ] Evaluated compute options for each workload
- [ ] Designed App Service scaling strategy
- [ ] Created container architecture with appropriate scaling
- [ ] Planned VM sizing and cost optimization
- [ ] Documented compute architecture
