# 🔧 MS-102 Copilot & Agent Resources Reference

Admin-focused reference for Microsoft 365 Copilot, Copilot Studio and related services in MS-102.

---

## 📋 Table of Contents

1. Microsoft 365 Copilot
   - Licensing & prerequisites
   - Copilot experiences in M365 apps
2. Microsoft 365 Admin Center
   - Copilot settings
   - Data access & governance
3. Copilot Studio
   - Agents, topics, and data connections
4. Data & Security
   - Microsoft Graph
   - Sensitivity labels & DLP
   - Audit & eDiscovery
5. Monitoring & Adoption
   - Usage reports
   - Adoption tools

---

# 1. Microsoft 365 Copilot

## 1.1 Licensing & Prerequisites

### Built-in (Once Licensed)

- Copilot endpoints and experiences in Word, Excel, PowerPoint, Outlook, Teams
- Integration with underlying Microsoft Graph data (emails, files, chats)

### Prerequisites

- Microsoft 365 E3/E5/Business Premium or similar base SKU
- Copilot license per user
- Exchange Online, SharePoint Online, OneDrive configured

### Limitations / Design Points

- Copilot **does not bypass permissions**—it can only access what user can
- Requires proper content governance to avoid oversharing

---

## 1.2 Copilot Experiences

- Word: drafting, rewriting, summarizing documents
- Excel: analysis, formula suggestions (preview features vary)
- PowerPoint: slide generation from prompts/documents
- Outlook: email drafting and summarization
- Teams: meeting recap, action items, chat assistance

---

# 2. Microsoft 365 Admin Center

## 2.1 Copilot Settings

### Built-in

- Org-wide toggles for Copilot features
- Per-user or group-based enablement (via licensing and policies)

### Requires Customization

- Defining which groups/segments get Copilot first (pilot vs rollout)
- Plugin and third-party integration controls

---

## 2.2 Data Access & Governance

### What You Can Do

- Configure **sensitivity labels, DLP, retention** to govern content accessible to Copilot
- Use **SharePoint permissions and sharing policies** to control data exposure

### Built-in

- Copilot respects existing permissions
- Integration with Purview for compliance

### Requires Customization

- Label taxonomy design (Public, Confidential, Highly Confidential, etc.)
- DLP policies for sensitive information types

---

# 3. Copilot Studio

## 3.1 Agents

- No/low-code environment to build **custom copilots/agents**

### Built-in

- Generative answers over your data
- Pre-built connectors (SharePoint, Dataverse, etc.)
- Publishing to Teams and other channels

### Requires Customization

- Agent purpose and scope definition
- Topic design (triggers, suggested questions)
- Data connections and security trimming

---

## 3.2 Data Connections

- Use Power Platform connectors, Graph, and custom APIs

### Built-in

- Pre-defined connectors for Microsoft and third-party services

### Requires Customization

- Connection references, environment strategy (Dev/Test/Prod)
- Custom connectors for line-of-business systems

---

# 4. Data & Security

## 4.1 Microsoft Graph

- Underlying API layer for user, group, message, file, and calendar data

### Built-in

- Standard permission scopes (User.Read, Files.Read.All, etc.)

### Requires Customization

- App registration and Graph permissions for custom apps and plugins

---

## 4.2 Sensitivity Labels & DLP

- As in Purview/M365 compliance

### Built-in

- Label inheritance into Office apps and some Copilot experiences

### Requires Customization

- Label policies, auto-labeling rules, and DLP policies consistent with Copilot rollout

---

## 4.3 Audit & eDiscovery

- Copilot activities are audited where applicable

### Built-in

- Unified audit logs and advanced eDiscovery (for E5)

### Requires Customization

- Queries, cases, and retention settings aligned to legal/compliance needs

---

# 5. Monitoring & Adoption

## 5.1 Usage Reports

- Copilot usage reporting in M365 Admin Center

### Built-in

- High-level metrics: active users, feature usage

### Requires Customization

- Interpreting metrics for ROI and adoption decisions

---

## 5.2 Adoption Tools

- Adoption.microsoft.com and in-product training

### Requires Customization

- Internal training programs, champions networks, support model

---

*Last updated: November 2025*