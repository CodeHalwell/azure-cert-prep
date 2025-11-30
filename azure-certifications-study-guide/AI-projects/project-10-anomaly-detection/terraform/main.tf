terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 3.0" }
    random  = { source = "hashicorp/random", version = "~> 3.0" }
  }
}

provider "azurerm" { features {} }

resource "random_string" "suffix" { length = 6; special = false; upper = false }

resource "azurerm_resource_group" "main" {
  name     = "rg-anomaly-detection"
  location = "eastus"
}

# Anomaly Detector
resource "azurerm_cognitive_account" "anomaly" {
  name                = "anomaly-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  kind                = "AnomalyDetector"
  sku_name            = "S0"
}

# Event Hub Namespace
resource "azurerm_eventhub_namespace" "main" {
  name                = "evhns-anomaly-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Standard"
  capacity            = 1
}

resource "azurerm_eventhub" "telemetry" {
  name                = "telemetry"
  namespace_name      = azurerm_eventhub_namespace.main.name
  resource_group_name = azurerm_resource_group.main.name
  partition_count     = 2
  message_retention   = 1
}

# Stream Analytics
resource "azurerm_stream_analytics_job" "main" {
  name                = "asa-anomaly-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  streaming_units     = 3
  
  transformation_query = <<QUERY
SELECT
    System.Timestamp() as event_time,
    device_id,
    AVG(value) as avg_value,
    MIN(value) as min_value,
    MAX(value) as max_value
INTO [output]
FROM [input]
TIMESTAMP BY timestamp
GROUP BY device_id, TumblingWindow(minute, 1)
QUERY
}

output "anomaly_detector_endpoint" { value = azurerm_cognitive_account.anomaly.endpoint }
output "eventhub_connection" { value = azurerm_eventhub_namespace.main.default_primary_connection_string; sensitive = true }
