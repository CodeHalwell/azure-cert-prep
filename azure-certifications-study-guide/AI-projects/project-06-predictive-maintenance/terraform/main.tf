terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    Project     = var.project_name
    Environment = var.environment
  }
}

# Storage Account (for ML workspace)
resource "azurerm_storage_account" "ml" {
  name                     = "stml${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = azurerm_resource_group.main.tags
}

# Application Insights
resource "azurerm_application_insights" "ml" {
  name                = "ai-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  application_type    = "web"
  tags                = azurerm_resource_group.main.tags
}

# Key Vault
resource "azurerm_key_vault" "ml" {
  name                = "kv-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"
  tags                = azurerm_resource_group.main.tags
}

data "azurerm_client_config" "current" {}

# Azure Machine Learning Workspace
resource "azurerm_machine_learning_workspace" "main" {
  name                    = "mlw-${var.project_name}-${random_string.suffix.result}"
  resource_group_name     = azurerm_resource_group.main.name
  location                = azurerm_resource_group.main.location
  application_insights_id = azurerm_application_insights.ml.id
  key_vault_id            = azurerm_key_vault.ml.id
  storage_account_id      = azurerm_storage_account.ml.id

  identity {
    type = "SystemAssigned"
  }

  tags = azurerm_resource_group.main.tags
}

# IoT Hub
resource "azurerm_iothub" "main" {
  name                = "iot-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location

  sku {
    name     = "S1"
    capacity = 1
  }

  tags = azurerm_resource_group.main.tags
}

# Event Hub Namespace
resource "azurerm_eventhub_namespace" "main" {
  name                = "evhns-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "Standard"
  capacity            = 1
  tags                = azurerm_resource_group.main.tags
}

resource "azurerm_eventhub" "telemetry" {
  name                = "telemetry"
  namespace_name      = azurerm_eventhub_namespace.main.name
  resource_group_name = azurerm_resource_group.main.name
  partition_count     = 2
  message_retention   = 1
}

# Stream Analytics Job
resource "azurerm_stream_analytics_job" "main" {
  name                = "asa-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  streaming_units     = 3

  transformation_query = <<QUERY
SELECT
    System.Timestamp() as event_time,
    device_id,
    AVG(temperature) as avg_temp,
    STDEV(vibration) as vibration_std,
    MAX(pressure) as max_pressure
INTO
    [output]
FROM
    [input]
TIMESTAMP BY timestamp
GROUP BY
    device_id,
    TumblingWindow(minute, 5)
QUERY

  tags = azurerm_resource_group.main.tags
}
