# 07 · Free managed databases and frontend extras

> Verified 2026-08-21 against each provider's own pricing page (linked per section). This file
> exists because every compute option in [02_gcp.md](02_gcp.md)/[03_azure.md](03_azure.md)/
> [04_aws.md](04_aws.md)/[06_other_free_platforms.md](06_other_free_platforms.md) that scales to
> zero or restarts also **loses local disk state** — a SQLite file on Cloud Run, Container Apps,
> Lambda, or a Render free instance does not reliably survive a restart. An agent that needs to
> remember anything across restarts needs a database that lives *outside* the compute.

---

## 1 · Why this matters for an agent specifically

Sutra's own design (Days 47, 62, 63) uses local SQLite files for sessions, approvals, and
write-idempotency — which works great on a laptop or a VM with a persistent disk
([01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md),
[02_gcp.md](02_gcp.md) §5's `e2-micro`, [06_other_free_platforms.md](06_other_free_platforms.md)
§1's Oracle Always Free VM) but **breaks silently** the moment compute scales to zero or runs on
more than one replica (exactly what [day_088.md](../days/day_088.md) §5's failure lab
demonstrates for Kubernetes specifically). If your deployment target is serverless
(Cloud Run, Container Apps, Lambda, Render), plan for a real external database from the start
rather than discovering the gap the way that failure lab does.

## 2 · Neon — serverless Postgres, free forever, no card

**Verified 2026-08-21, `neon.com/pricing`:** *"The Free plan is permanent (not a trial); no
credit card required."*

| Free grant | Amount |
| --- | --- |
| Compute | 100 CU-hours/project/month (1 CU ≈ 4 GB RAM + CPU + SSD; scale-to-zero after 5 min idle, so idle time is $0) |
| Storage | 0.5 GB/project |
| Egress | 5 GB/project/month |
| Projects | up to 100 |
| Branches | 10/project (Postgres branching — a full copy-on-write clone of your schema+data for testing) |
| Auth | up to 60,000 monthly active users (Neon Auth) |

*"What happens when I hit Free plan limits? Hitting any Free monthly limit … suspends compute
until the next billing month"* — i.e., Neon **pauses rather than silently bills you**, which is
one of the safer failure modes in this entire folder.

**Try without signing up at all:** `neon.new` ("Claimable Postgres") provisions an instant
Postgres database with no signup and no card, lasting 72 hours — claim it into an account
before it expires to keep it, otherwise it's deleted automatically.

```powershell
npx neon-new --yes    # provisions a temporary, unclaimed Postgres instance
```

## 3 · Supabase — Postgres + Auth + Storage + Edge Functions, free tier (with a catch)

**Verified 2026-08-21, `supabase.com/pricing`:**

| Free grant | Amount |
| --- | --- |
| Database | 500 MB (shared CPU, 500 MB RAM) |
| API requests | Unlimited |
| Monthly active users (Auth) | 50,000 |
| File storage | 1 GB |
| Egress | 5 GB + 5 GB cached |
| Edge Function invocations | 500,000/month |
| Realtime | 200 concurrent connections, 2,000,000 messages/month |

⚠️ **The catch, stated on their own pricing page:** *"Free projects are paused after 1 week of
inactivity. Limit of 2 active projects."* Unlike Neon (pauses only *compute usage*, keeps the
project alive), a Supabase free project needs manual un-pausing from the dashboard after a
week of no traffic — fine for active development, not for an unattended demo that needs to
answer requests after a week of silence.

**A genuinely-free-forever alternative that avoids the pause entirely:** Supabase is
open-source and self-hostable via Docker — run the whole stack (Postgres + Auth + Storage +
Studio) on the same Always-Free VM from
[06_other_free_platforms.md](06_other_free_platforms.md) §1 (Oracle) or
[02_gcp.md](02_gcp.md) §5 (GCP `e2-micro`):

```powershell
git clone --depth 1 https://github.com/supabase/supabase
cd supabase/docker
Copy-Item .env.example .env
docker compose up -d
```

