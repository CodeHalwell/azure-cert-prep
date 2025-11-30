# Lab 04: Configure Storage Accounts

## 🎯 Lab Goal

Practice key **Azure Storage account** tasks:

- Create a storage account with proper redundancy and access settings
- Configure containers and access tiers
- Secure access with SAS and firewalls/basic network rules

This supports the **Implement and manage storage** domain of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or sandbox
- Ability to create resource groups and storage accounts
- Azure CLI optional for scripting

---

## Step 1 – Create a Storage Resource Group

1. In the portal, create a resource group `rg-az104-storage-lab` in your preferred region.

Optional CLI:

```bash
az group create --name rg-az104-storage-lab --location westeurope
```

---

## Step 2 – Create a General-Purpose v2 Storage Account

1. In the portal, search for **Storage accounts** → **+ Create**.
2. Use values like:
	- Subscription: your lab subscription
	- Resource group: `rg-az104-storage-lab`
	- Storage account name: `staz104lab<unique>`
	- Region: same as RG
	- Performance: Standard
	- Redundancy: `Locally-redundant storage (LRS)` (or as required by your scenario)
3. Leave other settings at defaults for now and **Create**.

Note the differences between **LRS, ZRS, GRS, RA-GRS** in the **Redundancy** tooltip.

---

## Step 3 – Create Containers and Upload Blobs

1. Open your storage account → **Containers** → **+ Container**.
2. Create a container named `data` with **Private** access level.
3. Upload a few sample files (txt/json/jpg) into the container.
4. Verify you can see the files in the portal.

Optional CLI sample for upload (requires `az storage` with connection string or account key):

```bash
az storage blob upload \
  --account-name staz104lab<unique> \
  --container-name data \
  --name sample.txt \
  --file ./sample.txt \
  --auth-mode login
```

---

## Step 4 – Configure Access Tiers

1. In the container, select one of your blobs.
2. Change the **Access tier** (e.g., from Hot to Cool or Archive, depending on your region and SKU).
3. Observe how pricing guidance changes by tier in documentation.

Understand:

- When to use Hot vs Cool vs Archive
- Impact on storage and access costs

---

## Step 5 – Protect Access with SAS and (Optional) Network Rules

### Shared Access Signature (SAS)

1. From the storage account, go to **Shared access signature**.
2. Generate a SAS token that:
	- Applies to **Blob** service
	- Allows **Read** access only
	- Is valid for a short time window (e.g., 1 hour)
3. Construct a **blob SAS URL** for one of your files and test access in a browser or tool.

### Network Rules (Optional)

If allowed in your environment:

1. Go to **Networking** on the storage account.
2. Restrict access to **Selected networks** or enable **public network access** off.
3. Understand how this interacts with SAS tokens and private endpoints (conceptual for AZ‑104).

---

## Cleanup

- Delete the storage account if no longer needed.
- Delete the resource group:

```bash
az group delete --name rg-az104-storage-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a dedicated storage lab resource group
- [ ] Deployed a general‑purpose v2 storage account with chosen redundancy
- [ ] Created a private container and uploaded blobs
- [ ] Modified blob access tiers and understood when to use each
- [ ] Generated a SAS token and successfully accessed a blob via SAS URL
- [ ] (Optional) Explored basic network/firewall settings for the storage account
- [ ] Cleaned up lab resources

