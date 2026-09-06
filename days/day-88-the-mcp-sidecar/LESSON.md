---
day: 88
phase: 13
phase_name: "Observability & deployment"
title: "Kubernetes on the laptop — the MCP sidecar"
ids: ["ADK-69", "OPS-18"]
principles: [1, 2, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 15
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 88 — Kubernetes on the laptop: the MCP sidecar

> **Yesterday (Day 87):** the managed platform, written down and never billed. The Agent Engine
> configuration was authored and validated as a document, with the deploy command recorded and
> deliberately not run, because Addendum 02 forbids a billing account — after finding **five names
> for one product** in a single version, and a deploy path that reads your whole `.env` and ships
> every key in it.
> **Today:** the other end of the same idea — the system described as desired state and run on a
> cluster you own. The MCP server stops being another terminal and becomes a topology decision, and
> the decision has a security property: in one Pod it has **no cluster-visible address at all**. Then
> the failure that pattern ships with, measured for real on this machine: two processes on loopback,
> the caller dialling first, and `ConnectionRefusedError: [WinError 10061]`. The fix is three lines
> of manifest and fourteen of client, and the day's sharpest finding is that the manifest's version
> only guarantees *a process exists* unless a `startupProbe` says otherwise.
> **Tomorrow (Day 89):** Phase 14 opens with A2A v1.0 and signed Agent Cards, verified hands-on.

---

## §1 Where we are

The driver and the conductor.

Two people, two jobs, one bus. Neither could do the other's work, and neither is scheduled
separately: the depot schedules a bus, and the bus comes with its crew. When it goes in, both go in.
They talk by turning their heads, because they are in the same vehicle — no radio, nothing anybody
else can tune into.

That is a Pod, and it is the whole of today's architecture. Sutra's agent and `sutra-mcp` have been
two processes since Day 33, kept together by a human opening two terminals. A cluster removes the
human and asks the question directly: same Pod, or two Pods and a Service between them?

The answer this day argues for is the sidecar, and the reason is not convenience. In one Pod the
archive server has **no Service, no DNS name and no NetworkPolicy to get right** — there is nothing
for another Pod in the cluster to connect to, because there is no address. The split topology is a
legitimate choice and a different blast radius, and `address.py` derives both from the manifests
rather than asserting either.

Phase 13's gate is *"traced end-to-end; runs in local k8s"*, and this day was meant to close the
second clause. **It does not.** There is no `kubectl`, no `kind`, no `k3d` and no `docker` on this
machine. So the day does what a deployment day can honestly do without them: the deliverable of a
cluster deployment is a document, and the document is real, complete, and checkable. Nine properties
are asserted against it, a deliberately naive version fails seven, and eight cluster commands are
written down **unrun**, with no invented transcript anywhere.

What *is* measured for real is the failure that matters most. `race.py` starts two processes on
`127.0.0.1` — which is exactly what two containers in one Pod are — with the caller dialling
immediately and the callee binding after five seconds of startup work. It produces the operating
system's own words. And it produces a second finding nobody was looking for: at a one-second timeout
the same race reports `TimeoutError: timed out`, which sends an engineer to look for a network
problem on a loopback address inside one Pod.

---

## §2 The map

Five sections. Section 1 is what a cluster is told and why it is a document. Section 2 is the sidecar
decision and its two-sided security property. Section 3 is the nine properties the manifest must
have. Section 4 is the startup order nobody promised. Section 5 is what did not run, and what a real
deployment adds.

### 1 — What the cluster is told

*Desired state, the Pod, and the file that is the deployment.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Adjectives, not verbs](parts/01-what-the-cluster-is-told/1.1-adjectives-not-verbs.md) | Why a mistake stops being an event and becomes a condition | `foundation` |
| 1.2 | [The Pod is the unit, not the container](parts/01-what-the-cluster-is-told/1.2-the-pod-is-the-unit.md) | Four shared facts, and the one that decides the whole day | `foundation` |
| 1.3 | [The document is the artifact](parts/01-what-the-cluster-is-told/1.3-the-document-is-the-artifact.md) | Three layers of manifest checking, and which one needs a cluster | `working` |

### 2 — The sidecar decision

*One Pod or two, what that decides, and what it costs.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One Pod or two](parts/02-the-sidecar-decision/2.1-one-pod-or-two.md) | Address, failure, scaling and upgrade — all from one fact | `working` |
| 2.2 | [The address is the boundary](parts/02-the-sidecar-decision/2.2-the-address-is-the-boundary.md) | No Service means nothing to misconfigure — and the direction nobody checks | `production` |
| 2.3 | [What the sidecar costs](parts/02-the-sidecar-decision/2.3-what-the-sidecar-costs.md) | Every limitation from one shared thing, and the expiry condition | `working` |

