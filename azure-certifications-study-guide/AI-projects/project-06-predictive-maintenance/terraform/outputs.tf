output "ml_workspace_name" {
  description = "ML Workspace name"
  value       = azurerm_machine_learning_workspace.main.name
}

output "iot_hub_hostname" {
  description = "IoT Hub hostname"
  value       = azurerm_iothub.main.hostname
}

output "eventhub_namespace" {
  description = "Event Hub namespace"
  value       = azurerm_eventhub_namespace.main.name
}

output "stream_analytics_job" {
  description = "Stream Analytics job name"
  value       = azurerm_stream_analytics_job.main.name
}
