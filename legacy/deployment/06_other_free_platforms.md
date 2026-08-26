# 06 · Other free platforms — Oracle Cloud, Render, Hugging Face, Cloudflare, and tunnels

> Verified 2026-08-21 against each platform's own docs (linked per section). This file also
> records one important negative finding: a platform commonly recommended as "free" that no
> longer is, as of this research (§4).

---

## 1 · Oracle Cloud Always Free — the most generous permanent free compute of the major clouds

**Verified 2026-08-21, `oracle.com/cloud/free`:**

| Instance type | Free grant |
| --- | --- |
| **AMD Compute Instance** | 2 VMs, each 1/8 OCPU + 1 GB memory — Always Free |
| **Arm Compute Instance (Ampere A1)** | "Arm-based Ampere A1 cores and 12 GB of memory usable as 1 VM or 2 VMs — Always Free — 1,500 OCPU hours and 9,000 GB hours per month" |

⚠️ The Arm figure above is quoted **exactly** as fetched. It is commonly reported elsewhere
(and in Oracle's own past marketing) as "up to 4 OCPUs and 24 GB RAM total, split across up to
4 VMs" — roughly double what this specific fetch shows for a single catalog card. This may mean
the current page displays one of two Arm entries, or the headline figure has changed.
**Confirm the exact current Arm allocation in the OCI Console (Governance → Limits, Quotas and
Usage) after signup, before building on a specific number** — this is exactly the kind of
figure Principle 7/8 says to verify live rather than carry forward from memory.

Also note: **unlike AWS's 12-months-free EC2 or GCP/Azure's $300/$200 signup credits, Oracle's
Always Free compute has no 12-month clock** — it is the only one of the four providers in this
folder where "run a small Linux VM 24/7, indefinitely, for $0" is actually the intended,
supported use case rather than an edge case of a time-limited trial.

**Setup:**

```powershell
# No CLI install needed to create the VM — done via the OCI Console (a browser-based wizard):
# 1. Sign up at oracle.com/cloud/free (a card is required for identity verification only;
#    Always Free resources are excluded from metering, not just quota-limited).
# 2. Console → Compute → Instances → Create instance.
# 3. Choose "Ampere" shape, "VM.Standard.A1.Flex", and set OCPU/memory within the free pool.
# 4. Choose "Always Free eligible" image (Console labels these explicitly).
# 5. Add your SSH public key, create.
```

Once running, treat it exactly like the GCP `e2-micro` VM in [02_gcp.md](02_gcp.md) §5 — SSH
in, install Docker, run the container:

```powershell
ssh -i ~/.ssh/your_key ubuntu@<the-vm-public-ip>
# on the VM:
curl -fsSL https://get.docker.com | sh
sudo docker run -d -p 8080:8080 --env-file .env myagent:dev
```

⚠️ Oracle's default security posture blocks inbound traffic at **two layers** — the Virtual
Cloud Network's Security List *and* the instance's own `iptables`/firewalld. Both need an
explicit allow rule for port 8080, or the container runs but nothing external reaches it (the
same class of mistake as GCP's firewall rule and AWS's security group, just doubled).

## 2 · Render — genuinely free web service hosting, no card required to start

**Verified 2026-08-21, `render.com/docs/free`:**

- **750 free instance-hours/month** per workspace for a Free web service.
- **Spins down after 15 minutes of no inbound traffic**; spinning back up takes about a minute
  and shows a loading page to the connecting browser meanwhile.
- **Ephemeral filesystem** — any local file changes (a SQLite file, uploaded images) are lost on
  every redeploy, restart, *or* spin-down. Anything Sutra-shaped that writes to `data/*.db`
  locally would lose that data on Render's free tier specifically — use Render Postgres (also
  free, but expires 30 days after creation) or accept the data as ephemeral for a demo.
- Supports custom domains and managed TLS even on the Free instance type.

**Setup:** connect a GitHub repo in the Render dashboard, choose **Web Service**, select
**Free** as the instance type during creation, set environment variables (never commit them) in
the service's **Environment** tab. No `render.yaml` is required for a first deploy, though one
can pin the config as code if you want it version-controlled.

**Best fit:** a demo or portfolio deployment of an agent's UI/API where occasional cold starts
are acceptable — not a 24/7 production target.

## 3 · Hugging Face Spaces — free for static sites; **not** currently free for a Docker agent server

**Verified 2026-08-21, `huggingface.co/docs/hub/spaces-overview` — this is a finding worth
flagging, since it contradicts commonly-repeated older advice:**

> *"Static Spaces are free for everyone. Gradio and Docker Spaces run on compute and require a
> paid plan to create: PRO for personal accounts, Team or Enterprise for organizations. Free
> personal accounts in good standing can still host up to 2 Gradio Spaces running on ZeroGPU."*

