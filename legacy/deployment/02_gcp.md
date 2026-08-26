# 02 · Google Cloud Platform — free-tier deployment options

> **Verified against `cloud.google.com/free` on 2026-08-21.** Figures below are quoted from that
> page unless marked otherwise. Re-check before relying on any exact number — GCP's own free-tier
> page states limits "do not expire, but are subject to change."
>
> This file is a general GCP reference. For Sutra's own hands-on GCP walkthrough (which this
> file does not duplicate), see [day_086.md](../days/day_086.md) (containerize),
> [day_087.md](../days/day_087.md) (Agent Runtime, parked/never-run), and
> [day_088.md](../days/day_088.md) (`kind` Kubernetes, standing in for GKE).

---

## 1 · What's genuinely free on GCP, and for how long

| Tier | What it is | Expires? |
| --- | --- | --- |
| **$300 free credit** | Given to new customers to try any product | 30 days ("You won't be charged until you activate your full paid account" — but a card is required to sign up) |
| **"Free Tier" products (Always Free)** | A renewing monthly quota per product, no time limit | Never — but the quota resets monthly and does not roll over |

**Always-Free quotas relevant to running an agent (verified 2026-08-21):**

| Product | Free quota | Note |
| --- | --- | --- |
| Compute Engine | **1 non-preemptible `e2-micro` VM/month**, in **`us-west1` (Oregon), `us-central1` (Iowa), or `us-east1` (South Carolina) only** | Confirmed 2026-08-21, `docs.cloud.google.com/free/docs/free-cloud-features` (updated 2026-08-11): also includes **30 GB-months standard persistent disk** and **1 GB/month outbound data transfer** (North America only); the instance limit is by *total hours across all your e2-micro instances combined*, not per-instance |
| Cloud Run | **2 million requests/month** | Same page: also **360,000 GB-seconds memory + 180,000 vCPU-seconds compute** and **1 GB/month outbound data transfer** (North America). Scale-to-zero by default — the free quota is meaningful *because* an idle service costs nothing |
| Cloud Run functions | **2 million invocations/month** | GCP's current name for what was "Cloud Functions" |
| Cloud Storage | 5 GB-months Standard Storage | |
| Artifact Registry | 0.5 GB storage/month | small — a handful of container image layers, not many versions |
| Secret Manager | 6 secret versions/month | thin; see [00_stay_free_safety.md](00_stay_free_safety.md) §5 on preferring cheaper config paths for anything beyond a couple of secrets |
| BigQuery | 1 TB queries/month | not relevant to deploying an agent, listed for completeness |
| GKE | **One Autopilot or Zonal cluster's management fee waived, per month** | ⚠️ **Nodes are not included** — see §4 |
| Cloud Build | 120 build-minutes/day | |

**Agent Engine — a 2026-08-21 finding worth recording.** The same fetched page lists: *"Agent
Engine — Enterprise-grade orchestration and customization for AI agents. First 180,000
vCPU-seconds (50 hours) per month. First 360,000 GiB-seconds (100 hours) per month."* This is a
free monthly allotment that [day_087.md](../days/day_087.md) (dated 2026-08-20) did not record —
that day's research found only *"Agent Runtime is a paid service and you may incur costs if you
go above the no-cost access tier,"* without quoting the specific numbers above. **This doesn't
necessarily change Day 87's conclusion**: attaching a billing account is still required to use
Agent Runtime at all (Addendum 02's actual blocker), regardless of whether usage inside the
allotment is $0. Treat this as a "re-verify on the day" item for whoever runs Day 87, per that
day's own re-verification block — not as a standing green light.

## 2 · Before you create anything

1. Read [00_stay_free_safety.md](00_stay_free_safety.md) and set a budget alert.
2. `gcloud` requires a project with **billing enabled**, even to use $0-cost Always-Free
   resources — this surprises people the first time. Enabling billing is not the same as
   spending money, but it is the step that makes spending *possible*, which is exactly why
   the budget alert comes first.

```powershell
winget install -e --id Google.CloudSDK
gcloud init                              # interactive: sign in, pick/create a project
gcloud config set project YOUR_PROJECT_ID
gcloud billing accounts list             # confirm which account you'll attach
gcloud services enable run.googleapis.com compute.googleapis.com
```

## 3 · Cloud Run — deploy a container, pay only past 2M requests/month

```powershell
gcloud run deploy myagent `
  --source . `
  --region=us-central1 `
  --allow-unauthenticated `
  --min-instances=0 `
  --max-instances=2 `
  --memory=512Mi `
  --set-env-vars="GOOGLE_GENAI_USE_VERTEXAI=FALSE" `
  --set-secrets="GOOGLE_API_KEY=google-api-key:latest"
```

| Flag | What it does | Why it's set this way |
| --- | --- | --- |
| `--source .` | builds your Dockerfile via Cloud Build and deploys the result — no manual `docker push` needed | uses the 120 build-min/day free quota |
| `--region=us-central1` | Cloud Run is regional; pick one close to you or your users | any region works for the request-count free tier, which is not region-restricted the way `e2-micro` is |
| `--allow-unauthenticated` | makes the URL publicly reachable with no auth | fine for a demo; remove this and use IAM invoker roles for anything real |
| `--min-instances=0` | **the line that keeps this free** — scales fully to zero when idle | the opposite value (`--min-instances=1`) keeps a container warm 24/7 and bills for it continuously, defeating the free tier's scale-to-zero design |
| `--max-instances=2` | a hard ceiling on concurrent instances | caps worst-case cost from an unexpected traffic spike or bug (e.g., a retry loop) |
| `--set-secrets` | pulls from **Secret Manager** at start time, never bakes the key into the image or the service config | the same "inject at runtime, never bake in" rule as Day 86 §3, expressed as a managed-platform feature instead of a `docker run -e` flag |

Create the secret first: `printf "%s" "$env:GOOGLE_API_KEY" | gcloud secrets create google-api-key --data-file=-`

## 4 · GKE — the control plane is free; the nodes are not

```powershell
# Autopilot: Google manages node provisioning entirely — you pay per pod resource request.
gcloud container clusters create-auto myagent-cluster --region=us-central1
```

The Always-Free grant is **"one Autopilot or Zonal cluster per month"** — meaning the
**cluster management fee** is waived, not the compute. Autopilot bills per pod's requested
vCPU/memory/storage from the moment a pod exists, with no separate free node allowance. A
Zonal (Standard) cluster's node VMs are ordinary Compute Engine instances, billed normally (only
the one `e2-micro`/month is free — a real workload needs more than that).

