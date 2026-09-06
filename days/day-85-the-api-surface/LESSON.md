---
day: 85
phase: 13
phase_name: "Observability & deployment"
title: "The API surface — api_server, FastAPI endpoints"
ids: ["ADK-64", "ADK-65"]
principles: [7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 85 — The API surface: `api_server`, FastAPI endpoints

> **Yesterday (Day 84):** the desk became observable — OpenTelemetry spans and `AutoTracingPlugin`,
> with every node, tool call and model call arriving in one trace tree. One question came back as ten
> spans five levels deep, and the identical run with no tracer provider wired up produced **zero
> spans and no error at all**.
> **Today:** the desk becomes reachable. `adk api_server` turns it into twenty-seven HTTP routes, and
> the whole day is spent reading that surface the way a stranger would. Three of the twenty-seven run
> the agent; the other twenty-four are session and artifact bookkeeping, and **nothing on any of them
> asks for a credential** — which the library's own help text says before you start. A stranger
> listed, read and deleted another user's session in three requests by typing a different name in the
> URL, one field called `detail` is a string on three routes and a list on a fourth, and a 404 for an
> app that does not exist answers with the server's absolute filesystem path.
> **Tomorrow (Day 86):** containerize — Cloud-Run-shaped locally, where "run it on a trusted network
> only" stops being a sentence about somebody else's deployment.

---

## §1 Where we are

The enquiry counter with a numbered window.

For years the office worked by people walking in and finding whoever seemed to know. Then somebody
put up a counter with three windows and painted numbers on them. Nothing about the work changed —
same clerks, same files. What changed is that the office acquired a *surface*: a small number of
named places where the outside world touches it. That is a good thing, mostly. It is also the day the
office acquired a queue, opening hours, and the problem of somebody walking up to window two and
asking for another person's file.

Every day of this curriculum so far ran the desk in process. Import the agent, call it, print. Today
it gets a URL, and the questions change from *does my agent work* — which Days 79 to 83 were about —
to **what is now reachable, by whom, and what does it say when it says no.**

The answers, all measured for nothing:

**Twenty-seven routes, three of which run the agent.** An agent server is mostly not about agents; it
is about the state around them. Twenty-four routes answer from local state, which is why this entire
day costs zero provider requests, and why the two paid routes refuse an unknown session with a `404`
before they spend anything.

**No route takes a credential, and fifteen of them address somebody's data by a name in the URL.**
`mallory` listed, read and destroyed `alice`'s session in three requests, and `alice` got a `404` for
her own data. `adk api_server --help` says this in its opening paragraph; the path scheme is so
natural that everybody reads ownership into it anyway.

**One field name, two types.** `detail` is a `str` when a handler refuses and a `list` when
validation refuses, so the natural client — read one error, write a handler — dies with
`AttributeError: 'list' object has no attribute 'lower'` on the error that happens most in production
and least in development.

**A 404 that reads out the disk.** Ask for an app that is not there and the refusal contains the
absolute path it searched, account name included: a hundred and sixty-five characters where about
twenty-six were needed, on a route that needs no credential.

And one protection that is supplied and off: the guard against DNS rebinding is on when
`adk api_server` starts the server and off when you build the app yourself, because the factory
defaults `bind_host` to `None` and `None` means *do not guess*.

---

## §2 The map

Five sections. Section 1 is the surface itself and the two ways to start it. Section 2 is how to
exercise it for nothing. Section 3 is what it says when it refuses. Section 4 is who can reach it.
Section 5 is what has to be added before anybody else may call it.

### 1 — The routing table

*What `api_server` puts on the network, and what the paths claim.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A desk with a street address](parts/01-the-routing-table/1.1-a-desk-with-a-street-address.md) | Twenty-seven routes in eight families, and how many run the agent | `foundation` |
| 1.2 | [What the paths say about the design](parts/01-the-routing-table/1.2-what-the-paths-say-about-the-design.md) | An ownership hierarchy, and the segment the caller types | `foundation` |
| 1.3 | [Two ways to start it, and one is safer](parts/01-the-routing-table/1.3-two-ways-to-start-it.md) | The two arguments the command passes and the factory does not | `working` |

