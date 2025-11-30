# 🔧 Azure CLI Cheat Sheet

![Azure CLI](https://img.shields.io/badge/Azure%20CLI-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
![Last Updated](https://img.shields.io/badge/Last%20Updated-November%202025-green?style=for-the-badge)

A comprehensive quick reference guide for Azure Command-Line Interface (CLI) commands. Essential for all Azure certifications including AZ-104, AZ-204, AZ-305, and AZ-500.

---

## 📋 Table of Contents

- [Installation \& Configuration](#installation--configuration)
- [Authentication \& Account Management](#authentication--account-management)
- [Resource Groups](#resource-groups)
- [Virtual Machines](#virtual-machines)
- [Networking](#networking)
- [Storage](#storage)
- [Azure Active Directory (Entra ID)](#azure-active-directory-entra-id)
- [Azure Kubernetes Service (AKS)](#azure-kubernetes-service-aks)
- [Azure App Service](#azure-app-service)
- [Azure Functions](#azure-functions)
- [Azure SQL Database](#azure-sql-database)
- [Azure Cosmos DB](#azure-cosmos-db)
- [Azure Key Vault](#azure-key-vault)
- [Azure Monitor \& Logging](#azure-monitor--logging)
- [Azure Container Instances](#azure-container-instances)
- [Azure Container Registry](#azure-container-registry)
- [Azure Cognitive Services](#azure-cognitive-services)
- [ARM Templates \& Bicep](#arm-templates--bicep)
- [Tips \& Best Practices](#tips--best-practices)

---

## Installation & Configuration

### Install Azure CLI

```bash
# Windows (PowerShell)
winget install -e --id Microsoft.AzureCLI

# macOS
brew install azure-cli

# Linux (Ubuntu/Debian)
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Linux (RHEL/CentOS)
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo dnf install azure-cli
```

### Check Version & Update

```bash
# Check current version
az version

# Update Azure CLI
az upgrade

# Check for extension updates
az extension list-available --output table
```

### Configure Defaults

```bash
# Set default output format
az configure --defaults output=table

# Set default location
az configure --defaults location=eastus

# Set default resource group
az configure --defaults group=myResourceGroup

# View current configuration
az configure --list-defaults
```

---

## Authentication & Account Management

### Login & Logout

```bash
# Interactive login (opens browser)
az login

# Login with device code (for remote sessions)
az login --use-device-code

# Login with service principal
az login --service-principal -u <app-id> -p <password> --tenant <tenant-id>

# Login with managed identity (from Azure VM)
az login --identity

# Logout
az logout
```

### Account & Subscription Management

```bash
# List all subscriptions
az account list --output table

# Show current subscription
az account show

# Set active subscription
az account set --subscription "<subscription-name-or-id>"

# Get access token
az account get-access-token

# List account locations
az account list-locations --output table
```

---

## Resource Groups

```bash
# Create resource group
az group create --name myResourceGroup --location eastus

# List all resource groups
az group list --output table

# Show resource group details
az group show --name myResourceGroup

# Delete resource group (with confirmation)
az group delete --name myResourceGroup --yes --no-wait

# List resources in a resource group
az resource list --resource-group myResourceGroup --output table

# Export resource group as ARM template
az group export --name myResourceGroup > template.json

# Lock a resource group
az lock create --name LockGroup --lock-type CanNotDelete --resource-group myResourceGroup
```

---

## Virtual Machines

### Create & Manage VMs

```bash
# Create a Linux VM (Ubuntu)
az vm create \
  --resource-group myResourceGroup \
  --name myVM \
  --image Ubuntu2204 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B2s

# Create a Windows VM
az vm create \
  --resource-group myResourceGroup \
  --name myWindowsVM \
  --image Win2022Datacenter \
  --admin-username azureuser \
  --admin-password "ComplexPassword123!" \
  --size Standard_B2s

# List VMs in resource group
az vm list --resource-group myResourceGroup --output table

# Show VM details
az vm show --resource-group myResourceGroup --name myVM

# Get VM IP addresses
az vm list-ip-addresses --resource-group myResourceGroup --name myVM --output table
```

### VM Power Operations

```bash
# Start VM
az vm start --resource-group myResourceGroup --name myVM

# Stop VM (still incurs compute charges)
az vm stop --resource-group myResourceGroup --name myVM

# Deallocate VM (no compute charges)
az vm deallocate --resource-group myResourceGroup --name myVM

# Restart VM
az vm restart --resource-group myResourceGroup --name myVM

# Delete VM
az vm delete --resource-group myResourceGroup --name myVM --yes
```

### VM Disk & Images

```bash
# List available VM images
az vm image list --output table

# List VM sizes in a location
az vm list-sizes --location eastus --output table

# Create VM image from VM
az image create \
  --resource-group myResourceGroup \
  --name myImage \
  --source myVM

# Attach data disk to VM
az vm disk attach \
  --resource-group myResourceGroup \
  --vm-name myVM \
  --name myDataDisk \
  --size-gb 128 \
  --sku Premium_LRS \
  --new
```

---

## Networking

### Virtual Networks

```bash
# Create virtual network
az network vnet create \
  --resource-group myResourceGroup \
  --name myVNet \
  --address-prefix 10.0.0.0/16 \
  --subnet-name mySubnet \
  --subnet-prefix 10.0.1.0/24

# List virtual networks
az network vnet list --resource-group myResourceGroup --output table

# Create additional subnet
az network vnet subnet create \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name mySubnet2 \
  --address-prefix 10.0.2.0/24

# Show subnet details
az network vnet subnet show \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name mySubnet
```

### Network Security Groups (NSG)

```bash
# Create NSG
az network nsg create \
  --resource-group myResourceGroup \
  --name myNSG

# Create NSG rule (allow SSH)
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name myNSG \
  --name AllowSSH \
  --priority 1000 \
  --destination-port-ranges 22 \
  --access Allow \
  --protocol Tcp

# Create NSG rule (allow HTTP/HTTPS)
az network nsg rule create \
  --resource-group myResourceGroup \
  --nsg-name myNSG \
  --name AllowHTTP \
  --priority 1001 \
  --destination-port-ranges 80 443 \
  --access Allow \
  --protocol Tcp

# List NSG rules
az network nsg rule list --resource-group myResourceGroup --nsg-name myNSG --output table

# Associate NSG with subnet
az network vnet subnet update \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --name mySubnet \
  --network-security-group myNSG
```

### Public IP & Load Balancer

```bash
# Create public IP address
az network public-ip create \
  --resource-group myResourceGroup \
  --name myPublicIP \
  --sku Standard \
  --allocation-method Static

# Create load balancer
az network lb create \
  --resource-group myResourceGroup \
  --name myLoadBalancer \
  --sku Standard \
  --frontend-ip-name myFrontEnd \
  --backend-pool-name myBackEndPool \
  --public-ip-address myPublicIP

# Create load balancer health probe
az network lb probe create \
  --resource-group myResourceGroup \
  --lb-name myLoadBalancer \
  --name myHealthProbe \
  --protocol tcp \
  --port 80

# Create load balancer rule
az network lb rule create \
  --resource-group myResourceGroup \
  --lb-name myLoadBalancer \
  --name myLBRule \
  --protocol tcp \
  --frontend-port 80 \
  --backend-port 80 \
  --frontend-ip-name myFrontEnd \
  --backend-pool-name myBackEndPool \
  --probe-name myHealthProbe
```

### VNet Peering

```bash
# Create VNet peering
az network vnet peering create \
  --resource-group myResourceGroup \
  --name VNet1-to-VNet2 \
  --vnet-name VNet1 \
  --remote-vnet VNet2 \
  --allow-vnet-access

# List VNet peerings
az network vnet peering list \
  --resource-group myResourceGroup \
  --vnet-name myVNet \
  --output table
```

---

## Storage

### Storage Accounts

```bash
# Create storage account
az storage account create \
  --name mystorageaccount123 \
  --resource-group myResourceGroup \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2

# List storage accounts
az storage account list --resource-group myResourceGroup --output table

# Get storage account keys
az storage account keys list \
  --resource-group myResourceGroup \
  --account-name mystorageaccount123

# Get connection string
az storage account show-connection-string \
  --resource-group myResourceGroup \
  --name mystorageaccount123
```

### Blob Storage

```bash
# Create container
az storage container create \
  --name mycontainer \
  --account-name mystorageaccount123 \
  --auth-mode login

# Upload blob
az storage blob upload \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --name myblob.txt \
  --file /path/to/local/file.txt \
  --auth-mode login

# List blobs
az storage blob list \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --output table \
  --auth-mode login

# Download blob
az storage blob download \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --name myblob.txt \
  --file /path/to/download/file.txt \
  --auth-mode login

# Generate SAS token for blob
az storage blob generate-sas \
  --account-name mystorageaccount123 \
  --container-name mycontainer \
  --name myblob.txt \
  --permissions r \
  --expiry 2025-12-31T23:59:00Z \
  --auth-mode login
```

### File Shares

```bash
# Create file share
az storage share create \
  --name myfileshare \
  --account-name mystorageaccount123 \
  --quota 5

# Upload file to share
az storage file upload \
  --share-name myfileshare \
  --source /path/to/local/file.txt \
  --account-name mystorageaccount123

# List files in share
az storage file list \
  --share-name myfileshare \
  --account-name mystorageaccount123 \
  --output table
```

---

## Azure Active Directory (Entra ID)

### Users

```bash
# List all users
az ad user list --output table

# Create user
az ad user create \
  --display-name "John Doe" \
  --user-principal-name john.doe@contoso.onmicrosoft.com \
  --password "ComplexPassword123!"

# Show user details
az ad user show --id john.doe@contoso.onmicrosoft.com

# Delete user
az ad user delete --id john.doe@contoso.onmicrosoft.com
```

### Groups

```bash
# Create group
az ad group create \
  --display-name "Development Team" \
  --mail-nickname "dev-team"

# List groups
az ad group list --output table

# Add member to group
az ad group member add \
  --group "Development Team" \
  --member-id <user-object-id>

# List group members
az ad group member list --group "Development Team" --output table
```

### Service Principals & App Registrations

```bash
# Create service principal
az ad sp create-for-rbac \
  --name myServicePrincipal \
  --role Contributor \
  --scopes /subscriptions/<subscription-id>

# List service principals
az ad sp list --show-mine --output table

# Reset service principal credentials
az ad sp credential reset --name myServicePrincipal

# Assign role to service principal
az role assignment create \
  --assignee <app-id> \
  --role Reader \
  --scope /subscriptions/<subscription-id>/resourceGroups/myResourceGroup
```

---

## Azure Kubernetes Service (AKS)

### Cluster Management

```bash
# Create AKS cluster
az aks create \
  --resource-group myResourceGroup \
  --name myAKSCluster \
  --node-count 3 \
  --node-vm-size Standard_B2s \
  --generate-ssh-keys \
  --enable-managed-identity

# List AKS clusters
az aks list --output table

# Get cluster credentials (configure kubectl)
az aks get-credentials \
  --resource-group myResourceGroup \
  --name myAKSCluster

# Show cluster details
az aks show --resource-group myResourceGroup --name myAKSCluster

# Delete cluster
az aks delete --resource-group myResourceGroup --name myAKSCluster --yes --no-wait
```

### Node Pool Management

```bash
# Add node pool
az aks nodepool add \
  --resource-group myResourceGroup \
  --cluster-name myAKSCluster \
  --name mynodepool \
  --node-count 2 \
  --node-vm-size Standard_DS3_v2

# Scale node pool
az aks nodepool scale \
  --resource-group myResourceGroup \
  --cluster-name myAKSCluster \
  --name mynodepool \
  --node-count 5

# List node pools
az aks nodepool list --resource-group myResourceGroup --cluster-name myAKSCluster --output table
```

### Cluster Operations

```bash
# Start cluster (after stop)
az aks start --resource-group myResourceGroup --name myAKSCluster

# Stop cluster
az aks stop --resource-group myResourceGroup --name myAKSCluster

# Upgrade cluster
az aks upgrade \
  --resource-group myResourceGroup \
  --name myAKSCluster \
  --kubernetes-version 1.28.0

# Get available Kubernetes versions
az aks get-versions --location eastus --output table
```

---

## Azure App Service

### Web Apps

```bash
# Create App Service plan
az appservice plan create \
  --name myAppServicePlan \
  --resource-group myResourceGroup \
  --sku B1 \
  --is-linux

# Create web app
az webapp create \
  --resource-group myResourceGroup \
  --plan myAppServicePlan \
  --name myWebApp123 \
  --runtime "PYTHON:3.11"

# List web apps
az webapp list --resource-group myResourceGroup --output table

# Get web app URL
az webapp show --resource-group myResourceGroup --name myWebApp123 --query defaultHostName -o tsv

# Deploy code from Git
az webapp deployment source config \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --repo-url https://github.com/user/repo \
  --branch main \
  --manual-integration
```

### App Configuration

```bash
# Set app settings
az webapp config appsettings set \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --settings KEY1=VALUE1 KEY2=VALUE2

# List app settings
az webapp config appsettings list \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --output table

# Set connection string
az webapp config connection-string set \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --settings MyDbConnection="Server=..." \
  --connection-string-type SQLAzure

# Enable logging
az webapp log config \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --docker-container-logging filesystem

# View logs
az webapp log tail \
  --resource-group myResourceGroup \
  --name myWebApp123
```

### Deployment Slots

```bash
# Create deployment slot
az webapp deployment slot create \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --slot staging

# Swap slots
az webapp deployment slot swap \
  --resource-group myResourceGroup \
  --name myWebApp123 \
  --slot staging \
  --target-slot production
```

---

## Azure Functions

```bash
# Create function app
az functionapp create \
  --resource-group myResourceGroup \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.11 \
  --functions-version 4 \
  --name myFunctionApp123 \
  --storage-account mystorageaccount123

# List function apps
az functionapp list --resource-group myResourceGroup --output table

# Deploy function app
az functionapp deployment source config-zip \
  --resource-group myResourceGroup \
  --name myFunctionApp123 \
  --src function.zip

# Set function app settings
az functionapp config appsettings set \
  --resource-group myResourceGroup \
  --name myFunctionApp123 \
  --settings "AzureWebJobsStorage=..." "FUNCTIONS_WORKER_RUNTIME=python"

# Get function URL
az functionapp function show \
  --resource-group myResourceGroup \
  --name myFunctionApp123 \
  --function-name MyFunction \
  --query invokeUrlTemplate
```

---

## Azure SQL Database

```bash
# Create SQL server
az sql server create \
  --name mySqlServer123 \
  --resource-group myResourceGroup \
  --location eastus \
  --admin-user sqladmin \
  --admin-password "ComplexPassword123!"

# Create SQL database
az sql db create \
  --resource-group myResourceGroup \
  --server mySqlServer123 \
  --name myDatabase \
  --service-objective S0

# List databases
az sql db list --resource-group myResourceGroup --server mySqlServer123 --output table

# Create firewall rule (allow Azure services)
az sql server firewall-rule create \
  --resource-group myResourceGroup \
  --server mySqlServer123 \
  --name AllowAzureServices \
  --start-ip-address 0.0.0.0 \
  --end-ip-address 0.0.0.0

# Create firewall rule (allow specific IP)
az sql server firewall-rule create \
  --resource-group myResourceGroup \
  --server mySqlServer123 \
  --name AllowMyIP \
  --start-ip-address <your-ip> \
  --end-ip-address <your-ip>

# Get connection string
az sql db show-connection-string \
  --server mySqlServer123 \
  --name myDatabase \
  --client ado.net
```

---

## Azure Cosmos DB

```bash
# Create Cosmos DB account
az cosmosdb create \
  --name myCosmosAccount123 \
  --resource-group myResourceGroup \
  --kind GlobalDocumentDB \
  --default-consistency-level Session

# Create database
az cosmosdb sql database create \
  --account-name myCosmosAccount123 \
  --resource-group myResourceGroup \
  --name myDatabase

# Create container
az cosmosdb sql container create \
  --account-name myCosmosAccount123 \
  --resource-group myResourceGroup \
  --database-name myDatabase \
  --name myContainer \
  --partition-key-path "/partitionKey" \
  --throughput 400

# Get connection keys
az cosmosdb keys list \
  --name myCosmosAccount123 \
  --resource-group myResourceGroup

# Get connection string
az cosmosdb keys list \
  --name myCosmosAccount123 \
  --resource-group myResourceGroup \
  --type connection-strings
```

---

## Azure Key Vault

```bash
# Create Key Vault
az keyvault create \
  --name myKeyVault123 \
  --resource-group myResourceGroup \
  --location eastus

# Set secret
az keyvault secret set \
  --vault-name myKeyVault123 \
  --name mySecret \
  --value "SuperSecretValue123"

# Get secret
az keyvault secret show \
  --vault-name myKeyVault123 \
  --name mySecret

# List secrets
az keyvault secret list --vault-name myKeyVault123 --output table

# Delete secret
az keyvault secret delete --vault-name myKeyVault123 --name mySecret

# Create key
az keyvault key create \
  --vault-name myKeyVault123 \
  --name myKey \
  --kty RSA \
  --size 2048

# Set access policy
az keyvault set-policy \
  --name myKeyVault123 \
  --upn user@contoso.com \
  --secret-permissions get list set delete \
  --key-permissions get list create delete

# Enable soft delete recovery
az keyvault recover --name myKeyVault123
```

---

## Azure Monitor & Logging

```bash
# Create Log Analytics workspace
az monitor log-analytics workspace create \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace

# Get workspace ID and key
az monitor log-analytics workspace show \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace \
  --query customerId -o tsv

az monitor log-analytics workspace get-shared-keys \
  --resource-group myResourceGroup \
  --workspace-name myWorkspace

# Create metric alert
az monitor metrics alert create \
  --name myMetricAlert \
  --resource-group myResourceGroup \
  --scopes /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Compute/virtualMachines/<vm-name> \
  --condition "avg Percentage CPU > 80" \
  --description "High CPU Alert"

# Create action group
az monitor action-group create \
  --resource-group myResourceGroup \
  --name myActionGroup \
  --short-name myAG \
  --email-receiver name=admin email=admin@contoso.com

# View activity log
az monitor activity-log list \
  --resource-group myResourceGroup \
  --start-time 2025-01-01 \
  --output table
```

---

## Azure Container Instances

```bash
# Create container instance
az container create \
  --resource-group myResourceGroup \
  --name mycontainer \
  --image mcr.microsoft.com/azuredocs/aci-helloworld \
  --dns-name-label mycontainerdns \
  --ports 80

# Show container details
az container show \
  --resource-group myResourceGroup \
  --name mycontainer \
  --query "{FQDN:ipAddress.fqdn,Status:instanceView.state}" \
  --output table

# View container logs
az container logs \
  --resource-group myResourceGroup \
  --name mycontainer

# Execute command in container
az container exec \
  --resource-group myResourceGroup \
  --name mycontainer \
  --exec-command /bin/bash

# Stop container
az container stop --resource-group myResourceGroup --name mycontainer

# Delete container
az container delete --resource-group myResourceGroup --name mycontainer --yes
```

---

## Azure Container Registry

```bash
# Create container registry
az acr create \
  --resource-group myResourceGroup \
  --name myRegistry123 \
  --sku Basic

# Login to registry
az acr login --name myRegistry123

# Build and push image
az acr build \
  --registry myRegistry123 \
  --image myapp:v1 \
  .

# List repositories
az acr repository list --name myRegistry123 --output table

# List tags
az acr repository show-tags --name myRegistry123 --repository myapp --output table

# Get registry credentials
az acr credential show --name myRegistry123

# Enable admin user
az acr update --name myRegistry123 --admin-enabled true
```

---

## Azure Cognitive Services

```bash
# Create Cognitive Services account
az cognitiveservices account create \
  --name myCogServices \
  --resource-group myResourceGroup \
  --kind CognitiveServices \
  --sku S0 \
  --location eastus

# Create OpenAI resource
az cognitiveservices account create \
  --name myOpenAI \
  --resource-group myResourceGroup \
  --kind OpenAI \
  --sku S0 \
  --location eastus

# Get keys
az cognitiveservices account keys list \
  --name myCogServices \
  --resource-group myResourceGroup

# List deployments (OpenAI)
az cognitiveservices account deployment list \
  --name myOpenAI \
  --resource-group myResourceGroup

# Create deployment (OpenAI)
az cognitiveservices account deployment create \
  --name myOpenAI \
  --resource-group myResourceGroup \
  --deployment-name gpt-4-deployment \
  --model-name gpt-4 \
  --model-version "0613" \
  --model-format OpenAI \
  --sku-capacity 10 \
  --sku-name Standard
```

---

## ARM Templates & Bicep

### ARM Templates

```bash
# Validate template
az deployment group validate \
  --resource-group myResourceGroup \
  --template-file template.json \
  --parameters parameters.json

# Deploy template
az deployment group create \
  --resource-group myResourceGroup \
  --template-file template.json \
  --parameters parameters.json

# Deploy with inline parameters
az deployment group create \
  --resource-group myResourceGroup \
  --template-file template.json \
  --parameters storageAccountName=mystorageaccount location=eastus

# What-if deployment (preview changes)
az deployment group what-if \
  --resource-group myResourceGroup \
  --template-file template.json

# Export resource group to template
az group export --name myResourceGroup > exported-template.json
```

### Bicep

```bash
# Build Bicep to ARM
az bicep build --file main.bicep

# Decompile ARM to Bicep
az bicep decompile --file template.json

# Deploy Bicep
az deployment group create \
  --resource-group myResourceGroup \
  --template-file main.bicep \
  --parameters @parameters.json

# Install/upgrade Bicep
az bicep install
az bicep upgrade
```

---

## Tips & Best Practices

### Output Formatting

```bash
# Table format (readable)
az vm list --output table

# JSON format (for scripting)
az vm list --output json

# TSV format (for parsing)
az vm list --query "[].name" --output tsv

# YAML format
az vm list --output yaml
```

### JMESPath Queries

```bash
# Get specific property
az vm show -g myRG -n myVM --query hardwareProfile.vmSize

# Get multiple properties
az vm show -g myRG -n myVM --query "{Name:name, Size:hardwareProfile.vmSize}"

# Filter results
az vm list --query "[?location=='eastus']"

# Get first result
az vm list --query "[0]"

# Contains filter
az vm list --query "[?contains(name, 'prod')]"
```

### Useful Tips

```bash
# Use --no-wait for async operations
az vm create ... --no-wait

# Use --yes to skip confirmations
az group delete --name myRG --yes

# Use --debug for troubleshooting
az vm list --debug

# Use --verbose for detailed output
az vm create ... --verbose

# Check command help
az vm create --help

# Find commands
az find "create virtual machine"

# Interactive mode
az interactive
```

### Environment Variables

```bash
# Set subscription via environment
export AZURE_SUBSCRIPTION_ID="your-subscription-id"

# Disable CLI telemetry
export AZURE_CORE_COLLECT_TELEMETRY=false

# Set default output format
export AZURE_CORE_OUTPUT=table
```

---

## 📚 Additional Resources

- [Azure CLI Documentation](https://learn.microsoft.com/en-us/cli/azure/)
- [Azure CLI Reference](https://learn.microsoft.com/en-us/cli/azure/reference-index)
- [JMESPath Tutorial](https://jmespath.org/tutorial.html)
- [Azure CLI Samples](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-samples)

---

**Pro Tip**: Save frequently used commands as shell aliases or scripts for quick access!

```bash
# Example aliases
alias azl="az login"
alias azrg="az group list --output table"
alias azvms="az vm list --output table"
```

---

*Last Updated: November 2025*
