# 🔬 AZ-104 Labs Directory

## Overview

This directory contains hands-on lab exercises for the AZ-104: Microsoft Azure Administrator certification.

---

## 📁 Lab Files Index

| Lab | File | Skill Domain |
|-----|------|--------------|
| Lab 01 | `lab-01-entra-id.md` | Identity & Governance |
| Lab 02 | `lab-02-rbac.md` | Identity & Governance |
| Lab 03 | `lab-03-azure-policy.md` | Identity & Governance |
| Lab 04 | `lab-04-storage-accounts.md` | Storage |
| Lab 05 | `lab-05-blob-storage.md` | Storage |
| Lab 06 | `lab-06-azure-vms.md` | Compute |
| Lab 07 | `lab-07-scale-sets.md` | Compute |
| Lab 08 | `lab-08-virtual-networks.md` | Networking |
| Lab 09 | `lab-09-load-balancing.md` | Networking |
| Lab 10 | `lab-10-azure-monitor.md` | Monitor & Backup |

---

## 🎯 Lab Objectives by Skill Domain

### Identity and Governance (20-25%)

| Lab | Skills |
|-----|--------|
| Lab 01 | Manage Entra ID users and groups, configure self-service password reset |
| Lab 02 | Implement RBAC, create custom roles, manage role assignments |
| Lab 03 | Create Azure Policy definitions, initiatives, and assignments |

### Implement and Manage Storage (15-20%)

| Lab | Skills |
|-----|--------|
| Lab 04 | Configure storage accounts, replication, access tiers |
| Lab 05 | Manage blob containers, lifecycle policies, access control |

### Deploy and Manage Compute (20-25%)

| Lab | Skills |
|-----|--------|
| Lab 06 | Deploy and configure VMs, availability sets, managed disks |
| Lab 07 | Configure VM scale sets, autoscaling, update domains |

### Configure and Manage Virtual Networking (15-20%)

| Lab | Skills |
|-----|--------|
| Lab 08 | Configure VNets, subnets, NSGs, peering |
| Lab 09 | Implement Azure Load Balancer, Application Gateway |

### Monitor and Maintain Azure Resources (10-15%)

| Lab | Skills |
|-----|--------|
| Lab 10 | Configure Azure Monitor, alerts, Log Analytics |

---

## 🛠️ Prerequisites

Before starting the labs, ensure you have:

| Requirement | Description |
|-------------|-------------|
| Azure Subscription | Free account or existing subscription |
| Azure CLI | Latest version installed |
| Azure PowerShell | Az module installed |
| VS Code | With Azure extensions |
| Browser | Modern browser for Azure Portal |

### Setup Commands

```bash
# Install Azure CLI
# See https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

# Install Azure PowerShell
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force

# Login to Azure
az login
Connect-AzAccount
```

---

## 📋 Lab Completion Checklist

### Week 1-2: Identity & Governance
- [ ] Lab 01: Entra ID management
- [ ] Lab 02: RBAC configuration
- [ ] Lab 03: Azure Policy implementation

### Week 3-4: Storage
- [ ] Lab 04: Storage account setup
- [ ] Lab 05: Blob storage management

### Week 5-6: Compute
- [ ] Lab 06: VM deployment
- [ ] Lab 07: Scale set configuration

### Week 7: Networking
- [ ] Lab 08: Virtual network setup
- [ ] Lab 09: Load balancing implementation

### Week 8: Monitoring
- [ ] Lab 10: Azure Monitor configuration

---

## 🔗 Additional Lab Resources

| Resource | Link |
|----------|------|
| Microsoft Learn Labs | [Link](https://learn.microsoft.com/en-us/training/browse/?products=azure&resource_type=learning%20path) |
| Azure Free Account | [Link](https://azure.microsoft.com/free/) |
| Azure Sandbox | [Link](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/4-exercise-explore-learn-sandbox) |
| GitHub: Azure Samples | [Link](https://github.com/Azure-Samples) |

---

## ⚠️ Important Notes

1. **Clean up resources** after each lab to avoid unexpected charges
2. **Use resource naming conventions** for organization
3. **Document your work** as you complete each lab
4. **Take screenshots** of key configurations
5. **Review error messages** - understanding failures is valuable learning

### Resource Cleanup Command

```bash
# Delete resource group and all resources
az group delete --name <resource-group-name> --yes --no-wait
```

---

*Last updated: November 2025*
