# 00 · Stay-free safety checklist — read this before any cloud command

> **Read this file before you run a single command from [02_gcp.md](02_gcp.md),
> [03_azure.md](03_azure.md), [04_aws.md](04_aws.md), or [05_terraform.md](05_terraform.md).**
> Every command in those files is written to stay inside a free allowance, but "free tier"
> is a *quota*, not a *hard stop* — every major provider's default behavior, if you cross the
> quota, is to **keep running and bill you**, not to shut off. This file is the guardrail that
> makes that survivable.

---

## 1 · The one sentence to internalize

**A cloud "free tier" means "this specific quota costs $0 until you exceed it." It does not
mean "this account cannot be charged."** Only three things actually guarantee $0, ever:
not attaching a card at all (`kind`/`k3d`/`minikube`/Docker Compose, [01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md)),
a provider budget **hard cap** that disables billing when reached (rare — most "budgets" are
alert-only, see §3), or deleting/destroying the resource before its free window ends.

## 2 · Before you create *anything* on GCP, Azure, or AWS — do these four things, in order

1. **Set up billing/cost alerts first, on the billing account itself, before creating any
   resource.** Not after. An alert that fires after the spend already happened is a
   notification, not a guardrail — but it is still far better than nothing, and it is the
   only thing standing between a mistake and a bill you don't find out about for a month.
2. **Write down the free quota you intend to stay under**, in the units the provider bills in
   (vCPU-seconds, request count, instance-hours) — not "it's free," but the actual number, so
   you can compare it against what you observe in step 4.
3. **Prefer `scale-to-zero` / `min-instances=0` wherever the platform offers it.** A serverless
   container that scales to zero when idle only bills for the seconds it actually ran. A VM
   left running 24/7 bills 24/7 whether you use it or not — this is the single most common way
   a "free tier" experiment turns into a bill.
4. **Calendar the expiry date of anything that is time-limited** (a 30-day credit, a 12-month
   free-tier clock) the day you create it. Set a reminder several days before, not on the day.

## 3 · Budget alerts, provider by provider

⚠️ These are **alerts**, not caps, on all three providers by default — they email/notify you
past a threshold; they do not stop the resource from running or the bill from accruing unless
you additionally wire the alert to an automated shutoff (possible, but its own project). Set
them anyway: a surprised human who gets an email on day 2 of a mistake is much better off than
one who finds out on the invoice 28 days later.

**GCP** — budgets are billing-account-scoped, created once, cover everything under that account:

```powershell
# List billing accounts to get the ID this budget attaches to.
gcloud billing accounts list

# Create a budget with alert thresholds at 50%, 90%, and 100% of a $5 ceiling.
# ⚠️ Confirm exact flags with `gcloud billing budgets create --help` — the Budgets API
# has changed shape before, and this command was not executed in this session.
gcloud billing budgets create `
  --billing-account=BILLING_ACCOUNT_ID `
  --display-name="zero-spend-guard" `
  --budget-amount=5 `
  --threshold-rule=percent=0.5 `
  --threshold-rule=percent=0.9 `
  --threshold-rule=percent=1.0
```

| Flag | What it does |
| --- | --- |
| `--billing-account` | which account this budget watches — one budget does not automatically cover every account you have |
| `--budget-amount=5` | the ceiling in the account's currency; set it low ($5–$10) for a learning project so an alert fires almost immediately if anything unexpected bills |
| `--threshold-rule=percent=…` | repeatable; each one is a separate email trigger at that fraction of the ceiling |

Console alternative (no CLI syntax to get wrong): **Billing → Budgets & alerts → Create
budget**, same three numbers.

**AWS** — budgets are account-scoped via the Budgets service; the CLI needs two JSON files:

```powershell
# budget.json
@'
{
  "BudgetName": "zero-spend-guard",
  "BudgetLimit": {"Amount": "5", "Unit": "USD"},
  "TimeUnit": "MONTHLY",
  "BudgetType": "COST"
}
'@ | Out-File -Encoding utf8 budget.json

# notifications.json — who gets emailed and at what percentage
@'
[
  {
    "Notification": {"NotificationType": "ACTUAL", "ComparisonOperator": "GREATER_THAN", "Threshold": 80},
    "Subscribers": [{"SubscriptionType": "EMAIL", "Address": "you@example.com"}]
  }
]
'@ | Out-File -Encoding utf8 notifications.json

# ⚠️ Confirm exact flags with `aws budgets create-budget help` — not executed this session.
aws budgets create-budget --account-id 123456789012 `
  --budget file://budget.json `
  --notifications-with-subscribers file://notifications.json