**Recommendation for a zero-budget project:** don't run GKE for anything beyond a brief,
deliberate experiment you tear down the same session. Use `kind` locally instead — Day 88 makes
exactly this choice, for exactly this reason:

```powershell
gcloud container clusters delete myagent-cluster --region=us-central1 --quiet   # the moment you're done
```

## 5 · Compute Engine `e2-micro` — a small, real, Always-Free VM

```powershell
gcloud compute instances create myagent-vm `
  --zone=us-central1-a `
  --machine-type=e2-micro `
  --image-family=debian-12 `
  --image-project=debian-cloud `
  --tags=http-server

gcloud compute firewall-rules create allow-http --allow=tcp:8080 --target-tags=http-server

gcloud compute ssh myagent-vm --zone=us-central1-a
# on the VM:
curl -fsSL https://get.docker.com | sh
sudo docker run -d -p 8080:8080 --env-file .env myagent:dev
```

| Flag | What it does |
| --- | --- |
| `--machine-type=e2-micro` | the specific shape the Always-Free grant covers — any larger type bills immediately |
| `--zone=us-central1-a` | zone must be in an eligible region (§1) — an eligible-region rule, not an eligible-zone one, but pick a zone inside one of them |
| `firewall-rules create allow-http` | GCP VMs have **no open ports by default**; without this rule the container runs but nothing outside the VM can reach port 8080 |

## 6 · Terraform for GCP — the same Cloud Run deploy, declaratively

```hcl
# main.tf
terraform {
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
    scaling { min_instance_count = 0, max_instance_count = 2 }  # keeps it free — see §3
    containers {
      image = "gcr.io/${var.project_id}/myagent:dev"
      resources { limits = { memory = "512Mi", cpu = "1" } }
    }
  }
}

resource "google_cloud_run_v2_service_iam_member" "public" {
  location = google_cloud_run_v2_service.myagent.location
  name     = google_cloud_run_v2_service.myagent.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
```

| Block | What it does |
| --- | --- |
| `required_providers` | pins the `google` provider so `terraform init` downloads a known version — see [05_terraform.md](05_terraform.md) for why pinning matters |
| `google_cloud_run_v2_service` | the declarative equivalent of the `gcloud run deploy` command in §3 |
| `scaling { min_instance_count = 0 }` | the Terraform spelling of `--min-instances=0` — still the line that keeps this free |
| `google_cloud_run_v2_service_iam_member` | the declarative equivalent of `--allow-unauthenticated` |

```powershell
terraform init
terraform plan -var="project_id=YOUR_PROJECT_ID"     # review before applying — see 05_terraform.md §4
terraform apply -var="project_id=YOUR_PROJECT_ID"
terraform destroy -var="project_id=YOUR_PROJECT_ID"  # the moment you're done testing
```

## 7 · Cleanup

```powershell
gcloud run services delete myagent --region=us-central1 --quiet
gcloud compute instances delete myagent-vm --zone=us-central1-a --quiet
gcloud compute firewall-rules delete allow-http --quiet
gcloud container clusters delete myagent-cluster --region=us-central1 --quiet
gcloud secrets delete google-api-key --quiet
```
