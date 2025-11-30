# Lab 01: Configure Conditional Access Policies

## 🎯 Lab Goal

Implement **Conditional Access policies** to protect access to Azure resources:

- Create policies requiring MFA
- Configure location-based conditions
- Implement device compliance requirements

This supports the **Manage identity and access** domain of AZ‑500.

---

## ✅ Prerequisites

- Microsoft Entra ID P1 or P2 license
- Global Administrator or Security Administrator role
- Test user accounts

---

## Step 1 – Understand Conditional Access Components

### Policy Structure:

```
IF (Assignments)
  - Users/Groups
  - Cloud apps/Actions
  - Conditions (location, device, risk)

THEN (Access Controls)
  - Grant (MFA, compliant device, etc.)
  - OR Block
  - Session controls (app enforced, sign-in frequency)
```

---

## Step 2 – Create MFA Policy for Administrators

1. Go to **Entra ID → Security → Conditional Access → + New policy**.
2. Configure:
   - **Name**: `Require MFA for Admins`
   - **Users**: Select roles → Global Administrator, Security Administrator
   - **Cloud apps**: All cloud apps
   - **Grant**: Require multi-factor authentication
3. Set **Enable policy** to **Report-only** first.
4. Click **Create**.

### Test with What If:

1. Go to **Conditional Access → What If**.
2. Select an admin user and cloud app.
3. Verify the policy would apply.

---

## Step 3 – Create Location-Based Policy

### Define Named Locations:

1. Go to **Entra ID → Security → Named locations → + New location**.
2. Create:
   - **Name**: `Corporate Network`
   - **Type**: IP ranges
   - **IP ranges**: Add your office IP ranges
   - Check **Mark as trusted location**

### Create Policy:

1. Create new policy: `Block Access Outside Corporate Network`
2. Configure:
   - **Users**: All users (exclude emergency access accounts)
   - **Cloud apps**: Azure Management
   - **Conditions → Locations**: Include All locations, Exclude Corporate Network
   - **Grant**: Block access

---

## Step 4 – Require Compliant Devices

### Policy Configuration:

1. Create policy: `Require Compliant Device for Sensitive Apps`
2. Configure:
   - **Users**: All users
   - **Cloud apps**: Select sensitive apps (e.g., Azure Portal)
   - **Conditions → Device platforms**: Windows, macOS
   - **Grant**: Require device to be marked as compliant

> Note: Requires Microsoft Intune for device compliance.

---

## Step 5 – Configure Session Controls

### Sign-in Frequency:

1. Edit or create policy.
2. Go to **Session controls**.
3. Enable **Sign-in frequency**: 1 hour for high-risk apps.

### Persistent Browser Session:

- Enable for trusted devices on trusted networks only.
- Disable for public/shared computers.

---

## Step 6 – Monitor and Troubleshoot

### Sign-in Logs:

1. Go to **Entra ID → Sign-in logs**.
2. Filter by **Conditional Access** to see policy results.
3. Check **Conditional Access** column for Applied, Not Applied, or Failed.

### Common Issues:

| Issue | Cause | Resolution |
|-------|-------|------------|
| Policy not applying | Exclusions | Check excluded groups |
| Users blocked unexpectedly | Location misconfig | Verify named locations |
| Infinite MFA prompts | Session controls | Adjust sign-in frequency |

---

## Cleanup

1. Set test policies to **Report-only** or delete them.
2. Remove test named locations if not needed.

---

## ✅ Lab Checklist

- [ ] Created MFA policy for administrators
- [ ] Configured named locations for corporate network
- [ ] Created location-based blocking policy
- [ ] Implemented device compliance requirements
- [ ] Configured session controls
- [ ] Tested policies with What If tool
