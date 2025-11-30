# Lab 05: Manage Blob Storage and Lifecycle Policies

## 🎯 Lab Goal

Work specifically with **Azure Blob Storage** to:

- Create and manage containers
- Configure lifecycle management policies
- Explore access control options

This lab deepens the **Implement and manage storage** skills for AZ‑104.

---

## ✅ Prerequisites

- Completion of Lab 04 or an existing storage account with blob service enabled
- Azure CLI optional for scripting

---

## Step 1 – Create or Reuse a Storage Account

If you completed Lab 04, reuse `staz104lab<unique>`.

Otherwise, create a new **General-purpose v2** storage account in a lab resource group.

---

## Step 2 – Organize Data with Containers

1. In your storage account → **Containers**:
	- Create `logs`, `images`, and `archive` containers (all **Private** access).
2. Upload sample files into each container (e.g., text logs, images).

Think about how containers map to **logical organization** and security boundaries.

---

## Step 3 – Configure Lifecycle Management

1. In the storage account, go to **Lifecycle management**.
2. Add a new rule, for example:
	- Rule name: `logs-tiering`
	- Scope: limit to `logs` container
	- Condition: **If blob is older than 30 days**, then:
	  - Move to Cool tier
	- Optionally: after 90 days, move to Archive or delete.
3. Save the rule.

Understand that lifecycle rules run on a schedule; for lab purposes, you are configuring, not waiting 30 days.

---

## Step 4 – Explore Access Control Options

### Container-Level Public Access (Conceptual)

1. For one container (e.g., `images`), review the **Public access level** setting.
2. Understand levels:
	- **Private** – No anonymous access
	- **Blob** – Public read access to blobs only
	- **Container** – Public list + blob read
3. In production, public access is typically restricted; for the exam, know the options and implications.

### Azure RBAC vs. ACLs

1. In **Access control (IAM)** for the storage account, review roles like:
	- Storage Blob Data Reader
	- Storage Blob Data Contributor
2. Understand difference between:
	- **Management plane** roles vs **data plane** roles
	- How RBAC and access keys/SAS work together

---

## Step 5 – Optional: Use Azure CLI for Blob Operations

Using `az storage blob` commands (auth with `--auth-mode login` or account key):

```bash
# List containers
az storage container list \
  --account-name staz104lab<unique> \
  --output table

# List blobs in a container
az storage blob list \
  --account-name staz104lab<unique> \
  --container-name logs \
  --output table
```

This reinforces automation and scripting skills.

---

## Cleanup

- Remove test lifecycle rules if you don’t need them.
- Optionally delete containers or the entire storage account if the lab is complete.

---

## ✅ Lab Checklist

- [ ] Created or reused a storage account with blob service
- [ ] Organized data into multiple containers
- [ ] Configured a lifecycle management rule for at least one container
- [ ] Reviewed and understood container public access levels
- [ ] Explored RBAC roles relevant to blob data access
- [ ] (Optional) Used Azure CLI to list containers and blobs
- [ ] Cleaned up any unneeded lab resources

