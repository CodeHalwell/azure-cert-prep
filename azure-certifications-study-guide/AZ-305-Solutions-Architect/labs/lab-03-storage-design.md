# Lab 03: Design Data Storage Architecture

## 🎯 Lab Goal

Design a **data storage architecture** for various workloads:

- Select appropriate storage services
- Design for performance, cost, and security
- Plan data lifecycle and redundancy

This supports the **Design data storage solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of Azure storage services

---

## Scenario

Contoso needs storage for:
- Application files (images, documents) – 10 TB
- Archive data (compliance) – 50 TB, accessed rarely
- High-performance file shares for VMs – 500 GB
- Analytics data lake – 100 TB

---

## Step 1 – Select Storage Services

| Requirement | Service | Tier |
|-------------|---------|------|
| App files | Blob Storage | Hot |
| Archive data | Blob Storage | Archive |
| VM file shares | Azure Files | Premium |
| Analytics | Data Lake Gen2 | Hot |

### Decision Matrix:

| Factor | Blob | Files | Data Lake Gen2 |
|--------|------|-------|----------------|
| Unstructured data | ✓ | | ✓ |
| Hierarchical namespace | | | ✓ |
| SMB/NFS protocol | | ✓ | |
| Big data analytics | | | ✓ |

---

## Step 2 – Design Redundancy Strategy

| Workload | Redundancy | Reason |
|----------|------------|--------|
| App files | GRS | Business critical, DR required |
| Archive | LRS | Cost-sensitive, low access |
| File shares | ZRS | High availability in-region |
| Data lake | GRS | Analytics source of truth |

---

## Step 3 – Design Lifecycle Management

```json
{
  "rules": [
    {
      "name": "moveToArchive",
      "type": "Lifecycle",
      "definition": {
        "actions": {
          "baseBlob": {
            "tierToArchive": {"daysAfterModificationGreaterThan": 365}
          }
        },
        "filters": {
          "blobTypes": ["blockBlob"],
          "prefixMatch": ["documents/"]
        }
      }
    }
  ]
}
```

---

## Step 4 – Design Security Controls

### Access Control:

| Layer | Control |
|-------|--------|
| Network | Private endpoints, service endpoints |
| Identity | Entra ID RBAC, managed identities |
| Data | Encryption at rest (CMK), encryption in transit |
| Access | SAS tokens with limited scope/expiry |

### Enable private endpoint:

```bash
az storage account update \
  --name stcontosodata \
  --resource-group rg-storage \
  --default-action Deny

az network private-endpoint create \
  --name pe-storage \
  --resource-group rg-storage \
  --vnet-name vnet-main \
  --subnet subnet-private \
  --private-connection-resource-id <storage-account-id> \
  --group-id blob
```

---

## Step 5 – Design Document

```markdown
# Storage Architecture – Contoso Ltd.

## 1. Storage Accounts
| Account | Purpose | SKU | Redundancy |
|---------|---------|-----|------------|
| stcontosoapp | App files | Standard | GRS |
| stcontosoarchive | Compliance | Standard | LRS |
| stcontosopremium | File shares | Premium | ZRS |
| dlcontosodatalake | Analytics | Standard | GRS |

## 2. Security
- Private endpoints for all accounts
- Customer-managed keys in Key Vault
- No public access

## 3. Lifecycle Policies
- Hot → Cool after 30 days
- Cool → Archive after 365 days
- Delete after 7 years

## 4. Cost Optimization
- Reserved capacity for predictable workloads
- Archive tier for compliance data
```

---

## ✅ Lab Checklist

- [ ] Selected appropriate storage services for each workload
- [ ] Designed redundancy strategy based on requirements
- [ ] Created lifecycle management policies
- [ ] Planned security controls including private endpoints
- [ ] Documented storage architecture
