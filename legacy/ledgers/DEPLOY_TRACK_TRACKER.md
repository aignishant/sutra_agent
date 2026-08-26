# Deployment-track tracker (Phase 16, Days 97+) — meta-file, NOT `PROGRESS.md`

> **Read `ADR-0002-deployment-implementation-track.md` first** — it explains why this track has
> its own ledger instead of appending to `docs/days/PROGRESS.md`, and why that separation matters
> for `CLAUDE.md`'s "generate day N" workflow on the *original* 96-day curriculum.
>
> **Purpose:** turn `docs/deployment/00_stay_free_safety.md` .. `07_free_databases_and_extras.md`
> (which describe *which* free options exist) into day-numbered, hands-on, run-it-yourself
> implementation guides — one platform per day, "pick up one by one," per the user's request
> (2026-08-21). **This file is how work resumes if a session ends mid-track:** read the table
> below, find the first row that isn't ✅, that's the next day to write or run.
>
> **Rules for any session working this track:**
> - Write/edit only `docs/days/day_09{7,8,9}.md`, `docs/days/day_1{0-9}{0-9}.md`, and this
>   tracker. Never touch `sutra/`, `tests/`, `tools/`, or `docs/00_MASTER_PLAN.md`.
> - Each day closes exactly one `DEPLOY-NN` ID (§ below) — never a master-plan `AG/ADK/MCP/SK/
>   OPS/SEC` ID; those two ID spaces are deliberately kept apart.
> - Follow the master plan's §17 Day Document Contract / §18 Style Guide **in spirit**
>   (story → mission → concepts → build-with-verify → failure lab → interview corner →
>   gates-and-ledger), adapted per ADR-0002 point 5: the gate targets this file, not
>   `PROGRESS.md`/`TRACEABILITY.md`/`PACKAGES.md`.
> - Zero-budget discipline (Addendum 02) is not relaxed for this track. A day either (a) uses a
>   genuine, renewing Always-Free allowance and is real hands-on, or (b) touches something that
>   bills regardless of usage (a managed K8s node pool, EKS's control plane) and is written with
>   Day 87's parked discipline — first line says never run, dated sources, a re-verification
>   command, a stated trigger condition. Never (c): a required step that needs a billing account
>   to be attached with no free floor under it.
> - Every command in a day doc is something **the human runs on their own machine/account** —
>   these days do not, and cannot, execute cloud CLI commands on the user's behalf.

---

## The plan (subject to reordering — update this table, don't just trust memory)

| Day | `DEPLOY-NN` | Platform / topic | Expands on | Real hands-on or parked? | Status |
| --- | --- | --- | --- | --- | --- |
| 097 | DEPLOY-01 | GCP Cloud Run | [02_gcp.md](../deployment/02_gcp.md) §3 | Real — Always Free (2M req/mo) | 📄 doc written 2026-08-21; **not yet run** (needs a human with a GCP account) |
| 098 | DEPLOY-02 | GCP Compute Engine `e2-micro` | [02_gcp.md](../deployment/02_gcp.md) §5 | Real — Always Free | 📄 doc written 2026-08-21; **not yet run** (needs a human with a GCP account) |
| 099 | DEPLOY-03 | GCP GKE + Terraform for GCP | [02_gcp.md](../deployment/02_gcp.md) §4, §6 | Parked (nodes bill) + real Terraform against Cloud Run | 📄 doc written 2026-08-21; **not yet run** (needs a human with a GCP account) |
| 100 | DEPLOY-04 | Azure Container Apps | [03_azure.md](../deployment/03_azure.md) §3 | Real — Always Free (180k vCPU-s/mo) | 📄 doc written 2026-08-21; **not yet run** (needs a human with an Azure account + Docker) |
| 101 | DEPLOY-05 | Azure App Service F1 + Functions | [03_azure.md](../deployment/03_azure.md) §5 | Real — Always Free (F1 code-deploy); Functions documented + declined on shape grounds | 📄 doc written 2026-08-21; **not yet run** |
| 102 | DEPLOY-06 | Azure AKS + Terraform for Azure | [03_azure.md](../deployment/03_azure.md) §4, §6 | Parked (nodes bill) + real Terraform | 📄 doc written 2026-08-21; **not yet run** |
| 103 | DEPLOY-07 | AWS Lambda (container image) | [04_aws.md](../deployment/04_aws.md) §4 | Real — Always Free **compute**; ⚠️ ECR storage is not free (delete the repo same session) | 📄 doc written 2026-08-21; **not yet run** |
| 104 | DEPLOY-08 | AWS EC2 free tier | [04_aws.md](../deployment/04_aws.md) §5 | 🅿️ **Parked — re-scoped 2026-08-21.** ⚠️ **No** account vintage yields a $0 internet-reachable VM: public IPv4 is $0.005/h with no allowance. Rewritten as the track's cost-anatomy day | 📄 doc written 2026-08-21 (re-scope done) |
| 105 | DEPLOY-09 | AWS EKS (why not) + Terraform for AWS | [04_aws.md](../deployment/04_aws.md) §3, §6 | Parked — **not free, any tier** ($0.10/hr) + real Terraform against Lambda | ⬜ planned |
| 106 | DEPLOY-10 | Oracle Cloud Always Free VM | [06_other_free_platforms.md](../deployment/06_other_free_platforms.md) §1 | Real — Always Free, no 12-month clock | ⬜ planned |
| 107 | DEPLOY-11 | Terraform multi-cloud capstone | [05_terraform.md](../deployment/05_terraform.md) | Real — ties Days 97/100/103 under one workflow | ⬜ planned |
| 108 | DEPLOY-12 | Wiring in a free database (Neon + Upstash) | [07_free_databases_and_extras.md](../deployment/07_free_databases_and_extras.md) §2, §4 | Real — both free, no card | ⬜ planned |
| 109 | DEPLOY-13 | Render + free tunnels for demos | [06_other_free_platforms.md](../deployment/06_other_free_platforms.md) §2, §7 | Real — free | ⬜ planned |
| 110 | DEPLOY-14 | Phase 16 gate — cost audit & teardown verification | all of the above | Retro/audit day, no new platform | ⬜ planned |

**Resume pointer: next day to *write* is 105.** (Days 097-104's docs exist; whether any has
been *run* is a separate status tracked in its own row above, not this pointer.)

## Notes for whoever (human or agent) picks this up next

- **Day 97 did NOT wait for Day 86.** Day 86's `Dockerfile`/`docker-compose.yml` don't exist in
  the repo yet (pre-generated doc, not yet run, per `GENERATION_TRACKER.md`/`PROGRESS.md`). Day
  97 uses `adk deploy cloud_run` instead, which builds the container from Python source directly
  — this is *why* Phase 16 can proceed independently of how far the original curriculum has
  actually been run. Every later real-hands-on day in this track (100, 101, 103, 104, 106) should
  keep doing the same: deploy `sutra/` (or whatever exists) as-is, don't block on other days.
- **Real gaps found in `sutra/` while writing Day 97 (2026-08-21):** `sutra/__init__.py` is
  empty (Day 97 has the human add one line: `from . import agent`) and there is no
  `requirements.txt` (Day 97 has the human generate one fresh via `uv export`, gitignored, never
  committed — `pyproject.toml`/`uv.lock` stay the real source of truth). Both are one-time,
  additive fixes — record in each subsequent day whether the *same* platform needs the same or a
  different fix (Azure/AWS's own Python buildpacks may have different expectations).
- **Open question Day 97 could not resolve without a live run:** `sutra/agent.py` uses an
  absolute import (`from sutra.config import load_env`), and it is not 100% certain this
  resolves correctly inside `adk deploy cloud_run`'s packaged container (whose documented sample
  layout, `capital_agent/`, is a self-contained top-level package rather than one package among
  several at a repo root). Day 97 §5's failure lab is written as a live diagnostic rather than a
  scripted answer — **whoever actually runs Day 97 should come back and fill in the real
  outcome here**, since Days 100/103's Azure/AWS equivalents will hit the identical question.
- **Day 98 finding: the `__init__.py` fix Day 97 needed is packaging-tool-specific, not
  universal.** `adk api_server`/`adk run`/`adk web` accept a single-agent folder directly
  (confirmed `adk.dev/api-reference/cli/`, 2026-08-21) and do NOT need `sutra/__init__.py` to
  import `agent` — only `adk deploy cloud_run`/`gke`/`agent_engine` (the packaging commands)
  need it. Day 98 needed **zero** `sutra/` code changes. Worth re-confirming this holds for
  Azure/AWS's own "run the process directly on a VM" days (101, 104) — it should, since those
  don't involve ADK's packaging step either, but they weren't written when this note was made.
- **Day 98 also found `adk api_server --session_service_uri=sqlite:///...` works** for real,
  disk-backed session persistence — confirmed via `adk.dev/api-reference/cli/`. This is the
  answer to "how do I get persistence on a VM without a managed DB" and should be reused/cited
  by any later day that runs the agent directly on a VM (Azure/AWS/Oracle equivalents).
- **Day 99 finding: Day 97's cleanup is a prerequisite break for every later GCP day.** Day 97
  §4 Step 7 deletes the Cloud Run service *and* the `GOOGLE_API_KEY` secret, and notes the
  Artifact Registry image as an orphan to consider deleting. Day 99's Terraform config needs
  **both** the image URI and that secret, so Day 99 §4 Step 1 is an explicit
  "reconcile the prerequisites" step with a branch for each. This is correct behaviour on
  Day 97's part, not a bug — but **any future day that builds on a previous day's cloud
  artifacts must open with the same reconciliation step rather than assuming they survived.**
  Days 102 and 105 (Terraform for Azure/AWS) inherit this pattern directly from Days 100/103.
- **Day 99 finding: `adk deploy cloud_run` is usable purely as an image builder.** Deploy under
  a throwaway service name, delete the service, keep the image in Artifact Registry, then let
  Terraform create the real service from that image URI. This is how Phase 16 gets a genuine
  Sutra container without waiting for Day 86's `Dockerfile` to exist. ⚠️ Days 100/103
  (Azure/AWS) **cannot** reuse this trick — ADK only ships `cloud_run`/`gke`/`agent_engine`
  deploy targets, all GCP — so those days need their own container story, and that decision
  should be recorded here when each is written.
- **Day 100 finding — `Dockerfile.adk` now exists, and it is this track's container.** Day 100
  §4 Step 2 has the human create `Dockerfile.adk` + `.dockerignore` at the repo root. It serves
  `adk api_server` (a Day 098 *serving* command, so **no `sutra/` change needed**) and sets
  `ENV PYTHONPATH=/app`, which settles Day 097 §5's open import question deterministically
  instead of leaving it to how the entry point arranges `sys.path`.
  ⚠️ **It deliberately does not collide with Day 086's `Dockerfile`**, which is a different
  artifact for a different job: Day 086's runs `uvicorn sutra.api:app` and healthchecks
  `/readyz`, and **neither `sutra/api.py` nor `/readyz` exists in this repo** (Day 085 code,
  unrun) — so Day 086's image cannot be built today. Two files, two entry points, both valid.
  Whoever runs Day 086 should read this note rather than assume one overwrites the other.
  Days 103 (Lambda) and 106 (Oracle) start from `Dockerfile.adk`; ⚠️ Day 103 must **modify** it,
  because Lambda does not serve plain HTTP containers (it needs the Lambda Runtime API — see the
  Lambda Web Adapter note below).
- **Day 100 finding — ⚠️ `az containerapp up --source .` is not free, correcting
  `03_azure.md` §3.** `--source .` provisions an **Azure Container Registry** to hold the built
  image, and ACR has **no free tier** (verified 2026-08-21,
  `azure.microsoft.com/en-us/pricing/details/container-registry/` — Basic/Standard/Premium only;
  the page renders prices client-side, so the checkable fact recorded here is "no free tier,"
  not a dollar figure). Day 100 uses a **public `ghcr.io` package** instead: free, and Container
  Apps pulls from any public registry with no credentials at all
  (`learn.microsoft.com/en-us/azure/container-apps/containers`). ⚠️ **Not Docker Hub** — the same
  Microsoft page warns its pull rate limits make containers *fail to start*. The general rule
  worth carrying to every remaining day: **compute grants meter consumption, registries bill for
  existence** — so a forgotten registry is this track's likeliest orphan.
- **Azure Container Apps specifics that reject a config outright** (same page, 2026-08-21):
  `linux/amd64` images only (build with `--platform linux/amd64`, or an Apple Silicon build fails
  with an exec-format error), and Consumption-plan CPU/memory must be one of a **fixed set of
  pairs** (0.25/0.5Gi, 0.5/1.0Gi, 0.75/1.5Gi, … always 2 GiB per vCPU) — `0.5` vCPU with `512Mi`
  is rejected, not rounded.
- **The free grant converted to something decidable:** ACA's 180,000 vCPU-s + 360,000 GiB-s/month
  is **~100 replica-hours at 0.5 vCPU / 1.0 GiB** (200 h at the smallest size). A month is ~730
  hours, so unlike Day 098's `e2-micro` — whose grant is sized to *exactly* one instance running
  all month — this grant **cannot** cover a warm replica. `--min-replicas 0` is load-bearing, and
  "just set min-replicas to 1" spends the whole month's grant in about four days.
- **⚠️ Verified 2026-08-21 — AWS's 12-months-free tier no longer exists for new accounts, which
  changes the Day 104 row.** Confirmed against AWS's own announcement
  (`aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/` and the
  AWS News blog post of the same change): accounts created **on or after 2025-07-15** get a
  credit-based Free plan (up to $200 — $100 on signup, $100 earned) that expires after **6
  months or when the credits are spent, whichever comes first**. Accounts created before that
  date remain on the legacy program with its 12-month trials. Consequences:
  - **Day 103 (Lambda) stands as "real hands-on"** — `aws.amazon.com/free/` still lists Always
    Free as a separate category applying "on both the Free and Paid plans," and
    `aws.amazon.com/lambda/pricing/` confirms 1M requests + 400,000 GB-seconds/month.
  - **Day 104 (EC2) must be re-scoped before it is written.** For a new account, EC2 hours are
    paid out of an expiring credit balance, which is *not* a renewing free floor and therefore
    fails Addendum 02's category (a). Day 104 should open by having the human check their
    account's vintage, and treat the new-account path with Day 87's parked discipline.
  - **`docs/deployment/04_aws.md` §1's "12 Months Free" rows (EC2, S3, RDS) are now wrong for
    new accounts.** That file is outside this track's write scope (see the rules above), so this
    note is the record; fix it via a separate change, not from a Phase 16 day.
- **Verified 2026-08-21, for days not yet written** (so they don't have to re-fetch):
  `aws.amazon.com/eks/pricing/` — EKS control plane **$0.10/cluster/hour, no free tier**
  (Day 105 stays parked) · `azure.microsoft.com/en-us/pricing/details/functions/` — Consumption
  plan free grant **1M executions + 400,000 GB-s/month per subscription** (Day 101) ·
  `azure.microsoft.com/en-us/pricing/details/app-service/linux/` — F1 is **"Shared (60 CPU
  minutes / day)", 1 GB RAM, 1 GB storage**, explicitly "not supported" for production, and
  "Free and shared service plans do not support SSL" (Day 101) ·
  `developer.hashicorp.com/terraform/install` — Terraform stable **1.15.9** (Days 99/102/105/107)
  · `adk.dev/api-reference/cli/` — `--session_service_uri` accepts SQLite **and other
  SQLAlchemy-compatible database URIs**, which is what makes Day 108's Neon Postgres path real.
  ⚠️ **Day 103 will need this:** a Lambda container image must speak the **Lambda Runtime API** —
  a plain HTTP server like `adk api_server` does not work unmodified, which
  `04_aws.md` §4 glosses over when it calls Day 086's Dockerfile "the natural fit." The bridge is
  the **AWS Lambda Web Adapter**, current release **1.0.1** (verified 2026-08-21,
  `github.com/awslabs/aws-lambda-web-adapter`), added with
  `COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:1.0.1 /lambda-adapter /opt/extensions/lambda-adapter`
  plus `AWS_LWA_PORT` (default `8080`) and `AWS_LWA_READINESS_CHECK_PATH` (default `/`).
  ⚠️ Still unverified and flagged for the day that needs it: whether App Service **F1** accepts
  a custom Linux container at all (Microsoft's own custom-container quickstarts all specify
  **B1**, and `03_azure.md` §5 pairs `--sku F1` with `--deployment-container-image-name` — Day
  101 must resolve this live rather than trust that file).
- **Day 101 finding — F1 is metered in a unit nothing else in this track uses: CPU-minutes per
  *day*.** 60 CPU-min/day, 1 GB RAM, 1 GB storage; *"metered on a per app basis"*, *"no SLA"*,
  *"not supported"* for production, and Free/Shared *"can't scale out"*. Exceed the daily
  allowance and App Service **stops the app** until the quota resets — the tell is
  `az webapp show --query usageState` reading `Exceeded`, which no ordinary dashboard watches.
  ⚠️ Day 101 leaves **two questions for whoever runs it**: (a) whether the `adk` console script is
  on `PATH` in Oryx's build environment (the doc gives the log-stream diagnostic plus a
  `PYTHONPATH=/home/site/wwwroot` fallback), and (b) §6's deliberate experiment —
  **does F1 accept a custom container at all?** `03_azure.md` §5 pairs `--sku F1` with
  `--deployment-container-image-name`, while every Microsoft quickstart specifies **B1**. Day 101
  routes the real deployment through F1 **code deploy** (unambiguously supported) and treats the
  container question as a recorded experiment. **Its answer determines whether `03_azure.md` §5
  needs correcting.**
