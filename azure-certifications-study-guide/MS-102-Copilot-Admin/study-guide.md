# 📖 MS-102 Study Guide

## Microsoft 365 Copilot and Agent Administration Fundamentals

This study guide covers all skills measured in the MS-102 exam.

---

# Domain 1: Configure Copilot Licensing and Deployment (25-30%)

## 1.1 Copilot Licensing

### License Types

| License | Features |
|---------|----------|
| **Microsoft 365 Copilot** | Full Copilot in M365 apps |
| **Copilot Pro** | Personal subscription |
| **Copilot for Sales** | CRM integration |
| **Copilot for Service** | Customer service |

### Prerequisites

| Requirement | Description |
|-------------|-------------|
| Microsoft 365 E3/E5/Business Premium | Base license |
| Copilot license | Add-on required |
| Entra ID | Identity management |
| Exchange Online | Email integration |
| SharePoint Online | Data grounding |
| OneDrive | File storage |

---

## 1.2 Deployment Planning

### Rollout Phases

```
┌─────────────────────────────────────────────────────────────┐
│                    Copilot Deployment                        │
├─────────────────────────────────────────────────────────────┤
│  Phase 1: Pilot                                              │
│  ├── IT team and early adopters                              │
│  └── 5-10% of organization                                   │
│                                                              │
│  Phase 2: Expansion                                          │
│  ├── Additional departments                                  │
│  └── 25-50% of organization                                  │
│                                                              │
│  Phase 3: Full Deployment                                    │
│  └── Organization-wide                                       │
└─────────────────────────────────────────────────────────────┘
```

### Readiness Checklist

| Item | Description |
|------|-------------|
| License assignment | Assign Copilot licenses |
| Network readiness | Required endpoints |
| Data readiness | SharePoint, OneDrive content |
| User training | Adoption resources |

---

# Domain 2: Manage Copilot Settings and Governance (25-30%)

## 2.1 Admin Center Configuration

### Copilot Settings

| Setting | Description |
|---------|-------------|
| **Enable/Disable** | Organization-wide toggle |
| **User access** | Who can use Copilot |
| **Data access** | What content Copilot can access |
| **Plugin settings** | Third-party integrations |

### Location

```
Microsoft 365 Admin Center
└── Settings
    └── Org settings
        └── Microsoft 365 Copilot
```

---

## 2.2 Data Governance

### Sensitivity Labels

| Label | Behavior |
|-------|----------|
| **Public** | Copilot can reference |
| **Confidential** | Limited access |
| **Highly Confidential** | May be excluded |

### Data Loss Prevention (DLP)

| Feature | Purpose |
|---------|---------|
| Policies | Prevent data leakage |
| Rules | Define sensitive content |
| Actions | Block, alert, override |

---

## 2.3 Compliance

### Audit and Logging

| Feature | Description |
|---------|-------------|
| **Audit logs** | Track Copilot usage |
| **eDiscovery** | Search Copilot interactions |
| **Retention** | Manage Copilot data |

---

# Domain 3: Configure and Manage Agents (25-30%)

## 3.1 Copilot Studio Overview

### Agent Building

```
┌─────────────────────────────────────────────────────────────┐
│                    Copilot Studio                            │
├─────────────────────────────────────────────────────────────┤
│  1. Create Agent                                             │
│     ├── Name and description                                 │
│     └── Purpose definition                                   │
│                                                              │
│  2. Configure Topics                                         │
│     ├── Trigger phrases                                      │
│     └── Response actions                                     │
│                                                              │
│  3. Add Data Sources                                         │
│     ├── SharePoint sites                                     │
│     ├── Dataverse                                            │
│     └── Custom connectors                                    │
│                                                              │
│  4. Publish                                                  │
│     ├── Teams                                                │
│     └── Website                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 3.2 Agent Types

| Type | Description |
|------|-------------|
| **Declarative agents** | Custom Copilot experiences |
| **Conversational agents** | Traditional chatbots |
| **API-based agents** | Backend integrations |

---

## 3.3 Plugins and Connectors

### Plugin Types

| Plugin | Purpose |
|--------|---------|
| Message extension | Teams actions |
| Power Platform | Connectors |
| API plugins | Custom APIs |
| Graph connectors | M365 data |

---

# Domain 4: Monitor and Optimize Copilot (15-20%)

## 4.1 Usage Analytics

### Key Metrics

| Metric | Description |
|--------|-------------|
| Active users | Who's using Copilot |
| Feature usage | Which apps |
| Query volume | Usage frequency |
| Adoption rate | Percentage of licensed users |

### Reports Location

```
Microsoft 365 Admin Center
└── Reports
    └── Usage
        └── Microsoft 365 Copilot
```

---

## 4.2 Troubleshooting

### Common Issues

| Issue | Resolution |
|-------|------------|
| Copilot not appearing | Check license assignment |
| Poor responses | Check data grounding |
| Permission errors | Verify user permissions |
| Plugin issues | Check connector status |

---

## ✅ Study Checklist

### Licensing & Deployment
- [ ] Understand Copilot license requirements
- [ ] Plan deployment phases
- [ ] Verify prerequisites
- [ ] Assign licenses

### Settings & Governance
- [ ] Configure admin center settings
- [ ] Set up sensitivity labels
- [ ] Configure DLP policies
- [ ] Enable audit logging

### Agents
- [ ] Create basic agent in Copilot Studio
- [ ] Configure topics and triggers
- [ ] Add data sources
- [ ] Publish to Teams

### Monitoring
- [ ] Access usage reports
- [ ] Interpret adoption metrics
- [ ] Troubleshoot common issues

---

*Last updated: November 2025*
