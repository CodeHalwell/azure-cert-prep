# Lab 09: Monitor Agentic AI Solutions

## 🎯 Lab Goal

Design a **monitoring and evaluation approach** for agentic AI solutions:

- Define key metrics and signals
- Plan logging and tracing
- Design feedback and evaluation loops

This supports the **Deploy AI solutions** domain for AB‑100.

---

## ✅ Prerequisites

- Prior labs defining agents, RAG, and tool usage (Labs 04–08)
- Familiarity with basic observability concepts

---

## Step 1 – Define Metrics Across Layers

Consider three layers: **Business**, **Experience**, and **Technical**.

Create a table like:

| Layer | Metric | Description |
|-------|--------|-------------|
| Business | Conversion rate | % of sessions that lead to purchase |
| Experience | CSAT / thumbs up | User satisfaction with responses |
| Technical | Latency | Time from user input to response |

List at least **3 metrics per layer** relevant to your Contoso use cases.

---

## Step 2 – Plan Logging and Tracing

For your agents and tools, decide:

- What events to log (e.g., user messages, tool calls, errors)
- How to correlate events across agents (trace IDs, session IDs)
- Where to store logs (e.g., Application Insights, Log Analytics, custom store)

Sketch a simple log schema, for example:

| Field | Description |
|-------|-------------|
| `timestamp` | When the event occurred |
| `session_id` | Unique conversation/session identifier |
| `agent_name` | Which agent handled the turn |
| `event_type` | `user_message`, `tool_call`, `error`, etc. |

---

## Step 3 – Design User Feedback Collection

Define how you will collect **explicit** and **implicit** feedback:

- Explicit:
	- Thumbs up/down on responses
	- Short survey after session
- Implicit:
	- Escalation to human
	- Abandonment mid-conversation

Document where and how this feedback is stored, and who reviews it.

---

## Step 4 – Plan Evaluation and Review Cadence

Design a simple evaluation process:

- How often will the team review conversations? (e.g., weekly sampling)
- Who participates? (e.g., AI product owner, support lead, data scientist)
- What will they look for? (accuracy, tone, policy violations)

Define a **cadence** table:

| Cadence | Activity | Owner |
|---------|----------|-------|
| Weekly | Review 20 random conversations | AI product owner |
| Monthly | Deep dive on KPI trends | Analytics team |

---

## Step 5 – Connect to Azure Monitoring Tools (Conceptual)

Identify which Azure services you would use to support monitoring, for example:

- **Application Insights / Azure Monitor** for logs and metrics
- **Azure AI Studio evaluation tools** for LLM quality
- **Dashboards** (Azure dashboards or Power BI) for key KPIs

Map your metrics to specific tools/reports.

---

## ✅ Lab Checklist

- [ ] Defined business, experience, and technical metrics for agentic AI
- [ ] Planned logging and tracing structure (fields, correlation IDs, storage)
- [ ] Designed how user feedback will be collected and used
- [ ] Established an evaluation and review cadence with clear owners
- [ ] Mapped monitoring needs to Azure and/or analytics tools

