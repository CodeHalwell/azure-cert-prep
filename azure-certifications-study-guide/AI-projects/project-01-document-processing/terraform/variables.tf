# Required variables
variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-document-processing"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "eastus"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "docproc"

  validation {
    condition     = length(var.project_name) <= 10
    error_message = "Project name must be 10 characters or less."
  }
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

# Optional variables with defaults
variable "document_intelligence_sku" {
  description = "SKU for Azure Document Intelligence"
  type        = string
  default     = "S0"
}

variable "openai_sku" {
  description = "SKU for Azure OpenAI"
  type        = string
  default     = "S0"
}

variable "openai_location" {
  description = "Azure region for OpenAI (limited availability)"
  type        = string
  default     = "eastus"
}

variable "openai_capacity" {
  description = "Capacity units for OpenAI deployment"
  type        = number
  default     = 10
}
