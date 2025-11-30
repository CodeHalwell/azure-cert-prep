# Lab 07: Build a Multi-Agent Orchestration Pattern

## 🎯 Lab Goal

Design a **multi-agent orchestration pattern** for Contoso, where multiple specialized agents collaborate under an orchestrator:

- Define agent roles and responsibilities
- Design the orchestration flow
- Optionally map to a framework (Semantic Kernel, AutoGen, etc.)

This supports the **Deploy AI solutions** domain of AB‑100.

---

## ✅ Prerequisites

- Understanding of single-agent design (Lab 04)
- Basic familiarity with multi-agent concepts

Hands-on coding is optional; focus on architecture.

---

## Step 1 – Identify the Multi-Agent Scenario

Choose a scenario where multiple skills are needed. For example:

- "Customer support triage and resolution" across:
	- FAQ lookup
	- Order status
	- Returns eligibility

Write 2–3 example conversations that would benefit from multiple agents.

---

## Step 2 – Define Agent Types

Propose **3–4 agents** such as:

- **Orchestrator Agent** – Routes requests, manages context, decides which agent to call
- **Knowledge Agent** – Performs RAG over FAQs/policies
- **Order Agent** – Calls order APIs and interprets responses
- **Returns Agent** – Applies business rules for eligibility

For each agent, document:

| Agent | Responsibilities | Inputs | Outputs |
|-------|-------------------|--------|---------|
| Orchestrator | Classify user intent, call other agents, compose final answer | User query, prior context | Final answer, follow-up actions |

---

## Step 3 – Design the Orchestration Flow

Draw or describe the orchestration pattern:

1. User sends a message
2. Orchestrator:
	 - Classifies intent (FAQ vs order vs returns vs other)
	 - Calls the appropriate specialist agent(s)
	 - Aggregates results
3. Orchestrator sends a grounded, user-friendly response

Include how errors are handled (e.g., when an agent fails or returns low-confidence results).

---

## Step 4 – Map to an Implementation Framework (Conceptual)

Choose a framework such as **Semantic Kernel**, **AutoGen**, or similar.

High-level mapping:

- How agents would be represented (skills, tools, or agents)
- How orchestration logic would be implemented (planner, manual routing, etc.)
- Where prompts and system messages live for each agent

You do not need full code; focus on how responsibilities would map to components.

---

## Step 5 – Consider Observability and Control

For this multi-agent system, answer:

- What logs and traces do you need (e.g., which agent was called, with what inputs/outputs)?
- How will you capture **user feedback** (thumbs up/down, comments)?
- How will you debug a problematic conversation?

Document 3–5 monitoring and control mechanisms you would implement.

---

## ✅ Lab Checklist

- [ ] Selected a scenario that benefits from multiple agents
- [ ] Defined at least 3–4 agent roles with responsibilities
- [ ] Designed an orchestration flow from user query to final answer
- [ ] Mapped the design to a concrete framework (e.g., Semantic Kernel or AutoGen) at a conceptual level
- [ ] Identified key observability and control requirements for multi-agent systems