### 3 — What the manifest must say

*Nine properties, and the checker that asserts them.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Checking what the cluster would read](parts/03-what-the-manifest-must-say/3.1-checking-what-the-cluster-would-read.md) | 💥 The check that passed on an empty set, and the third outcome that fixes it | `working` |
| 3.2 | [The PIN on the back of the card](parts/03-what-the-manifest-must-say/3.2-the-pin-on-the-back-of-the-card.md) | `value` against `valueFrom`, and two things people get wrong about Secrets | `working` |
| 3.3 | ["The usual"](parts/03-what-the-manifest-must-say/3.3-the-usual.md) | Why `latest` has no rollback, and why `Never` is the safer pull policy | `working` |
| 3.4 | [The whistle and the limit](parts/03-what-the-manifest-must-say/3.4-the-whistle-and-the-limit.md) | Three probes, two of which people collapse into one | `working` |

### 4 — The order nobody promised

*The startup race, measured, and the two halves of the fix.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The clinic was not open yet](parts/04-the-order-nobody-promised/4.1-the-clinic-was-not-open-yet.md) | 💥 Running is not listening — and the timeout decides which error you see | `production` |
| 4.2 | [Redial](parts/04-the-order-nobody-promised/4.2-redial.md) | Seven attempts, and the deadline people leave out | `working` |
| 4.3 | [What Kubernetes actually promises](parts/04-the-order-nobody-promised/4.3-what-kubernetes-actually-promises.md) | The guarantee is real and, by default, nearly empty | `production` |

### 5 — What did not run

*The honest inventory, and the distance to something operable.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Taught on dry land](parts/05-what-did-not-run/5.1-taught-on-dry-land.md) | Six things measured, eight commands unrun, and no invented transcript | `production` |
| 5.2 | [The first night in a new house](parts/05-what-did-not-run/5.2-the-first-night-in-a-new-house.md) | Nine items, three of which take about twenty minutes | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [Labels over hierarchies](papers/01-labels-over-hierarchies.md) | `doi:10.1145/2890784` — the Pod and the label selector, and why they were chosen. The demo answers four questions with labels and two of four with a tree; a third arm adds one service and shows the tree's correct answer quietly becoming a smaller one, with no error |

---

## §3 Setup — run this

