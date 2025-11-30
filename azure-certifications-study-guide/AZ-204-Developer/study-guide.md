# 📖 AZ-204 Study Guide

## Azure Developer Associate

This study guide covers all skills measured in the AZ-204 exam.

---

# Domain 1: Develop Azure Compute Solutions (25-30%)

## 1.1 Azure App Service

### App Service Plans

| Tier | Features | Use Case |
|------|----------|----------|
| **Free/Shared** | Limited, shared compute | Dev/test |
| **Basic** | Dedicated compute, custom domain | Low traffic |
| **Standard** | Autoscale, staging slots | Production |
| **Premium** | More slots, VNet integration | Enterprise |
| **Isolated** | App Service Environment | High security |

### Deployment Slots

```
Production Slot ◄─── Swap ───► Staging Slot
     │                              │
     └── Traffic 100%               └── Traffic 0%
         
After swap:
Production (was Staging) ◄───► Staging (was Production)
```

### App Settings

```csharp
// Access app settings in C#
var connectionString = Environment.GetEnvironmentVariable("ConnectionString");

// Configuration in .NET
builder.Services.Configure<AppSettings>(
    builder.Configuration.GetSection("AppSettings")
);
```

---

## 1.2 Azure Functions

### Triggers

| Trigger | Use Case |
|---------|----------|
| **HTTP** | REST APIs, webhooks |
| **Timer** | Scheduled jobs |
| **Blob** | File processing |
| **Queue** | Message processing |
| **Event Grid** | Event handling |
| **Cosmos DB** | Database changes |
| **Service Bus** | Enterprise messaging |

### Bindings Example

```csharp
[Function("ProcessOrder")]
[BlobOutput("orders-processed/{id}.json")]
public static string Run(
    [QueueTrigger("orders")] Order order,
    [CosmosDBInput("database", "customers", 
        Id = "{customerId}")] Customer customer,
    FunctionContext context)
{
    var logger = context.GetLogger("ProcessOrder");
    logger.LogInformation($"Processing order {order.Id}");
    
    return JsonSerializer.Serialize(new ProcessedOrder(order, customer));
}
```

### Durable Functions Patterns

| Pattern | Description |
|---------|-------------|
| **Function chaining** | Sequential execution |
| **Fan-out/fan-in** | Parallel execution |
| **Async HTTP APIs** | Long-running operations |
| **Monitor** | Polling pattern |
| **Human interaction** | Approval workflows |

---

## 1.3 Container Solutions

### Azure Container Apps

```yaml
# Container App configuration
properties:
  template:
    containers:
      - name: myapp
        image: myregistry.azurecr.io/myapp:v1
        resources:
          cpu: 0.5
          memory: 1Gi
    scale:
      minReplicas: 1
      maxReplicas: 10
      rules:
        - name: http-scaling
          http:
            metadata:
              concurrentRequests: 100
```

### Container Registry

```bash
# Build and push image
az acr build --registry myregistry --image myapp:v1 .

# Enable admin
az acr update -n myregistry --admin-enabled true
```

---

# Domain 2: Develop for Azure Storage (15-20%)

## 2.1 Blob Storage

### Storage Tiers

| Tier | Access | Cost |
|------|--------|------|
| **Hot** | Frequent | High storage, low access |
| **Cool** | Infrequent (30+ days) | Lower storage, higher access |
| **Cold** | Rare (90+ days) | Lower storage, higher access |
| **Archive** | Rarely (180+ days) | Lowest storage, highest access |

### Blob SDK

```csharp
// Upload blob
BlobClient blobClient = containerClient.GetBlobClient(blobName);
await blobClient.UploadAsync(stream, overwrite: true);

// Download blob
BlobDownloadResult result = await blobClient.DownloadContentAsync();
string content = result.Content.ToString();

// Set metadata
var metadata = new Dictionary<string, string>
{
    { "category", "documents" },
    { "author", "user1" }
};
await blobClient.SetMetadataAsync(metadata);
```

### Lifecycle Management

```json
{
  "rules": [
    {
      "name": "move-to-cool",
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": ["blockBlob"]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 }
          }
        }
      }
    }
  ]
}
```

---

## 2.2 Cosmos DB

### Consistency Levels

| Level | Guarantee | Performance |
|-------|-----------|-------------|
| **Strong** | Linearizable | Highest latency |
| **Bounded Staleness** | Bounded lag | High latency |
| **Session** | Read your writes | Balanced |
| **Consistent Prefix** | Ordered reads | Low latency |
| **Eventual** | No order guarantee | Lowest latency |

### SDK Operations