### 2 — Exercising it for nothing

*Real HTTP, no socket, no quota.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A client with no socket](parts/02-exercising-it-free/2.1-a-client-with-no-socket.md) | `ASGITransport`, what it exercises and the five things it cannot | `working` |
| 2.2 | [Which endpoints cost nothing](parts/02-exercising-it-free/2.2-which-endpoints-cost-nothing.md) | Twenty-four free against three paid, and the free branch inside the paid ones | `working` |
| 2.3 | [The endpoint that sends a stream](parts/02-exercising-it-free/2.3-the-endpoint-that-sends-a-stream.md) | `/run_sse` declares JSON and sends `text/event-stream` | `working` |

### 3 — When it refuses

*The error body is part of the interface.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [One field, two types](parts/03-when-it-refuses/3.1-one-field-two-types.md) | 💥 `detail` as `str` and `list`, and the client that crashed | `working` |
| 3.2 | [The 404 that reads out the disk](parts/03-when-it-refuses/3.2-the-404-that-reads-out-the-disk.md) | 💥 One hundred and sixty-five characters where twenty-six were needed | `production` |
| 3.3 | [An error with a handle on it](parts/03-when-it-refuses/3.3-an-error-with-a-handle-on-it.md) | One shape, a stable identifier, and prose that may change | `working` |

### 4 — Blast radius

*Who can reach it, and as whom.* (Principle 13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The caller says who they are](parts/04-blast-radius/4.1-the-caller-says-who-they-are.md) | 💥 Three requests, three `200`s, no credential, another user's session gone | `production` |
| 4.2 | [Which pages may call it](parts/04-blast-radius/4.2-which-pages-may-call-it.md) | `403` by default, and what `allow_origins=["*"]` really sends back | `working` |
| 4.3 | [The guard in the box](parts/04-blast-radius/4.3-the-guard-in-the-box.md) | DNS rebinding, and the one argument that turns the guard on | `production` |

### 5 — In production

*What has to be added before anybody else calls it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Health is not readiness](parts/05-in-production/5.1-health-is-not-readiness.md) | A two-line handler that checks nothing, and why that is correct | `production` |
| 5.2 | [What a real API surface adds](parts/05-in-production/5.2-what-a-real-api-surface-adds.md) | Eight items, three of which take minutes between them | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [An error a client can act on](papers/01-an-error-a-client-can-act-on.md) | `doi:10.17487/RFC9457` — `application/problem+json` and a stable `type` a client branches on. The demo routes two refusals correctly, two of two; the ablation removes the handler and routes zero of two from bodies a person would call clearer |

---

## §3 Setup — run this

