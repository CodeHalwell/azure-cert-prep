# Lab 05: Secure Access with Private Link

## 🎯 Lab Goal

Implement **Private Link and Private Endpoints** to secure PaaS access:

- Create private endpoints for Azure services
- Configure Private DNS zones
- Disable public access to protected resources

This supports the **Implement platform protection** domain of AZ‑500.

---

## ✅ Prerequisites

- Azure subscription
- Virtual network with subnets
- Azure Storage account or SQL Database

---

## Step 1 – Understand Private Link Components

```
┌─────────────────────┐
│  Virtual Network    │
│                     │
│  ┌───────────────┐ │
│  │Private Endpoint│ │─────┐
│  │ 10.0.1.5      │ │     │
│  └───────────────┘ │     │
│                     │     │
│  ┌───────────────┐ │     │    ┌──────────────┐
│  │ VM            │ │     └────┤Azure Storage  │
│  └───────────────┘ │          │(Public disabled)│
└─────────────────────┘          └──────────────┘
```

| Component | Purpose |
|-----------|--------|
| Private Endpoint | NIC with private IP for PaaS service |
| Private Link Service | Custom service exposure |
| Private DNS Zone | Resolves PaaS FQDN to private IP |

---

## Step 2 – Create Subnet for Private Endpoints

```bash
az network vnet subnet create \
  --name subnet-private-endpoints \
  --vnet-name vnet-main \
  --resource-group rg-network \
  --address-prefixes 10.0.5.0/24 \
  --disable-private-endpoint-network-policies true
```

---

## Step 3 – Create Private Endpoint for Storage

```bash
# Get storage account resource ID
STORAGE_ID=$(az storage account show \
  --name stcontosoprivate \
  --resource-group rg-storage \
  --query id -o tsv)

# Create private endpoint
az network private-endpoint create \
  --name pe-storage-blob \
  --resource-group rg-network \
  --vnet-name vnet-main \
  --subnet subnet-private-endpoints \
  --private-connection-resource-id $STORAGE_ID \
  --group-id blob \
  --connection-name storage-connection
```

---

## Step 4 – Configure Private DNS Zone

```bash
# Create private DNS zone for blob storage
az network private-dns zone create \
  --name privatelink.blob.core.windows.net \
  --resource-group rg-network

# Link DNS zone to VNet
az network private-dns link vnet create \
  --name link-vnet-main \
  --resource-group rg-network \
  --zone-name privatelink.blob.core.windows.net \
  --virtual-network vnet-main \
  --registration-enabled false

# Create DNS zone group (auto-registers DNS records)
az network private-endpoint dns-zone-group create \
  --name storage-dns-group \
  --resource-group rg-network \
  --endpoint-name pe-storage-blob \
  --private-dns-zone privatelink.blob.core.windows.net \
  --zone-name blob
```

### DNS Zone Names by Service:

| Service | Zone Name |
|---------|----------|
| Blob Storage | privatelink.blob.core.windows.net |
| SQL Database | privatelink.database.windows.net |
| Key Vault | privatelink.vaultcore.azure.net |
| Cosmos DB | privatelink.documents.azure.com |

---

## Step 5 – Disable Public Access

```bash
# Disable public access to storage account
az storage account update \
  --name stcontosoprivate \
  --resource-group rg-storage \
  --public-network-access Disabled
```

---

## Step 6 – Verify Private Connectivity

### From a VM in the VNet:

```bash
# Verify DNS resolution
nslookup stcontosoprivate.blob.core.windows.net
# Should return private IP (e.g., 10.0.5.4)

# Test connectivity
az storage blob list \
  --account-name stcontosoprivate \
  --container-name data \
  --auth-mode login
```

### Verify from Azure Portal:

1. Go to **Private endpoint → DNS configuration**.
2. Verify A record points to private IP.

---

## Step 7 – Create Private Endpoint for SQL Database

```bash
# Get SQL Server resource ID
SQL_ID=$(az sql server show \
  --name sql-contoso \
  --resource-group rg-data \
  --query id -o tsv)

# Create private endpoint
az network private-endpoint create \
  --name pe-sql \
  --resource-group rg-network \
  --vnet-name vnet-main \
  --subnet subnet-private-endpoints \
  --private-connection-resource-id $SQL_ID \
  --group-id sqlServer \
  --connection-name sql-connection

# Create DNS zone for SQL
az network private-dns zone create \
  --name privatelink.database.windows.net \
  --resource-group rg-network

az network private-dns link vnet create \
  --name link-vnet-main-sql \
  --resource-group rg-network \
  --zone-name privatelink.database.windows.net \
  --virtual-network vnet-main \
  --registration-enabled false
```

---

## Cleanup

```bash
az network private-endpoint delete --name pe-storage-blob --resource-group rg-network
az network private-dns zone delete --name privatelink.blob.core.windows.net --resource-group rg-network
```

---

## ✅ Lab Checklist

- [ ] Created subnet for private endpoints
- [ ] Deployed private endpoint for Azure Storage
- [ ] Configured Private DNS zone and VNet link
- [ ] Verified DNS resolution returns private IP
- [ ] Disabled public access on storage account
- [ ] Created private endpoint for SQL Database
- [ ] Tested connectivity from within VNet