- **Day 101 decision — Azure Functions documented and declined, on shape not cost.** The grant is
  real (1M executions + 400,000 GB-s/month) but ⚠️ the pricing page states it applies to *paid,
  consumption subscriptions* — check `az account show` before assuming a Free Trial subscription
  qualifies. The reason not to host the agent there: per-invocation billing means paying by the
  GB-second for time spent **blocked on the model's network call**. Functions earns its place as
  an agent's *edges* (webhook receiver, timer digest, alert handler), never the agent itself.
- **Day 102 finding — ⚠️ the secret-in-tfstate answer is provider-specific, and Azure fails where
  GCP passed.** `google_cloud_run_v2_service` takes a Secret Manager **reference**, so Day 99's
  grep of `terraform.tfstate` found nothing. `azurerm_container_app`'s `secret` block takes the
  **value**, so Day 102's identical grep finds the key in plaintext. **`sensitive = true` does
  not fix this** — it redacts CLI *output* only; state is plaintext JSON of every managed
  attribute. Day 102 §5 makes the reader run both greps and compare. **Day 105 must re-ask the
  same question for `aws_lambda_function`'s inline `environment` block and record the answer** —
  do not assume it matches either previous result.
- **Day 102 also records:** `provider "azurerm"` requires a mandatory-even-when-empty
  `features {}` block; `azurerm_container_app` requires a `traffic_weight` block (no default);
  and ⚠️ AKS provisions a **second, hidden `MC_<rg>_<cluster>_<region>` resource group** holding
  node VMs, disks, and a load balancer — so `az group delete` on the group you know about is not
  automatically sufficient. Teardown checks must query `az group list --query "[?starts_with(name,'MC_')]"`.
