# 🧪 AZ-204 Practice Resources

## Official Practice Assessment

| Resource | Details |
|----------|---------|
| **Link** | [AZ-204 Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/practice/assessment?assessment-type=practice&assessmentId=35) |
| **Format** | Multiple choice, code scenarios |
| **Cost** | Free |

---

## ☁️ Hands-On Practice

### Azure Free Account

| Feature | Details |
|---------|---------|
| **Link** | [Create Free Account](https://azure.microsoft.com/free/) |
| **Credit** | $200 for 30 days |
| **Free Services** | App Service, Functions, Cosmos DB free tier |

---

## 📚 Key Labs by Domain

### Compute Solutions
| Lab | Skills |
|-----|--------|
| Deploy App Service | Web apps, slots |
| Create Azure Functions | Triggers, bindings |
| Deploy Container Apps | Containers, scaling |

### Storage Solutions
| Lab | Skills |
|-----|--------|
| Blob operations | Upload, download, tiers |
| Cosmos DB CRUD | Queries, partitioning |

### Security
| Lab | Skills |
|-----|--------|
| MSAL authentication | OAuth flows |
| Key Vault integration | Secrets management |
| Managed identity | System-assigned |

### Integration
| Lab | Skills |
|-----|--------|
| API Management | Policies, products |
| Service Bus | Queues, topics |
| Event Grid | Event routing |

---

## 🔧 Code Practice

### Azure Functions

```csharp
[Function("HttpTrigger")]
public static async Task<HttpResponseData> Run(
    [HttpTrigger(AuthorizationLevel.Function, "get", "post")] HttpRequestData req,
    FunctionContext context)
{
    var response = req.CreateResponse(HttpStatusCode.OK);
    await response.WriteStringAsync("Hello from Azure Functions!");
    return response;
}
```

### Blob Storage

```csharp
var blobClient = containerClient.GetBlobClient(blobName);
await blobClient.UploadAsync(stream, overwrite: true);
```

---

## 🔗 Resources

| Resource | Link |
|----------|------|
| Azure Code Samples | [GitHub](https://github.com/Azure-Samples) |
| Exam Sandbox | [Link](https://aka.ms/examdemo) |
| SDK Documentation | [Link](https://learn.microsoft.com/en-us/dotnet/azure/) |

---

*Last updated: November 2025*
