# Lab 01: Assessing AI Readiness and Opportunities

## 🎯 Lab Goal

Perform a **structured AI readiness and opportunity assessment** for a fictional organization, capturing:

- Business goals and pain points
- AI opportunities mapped to value
- Risks, constraints, and readiness gaps

This lab is intentionally **tool-agnostic and business-focused**, mirroring the **“Plan AI solutions”** domain of AB‑100.

---

## ✅ Prerequisites

- Basic understanding of AI capabilities (from AI‑900 or equivalent)
- Familiarity with common business processes (sales, support, operations)
- Note-taking tool: Word, OneNote, Markdown, or similar

No coding or Azure configuration is required for this lab.

---

## Scenario – Contoso Retail Group

You are an **Agentic AI Business Solutions Architect** engaged by **Contoso Retail Group**, a mid‑size retailer with:

- 50 physical stores across 3 countries
- An e‑commerce website and mobile app
- A central customer support center (phone + chat)

Contoso leadership wants to "use AI and agents" to:

- Improve customer experience
- Reduce support costs
- Increase sales conversion

Your first task is to **assess readiness and identify AI opportunities** – not to jump into solutions.

---

## Step 1 – Capture Business Objectives and Pain Points

Create a simple table with three columns: **Objective**, **Current Pain Point**, **Success Metric**.

Examples to get you started (expand/customize as needed):

| Objective | Current Pain Point | Success Metric |
|----------|--------------------|----------------|
| Improve customer support experience | Long wait times on phone and chat | Average handle time, CSAT, NPS |
| Increase online sales conversion | High cart abandonment on website | Conversion rate, average order value |
| Reduce manual back‑office work | Staff manually review refund and return requests | Hours saved, error rate |

Add **at least 3–5 rows** that reflect what you think Contoso cares about.

---

## Step 2 – Identify AI / Agentic Opportunities

For each objective/pain point, brainstorm **AI opportunities**. Use another table:

| Objective | Potential AI Use Case | Type of Solution | Value Hypothesis |
|----------|-----------------------|------------------|------------------|
| Improve customer support experience | Copilot/agent to answer common questions and handle simple requests | Customer-facing agent | Reduce wait times, free agents for complex issues |

Aim for **5–10 potential AI use cases**, such as:

- FAQ and order status agent for customers
- Agent to assist support reps with suggested replies and knowledge lookup
- Personalized product recommendations on the website
- Document intelligence for extracting data from invoices or receipts
- Agent to help store managers with sales insights and staffing suggestions

Focus on **business value**, not specific technologies yet.

---

## Step 3 – Assess Readiness (Data, Tech, People, Governance)

Use a simple readiness model with four dimensions:

- **Data** – Is necessary data available, clean, and accessible?
- **Technology** – Are required platforms (Azure, M365, Copilot Studio, CRM, etc.) in place?
- **People & Skills** – Are there people who can own and operate the solution?
- **Governance & Risk** – Are there policies around privacy, security, and responsible AI?

Create a table like:

| Dimension | Current State (1-5) | Notes |
|-----------|---------------------|-------|
| Data | 2 | Customer data spread across CRM, e‑commerce DB, and spreadsheets |
| Technology | 3 | Uses Microsoft 365 and some Azure services, no AI agents yet |
| People & Skills | 2 | Limited AI experience, strong business analysts |
| Governance & Risk | 1 | No formal AI governance yet |

Score each dimension from **1 (low)** to **5 (high)** and add notes.

---

## Step 4 – Prioritize Use Cases (Value vs. Feasibility)

Pick **3–5 of your best AI opportunities** from Step 2 and score them on two axes:

- **Business value** (1–5)
- **Feasibility / readiness** (1–5) based on Step 3

Example:

| Use Case | Business Value (1-5) | Feasibility (1-5) | Comments |
|----------|----------------------|--------------------|----------|
| Customer FAQ & order status agent | 5 | 4 | High impact, uses existing FAQ and order data |
| Back‑office returns automation | 4 | 2 | Needs more structured data and process redesign |

From this, identify **1–2 “quick win” use cases** where both value and feasibility are high.

---

## Step 5 – Draft a One-Page AI Opportunity Summary

Create a one‑page summary (or equivalent) for Contoso leadership that includes:

1. **Top 3 business objectives** you identified
2. **1–2 recommended “quick win” AI/agent use cases**, with:
	- Problem statement
	- Proposed AI/agent solution
	- Expected benefits / KPIs
3. **Key readiness gaps** (e.g., data quality, governance) they must address

Keep this **non‑technical** and business‑oriented – assume your audience is executives.

This deliverable mirrors what AB‑100 expects you to recognize in scenario questions.

---

## Stretch Goal (Optional) – Map to Azure and Copilot Studio

Take your top **1–2 use cases** and, at a high level, map them to:

- **Azure services** (e.g., Azure AI Search, Azure OpenAI, Azure AI Document Intelligence)
- **Copilot Studio** agents or plugins
- **Data sources** they would need (CRM, ERP, website logs, etc.)

You do **not** need to implement anything here; just sketch the mapping as bullets or a simple diagram.

---

## ✅ Lab Checklist

- [ ] Documented Contoso’s main business objectives and pain points
- [ ] Identified at least 5 potential AI/agent use cases
- [ ] Assessed readiness across data, technology, people, and governance
- [ ] Prioritized use cases by value and feasibility
- [ ] Created a one‑page AI opportunity summary for leadership
- [ ] (Optional) Mapped 1–2 use cases to Azure/Copilot Studio building blocks