```bash
mkdir -p days/day-85-the-api-surface/lab/agents/echo
mkdir -p days/day-85-the-api-surface/lab/papers/problem-details
cd days/day-85-the-api-surface/lab
touch _desk.py routes.py free.py shapes.py leak.py whoami.py cors.py rebind.py stream.py gate.py
touch agents/echo/__init__.py agents/echo/agent.py
touch papers/problem-details/api.py papers/problem-details/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
`fastapi`, `starlette`, `uvicorn` and `httpx` are already installed as dependencies of
`google-adk==2.7.1`, which is itself the finding that Day 79 part 4.3 made about the eval extra: an
ADK install is larger than it looks.

**What each file is for:**

- `agents/echo/` is the fixture: the smallest agent that is still a real one, so the server has
  something to serve. Nothing in this day calls it.
- `_desk.py` is the file to read first. It builds the app through ADK's own factory, gives every
  script an in-process HTTP client, and masks the two fields that differ on every run so a transcript
  is reproducible.
- `routes.py` prints the routing table; `free.py` exercises the endpoints that cost nothing.
- `shapes.py`, `leak.py` are section 3's two findings; `stream.py` is the declared-versus-sent
  comparison.
- `whoami.py`, `cors.py`, `rebind.py` are section 4, one per part.
- `gate.py` is the day's eval against `sutra/api.py`.
- `papers/problem-details/` holds the paper's demo: `api.py` is one route that refuses two ways.

The lab is gitignored repo-wide. Confirm it before you start:

```bash
git check-ignore -v days/day-85-the-api-surface/lab/_desk.py
```

**Why:**

- `days/*/lab/` is the repository's rule for the learner's own code (Principle 9), and this day's lab
  creates no files outside it — `session_service_uri="memory://"` is passed precisely so the server
  writes nothing to disk.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that
belongs in the product. Day 84 promoted tracing; today promotes the HTTP surface, and it is the first
module in this repository whose job is to *refuse* things.

**`sutra/api.py`** — the desk as a service, built from ADK's factory with every argument chosen.

- `TODO(me)`: `serve()` calling `get_fast_api_app` with `web=False`, an absolute `agents_dir`, and
  **every non-default argument spelled out with a comment saying why**. Part 1.3's point: moving from
  the command to the factory is a migration of defaults.
- `TODO(me)`: `bound` — pass `bind_host` explicitly, always, derived from the same variable the server
  binds. Part 4.3 measured a foreign `Host` served with a `200` when it is omitted.
- `TODO(me)`: `origins` — a named list or a `regex:` anchored to a domain you own, never `["*"]`.
  Part 4.2 measured the wildcard reflecting the caller's own origin back.
- `TODO(me)`: `caller` — a dependency that validates a credential and yields a subject. This is the
  one that does not exist anywhere yet, and everything else on the list assumes it.
- `TODO(me)`: `owns` — a dependency comparing that subject to the `{user_id}` path parameter,
  attached at the router so all fifteen routes inherit it. Part 4.1 is why, and part 5.2 gives the
  shape.
- `TODO(me)`: `problem` — one exception handler rendering every refusal as
  `application/problem+json`, with the body **constructed from chosen fields** and never from an
  exception's string. Convert the framework's validation errors in the same change, or part 3.1's
  finding survives the fix.
- `TODO(me)`: `ready` — a readiness route that touches the session store and returns `503` naming the
  dependency that failed. Different probe from `/health`, and no model call in it.

**`tests/test_api.py`**

- `TODO(me)`: a test that a session created as `alice` returns `403` when read as `mallory`. Part 4.1
  as a test, and the one that will still be true in a year.
- `TODO(me)`: a test that every error response has `content-type: application/problem+json` and a
  `type` member — including a deliberately malformed body, which is the validation path.
- `TODO(me)`: a test that no error body contains `str(Path.home())` or a path-shaped string. Part
  3.2's check, as a regression test rather than a one-off measurement.
- `TODO(me)`: a test that a request with a foreign `Host` is refused. Use
  `ASGITransport(raise_app_exceptions=False)` so a `500` is a response rather than an exception in
  the test — part 2.1's measured trap.

**Two `TODO(me)`s that are not code:**

- **Decide the `type` vocabulary** and keep it in one module. The paper gives you a slot for an
  identifier and no help choosing identifiers; the format is the easy half.
- **Run the two paid routes once, deliberately**, and record what `/run_sse` actually sends:
  `curl -N -X POST http://127.0.0.1:8000/run_sse -H 'content-type: application/json' -d '{...}'`.
  Part 2.3 cites the media type from the library's source because measuring it costs provider quota;
  one run closes that gap, and the `-N` is what stops curl buffering the stream.

---

## §5 The eval that must be able to fail

```bash
cd days/day-85-the-api-surface/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/api.py`, all red today because the module is the build brief. A check that
cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes the
other way:

```bash
uv run python routes.py; echo "exit: $?"                    # 0 — 27 routes in 8 families
uv run python free.py; echo "exit: $?"                      # 0 — 6 of 6 answered, 0 requests
uv run python free.py --paid; echo "exit: $?"               # 0 — the three this day will not call
uv run python shapes.py; echo "exit: $?"                    # 1 — `detail` is str and list
uv run python shapes.py --count-only; echo "exit: $?"       # 0 — 4 of 4, three times over
uv run python leak.py; echo "exit: $?"                      # 1 — 165 characters, home directory in it
uv run python leak.py --redacted; echo "exit: $?"           # 0 — the same refusal, saying less
uv run python whoami.py; echo "exit: $?"                    # 1 — 3 of 3, zero credentials
uv run python whoami.py --trusted-network; echo "exit: $?"  # 0 — the same numbers, waved through
uv run python cors.py; echo "exit: $?"                      # 0 — 403 for a stranger's origin
uv run python cors.py --open; echo "exit: $?"               # 1 — 200, and the origin echoed back
uv run python rebind.py; echo "exit: $?"                    # 1 — a foreign Host served
uv run python rebind.py --bound; echo "exit: $?"            # 0 — 403 Forbidden: host not allowed
uv run python stream.py; echo "exit: $?"                    # 1 — declared JSON, sends event-stream
uv run python stream.py --refusal; echo "exit: $?"          # 0 — 404 before any agent starts
```

Note the three arms that **exit 0 while hiding a finding**: `shapes.py --count-only`, which reports
four of four on three properties and none of them the one that matters; `whoami.py
--trusted-network`, which prints the same three lines of evidence and adds a sentence about the
deployment; and `leak.py --redacted`, which is the only one of the three that is a genuine fix rather
than a report. Telling those apart is the exercise.

The paper's demo does the same for its own claim: `demo.py` exits `0` having routed two of two
refusals, and `demo.py --off` exits `1` having routed zero of two from bodies a person would call
clearer.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Everything in this day is the real server. `get_fast_api_app` is ADK's own factory — the one
`adk api_server` calls — every status code was returned by it, and `httpx.ASGITransport` runs the
request through every middleware, dependency and exception handler the app has. What is skipped is
the socket, and part 2.1 lists the five things that skipping costs.

Three of the twenty-seven routes are not exercised, and that is the day's honest boundary: `/run`,
`/run_sse` and `/run_live` each start an agent turn. Part 2.2 prices them and part 2.3 cites the one
fact about `/run_sse` that cannot be had for free — its actual `Content-Type`, read from the
library's source with the file, date and line numbers recorded rather than measured. The build brief
carries the exact command for closing that gap in one deliberate run.

---

## §7 Traps

1. **Reading the URL scheme as ownership.** `users/alice` is a string the caller typed, and fifteen
   routes carry it — part 4.1.
2. **Assuming the factory and the command are the same.** The command passes `bind_host` and the
   factory defaults it to `None` — part 1.3.
3. **Setting `host` and thinking you have bound something.** Its own documentation says it is unused
   by the returned app — part 1.3.
4. **Writing one error handler after reading one error.** `detail` is a `str` on three routes and a
   `list` on the fourth — part 3.1.
5. **Putting an exception's string in a response body.** That is how a 404 comes to contain the
   account name and the repository layout — part 3.2.
6. **Branching on the prose.** A wording change is not a breaking change to anybody, and it reroutes
   a customer — part 3.3 and the paper.
7. **Reaching for `allow_origins=["*"]` to fix a console error.** The named origin costs the same ten
   seconds, and the wildcard echoes the caller's origin back — part 4.2.
8. **Believing CORS is access control.** It is enforced by the browser; every other client ignores it
   — part 4.2.
9. **Pointing a liveness probe at a dependency check.** A slow session store then restarts every
   replica, repeatedly — part 5.1.
10. **Pointing a readiness probe at `/health`.** It returns `ok` from a two-line function, so traffic
    goes to a replica that cannot serve it — part 5.1.
11. **Probing a paid route.** Day 78's observed allowance is twenty a day; a probe every five seconds
    is finished before breakfast — part 2.2.
12. **Trusting the generated schema.** `/run_sse` declares `application/json` with an empty schema and
    sends `text/event-stream` — part 2.3.

---

## §8 Verify before you code

Fetched on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| ADK deployment and serving | <https://adk.dev/deploy/> | `adk api_server` and `get_fast_api_app` as the two supported entry points |
| Paper record | <https://api.crossref.org/works/10.17487/RFC9457> | *Problem Details for HTTP APIs*, RFC Editor, 2023 |
| `adk api_server --help` | the installed CLI | *"This server's endpoints are unauthenticated. Run it on a trusted network only, and put it behind your own authentication and authorization layer before exposing it to untrusted or public networks or serving multiple users."* |

**ADK symbols verified against the installed `google-adk==2.7.1`**, not only against the docs.
`get_fast_api_app` takes **twenty-eight keyword-only parameters**, with `host: str = "127.0.0.1"`,
`bind_host: str | None = None` and `allow_origins: list[str] | None = None` — and `host`'s own
docstring says *"Unused by the returned app; pass `bind_host` to guard it."*
`google/adk/cli/cli_tools_click.py` lines 2071–2072 pass `host=host, bind_host=host`, which is why
the command has the rebinding guard on and an embedder does not. The app registers **twenty-seven
routes in eight families**, one of them an `APIWebSocketRoute` (`/run_live`). `/health` is a two-line
handler returning `{"status": "ok"}` unconditionally, and `/version` reports the ADK version and the
Python version. `_is_dns_rebinding_request` in `google/adk/cli/api_server.py` gates on
`bind_host is None` and on `_is_loopback_address(bind_host)`, and its own comment explains why
`Origin` cannot substitute for `Host`. The SSE handler returns `StreamingResponse(...,
media_type="text/event-stream")` at lines 1955–1957, while `/openapi.json` declares
`application/json` with an empty schema for that route's `200`.

**The 1.x → 2.x trap this day pays for is ADK-73** — every model pinned explicitly. The fixture agent
pins `gemini-2.5-flash-lite` even though nothing in this day calls it, because a fixture that would
have spent quota if it had run is a fixture that will spend it the day somebody extends the lab.

---

## §9 Say it in an interview

*"We took the agent out of the terminal and served it over HTTP, and then spent the day reading the
surface as a stranger rather than as its author. Twenty-seven routes, and only three of them run the
agent — the rest is session and artifact state, which meant we could exercise almost the whole API in
process with an ASGI transport for zero cost and full determinism. Three findings came out of that.
The first is the one I would lead with: fifteen routes are shaped `/users/{user_id}/sessions/...` and
nothing takes a credential, so one caller listed, read and deleted another's session in three
requests by typing a different name — and the caller whose data it was got a 404 for her own session.
That is not a vendor bug; the CLI's help text says the endpoints are unauthenticated and to put your
own layer in front. The interesting part is that the URL scheme is so natural that everybody reads
ownership into it. The second is the error contract: one field called `detail`, a string when a
handler refuses and a list when validation refuses, so the obvious client crashes with an
AttributeError on the error that is rare in development and common in production — we fixed that with
RFC 9457 problem documents, one exception handler, and a stable `type` the client branches on instead
of the prose. The third was a 404 for a non-existent app that answered with the server's absolute
filesystem path including the account name, on an unauthenticated route — which is the same fix,
because a constructed error body cannot leak a message nobody chose. And one thing we would have
missed: the rebinding guard ADK ships is on when you run their command and off when you embed their
factory, because `bind_host` defaults to None. One argument, no cost to legitimate traffic."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 85` refuses to commit until they are.

The day is finished when you can be shown any HTTP API and ask the four questions in order: which
routes exist, which of them cost something, what does a refusal look like, and who is allowed to
ask — and when you know which of those four your own service currently answers.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 85 | 2026-09-07 | ADK-64, ADK-65 | 14 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth`, `./m trace` and `./m wiki --check` are green over
this day and every measurement in it was run. What is not green: `sutra/api.py` is the build brief
and `lab/gate.py` reports 0 of 6, by design. Three findings carry forward into Day 86 — the server
has no authentication and takes the caller's identity from the URL, the error contract has two shapes
and one of them leaks a filesystem path, and the rebinding guard is off unless `bind_host` is passed.
All three get harder to argue about tomorrow, because "trusted network" is a sentence about a laptop.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one new row:

```text
| Problem Details for HTTP APIs | doi:10.17487/RFC9457 | 2023 | 2026-09-07 | 85 | `days/day-85-the-api-surface/papers/01-an-error-a-client-can-act-on.md` |
```

The title, publisher and year were copied from `api.crossref.org/works/10.17487/RFC9457` on
2026-09-07 — the record, not the memory (§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 85: the api surface - api_server, fastapi endpoints - closes ADK-64, ADK-65
```
