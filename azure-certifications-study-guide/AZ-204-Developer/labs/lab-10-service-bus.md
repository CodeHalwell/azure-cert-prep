# Lab 10: Implement Asynchronous Messaging with Azure Service Bus

## 🎯 Lab Goal

Use **Azure Service Bus** to:

- Send and receive messages via queues
- Work with topics and subscriptions

This supports the **Develop message-based solutions** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- Python 3.9+ with `azure-servicebus` package

```bash
pip install azure-servicebus python-dotenv
```

---

## Step 1 – Create a Service Bus Namespace and Queue

```bash
az group create --name rg-az204-sb --location eastus

az servicebus namespace create \
  --name sb-az204-<unique> \
  --resource-group rg-az204-sb \
  --sku Standard

az servicebus queue create \
  --name orders \
  --namespace-name sb-az204-<unique> \
  --resource-group rg-az204-sb
```

Get the connection string:

```bash
az servicebus namespace authorization-rule keys list \
  --namespace-name sb-az204-<unique> \
  --resource-group rg-az204-sb \
  --name RootManageSharedAccessKey \
  --query primaryConnectionString -o tsv
```

---

## Step 2 – Send Messages to Queue

```python
import os
from dotenv import load_dotenv
from azure.servicebus import ServiceBusClient, ServiceBusMessage

load_dotenv()
conn_str = os.getenv("SERVICEBUS_CONNECTION_STRING")

with ServiceBusClient.from_connection_string(conn_str) as client:
    sender = client.get_queue_sender(queue_name="orders")
    with sender:
        for i in range(5):
            message = ServiceBusMessage(f"Order {i}")
            sender.send_messages(message)
            print(f"Sent: Order {i}")
```

---

## Step 3 – Receive Messages from Queue

```python
with ServiceBusClient.from_connection_string(conn_str) as client:
    receiver = client.get_queue_receiver(queue_name="orders", max_wait_time=5)
    with receiver:
        for msg in receiver:
            print(f"Received: {str(msg)}")
            receiver.complete_message(msg)
```

---

## Step 4 – Create a Topic and Subscription

```bash
az servicebus topic create \
  --name notifications \
  --namespace-name sb-az204-<unique> \
  --resource-group rg-az204-sb

az servicebus topic subscription create \
  --name email-sub \
  --topic-name notifications \
  --namespace-name sb-az204-<unique> \
  --resource-group rg-az204-sb

az servicebus topic subscription create \
  --name sms-sub \
  --topic-name notifications \
  --namespace-name sb-az204-<unique> \
  --resource-group rg-az204-sb
```

---

## Step 5 – Publish and Subscribe

```python
# Send to topic
with ServiceBusClient.from_connection_string(conn_str) as client:
    sender = client.get_topic_sender(topic_name="notifications")
    with sender:
        sender.send_messages(ServiceBusMessage("New notification!"))
        print("Sent to topic")

# Receive from subscription
with ServiceBusClient.from_connection_string(conn_str) as client:
    receiver = client.get_subscription_receiver(
        topic_name="notifications",
        subscription_name="email-sub",
        max_wait_time=5
    )
    with receiver:
        for msg in receiver:
            print(f"Email sub received: {str(msg)}")
            receiver.complete_message(msg)
```

---

## Cleanup

```bash
az group delete --name rg-az204-sb --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created a Service Bus namespace and queue
- [ ] Sent messages to a queue using the SDK
- [ ] Received and completed messages from the queue
- [ ] Created a topic with multiple subscriptions
- [ ] Published to a topic and received from subscriptions
- [ ] Cleaned up resources
