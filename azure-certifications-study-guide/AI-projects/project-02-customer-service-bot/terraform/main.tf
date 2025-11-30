# Terraform configuration for Customer Service Bot

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

data "azurerm_client_config" "current" {}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
  tags = {
    Project     = var.project_name
    Environment = var.environment
  }
}

# App Service Plan
resource "azurerm_service_plan" "bot" {
  name                = "asp-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = var.app_service_sku
  tags                = azurerm_resource_group.main.tags
}

# App Service for Bot
resource "azurerm_linux_web_app" "bot" {
  name                = "bot-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  service_plan_id     = azurerm_service_plan.bot.id

  site_config {
    application_stack {
      python_version = "3.11"
    }
  }

  app_settings = {
    "BOT_APP_ID"             = azurerm_bot_channels_registration.bot.microsoft_app_id
    "AZURE_OPENAI_ENDPOINT"  = azurerm_cognitive_account.openai.endpoint
    "COSMOS_ENDPOINT"        = azurerm_cosmosdb_account.main.endpoint
    "COSMOS_DATABASE"        = azurerm_cosmosdb_sql_database.bot.name
  }

  tags = azurerm_resource_group.main.tags
}

# Azure OpenAI
resource "azurerm_cognitive_account" "openai" {
  name                = "openai-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = var.openai_location
  kind                = "OpenAI"
  sku_name            = "S0"

  custom_subdomain_name = "openai-${var.project_name}-${random_string.suffix.result}"
  tags                  = azurerm_resource_group.main.tags
}

resource "azurerm_cognitive_deployment" "gpt4o" {
  name                 = "gpt-4o"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  model {
    format  = "OpenAI"
    name    = "gpt-4o"
    version = "2024-05-13"
  }
  scale {
    type     = "Standard"
    capacity = 10
  }
}

# Cosmos DB
resource "azurerm_cosmosdb_account" "main" {
  name                = "cosmos-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = azurerm_resource_group.main.location
    failover_priority = 0
  }

  tags = azurerm_resource_group.main.tags
}

resource "azurerm_cosmosdb_sql_database" "bot" {
  name                = "botdb"
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}

# Bot Channels Registration
resource "azurerm_bot_channels_registration" "bot" {
  name                = "bot-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = "global"
  sku                 = "S1"
  microsoft_app_id    = var.bot_app_id

  endpoint = "https://${azurerm_linux_web_app.bot.default_hostname}/api/messages"

  tags = azurerm_resource_group.main.tags
}

# Key Vault
resource "azurerm_key_vault" "main" {
  name                       = "kv-${var.project_name}-${random_string.suffix.result}"
  resource_group_name        = azurerm_resource_group.main.name
  location                   = azurerm_resource_group.main.location
  tenant_id                  = data.azurerm_client_config.current.tenant_id
  sku_name                   = "standard"
  soft_delete_retention_days = 7

  access_policy {
    tenant_id = data.azurerm_client_config.current.tenant_id
    object_id = data.azurerm_client_config.current.object_id
    secret_permissions = ["Get", "List", "Set", "Delete", "Purge"]
  }

  tags = azurerm_resource_group.main.tags
}
