# Lab 06: Design High Availability Architecture

## 🎯 Lab Goal

Design **high availability architecture** for enterprise workloads:

- Evaluate availability options for compute
- Design multi-zone and multi-region deployments
- Plan for SLA requirements

This supports the **Design business continuity solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of availability zones and regions

---

## Scenario

Contoso requires:
- 99.99% SLA for e-commerce web tier
- 99.95% SLA for application tier
- Active-active deployment for global customers

---

## Step 1 – Understand Azure SLAs

### Compute SLAs:

| Configuration | SLA |
|--------------|-----|
| Single VM (Premium SSD) | 99.9% |
| Availability Set | 99.95% |
| Availability Zones | 99.99% |

### Calculating Composite SLA:

```
Web (99.99%) × App (99.95%) × Database (99.99%) = 99.93%
```

---

## Step 2 – Design Zone-Redundant Architecture

### Web Tier:

```
Azure Load Balancer (Zone-redundant)
       │
       ├── Zone 1: VM-Web-1
       ├── Zone 2: VM-Web-2
       └── Zone 3: VM-Web-3
```

### Create zone-redundant VM:

```bash
az vm create \
  --resource-group rg-ha \
  --name vm-web-1 \
  --zone 1 \
  --image Ubuntu2204 \
  --size Standard_D2s_v3
```

### Zone-redundant services:

| Service | Zone-Redundant Option |
|---------|----------------------|
| Load Balancer | Standard SKU |
| Public IP | Standard SKU |
| Storage | ZRS |
| SQL Database | Zone-redundant |
| App Service | Zone-redundant (Premium v3) |

---

## Step 3 – Design Multi-Region Active-Active

### Architecture:

```
                    Azure Front Door
                          │
            ┌────────────┴────────────┐
            │                         │
       East US                   West Europe
   ┌─────┴─────┐             ┌─────┴─────┐
   │  App GW    │             │  App GW    │
   │  VMs       │             │  VMs       │
   │  SQL (Primary) │         │  SQL (Replica) │
   └───────────┘             └───────────┘
```

### Front Door configuration:

```bash
az afd endpoint create \
  --endpoint-name contoso-global \
  --profile-name fd-contoso \
  --resource-group rg-global

az afd origin-group create \
  --origin-group-name og-eastus \
  --profile-name fd-contoso \
  --resource-group rg-global \
  --probe-path "/health"
```

---

## Step 4 – Design Health Probes and Failover

### Health Probe Design:

| Layer | Probe Type | Interval |
|-------|-----------|----------|
| Load Balancer | TCP/HTTP | 15 sec |
| Application Gateway | HTTP path | 30 sec |
| Front Door | HTTP path | 30 sec |
| Traffic Manager | HTTP/TCP | 30 sec |

### Health endpoint implementation:

```python
@app.route('/health')
def health():
    # Check dependencies
    try:
        db_healthy = check_database()
        cache_healthy = check_redis()
        if db_healthy and cache_healthy:
            return 'OK', 200
        return 'Degraded', 503
    except:
        return 'Unhealthy', 503
```

---

## Step 5 – Design Document

```markdown
# High Availability Architecture – Contoso Ltd.

## 1. SLA Requirements
| Tier | Target SLA | Design |
|------|-----------|--------|
| Web | 99.99% | Zone-redundant LB + 3 VMs |
| App | 99.95% | Zone-redundant App Service |
| Database | 99.99% | Zone-redundant SQL |

## 2. Regional Distribution
- Primary: East US (all zones)
- Secondary: West Europe (active-active)
- Global routing: Azure Front Door

## 3. Health Monitoring
- Health probes on all tiers
- Custom health endpoints with dependency checks
- Automatic failover on unhealthy

## 4. Failure Scenarios
| Failure | Detection | Recovery |
|---------|-----------|----------|
| VM failure | Health probe | LB routes to healthy VMs |
| Zone failure | Zone health | Traffic to other zones |
| Region failure | Front Door | Route to secondary region |
```

---

## ✅ Lab Checklist

- [ ] Calculated composite SLA for the architecture
- [ ] Designed zone-redundant deployment for all tiers
- [ ] Created multi-region active-active architecture
- [ ] Planned health probes and failover mechanisms
- [ ] Documented high availability design
