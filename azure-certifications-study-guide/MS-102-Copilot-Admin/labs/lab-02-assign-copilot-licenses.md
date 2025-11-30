# Lab 02: Assign Copilot Licenses to Users

## 🎯 Lab Goal

Assign **Microsoft 365 Copilot licenses** to users:

- Assign licenses individually and in bulk
- Use group-based licensing
- Verify license assignment

This supports the **Deploy Copilot** domain of MS‑102.

---

## ✅ Prerequisites

- License Administrator or Global Administrator role
- Purchased Copilot for Microsoft 365 licenses

---

## Step 1 – View Available Copilot Licenses

1. Go to **Microsoft 365 admin center**.
2. Navigate to **Billing → Licenses**.
3. Find **Copilot for Microsoft 365**.
4. Note:
   - Total licenses purchased
   - Licenses assigned
   - Licenses available

---

## Step 2 – Assign License to Individual User

1. Go to **Users → Active users**.
2. Select a user.
3. Click **Licenses and apps**.
4. Check **Copilot for Microsoft 365**.
5. Click **Save changes**.

---

## Step 3 – Assign Licenses in Bulk

### Via Admin Center:

1. Go to **Users → Active users**.
2. Select multiple users (checkboxes).
3. Click **Manage product licenses**.
4. Choose **Assign more**.
5. Check **Copilot for Microsoft 365**.
6. Click **Save changes**.

### Via PowerShell:

```powershell
# Connect to Microsoft Graph
Connect-MgGraph -Scopes "User.ReadWrite.All", "Organization.Read.All"

# Get Copilot SKU ID
$skus = Get-MgSubscribedSku
$copilotSku = $skus | Where-Object { $_.SkuPartNumber -like "*Copilot*" }
$copilotSkuId = $copilotSku.SkuId

# Get users from a CSV
$users = Import-Csv "users.csv"

foreach ($user in $users) {
    $license = @{
        addLicenses = @(
            @{
                skuId = $copilotSkuId
            }
        )
        removeLicenses = @()
    }
    
    Set-MgUserLicense -UserId $user.UserPrincipalName -BodyParameter $license
    Write-Host "Assigned Copilot license to $($user.UserPrincipalName)"
}
```

---

## Step 4 – Use Group-Based Licensing

### Create a Licensing Group:

1. Go to **Entra admin center → Groups**.
2. Create a new security group:
   - **Name**: `Copilot-Licensed-Users`
   - **Type**: Security
3. Add members who should receive Copilot.

### Assign License to Group:

1. Go to **Microsoft 365 admin center → Billing → Licenses**.
2. Select **Copilot for Microsoft 365**.
3. Click **+ Assign licenses**.
4. Search for and select the group.
5. Click **Assign**.

> New members added to the group automatically receive the license.

---

## Step 5 – Verify License Assignment

### For Individual User:

1. Go to **Users → Active users**.
2. Select the user.
3. Click **Licenses and apps**.
4. Verify **Copilot for Microsoft 365** is checked.

### Via PowerShell:

```powershell
# Check user license
Get-MgUserLicenseDetail -UserId "user@contoso.com" | 
    Where-Object { $_.SkuPartNumber -like "*Copilot*" }
```

### List All Copilot Users:

```powershell
# Get all users with Copilot license
$copilotUsers = Get-MgUser -All | ForEach-Object {
    $licenses = Get-MgUserLicenseDetail -UserId $_.Id
    if ($licenses.SkuPartNumber -like "*Copilot*") {
        [PSCustomObject]@{
            DisplayName = $_.DisplayName
            UserPrincipalName = $_.UserPrincipalName
        }
    }
}

$copilotUsers | Export-Csv "copilot-users.csv" -NoTypeInformation
```

---

## Step 6 – Handle License Conflicts

### Common Issues:

| Issue | Cause | Resolution |
|-------|-------|------------|
| No base license | Missing M365 E3/E5 | Assign base license first |
| Conflicting service plans | Service plan overlap | Disable conflicting plan |
| License limit reached | All licenses assigned | Purchase more or reclaim |

### Reclaim Unused Licenses:

1. Review license usage reports.
2. Identify inactive users.
3. Remove Copilot license from inactive users.

---

## Step 7 – Pilot Deployment Strategy

### Recommended Approach:

1. **Phase 1**: IT and early adopters (5-10%)
2. **Phase 2**: Power users and champions (20%)
3. **Phase 3**: Department rollout (50%)
4. **Phase 4**: Full deployment (100%)

### Track Progress:

1. Create groups for each phase.
2. Use group-based licensing.
3. Monitor adoption metrics.

---

## ✅ Lab Checklist

- [ ] Viewed available Copilot licenses
- [ ] Assigned license to individual user
- [ ] Assigned licenses in bulk
- [ ] Created group for Copilot users
- [ ] Configured group-based licensing
- [ ] Verified license assignment
- [ ] Understood pilot deployment strategy
