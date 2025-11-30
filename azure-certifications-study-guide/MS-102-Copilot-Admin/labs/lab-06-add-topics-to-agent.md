# Lab 06: Add Topics and Actions to an Agent

## 🎯 Lab Goal

Enhance your agent with **topics and actions**:

- Create custom topics for specific scenarios
- Add actions to perform tasks
- Configure topic triggers and flows

This supports the **Build agents with Copilot Studio** domain of MS‑102.

---

## ✅ Prerequisites

- Agent created in Lab 05
- Copilot Studio access

---

## Step 1 – Understand Topics vs. Actions

| Concept | Purpose |
|---------|--------|
| Topic | Conversation flow for a specific scenario |
| Action | Task the agent can perform (create ticket, send email) |
| Trigger | Phrase or condition that starts a topic |
| Node | Step in a topic flow |

---

## Step 2 – Create a Custom Topic

1. Open your agent in Copilot Studio.
2. Go to **Topics**.
3. Click **+ Add topic → From blank**.
4. Configure:
   - **Name**: `Password Reset`
   - **Description**: "Help users reset their passwords"

---

## Step 3 – Configure Trigger Phrases

1. In the topic, go to **Trigger phrases**.
2. Add phrases that activate this topic:

```
- "reset my password"
- "forgot my password"
- "can't log in"
- "password expired"
- "change my password"
- "need a new password"
```

The AI will recognize variations of these phrases.

---

## Step 4 – Build the Topic Flow

### Add Message Node:

1. Click **+** to add a node.
2. Select **Send a message**.
3. Enter:

```
I can help you reset your password. Let me gather some information first.
```

### Add Question Node:

1. Add another node → **Ask a question**.
2. Configure:
   - **Question**: "What type of account are you trying to reset?"
   - **Options**: 
     - Work email
     - VPN
     - System access
3. Save response to a variable: `AccountType`

### Add Condition Node:

1. Add node → **Add a condition**.
2. Configure branches:

```
If AccountType = "Work email":
  → Provide self-service reset instructions
  
If AccountType = "VPN":
  → Escalate to IT support
  
Otherwise:
  → Ask for more details
```

---

## Step 5 – Add an Action

### Create Ticket Action:

1. Go to **Actions**.
2. Click **+ Add action**.
3. Choose action type:
   - **Power Automate flow**: Connect to existing flow
   - **Plugin**: Use a connector
   - **HTTP request**: Call an API

### Configure Power Automate Action:

1. Select **Create new flow** or use existing.
2. Configure flow:
   - Trigger: From Copilot
   - Action: Create item in SharePoint/ServiceNow
   - Return: Ticket number

3. In Copilot Studio, configure:
   - **Input parameters**: Issue description, user email
   - **Output**: Ticket ID

---

## Step 6 – Use Action in Topic

1. In your topic flow, add node → **Call an action**.
2. Select the action you created.
3. Map inputs:
   - Description: `IssueDescription` variable
   - Email: `System.User.Email`
4. Store output:
   - TicketID: `CreatedTicketNumber`

5. Add message:

```
I've created a support ticket for you. Your ticket number is {CreatedTicketNumber}. 
Our IT team will contact you within 24 hours.
```

---

## Step 7 – Add Entity Recognition

### Use Built-in Entities:

1. In a question node, use entities:
   - **Email**: Automatically recognizes email addresses
   - **Number**: Recognizes numbers
   - **Date/Time**: Recognizes dates

### Create Custom Entity:

1. Go to **Entities**.
2. Click **+ Add entity**.
3. Configure:
   - **Name**: `ITSystems`
   - **Type**: Closed list
   - **Values**: Outlook, Teams, SharePoint, VPN, Printer

4. Use in questions:

```
Which system are you having trouble with?
[Uses ITSystems entity for recognition]
```

---

## Step 8 – Add Topic Handoff

### Escalate to Human:

1. Add node → **Transfer conversation**.
2. Configure:
   - Target: Dynamics 365 Customer Service
   - Or: Microsoft Teams

### End with Survey:

1. Add node → **End conversation**.
2. Enable satisfaction survey.

---

## Step 9 – Test the Enhanced Topic

1. Click **Test** in the top right.
2. Try the conversation:

```
User: I forgot my password
Agent: I can help you reset your password. What type of account?
User: Work email
Agent: [Provides instructions or creates ticket]
User: Thanks!
Agent: [Shows satisfaction survey]
```

3. Verify:
   - Trigger phrases work
   - Flow branches correctly
   - Actions execute successfully

---

## ✅ Lab Checklist

- [ ] Understood topics, actions, and triggers
- [ ] Created a custom topic
- [ ] Added trigger phrases
- [ ] Built topic flow with messages and questions
- [ ] Added condition branches
- [ ] Created and configured an action
- [ ] Used action in topic flow
- [ ] Added entity recognition
- [ ] Tested the complete topic
