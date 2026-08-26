# 03 · Microsoft Azure — free-tier deployment options

> **Verified against `azure.microsoft.com/en-us/pricing/free-services` and
> `azure.microsoft.com/en-us/pricing/details/container-apps/` on 2026-08-21.** Figures marked
> "⚠️ recalled" are long-stable, widely documented Azure facts that this session's fetches did
> not directly confirm — re-verify at the linked pricing page before relying on the exact number.

---

## 1 · Two kinds of free, and what's genuinely renewing

Azure's free-services page (fetched 2026-08-21) describes exactly two categories:

| Tier | What it is | Expires? |
| --- | --- | --- |
| **Free for your first 12 months** | Elevated free monthly amounts of specific services, from account-creation date | Yes — 12 months, new customers only |
| **65+ always-free services** | A renewing monthly amount, for as long as you have an Azure account | Never — resets monthly |

Plus a **$200 credit for 30 days** on signup (separate from both of the above).

**Confirmed Always Free, relevant to deploying an agent:**

| Service | Free grant | Source |
| --- | --- | --- |
| **Azure Container Apps** (Consumption plan) | **First 180,000 vCPU-seconds, 360,000 GiB-seconds, and 2 million requests per subscription per month are free** | confirmed 2026-08-21, `azure.microsoft.com/en-us/pricing/details/container-apps/` |
| **Azure Kubernetes Service (AKS)** | "AKS cluster management is free; you'll incur a charge for resources consumed by nodes" | confirmed 2026-08-21, same as GCP's GKE shape — see §4 |
| Azure Blob Storage | 5 GB LRS hot block, 20,000 read + 10,000 write ops | confirmed 2026-08-21 |
| API Management | 1 million monthly calls (Consumption tier) | confirmed 2026-08-21 |

**⚠️ Recalled, not directly confirmed this session — verify at the product's own pricing page
before relying on the exact figure:**

| Service | Commonly documented free grant |
| --- | --- |
| Azure App Service (Free **F1** tier) | Always free; ~60 CPU-minutes/day, 1 GB storage, no custom domain SSL, no auto-scale |
| Azure Functions (Consumption plan) | Always free; 1,000,000 executions + 400,000 GB-seconds of execution time, per month |
| Azure Container Instances (ACI) | **No free tier** — billed per vCPU-second/GiB-second from the first second |

## 2 · Before you create anything

1. Read [00_stay_free_safety.md](00_stay_free_safety.md) and set a budget (§3 there has the
   exact `az consumption budget create` shape).
2. A **Free Trial** account type is capped by design (cannot silently convert to pay-as-you-go)
   — leaving it in that state until you deliberately upgrade is itself a safety control.

```powershell
winget install -e --id Microsoft.AzureCLI
az login
az account show                          # confirm the subscription you expect
az group create --name myagent-rg --location eastus
```

## 3 · Azure Container Apps — the Cloud-Run-equivalent

```powershell
az containerapp up `
  --name myagent `
  --resource-group myagent-rg `
  --location eastus `
  --environment myagent-env `
  --source . `
  --target-port 8080 `
  --ingress external `
  --min-replicas 0 `
  --max-replicas 2 `
  --env-vars "GOOGLE_GENAI_USE_VERTEXAI=FALSE"
```

| Flag | What it does | Why it's set this way |
| --- | --- | --- |
| `--source .` | builds the Dockerfile in-place and pushes to a managed registry | avoids a manual `az acr build` + `docker push` round trip |
| `--ingress external` | exposes a public HTTPS URL | use `internal` instead if this only needs to be reached by other Container Apps in the same environment |
| `--min-replicas 0` | **the line that keeps this inside the free grant** — scales to zero when idle | the direct analog of Cloud Run's `--min-instances=0`; setting this to 1+ keeps a replica warm continuously and consumes the vCPU-second/GiB-second allowance around the clock |
| `--max-replicas 2` | caps worst-case concurrent replicas | bounds cost from an unexpected spike |

Secrets, injected at runtime rather than baked in (same rule as every other file in this
folder):

```powershell
az containerapp secret set --name myagent --resource-group myagent-rg `
  --secrets "google-api-key=$env:GOOGLE_API_KEY"
