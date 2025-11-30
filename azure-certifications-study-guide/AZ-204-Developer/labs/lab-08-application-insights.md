# Lab 08: Monitor Applications with Azure Application Insights

## 🎯 Lab Goal

Integrate **Application Insights** to:

- Track requests, dependencies, and exceptions
- Create custom telemetry
- View logs and metrics

This supports the **Instrument solutions to support monitoring and logging** domain of AZ‑204.

---

## ✅ Prerequisites

- Azure subscription
- A deployed web app or Function App
- Python with `opencensus-ext-azure` or Node.js with `applicationinsights`

```bash
pip install opencensus-ext-azure opencensus-ext-flask
```

---

## Step 1 – Create Application Insights Resource

```bash
az group create --name rg-az204-insights --location eastus

az monitor app-insights component create \
  --app ai-az204-<unique> \
  --location eastus \
  --resource-group rg-az204-insights \
  --kind web
```

Get the connection string:

```bash
az monitor app-insights component show \
  --app ai-az204-<unique> \
  --resource-group rg-az204-insights \
  --query connectionString -o tsv
```

---

## Step 2 – Instrument a Flask Application

```python
import os
from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler

app = Flask(__name__)

# Configure Application Insights
middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string=os.getenv("APPINSIGHTS_CONNECTION_STRING")),
    sampler=ProbabilitySampler(rate=1.0),
)

@app.route("/")
def hello():
    return "Hello, monitored world!"

@app.route("/error")
def error():
    raise Exception("Test exception for App Insights")

if __name__ == "__main__":
    app.run()
```

---

## Step 3 – Send Custom Telemetry

```python
from opencensus.ext.azure import metrics_exporter
from opencensus.stats import stats as stats_module
from opencensus.stats import measure, view, aggregation

# Custom metric
request_measure = measure.MeasureInt("requests", "Number of requests", "requests")
request_view = view.View(
    "request_count",
    "Count of requests",
    [],
    request_measure,
    aggregation.CountAggregation()
)

stats = stats_module.stats
view_manager = stats.view_manager
stats_recorder = stats.stats_recorder

exporter = metrics_exporter.new_metrics_exporter(
    connection_string=os.getenv("APPINSIGHTS_CONNECTION_STRING")
)
view_manager.register_exporter(exporter)
view_manager.register_view(request_view)

# Record a metric
mmap = stats_recorder.new_measurement_map()
mmap.measure_int_put(request_measure, 1)
mmap.record()
```

---

## Step 4 – View Telemetry in Azure Portal

1. Go to Application Insights in the portal.
2. Explore:
   - **Live Metrics** – Real-time requests
   - **Failures** – Exceptions and failed requests
   - **Performance** – Request duration and dependencies
   - **Logs** – Query telemetry with Kusto

Sample Kusto query:

```kusto
requests
| where timestamp > ago(1h)
| summarize count() by resultCode
```

---

## Cleanup

```bash
az group delete --name rg-az204-insights --yes --no-wait
```

---

## ✅ Lab Checklist

- [ ] Created an Application Insights resource
- [ ] Instrumented a Flask app with OpenCensus
- [ ] Generated requests and exceptions
- [ ] Sent custom metrics/telemetry
- [ ] Viewed telemetry in the Azure portal
- [ ] Cleaned up resources
