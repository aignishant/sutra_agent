---
day: 86
phase: 13
phase_name: "Observability & deployment"
title: "Containerize — Cloud-Run-shaped, locally"
ids: ["ADK-66", "ADK-67", "OPS-17"]
principles: [1, 2, 7, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 86 — Containerize: Cloud-Run-shaped, locally

> **Yesterday (Day 85):** the desk got a front door — `api_server`, the FastAPI routes it
> exposes, and a written shape for what an error looks like when it leaves the process. Sutra
> stopped being a package you import and became a service something else can call: twenty-seven
> routes, three of which run the agent, and **not one of them asks for a credential**.
> **Today:** that service gets packaged into the exact shape a hosted platform would run — one
> image, configuration from the environment, a port it is told about, a health endpoint that
> answers the right question. Nothing is deployed and nothing is billed. The interesting part is
> not the Dockerfile; it is what containerising **reveals**, which is that this system is not as
> stateless as the word suggests and today is when it is measured. Two replicas, and a session
> created on one returns `404` on the other; twenty units of spend leave a shared ledger
> recording **six**.
> **Tomorrow (Day 87):** Agent Engine — a managed platform walked through in full, configuration
> written and never billed 🅿️.

---

## §1 Where we are

The recipe card that says *"cook till done"*.

It works perfectly for the person who wrote it, because they already know what done looks like,
how big their onions are and which pan they meant. None of that is on the card; it is in the
kitchen. Hand it to somebody who has never cooked the dish and only a card with measurements on
it is a recipe. The other is a reminder, and a reminder is only useful to the person who does not
need it.

Everything the desk needs in order to run is currently a reminder. A particular Python, a
particular lockfile, three settings in a `.env` that is deliberately not in git, a writable folder
chosen by accident, and a port somebody remembers. Two of those five are written down anywhere a
second machine could read.

Today writes the rest of them down, and then finds three things that were true all along and
nobody had asked about.

**Without a `.dockerignore` the build would collect 414,219,769 bytes across 22,020 files**,
including this repository's real `.env` and its `.git/config`. With one it collects forty files
and 2,207,035 bytes. That is not a build-time optimisation: a layer is written once and never
edited, so a file that reaches one is in the image for the life of the image, in every registry
and every cache that has ever pulled it.

**A liveness probe answers `200 ok` on a service that can do no work at all.** Delete the quota
ledger and `/healthz` is unchanged while `/readyz` says `503 quota_ledger_missing` — and the arm
of the measurement that consults only liveness reports a healthy service and exits `0`. That is
the fourth time this phase and the last have produced the same shape.

**And the word "stateless" does not survive being tested.** Two replicas: a session created on one
is `404` on the other, and twenty spends against a shared ledger record six. Then the ablation
inverts the obvious reading — with **one** replica the ledger still loses fifteen of twenty,
because the file race needs concurrency rather than replication, and the second replica's real
contribution is to remove the fix.

One thing this day cannot do: **there is no container runtime on this machine.** `docker` reports
`command not found`. Nothing here was built and nothing was run in a container. Every measurement
above is real and none of them needed one — but the Dockerfile is a hypothesis with good grammar,
and §6 lists exactly what has not been executed.

---

## §2 The map

Five sections. Section 1 is what an image promises and the three properties that make it odd.
Section 2 is the image contract and what is checkable without a daemon. Section 3 is
configuration arriving from outside. Section 4 is the two health questions. Section 5 is the word
"stateless", tested.

### 1 — What a container promises

*Three properties that decide everything else: reproducibility, immutability, and who chooses the
port.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [An image is a recipe a stranger can follow](parts/01-what-a-container-promises/1.1-an-image-is-a-recipe.md) | The five unwritten assumptions the desk currently runs on | `foundation` |
| 1.2 | [A layer is written once and kept forever](parts/01-what-a-container-promises/1.2-a-layer-is-written-once.md) | Why ordering decides rebuild speed, and why deleting is not deleting | `foundation` |
| 1.3 | [The platform chooses the port and the address](parts/01-what-a-container-promises/1.3-the-platform-chooses-the-port.md) | `$PORT` and `0.0.0.0` — the one place loopback is the wrong answer | `foundation` |

### 2 — The image contract

*A real Dockerfile, eight properties checkable in text, and the build context nobody looks at.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Writing the Dockerfile](parts/02-the-image-contract/2.1-writing-the-dockerfile.md) | Ordered by change frequency, with the two instructions people omit | `working` |
| 2.2 | [Eight properties, checked without a daemon](parts/02-the-image-contract/2.2-eight-properties-checked.md) | 8 of 8 for this file, 2 of 8 for one written fast | `working` |
| 2.3 | [The build context nobody looked at](parts/02-the-image-contract/2.3-the-build-context-nobody-looked-at.md) | 💥 414 MB and a real `.env`, against 40 files | `production` |

