# Day 44 — Definition of done

`./m done 44` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] **The freshness gate.** `curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1`
      prints `2026-07-28`. If it does not, stop and amend the plan first (Principle 14).
- [ ] Day 43's parts and checklist are done, and `sutra_mcp/app.py` serves from any instance.
- [ ] You have re-read the list you wrote at the end of Day 38's
      [6.4](../day-38-failure-and-migration-lab/parts/06-in-production/6.4-the-test-that-must-go-red.md)
      — *which tests stay red and why*. That list is this day's specification.
- [ ] `lab/` scaffolded per §3 — nineteen scripts and `lab/papers/the-tail-at-scale/`.

## Section 1 — what may be repeated (MCP-22)

- [ ] **1.1** read · ran both arms of `idem.py` · saw **two closure notices against one** · added
      `"close_ticket"` to `IDEMPOTENT`, watched the `--safe` arm go green, and can say why a green run
      is the worse outcome
- [ ] **1.2** read · ran `unknown.py` · saw one sentence for three different worlds · can say which of
      the three makes a retry dangerous and why the other two do not
- [ ] **1.3** read · ran both arms of `repeatable.py` · saw `refund_order` granted a retry by the
      optimistic default · **wrote `RETRYABLE` with a reason per row** and a date
- [ ] **1.4** read · ran both arms of `key.py` · **two notices against one** · moved the `key = ...`
      line inside a loop and watched the mechanism stop working while still looking correct

## Section 2 — the deadline (MCP-22)

- [ ] **2.1** read · ran `clocks.py` · saw `0.51s` against `1.50s` for the same exception text · chose
      a connect deadline and a per-tool call deadline for every server in Day 40's `REGISTRY`, with a
      reason beside each
- [ ] **2.2** read · ran both arms of `budget.py` · **4.50s against 2.00s** · saw attempt 3 ask for
      1.50s with 0.00s left · can state the difference between a timeout and a deadline in one sentence
- [ ] **2.3** read · ran `wrap.py` · saw **2 completions for 2 calls, 1 of which nobody read** · set
      `max_workers=1` and watched two calls report a server timeout without ever reaching the server
- [ ] **2.4** read · ran all three arms of `sdkclock.py` · saw the default arm **answer after 3.01s
      with no deadline at all** · read the `--session` traceback in full · can name which of ADK's two
      numbers becomes the call deadline over Streamable HTTP, and how many times ADK retries a
      `close_ticket` that times out

## Section 3 — backing off (MCP-22)

- [ ] **3.1** read · ran `backoff.py` · saw the immediate ladder spend six requests at `0s` · set
      `RECOVERS_AT` to `2.0` and saw which ladder wins then
- [ ] **3.2** read · ran both arms of `jitter.py` · **640 shed against 246**, busiest second 200
      against 134 · changed the jitter to `ceiling + uniform(0, 0.3)` and saw a sprinkle achieve
      nothing
- [ ] **3.3** read · ran both arms of `retry_after.py` · **2 requests and 6.08s against 5 requests and
      7.59s** · can name the one situation in which you must not sleep for the stated delay
- [ ] **3.4** read · ran both arms of `attempts.py` · **27 requests against 2** · wrote down Sutra's
      attempt budget **including ADK's free retry**, because Day 45 asks for that number

## Section 4 — when to stop asking (MCP-22)

- [ ] **4.1** read · ran both arms of `storm.py` · **the same 40 callers answered, 520 requests
      against 200, 12.9s against 4.9s** · set `RATE` to `150.0`, watched the retry arm win, and can say
      why that result is more dangerous
- [ ] **4.2** read · ran all three arms of `breaker.py` · **24 answered against 14** in the correct
      arm versus the sticky one · found the one line that is missing in the sticky arm · decided the
      threshold, the cooldown, the granularity and which failure classes count

## Section 5 — no held connections (MCP-23)

- [ ] **5.1** read · ran both arms of `held.py` · saw `[None, 1, 1, None, None]` and then
      **connection 1 return an empty string, not an exception** · can name the four expired reasons
      for holding a connection
- [ ] **5.2** read · ran both arms of `catalog.py` · **12 list calls against 2** · set `TTL_MS` to
      `60000` and can say what Sutra would do for a whole minute after a tool is deleted
- [ ] **5.3** read · ran `cost.py` · **1.484s against 5.422s, all of it in the connect column** · wrote
      down, per transport, what Sutra holds between requests and what breaks if it is taken away

## Section 6 — the last word (MCP-22 · MCP-23)

- [ ] **6.1** read · ran `escalate.py` · rewrote the payload for `close_ticket` · **the `message` does
      not claim the ticket was not closed**
- [ ] **6.2** read · ran `onepolicy.py` against both files · `findings: 4` and `exit: 1` against
      `findings: 0` and `exit: 0` · can say why `article` — the function that *does* retry — is one of
      the four findings

## The paper

- [ ] Read [`papers/01-the-tail-at-scale.md`](papers/01-the-tail-at-scale.md) **after** the parts
- [ ] Ran both arms of the demo: page p50 **`559.1ms` against `18.9ms`**, pages over 100ms
      **`63.4%` against `0.9%`**, for **`1.0%`** extra load
- [ ] Set `SLOW_SHARE` to `0.5` and watched hedging stop helping — say out loud why
- [ ] **Said out loud**, without the word "percentile", what this paper claimed and what the field
      does differently now

## The project code

- [ ] `sutra/mcp/hardening.py` written, with `with_timeout`, `with_retries`, `RETRYABLE`,
      `RetryPolicy` and `Deadline`
- [ ] `uv run python days/day-44-client-hardening/lab/gate.py` prints `findings: 0` and `exit: 0`
- [ ] You ran the gate **before** writing the module and saw it red
- [ ] You broke exactly one assertion on purpose — added `"close_ticket"` to `RETRYABLE` — and watched
      the finding appear
- [ ] Nothing under `sutra/mcp/` holds a session, client or connection at module scope
- [ ] Every `McpToolset` Sutra constructs is closed

## The whole day

- [ ] Every `TODO(me)` in §4 has been **read**, and the ones you answered are written down somewhere
      that is not this checklist
- [ ] `./m depth 44` is green
- [ ] `.venv/Scripts/ruff.exe check days/day-44-client-hardening/` passes
- [ ] `uv run python -m pytest -q -m "not live"` — you know which tests are red and why, and the ones
      Day 38 left red for today are now green
- [ ] **`git diff --stat pyproject.toml uv.lock` prints nothing.** No package was added and no pin was
      moved.
- [ ] `docs/PROGRESS.md` row appended verbatim from §11
- [ ] `git status` shows no `.env` (Principle 9)
- [ ] Commit made with the message in §11
