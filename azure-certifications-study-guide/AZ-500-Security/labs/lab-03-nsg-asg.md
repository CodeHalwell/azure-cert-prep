# Lab 03: Secure Networks with NSG and ASG

## 🎯 Lab Goal

Implement **Network Security Groups (NSGs)** and **Application Security Groups (ASGs)**:

- Create and apply NSG rules
- Use ASGs for simplified rule management
- Configure NSG flow logs

This supports the **Implement platform protection** domain of AZ‑500.

---

## ✅ Prerequisites

- Azure subscription
- Virtual network with subnets and VMs

---

## Step 1 – Create Application Security Groups

ASGs allow logical grouping of VMs for security rules.

```bash
# Create ASGs
az network asg create \
  --name asg-webservers \
  --resource-group rg-security \
  --location eastus

az network asg create \
  --name asg-appservers \
  --resource-group rg-security \
  --location eastus

az network asg create \
  --name asg-dbservers \
  --resource-group rg-security \
  --location eastus
```

---

## Step 2 – Associate NICs with ASGs

```bash
# Associate VM NIC with ASG
az network nic ip-config update \
  --resource-group rg-security \
  --nic-name vm-web-1-nic \
  --name ipconfig1 \
  --application-security-groups asg-webservers
```

---

## Step 3 – Create Network Security Group

```bash
az network nsg create \
  --name nsg-web-tier \
  --resource-group rg-security \
  --location eastus
```

### Add Security Rules:

```bash
# Allow HTTP/HTTPS from Internet to Web servers
az network nsg rule create \
  --nsg-name nsg-web-tier \
  --resource-group rg-security \
  --name Allow-Web-Inbound \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-address-prefixes Internet \
  --destination-asgs asg-webservers \
  --destination-port-ranges 80 443

# Allow Web to App communication
az network nsg rule create \
  --nsg-name nsg-app-tier \
  --resource-group rg-security \
  --name Allow-Web-To-App \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-asgs asg-webservers \
  --destination-asgs asg-appservers \
  --destination-port-ranges 8080

# Allow App to DB communication
az network nsg rule create \
  --nsg-name nsg-data-tier \
  --resource-group rg-security \
  --name Allow-App-To-DB \
  --priority 100 \
  --direction Inbound \
  --access Allow \
  --protocol Tcp \
  --source-asgs asg-appservers \
  --destination-asgs asg-dbservers \
  --destination-port-ranges 1433

# Deny all other inbound
az network nsg rule create \
  --nsg-name nsg-web-tier \
  --resource-group rg-security \
  --name Deny-All-Inbound \
  --priority 4096 \
  --direction Inbound \
  --access Deny \
  --protocol '*' \
  --source-address-prefixes '*' \
  --destination-address-prefixes '*' \
  --destination-port-ranges '*'
```

---

## Step 4 – Associate NSG with Subnet

```bash
az network vnet subnet update \
  --vnet-name vnet-main \
  --name subnet-web \
  --resource-group rg-security \
  --network-security-group nsg-web-tier
```

---

## Step 5 – Enable NSG Flow Logs

```bash
# Create storage account for flow logs
az storage account create \
  --name stflowlogs \
  --resource-group rg-security \
  --location eastus \
  --sku Standard_LRS

# Enable flow logs
az network watcher flow-log create \
  --name fl-nsg-web \
  --resource-group rg-security \
  --nsg nsg-web-tier \
  --storage-account stflowlogs \
  --enabled true \
  --retention 90 \
  --format JSON \
  --log-version 2
```

### Enable Traffic Analytics (Optional):

```bash
az network watcher flow-log update \
  --name fl-nsg-web \
  --resource-group rg-security \
  --workspace <log-analytics-workspace-id> \
  --traffic-analytics true \
  --interval 10
```

---

## Step 6 – Verify and Test

### Verify Effective Security Rules:

```bash
az network nic show-effective-nsg \
  --name vm-web-1-nic \
  --resource-group rg-security
```

### Test Connectivity:

1. Use **Network Watcher → IP flow verify** to test if traffic would be allowed.
2. Test actual connectivity from web to app tier.
3. Verify blocked traffic from unauthorized sources.

---

## Cleanup

```bash
az group delete --name rg-security --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created Application Security Groups for each tier
- [ ] Associated VM NICs with appropriate ASGs
- [ ] Created NSGs with tier-specific rules
- [ ] Used ASGs in NSG rules for simplified management
- [ ] Associated NSGs with subnets
- [ ] Enabled NSG flow logs for monitoring
- [ ] Verified effective security rules