### 3 — Configuration from outside

*The environment is the private part, and "injected" has a testable meaning.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [An app that refuses to start](parts/03-config-from-outside/3.1-an-app-that-refuses-to-start.md) | Failing at import with the setting named, and the ablation that proves nothing | `working` |
| 3.2 | [Three ways a secret gets in, one of them acceptable](parts/03-config-from-outside/3.2-three-ways-a-secret-gets-in.md) | The mat, the drawer and the neighbour — and why a build argument is the drawer | `working` |
| 3.3 | [compose.yaml is the shape, not the tool](parts/03-config-from-outside/3.3-compose-is-the-shape.md) | Two services, one volume, and one number that is a confession | `working` |

### 4 — Health checks

*Two questions with different consequences, and what happens when only one is asked.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Alive and able to work are different questions](parts/04-health-checks/4.1-alive-and-able-to-work.md) | Restart against remove-from-rotation, and why a probe must be as narrow as its action | `working` |
| 4.2 | [The health check that only watched the process](parts/04-health-checks/4.2-the-check-that-only-watched-the-process.md) | 💥 `200 ok` beside `503 quota_ledger_missing`, and the arm that exits 0 | `production` |

### 5 — The word "stateless"

*Tested by replacing the process, and then by running two of it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The statefulness audit](parts/05-the-word-stateless/5.1-the-statefulness-audit.md) | Kill it and start it again: one of two kinds of state comes back | `working` |
| 5.2 | [Two replicas, and only one failure is about replication](parts/05-the-word-stateless/5.2-two-replicas-one-failure.md) | 💥 A `404` for a live session, and 20 spends recorded as 6 | `production` |
| 5.3 | [What a real deployment adds](parts/05-the-word-stateless/5.3-what-a-real-deployment-adds.md) | Nine items, three free, and the one that is a bug rather than a task | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [What isolation costs](papers/01-what-isolation-costs.md) | `doi:10.1109/ISPASS.2015.7095802` — isolation is nearly free to compute behind and charged per crossing. The demo measures a boundary at 29.3 microseconds and prices the same eight million rounds at 0.00% and 16.0% depending only on how many times they are split; the ablation removes the boundary and both collapse to zero |

---

## §3 Setup — run this

