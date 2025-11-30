# Lab 10: Design Migration Strategy

## 🎯 Lab Goal

Design a **migration strategy** for moving to Azure:

- Assess workloads for migration
- Select migration approaches (rehost, refactor, etc.)
- Plan migration waves and cutover

This supports the **Design migrations** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of Azure Migrate and migration patterns

---

## Scenario

Contoso is migrating from on-premises:
- 50 Windows/Linux VMs
- 10 SQL Server databases
- 5 web applications
- Legacy mainframe integration

Timeline: 12 months

---

## Step 1 – Assess Current State

### Discovery with Azure Migrate:

```bash
# Create Azure Migrate project
az resource create \
  --resource-group rg-migration \
  --resource-type Microsoft.Migrate/migrateProjects \
  --name migrate-contoso \
  --location eastus \
  --properties '{}'
```

### Assessment Categories:

| Category | Tool | Output |
|----------|------|--------|
| VM discovery | Azure Migrate appliance | Inventory |
| Dependency mapping | Service Map | Dependencies |
| Database assessment | Data Migration Assistant | Compatibility |
| Web app assessment | App Service Migration Assistant | Readiness |

### Assessment Report:

| Workload | VMs | Databases | Complexity |
|----------|-----|-----------|------------|
| ERP | 15 | 3 | High |
| E-commerce | 10 | 2 | Medium |
| Internal apps | 20 | 4 | Low |
| Legacy | 5 | 1 | Very High |

---

## Step 2 – Select Migration Strategy (5 Rs)

### Migration Approaches:

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| Rehost | Lift and shift | Quick migration, minimal change |
| Refactor | Minimal code changes | Containerize, use PaaS |
| Rearchitect | Significant changes | Cloud-native transformation |
| Rebuild | Rewrite from scratch | Legacy with no path forward |
| Replace | Adopt SaaS | Commodity workloads |

### Contoso Decisions:

| Workload | Strategy | Target |
|----------|----------|--------|
| ERP VMs | Rehost | Azure VMs |
| E-commerce | Refactor | App Service + SQL DB |
| Internal apps | Rehost | Azure VMs → Refactor later |
| Legacy | Replace | SaaS alternative or API wrapper |

---

## Step 3 – Design Migration Waves

### Wave Planning:

```
Wave 0 (Month 1-2): Foundation
  • Landing zone setup
  • Network connectivity
  • Identity (Entra Connect)

Wave 1 (Month 3-4): Low Risk
  • Internal apps (20 VMs)
  • Non-critical databases

Wave 2 (Month 5-7): Medium Risk
  • E-commerce (refactor)
  • Supporting services

Wave 3 (Month 8-10): High Risk
  • ERP system
  • Critical databases

Wave 4 (Month 11-12): Cleanup
  • Legacy remediation
  • Decommission on-prem
```

---

## Step 4 – Design Database Migration

### Migration Options:

| Source | Target | Method |
|--------|--------|--------|
| SQL Server | Azure SQL DB | DMS (online) |
| SQL Server | SQL MI | DMS (online) |
| SQL Server | SQL on VM | Backup/restore |
| Oracle | PostgreSQL | Ora2Pg + DMS |

### Azure Database Migration Service:

```bash
az dms create \
  --name dms-contoso \
  --resource-group rg-migration \
  --location eastus \
  --sku-name Premium_4vCores \
  --subnet <subnet-id>
```

### Migration Steps:
1. Assess compatibility (DMA)
2. Pre-migration fixes
3. Schema migration
4. Data migration (initial + continuous sync)
5. Cutover (minimal downtime)
6. Validation

---

## Step 5 – Design Document

```markdown
# Migration Strategy – Contoso Ltd.

## 1. Assessment Summary
- 50 VMs, 10 databases, 5 web apps
- 80% suitable for rehost/refactor
- 20% require rearchitect/replace

## 2. Migration Approach
| Workload | Strategy | Target | Timeline |
|----------|----------|--------|----------|
| ERP | Rehost | VMs | Wave 3 |
| E-commerce | Refactor | App Service | Wave 2 |
| Internal | Rehost | VMs | Wave 1 |
| Legacy | Replace | SaaS | Wave 4 |

## 3. Wave Schedule
[Timeline from Step 3]

## 4. Tools
- Azure Migrate for discovery and VM migration
- DMS for database migration
- App Service Migration Assistant for web apps

## 5. Success Criteria
- < 4 hours downtime per workload
- Zero data loss
- Performance parity or better
- Security compliance maintained

## 6. Rollback Plan
- Maintain on-prem for 30 days post-migration
- DNS-based failback capability
- Tested rollback procedures
```

---

## ✅ Lab Checklist

- [ ] Assessed workloads using Azure Migrate
- [ ] Selected migration strategy for each workload (5 Rs)
- [ ] Designed migration waves with timeline
- [ ] Planned database migration approach
- [ ] Documented comprehensive migration strategy
