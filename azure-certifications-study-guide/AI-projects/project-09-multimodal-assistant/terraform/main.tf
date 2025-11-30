terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 3.0" }
    random  = { source = "hashicorp/random", version = "~> 3.0" }
  }
}

provider "azurerm" { features {} }

resource "random_string" "suffix" { length = 6; special = false; upper = false }

resource "azurerm_resource_group" "main" {
  name     = "rg-multimodal-assistant"
  location = "eastus"
}

resource "azurerm_cognitive_account" "openai" {
  name                  = "openai-multimodal-${random_string.suffix.result}"
  resource_group_name   = azurerm_resource_group.main.name
  location              = azurerm_resource_group.main.location
  kind                  = "OpenAI"
  sku_name              = "S0"
  custom_subdomain_name = "openai-multimodal-${random_string.suffix.result}"
}

resource "azurerm_cognitive_deployment" "gpt4o" {
  name                 = "gpt-4o"
  cognitive_account_id = azurerm_cognitive_account.openai.id
  model { format = "OpenAI"; name = "gpt-4o"; version = "2024-05-13" }
  scale { type = "Standard"; capacity = 10 }
}

resource "azurerm_cognitive_account" "speech" {
  name                = "speech-multimodal-${random_string.suffix.result}"
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  kind                = "SpeechServices"
  sku_name            = "S0"
}
