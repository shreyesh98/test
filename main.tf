terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.84.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "aks_rg" {
  name     = "myResourceGroup"
  location = "East US" 
}

resource "azurerm_kubernetes_cluster" "aks_cluster" {
  name                = "myAKSCluster"
  location            = azurerm_resource_group.aks_rg.location
  resource_group_name = azurerm_resource_group.aks_rg.name
  dns_prefix          = "myakscluster"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2" 
  }

  service_principal {
    client_id     = "client_id"
    client_secret = "client_secret"
  }

  tags = {
    Environment = "Production"
  }
}

