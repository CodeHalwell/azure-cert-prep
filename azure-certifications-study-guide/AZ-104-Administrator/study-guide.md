# 📖 AZ-104 Study Guide

## Exam Overview

**Exam AZ-104: Microsoft Azure Administrator**

This comprehensive study guide covers all skills measured on the AZ-104 exam as of April 2025.

---

## Audience Profile

As an Azure administrator, you have subject matter expertise in implementing, managing, and monitoring an organization's Microsoft Azure environment, including:

- Virtual networks
- Storage
- Compute
- Identity
- Security
- Governance

You often serve as part of a larger team and coordinate with other roles to deliver Azure solutions.

**Required Skills:**
- Operating systems
- Networking
- Servers and virtualization
- PowerShell and Azure CLI
- Azure portal and ARM templates
- Microsoft Entra ID

---

## Skills Measured (April 2025)

### 1. Manage Azure Identities and Governance (20-25%)

#### 1.1 Manage Microsoft Entra Users and Groups

| Task | Description |
|------|-------------|
| Create users and groups | Portal, PowerShell, CLI methods |
| Manage properties | User/group attributes |
| Manage licenses | Assign and manage M365/Azure licenses |
| External users | B2B guest access |
| SSPR | Self-service password reset |

**PowerShell Examples:**
```powershell
# Create a new user
New-AzADUser -DisplayName "John Doe" `
    -UserPrincipalName "john@contoso.com" `
    -Password (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force)

# Create a group
New-AzADGroup -DisplayName "IT Admins" -MailNickname "ITAdmins"
```

#### 1.2 Manage Access to Azure Resources

**RBAC Concepts:**

| Concept | Description |
|---------|-------------|
| Security Principal | Who (user, group, service principal, managed identity) |
| Role Definition | What permissions (Reader, Contributor, Owner, custom) |
| Scope | Where (management group, subscription, resource group, resource) |
| Role Assignment | Combines principal + role + scope |

**Built-in Roles:**
- **Owner**: Full access + assign roles
- **Contributor**: Full access, can't assign roles
- **Reader**: View only
- **User Access Administrator**: Manage access only

```powershell
# Assign a role
New-AzRoleAssignment -ObjectId <user-id> `
    -RoleDefinitionName "Contributor" `
    -ResourceGroupName "myResourceGroup"
```

#### 1.3 Manage Azure Subscriptions and Governance

**Azure Policy:**
- Enforce organizational standards
- Assess compliance
- Apply at scale with initiatives

**Resource Locks:**
| Lock Type | Effect |
|-----------|--------|
| ReadOnly | Prevent modifications |
| CanNotDelete | Prevent deletion |

**Tags:**
- Organize resources
- Cost tracking
- Governance enforcement

**Management Groups:**
- Organize subscriptions hierarchically
- Apply policy at scale
- Centralized governance

---

### 2. Implement and Manage Storage (15-20%)

#### 2.1 Configure Access to Storage

| Feature | Description |
|---------|-------------|
| Firewalls | IP-based access control |
| Virtual Networks | Service endpoints, private endpoints |
| SAS Tokens | Time-limited access |
| Stored Access Policies | Manage SAS at account level |
| Access Keys | Full account access |
| Entra ID | Identity-based access for Blob/Files |

**SAS Token Types:**
- Account SAS
- Service SAS
- User delegation SAS (recommended)

#### 2.2 Configure and Manage Storage Accounts

| Setting | Options |
|---------|---------|
| Performance | Standard, Premium |
| Redundancy | LRS, ZRS, GRS, GZRS, RA-GRS, RA-GZRS |
| Access Tier | Hot, Cool, Cold, Archive |
| Encryption | Microsoft-managed or customer-managed keys |

**Replication Options:**

| Type | Description |
|------|-------------|
| LRS | 3 copies, single datacenter |
| ZRS | 3 copies, 3 availability zones |
| GRS | 6 copies, 2 regions |
| GZRS | ZRS + GRS |

#### 2.3 Configure Azure Files and Blob Storage

**Azure Blob Storage:**
- Block blobs (files)
- Append blobs (logs)
- Page blobs (VHDs)

**Azure Files:**
- SMB/NFS file shares
- Mountable on Windows/Linux/macOS
- Azure File Sync for hybrid scenarios

**Lifecycle Management:**
- Automatic tiering
- Deletion policies
- Blob versioning

---

### 3. Deploy and Manage Azure Compute Resources (20-25%)

#### 3.1 Create and Configure Virtual Machines

**VM Components:**

| Component | Description |
|-----------|-------------|
| Size | CPU, memory, disk capacity |
| Image | OS and pre-installed software |
| Disk | OS disk, data disks |
| Networking | NIC, public IP, NSG |
| Extensions | Post-deployment configuration |

**Availability Options:**

| Option | SLA | Description |
|--------|-----|-------------|
| Availability Set | 99.95% | Fault/update domains |
| Availability Zone | 99.99% | Separate datacenters |
| Virtual Machine Scale Sets | 99.95%+ | Auto-scaling VM groups |

