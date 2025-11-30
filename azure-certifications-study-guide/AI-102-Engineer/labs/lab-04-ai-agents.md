# Lab 04: Create AI Agents

## 🎯 Lab Goal

Design and implement a simple **AI agent** that:

- Maintains multi‑turn conversation state
- Calls one or more **tools/functions** to answer questions
- Uses Azure OpenAI under the hood for reasoning

This aligns with AI‑102 topics around orchestrating AI workflows, tools, and conversations.

---

## ✅ Prerequisites

- Completed Labs 01–03 (provisioning, OpenAI client, optional RAG backend)
- Python 3.9+ and the `openai` package available

---

## Step 1 – Define a Simple Tool

For this lab, we’ll build a trivial “weather lookup” tool (mocked), but you can adapt it to any domain.

```python
# tools.py
from datetime import datetime


def get_weather(city: str) -> str:
	# In a real app you'd call an external API.
	# Here we return a deterministic fake response.
	return f"The weather in {city} is sunny and 24°C (simulated)."


def get_time() -> str:
	return datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
```

---

## Step 2 – Describe Tools to the Model

Use Azure OpenAI **function calling** (tools) to let the model decide when to call your functions.

```python
# agent.py
from typing import Any, Dict
from openai_client import client, AZURE_OPENAI_CHAT_DEPLOYMENT
from tools import get_weather, get_time


TOOLS = [
	{
		"type": "function",
		"function": {
			"name": "get_weather",
			"description": "Get the current weather in a city (simulated).",
			"parameters": {
				"type": "object",
				"properties": {
					"city": {"type": "string", "description": "City name"},
				},
				"required": ["city"],
			},
		},
	},
	{
		"type": "function",
		"function": {
			"name": "get_time",
			"description": "Get current UTC time.",
			"parameters": {"type": "object", "properties": {}},
		},
	},
]


def call_tool(name: str, arguments: Dict[str, Any]) -> str:
	if name == "get_weather":
		return get_weather(arguments.get("city", ""))
	if name == "get_time":
		return get_time()
	return "Unknown tool"


def agent_chat(user_input: str, history: list[dict]) -> tuple[str, list[dict]]:
	messages = [
		{"role": "system", "content": "You are an assistant that can call tools when helpful."},
		*history,
		{"role": "user", "content": user_input},
	]

	response = client.chat.completions.create(
		model=AZURE_OPENAI_CHAT_DEPLOYMENT,
		messages=messages,
		tools=TOOLS,
		tool_choice="auto",
		temperature=0.3,
	)

	message = response.choices[0].message

	# If the model wants to call a tool
	if message.tool_calls:
		for tool_call in message.tool_calls:
			name = tool_call.function.name
			args = tool_call.function.arguments or "{}"

			import json

			parsed_args = json.loads(args)
			tool_result = call_tool(name, parsed_args)

			# Add tool call and result to history
			history.append({"role": "assistant", "content": None, "tool_calls": [
				{
					"id": tool_call.id,
					"type": "function",
					"function": {"name": name, "arguments": args},
				}
			]})

			history.append(
				{
					"role": "tool",
					"tool_call_id": tool_call.id,
					"name": name,
					"content": tool_result,
				}
			)

		# Second call: let the model respond using tool results
		follow_up = client.chat.completions.create(
			model=AZURE_OPENAI_CHAT_DEPLOYMENT,
			messages=[
				{"role": "system", "content": "You are an assistant that can call tools when helpful."},
				*history,
			],
			temperature=0.3,
		)
		final_msg = follow_up.choices[0].message
		history.append({"role": "assistant", "content": final_msg.content})
		return final_msg.content or "", history

	# No tool call: just respond
	history.append({"role": "assistant", "content": message.content})
	return message.content or "", history


def main():
	history: list[dict] = []
	print("Agent Chat – type 'exit' to quit")
	while True:
		user = input("You: ")
		if user.lower() in {"exit", "quit"}:
			break
		answer, history = agent_chat(user, history)
		print("Agent:\n", answer, "\n")


if __name__ == "main__":  # note: fix to __name__ == "__main__" in your code
	main()
```

> Ensure you fix the guard to `if __name__ == "__main__":` when copying.

---

## Step 3 – Test the Agent

Try prompts like:

- “What time is it now?” → agent should call `get_time`.
- “What is the weather in London?” → agent should call `get_weather`.
- “Explain what you just did.” → no tool call, just a narrative explanation.

Observe in logs:

- When the model chooses to call tools
- The arguments it passes
- How the second call incorporates tool results into the answer

---

## Step 4 – Discuss Design Considerations

Reflect (and take notes) on:

- How would you **restrict** which tools are available in regulated environments?
- When would you route to **RAG** instead of a simple tool?
- Where would you enforce **authorization** (e.g., user cannot call certain tools)?

These design questions often appear in scenario‑style questions in AI‑102.

---

## ✅ Lab Checklist

- [ ] Simple tools implemented in code (`get_weather`, `get_time`)
- [ ] Tools described to the model via function/tool schema
- [ ] Agent loop implemented with multi‑turn history
- [ ] Tool call round‑trip (model → tool → model) working
- [ ] Notes captured on security, routing, and governance for tools