- **Day 103 finding — ⚠️ `04_aws.md` §4 is wrong**, and this is the sharpest correction in the
  track so far. It calls an HTTP-serving Dockerfile "the natural fit" for Lambda. It is not:
  *"The container image must implement the Lambda runtime API"*
  (`docs.aws.amazon.com/lambda/latest/dg/images-create.html`). Lambda is a **pull** model — the
  process must call out to `$AWS_LAMBDA_RUNTIME_API` for events — so `adk api_server` starts,
  looks healthy, and times out on **every** invocation because nothing ever connects to its
  socket. The bridge is the **AWS Lambda Web Adapter 1.0.1** as a `/opt/extensions/` extension,
  with `AWS_LWA_PORT=8000` (its default is 8080 — omitting this reproduces the identical timeout).
  Day 103 deploys the broken version **on purpose** as its failure lab. New file:
  `Dockerfile.lambda`, three lines different from `Dockerfile.adk`.
- **Day 103 finding — Lambda's registry cannot be swapped, and it is not free.** Lambda pulls
  function images only from **private ECR**, same region — not `ghcr.io`, not Docker Hub, and
  **not ECR Public** (whose 50 GB always-free grant covers *public* repos only). Private ECR is
  500 MB/month **for one year**, then $0.10/GB-month — and post-2025-07-15 accounts never get
  that year. Verdict: **Lambda compute is free; deploying to Lambda is a few cents/month.**
  Day 103's rule is create-use-delete in the same session, and ⚠️ **teardown order is
  function-first, repository-second** (deleting the image under a live function makes it `Failed`).
  ⚠️ **Day 105 points Terraform at the same ECR image** — decide whether Day 105 re-runs Day 103's
  build steps or keeps the repo alive across the two days, because it changes whether
  "delete same session" survives the day boundary.
