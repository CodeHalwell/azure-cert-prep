# Lab 03: Copilot Studio Basics – Topics, Entities, and Flows

## 🎯 Lab Goal

Get hands-on with **Microsoft Copilot Studio** by:

- Creating a simple copilot/agent
- Designing topics, triggers, and entity capture
- Testing and refining conversation flows

This lab supports the **Design AI solutions** domain for AB‑100.

---

## ✅ Prerequisites

- Microsoft 365 tenant with access to Copilot Studio (trial is fine)
- Role allowing you to create and edit copilots
- Basic familiarity with conversational bots

No code is required; this is a low-code experience.

---

## Step 1 – Create a New Copilot

1. Go to Copilot Studio: https://copilotstudio.microsoft.com/
2. Sign in with your work or school account.
3. Select **+ New copilot**.
4. Name it: `Contoso Support Assistant`.
5. Choose the appropriate environment (e.g., default or a sandbox environment).

Once created, you’ll land in the copilot’s design surface.

---

## Step 2 – Explore System Topics and Conversation Canvas

1. In the left navigation, open **Topics**.
2. Review built-in/system topics such as:
	- Greeting
	- Goodbye
	- Escalate to agent (if present)
3. Open the **Greeting** topic and inspect the node-based flow:
	- Trigger phrases
	- Messages sent to the user
	- Any questions/conditions

This helps you understand how Copilot Studio structures conversations.

---

## Step 3 – Create a Custom Topic with Trigger Phrases

You’ll build a topic to help users check store hours.

1. In **Topics**, select **+ Add topic**.
2. Name it: `Store hours`.
3. Add trigger phrases like:
	- "What time do you open?"
	- "Store hours"
	- "Are you open on weekends?"
4. In the authoring canvas, add nodes to:
	- Ask which city or store the customer is interested in
	- Provide a sample answer, e.g.:
	  - "Our Contoso downtown store is open 9am–9pm Monday–Saturday, and 10am–6pm on Sundays."

Keep it simple and rule-based for now.

---

## Step 4 – Capture Entities (Store Location)

1. In the copilot, go to **Entities** and create a new entity:
	- Name: `StoreLocation`
	- Type: **List**
	- Values: add items like `Downtown`, `Airport`, `Mall` with synonyms
2. Return to your `Store hours` topic.
3. Modify the question node to **identify** `StoreLocation` from the user’s answer.
4. Use a conditional step (if available in your UX) to:
	- Provide different responses depending on which `StoreLocation` value is selected
	- Use a default fallback message if no match.

This demonstrates basic **entity capture and branching**.

---

## Step 5 – Test the Copilot

1. Use the **Test** pane on the right side of Copilot Studio.
2. Say "Hi" and verify the greeting.
3. Ask "What are your store hours?" and:
	- Confirm the `Store hours` topic is triggered
	- Provide a location and ensure the bot responds with appropriate hours
4. Try variations like "Are you open at the airport on Sunday?" and see if the entity is recognized.

Adjust trigger phrases and entity values to improve recognition.

---

## Step 6 – (Optional) Add a Handoff Path

For more realistic behavior:

1. At the end of your `Store hours` topic, add a message like:
	- "Would you like to talk to a human agent?"
2. Provide simple options (Yes/No).
3. If **Yes**, end the topic by triggering a system topic or message that explains how to reach support (e.g., phone or email), or that in production you’d connect to a live agent system.

This introduces the concept of **handoff and escalation**.

---

## ✅ Lab Checklist

- [ ] Created a new Copilot Studio agent
- [ ] Reviewed system topics and the conversation canvas
- [ ] Built a custom `Store hours` topic with trigger phrases
- [ ] Defined and used a `StoreLocation` entity in the topic flow
- [ ] Tested the copilot via the Test pane and refined trigger phrases
- [ ] (Optional) Implemented a simple handoff/escalation path

