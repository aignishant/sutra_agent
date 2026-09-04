# Day 38 — Definition of done

`./m done 38` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] **The freshness gate.** `curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1`
      prints `2026-07-28`. If it does not, stop and amend the plan first (Principle 14).
- [ ] Day 37's parts and checklist are done, and `sutra_mcp` serves tools, resources, prompts, task
      handles and a gated write.
- [ ] `lab/` scaffolded per §3 — eighteen scripts, one JSON fixture, and
      `lab/papers/maintaining-robust-protocols/`.

## Section 1 — the clock (MCP-11)

- [ ] **1.1** read · ran both arms of `deadline.py slow` · saw `6.05s` against `2.01s` · ran
      `DEADLINE=0 python deadline.py hang` and had to press Ctrl-C · **said out loud** what a client
      can conclude about a server that has not answered for six seconds
- [ ] **1.2** read · ran `oblivious.py` · saw the server announce it had finished **after** the client
      gave up · can say why `TimeoutError` means *unknown* rather than *failed*
- [ ] **1.3** read · ran `cancel.py` · saw the server write one more chunk successfully **after** the
      hang-up, and discover it on the chunk after that · changed `return` to `pass` and watched a
      legal server finish into a dead socket
- [ ] **1.4** read · ran both arms of `reissue.py` · saw `['OLD']` accepted as the answer to a question
      that had not been asked when it was computed · can quote the rule about re-issuing with a new
      request id

## Section 2 — the boundary (MCP-12)

- [ ] **2.1** read · ran `HARDENED=1` and saw `crimes named at the boundary: 5/5` · ran `HARDENED=0`
      and read the `JSONDecodeError` traceback in full · deleted check 3 and saw which crime got
      accepted
- [ ] **2.2** read · ran `classify.py` · can state the one question that decides whether to retry ·
      knows why the default for an unrecognised failure is quarantine
- [ ] **2.3** read · ran both arms of `errors.py` · `14` requests against `50` · can name which of the
      five codes deserves a retry and why its missing `data` block is part of the reason
- [ ] **2.4** read · ran both arms of `twice.py` · saw `2/3` answers about the wrong ticket with no
      exception · changed `range(2)` to `range(3)` and saw the single `if` fail to save it

## Section 3 — the quiet ones

- [ ] **3.1** read · ran both arms of `plausible.py` · saw `envelope checks: all five passed` in the
      run that produced a false sentence · can say why a schema validator cannot do the echo check
- [ ] **3.2** read · ran both arms of `double_close.py` · **two customer emails against one** · can
      say why the idempotency key cannot be the JSON-RPC request id

## Section 4 — the leaving list (MCP-31)

- [ ] **4.1** read · ran `lifecycle.py` · saw `327 days` · can state the difference between *eligible
      for removal* and *removed*
- [ ] **4.2** read · can name the one property Roots, Sampling and Logging share, and the change in the
      same revision that took it away · recited the three migration paths closed-book
- [ ] **4.3** read · ran `deprecation_scan.py` and saw `exit: 1` with three findings · removed the
      `capabilities.client` block and saw which finding disappeared

## Section 5 — the replacement (MCP-31)

- [ ] **5.1** read · ran both arms of `mrtr.py` · saw `completed: True` against
      `worker-2 has no pending question for this call` · can state what the JSON-RPC id must do
      between the first attempt and the retry, and what `requestState` must not do
- [ ] **5.2** read · ran both arms of `tamper.py` · **400 tickets against 0** · can say why
      `hmac.compare_digest` is used instead of `==`, and why you sign the bytes rather than the object
- [ ] **5.3** read · wrote out, for each of the three migration paths, what a server acquires by
      following it · marked which of those Sutra already owns

## Section 6 — in production

- [ ] **6.1** read · ran both `uv run --isolated` imports · read the bare `ModuleNotFoundError` and the
      one carrying `MCPServer`, the migration URL and `pin 'mcp<2'` · can name the six pieces of
      information in the second message
- [ ] **6.2** read · ran `bump_probe.py` under both SDKs · **nine cells, no warnings** · can say why an
      SDK supporting several revisions cannot mark deprecated types the way the policy asks
- [ ] **6.3** read · ran both arms · diffed the two symbol tables · grepped the repository for the
      three moved names · can name the four things that change and which half of the codebase pays
- [ ] **6.4** read · wrote `tests/test_mcp_failures.py` · ran it · **wrote down which tests stay red
      and why** — that list is Day 44's specification

## The paper

- [ ] Read [`papers/01-maintaining-robust-protocols.md`](papers/01-maintaining-robust-protocols.md)
      **after** the parts
- [ ] Ran both arms of the demo: `STRICT=0` gives `3/3` then `2/3` and *rolled back*; `STRICT=1` gives
      `1/3` then `3/3` and *still moves*
- [ ] Set `grease=False` in the strict arm and watched `brittle` pass both eras while still being broken
- [ ] **Said out loud**, without the word "ossification", what a tolerant server takes away from a
      protocol

## The whole day

- [ ] Every `TODO(me)` in §4 has been **read**, and the ones you answered are written down somewhere
      that is not this checklist
- [ ] `./m depth 38` is green
- [ ] `.venv/Scripts/ruff.exe check days/day-38-failure-and-migration-lab/` passes
- [ ] `uv run python -m pytest -q -m "not live"` — you know which tests are red and why
- [ ] **`git diff --stat pyproject.toml uv.lock` prints nothing.** The pin was not moved.
- [ ] **Phase 5 freshness check** run and any finding recorded in `docs/CHANGELOG_PLAN.md` before Day
      39 begins: the specification revision, `google-adk` and `mcp` releases since the pins, and the
      three providers' free rosters
- [ ] `docs/PROGRESS.md` row appended verbatim from §11
- [ ] `git status` shows no `.env` (Principle 9)
- [ ] Commit made with the message in §11
