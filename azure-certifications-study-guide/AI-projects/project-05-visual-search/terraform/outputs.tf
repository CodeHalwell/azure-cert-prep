output "function_app_url" {
  description = "Function App URL"
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "vision_endpoint" {
  description = "Computer Vision endpoint"
  value       = azurerm_cognitive_account.vision.endpoint
}

output "vision_key" {
  description = "Computer Vision key"
  value       = azurerm_cognitive_account.vision.primary_access_key
  sensitive   = true
}

output "search_endpoint" {
  description = "AI Search endpoint"
  value       = "https://${azurerm_search_service.main.name}.search.windows.net"
}

output "search_key" {
  description = "AI Search key"
  value       = azurerm_search_service.main.primary_key
  sensitive   = true
}

output "storage_connection_string" {
  description = "Storage connection string"
  value       = azurerm_storage_account.main.primary_connection_string
  sensitive   = true
}