What this means concretely: **a free personal Hugging Face account can no longer create a
Docker Space** (which is what a generic FastAPI-based agent server needs — Sutra's own
`sutra/api.py` shape) **without a paid PRO subscription.** The only genuinely free compute path
left is the **Gradio SDK on ZeroGPU**, capped at 2 Spaces per free account, and Gradio-specific
(not a general container). Static Spaces (plain HTML/CSS/JS) remain free for everyone but can't
run a Python agent process at all.

**Recommendation:** don't rely on Hugging Face Spaces for hosting an agent's HTTP API on a free
account. It remains a good, genuinely free option for a **Gradio UI demo in front of an agent**
(within the 2-Space ZeroGPU allowance) if the agent's compute itself lives elsewhere (e.g., the
UI calls out to a Cloud Run/Container Apps endpoint from [02_gcp.md](02_gcp.md)/[03_azure.md](03_azure.md)).

## 4 · Fly.io — flagged out: no longer a genuine free tier

**Verified 2026-08-21, `fly.io/docs/about/pricing/`:** *"All organizations (except for Linked
Organizations) require a credit card on file."* The pricing page describes only usage-based
billing (per-second compute, per-GB storage, per-GB egress) and a time-limited **Free Trial**
(a credit, not a renewing allowance) — there is no Always-Free compute grant of the kind GCP,
Azure, or Oracle offer. The smallest possible VM (`shared-cpu-1x`, 256 MB) still accrues real,
if small, per-second charges once the trial credit is spent.

**This folder does not recommend Fly.io for a zero-budget project.** It's included here only so
you don't rediscover this the hard way — Fly.io is frequently recommended in older tutorials
and blog posts as a free container host, and that appears to no longer be accurate.

## 5 · Cloudflare — free edge functions, static hosting, and tunnels (not a Python container host)

- **Cloudflare Pages** — free static site hosting with unlimited requests; good for a frontend,
  not for running a Python agent process.
- **Cloudflare Workers** — a free tier for edge functions (JavaScript/WASM, V8 isolates — not a
  general container runtime, so it cannot run `sutra/api.py` or similar directly), useful as a
  free lightweight proxy/webhook receiver in front of a "real" backend hosted elsewhere.
- **Cloudflare Tunnel** (`cloudflared`) — free, and directly useful for this folder's purposes:
  exposes a `localhost` service to the public internet without opening a router port, similar in
  spirit to ngrok:

```powershell
winget install -e --id Cloudflare.cloudflared
cloudflared tunnel --url http://localhost:8080
```

This prints a temporary `https://<random>.trycloudflare.com` URL that forwards to your laptop.
Use it for a live demo, then `Ctrl-C` — same discipline as
[01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md) §5.

## 6 · GitHub Actions / Codespaces — free compute minutes, not a deployment target

- **GitHub Actions**: unlimited minutes on **public** repositories; a monthly free-minutes grant
  on private repositories. Useful for running `make check`/`python tools/trace.py` in CI on
  every push — not a place to host a long-running agent process.
- **GitHub Codespaces**: a free monthly core-hours grant for personal accounts — a full cloud
  dev environment (effectively a free, temporary VM with a browser-based VS Code), useful for
  developing Sutra from a machine that doesn't have Docker Desktop installed, not for hosting a
  public-facing deployment.

## 7 · Tunnels, side by side

| Tool | Free tier | Best for |
| --- | --- | --- |
| **ngrok** | 1 online tunnel, random URL, session-limited | Quick one-off demos |
| **Cloudflare Tunnel** | Free, no strict account requirement for a `trycloudflare.com` URL | Same use case, no ngrok account needed |

Both expose whatever is running locally ([01_local_docker_and_kubernetes.md](01_local_docker_and_kubernetes.md))
to one other person, briefly — neither is a deployment, and neither should be left running
unattended.

## 8 · Summary table

| Platform | Genuinely free for a Docker/Python agent? | Card required? | Best use here |
| --- | --- | --- | --- |
| **Oracle Cloud (Always Free)** | ✅ Yes, indefinitely | Yes (identity check) | The closest thing to a real "runs 24/7 for $0" VM |
| **Render (Free web service)** | ✅ Yes, with cold starts + ephemeral disk | No | Low-traffic demo/portfolio deploy |
| **Hugging Face Spaces** | ⚠️ Static only; Docker needs PRO | No | A free Gradio UI (ZeroGPU, ≤2 Spaces), not the agent's backend |
| **Fly.io** | ❌ No — card required, billed per-second | Yes | Not recommended for this project |
| **Cloudflare Pages/Workers** | ✅ Yes, for static/edge-function workloads only | No | Frontend or lightweight proxy, not the agent process itself |
| **GitHub Actions/Codespaces** | ✅ Yes, for CI/dev environments | No (Actions on public repos) | CI checks, not deployment |
