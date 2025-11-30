# Lab 08: Design Network Architecture

## 🎯 Lab Goal

Design **network architecture** for enterprise workloads:

- Design hub-and-spoke topology
- Plan network security and segmentation
- Implement hybrid connectivity

This supports the **Design infrastructure solutions** domain of AZ‑305.

---

## ✅ Prerequisites

- Azure subscription
- Understanding of Azure networking services

---

## Scenario

Contoso requires:
- 3 environments (Dev, Test, Prod) with network isolation
- Hybrid connectivity to on-premises datacenter
- Centralized network security
- PaaS services secured with private endpoints

---

## Step 1 – Design Hub-and-Spoke Topology

### Architecture:

```
                    On-Premises
                         │
                    ExpressRoute / VPN
                         │
                  ┌──────┴──────┐
                  │     HUB      │
                  │  10.0.0.0/16 │
                  │  • Firewall   │
                  │  • VPN GW     │
                  │  • Bastion    │
                  └──────┬──────┘
           ┌──────────┴──────────┐
      ┌────┴────┐     ┌────┴────┐     ┌────┴────┐
      │   DEV    │     │   TEST   │     │   PROD   │
      │ 10.1.0/16│     │ 10.2.0/16│     │ 10.3.0/16│
      └─────────┘     └─────────┘     └─────────┘
```

### IP Address Planning:

| VNet | CIDR | Purpose |
|------|------|--------|
| Hub | 10.0.0.0/16 | Shared services |
| Dev Spoke | 10.1.0.0/16 | Development |
| Test Spoke | 10.2.0.0/16 | Testing |
| Prod Spoke | 10.3.0.0/16 | Production |

---

## Step 2 – Design Subnet Strategy

### Hub Subnets:

| Subnet | CIDR | Purpose |
|--------|------|--------|
| AzureFirewallSubnet | 10.0.1.0/26 | Azure Firewall |
| GatewaySubnet | 10.0.2.0/27 | VPN/ExpressRoute |
| AzureBastionSubnet | 10.0.3.0/26 | Bastion |
| SharedServices | 10.0.4.0/24 | DNS, AD |

### Spoke Subnets (each):

| Subnet | CIDR | Purpose |
|--------|------|--------|
| Web | x.x.1.0/24 | Web tier |
| App | x.x.2.0/24 | Application tier |
| Data | x.x.3.0/24 | Database tier |
| PrivateEndpoints | x.x.4.0/24 | Private endpoints |

---

## Step 3 – Design Network Security

### NSG Strategy:

| NSG | Applied To | Rules |
|-----|-----------|-------|
| nsg-web | Web subnets | Allow HTTP/HTTPS from Internet |
| nsg-app | App subnets | Allow from Web tier only |
| nsg-data | Data subnets | Allow from App tier only |

### Azure Firewall Rules:

| Rule Collection | Type | Purpose |
|-----------------|------|--------|
| allow-azure | Application | Azure services |
| allow-web | Application | Outbound web traffic |
| deny-all | Network | Default deny |

```bash
az network firewall create \
  --name fw-hub \
  --resource-group rg-hub \
  --location eastus

az network firewall application-rule create \
  --firewall-name fw-hub \
  --resource-group rg-hub \
  --collection-name allow-azure \
  --name azure-services \
  --source-addresses '*' \
  --protocols https=443 \
  --target-fqdns '*.azure.com' '*.microsoft.com'
```

---

## Step 4 – Design Hybrid Connectivity

### Options:

| Option | Bandwidth | Use Case |
|--------|-----------|----------|
| S2S VPN | Up to 1.25 Gbps | Dev/Test, backup |
| ExpressRoute | Up to 100 Gbps | Production, low latency |
| ExpressRoute + VPN | Combined | HA with failover |

### ExpressRoute Design:

```bash
az network express-route create \
  --name er-contoso \
  --resource-group rg-connectivity \
  --bandwidth 1000 \
  --peering-location "Washington DC" \
  --provider "Equinix"
```

---

## Step 5 – Design Document

```markdown
# Network Architecture – Contoso Ltd.

## 1. Topology
- Hub-and-spoke with Azure Virtual WAN (optional)
- Hub: 10.0.0.0/16
- Spokes: 10.1-3.0.0/16

## 2. Connectivity
- ExpressRoute (1 Gbps) for production
- S2S VPN as backup
- VNet peering hub-to-spoke

## 3. Security
- Azure Firewall in hub (forced tunneling)
- NSGs on all subnets
- Private endpoints for PaaS
- DDoS Protection Standard

## 4. DNS
- Azure Private DNS zones
- Custom DNS forwarders in hub
- Private DNS zone links to all VNets

## 5. Monitoring
- Network Watcher enabled
- NSG flow logs to Log Analytics
- Connection Monitor for hybrid
```

---

## ✅ Lab Checklist

- [ ] Designed hub-and-spoke topology
- [ ] Planned IP addressing and subnets
- [ ] Created network security strategy with NSGs and Firewall
- [ ] Designed hybrid connectivity with ExpressRoute/VPN
- [ ] Documented network architecture
