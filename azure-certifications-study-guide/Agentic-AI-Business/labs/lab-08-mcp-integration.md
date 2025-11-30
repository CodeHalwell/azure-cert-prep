# Lab 08: Integrate External Tools via MCP

## 🎯 Lab Goal

Design how to integrate **external tools and systems** into your agents using the **Model Context Protocol (MCP)** or similar tool abstraction:

- Identify candidate tools/APIs
- Define tool schemas and capabilities
- Design how agents will call tools safely

This supports the **Deploy AI solutions** domain of AB‑100.

> This lab is architecture-focused; you don’t need to implement a full MCP server.

---

## ✅ Prerequisites

- Understanding of your Contoso AI use cases (Labs 01–07)
- Familiarity with MCP concepts (tools, servers, clients)

---

## Step 1 – Identify External Tools and Data Sources

For your Contoso scenario, list **3–6 external tools/APIs** that an agent may need, such as:

- Order management API (get order status, create returns)
- Inventory system API (check stock levels)
- Knowledge base search API
- CRM system (customer tier, preferences)

For each, capture:

| Tool | Description | Example Operations |
|------|-------------|--------------------|
| Order API | Accesses order status and history | `GetOrderStatus(orderId)`, `ListRecentOrders(customerId)` |

---

## Step 2 – Define Tool Schemas (Inputs/Outputs)

For 2–3 tools, sketch a **schema** (similar to JSON schema) describing:

- Operation name
- Input parameters (name, type, required)
- Output shape

Example (pseudo‑schema):

```json
{
	"name": "get_order_status",
	"description": "Get the status of a customer order by order ID.",
	"input": {
		"type": "object",
		"properties": {
			"order_id": { "type": "string" }
		},
		"required": ["order_id"]
	},
	"output": {
		"type": "object",
		"properties": {
			"status": { "type": "string" },
			"estimated_delivery": { "type": "string" }
		}
	}
}
```

You don’t need exact syntax—focus on clarity.

---

## Step 3 – Decide Which Agents Can Call Which Tools

Using your multi-agent design from Lab 07, create a mapping:

| Agent | Allowed Tools | Reason |
|-------|---------------|--------|
| Order Agent | `get_order_status`, `list_recent_orders` | Needs order data to answer questions |
| Knowledge Agent | `search_kb` | Performs knowledge base lookups |

Ensure **least privilege**: agents should only be able to call tools necessary for their role.

---

## Step 4 – Design Tool Call Flow and Error Handling

Outline how a typical tool call will work:

1. LLM/agent decides to call a tool based on user request.
2. MCP client constructs a tool invocation request using the schema.
3. MCP server calls the actual backend API and returns a structured result.
4. Agent interprets the result and responds to the user.

Then, consider error cases:

- Tool times out
- Invalid input (missing `order_id`)
- Backend API returns an error

Document how the agent should respond in each case (e.g., apologize, ask for clarification, or escalate).

---

## Step 5 – Security and Governance Considerations

For each tool, think about:

- Authentication method (API keys, OAuth, managed identity)
- Data access level (read‑only vs read/write)
- Logging (what is logged and how it is protected)

Capture at least **one security consideration** and **one governance consideration** per tool.

---

## ✅ Lab Checklist

- [ ] Identified 3–6 external tools/APIs relevant to your scenario
- [ ] Defined input/output schemas for at least 2–3 tools
- [ ] Mapped tools to agent roles following least privilege
- [ ] Described the end-to-end tool call flow and error handling
- [ ] Documented key security and governance considerations for tool usage

