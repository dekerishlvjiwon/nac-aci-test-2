terraform {
  required_providers {
    aci = {
      source  = "CiscoDevNet/aci"
      version = "2.18.0"
    }
  }
}

provider "aci" {
  username = "admin"
  private_key = "/home/user/admin.key"
  cert_name = "terraform"
  url      = "https://172.17.220.100"
  insecure = true
}

module "aci" {
  source  = "netascode/nac-aci/aci"
  version = "1.2.0"

  yaml_directories = ["data"]

  manage_access_policies    = true
  manage_fabric_policies    = true
  manage_pod_policies       = true
  manage_node_policies      = true
  manage_interface_policies = true
  manage_tenants            = true
}
