output "function_app_url" {
  description = "Function App URL"
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "language_endpoint" {
  description = "Language Service endpoint"
  value       = azurerm_cognitive_account.language.endpoint
}

output "language_key" {
  description = "Language Service key"
  value       = azurerm_cognitive_account.language.primary_access_key
  sensitive   = true
}

output "cosmos_endpoint" {
  description = "Cosmos DB endpoint"
  value       = azurerm_cosmosdb_account.main.endpoint
}
