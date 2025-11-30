# Lab 05: Design Backup and Disaster Recovery Strategy

## 🎯 Lab Goal

Design a **backup and disaster recovery strategy**:

- Define RTO/RPO requirements
- Select appropriate backup solutions
- Design cross-region disaster recovery

This supports the **Design business continuity solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of Azure Backup and Site Recovery

---

## Scenario

Contoso requires:
- VMs: RPO 1 hour, RTO 4 hours
- Databases: RPO 5 minutes, RTO 1 hour
- File shares: RPO 24 hours, RTO 8 hours
- Full DR capability to secondary region

---

## Step 1 – Define Recovery Objectives

### Key Metrics:

| Metric | Definition | Business Impact |
|--------|------------|----------------|
| RTO | Recovery Time Objective | Max downtime tolerated |
| RPO | Recovery Point Objective | Max data loss tolerated |

### Contoso Requirements:

| Workload | RPO | RTO | Tier |
|----------|-----|-----|------|
| E-commerce VMs | 1 hour | 4 hours | High |
| SQL Databases | 5 minutes | 1 hour | Critical |
| File Shares | 24 hours | 8 hours | Medium |
| Archive Data | 7 days | 72 hours | Low |

---

## Step 2 – Design Azure Backup Strategy

### Backup Solutions:

| Resource | Solution | Frequency |
|----------|----------|----------|
| Azure VMs | Azure Backup | Daily |
| SQL Database | Automated backup + LTR | Continuous |
| Azure Files | Azure Backup | Daily |
| Blobs | Soft delete + versioning | Continuous |

### Create Recovery Services Vault:

```bash
az backup vault create \
  --name rsv-contoso-backup \
  --resource-group rg-backup \
  --location eastus
```

### Configure VM Backup Policy:

```bash
az backup policy create \
  --vault-name rsv-contoso-backup \
  --resource-group rg-backup \
  --name policy-vm-daily \
  --policy '{"schedulePolicy":{"schedulePolicyType":"SimpleSchedulePolicy","scheduleRunFrequency":"Daily","scheduleRunTimes":["2024-01-01T02:00:00Z"]},"retentionPolicy":{"retentionPolicyType":"LongTermRetentionPolicy","dailySchedule":{"retentionDuration":{"count":30,"durationType":"Days"}}}}'
```

---

## Step 3 – Design Disaster Recovery Architecture

### Azure Site Recovery for VMs:

```
Primary Region (East US)          Secondary Region (West US)
├── VM-Web-1          ──ASR──→    VM-Web-1 (replica)
├── VM-Web-2          ──ASR──→    VM-Web-2 (replica)
└── VM-App-1          ──ASR──→    VM-App-1 (replica)
```

### Enable replication:

```bash
az site-recovery protected-item create \
  --vault-name rsv-contoso-dr \
  --resource-group rg-dr \
  --fabric-name primary-fabric \
  --protection-container primary-container \
  --name vm-web-1 \
  --policy-id <replication-policy-id>
```

### Failover Types:

| Type | Use Case |
|------|----------|
| Test Failover | DR drill, no impact |
| Planned Failover | Maintenance, graceful |
| Unplanned Failover | Actual disaster |

---

## Step 4 – Design Database DR

### SQL Database:

- **Auto-failover groups** for automatic failover
- **Active geo-replication** for read-scale and manual failover

```bash
az sql failover-group create \
  --name fg-contoso-sql \
  --resource-group rg-primary \
  --server sql-contoso-primary \
  --partner-server sql-contoso-secondary \
  --failover-policy Automatic \
  --grace-period 1
```

### Cosmos DB:

- Multi-region deployment with automatic failover
- Configure failover priority

---

## Step 5 – Design Document

```markdown
# Backup & DR Architecture – Contoso Ltd.

## 1. Recovery Objectives
[Table from Step 1]

## 2. Backup Strategy
| Resource | Solution | Retention |
|----------|----------|----------|
| VMs | Azure Backup | 30 days daily, 12 months monthly |
| SQL | Automated + LTR | 35 days PITR, 10 years LTR |
| Files | Azure Backup | 30 days |

## 3. DR Strategy
- Primary: East US
- Secondary: West US
- ASR for all production VMs
- SQL auto-failover groups
- Cosmos DB multi-region

## 4. DR Procedures
- Quarterly DR drills
- Runbooks in Azure Automation
- Documented failover/failback procedures

## 5. Monitoring
- Backup alerts for failures
- ASR health monitoring
- RPO/RTO dashboards
```

---

## ✅ Lab Checklist

- [ ] Defined RTO/RPO for all workloads
- [ ] Designed Azure Backup policies for VMs and databases
- [ ] Created ASR disaster recovery architecture
- [ ] Planned database DR with failover groups
- [ ] Documented backup and DR strategy
