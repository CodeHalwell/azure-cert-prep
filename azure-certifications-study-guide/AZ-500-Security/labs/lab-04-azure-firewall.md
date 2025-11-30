# Lab 04: Protect Traffic with Azure Firewall

## 🎯 Lab Goal

Deploy and configure **Azure Firewall** for network protection:

- Deploy Azure Firewall in a hub VNet
- Configure application and network rules
- Implement forced tunneling through firewall

This supports the **Implement platform protection** domain of AZ‑500.

---

## ✅ Prerequisites

- Azure subscription
- Hub-spoke network topology

---

## Step 1 – Create Azure Firewall Subnet

Azure Firewall requires a dedicated subnet named `AzureFirewallSubnet`.

```bash
az network vnet subnet create \
  --name AzureFirewallSubnet \
  --vnet-name vnet-hub \
  --resource-group rg-hub \
  --address-prefixes 10.0.1.0/26
```

---

## Step 2 – Deploy Azure Firewall

```bash
# Create public IP for firewall
az network public-ip create \
  --name pip-firewall \
  --resource-group rg-hub \
  --location eastus \
  --sku Standard \
  --allocation-method Static

# Create firewall
az network firewall create \
  --name fw-hub \
  --resource-group rg-hub \
  --location eastus \
  --sku AZFW_VNet \
  --tier Standard

# Configure firewall IP
az network firewall ip-config create \
  --firewall-name fw-hub \
  --resource-group rg-hub \
  --name fw-config \
  --public-ip-address pip-firewall \
  --vnet-name vnet-hub

# Get private IP
FW_PRIVATE_IP=$(az network firewall show \
  --name fw-hub \
  --resource-group rg-hub \
  --query "ipConfigurations[0].privateIPAddress" -o tsv)
echo $FW_PRIVATE_IP
```

---

## Step 3 – Create Firewall Policy

```bash
az network firewall policy create \
  --name policy-fw-hub \
  --resource-group rg-hub \
  --location eastus \
  --sku Standard

# Associate policy with firewall
az network firewall update \
  --name fw-hub \
  --resource-group rg-hub \
  --firewall-policy policy-fw-hub
```

---

## Step 4 – Configure Application Rules

Application rules filter outbound HTTP/HTTPS traffic by FQDN.

```bash
# Create rule collection group
az network firewall policy rule-collection-group create \
  --name DefaultApplicationRuleCollectionGroup \
  --policy-name policy-fw-hub \
  --resource-group rg-hub \
  --priority 300

# Create application rule collection
az network firewall policy rule-collection-group collection add-filter-collection \
  --name allow-web \
  --policy-name policy-fw-hub \
  --resource-group rg-hub \
  --rule-collection-group-name DefaultApplicationRuleCollectionGroup \
  --action Allow \
  --priority 100 \
  --collection-type ApplicationRuleCollection \
  --rule-name allow-microsoft \
  --rule-type ApplicationRule \
  --source-addresses "10.1.0.0/16" \
  --protocols https=443 \
  --target-fqdns "*.microsoft.com" "*.azure.com"
```

---

## Step 5 – Configure Network Rules

Network rules filter traffic by IP, port, and protocol.

```bash
# Create network rule collection group
az network firewall policy rule-collection-group create \
  --name DefaultNetworkRuleCollectionGroup \
  --policy-name policy-fw-hub \
  --resource-group rg-hub \
  --priority 200

# Allow DNS
az network firewall policy rule-collection-group collection add-filter-collection \
  --name allow-dns \
  --policy-name policy-fw-hub \
  --resource-group rg-hub \
  --rule-collection-group-name DefaultNetworkRuleCollectionGroup \
  --action Allow \
  --priority 100 \
  --collection-type NetworkRuleCollection \
  --rule-name allow-dns \
  --rule-type NetworkRule \
  --source-addresses "10.0.0.0/8" \
  --destination-addresses "168.63.129.16" \
  --destination-ports 53 \
  --ip-protocols UDP TCP
```

---

## Step 6 – Configure Forced Tunneling via UDR

Route all traffic through the firewall.

```bash
# Create route table
az network route-table create \
  --name rt-spoke-to-firewall \
  --resource-group rg-spoke \
  --location eastus

# Add default route to firewall
az network route-table route create \
  --route-table-name rt-spoke-to-firewall \
  --resource-group rg-spoke \
  --name route-to-firewall \
  --address-prefix 0.0.0.0/0 \
  --next-hop-type VirtualAppliance \
  --next-hop-ip-address $FW_PRIVATE_IP

# Associate route table with spoke subnet
az network vnet subnet update \
  --vnet-name vnet-spoke \
  --name subnet-workload \
  --resource-group rg-spoke \
  --route-table rt-spoke-to-firewall
```

---

## Step 7 – Enable Logging

```bash
az monitor diagnostic-settings create \
  --name fw-diagnostics \
  --resource $(az network firewall show --name fw-hub --resource-group rg-hub --query id -o tsv) \
  --workspace <log-analytics-workspace-id> \
  --logs '[{"category":"AzureFirewallApplicationRule","enabled":true},{"category":"AzureFirewallNetworkRule","enabled":true}]'
```

### Kusto Query for Blocked Traffic:

```kusto
AzureDiagnostics
| where Category == "AzureFirewallNetworkRule" or Category == "AzureFirewallApplicationRule"
| where msg_s contains "Deny"
| project TimeGenerated, msg_s
| take 100
```

---

## Cleanup

```bash
az group delete --name rg-hub --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created Azure Firewall subnet
- [ ] Deployed Azure Firewall with public IP
- [ ] Created and associated Firewall Policy
- [ ] Configured application rules for FQDN filtering
- [ ] Configured network rules for IP-based filtering
- [ ] Implemented forced tunneling via route table
- [ ] Enabled diagnostic logging