```

| Field | What it does |
| --- | --- |
| `BudgetType: COST` | tracks dollars spent, not usage units — the simplest kind for a guardrail |
| `TimeUnit: MONTHLY` | resets the tracked amount every calendar month |
| `Threshold: 80` | fire at 80% of the $5 ceiling — tune this down for a smaller, faster warning |

Console alternative: **Billing and Cost Management → Budgets → Create budget → Zero spend
budget** — AWS ships an actual one-click "alert me the instant *anything* bills" template,
which is the closest any of the three gets to a true zero-spend tripwire.

**Azure** — budgets attach to a subscription:

```powershell
# ⚠️ Confirm exact flags with `az consumption budget create --help` — not executed this session.
az consumption budget create `
  --budget-name "zero-spend-guard" `
  --amount 5 `
  --time-grain Monthly `
  --start-date 2026-08-01 `
  --end-date 2027-08-01 `
  --category cost
```

Console alternative: **Cost Management + Billing → Budgets → Add**, same numbers. Azure also
lets a **free trial account** be capped so it *cannot* convert to pay-as-you-go without an
explicit upgrade — leaving that default in place is itself a safety control; don't switch to a
paid subscription type until you mean to.

**Oracle Cloud** — the Always Free resources genuinely bill $0 by design (they are excluded from
metering, not just quota-limited), so there is no equivalent budget step for the Always Free
VMs themselves. If you ever add a paid resource on the same tenancy, Cost Management → Budgets
exists there too.

## 4 · After every hands-on cloud experiment — the cleanup checklist

Run this the same session you finish testing, not "later":

- [ ] `terraform destroy` if you used Terraform for the resource ([05_terraform.md](05_terraform.md) §5)
- [ ] Delete the specific compute resource by hand if you didn't use Terraform:
      `gcloud run services delete …` / `az containerapp delete …` / `aws lambda delete-function …`
      / stop **and terminate** (not just stop) any VM instance
- [ ] Check for orphans the resource may have created silently: reserved/static public IPs,
      persistent disks/volumes, load balancers, NAT gateways, DNS zones — **these often survive
      deleting the compute resource itself** and are the most common source of a surprise bill
      on an otherwise-free project (§5)
- [ ] Re-run `kind get clusters` / `k3d cluster list` / `docker ps -a` locally and remove test
      clusters/containers you no longer need — free, but they consume laptop disk and RAM
- [ ] Confirm no secret, `.tfstate` file, or key ended up committed (`git status`, same rule as
      the rest of this repo)

## 5 · Resources that are rarely free, on any provider, regardless of what got you there

The trap is never the VM or the function — it's the thing next to it that a tutorial didn't
mention:

| Resource | Why it slips past "I used the free tier" | What to do instead |
| --- | --- | --- |
| **Load balancers** (any provider's L4/L7 LB) | Billed hourly *and* per GB processed, almost never inside a free tier, even when every backend behind it is free | Use the free tier's own front door directly (Cloud Run/Container Apps URL, `kubectl port-forward`, or a `ClusterIP` Service — Day 88's exact choice) |
| **NAT gateways** (AWS especially) | ~$0.045/hour **plus** per-GB data processing — one of the most notorious "surprise bill" line items in all of AWS | Don't provision one for a learning project; keep instances in a public subnet with a security group instead, or skip networking that needs egress-without-a-public-IP entirely |
| **Reserved/static public IP addresses left unattached** | GCP and AWS both charge for a reserved IP that is *not* currently attached to a running resource (attached-and-running is sometimes free; idle-and-reserved is not) | Release/deallocate the IP the moment you delete the resource it was for |
| **Managed Kubernetes *nodes*** (any of the three) | The control plane fee is waived (GCP/Azure) or flat ($0.10/hr, AWS) — but node VMs are ordinary compute, billed normally, and people read "control plane free" as "cluster free" | Use `kind`/`k3d` locally instead (Day 88's choice) unless you have a specific reason to need a real managed cluster |
| **Secrets managers** (AWS Secrets Manager, Azure Key Vault premium ops) | Small per-secret/per-operation charges that a "the compute is free" mental model forgets entirely | Prefer the tier's genuinely free config path: AWS **SSM Parameter Store** (standard parameters are free) over Secrets Manager; Kubernetes `Secret` objects (free, though only base64-encoded — see Day 88's note) over a managed vault, for a learning project |
| **Snapshots and backups accumulating silently** | A daily automatic snapshot policy left on after you delete the source volume keeps billing for the snapshots | Check the snapshot/backup list explicitly during cleanup, not just the primary resource list |
| **DNS hosted zones** (e.g. Route 53) | A small flat monthly fee per hosted zone, independent of traffic | Use the platform's own generated hostname (`*.run.app`, `*.azurecontainerapps.io`, the Lambda Function URL) instead of a custom domain for a learning project |
| **Data egress past the free monthly allowance** | Every provider's free egress allowance is modest (roughly 1 GB/month order of magnitude) and none of it applies to inter-region or internet-bound traffic beyond that | Keep test traffic small; a handful of manual `curl` requests for a demo will never come close, but a load test will |

## 6 · If you only remember one thing from this file

**Before you create the resource, know two numbers: the free quota (in the provider's own
units) and the date anything time-limited expires. After you finish testing, delete the
resource the same day — including its neighbors from §5.** Everything else in this folder is
detail in service of that one habit.
