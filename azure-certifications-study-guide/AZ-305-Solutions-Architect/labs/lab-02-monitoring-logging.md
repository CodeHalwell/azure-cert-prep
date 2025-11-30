# Lab 02: Design Monitoring and Logging Architecture

## 🎯 Lab Goal

Design an **enterprise monitoring and logging architecture**:

- Centralize logs with Log Analytics
- Design alerts and dashboards
- Plan Application Insights integration

This supports the **Design identity, governance, and monitoring solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of Azure Monitor components

---

## Scenario

Contoso needs:
- Centralized logging across 3 subscriptions
- Proactive alerting for critical issues
- Application performance monitoring
- 90-day log retention for compliance

---

## Step 1 – Design Log Analytics Workspace Strategy

### Options:

| Strategy | Pros | Cons |
|----------|------|------|
| Single workspace | Simple queries, unified view | Less isolation |
| Workspace per subscription | Isolation, cost allocation | Complex cross-workspace queries |
| Hybrid (by environment) | Balance of both | Moderate complexity |

### Recommendation:

**Hybrid approach** – One workspace per environment:
- `law-contoso-prod` (Production)
- `law-contoso-nonprod` (Dev + Test)

```bash
az monitor log-analytics workspace create \
  --resource-group rg-monitoring \
  --workspace-name law-contoso-prod \
  --location eastus \
  --retention-time 90
```

---

## Step 2 – Configure Diagnostic Settings

### Resources to Monitor:

| Resource Type | Logs | Metrics |
|---------------|------|--------|
| App Service | HTTPLogs, AppServiceAuditLogs | Requests, Response Time |
| SQL Database | SQLSecurityAuditEvents, Errors | DTU, CPU |
| Key Vault | AuditEvent | Availability |
| Virtual Machines | Security, System events | CPU, Memory, Disk |

### Enable via Policy:

```bash
az policy assignment create \
  --name deploy-diagnostics \
  --policy "<policy-definition-id>" \
  --scope "/subscriptions/<subscription-id>" \
  --params '{"logAnalyticsWorkspace": "<workspace-resource-id>"}'
```

---

## Step 3 – Design Alert Strategy

### Alert Categories:

| Category | Example | Action |
|----------|---------|--------|
| Availability | Resource health changes | Email + Teams |
| Performance | CPU > 90% for 5 min | Auto-scale + Alert |
| Security | Suspicious sign-in | SIEM integration |
| Cost | Budget threshold reached | Email |

### Create action group:

```bash
az monitor action-group create \
  --name ag-critical \
  --resource-group rg-monitoring \
  --short-name Critical \
  --email-receiver name=OnCall email=oncall@contoso.com
```

### Create alert rule:

```bash
az monitor metrics alert create \
  --name "High CPU Alert" \
  --resource-group rg-monitoring \
  --scopes <vm-resource-id> \
  --condition "avg Percentage CPU > 90" \
  --action ag-critical
```

---

## Step 4 – Design Application Insights Strategy

### Workspace-based vs. Classic:

- Always use **workspace-based** Application Insights
- Connect to the same Log Analytics workspace for unified querying

### Instrumentation approach:

| App Type | Method |
|----------|--------|
| .NET / Java | Auto-instrumentation or SDK |
| Containers | OpenTelemetry Collector |
| Functions | Built-in integration |

---

## Step 5 – Design Document

```markdown
# Monitoring Architecture – Contoso Ltd.

## 1. Log Analytics Workspaces
- law-contoso-prod (90-day retention)
- law-contoso-nonprod (30-day retention)

## 2. Data Sources
- All PaaS resources via diagnostic settings
- VMs via Azure Monitor Agent
- Applications via Application Insights

## 3. Alert Strategy
- Critical alerts → Action Group → PagerDuty
- Warning alerts → Email
- Informational → Log only

## 4. Dashboards
- Executive: SLA compliance, availability
- Operations: Performance, errors
- Security: Sign-ins, access anomalies
```

---

## ✅ Lab Checklist

- [ ] Designed Log Analytics workspace topology
- [ ] Planned diagnostic settings for key resource types
- [ ] Created alert strategy with action groups
- [ ] Designed Application Insights integration
- [ ] Documented monitoring architecture
