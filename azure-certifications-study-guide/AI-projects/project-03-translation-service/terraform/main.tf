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

# Storage Account for Function App
resource "azurerm_storage_account" "functions" {
  name                     = "st${var.project_name}${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  tags                     = azurerm_resource_group.main.tags
}

# App Service Plan (Consumption)
resource "azurerm_service_plan" "functions" {
  name                = "asp-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  os_type             = "Linux"
  sku_name            = "Y1"
  tags                = azurerm_resource_group.main.tags
}

# Azure Translator
resource "azurerm_cognitive_account" "translator" {
  name                = "translator-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = "global"
  kind                = "TextTranslation"
  sku_name            = "S1"

  tags = azurerm_resource_group.main.tags
}

# Azure Speech Service
resource "azurerm_cognitive_account" "speech" {
  name                = "speech-${var.project_name}-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  kind                = "SpeechServices"
  sku_name            = "S0"

  tags = azurerm_resource_group.main.tags
}

# Function App
resource "azurerm_linux_function_app" "main" {
  name                       = "func-${var.project_name}-${random_string.suffix.result}"
  resource_group_name        = azurerm_resource_group.main.name
  location                   = azurerm_resource_group.main.location
  service_plan_id            = azurerm_service_plan.functions.id
  storage_account_name       = azurerm_storage_account.functions.name
  storage_account_access_key = azurerm_storage_account.functions.primary_access_key

  site_config {
    application_stack {
      python_version = "3.11"
    }
  }

  app_settings = {
    "AZURE_TRANSLATOR_KEY"      = azurerm_cognitive_account.translator.primary_access_key
    "AZURE_TRANSLATOR_ENDPOINT" = azurerm_cognitive_account.translator.endpoint
    "AZURE_TRANSLATOR_REGION"   = azurerm_resource_group.main.location
    "AZURE_SPEECH_KEY"          = azurerm_cognitive_account.speech.primary_access_key
    "AZURE_SPEECH_REGION"       = azurerm_resource_group.main.location
  }

  tags = azurerm_resource_group.main.tags
}