```bash
mkdir -p days/day-88-the-mcp-sidecar/lab/k8s
mkdir -p days/day-88-the-mcp-sidecar/lab/papers/pods-and-labels
cd days/day-88-the-mcp-sidecar/lab
touch _manifests.py check.py address.py race.py serve.py gate.py
touch k8s/deployment.yaml k8s/deployment-naive.yaml k8s/deployment-split.yaml
touch papers/pods-and-labels/workloads.yaml papers/pods-and-labels/select.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
`pyyaml==6.0.3` is already present as an ADK dependency, and everything else is the standard library.

**What each file is for:**

- `k8s/` holds three real manifests, and they are the day's actual deliverable: `deployment.yaml` is
  the sidecar topology, `deployment-naive.yaml` is the same intention written fast, and
  `deployment-split.yaml` is the two-Deployment alternative with the Service it forces.
- `_manifests.py` loads them the way `kubectl apply -f` would, and classifies each container as an
  app container, a sidecar or an ordinary init container.
- `check.py` is the nine properties; `address.py` derives the address and the blast radius from the
  topology.
- `serve.py` is a process that exists before it is listening, and `race.py` is the agent that does or
  does not wait for it. These two are the day's real measurement.
- `gate.py` is the day's eval against `deploy/k8s/`, which is the build brief.
- `papers/pods-and-labels/` holds the paper's demo: twelve workloads described twice, and nothing
  else.

`race.py` starts a child process. Confirm it cannot outlive the run before you go further:

```bash
grep -n "DEADLINE_SECONDS" days/day-88-the-mcp-sidecar/lab/serve.py
```

**Why:**

- The child stops itself after a hard deadline **and** is terminated by the parent in a `finally`
  block. Either alone would be a way to leave a process holding port 8931 after a run you interrupted
  — which is a trap this lab would otherwise set for its own next run.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the artifact that
belongs in the product. Day 85 gave Sutra an API, Day 86 an image, Day 87 the managed-platform
walkthrough; today produces the thing a cluster is handed.

**`deploy/k8s/`** — the deployment, as documents.

- `TODO(me)`: `deployment.yaml`, carrying all nine properties from part 3.1 and the three-part sidecar
  declaration from part 4.3. The lab's version is teaching material; the product's is yours, and the
  `replicas: 1` comment naming Day 47's finding is not optional.
- `TODO(me)`: a `Namespace` object and `namespace: sutra` on every other object. Part 5.2 item 1 —
  ten lines, and it is what makes cleanup a single safe command.
- `TODO(me)`: `README.md` carrying the cold start in order — `kind create cluster`, `kind load
  docker-image`, `kubectl apply` — plus the rollback line and the Secret creation command with its
  rotation caveat. `gate.py` checks for those three strings by name.
- `TODO(me)`: the Secret is **created by a command, from `.env`**, and the command is committed while
  the Secret is not. Part 3.2 is why a base64 blob in the repository is not progress.

**`sutra/`** — two changes, both small and both load-bearing.

- `TODO(me)`: the MCP client's startup connection gets a bounded retry with a deadline — part 4.2's
  `wait_until_ready`, in the product rather than the lab. Log the attempt count; a number that creeps
  up over months is the earliest warning of a slowing dependency.
- `TODO(me)`: `/readyz` must mean *the MCP session is established and the tools are listed*, not *a
  socket is open*. Part 5.2 item 4, and it is the only item on that list that is a code change.

**`tests/test_deploy.py`**

- `TODO(me)`: the nine manifest properties, as tests over `deploy/k8s/`, so a manifest change goes
  through the same gate as a code change.
- `TODO(me)`: a test that the **naive** manifest fails. A policy checker that has never rejected
  anything is indistinguishable from one that cannot — part 3.1's review comment, as a test.
- `TODO(me)`: a test that a check with no subject reports `n/a` rather than passing. That is the bug
  part 3.1 found in this lab's own checker, and it is the third time this repository has met the
  shape.
- `TODO(me)`: extend the pin check to accept a digest reference (`image@sha256:…`), which part 3.3
  measured as a gap: the strongest possible pin is currently reported as unpinned.

**Three `TODO(me)`s that need tooling this machine does not have.** Part 5.1 lists all eight commands;
these are the three that must be run before anybody calls this day done:

- **Install `kind` (or `k3d`) and `kubectl`**, and record the versions you actually got in
  `docs/PACKAGES.md` with the date. Never write a version you have not read off the tool.
- **Run the cold start once, from the README, on a clean machine** — that is the whole of OPS-18, and
  reading the README is not the same as following it.
- **Reproduce the two Pod-level failures deliberately**: skip the image load and see
  `ErrImageNeverPull`; remove `restartPolicy: Always` and see the Pod sit in `Init:0/1`. Both are in
  part 4.3 and part 3.3 as unrun commands.

---

## §5 The eval that must be able to fail

```bash
cd days/day-88-the-mcp-sidecar/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `deploy/k8s/`, all red today because the deploy directory is the build brief. A
check that cannot run counts as a **failure**, never as skipped (Principle 11) — and note that checks
4 and 5 report *"no deploy/k8s to search"* rather than *"nothing found"*, which would have been
technically true and a vacuous pass.

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes red:

```bash
uv run python check.py; echo "exit: $?"                      # 0 — 9 of 9 properties hold
uv run python check.py --naive; echo "exit: $?"              # 1 — 1 of 9, and one n/a
uv run python address.py; echo "exit: $?"                    # 0 — the archive server has no address
uv run python address.py --split; echo "exit: $?"            # 1 — it has one, and needs a policy
uv run python race.py; echo "exit: $?"                       # 1 — ConnectionRefusedError, WinError 10061
uv run python race.py --impatient; echo "exit: $?"           # 1 — the same race, called a timeout
uv run python race.py --gate; echo "exit: $?"                # 0 — connected on attempt 7
uv run python gate.py; echo "exit: $?"                       # 1 — 0 of 6, by design
uv run python papers/pods-and-labels/select.py; echo "exit: $?"         # 0 — 4 of 4 questions
uv run python papers/pods-and-labels/select.py --off; echo "exit: $?"   # 1 — 2 of 4
uv run python papers/pods-and-labels/select.py --grow; echo "exit: $?"  # 1 — the answer shrank silently
```