**VM Extensions:**
- Custom Script Extension
- Azure Monitor Agent
- DSC Extension
- Azure AD Login

#### 3.2 Configure Virtual Machine Availability

**Scale Sets:**
```powershell
# Create VMSS
New-AzVmss -ResourceGroupName "myRG" `
    -VMScaleSetName "myScaleSet" `
    -Location "EastUS" `
    -InstanceCount 3 `
    -Image "Win2019Datacenter"
```

**Autoscaling:**
- Metric-based (CPU, memory, custom)
- Schedule-based
- Predictive scaling

#### 3.3 Configure Azure App Service

| Plan Tier | Features |
|-----------|----------|
| Free/Shared | Development, limited resources |
| Basic | Custom domains, manual scale |
| Standard | Auto-scale, staging slots |
| Premium | Better performance, more slots |
| Isolated | VNet integration, dedicated |

**Deployment Slots:**
- Test in production-like environment
- Zero-downtime deployments
- Traffic routing

#### 3.4 Configure Azure Container Instances

```bash
# Create container instance
az container create \
    --resource-group myRG \
    --name mycontainer \
    --image nginx \
    --ports 80 \
    --dns-name-label myapp
```

---

### 4. Implement and Manage Virtual Networking (15-20%)

#### 4.1 Configure Virtual Networks

**VNet Components:**

| Component | Description |
|-----------|-------------|
| Address Space | CIDR range (e.g., 10.0.0.0/16) |
| Subnet | Network segment within VNet |
| NSG | Stateful firewall rules |
| Route Table | Custom routing |
| Service Endpoint | Direct connectivity to PaaS |
| Private Endpoint | Private IP for PaaS |

**Subnet Reserved Addresses:**
- .0 - Network address
- .1 - Gateway
- .2-.3 - Azure DNS
- .255 - Broadcast

#### 4.2 Configure Network Security Groups

**NSG Rules:**

| Property | Description |
|----------|-------------|
| Priority | 100-4096 (lower = higher priority) |
| Source/Destination | IP, tag, or * |
| Protocol | TCP, UDP, ICMP, Any |
| Port | Single, range, or * |
| Action | Allow or Deny |

**Default Rules:**
- AllowVNetInBound (65000)
- AllowAzureLoadBalancerInBound (65001)
- DenyAllInBound (65500)

#### 4.3 Configure Load Balancing

**Azure Load Balancer:**
- Layer 4 (TCP/UDP)
- Internal or public
- Health probes
- Load balancing rules

**Application Gateway:**
- Layer 7 (HTTP/HTTPS)
- SSL termination
- URL-based routing
- WAF capability

**Traffic Manager:**
- DNS-based load balancing
- Geographic routing
- Failover scenarios

#### 4.4 Configure VPN and ExpressRoute

**VPN Gateway:**

| SKU | Connections | Throughput |
|-----|-------------|------------|
| Basic | 10 S2S | 100 Mbps |
| VpnGw1 | 30 S2S | 650 Mbps |
| VpnGw2 | 30 S2S | 1 Gbps |
| VpnGw3 | 30 S2S | 1.25 Gbps |

**Connection Types:**
- Site-to-Site (S2S)
- Point-to-Site (P2S)
- VNet-to-VNet

---

### 5. Monitor and Maintain Azure Resources (10-15%)

#### 5.1 Azure Monitor

**Components:**

| Component | Description |
|-----------|-------------|
| Metrics | Numerical time-series data |
| Logs | Structured log data |
| Alerts | Notifications on conditions |
| Dashboards | Visualizations |
| Workbooks | Interactive reports |

**Log Analytics:**
- Kusto Query Language (KQL)
- Workspace-based storage
- Cross-resource queries

**Sample KQL:**
```kusto
// VM CPU usage over time
Perf
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| summarize avg(CounterValue) by bin(TimeGenerated, 5m), Computer
| render timechart
```

#### 5.2 Azure Backup

**Supported Workloads:**
- Azure VMs
- Azure Files
- SQL in Azure VMs
- SAP HANA
- Azure Blobs

**Backup Policies:**
- Frequency (daily, weekly)
- Retention (days, weeks, months, years)
- Instant recovery

#### 5.3 Site Recovery

- Disaster recovery for VMs
- Replication to secondary region
- Failover and failback
- Recovery plans

---

## Exam Preparation Resources

### Official Resources

| Resource | Link |
|----------|------|
| Exam Page | [AZ-104](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/) |
| Study Guide | [Study Guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104) |
| Practice Assessment | [Free Practice Test](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/practice/assessment?assessment-type=practice&assessmentId=21) |
| Learning Paths | [AZ-104 Training](https://learn.microsoft.com/en-us/training/paths/az-104-administrator-prerequisites/) |

### Azure CLI vs PowerShell

Both are tested on the exam. Know the equivalent commands:

| Task | Azure CLI | PowerShell |
|------|-----------|------------|
| Create RG | `az group create` | `New-AzResourceGroup` |
| Create VM | `az vm create` | `New-AzVM` |
| Create Storage | `az storage account create` | `New-AzStorageAccount` |

---

*Last updated: November 2025*
