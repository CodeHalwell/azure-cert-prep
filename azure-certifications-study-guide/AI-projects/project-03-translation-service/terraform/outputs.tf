output "function_app_url" {
  description = "Function App URL"
  value       = "https://${azurerm_linux_function_app.main.default_hostname}"
}

output "translator_endpoint" {
  description = "Translator endpoint"
  value       = azurerm_cognitive_account.translator.endpoint
}

output "translator_key" {
  description = "Translator key"
  value       = azurerm_cognitive_account.translator.primary_access_key
  sensitive   = true
}

output "speech_key" {
  description = "Speech service key"
  value       = azurerm_cognitive_account.speech.primary_access_key
  sensitive   = true
}

output "speech_region" {
  description = "Speech service region"
  value       = azurerm_resource_group.main.location
}