- **Day 103 also records:** Lambda's binding meter is **GB-seconds, not requests** — at 512 MB and
  ~5 s per agent request, 400,000 GB-s ≈ **160,000 requests**, about a sixth of the 1M headline.
  ⚠️ The usual "raise memory so CPU scales up" advice does **not** apply, because the seconds are
  network wait. Also: read-only filesystem except `/tmp` (so Day 98's SQLite trick cannot port);
  single-architecture images only (build with `--provenance=false` or buildx attestations make it
  look multi-arch); default timeout is **3 s** and must be raised; and a function not invoked for
  weeks goes `Inactive` and **rejects its first invocation** before working on retry.
- **Day 104 — re-scoped to 🅿️ parked, and the reason is a second AWS charge nobody flagged.**
  Beyond the 2025-07-15 credit change below, ⚠️ **public IPv4 costs $0.005/hour with no free
  allowance** — *"the price is the same whether… in-use… or an idle public IPv4 address"*
  (`aws.amazon.com/vpc/pricing/`, 2026-08-21). That is **~$3.65/month**, and it applies **even to
  a legacy account whose instance-hours are free**. Conclusion: **no AWS account vintage yields a
  $0 internet-reachable VM.** Day 104 is therefore rewritten as the track's **cost-anatomy day** —
  an EC2 instance is **four meters** (instance hours, EBS volume, public IPv4, egress) and the
  phrase "free tier" only ever described the first. Day 98's `e2-micro` grant was genuinely $0
  because Google's grant names the instance, the 30 GB disk, *and* the egress; AWS's never did.
  Day 104 offers one **optional, alarm-bounded, sub-$0.10, same-session** experiment for anyone
  who wants the hands-on hour, and forbids the unbounded version.
- **⚠️ `04_aws.md` §1's table is now wrong in two ways** (recorded here; that file is outside this
  track's write scope): its "12 Months Free" rows don't apply to post-2025-07-15 accounts, and it
  has **no row at all** for the public IPv4 charge.
- **The recurring rule this track keeps rediscovering, now on three providers:** *compute meters
  bill for **running**; storage and address meters bill for **existing**.* Day 100's container
  registry, Day 103's ECR repository, and Day 104's EBS volume / Elastic IP are the same lesson in
  three disguises. **Day 110's audit should be built on this distinction**, and every earlier day
  re-read through it: what does each deployment bill for existing rather than running?
- **⚠️ Day 106 is now load-bearing for this track, not just another platform.** With Day 104
  parked, Oracle Cloud Always Free is the **only** remaining candidate for "an always-on VM
  running Sutra at genuinely $0, indefinitely." If Oracle turns out to have an equivalent hidden
  meter, this track has **no** free always-on VM, and Day 110's retro must say so plainly rather
  than let the earlier days imply otherwise.
- Every "real hands-on" day requires the human to have signed up for that specific provider and
  to have read `docs/deployment/00_stay_free_safety.md` first — each day's header says so and
  does not re-litigate the budget-alert setup, it just points there.
- If you are a future session resuming this: **do not renumber days that already have a ✅** —
  append only, same rule as every other ledger in this repo.
