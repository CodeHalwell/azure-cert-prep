output "search_endpoint" { value = "https://${azurerm_search_service.main.name}.search.windows.net" }
output "openai_endpoint" { value = azurerm_cognitive_account.openai.endpoint }
output "storage_connection" { value = azurerm_storage_account.main.primary_connection_string; sensitive = true }
