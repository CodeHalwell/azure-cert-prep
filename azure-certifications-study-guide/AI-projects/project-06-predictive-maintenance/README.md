# Project 06: Predictive Maintenance Solution

![Azure](https://img.shields.io/badge/Azure-Machine%20Learning-0078D4?style=flat-square)
![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-8--10%20hours-red?style=flat-square)

## 🎯 Project Overview

Build a predictive maintenance solution that uses IoT sensor data and machine learning to predict equipment failures before they occur.

### What You'll Build

- IoT data ingestion pipeline
- Real-time streaming analytics
- ML model for failure prediction
- Alert and notification system
- Maintenance dashboard

### Skills You'll Learn

- Azure Machine Learning
- Azure IoT Hub
- Azure Stream Analytics
- Time series analysis
- MLOps practices

---

## 📦 Azure Resources Required

| Resource | SKU/Tier | Purpose |
|----------|----------|---------|
| Azure Machine Learning | Basic | Model training and deployment |
| Azure IoT Hub | S1 | Device connectivity |
| Azure Stream Analytics | Standard | Real-time processing |
| Azure Event Hubs | Standard | Event streaming |
| Azure SQL Database | Basic | Historical data |
| Azure Functions | Consumption | Alerting logic |

### Estimated Monthly Cost

- **Development/Testing**: $80-150/month
- **Production (low volume)**: $200-400/month

---

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "IoT Devices"
        A[Sensors]
        B[Equipment]
        C[Controllers]
    end
    
    subgraph "Ingestion"
        D[IoT Hub]
        E[Event Hubs]
    end
    
    subgraph "Processing"
        F[Stream Analytics]
        G[Real-time Scoring]
    end
    
    subgraph "Machine Learning"
        H[Azure ML Workspace]
        I[Training Pipeline]
        J[Model Registry]
        K[Managed Endpoint]
    end
    
    subgraph "Storage"
        L[(SQL Database)]
        M[(Blob Storage)]
    end
    
    subgraph "Actions"
        N[Azure Functions]
        O[Alerts]
        P[Dashboard]
    end
    
    A & B & C --> D --> E --> F
    F --> G --> K
    K --> N --> O
    F --> L
    H --> I --> J --> K
    L --> P
    
    style H fill:#e8f5e9
    style F fill:#fff3e0
```

---

## 📁 Project Structure

```
project-06-predictive-maintenance/
├── README.md
├── setup.md
├── architecture.md
├── checklist.md
├── src/
│   ├── data_generator/
│   │   └── simulate_sensors.py
│   ├── ml/
│   │   ├── train.py
│   │   ├── score.py
│   │   └── register_model.py
│   ├── streaming/
│   │   └── stream_analytics_query.sql
│   ├── functions/
│   │   └── alert_handler.py
│   └── requirements.txt
└── terraform/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── terraform.tfvars.example
```

---

## 🚀 Quick Start

### 1. Deploy Infrastructure

```bash
cd terraform
terraform init && terraform apply
```

### 2. Train the Model

```bash
cd ../src/ml
python train.py --data-path ./sample_data
python register_model.py
```

### 3. Start Simulation

```bash
python data_generator/simulate_sensors.py
```

---

## 🔗 Related Resources

- [Azure Machine Learning Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)
- [Azure IoT Hub Documentation](https://learn.microsoft.com/en-us/azure/iot-hub/)
- [Azure Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/)

---

*Last updated: November 2025*