Three of those belong in a pipeline, in this order: **`check.py` first**, because a manifest that
fails its properties should never reach a cluster; then `check.py --naive`, asserted to fail, because
that is what proves the checker can reject; then `gate.py`, which is the product's own artifact.

Note the pairs where the **ablation exits 0**. `race.py --gate` is the only one, and it is green
because it is the fix rather than the failure — this day's shape is the opposite of the eval phase's,
because here the honest arm is the one that succeeds. The arm to be suspicious of is `check.py` on a
manifest with no sidecar in it, which is exactly the vacuous pass part 3.1 found and fixed.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

**And zero cluster requests, because there is no cluster.** This is the day's honest boundary and it
is stated here rather than buried: `kubectl`, `kind`, `k3d`, `minikube` and `docker` are all absent
on this machine, verified on 2026-09-07. Nothing in this day was applied to a cluster, no Pod ran, and
**no `kubectl` output appears anywhere in these documents.**

What was measured for real: nine manifest properties over three real manifests; the address and blast
radius derived from two topologies; a genuine startup race between two processes on `127.0.0.1`,
producing `ConnectionRefusedError: [WinError 10061]` and, at a shorter timeout, `TimeoutError: timed
out`; a bounded retry closing it in seven attempts; and the paper's demo over twelve workloads. Every
transcript in this day came from one of those runs.

What was not: eight cluster commands, listed in full with their exact syntax in part 5.1, each marked
unrun. The Phase 13 gate's second clause — *runs in local k8s* — is therefore **not closed by this
day**, and §11 says so.

---

## §7 Traps

1. **Writing a verb where the file wants an adjective.** A wrong `replicas` is not executed once, it
   is enforced every second until somebody edits it — part 1.1.
2. **Reading only `containers:`.** A Pod's containers live in two lists, and the sidecar is in the
   other one — part 1.2.
3. **Assuming a parse is a validation.** YAML parsing catches malformed documents; only the API
   server catches a misspelled field, and that needs a cluster — part 1.3.
4. **Choosing the topology by default.** Both containers under `containers:` is a decision about
   address, scaling, failure and upgrade, made without noticing — part 2.1.
5. **Thinking the Pod boundary replaces authorisation.** Topology removes reachability, not
   authority; the agent can still call every port the sidecar opens, with no credential — part 2.2.
6. **A sidecar decision with no expiry condition.** *"At scale"* is not an observation; *"when a
   second consumer needs the archive"* is — part 2.3.
7. **A check that passes on an empty set.** *"Every sidecar has a startupProbe"* is true of a manifest
   with no sidecars, and counting that as a pass is the third time this repository has met the shape
   — part 3.1.
8. **A credential as a literal.** `value:` puts it in the repository forever; `valueFrom.secretKeyRef`
   puts a pointer there instead — part 3.2.
9. **`latest`, and the pull policy that follows it.** An unpinned tag has nothing to roll back to, and
   an untagged image means `latest` silently — part 3.3.
10. **Liveness where readiness belonged.** Restarting a container that was merely busy, at exactly the
    moment restarting makes things worse — part 3.4.
11. **Believing the error you were given.** The same startup race reports `ConnectionRefusedError` or
    `TimeoutError` depending on a number you chose — part 4.1.
12. **A retry with no deadline.** It converts a loud failure into a process that runs forever, doing
    nothing, in a Pod that never becomes ready — part 4.2.
13. **Trusting the ordering guarantee as written.** Without a `startupProbe`, *started* means a
    process exists — part 4.3.
14. **Pasting a transcript nobody produced.** There is no cluster here, and every unrun command says
    so — part 5.1.

---

## §8 Verify before you code

Fetched on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| Kubernetes sidecar containers | <https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/> | sidecars are init containers with `restartPolicy: Always`; **stable since v1.33**, first available in **v1.28**, on by default since **v1.29**, feature gate now locked |
| The `started` condition | same page | *"That status either becomes true because there is a process running in the container and no startup probe defined, or as a result of its `startupProbe` succeeding."* |
| Init container messaging | same page | *"Init containers stop before the main containers start up, so init containers cannot exchange messages with the app container in a Pod."* |
| Paper record | <https://api.crossref.org/works/10.1145/2890784> | *Borg, Omega, and Kubernetes*, Communications of the ACM 59(5), 2016, pp. 50–57 |

**Local tooling verified on 2026-09-07**, because the day's honesty depends on it: `docker`,
`kubectl`, `kind`, `k3d` and `minikube` all report as absent; `curl 8.19.0` is present;
`pyyaml==6.0.3`, `httpx==0.28.1`, `fastapi==0.141.1` and `uvicorn==0.52.4` are installed as ADK
dependencies, so no package is added today.