```csharp
// Create item
await container.CreateItemAsync(item, new PartitionKey(item.Category));

// Query items
var query = container.GetItemQueryIterator<Product>(
    "SELECT * FROM c WHERE c.category = 'electronics'"
);

while (query.HasMoreResults)
{
    var response = await query.ReadNextAsync();
    foreach (var item in response)
    {
        Console.WriteLine(item.Name);
    }
}
```

---

# Domain 3: Implement Azure Security (20-25%)

## 3.1 Authentication

### MSAL Authentication

```csharp
// Interactive authentication
var app = PublicClientApplicationBuilder
    .Create(clientId)
    .WithAuthority(AzureCloudInstance.AzurePublic, tenantId)
    .WithRedirectUri("http://localhost")
    .Build();

var result = await app.AcquireTokenInteractive(scopes).ExecuteAsync();
```

### Managed Identity

```csharp
// Use managed identity
var credential = new DefaultAzureCredential();

// Access Key Vault
var client = new SecretClient(
    new Uri("https://myvault.vault.azure.net/"),
    credential
);

var secret = await client.GetSecretAsync("MySecret");
```

---

## 3.2 Azure Key Vault

### Key Vault Operations

```csharp
// Secret operations
var secretClient = new SecretClient(vaultUri, credential);
await secretClient.SetSecretAsync("SecretName", "SecretValue");
var secret = await secretClient.GetSecretAsync("SecretName");

// Key operations
var keyClient = new KeyClient(vaultUri, credential);
var key = await keyClient.CreateKeyAsync("KeyName", KeyType.Rsa);

// Certificate operations
var certClient = new CertificateClient(vaultUri, credential);
var cert = await certClient.GetCertificateAsync("CertName");
```

---

# Domain 4: Monitor, Troubleshoot, Optimize (15-20%)

## 4.1 Application Insights

### Telemetry

```csharp
// Track custom event
telemetryClient.TrackEvent("OrderPlaced", new Dictionary<string, string>
{
    { "OrderId", orderId },
    { "CustomerId", customerId }
});

// Track metric
telemetryClient.TrackMetric("OrderValue", orderValue);

// Track dependency
using (var operation = telemetryClient.StartOperation<DependencyTelemetry>("External API"))
{
    // Call external service
    operation.Telemetry.Success = true;
}
```

---

## 4.2 Azure Cache for Redis

### Caching Patterns

| Pattern | Description |
|---------|-------------|
| **Cache-aside** | Load on miss, store on read |
| **Write-through** | Write to cache and DB |
| **Write-behind** | Write to cache, async to DB |

```csharp
// Cache-aside pattern
public async Task<Product> GetProductAsync(string id)
{
    var cacheKey = $"product:{id}";
    var cached = await cache.GetStringAsync(cacheKey);
    
    if (cached != null)
        return JsonSerializer.Deserialize<Product>(cached);
    
    var product = await database.GetProductAsync(id);
    await cache.SetStringAsync(cacheKey, JsonSerializer.Serialize(product));
    
    return product;
}
```

---

# Domain 5: Connect to and Consume Services (15-20%)

## 5.1 API Management

### Policies

```xml
<policies>
    <inbound>
        <rate-limit calls="100" renewal-period="60" />
        <set-header name="X-Custom-Header" exists-action="override">
            <value>MyValue</value>
        </set-header>
        <validate-jwt header-name="Authorization">
            <issuer-signing-keys>
                <key>base64-encoded-key</key>
            </issuer-signing-keys>
        </validate-jwt>
    </inbound>
    <backend>
        <forward-request />
    </backend>
    <outbound>
        <set-header name="X-Powered-By" exists-action="delete" />
    </outbound>
</policies>
```

---

## 5.2 Messaging Services

### Service Bus vs Event Grid

| Feature | Service Bus | Event Grid |
|---------|-------------|------------|
| Pattern | Message queue | Event routing |
| Ordering | Guaranteed | Not guaranteed |
| Delivery | At-least-once | At-least-once |
| Size | Up to 100MB | 1MB |
| Use case | Enterprise messaging | Event distribution |

### Service Bus Example

```csharp
// Send message
await sender.SendMessageAsync(new ServiceBusMessage("Hello"));

// Receive message
var message = await receiver.ReceiveMessageAsync();
await receiver.CompleteMessageAsync(message);
```

---

## ✅ Study Checklist

### Compute
- [ ] App Service deployment and configuration
- [ ] Azure Functions triggers and bindings
- [ ] Container Apps and ACI

### Storage
- [ ] Blob Storage operations and tiers
- [ ] Cosmos DB queries and consistency

### Security
- [ ] MSAL authentication flows
- [ ] Managed identities
- [ ] Key Vault integration

### Monitoring
- [ ] Application Insights telemetry
- [ ] Caching strategies

### Integration
- [ ] API Management policies
- [ ] Service Bus and Event Grid

---

*Last updated: November 2025*