## 4 · Upstash — serverless Redis, genuinely free, and a trick specifically for agents

**Verified 2026-08-21, `upstash.com/pricing`:**

| Free grant | Amount |
| --- | --- |
| Max data size | 256 MB |
| Bandwidth | 10 GB/month |
| Commands | 500,000/month |
| Databases | up to 10 |

No card is required for the Free tier — *"Once you enter your credit card, your database will
be upgraded to the pay-as-you-go plan"* implies the free tier itself never asks for one.

**Notable finding: Upstash offers an instant, no-signup Redis instance specifically aimed at
coding agents.** Their pricing page includes this as a documented, intentional feature (not
something discovered by accident):

```powershell
# Provisions a temporary Redis DB, no signup, no API key. Unclaimed DBs are deleted after 3 days.
curl -X POST https://upstash.com/start-redis -H "User-Agent: your-agent-name"
```

This is useful for a quick "does my agent's caching layer work at all" test without setting up
an account first — claim the database via the console URL in the response before the 3-day
window if you want to keep it. (This folder mentions the command for your own reference; it was
not invoked as part of writing this guide, since no live resource was needed to document it.)

**Pay-as-you-go safety net:** Upstash's paid tier supports a hard **budget cap** — *"If your
usage exceeds the budget cap, your database will be rate limited and your total cost will not
exceed the chosen budget"* — one of the only genuinely hard (not just alert-based) spending caps
found across every provider in this folder. Not relevant on the Free tier itself, but worth
knowing if you ever outgrow it.

## 5 · MongoDB Atlas M0 — the document-database equivalent (⚠️ recalled, verify before relying on it)

Not fetched live this session; long-stable, widely documented: MongoDB Atlas's **M0** shared
cluster tier is free with no time limit, offering roughly 512 MB storage, shared RAM/vCPU, on a
shared multi-tenant cluster. Confirm current exact numbers and any account/card requirement at
`mongodb.com/pricing` before relying on this.

## 6 · Vercel — frontend hosting and edge functions, free "Hobby" tier

**Verified 2026-08-21, `vercel.com/docs/plans/hobby`:**

| Free grant | Amount |
| --- | --- |
| Edge Requests | up to 1,000,000 |
| Function invocations | 1,000,000 |
| Active CPU | 4 CPU-hours |
| Provisioned memory | 360 GB-hours |
| Max function duration | 300s (5 minutes) |
| Projects | 200 |

⚠️ **Restriction stated directly on the page:** *"the Hobby plan restricts users to
non-commercial, personal use only."* Fine for a portfolio/demo deployment of an agent's chat
UI; not licensed for anything commercial. No card is required to start on Hobby.

**Best fit in this folder's context:** host a small frontend (a chat UI calling out to an
agent backend) on Vercel's free tier, with the actual agent compute running on
[02_gcp.md](02_gcp.md)/[03_azure.md](03_azure.md)/[04_aws.md](04_aws.md)'s free container/function
options — Vercel's own Functions are not a fit for a persistent Python/Docker agent process.

## 7 · Summary table — picking a free data layer

| Need | Pick | Why |
| --- | --- | --- |
| Relational data (sessions, tickets, approvals — Sutra's own shape), no card, won't pause | **Neon** | Only genuinely-forever free Postgres in this file with no inactivity pause and no card requirement |
| Relational data + built-in Auth/Storage/Edge Functions in one product | **Supabase** | More batteries included, at the cost of a 1-week-inactivity pause on the free tier (or self-host to remove the pause entirely) |
| A cache or short-lived key-value store in front of an agent (rate-limit counters, session cache) | **Upstash Redis** | Free, no card, and has the fastest "try it right now" path of anything in this folder |
| Document storage matching a Mongo-shaped data model | **MongoDB Atlas M0** | ⚠️ verify current numbers first (§5) |
| A demo frontend in front of a backend hosted elsewhere | **Vercel Hobby** or **Cloudflare Pages** (§[06_other_free_platforms.md](06_other_free_platforms.md) §5) | Free, but Vercel's Hobby tier is explicitly personal-use-only |
