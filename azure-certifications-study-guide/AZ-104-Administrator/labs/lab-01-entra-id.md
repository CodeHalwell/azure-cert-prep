# Lab 01: Manage Entra ID Users and Groups

## 🎯 Lab Goal

Use the Azure portal and PowerShell/CLI to perform **core Microsoft Entra ID (Azure AD) identity tasks**:

- Create and manage users and groups
- Assign licenses and roles
- Configure self-service password reset (SSPR) basics

This lab directly supports the **“Manage Azure identities and governance”** domain of AZ‑104.

---

## ✅ Prerequisites

- Azure subscription or Microsoft Learn sandbox with Entra ID access
- Permissions: at least **User Administrator** (or Global Administrator in a test tenant)
- Web browser

Optional:

- Azure PowerShell (`Az` module) or Azure CLI installed locally

---

## Step 1 – Explore Entra ID in the Portal

1. Sign in to the Azure portal: https://portal.azure.com
2. Search for **“Microsoft Entra ID”** and open your tenant.
3. In the left menu, briefly explore:
	- **Users**
	- **Groups**
	- **Licenses** (or “Licenses | All products”)
	- **Roles and administrators**

Take note of:

- The tenant name and primary domain
- Approximate number of existing users and groups (if any)

---

## Step 2 – Create Test Users

You will create at least **two test users** for this lab.

1. In **Microsoft Entra ID → Users → All users**, select **+ New user**.
2. Choose **Create new user**.
3. Use values similar to:
	- User 1:
	  - Name: `Lab User One`
	  - User principal name: `labuser1@<yourtenant>.onmicrosoft.com`
	- User 2:
	  - Name: `Lab User Two`
	  - User principal name: `labuser2@<yourtenant>.onmicrosoft.com`
4. Set an initial password (or let Azure generate one) and note it for testing.

Optional – CLI example (if you have rights and want to practice):

```bash
az ad user create \
  --display-name "Lab User One" \
  --user-principal-name labuser1@<yourtenant>.onmicrosoft.com \
  --password "P@ssw0rd123!" \
  --force-change-password-next-sign-in true
```

> In real environments, follow your organization’s password policies.

---

## Step 3 – Create Security and Microsoft 365 Groups

You will create **at least one security group** and **one Microsoft 365 group**.

1. In **Microsoft Entra ID → Groups → All groups**, select **+ New group**.
2. Create a **Security** group:
	- Group type: `Security`
	- Group name: `az104-lab-security`
	- Membership type: `Assigned`
	- Add `Lab User One` as a member.
3. Create a **Microsoft 365** group:
	- Group type: `Microsoft 365`
	- Group name: `az104-lab-m365`
	- Membership type: `Assigned`
	- Add `Lab User Two` as a member.

Observe differences in the **Group type** and where each group is intended to be used.

---

## Step 4 – Assign Licenses via Group (Optional but Recommended)

If your tenant has licenses (e.g., Microsoft 365 E5, Office, or other SKUs), you can practice **group-based licensing**.

1. Go to **Microsoft Entra ID → Licenses → All products**.
2. Select a product (for example, `Microsoft 365 E5` if available).
3. Choose **+ Assign** → **Users and groups**.
4. Select the **`az104-lab-m365`** group.
5. Complete the wizard.

Verify:

- In **Groups → az104-lab-m365 → Licenses**, confirm the product is assigned.
- In **Users → Lab User Two → Licenses**, confirm the license now appears for the user via group assignment.

---

## Step 5 – Assign a Role to a User (RBAC in Entra ID)

1. In **Microsoft Entra ID → Roles and administrators**, locate the **User administrator** role.
2. Select it, then choose **+ Add assignments**.
3. Assign the role to `Lab User One`.
4. Review the **Description** and **Permissions** for the role to understand what it allows.

This demonstrates **directory roles** (Entra ID admin roles) and how they differ from **Azure RBAC roles** on resources.

---

## Step 6 – Configure Basic Self-Service Password Reset (SSPR)

> Note: SSPR configuration may require specific licenses and permissions. If full configuration isn’t available in your tenant, just walk through the blades and settings conceptually.

1. From the Entra ID blade, go to **Password reset**.
2. Under **Properties**, set **Self service password reset enabled** to:
	- `Selected` or `All` (use a small pilot group in a real tenant).
3. Under **Authentication methods**, review which methods are allowed (e.g., mobile app, email, phone).
4. Under **Registration**, review configuration such as requiring users to register when signing in.

Understand:

- Where SSPR is enabled
- Which users are in scope
- Which authentication methods are allowed

---

## Cleanup (Optional but Recommended)

If you are using a shared or corporate tenant, clean up after the lab:

- Delete test users (`Lab User One`, `Lab User Two`)
- Delete lab groups (`az104-lab-security`, `az104-lab-m365`)
- Remove any temporary role assignments

---

## ✅ Lab Checklist

- [ ] Located Microsoft Entra ID in the Azure portal and reviewed key blades
- [ ] Created at least two test users
- [ ] Created a security group and a Microsoft 365 group
- [ ] (Optional) Configured group-based licensing for a group
- [ ] Assigned a directory role (e.g., User administrator) to a user
- [ ] Reviewed SSPR configuration options and understood scope & methods
- [ ] (Optional) Cleaned up test users, groups, and role assignments

