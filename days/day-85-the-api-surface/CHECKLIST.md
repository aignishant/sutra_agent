# Day 85 — checklist

**Definition of done.** `./m done 85` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-85-the-api-surface/lab && uv run python whoami.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-85-the-api-surface/lab/` exists with the twelve files listed in the hub's §3, plus the
      `agents/echo/` fixture.
- [ ] `git check-ignore -v days/day-85-the-api-surface/lab/_desk.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_desk.py` and can say why `session_service_uri="memory://"` is passed and what it prevents.
- [ ] Can say what `mask()` replaces and why that is presentation rather than a finding.

## Section 1 — the routing table

- [ ] Read [1.1 A desk with a street address](parts/01-the-routing-table/1.1-a-desk-with-a-street-address.md);
      ran `routes.py` and can say how many of the twenty-seven routes run the agent.
- [ ] Moved the `LIVENESS` check to the bottom of `family()`, predicted how many routes move, ran it,
      and put it back.
- [ ] Read [1.2 What the paths say about the design](parts/01-the-routing-table/1.2-what-the-paths-say-about-the-design.md);
      counted the routes carrying `{user_id}` with `routes.py | grep -c user_id`.
- [ ] Found the one route that hangs off `{user_id}` but not off a session, and can say why.
- [ ] Read [1.3 Two ways to start it](parts/01-the-routing-table/1.3-two-ways-to-start-it.md);
      can name the two arguments `adk api_server` passes that the factory defaults to nothing.
- [ ] Read `adk api_server --help` and found the paragraph about authentication.

## Section 2 — exercising it for nothing

- [ ] Read [2.1 A client with no socket](parts/02-exercising-it-free/2.1-a-client-with-no-socket.md);
      ran `free.py` and can name the five things an ASGI transport cannot exercise.
- [ ] Can say what `raise_app_exceptions=True` does to a test that is about a server error.
- [ ] Read [2.2 Which endpoints cost nothing](parts/02-exercising-it-free/2.2-which-endpoints-cost-nothing.md);
      ran both arms and priced a liveness probe pointed at `/run`.
- [ ] Ran `stream.py --refusal` and can say why a wrong session id costs nothing.
- [ ] Read [2.3 The endpoint that sends a stream](parts/02-exercising-it-free/2.3-the-endpoint-that-sends-a-stream.md);
      found the `200` schema for `/run_sse` in `/openapi.json` and compared it with the `422`.

## Section 3 — when it refuses

- [ ] Read [3.1 One field, two types](parts/03-when-it-refuses/3.1-one-field-two-types.md);
      ran both arms and looked for a false statement in the `--count-only` output.
- [ ] Added a fifth entry to `WRONG` sending `userId` as a number, predicted the status and the type
      of `detail`, and checked.
- [ ] Read [3.2 The 404 that reads out the disk](parts/03-when-it-refuses/3.2-the-404-that-reads-out-the-disk.md);
      ran both arms and listed four separate facts a stranger learns from the real message.
- [ ] Can say why the fix is a **constructed** body rather than a filter on the message.
- [ ] Read [3.3 An error with a handle on it](parts/03-when-it-refuses/3.3-an-error-with-a-handle-on-it.md);
      can name the field a client may branch on and the field it must not.

## Section 4 — blast radius

- [ ] Read [4.1 The caller says who they are](parts/04-blast-radius/4.1-the-caller-says-who-they-are.md);
      ran `whoami.py` and saw `alice` get a `404` for her own session.
- [ ] Ran `whoami.py --trusted-network`, confirmed every number is identical, and can say what changed.
- [ ] Can state the difference between identification, authentication and authorization in one sentence
      each.
- [ ] Read [4.2 Which pages may call it](parts/04-blast-radius/4.2-which-pages-may-call-it.md);
      ran both arms and read the `allow-origin` value the wildcard actually returns.
- [ ] Rebuilt with `allow_origins=["http://localhost:3000"]`, predicted both status codes, and checked.
- [ ] Read [4.3 The guard in the box](parts/04-blast-radius/4.3-the-guard-in-the-box.md);
      ran both arms and can walk through the six steps of a DNS-rebinding attack.
- [ ] Built with `bind_host="0.0.0.0"`, predicted what the foreign host gets, and checked.

## Section 5 — in production

- [ ] Read [5.1 Health is not readiness](parts/05-in-production/5.1-health-is-not-readiness.md);
      can name the two probes, the two questions and the two failure actions.
- [ ] Can say what goes wrong in **both** directions when the two probes are confused.
- [ ] Read [5.2 What a real API surface adds](parts/05-in-production/5.2-what-a-real-api-surface-adds.md);
      mapped the seven-step sequence onto the eight items and found the step no item covers.

## The paper — after the parts

- [ ] Read [papers/01 An error a client can act on](papers/01-an-error-a-client-can-act-on.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/problem-details/` and saw two of two against
      zero of two.
- [ ] Reworded both `detail` strings completely, re-ran both arms, and can say what that demonstrates.
- [ ] Added a third refusal with its own `type`, left it out of `ROUTE_TO`, predicted the client's
      behaviour, and checked.
- [ ] Can name the class of errors that will never arrive as problem documents however well you adopt
      the standard.

## The build brief

- [ ] `sutra/api.py` written — `serve()`, `bound`, `origins`, `caller`, `owns`, `problem`, `ready`.
- [ ] Every non-default argument to `get_fast_api_app` spelled out with a comment saying why.
- [ ] `bind_host` passed explicitly, derived from the same variable the server binds to.
- [ ] `allow_origins` is a named list or a `regex:` anchored to a domain you own — never `["*"]`.
- [ ] `owns` attached at the router, so all fifteen `{user_id}` routes inherit it.
- [ ] `problem` builds every error body from **chosen fields**, never from an exception's string, and
      the framework's validation errors are converted in the same change.
- [ ] `ready` touches the session store, returns `503` naming the failed dependency, and calls no model.
- [ ] `tests/test_api.py` written — the cross-user `403` test, the problem-document test, the
      no-filesystem-path test, and the foreign-`Host` test.
- [ ] **Decide the `type` vocabulary** and keep it in one module.
- [ ] **Run the two paid routes once, deliberately**, and record what `/run_sse` actually sends. Part
      2.3 cites it rather than measuring it, and this closes the gap.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/api.py` is the build brief.
- [ ] `routes.py` exits `0`; `free.py` and `free.py --paid` exit `0`.
- [ ] `shapes.py` exits `1`; `--count-only` exits `0`.
- [ ] `leak.py` exits `1`; `--redacted` exits `0`.
- [ ] `whoami.py` exits `1`; `--trusted-network` exits `0`.
- [ ] `cors.py` exits `0`; `--open` exits `1`.
- [ ] `rebind.py` exits `1`; `--bound` exits `0`.
- [ ] `stream.py` exits `1`; `--refusal` exits `0`.
- [ ] `papers/problem-details/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** deleted `agents/echo/agent.py`, ran `routes.py` and `free.py`,
      and confirmed the app still builds and only the request fails. Then put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can name the three routes this day deliberately did not call, and the one fact about `/run_sse`
      that is cited from source rather than measured.

## Ledger & commit

- [ ] `./m depth 85` green.
- [ ] `./m trace` regenerated; day 85 closes exactly `ADK-64`, `ADK-65`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `doi:10.17487/RFC9457` row added.
- [ ] Committed with the message in the hub's §11.
