# Lab 04: Designing Generative AI Agents

## 🎯 Lab Goal

Design and prototype a **generative AI agent** that uses LLM capabilities for Contoso Retail:

- Define the agent’s purpose and boundaries
- Draft system messages/prompts
- Test behavior in a chat playground (Copilot Studio or Azure AI Studio)

This supports the **Design AI solutions** domain for AB‑100.

---

## ✅ Prerequisites

- Completed Labs 01–03 (assessment, strategy, Copilot basics)
- Access to either **Copilot Studio** or **Azure AI Studio** chat playgrounds

Coding is optional; the focus is on design.

---

## Step 1 – Define the Agent’s Role and Scope

Choose **one** high‑priority use case from Lab 01 (e.g., "Customer FAQ & order status agent").

Document for this agent:

- **Primary goal** (e.g., "answer customer questions and provide order status")
- **In‑scope topics** (FAQ, store hours, basic order tracking)
- **Out‑of‑scope topics** (legal advice, HR questions, internal operations)
- **Success metrics** (CSAT, deflection rate, average handle time)

This becomes your **agent charter**.

---

## Step 2 – Draft the System Message / Instructions

Write a **system message** that will be used in Copilot Studio or Azure AI Studio. For example:

> You are Contoso’s Customer Support Copilot. Your job is to help customers with store hours, product information, and order status. If you do not know the answer or the question is outside these topics, you must say you don’t know and suggest contacting human support. Always be polite, concise, and clear.

Include:

- Tone (friendly, professional)
- Behavior when knowledge is missing
- Compliance requirements (no making up policies or prices)

---

## Step 3 – Create a Prototype in a Chat Playground

In **Azure AI Studio** or Copilot Studio:

1. Open a **Chat** or **Prompt flow** / generative playground.
2. Enter your system message as the **system prompt**.
3. Test sample user queries:
	- "What time do you open on Saturday?"
	- "Can you tell me about my salary at Contoso?" (out of scope)
	- "What’s your return policy?"

Observe:

- Does the agent follow scope boundaries?
- Does it respond clearly when out of scope?

Adjust the system message to tighten behavior as needed.

---

## Step 4 – Design Guardrails and Fallbacks

Think through **guardrails** for this agent:

- What types of content should it **never** generate? (e.g., offensive content, legal promises)
- How should it respond to ambiguous or risky questions?
- When should it escalate to a human?

Document 5–10 bullet points under headings such as:

- Safety & tone
- Data and privacy
- Escalation rules

These will later map to content filters and safety settings.

---

## Step 5 – Map to Data Sources (Conceptual)

Identify what **data sources** this agent should use in production:

- FAQ documents or knowledge base
- Order management system/API
- Store hours database or configuration

For each data source, note:

- How often it changes
- Who owns it
- How the agent would access it (read‑only, via API, via RAG, etc.)

This prepares you for Labs 05–06 (Azure AI Studio and RAG).

---

## Step 6 – Summarize Agent Design

Create a short **agent design one‑pager** that includes:

- Agent charter (role, scope, goals)
- System message
- Guardrails
- Data sources and access approach

This is the kind of artifact AB‑100 expects you to interpret or create in scenario questions.

---

## ✅ Lab Checklist

- [ ] Selected a high‑priority use case and defined an agent charter
- [ ] Drafted a clear system message/instructions for the agent
- [ ] Tested the agent behavior in a chat playground
- [ ] Documented guardrails for safety, privacy, and escalation
- [ ] Mapped the agent to key data sources and access patterns
- [ ] Created a concise agent design summary

