# Lab 02: Configure Role-Based Access Control (RBAC)

## 🎯 Lab Goal

Practice **Azure role-based access control (RBAC)** to:

- Create a resource group for labs
- Assign built-in roles at different scopes
- Verify effective permissions using the portal and CLI

This lab reinforces the **“Manage Azure identities and governance”** domain of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or Microsoft Learn sandbox
- Permissions: ability to create resource groups and role assignments (Owner or User Access Administrator on the subscription or a management group)
- Azure CLI or Azure PowerShell (optional but recommended)

You should have completed **Lab 01 (Entra ID Users and Groups)** or be familiar with Entra ID basics.

---

## Step 1 – Create a Lab Resource Group

1. In the Azure portal, search for **Resource groups**.
2. Select **+ Create** and use values similar to:
	 - Subscription: your lab subscription
	 - Resource group name: `rg-az104-rbac-lab`
	 - Region: any region close to you
3. Review and create the resource group.

Optional – Azure CLI:

```bash
az group create \
	--name rg-az104-rbac-lab \
	--location westeurope
```

---

## Step 2 – Identify Test Identities

For this lab you need:

- Your own admin account
- At least **one test user** (for example `Lab User One` from Lab 01)

If you don’t have a separate test user, you can create one now in **Microsoft Entra ID → Users** (see Lab 01 for guidance).

---

## Step 3 – Assign RBAC Role at Resource Group Scope

1. Open **rg-az104-rbac-lab** in the portal.
2. In the left menu, select **Access control (IAM)**.
3. Click **+ Add → Add role assignment**.
4. Choose a role such as **Contributor** (for lab purposes only) and select **Next**.
5. Under **Members**, choose **+ Select members**, search for your **test user**, and select them.
6. Review and assign.

Verify:

- In **Access control (IAM) → Role assignments**, confirm the role is visible at the **resource group** scope for that user.

---

## Step 4 – Test Permissions (Portal)

1. In a separate browser or InPrivate window, sign in as the **test user**.
2. Navigate to **Resource groups** and locate `rg-az104-rbac-lab`.
3. Confirm that the test user can:
	 - See the resource group
	 - Create a simple resource (e.g., a tag or a very small resource like a storage account if allowed in your environment)

Note any actions that are **blocked**, such as:

- Access to subscription-level settings
- Creating resource groups at the subscription scope

This demonstrates the **scope** of the assignment.

---

## Step 5 – Compare Role at Different Scopes

If you have permissions at the subscription level and this is a safe lab environment:

1. At the **subscription** level, go to **Access control (IAM)**.
2. Assign the same test user a more limited role (for example **Reader**) at the **subscription** scope.
3. Use the **View my access** or **Check access** features to compare:
	 - Resource group scope: Contributor
	 - Subscription scope: Reader

Discuss/understand:

- **Deny by default** and **additive** nature of roles
- How higher-scope roles apply to all child resources

> If subscription-level changes are not allowed in your environment, just walk through the blades and understand the conceptually different scopes (management group → subscription → resource group → resource).

---

## Step 6 – Use CLI to Inspect Role Assignments (Optional)

Using Azure CLI:

```bash
az role assignment list \
	--assignee <test-user-upn-or-object-id> \
	--scope $(az group show -n rg-az104-rbac-lab --query id -o tsv) \
	--output table
```

Observe:

- Which role definitions are assigned
- At what scopes

Optionally, experiment with removing an assignment:

```bash
az role assignment delete \
	--assignee <test-user-upn-or-object-id> \
	--role Contributor \
	--scope $(az group show -n rg-az104-rbac-lab --query id -o tsv)
```

> Only do this in a lab environment and be sure you still have an account with sufficient privileges.

---

## Cleanup

To avoid clutter and potential charges:

- Remove RBAC assignments for the test user from `rg-az104-rbac-lab` (and subscription, if you added any)
- Delete the test resource group:

```bash
az group delete --name rg-az104-rbac-lab --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a dedicated lab resource group
- [ ] Identified or created a test user
- [ ] Assigned a built-in role (e.g., Contributor) at resource group scope
- [ ] Verified effective permissions from the test user’s perspective
- [ ] (Optional) Compared role assignments at subscription vs resource group scope
- [ ] (Optional) Inspected role assignments using Azure CLI
- [ ] Cleaned up role assignments and the lab resource group

