variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-customer-bot"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "eastus"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "csbot"
}

variable "environment" {
  description = "Environment"
  type        = string
  default     = "dev"
}

variable "app_service_sku" {
  description = "App Service SKU"
  type        = string
  default     = "B1"
}

variable "openai_location" {
  description = "Azure OpenAI location"
  type        = string
  default     = "eastus"
}

variable "bot_app_id" {
  description = "Bot Application ID from Azure AD"
  type        = string
}
