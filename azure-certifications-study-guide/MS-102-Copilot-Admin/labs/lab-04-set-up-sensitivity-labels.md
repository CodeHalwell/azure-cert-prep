# Lab 04: Set Up Sensitivity Labels and Policies

## 🎯 Lab Goal

Configure **sensitivity labels** to protect data used by Copilot:

- Create sensitivity labels
- Configure label policies
- Understand how labels affect Copilot

This supports the **Protect data for Copilot** domain of MS‑102.

---

## ✅ Prerequisites

- Global Administrator or Compliance Administrator role
- Microsoft 365 E3/E5 or equivalent

---

## Step 1 – Access Microsoft Purview

1. Go to **Microsoft Purview compliance portal**.
2. Or navigate to **purview.microsoft.com**.
3. Go to **Information protection → Labels**.

---

## Step 2 – Create Sensitivity Labels

### Create Parent Label:

1. Click **+ Create a label**.
2. Configure:
   - **Name**: `Confidential`
   - **Display name**: `Confidential`
   - **Description for users**: "Sensitive business information"

### Create Sublabels:

1. Select parent label → **Create sublabel**.
2. Configure sublabels:

| Sublabel | Protection |
|----------|------------|
| Internal Only | No encryption, watermark |
| Recipients Only | Encrypt for specific people |
| All Employees | Encrypt for organization |

---

## Step 3 – Configure Label Settings

### Encryption:

1. Under **Encryption**, choose:
   - **No encryption**: Label only
   - **Apply encryption**: Protect content

2. Configure permissions:

```
Permissions:
- All employees: Co-Author
- External users: Viewer (optional)
```

### Content Marking:

1. Enable **Content marking**.
2. Configure:
   - **Watermark**: "CONFIDENTIAL"
   - **Header**: Company name
   - **Footer**: "Internal Use Only"

---

## Step 4 – Configure Auto-Labeling (Optional)

### For Emails:

1. Under **Auto-labeling for files and emails**.
2. Configure conditions:

```
If content contains:
- Credit card numbers
- Social Security numbers
- Custom keywords: "Project X", "Acquisition"
```

3. Set action: Apply this label automatically.

---

## Step 5 – Create Label Policy

1. Go to **Label policies → Publish labels**.
2. Select labels to publish.
3. Configure:
   - **Name**: `Confidential Policy`
   - **Users/Groups**: All users or specific groups

### Policy Settings:

| Setting | Value |
|---------|-------|
| Default label for documents | None (or Confidential) |
| Default label for emails | None |
| Justification required | Yes |
| Help link | Custom URL |

---

## Step 6 – Understand Copilot and Sensitivity Labels

### How Copilot Respects Labels:

1. **Encrypted content**: Copilot can't access if user lacks permission.
2. **Labeled documents**: Copilot shows label in responses.
3. **Output inheritance**: Content created by Copilot may inherit labels.

### Best Practices:

| Practice | Benefit |
|----------|--------|
| Label sensitive data | Copilot respects access controls |
| Use auto-labeling | Consistent protection |
| Train users | Proper label application |

---

## Step 7 – Configure Default Labels

### For SharePoint Sites:

1. Go to **SharePoint admin center**.
2. Select a site → **Policies**.
3. Apply sensitivity label to site.

### For Teams:

1. Go to **Teams admin center**.
2. Configure sensitivity labels for teams.

---

## Step 8 – Monitor Label Usage

### Reports:

1. Go to **Microsoft Purview → Data classification**.
2. View:
   - **Overview**: Label distribution
   - **Content explorer**: Labeled content
   - **Activity explorer**: Labeling activity

### Copilot Interactions:

1. Monitor if Copilot accesses labeled content.
2. Review audit logs for access patterns.

---

## Step 9 – User Training

Prepare training materials:

```markdown
## Understanding Sensitivity Labels

**What are sensitivity labels?**
Labels help protect sensitive information by applying 
protection settings like encryption and watermarks.

**Labels in our organization:**
- Public: No restrictions
- Internal: For internal use only
- Confidential: Sensitive business information
- Highly Confidential: Restricted access

**Using labels with Copilot:**
- Copilot respects your permissions
- If you can't open a document, Copilot can't either
- Content you create may inherit labels
```

---

## ✅ Lab Checklist

- [ ] Accessed Microsoft Purview compliance portal
- [ ] Created parent and child sensitivity labels
- [ ] Configured encryption and content marking
- [ ] Set up auto-labeling conditions
- [ ] Created and published label policy
- [ ] Understood Copilot's label behavior
- [ ] Configured default labels for sites
- [ ] Reviewed label usage reports