```bash
mkdir -p days/day-86-cloud-run-shaped/lab/papers/isolation
cd days/day-86-cloud-run-shaped/lab
touch _app.py config.py image.py context.py health.py replicas.py audit.py gate.py
touch Dockerfile .dockerignore compose.yaml
touch papers/isolation/boundary.py papers/isolation/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.
Everything used here — `fastapi==0.141.1`, `uvicorn==0.52.4`, `httpx==0.28.1`, `pyyaml==6.0.3` —
is already present as a dependency of `google-adk==2.7.1`, which is worth knowing rather than
assuming:

```bash
uv run python -c "import fastapi, uvicorn, httpx, yaml; print('all four present')"
```

**Why:**

- If any of the four were missing this day would need a package added, a dated `docs/PACKAGES.md`
  row and a lockfile change. They are not, so it does not — and checking is Principle 7's habit
  applied to what is already installed rather than to what is being added.

**What each file is for:**

- `_app.py` is the file to read first: the desk's front door, small enough to read whole. Two
  health endpoints answering different questions, a session store that is a dictionary, and a
  spend handler that does read-modify-write on a file. Every finding in sections 4 and 5 comes out
  of those three.
- `Dockerfile`, `.dockerignore` and `compose.yaml` are real artefacts, written to be deployed and
  never built here.
- `config.py`, `image.py`, `context.py`, `health.py`, `replicas.py` and `audit.py` are the six
  measurements, one per finding, each with its own exit code.
- `gate.py` is the day's eval against `sutra/deploy.py`.
- `papers/isolation/` holds the paper's demo; `boundary.py` is the workload and nothing else.

The lab is gitignored repo-wide. Confirm it before running `context.py`, which walks the whole
repository:

```bash
git check-ignore -v days/day-86-cloud-run-shaped/lab/_app.py
```

**Why:**

- `days/*/lab/` is the repository's rule for the learner's own code (Principle 9). It matters here
  because `context.py` reads every file under the repository root including `.env`, and knowing
  which rule protects what is the subject of part 2.3.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that
belongs in the product. Day 85 promoted the API surface; today promotes the deployment artefacts
and the two defects the containerisation work found.

**`sutra/deploy.py`** — the deployment contract, as data the rest of the repository can assert on.

- `TODO(me)`: `image_report()` returning the eight properties from part 2.2 as structured data
  rather than printed text, so a test can assert on them and CI can fail on them.
- `TODO(me)`: `context_report()` returning what the build would collect and which never-ship paths
  survive. Part 2.3's measurement, promoted — **and it must redact values**, because part 3.2's
  version prints the offending line and CI logs are a place a key can appear.
- `TODO(me)`: `required_env()` — the settings list with no defaults, read once at import, raising
  a named error listing every missing name at once. Part 3.1 is the shape; the trap is that
  nothing below it may read `os.environ` again.
- `TODO(me)`: `readiness()` returning a status **and a reason**, with separate reasons for missing
  and unparseable. Part 4.1 measured why one string is not enough.
- `TODO(me)`: `state_inventory()` — every writable path with its survives-restart and shared
  columns. Part 5.1's table, computed rather than remembered, and part 5.1's review comment names
  two rows it is currently missing.
- `TODO(me)`: `replica_limit()` returning the number of replicas this system can honestly run,
  derived from `state_inventory()` rather than hard-coded. It returns 1 today and the interesting
  part is that it should be able to explain why.

**`tests/test_deploy.py`**

- `TODO(me)`: a test that the Dockerfile has no `ENV` whose name matches the secret pattern — the
  version that would have caught `GOOGLE_API_KEY`, which the first draft of the checker missed
  because `\b` does not fire at an underscore.
- `TODO(me)`: a test that `.dockerignore` excludes `.env`, asserted against the real file rather
  than against a fixture. Part 2.3's measurement as a regression test.
- `TODO(me)`: a test that the app raises on an incomplete environment and names **every** missing
  setting, not just the first.
- `TODO(me)`: a test that a readiness failure returns 503 with a reason and that liveness is
  unaffected. Part 4.2, as an assertion.

**Two `TODO(me)`s that are defects rather than tasks**, and part 5.3 argues they should not wait
for a deployment:

- **The ledger increment is not atomic**, measured losing fifteen of twenty updates with a single
  replica. This is live today. The fix is not a lock — a lock makes the single-replica measurement
  green and hides it until somebody scales.
- **The session store lives in the process.** Day 47 built persistent sessions; pointing the app
  at them is what makes a second replica possible, and a rolling update makes the replica count
  two for a moment whether or not anybody scales.

**And one that needs an installation:**

- **Install a container runtime and build the image**, then run it once and probe `/readyz`. The
  exact command is in part 5.3. Note before starting that it will fail on the entry point —
  `sutra/api.py` is Day 85's build brief and the `CMD` imports `sutra.api:app`.

---

## §5 The eval that must be able to fail

```bash
cd days/day-86-cloud-run-shaped/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/deploy.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes
the other way:

```bash
uv run python config.py; echo "exit: $?"                  # 0 — complete starts, incomplete refuses
uv run python config.py --half; echo "exit: $?"           # 1 — only the good input was tried
uv run python image.py; echo "exit: $?"                   # 0 — 8 of 8 text properties hold
uv run python image.py --sloppy; echo "exit: $?"          # 1 — 2 of 8, from seven lines written fast
uv run python context.py; echo "exit: $?"                 # 0 — 40 files, nothing on the never-ship list
uv run python context.py --no-ignore; echo "exit: $?"     # 1 — 22,020 files, .env and .git/config in
uv run python health.py; echo "exit: $?"                  # 0 — readiness caught what liveness missed
uv run python health.py --liveness-only; echo "exit: $?"  # 1 — a healthy report on a dead service
uv run python audit.py; echo "exit: $?"                   # 1 — one of two kinds of state did not survive
uv run python replicas.py; echo "exit: $?"                # 0 — both failures reproduced
uv run python replicas.py --single; echo "exit: $?"       # 1 — one of the two survives the ablation
```

Note the three arms where the **ablation exits 0** — `config.py --half`, `health.py
--liveness-only` and, in spirit, `context.py` without its ignore file returning a build that
"works". Two of those are the report that hides the finding passing, which is this repository's
recurring shape and is now on its fourth appearance.

`audit.py` is red on purpose and has no ablation: the finding is the state of the system rather
than a property of the check, and §4's build brief is what turns it green.

The paper's demo does the same for its own claim: `demo.py` exits `0` having priced the same work
at 0.00% and 16.0% depending only on crossings, and `demo.py --off` exits `1` with both at zero.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Nothing in this day calls a model, and nothing needs to: the subject is packaging, and every
finding comes from a file, a process or a port.

**What was not run, and why.** This is the honest boundary of the day and it is larger than usual.
There is no container runtime on this machine:

```text
/usr/bin/bash: line 1: docker: command not found
```

So the following were **written and never executed**, each with its exact command:

| Not run | The command | What it would catch |
| --- | --- | --- |
| the image build | `docker build -t sutra-api:local .` | base tag, lockfile, entry point |
| a container run | `docker run --rm -e PORT=8080 -p 8080:8080 sutra-api:local` | the `$PORT` and `0.0.0.0` handling |
| the `HEALTHCHECK` | `docker inspect --format '{{.State.Health.Status}}' <id>` | whether the probe command works in a `slim` image |
| the composition | `docker compose up` | service-name resolution, volume ownership |
| pinning by digest | `docker buildx imagetools inspect python:3.12-slim-bookworm --format '{{.Manifest.Digest}}'` | a base that cannot move |
| a second replica, for real | `docker compose up --scale sutra-api=2` | that part 5.2 holds across containers, not only processes |

All six are free — a container runtime costs nothing — so this is an installation rather than a
budget problem, and it is item 1 in part 5.3.

**What replaced them.** Every property that is visible in text is checked in text (part 2.2), and
every behaviour that a process boundary can demonstrate is demonstrated with real processes
(sections 4 and 5). The two-replica finding in particular does not need containers: the isolation
between two containers on one host **is** a process boundary and a mount, which is exactly what
`replicas.py` builds.

What that substitution cannot cover is named in part 5.3, and one item is a certainty rather than
a risk: the image would fail to import `sutra.api:app`, because that module is Day 85's build
brief and does not exist yet.

---

## §7 Traps

1. **Treating `.dockerignore` as a build optimisation.** It is a security control: a layer is
   written once, so a file that reaches one is in the image permanently — part 2.3.
2. **Deleting a secret in a later instruction.** The running container does not have the file and
   the image does, which is what makes people believe it is fixed. The remedy is rotation — part
   1.2.
3. **Copying the source before the lockfile.** Every source edit then reinstalls every package,
   and nobody attributes the slowdown to the commit that caused it — part 1.2.
4. **Hard-coding the port.** The platform assigns it; an image with a literal port listens where
   nothing is looking and logs nothing wrong — part 1.3.
5. **Binding `127.0.0.1` inside a container.** Healthy logs, no connections, and it is the one
   place in this curriculum where `0.0.0.0` is the correct answer — part 1.3.
6. **Believing `EXPOSE` publishes a port.** It is metadata a tool may read, and nothing else —
   part 1.1.
7. **Reading a setting at the point of use.** `os.environ.get` returns `None`, which travels and
   fails somewhere unrelated. Read once, at import, and refuse — part 3.1.
8. **Passing a secret as a build argument.** It feels transient and is recorded in the image's
   history: the key in the drawer — part 3.2.
9. **Reading `depends_on` as readiness.** It is start order only, and the fix is a retry in the
   client because a cluster gives even less — part 3.3.
10. **Pointing a health probe at liveness.** `200 ok` on a service that can do no work, and the
    run that asks only that endpoint exits 0 — part 4.2.
11. **Putting a dependency check in the liveness probe.** A slow disk then restarts containers,
    and a restart never fixes a disk — part 4.1.
12. **Saying "stateless" without testing it.** Kill the process and one of two kinds of state
    comes back — part 5.1.
13. **Assuming a lost-update bug is a scaling bug.** It reproduces with one replica; the second
    replica removes the fix rather than causing the fault — part 5.2.
14. **Raising the replica count because the flag is there.** `--scale sutra-api=2` is inviting,
    documented, and produces a `404` for a live session — part 5.2.

---

## §8 Verify before you code

Fetched on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| ADK deployment guide | <https://adk.dev/deploy/> | the deployment targets, and the image shape each expects — `PORT`, a health endpoint, stateless |
| Paper record | <https://api.crossref.org/works/10.1109/ISPASS.2015.7095802> | *An updated performance comparison of virtual machines and Linux containers*, ISPASS 2015, pp. 171–172 |
| Cloud Run container contract | <https://cloud.google.com/run/docs/container-contract> | *"must listen for requests on the correct port"* and on `0.0.0.0` — both phrases read out of the page; the `PORT` variable's name is rendered by script and was not verifiable from the fetched HTML, so it is taken from the ADK deployment guide instead |

**Versions read live rather than remembered**, because Principle 7 applies to a base image and a
copied binary exactly as it applies to a package:

- `uv --version` → `uv 0.12.3`, which is the tag in the Dockerfile's `COPY --from`.
- `pyproject.toml` → `requires-python = "==3.12.*"`, which is why the base is `python:3.12-slim-bookworm`.
- `uv run python -V` → `Python 3.12.12`.
- `importlib.metadata` for the four packages this day uses: `fastapi 0.141.1`, `uvicorn 0.52.4`,
  `httpx 0.28.1`, `pyyaml 6.0.3` — all already installed, so no package is added.

**Not verified, and pinned as a `TODO(me)` rather than guessed:** the digest of
`python:3.12-slim-bookworm`. Resolving it needs a registry lookup and there is no runtime here, so
the Dockerfile carries the exact command instead of an invented `sha256`. Principle 7 is explicit
about which of those two a day is allowed to contain.

**No new 1.x → 2.x trap today.** The ADK surface is untouched — this day packages what Day 85
built and adds no ADK call at all.

---

## §9 Say it in an interview

*"We packaged the service into the shape a hosted runtime expects — image, environment
configuration, an assigned port, a readiness endpoint — and the useful part was not the Dockerfile.
It was three things the packaging exposed. First, we measured what the build would actually
collect: four hundred and fourteen megabytes across twenty-two thousand files, including a real
`.env` and `.git/config`, against forty files with an ignore file in place. That is a security
control rather than an optimisation, because a layer is immutable — deleting a secret in a later
instruction leaves the bytes in the earlier one, so the fix after the fact is key rotation, not a
rebuild. Second, we separated liveness from readiness and then measured the difference: delete the
dependency and the liveness endpoint still answers two hundred, so a platform watching only that
keeps routing traffic to a container that can do nothing. Third, and this is the one I would lead
with, we tested the word 'stateless' by running two copies. A session created on one returned
four-oh-four on the other, and twenty spend requests against a shared ledger recorded six. Then we
ran the ablation — one replica — and the session failure vanished while the ledger still lost
fifteen of twenty. So only one of the two was about replication. The lost updates were already
there in the single-instance system; scaling did not cause them, it removed the fix, because an
in-process lock cannot serialise writers in another process. That distinction changes what you
build, and a team that adds a mutex and watches the single-replica number go green ships the bug.
The honest caveat is that there was no container runtime on the machine, so nothing was built —
every measurement came from real processes and real files, and the daemon steps are written down
as unrun commands rather than as invented output."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands
rather than read them. `./m done 86` refuses to commit until they are.

The day is finished when you can look at any service and answer three questions without running
anything: what does it need that is not written down, what does it hold that would not survive
being replaced, and which of those two failures a second copy would cause rather than merely
reveal.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 86 | 2026-09-07 | ADK-66, ADK-67, OPS-17 | 14 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it is meant. `./m depth` is green over this day and every measurement
in it was run. What is not green: **no image was built**, because this machine has no container
runtime, so the Dockerfile and compose file are verified in text and unverified in behaviour — §6
lists the six commands that were not executed. And two defects were found that are not deployment
tasks: the quota ledger loses updates under concurrency with a single replica, and the session
store lives in the process, which a rolling update alone is enough to expose.

**`docs/PACKAGES.md`** — no new rows. No package is added today; the four this day uses are
already present as dependencies of `google-adk==2.7.1`.

**`docs/PAPERS.md`** — one new row:

```text
| An updated performance comparison of virtual machines and Linux containers | doi:10.1109/ISPASS.2015.7095802 | 2015 | 2026-09-07 | 86 | `days/day-86-cloud-run-shaped/papers/01-what-isolation-costs.md` |
```

The title, venue, year and pages were copied from
`api.crossref.org/works/10.1109/ISPASS.2015.7095802` on 2026-09-07 — the record, not the memory
(§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 86: containerize - cloud-run-shaped, locally - closes ADK-66, ADK-67, OPS-17
```
