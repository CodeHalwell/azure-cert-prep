variable "resource_group_name" {
  description = "Resource group name"
  type        = string
  default     = "rg-visual-search"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "vissearch"
}

variable "environment" {
  description = "Environment"
  type        = string
  default     = "dev"
}
