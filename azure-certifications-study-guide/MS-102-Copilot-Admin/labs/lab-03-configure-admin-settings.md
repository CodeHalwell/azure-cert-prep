# Lab 03: Configure Copilot Admin Settings

## 🎯 Lab Goal

Configure **Copilot admin settings** in Microsoft 365:

- Enable or disable Copilot features
- Configure data access controls
- Set up web content settings

This supports the **Manage Copilot** domain of MS‑102.

---

## ✅ Prerequisites

- Global Administrator role
- Copilot licenses assigned

---

## Step 1 – Access Copilot Settings

1. Go to **Microsoft 365 admin center**.
2. Navigate to **Settings → Microsoft 365 Copilot**.
3. Or go directly to **admin.microsoft.com/AdminPortal/Home#/copilot**.

---

## Step 2 – Configure Web Content Access

### Web Search Integration:

Copilot can use web content to enhance responses.

1. In Copilot settings, find **Web content**.
2. Choose:
   - **On**: Copilot can access web content
   - **Off**: Copilot uses only organizational data

### Considerations:

| Setting | Use Case |
|---------|----------|
| On | General knowledge, current events |
| Off | Strict data governance, regulated industries |

---

## Step 3 – Configure Plugin Settings

### Enable/Disable Plugins:

1. Go to **Settings → Integrated apps**.
2. Find Copilot plugins.
3. Configure:
   - **Available for users**: Which plugins users can access
   - **Admin-managed**: Plugins deployed by admin

### Plugin Categories:

| Category | Examples |
|----------|----------|
| Microsoft | Loop, Forms, SharePoint |
| Third-party | Salesforce, ServiceNow, Jira |
| Custom | Line-of-business plugins |

---

## Step 4 – Configure Data Access

### Microsoft Graph Permissions:

Copilot respects existing permissions:

- Users only see content they have access to
- SharePoint permissions apply
- Email permissions apply

### Review Oversharing:

1. Use SharePoint Admin Center to audit sharing.
2. Review who has access to sensitive sites.
3. Implement information barriers if needed.

---

## Step 5 – Configure Copilot in Specific Apps

### Teams:

1. Go to **Teams admin center**.
2. Navigate to **Messaging policies**.
3. Enable/disable Copilot features in Teams.

### Outlook:

1. Go to **Exchange admin center**.
2. Configure mailbox policies.
3. Ensure Copilot is enabled.

### Word, Excel, PowerPoint:

1. Use Microsoft 365 Apps admin center.
2. Configure Office cloud policy.
3. Enable Copilot features.

---

## Step 6 – Set Up Conditional Access for Copilot

### Create Policy:

1. Go to **Entra admin center → Conditional Access**.
2. Create new policy: `Copilot Access Controls`
3. Configure:
   - **Users**: Copilot-licensed users
   - **Cloud apps**: Microsoft 365 Copilot
   - **Conditions**: Compliant devices only (optional)
   - **Grant**: Require MFA, require compliant device

---

## Step 7 – Configure Usage Analytics

### Enable Usage Analytics:

1. Go to **Microsoft 365 admin center → Reports**.
2. Navigate to **Usage**.
3. Enable Copilot usage tracking.

### Data Retention:

- Configure how long usage data is retained
- Set up data export if needed

---

## Step 8 – Privacy and Security Settings

### Data Processing:

1. Review Microsoft's data processing terms.
2. Configure data residency settings if applicable.
3. Review audit logging.

### Audit Copilot Activity:

1. Go to **Microsoft Purview compliance portal**.
2. Navigate to **Audit**.
3. Search for Copilot-related activities:
   - `CopilotInteraction`
   - `CopilotSearch`

---

## Step 9 – Create Admin Communication

Prepare communications for users:

```markdown
## Microsoft 365 Copilot is now available!

We're excited to announce that Microsoft 365 Copilot is now 
available to select users.

**What is Copilot?**
Copilot is an AI assistant integrated into Microsoft 365 apps 
that helps you work more efficiently.

**Getting Started:**
1. Look for the Copilot icon in your Microsoft 365 apps
2. Try asking Copilot to help with tasks
3. Review our training resources

**Questions?**
Contact the IT Help Desk.
```

---

## ✅ Lab Checklist

- [ ] Accessed Copilot admin settings
- [ ] Configured web content access
- [ ] Managed plugin settings
- [ ] Reviewed data access and permissions
- [ ] Configured Copilot in specific apps
- [ ] Created Conditional Access policy
- [ ] Enabled usage analytics
- [ ] Reviewed privacy and audit settings
