# 🔧 AZ-104 Azure Resources Reference

## Complete Guide to Azure Resources for Administrators

This document provides detailed explanations of all Azure resources covered in the AZ-104 exam.

---

## 📋 Table of Contents

1. [Identity and Access Management](#identity-and-access-management)
2. [Virtual Networking](#virtual-networking)
3. [Compute Resources](#compute-resources)
4. [Storage Resources](#storage-resources)
5. [Monitoring and Backup](#monitoring-and-backup)

---

# Identity and Access Management

## 1. Microsoft Entra ID (Azure AD)

### What It Does

| Capability | Description |
|------------|-------------|
| **Identity management** | User and group management |
| **Authentication** | MFA, passwordless, SSO |
| **Application integration** | Enterprise app management |
| **Conditional Access** | Risk-based access control |
| **B2B/B2C** | External identity |

### Built-in Features

| Feature | Free | P1 | P2 |
|---------|------|-----|-----|
| User/group management | ✅ | ✅ | ✅ |
| SSO (unlimited apps) | ✅ | ✅ | ✅ |
| MFA | ✅ | ✅ | ✅ |
| Conditional Access | ❌ | ✅ | ✅ |
| PIM | ❌ | ❌ | ✅ |
| Identity Protection | ❌ | ❌ | ✅ |
| Access Reviews | ❌ | ❌ | ✅ |

### Customization Options

| Customization | How | Use Case |
|---------------|-----|----------|
| **Custom domains** | Add and verify | Branded sign-in |
| **Company branding** | Logo, colors, text | User experience |
| **Custom roles** | Define permissions | Granular access |
| **Dynamic groups** | Rule-based membership | Auto assignment |

### Limitations

| Limitation | Free | P1/P2 |
|------------|------|-------|
| Objects | 500,000 | 500,000 (expandable) |
| Conditional Access policies | 0 | 195 |
| Custom roles | 0 | 5,000 |
| App registrations | 100 | Unlimited |

---

## 2. Role-Based Access Control (RBAC)

### Built-in Roles

| Role | Scope | Permissions |
|------|-------|-------------|
| **Owner** | Full | Full access + assign roles |
| **Contributor** | Full | Full access, no role assignment |
| **Reader** | Read | View only |
| **User Access Administrator** | RBAC | Manage role assignments |

### Common Service Roles

| Role | Service | Permissions |
|------|---------|-------------|
| Virtual Machine Contributor | VMs | Manage VMs, not VNet/storage |
| Storage Blob Data Contributor | Storage | Read/write blobs |
| Network Contributor | Network | Manage networking |
| Key Vault Administrator | Key Vault | Full Key Vault access |
| Monitoring Contributor | Monitor | Manage monitoring |

### Custom Roles

| Property | Description | Limit |
|----------|-------------|-------|
| Actions | Allowed operations | Multiple |
| NotActions | Excluded operations | Multiple |
| DataActions | Data plane operations | Multiple |
| AssignableScopes | Where assignable | Subscription/RG/Resource |

### Limitations

| Limitation | Details |
|------------|---------|
| Custom roles per tenant | 5,000 |
| Role assignments per subscription | 4,000 |
| Role assignment scope | Management group, subscription, RG, resource |

---

# Virtual Networking

## 1. Virtual Network (VNet)

### What It Does

| Capability | Description |
|------------|-------------|
| **Isolation** | Private network in Azure |
| **Subnets** | Segment network |
| **IP addressing** | Private/public IPs |
| **DNS** | Name resolution |
| **Routing** | Traffic flow control |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Azure DNS | ✅ Yes | Free with VNet |
| DDoS Basic | ✅ Yes | Free protection |
| Service endpoints | ✅ Yes | Free to enable |
| Private DNS zones | ✅ Yes | Separate resource |

### Customization Options

| Customization | Purpose | How |
|---------------|---------|-----|
| **Custom DNS** | Use own DNS servers | Configure in VNet |
| **User-defined routes** | Custom routing | Create route tables |
| **Network Security Groups** | Traffic filtering | Create and associate |
| **Peering** | Connect VNets | Create peering |

### Limitations

| Limitation | Details |
|------------|---------|
| VNets per subscription | 1,000 |
| Subnets per VNet | 3,000 |
| Private IPs per VNet | 65,536 |
| Peerings per VNet | 500 |
| Address spaces per VNet | 100 |

### Reserved Addresses (per subnet)

| Address | Purpose |
|---------|---------|
| x.x.x.0 | Network address |
| x.x.x.1 | Default gateway |
| x.x.x.2-3 | Azure DNS |
| x.x.x.255 | Broadcast |

---

## 2. Network Security Groups (NSG)

### What It Does

| Capability | Description |
|------------|-------------|
| **Traffic filtering** | Allow/deny rules |
| **Stateful** | Return traffic automatic |
| **Association** | Subnet or NIC level |
| **Prioritized** | Rules evaluated by priority |

### Default Rules

| Rule | Priority | Direction | Action |
|------|----------|-----------|--------|
| AllowVNetInBound | 65000 | Inbound | Allow |
| AllowAzureLoadBalancerInBound | 65001 | Inbound | Allow |
| DenyAllInBound | 65500 | Inbound | Deny |
| AllowVNetOutBound | 65000 | Outbound | Allow |
| AllowInternetOutBound | 65001 | Outbound | Allow |
| DenyAllOutBound | 65500 | Outbound | Deny |

### Rule Components

| Component | Description | Values |
|-----------|-------------|--------|
| Priority | Processing order | 100-4096 |
| Source | Traffic origin | IP, CIDR, Tag, ASG |
| Destination | Traffic target | IP, CIDR, Tag, ASG |
| Protocol | Network protocol | TCP, UDP, ICMP, Any |
| Port | Destination port | Single, range, * |
| Action | Allow or Deny | Allow, Deny |

### Limitations

| Limitation | Details |
|------------|---------|
| NSGs per subscription | 5,000 |
| Rules per NSG | 1,000 |
| NSGs per subnet | 1 |
| NSGs per NIC | 1 |

---

## 3. Azure Load Balancer

### SKU Comparison

| Feature | Basic | Standard |
|---------|-------|----------|
| Backend pool size | 300 | 1,000 |
| Health probes | TCP, HTTP | TCP, HTTP, HTTPS |
| Availability Zones | ❌ | ✅ |
| HA Ports | ❌ | ✅ |
| SLA | None | 99.99% |
| Price | Free | Charged |

### Built-in Features

| Feature | Description |
|---------|-------------|
| Load balancing rules | Distribute traffic |
| NAT rules | Port forwarding |
| Outbound rules | SNAT configuration |
| Health probes | Backend health check |

### Limitations

| Limitation | Basic | Standard |
|------------|-------|----------|
| Frontend IPs | 200 | 600 |
| Backend pools | 1 | Multiple |
| Availability Zones | ❌ | ✅ |

---

## 4. Azure Application Gateway

### What It Does

| Capability | Description |
|------------|-------------|
| **Layer 7 load balancing** | HTTP/HTTPS |
| **SSL termination** | Offload encryption |
| **Web Application Firewall** | OWASP protection |
| **URL routing** | Path-based routing |
| **Session affinity** | Cookie-based |

### SKU Comparison

| Feature | Standard_v2 | WAF_v2 |
|---------|-------------|---------|
| Autoscaling | ✅ | ✅ |
| Zone redundancy | ✅ | ✅ |
| WAF | ❌ | ✅ |
| Price | $$ | $$$ |

### Customization

| Customization | Purpose |
|---------------|---------|
| Custom probes | Application-specific health |
| Rewrite rules | Modify headers |
| Custom WAF rules | Application-specific protection |
| Backend settings | Timeout, affinity |

---

## 5. VPN Gateway

### SKU Comparison

| SKU | Tunnels | Throughput | Use Case |
|-----|---------|------------|----------|
| Basic | 10 | 100 Mbps | Dev/test |
| VpnGw1 | 30 | 650 Mbps | Small prod |
| VpnGw2 | 30 | 1 Gbps | Medium prod |
| VpnGw3 | 30 | 1.25 Gbps | Large prod |
| VpnGw4 | 100 | 5 Gbps | High perf |
| VpnGw5 | 100 | 10 Gbps | Max perf |

### Connection Types

| Type | Description | Use Case |
|------|-------------|----------|
| Site-to-Site (S2S) | On-prem to Azure | Branch offices |
| Point-to-Site (P2S) | Client to Azure | Remote users |
| VNet-to-VNet | Azure to Azure | VNet connection |

---

# Compute Resources

## 1. Virtual Machines

### What It Does

| Capability | Description |
|------------|-------------|
| **IaaS compute** | Full OS control |
| **Flexibility** | Any workload |
| **Scaling** | Manual or VMSS |
| **Extensions** | Add capabilities |

### VM Series

| Series | Use Case | Features |
|--------|----------|----------|
| B | Burstable | Cost-effective, variable |
| D | General purpose | Balanced CPU/memory |
| E | Memory optimized | High memory ratio |
| F | Compute optimized | High CPU ratio |
| N | GPU | AI/ML, graphics |
| L | Storage optimized | High IOPS |
| M | Memory intensive | SAP HANA |

### Built-in Features

| Feature | Included | Notes |
|---------|----------|-------|
| Azure Hybrid Benefit | ✅ | Bring Windows license |
| Reserved Instances | ✅ | Up to 72% savings |
| Spot VMs | ✅ | Up to 90% savings |
| Accelerated Networking | ✅ | Free on supported |
| Azure Backup integration | ✅ | Agent included |

### Customization Options

| Customization | Purpose |
|---------------|---------|
| Custom images | Pre-configured VMs |
| Extensions | Add software/config |
| User data | Bootstrap scripts |
| cloud-init | Linux initialization |
| Custom Script Extension | Run scripts |

### Limitations

| Limitation | Details |
|------------|---------|
| VMs per subscription | 25,000 per region |
| VM sizes | Region-dependent |
| Disks per VM | Up to 64 |
| NICs per VM | Size-dependent |

---

## 2. Virtual Machine Scale Sets (VMSS)

### What It Does

| Capability | Description |
|------------|-------------|
| **Auto-scaling** | Scale based on metrics |
| **High availability** | Across fault domains |
| **Load balancing** | Built-in integration |
| **Uniform deployment** | Identical instances |

### Orchestration Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| Uniform | Identical VMs | Web servers |
| Flexible | Mixed VMs | Heterogeneous |

### Scaling Options

| Type | Trigger | Configuration |
|------|---------|---------------|
| Manual | User action | Set instance count |
| Automatic | Metrics | CPU, memory, custom |
| Scheduled | Time | Scale for events |
| Predictive | ML | Forecasted demand |

### Limitations

| Limitation | Details |
|------------|---------|
| Instances per VMSS | 1,000 (standard), 600 (custom image) |
| Scale sets per subscription | 2,500 per region |

---

## 3. Azure App Service

### What It Does

| Capability | Description |
|------------|-------------|
| **PaaS hosting** | Web apps, APIs |
| **Managed platform** | No infrastructure |
| **Deployment** | Git, containers, packages |
| **Scaling** | Auto-scale built-in |

### Service Plan Tiers

| Tier | Use Case | Features |
|------|----------|----------|
| Free/Shared | Dev/test | Limited, shared |
| Basic | Low traffic | Dedicated, manual scale |
| Standard | Production | Auto-scale, slots |
| Premium | High perf | More scale, VNet |
| Isolated | Compliance | Private environment |

### Built-in Features

| Feature | Tier Required |
|---------|---------------|
| Custom domains | Basic+ |
| SSL certificates | Basic+ |
| Deployment slots | Standard+ |
| Auto-scale | Standard+ |
| VNet integration | Premium+ |
| Private endpoints | Premium+ |

### Limitations

| Limitation | Details |
|------------|---------|
| Apps per plan | Unlimited (share resources) |
| Deployment slots | Up to 20 |
| Scale out | Up to 30 instances |
| Isolated | Up to 100 instances |

---

# Storage Resources

## 1. Storage Accounts

### Types

| Type | Performance | Use Case |
|------|-------------|----------|
| Standard GPv2 | HDD | General purpose |
| Premium Block Blob | SSD | High transaction |
| Premium File Shares | SSD | Enterprise files |
| Premium Page Blobs | SSD | VM disks |

### Services

| Service | Description | Protocol |
|---------|-------------|----------|
| Blob | Object storage | REST, SDKs |
| Files | SMB/NFS shares | SMB 3.0, NFS 4.1 |
| Queue | Message queue | REST |
| Table | NoSQL store | REST |

### Access Tiers (Blob)

| Tier | Access | Storage Cost | Access Cost |
|------|--------|--------------|-------------|
| Hot | Frequent | $$$ | $ |
| Cool | Infrequent (30 days) | $$ | $$ |
| Cold | Rare (90 days) | $ | $$$ |
| Archive | Archival (180 days) | ¢ | $$$$ (+ rehydrate time) |

### Replication Options

| Option | Durability | Regions | Cost |
|--------|------------|---------|------|
| LRS | 99.999999999% | 1 | $ |
| ZRS | 99.9999999999% | 1 (3 zones) | $$ |
| GRS | 99.99999999999999% | 2 | $$$ |
| GZRS | 99.99999999999999% | 2 (3 zones primary) | $$$$ |

### Security Features

| Feature | Built-in | Notes |
|---------|----------|-------|
| Encryption at rest | ✅ Yes | Always on (Microsoft-managed) |
| Encryption in transit | ✅ Yes | HTTPS enforced |
| SAS tokens | ✅ Yes | Time-limited access |
| Firewall | ✅ Yes | IP and VNet rules |
| Private endpoints | ✅ Yes | Private connectivity |

### Limitations

| Limitation | Details |
|------------|---------|
| Storage accounts per subscription | 250 per region |
| Max account size | 5 PB |
| Max blob size | 190.7 TB |
| Max file size | 4 TB |
| Max IOPS (standard) | 20,000 |

---

## 2. Azure Files

### What It Does

| Capability | Description |
|------------|-------------|
| **Cloud file shares** | SMB/NFS access |
| **Hybrid** | Azure File Sync |
| **Lift and shift** | Replace on-prem |
| **Shared storage** | Multi-VM access |

### Protocol Support

| Protocol | Version | OS Support |
|----------|---------|------------|
| SMB | 2.1, 3.0, 3.1.1 | Windows, Linux, macOS |
| NFS | 4.1 | Linux |

### Tiers

| Tier | Performance | Use Case |
|------|-------------|----------|
| Premium | SSD, provisioned | Low latency |
| Transaction optimized | HDD | Heavy transactions |
| Hot | HDD | General |
| Cool | HDD | Archive |

### Azure File Sync

| Feature | Description |
|---------|-------------|
| Cloud tiering | Hot files local, cold in cloud |
| Multi-site sync | Sync across locations |
| Rapid DR | Fast failover |
| Backup integration | Azure Backup support |

---

# Monitoring and Backup

## 1. Azure Monitor

### What It Does

| Capability | Description |
|------------|-------------|
| **Metrics** | Numeric time-series data |
| **Logs** | Text-based event data |
| **Alerts** | Proactive notifications |
| **Insights** | Pre-built dashboards |

### Built-in Features

| Feature | Included | Cost |
|---------|----------|------|
| Platform metrics | ✅ Yes | Free |
| Activity logs | ✅ Yes | Free (90 days) |
| Basic alerts | ✅ Yes | Per alert |
| Insights (VMs, etc.) | ✅ Yes | Log ingestion |

### Log Analytics

| Feature | Description |
|---------|-------------|
| KQL queries | Analyze logs |
| Workbooks | Visual reports |
| Retention | 30 days free, up to 2 years |
| Export | Storage, Event Hubs |

### Limitations

| Limitation | Details |
|------------|---------|
| Workspaces per subscription | 100 |
| Query timeout | 10 minutes |
| Data retention | 730 days max |
| Ingestion | Per-GB pricing |

---

## 2. Azure Backup

### What It Does

| Capability | Description |
|------------|-------------|
| **VM backup** | Full VM protection |
| **File backup** | Files and folders |
| **SQL backup** | Database backup |
| **Blob backup** | Storage backup |

### Supported Workloads

| Workload | Agent | Integration |
|----------|-------|-------------|
| Azure VMs | Built-in | Native |
| On-prem VMs | MARS/MABS | Agent-based |
| Azure Files | Native | Native |
| SQL in VM | Built-in | Native |
| SAP HANA | Built-in | Native |

### Vault Types

| Type | Use Case | Features |
|------|----------|----------|
| Recovery Services vault | Azure Backup | Backup, ASR |
| Backup vault | Newer workloads | Blob, disk, PostgreSQL |

### Retention

| Range | Options |
|-------|---------|
| Daily | Up to 9,999 points |
| Weekly | Up to 5,163 points |
| Monthly | Up to 1,188 points |
| Yearly | Up to 99 points |

---

## 📊 Quick Reference: Resource Limits

| Resource | Default Limit | Can Increase |
|----------|---------------|--------------|
| VMs per subscription | 25,000/region | ✅ Yes |
| VNets per subscription | 1,000 | ✅ Yes |
| Storage accounts | 250/region | ✅ Yes |
| NSGs per subscription | 5,000 | ✅ Yes |
| Public IPs | 1,000 | ✅ Yes |
| Load balancers | 1,000 | ✅ Yes |

---

*Last updated: November 2025*
