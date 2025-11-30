# Project 06: Architecture Guide

## 🏗️ System Architecture

### Data Pipeline

```mermaid
graph LR
    subgraph "Data Sources"
        A[IoT Sensors] --> B[IoT Hub]
    end
    
    subgraph "Stream Processing"
        B --> C[Event Hubs]
        C --> D[Stream Analytics]
        D --> E{Anomaly?}
    end
    
    subgraph "ML Inference"
        E -->|Potential| F[ML Endpoint]
        F --> G{Failure Risk}
    end
    
    subgraph "Actions"
        G -->|High| H[Alert]
        G -->|Medium| I[Schedule Maintenance]
        G -->|Low| J[Log Only]
    end
    
    style F fill:#e8f5e9
```

---

## Machine Learning Pipeline

```mermaid
graph TB
    subgraph "Training"
        A[Historical Data] --> B[Feature Engineering]
        B --> C[Model Training]
        C --> D[Evaluation]
        D --> E{Metrics OK?}
        E -->|Yes| F[Register Model]
        E -->|No| C
    end
    
    subgraph "Deployment"
        F --> G[Create Endpoint]
        G --> H[Deploy Model]
        H --> I[Monitor Performance]
    end
    
    subgraph "Retraining"
        I --> J{Drift Detected?}
        J -->|Yes| A
    end
```

---

## Feature Engineering

Key features for predictive maintenance:

| Feature | Description | Type |
|---------|-------------|------|
| temperature_avg | Rolling average temperature | Numeric |
| vibration_std | Vibration standard deviation | Numeric |
| operating_hours | Total hours in operation | Numeric |
| time_since_maintenance | Days since last maintenance | Numeric |
| failure_history | Previous failure count | Numeric |

---

## Stream Analytics Query

```sql
SELECT
    System.Timestamp() as event_time,
    device_id,
    AVG(temperature) as avg_temp,
    STDEV(vibration) as vibration_std,
    MAX(pressure) as max_pressure
INTO
    [output-eventhub]
FROM
    [input-iothub]
TIMESTAMP BY event_time
GROUP BY
    device_id,
    TumblingWindow(minute, 5)
HAVING
    AVG(temperature) > 80 OR STDEV(vibration) > 0.5
```

---

*Next: [Implementation Checklist](./checklist.md)*
