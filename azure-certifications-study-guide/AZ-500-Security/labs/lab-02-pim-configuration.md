# Lab 02: Configure Privileged Identity Management (PIM)

## 🎯 Lab Goal

Implement **Privileged Identity Management** for just-in-time access:

- Configure PIM for Entra ID roles
- Configure PIM for Azure resource roles
- Set up access reviews

This supports the **Manage identity and access** domain of AZ‑500.

---

## ✅ Prerequisites

- Microsoft Entra ID P2 license
- Global Administrator or Privileged Role Administrator

---

## Step 1 – Enable PIM

1. Go to **Entra ID → Identity Governance → Privileged Identity Management**.
2. First-time setup will prompt to verify identity with MFA.
3. Click **Consent to PIM** if prompted.

---

## Step 2 – Configure Entra ID Role Settings

### Edit Role Settings:

1. Go to **PIM → Microsoft Entra roles → Settings**.
2. Select **Global Administrator** role.
3. Click **Edit** and configure:

| Setting | Value |
|---------|-------|
| Activation maximum duration | 8 hours |
| Require MFA on activation | Yes |
| Require justification | Yes |
| Require ticket information | Optional |
| Require approval | Yes |
| Approvers | Select security team |

4. Under **Assignment**:
   - Eligible assignment: 90 days max
   - Active assignment: Require justification

---

## Step 3 – Assign Eligible Roles

1. Go to **PIM → Microsoft Entra roles → Roles**.
2. Select **Global Administrator**.
3. Click **+ Add assignments**.
4. Select user(s) and set:
   - **Assignment type**: Eligible
   - **Duration**: 90 days
5. Click **Assign**.

---

## Step 4 – Activate a Role (User Experience)

1. As the assigned user, go to **PIM → My roles**.
2. Find the eligible role and click **Activate**.
3. Complete:
   - MFA challenge
   - Justification: "Need to perform admin task X"
   - Duration: Select required time
4. Wait for approval (if configured).
5. Once approved, role is active for the specified duration.

---

## Step 5 – Configure PIM for Azure Resources

### Discover Resources:

1. Go to **PIM → Azure resources → Discover resources**.
2. Select a subscription or management group.
3. Click **Manage resource**.

### Configure Role Settings:

1. Select the resource → **Settings**.
2. Choose a role (e.g., Contributor).
3. Configure similar settings as Entra ID roles.

### Assign Azure Resource Roles:

```bash
# Via Azure CLI (alternative)
az role assignment create \
  --assignee <user-principal-name> \
  --role "Contributor" \
  --scope "/subscriptions/<subscription-id>" \
  --condition "@Resource[Microsoft.Authorization/roleAssignments:PrincipalType] equals 'User'" \
  --condition-version "2.0"
```

---

## Step 6 – Create Access Reviews

### Configure Review:

1. Go to **PIM → Microsoft Entra roles → Access reviews**.
2. Click **+ New access review**.
3. Configure:
   - **Name**: `Quarterly Admin Review`
   - **Roles**: Global Administrator, Security Administrator
   - **Reviewers**: Manager or self-review
   - **Duration**: 14 days
   - **Recurrence**: Quarterly
4. Under **Settings**:
   - Auto-apply results: Yes
   - If reviewer doesn't respond: Remove access

---

## Step 7 – Monitor PIM Activity

### Audit Logs:

1. Go to **PIM → Microsoft Entra roles → Audit**.
2. Review:
   - Role activations
   - Assignment changes
   - Setting modifications

### Alerts:

1. Go to **PIM → Microsoft Entra roles → Alerts**.
2. Configure alerts for:
   - Roles being activated too frequently
   - Permanent role assignments
   - Roles assigned outside of PIM

---

## ✅ Lab Checklist

- [ ] Enabled and configured PIM
- [ ] Configured role settings for Global Administrator
- [ ] Assigned eligible roles to users
- [ ] Tested role activation as a user
- [ ] Configured PIM for Azure resource roles
- [ ] Created quarterly access review
- [ ] Reviewed audit logs and alerts
