# Lab 01: Verify Copilot and Tenant Prerequisites

## 🎯 Lab Goal

Verify **prerequisites for Microsoft 365 Copilot** deployment:

- Check tenant configuration
- Verify Microsoft 365 licensing
- Ensure technical requirements are met

This supports the **Plan for Copilot** domain of MS‑102.

---

## ✅ Prerequisites

- Global Administrator or License Administrator role
- Microsoft 365 tenant

---

## Step 1 – Verify Microsoft 365 Licensing

### Required Base Licenses:

Copilot for Microsoft 365 requires one of:

| License | Included Apps |
|---------|---------------|
| Microsoft 365 E3/E5 | Office apps, Exchange, SharePoint, Teams |
| Office 365 E3/E5 | Office apps, Exchange, SharePoint, Teams |
| Microsoft 365 Business Standard/Premium | Office apps, Exchange, SharePoint, Teams |

### Check Current Licenses:

1. Go to **Microsoft 365 admin center** → **Billing → Licenses**.
2. Verify you have eligible base licenses.
3. Note available Copilot licenses.

---

## Step 2 – Verify Entra ID Configuration

### Check Tenant Settings:

1. Go to **Entra admin center** → **Users → User settings**.
2. Verify:
   - Users can register applications: As appropriate
   - Users can consent to apps: As appropriate

### Verify Authentication:

1. Check that users have modern authentication enabled.
2. Verify MFA is configured (recommended for security).

---

## Step 3 – Check Network Requirements

### Required Endpoints:

Copilot requires access to:

| Endpoint | Purpose |
|----------|--------|
| *.microsoft.com | Microsoft services |
| *.office.com | Office applications |
| *.office365.com | Microsoft 365 services |
| *.microsoftonline.com | Authentication |

### Verify Connectivity:

1. Use the **Microsoft 365 network connectivity test**:
   - Go to [connectivity.office.com](https://connectivity.office.com)
   - Run the test from your network
2. Ensure all required endpoints are accessible.

---

## Step 4 – Verify Application Versions

### Minimum App Versions:

| Application | Minimum Version |
|-------------|----------------|
| Microsoft 365 Apps | Current Channel or Monthly Enterprise Channel |
| Outlook (Windows) | Version 2309 or later |
| Teams | Latest version |
| Edge | Latest version |

### Check Update Channel:

1. Open any Office app → **File → Account**.
2. Verify **Update Channel** is Current or Monthly Enterprise.
3. Update if necessary.

---

## Step 5 – Verify OneDrive and SharePoint

### OneDrive Sync:

1. Verify OneDrive sync is enabled for users.
2. Check sync client version is current.

### SharePoint Configuration:

1. Go to **SharePoint admin center**.
2. Verify:
   - External sharing settings (as appropriate)
   - Site creation permissions

---

## Step 6 – Check Microsoft Graph Permissions

Copilot uses Microsoft Graph to access:

- Emails and calendar
- Files in OneDrive and SharePoint
- Teams messages and meetings
- User profile information

### Verify API Access:

1. Go to **Entra admin center → App registrations**.
2. Check for Copilot-related apps.
3. Review granted permissions.

---

## Step 7 – Readiness Checklist

| Requirement | Status |
|-------------|--------|
| Eligible Microsoft 365 license | ☐ |
| Copilot for Microsoft 365 license | ☐ |
| Modern authentication enabled | ☐ |
| MFA configured | ☐ |
| Network endpoints accessible | ☐ |
| Office apps updated | ☐ |
| OneDrive sync configured | ☐ |
| SharePoint configured | ☐ |

---

## Step 8 – Use Microsoft 365 Copilot Readiness Tool

1. Go to **Microsoft 365 admin center**.
2. Navigate to **Settings → Microsoft 365 Copilot**.
3. Run the readiness assessment.
4. Review and address any issues.

---

## ✅ Lab Checklist

- [ ] Verified Microsoft 365 base licensing
- [ ] Checked Entra ID configuration
- [ ] Validated network connectivity
- [ ] Confirmed application versions
- [ ] Reviewed OneDrive and SharePoint settings
- [ ] Checked Microsoft Graph permissions
- [ ] Completed readiness checklist