**No new ADK symbol is used today.** That is itself worth recording: this day deploys Day 85's app and
Day 86's image without touching either, and if it had needed a code change in `sutra/` that would
have been a finding rather than a chore. The two `sutra/` items in §4 are consequences of the
*cluster*, not of ADK.

**The 1.x → 2.x trap this day pays for is ADK-73** — every model pinned explicitly. Its deployment
analogue is part 3.3: an unpinned image tag is the same defect one layer down, and the manifest pins
both containers by tag with a `TODO(me)` to move to digests.

---

## §9 Say it in an interview

*"We had an agent and its MCP server as two processes, and moving to Kubernetes forced a decision
we had been avoiding: same Pod or two Pods. We took the sidecar, and the reason was security rather
than convenience — in one Pod the MCP server has no Service, so it has no DNS name and no cluster IP,
which means there is no NetworkPolicy to get right. A capability that does not exist cannot be
misconfigured. The honest other half is that the agent then has unauthenticated access to it forever,
because they share a loopback interface, so the tool allowlist is still doing real work. Then we hit
the failure that pattern always ships with. Containers in a Pod start together, and our agent
connects to the MCP server at boot, so it dials a process that exists and has not called bind yet. We
reproduced it with two local processes and got connection refused — and the thing I did not expect
was that at a one-second client timeout the same race reports a timeout instead, because the kernel
takes longer than that to surface the reset. Two names for one failure, and one of them sends you
looking for a network problem on loopback. The fix is two halves: a bounded retry with a deadline in
the client, and, in the manifest, declaring the sidecar as an init container with `restartPolicy:
Always`. That second one has a trap in the documentation worth reading twice — the kubelet marks a
sidecar started when there is a process running and no startup probe defined, so without a
`startupProbe` the ordering guarantee is real and almost empty. We wrote nine manifest properties as
a checker and kept a deliberately bad manifest in the repository that the pipeline asserts fails,
because a policy checker that has never rejected anything is indistinguishable from one that cannot."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 88` refuses to commit until they are.

The day is finished when you can look at a Pod manifest and say, without running anything, where each
container will be reachable from, what happens if one of them is slow to start, and which of its
properties a cluster would accept without comment and a reviewer should not.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 88 | 2026-09-07 | ADK-69, OPS-18 | 15 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it is the verdict rather than a formality. `./m depth` is green over this
day and every measurement in it was run. What is not green: **Phase 13's gate says *"traced
end-to-end; runs in local k8s"* and the second clause is not closed.** There is no `kubectl`, no
`kind`, no `k3d` and no `docker` on this machine, verified 2026-09-07, so no manifest in this day has
ever been applied to a cluster and no Pod has ever run. Eight cluster commands are written out unrun
in part 5.1, and no `kubectl` output appears anywhere in the day. Two findings carry forward: the
deploy artifact `deploy/k8s/` does not exist yet and `gate.py` reports 0 of 6 by design, and the
checker's own vacuous-pass bug — a property that held over an empty set — is the third time this
repository has met that shape, after Day 79 and Day 83.

**`docs/PACKAGES.md`** — no new rows today. Two rows are owed once the tooling is installed: the
`kind` (or `k3d`) version and the `kubectl` version, each read off the tool rather than remembered,
each with the date.

**`docs/PAPERS.md`** — one new row:

```text
| Borg, Omega, and Kubernetes | doi:10.1145/2890784 | 2016 | 2026-09-07 | 88 | `days/day-88-the-mcp-sidecar/papers/01-labels-over-hierarchies.md` |
```

The title, journal, volume, issue and pages were copied from
`api.crossref.org/works/10.1145/2890784` on 2026-09-07 — the record, not the memory (§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**What Phase 14 inherits.** Phase 13 closes here, and it hands over three things. The tracing from
Day 84 works and is the half of the gate that is closed. The deployment exists as a checked document
and has never run, which is the half that is not. And the sidecar's security property — no
cluster-visible address — is the assumption Day 89's A2A work will immediately press on, because
agent-to-agent means external callers, and the first question they raise is which of Sutra's internal
services are addressable. Today's answer is *none*, deliberately, and part 2.3 wrote down the
condition under which that has to change.

**Commit:**

```text
day 88: kubernetes on the laptop - the mcp sidecar - closes ADK-69, OPS-18
```