az containerapp update --name myagent --resource-group myagent-rg `
  --set-env-vars "GOOGLE_API_KEY=secretref:google-api-key"
```

## 4 · AKS — free control plane, billable nodes (same shape as GKE)

```powershell
az aks create --resource-group myagent-rg --name myagent-aks `
  --node-count 1 --node-vm-size Standard_B2s `
  --generate-ssh-keys
az aks get-credentials --resource-group myagent-rg --name myagent-aks
kubectl get nodes
```

| Flag | What it does |
| --- | --- |
| `--node-count 1` | one node — more nodes means more billable VMs, with no corresponding free grant |
| `--node-vm-size Standard_B2s` | a small burstable VM size; still an ordinary billed Compute resource — **the cluster management itself is the only free part** |

**Recommendation, identical to the GCP file's §4:** don't run AKS for anything beyond a brief,
deliberate, torn-down-the-same-session experiment. Use `kind`/`k3d` locally
([01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md)) for actual iteration —
it is the same Kubernetes API, at genuinely $0.

```powershell
az aks delete --resource-group myagent-rg --name myagent-aks --yes --no-wait
```

## 5 · Azure App Service Free (F1) tier — for a small always-on-ish web app

```powershell
az appservice plan create --name myagent-plan --resource-group myagent-rg --sku F1 --is-linux
az webapp create --name myagent-app --resource-group myagent-rg `
  --plan myagent-plan --deployment-container-image-name "myregistry.azurecr.io/myagent:dev"
az webapp config appsettings set --name myagent-app --resource-group myagent-rg `
  --settings GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

| Flag | What it does |
| --- | --- |
| `--sku F1` | the Free tier — no cost, but capped CPU-minutes/day (⚠️ recalled: ~60/day) and no custom-domain TLS |
| `--is-linux` | Linux App Service plans support container deployment; Windows plans have a different model |

F1's CPU-minute cap makes it a reasonable choice for a low-traffic demo, not for anything doing
real per-request LLM inference at volume — Container Apps' request-based free grant (§3) fits
an agent's bursty traffic shape better.

## 6 · Terraform for Azure

```hcl
# main.tf
terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" }
  }
}

provider "azurerm" { features {} }

resource "azurerm_resource_group" "myagent" {
  name     = "myagent-rg"
  location = "eastus"
}

resource "azurerm_container_app_environment" "myagent" {
  name                = "myagent-env"
  resource_group_name = azurerm_resource_group.myagent.name
  location            = azurerm_resource_group.myagent.location
}

resource "azurerm_container_app" "myagent" {
  name                         = "myagent"
  container_app_environment_id = azurerm_container_app_environment.myagent.id
  resource_group_name          = azurerm_resource_group.myagent.name
  revision_mode                = "Single"

  template {
    min_replicas = 0     # keeps this inside the free vCPU-s/GiB-s/request grant — see §3
    max_replicas = 2
    container {
      name   = "myagent"
      image  = "myregistry.azurecr.io/myagent:dev"
      cpu    = 0.5
      memory = "1Gi"
    }
  }

  ingress {
    external_enabled = true
    target_port      = 8080
  }
}
```

| Block | What it does |
| --- | --- |
| `azurerm_resource_group` | Azure's unit of "delete everything at once" — the single most useful cleanup primitive Azure has (§7) |
| `azurerm_container_app_environment` | the shared networking/logging boundary a Container App must live inside |
| `template.min_replicas = 0` | the Terraform spelling of `--min-replicas 0` from §3 — still the line that keeps this free |

```powershell
terraform init
terraform plan     # review before applying — see 05_terraform.md §4
terraform apply
terraform destroy  # the moment you're done testing
```

## 7 · Cleanup — the resource-group nuke

```powershell
az group delete --name myagent-rg --yes --no-wait
```

Deleting the resource group deletes everything inside it — Container Apps, the AKS cluster, the
App Service plan, all of it, in one command. This is the fastest way to guarantee nothing from
§5's danger list (orphaned IPs, load balancers, etc.) survives an experiment on Azure
specifically, because Azure's resource model makes "everything in this group" a first-class,
reliable unit.
