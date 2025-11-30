output "function_app_url" {
  description = "Function App URL"
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "content_safety_endpoint" {
  description = "Content Safety endpoint"
  value       = azurerm_cognitive_account.content_safety.endpoint
}

output "content_safety_key" {
  description = "Content Safety key"
  value       = azurerm_cognitive_account.content_safety.primary_access_key
  sensitive   = true
}

output "cosmos_endpoint" {
  description = "Cosmos DB endpoint"
  value       = azurerm_cosmosdb_account.main.endpoint
}
