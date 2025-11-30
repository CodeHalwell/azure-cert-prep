output "bot_endpoint" {
  description = "Bot messaging endpoint"
  value       = "https://${azurerm_linux_web_app.bot.default_hostname}/api/messages"
}

output "openai_endpoint" {
  description = "Azure OpenAI endpoint"
  value       = azurerm_cognitive_account.openai.endpoint
}

output "cosmos_endpoint" {
  description = "Cosmos DB endpoint"
  value       = azurerm_cosmosdb_account.main.endpoint
}

output "key_vault_url" {
  description = "Key Vault URL"
  value       = azurerm_key_vault.main.vault_uri
}

output "app_service_url" {
  description = "App Service URL"
  value       = "https://${azurerm_linux_web_app.bot.default_hostname}"
}
