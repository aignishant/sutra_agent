# 05 · Terraform — infrastructure as code, for all three clouds

> **Verified against `developer.hashicorp.com/terraform/install` on 2026-08-21: current version
> is 1.15.9.** Re-check before pinning a version in any config.

---

## 1 · What Terraform is, in one paragraph

Terraform is a **declarative** tool: you describe the infrastructure you want in `.tf` files,
and Terraform figures out what to create, change, or destroy to make reality match the file —
the same "describe the desired state, let a control loop reconcile it" idea Kubernetes uses
([01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md) §3's Deployment), just
applied to cloud resources instead of pods. The reason it matters for a zero-budget project
specifically: **`terraform destroy` reliably removes everything `apply` created**, including the
orphaned neighbors ([00_stay_free_safety.md](00_stay_free_safety.md) §5) that are easy to forget
when deleting things by hand one console click at a time.

## 2 · Install (Windows)

```powershell
winget install -e --id Hashicorp.Terraform
terraform version   # confirm what you actually got — don't assume it matches 1.15.9 above
```

Terraform itself never touches a cloud account — only the *providers* you configure do. You can
practice the workflow below entirely against the `local` and `null` providers (no cloud
account, no card, genuinely $0) before ever pointing it at GCP/Azure/AWS.

## 3 · The core workflow, explained

```powershell
terraform init       # downloads the providers this config declares, sets up local state
terraform plan       # computes what WOULD change — reads nothing destructively, changes nothing
terraform apply      # shows the same plan again, asks for confirmation, then executes it
terraform destroy    # computes and executes the removal of everything this config created
```

| Command | What it actually does | Why it's safe to run often |
| --- | --- | --- |
| `init` | reads `required_providers` blocks, downloads the matching plugin binaries into `.terraform/`, initializes the state backend | idempotent — safe to re-run any time, including after adding a new provider |
| `plan` | compares the `.tf` files against the current state file and the real infrastructure, prints a diff (`+` create, `~` update, `-` destroy) | **read-only** — this is the step to actually read before ever typing `apply`, especially the `-` lines |
| `apply` | re-runs the same comparison, then executes it after you type `yes` | the only command that changes real infrastructure |
| `destroy` | `apply` with every resource's target state set to "absent" | the command [00_stay_free_safety.md](00_stay_free_safety.md) §4 asks you to run the same session you finish testing |

## 4 · Reading a `terraform plan` — the habit that prevents surprise bills

Before typing `yes` at an `apply` prompt, read the summary line:

```
Plan: 3 to add, 0 to change, 0 to destroy.
```

If a `plan` you expected to be small says **"12 to add"**, stop and read *why* — a single
resource block (like a Container App environment, or a VPC) often implicitly creates several
child resources (subnets, route tables, a default security group), and it's much cheaper to
notice that in a `plan` than in a bill. This is the direct Terraform-shaped version of
[00_stay_free_safety.md](00_stay_free_safety.md) §2's "know the number you expect before you
create anything."

## 5 · State: what it is, and where it's safe to keep it for free

Terraform's **state file** (`terraform.tfstate`) is its record of what it created and their
real-world IDs — without it, `terraform destroy` doesn't know what to remove.

| Backend | Cost | Good for |
| --- | --- | --- |
| **Local** (default — a `.tfstate` file next to your `.tf` files) | Free | Solo learning, exactly what every example in this folder assumes |
| **GCS bucket** | Free up to 5 GB (GCP's Always-Free storage grant, §[02_gcp.md](02_gcp.md) §1) | If you want state to survive a wiped laptop, still at $0 |
| **S3 bucket** | Free up to 5 GB for 12 months (AWS's free-tier grant), then pennies/month after | Same idea, on AWS |
| **Azure Storage (Blob)** | Free up to 5 GB (Azure's Always-Free grant) | Same idea, on Azure |
| **HCP Terraform (Terraform Cloud)** | Free for up to 5 users | Adds locking (prevents two people applying at once) and a web UI for free, without self-hosting a backend |

⚠️ **`terraform.tfstate` can contain secrets in plaintext** (e.g., a generated database
password) — treat it exactly like `.env`: add it to `.gitignore`, never commit it. This repo's
existing rule ("secrets never touch git," Principle 9) applies to Terraform state without
exception.

```gitignore
# Terraform — add to .gitignore alongside the existing secrets rules
.terraform/
*.tfstate
*.tfstate.*
*.tfvars
!*.tfvars.example
```

## 6 · A full worked example — a minimal, free-tier-only Cloud Run deploy

```
myagent-infra/
├── main.tf         # the resources
├── variables.tf    # inputs
├── outputs.tf       # what to print after apply
└── terraform.tfvars # your actual values — gitignored
```

`variables.tf`:

```hcl
variable "project_id" {
  description = "GCP project ID"
  type        = string
}
```

`main.tf` — the same Cloud Run service from [02_gcp.md](02_gcp.md) §6, reproduced here to show
the full file layout:

```hcl
terraform {
  required_version = ">= 1.9"
  required_providers {
    google = { source = "hashicorp/google", version = "~> 6.0" }
  }
}

provider "google" {
  project = var.project_id
  region  = "us-central1"
}

resource "google_cloud_run_v2_service" "myagent" {
  name     = "myagent"
  location = "us-central1"
  template {
    scaling { min_instance_count = 0, max_instance_count = 2 }
    containers {
      image = "gcr.io/${var.project_id}/myagent:dev"
    }
  }
}
```

`outputs.tf`:

```hcl
output "service_url" {
  value = google_cloud_run_v2_service.myagent.uri
}
```

`terraform.tfvars` (gitignored — this is where the real project ID lives, never in `main.tf`):

```hcl
project_id = "your-actual-project-id"
```

```powershell
cd myagent-infra
terraform init
terraform plan       # confirm: Plan: 1 to add, 0 to change, 0 to destroy
terraform apply
# terraform output service_url   → prints the live URL
terraform destroy    # when done
```

The equivalent Azure and AWS examples are in [03_azure.md](03_azure.md) §6 and
[04_aws.md](04_aws.md) §6 — same four-command workflow, different provider block and resources.

## 7 · Cost-safety practices specific to Terraform

- **Always run `plan` and read it before `apply`** — §4.
- **`terraform destroy` after every test session** — the single highest-leverage habit in this
  entire folder for Terraform specifically, because it removes orphans (§00's danger list)
  automatically, which manual console cleanup routinely misses.
- **Pin provider versions** (`~> 6.0`, not unpinned) so `terraform init` can't silently pull a
  major version with different defaults or pricing-relevant behavior between one `init` and the
  next.
- **Consider a free cost-estimation tool** (e.g., Infracost, which has a free tier for local/CLI
  use) if you want a dollar estimate *before* `apply` rather than after — optional, not required
  for anything in this folder, since every example here is built to fit inside a real Always-Free
  grant already.
- **Never commit `terraform.tfvars` or `*.tfstate`** — §5.
