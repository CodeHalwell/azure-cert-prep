# Output values for application configuration

output "resource_group_name" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.main.name
}

output "document_intelligence_endpoint" {
  description = "Azure Document Intelligence endpoint"
  value       = azurerm_cognitive_account.document_intelligence.endpoint
}

output "document_intelligence_key" {
  description = "Azure Document Intelligence primary key"
  value       = azurerm_cognitive_account.document_intelligence.primary_access_key
  sensitive   = true
}

output "openai_endpoint" {
  description = "Azure OpenAI endpoint"
  value       = azurerm_cognitive_account.openai.endpoint
}

output "openai_key" {
  description = "Azure OpenAI primary key"
  value       = azurerm_cognitive_account.openai.primary_access_key
  sensitive   = true
}

output "openai_deployment_name" {
  description = "Azure OpenAI model deployment name"
  value       = azurerm_cognitive_deployment.gpt4o.name
}

output "storage_account_name" {
  description = "Storage account name"
  value       = azurerm_storage_account.documents.name
}

output "storage_connection_string" {
  description = "Storage account connection string"
  value       = azurerm_storage_account.documents.primary_connection_string
  sensitive   = true
}

output "storage_container_name" {
  description = "Storage container name for documents"
  value       = azurerm_storage_container.documents.name
}

output "key_vault_url" {
  description = "Key Vault URL"
  value       = azurerm_key_vault.main.vault_uri
}

output "key_vault_name" {
  description = "Key Vault name"
  value       = azurerm_key_vault.main.name
}
