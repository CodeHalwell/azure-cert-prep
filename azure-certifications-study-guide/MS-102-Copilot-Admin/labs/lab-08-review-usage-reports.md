# Lab 08: Review Copilot Usage Reports and Insights

## 🎯 Lab Goal

Monitor and analyze **Copilot usage** across your organization:

- Access Copilot usage reports
- Analyze adoption metrics
- Identify optimization opportunities

This supports the **Manage and optimize Copilot** domain of MS‑102.

---

## ✅ Prerequisites

- Global Reader, Reports Reader, or Global Administrator role
- Copilot deployed with active users

---

## Step 1 – Access Copilot Dashboard

1. Go to **Microsoft 365 admin center**.
2. Navigate to **Reports → Usage**.
3. Find **Microsoft 365 Copilot** section.
4. Or navigate directly to **admin.microsoft.com/AdminPortal/Home#/reports/copilot**.

---

## Step 2 – Review Readiness Report

### Readiness Metrics:

| Metric | Description |
|--------|------------|
| Licensed users | Users with Copilot licenses |
| Active users | Users who have used Copilot |
| Activation rate | % of licensed users who are active |
| App adoption | Which apps are being used |

### Identify Gaps:

- Users with licenses but no activity
- Apps with low adoption
- Departments needing training

---

## Step 3 – Review Usage Report

### Key Metrics:

| Metric | What It Shows |
|--------|---------------|
| Active users | Unique users over time period |
| Total actions | Number of Copilot interactions |
| Time saved | Estimated productivity gains |
| Feature usage | Which features are popular |

### Filter Options:

- Time period: 7 days, 30 days, 90 days, 180 days
- Users: All, specific groups
- Apps: Word, Excel, PowerPoint, Outlook, Teams

---

## Step 4 – Analyze App-Specific Usage

### Copilot in Word:

- Draft documents
- Rewrite content
- Summarize documents

### Copilot in Excel:

- Analyze data
- Create formulas
- Generate charts

### Copilot in PowerPoint:

- Create presentations
- Design slides
- Add content

### Copilot in Outlook:

- Draft emails
- Summarize threads
- Schedule meetings

### Copilot in Teams:

- Meeting summaries
- Chat summaries
- Action items

---

## Step 5 – Review Agent Analytics

### In Copilot Studio:

1. Open your agent.
2. Go to **Analytics**.
3. Review:

| Metric | Description |
|--------|------------|
| Sessions | Total conversations |
| Engagement rate | % of conversations with multiple turns |
| Resolution rate | % resolved without escalation |
| CSAT score | Customer satisfaction |
| Escalation rate | % transferred to human |

### Topic Performance:

- Most triggered topics
- Topics with high abandonment
- Topics needing improvement

---

## Step 6 – Export and Analyze Data

### Export Reports:

1. In the usage dashboard, click **Export**.
2. Choose format: CSV or Excel.
3. Download and analyze in Power BI or Excel.

### Power BI Integration:

1. Connect to Microsoft 365 usage data.
2. Create custom dashboards.
3. Track trends over time.

---

## Step 7 – Set Up Alerts

### Create Usage Alerts:

1. In the admin center, go to **Health → Message center preferences**.
2. Configure notifications for:
   - Copilot updates
   - Usage thresholds
   - Security events

### Via Microsoft Graph:

```powershell
# Query Copilot usage via Graph API
GET https://graph.microsoft.com/v1.0/reports/getMicrosoft365CopilotUsageUserDetail(period='D30')
```

---

## Step 8 – Identify Optimization Opportunities

### Low Adoption Analysis:

| Symptom | Possible Cause | Action |
|---------|----------------|--------|
| Low active users | Lack of awareness | Training campaign |
| Low Word usage | Feature not useful | Gather feedback |
| High escalations | Poor agent answers | Improve knowledge |
| Low CSAT | Bad user experience | Review and fix issues |

### Improvement Actions:

1. **Training**: Schedule Copilot training sessions.
2. **Champions**: Identify and empower power users.
3. **Content**: Update agent knowledge sources.
4. **Communication**: Share success stories.

---

## Step 9 – Create Executive Report

### Monthly Report Template:

```markdown
# Copilot Usage Report - [Month]

## Executive Summary
- Active users: [X] / [Y] licensed ([Z]% adoption)
- Total interactions: [Number]
- Estimated time saved: [Hours]

## Highlights
- Most used feature: [Feature]
- Top department: [Department]
- Growth: [X]% from last month

## Recommendations
1. Increase training for [Department]
2. Promote [Feature] which is underutilized
3. Review agent topic [X] with high abandonment

## Next Steps
- Scheduled training: [Date]
- Feature rollout: [Feature]
```

---

## Step 10 – Plan Continuous Improvement

### Monthly Review Cadence:

1. **Week 1**: Collect and analyze data.
2. **Week 2**: Identify issues and opportunities.
3. **Week 3**: Implement improvements.
4. **Week 4**: Communicate updates and successes.

### Feedback Loop:

1. Collect user feedback via surveys.
2. Review agent conversation logs.
3. Update training materials.
4. Enhance agent knowledge and topics.

---

## ✅ Lab Checklist

- [ ] Accessed Copilot usage dashboard
- [ ] Reviewed readiness and activation metrics
- [ ] Analyzed usage reports by app and time period
- [ ] Reviewed agent-specific analytics
- [ ] Exported data for detailed analysis
- [ ] Set up usage alerts
- [ ] Identified optimization opportunities
- [ ] Created executive summary report
- [ ] Planned continuous improvement cycle
