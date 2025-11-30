# Lab 05: Create a Basic Agent in Copilot Studio

## 🎯 Lab Goal

Create a **custom agent** in Microsoft Copilot Studio:

- Set up Copilot Studio environment
- Create an agent with basic configuration
- Test the agent in the studio

This supports the **Build agents with Copilot Studio** domain of MS‑102.

---

## ✅ Prerequisites

- Copilot Studio license or trial
- Power Platform environment access

---

## Step 1 – Access Copilot Studio

1. Go to **copilotstudio.microsoft.com**.
2. Sign in with your organizational account.
3. Select or create an environment.

---

## Step 2 – Create a New Agent

1. Click **+ Create** in the left navigation.
2. Choose **New agent**.
3. Configure:
   - **Name**: `IT Help Desk Agent`
   - **Description**: "Helps employees with common IT questions"
   - **Language**: English (or your preferred)
4. Click **Create**.

---

## Step 3 – Configure Agent Identity

1. In the agent settings, go to **Details**.
2. Configure:
   - **Display name**: `IT Help Desk`
   - **Icon**: Upload or choose an icon
   - **Short description**: "Your IT assistant"
   - **Long description**: Detailed info about capabilities

---

## Step 4 – Configure Agent Instructions

### System Message:

1. Go to **Agent → Instructions**.
2. Write instructions that define agent behavior:

```
You are an IT Help Desk assistant for Contoso Corporation.

Your role is to:
- Help employees with common IT issues
- Provide guidance on using Microsoft 365 apps
- Direct complex issues to the IT support team

Behavior guidelines:
- Be friendly and professional
- Provide step-by-step instructions when helpful
- If you don't know the answer, suggest contacting IT support
- Never share passwords or sensitive information
```

---

## Step 5 – Configure Knowledge Sources

### Add SharePoint Source:

1. Go to **Knowledge**.
2. Click **+ Add knowledge**.
3. Select **SharePoint**.
4. Choose sites containing IT documentation.
5. Configure:
   - Sites to include
   - Folders/libraries to scan

### Add Website Source:

1. Click **+ Add knowledge**.
2. Select **Public website**.
3. Enter URLs:
   - Company intranet pages
   - Microsoft support pages

### Add Documents:

1. Click **+ Add knowledge**.
2. Select **Files**.
3. Upload:
   - IT policy documents
   - How-to guides
   - FAQ documents

---

## Step 6 – Configure Conversation Starters

1. Go to **Conversation starters**.
2. Add starter prompts:

```
- "How do I reset my password?"
- "I can't connect to VPN"
- "How do I share a file in Teams?"
- "My Outlook is not syncing"
```

These appear as suggested prompts for users.

---

## Step 7 – Test the Agent

1. Click **Test** in the top right.
2. The test pane opens.
3. Try conversations:

```
User: How do I reset my password?
Agent: [Responds based on knowledge and instructions]

User: I'm having trouble with VPN
Agent: [Provides VPN troubleshooting steps]
```

4. Verify:
   - Responses are accurate
   - Tone matches instructions
   - Knowledge sources are being used

---

## Step 8 – Review Agent Analytics

1. Go to **Analytics**.
2. Review (after publishing):
   - Session count
   - Engagement rate
   - Topic performance
   - User satisfaction

---

## Step 9 – Save and Prepare for Publishing

1. Review all settings.
2. Click **Publish** (we'll complete publishing in Lab 07).
3. Choose publishing options:
   - Test only
   - Share with team
   - Publish to channel

---

## Agent Best Practices

| Practice | Benefit |
|----------|--------|
| Clear instructions | Consistent behavior |
| Curated knowledge | Accurate responses |
| Conversation starters | Better user engagement |
| Regular testing | Quality assurance |
| Analytics review | Continuous improvement |

---

## ✅ Lab Checklist

- [ ] Accessed Copilot Studio
- [ ] Created a new agent
- [ ] Configured agent identity and description
- [ ] Wrote system instructions
- [ ] Added knowledge sources (SharePoint, files)
- [ ] Created conversation starters
- [ ] Tested the agent in studio
- [ ] Reviewed analytics options
