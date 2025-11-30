# 🧪 AZ-104 Practice Resources

## Official Microsoft Practice Assessment

The best way to prepare for the exam is with the official practice assessment.

### 📋 Microsoft Practice Assessment

| Resource | Details |
|----------|---------|
| **Link** | [AZ-104 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/practice/assessment?assessment-type=practice&assessmentId=21) |
| **Format** | Multiple choice, case studies |
| **Cost** | Free |
| **Questions** | 50+ questions |
| **Features** | Explanations, linked documentation |

**Benefits:**
- Experience actual exam format
- Learn from detailed explanations
- Identify knowledge gaps
- Track improvement over time

---

## 🎓 Exam Sandbox

Practice the exam interface before test day.

| Resource | Link |
|----------|------|
| Exam Sandbox | [Take Demo Exam](https://aka.ms/examdemo) |

**What to practice:**
- Question navigation
- Marking questions for review
- Time management
- Interface familiarity

---

## ☁️ Azure Sandbox Environments

### Azure Free Account

| Feature | Details |
|---------|---------|
| **Link** | [Create Free Account](https://azure.microsoft.com/free/) |
| **Credit** | $200 for 30 days |
| **Free Services** | 55+ always free services |
| **Duration** | 12 months for popular services |

### Microsoft Learn Sandbox

| Feature | Details |
|---------|---------|
| **Activation** | Included in Learn modules |
| **Cost** | Free |
| **Duration** | 4 hours per session |
| **Requires** | Microsoft account |

---

## 📚 Hands-On Labs by Topic

### Identity and Governance (20-25%)

| Lab | Skills Practiced |
|-----|-----------------|
| Create Entra ID users | User management, bulk creation |
| Configure Entra ID groups | Group types, membership |
| Implement RBAC | Role assignments, custom roles |
| Create Azure Policy | Policy definitions, initiatives |
| Manage subscriptions | Management groups, cost management |

### Storage (15-20%)

| Lab | Skills Practiced |
|-----|-----------------|
| Create storage accounts | Account types, replication |
| Configure blob storage | Containers, access tiers |
| Implement storage security | SAS tokens, access keys |
| Set up Azure Files | File shares, File Sync |
| Configure lifecycle management | Tier transitions, deletion |

### Compute (20-25%)

| Lab | Skills Practiced |
|-----|-----------------|
| Deploy Azure VMs | Create, configure, connect |
| Configure VM availability | Availability sets, zones |
| Implement scale sets | Autoscaling, instances |
| Deploy App Service | Web apps, deployment slots |
| Configure containers | ACI, container groups |

### Networking (15-20%)

| Lab | Skills Practiced |
|-----|-----------------|
| Configure virtual networks | VNets, subnets, IP addressing |
| Implement NSGs | Security rules, ASGs |
| Configure VNet peering | Peering connections |
| Set up VPN Gateway | Site-to-site, point-to-site |
| Configure load balancing | LB, Application Gateway |

### Monitoring and Backup (10-15%)

| Lab | Skills Practiced |
|-----|-----------------|
| Configure Azure Monitor | Metrics, diagnostics |
| Set up Log Analytics | Workspaces, KQL queries |
| Create alerts | Alert rules, action groups |
| Implement Azure Backup | Backup policies, recovery |
| Configure Network Watcher | Connectivity checks, NSG flow logs |

---

## 🔧 CLI and PowerShell Practice

### Azure CLI Examples

```bash
# Resource Groups
az group create --name myRG --location eastus
az group list --output table

# Virtual Machines
az vm create --resource-group myRG --name myVM --image Ubuntu2204 --admin-username azureuser
az vm list --output table

# Storage
az storage account create --name mystorageacct --resource-group myRG --sku Standard_LRS
az storage container create --name mycontainer --account-name mystorageacct

# Networking
az network vnet create --name myVNet --resource-group myRG --address-prefix 10.0.0.0/16
az network nsg create --name myNSG --resource-group myRG
```

### Azure PowerShell Examples

```powershell
# Resource Groups
New-AzResourceGroup -Name myRG -Location eastus
Get-AzResourceGroup | Format-Table

# Virtual Machines
New-AzVM -ResourceGroupName myRG -Name myVM -Image Ubuntu2204
Get-AzVM | Format-Table

# Storage
New-AzStorageAccount -ResourceGroupName myRG -Name mystorageacct -SkuName Standard_LRS -Location eastus
New-AzStorageContainer -Name mycontainer -Context $context

# Networking
New-AzVirtualNetwork -Name myVNet -ResourceGroupName myRG -AddressPrefix 10.0.0.0/16 -Location eastus
New-AzNetworkSecurityGroup -Name myNSG -ResourceGroupName myRG -Location eastus
```

---

## 📊 Knowledge Check Questions

### Identity and Governance

1. **What is the difference between Entra ID roles and Azure RBAC?**
2. **How do you create a custom RBAC role?**
3. **What is the scope hierarchy for RBAC?**
4. **How does Azure Policy differ from RBAC?**
5. **What are management groups used for?**

### Storage

1. **What are the storage account types?**
2. **How does storage replication (LRS, ZRS, GRS) work?**
3. **What is the difference between hot, cool, and archive tiers?**
4. **How do you secure access using SAS tokens?**
5. **What is Azure File Sync?**

### Compute

1. **What is the difference between availability sets and zones?**
2. **How do you configure VM scale sets for autoscaling?**
3. **What are the App Service plan tiers?**
4. **How do you use deployment slots?**
5. **When would you use Azure Container Instances?**

### Networking

1. **What is the difference between NSGs and Azure Firewall?**
2. **How does VNet peering work?**
3. **What are the VPN Gateway SKUs?**
4. **How do you configure Azure Load Balancer?**
5. **What is the difference between public and private endpoints?**

### Monitoring

1. **What is the difference between metrics and logs?**
2. **How do you write KQL queries?**
3. **What are action groups?**
4. **How does Azure Backup work with VMs?**
5. **What does Network Watcher provide?**

---

## 🎯 Study Tips

### Before the Exam

| Tip | Details |
|-----|---------|
| **Complete all learning paths** | Don't skip any modules |
| **Do hands-on labs** | Theory isn't enough |
| **Take practice assessments** | Multiple times |
| **Review explanations** | Learn from mistakes |
| **Focus on weak areas** | Use practice results |

### Exam Day Tips

| Tip | Details |
|-----|---------|
| **Read questions carefully** | Look for key words |
| **Manage time** | ~2 minutes per question |
| **Mark difficult questions** | Review later |
| **Don't leave blanks** | No penalty for guessing |
| **Trust your preparation** | Stay calm and focused |

---

## 📖 Additional Study Resources

### Documentation

| Resource | Link |
|----------|------|
| Azure Documentation | [Link](https://learn.microsoft.com/en-us/azure/) |
| Azure CLI Reference | [Link](https://learn.microsoft.com/en-us/cli/azure/) |
| Azure PowerShell Reference | [Link](https://learn.microsoft.com/en-us/powershell/azure/) |
| ARM Template Reference | [Link](https://learn.microsoft.com/en-us/azure/templates/) |

### Community Resources

| Resource | Description |
|----------|-------------|
| Microsoft Q&A | Official community forum |
| Stack Overflow | Azure-tagged questions |
| Reddit r/Azure | Community discussions |
| Azure GitHub | Sample code repositories |

### GitHub Repositories

| Repository | Link |
|------------|------|
| Azure Samples | [Link](https://github.com/Azure-Samples) |
| Azure Docs | [Link](https://github.com/MicrosoftDocs/azure-docs) |
| Azure CLI | [Link](https://github.com/Azure/azure-cli) |
| Azure PowerShell | [Link](https://github.com/Azure/azure-powershell) |

---

## ⏰ Recommended Study Timeline

### 4-Week Intensive Plan

| Week | Focus | Practice |
|------|-------|----------|
| Week 1 | Prerequisites + Identity | Practice assessment |
| Week 2 | Storage + Compute | Labs + practice |
| Week 3 | Networking | Labs + practice |
| Week 4 | Monitoring + Review | Full practice exams |

### 8-Week Standard Plan

| Weeks | Focus | Practice |
|-------|-------|----------|
| 1-2 | Prerequisites + Identity | Labs |
| 3-4 | Storage | Labs + practice |
| 5-6 | Compute + Networking | Labs + practice |
| 7-8 | Monitoring + Review | Full practice exams |

---

*Last updated: November 2025*
