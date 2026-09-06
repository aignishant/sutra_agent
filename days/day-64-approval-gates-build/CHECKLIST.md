# Day 64 — Definition of done

`./m done 64` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 63's parts and checklist are done, and you have its policy table in front of you — today
      turns it into code and part 1.2 is the shape it has to take.
- [ ] `uv run python days/day-64-approval-gates-build/lab/gate.py; echo "exit: $?"` is **red** before
      you write anything: `0/6`, exit 1, with checks 2–6 reported as **skipped** rather than passed.
- [ ] `ls days/day-64-approval-gates-build/lab` lists nineteen files. The lab is written for you today;
      the reps are in §4.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `python -c "import google.adk; print(google.adk.__version__)"` prints **2.7.1** — every symbol in
      this day was verified against that build, and three of them disagree with the docs (§8).

## Section 1 — the policy is data

- [ ] **1.1** read · ran `_policy.py` and saw **doctest 4/4** · reached `UnknownAction` on purpose ·
      can say why a gate on `close_ticket` is wrong whichever way it is set
- [ ] **1.2** read · ran `decide.py` · can name the three columns every row carries and say why the
      **ungated** rows need a `because` too
- [ ] **1.3** read · ran `decide.py --all-writes` · saw the tool-level gate be wrong for **20 of 24**
      real calls · can give the two `close_ticket` calls that break a tool-name gate
- [ ] **1.4** read · ran `scatter.py` · saw **2 of 4 call sites** let through a call the policy stops,
      and that **one of the two has a guard** that is out of date

## Section 2 — the tool gate

- [ ] **2.1** read · ran `toolgate.py` · saw pass 2 return an error dict with **`effects: []`** · can
      say why the empty ledger is the evidence and the return value is not
- [ ] **2.1** broke it: changed `gate_close` to take `**kwargs` and watched the gate stop firing
- [ ] **2.2** read · ran `pending.py` · read the default `hint` as if you were the approver and wrote
      down what you would put there instead · ran the three-attempt loop and saw
      **three refusals, `effects: []`**
- [ ] **2.3** read · compared the two error strings (`requires confirmation` against `is rejected`) ·
      found the `requested for:` line that appears under only one of them · can name the three states
      that `confirmed` cannot represent

## Section 3 — binding the answer

- [ ] **3.1** read · ran `pending.py` · found **both** ids (`fc-4655` and the `adk-` one) and can say
      what each identifies · ran the collision snippet and saw **`pending keys: ['fc-1']`** for two
      different tickets
- [ ] **3.2** read · found `originalFunctionCall` in the output · ran the camel/snake snippet and saw
      **`snake : None`** rather than an error
- [ ] **3.3** read · ran `toctou.py` and `toctou.py --no-checks` · saw **1 of 4** against **4 of 4** ·
      can name the three checks the real validator makes
- [ ] **3.4** read · ran `twice.py` and `twice.py --keyed` · saw **2 emails** become **1** · ran the
      threading-barrier snippet and saw the keyed version still send **twice** under concurrency ·
      reached the real `sqlite3.IntegrityError`
- [ ] **3.5** read · ran the key-discrimination snippet and saw **one `True`, three `False`** · ran the
      timestamp-defeat snippet and saw the key prevent **nothing** · can name the two ways a key is
      wrong and which one is silent

## Section 4 — the node gate

- [ ] **4.1** read · ran `nodegate.py` · saw **`effects after pass 1: []`** and the run *end* rather
      than block · ran the mismatch snippet and saw `approval:9999` produce **`effects: []` with no
      error**
- [ ] **4.2** read · ran `rerun.py` · saw **`ask body executed 1 time(s)`** across both passes and the
      successor holding the approval · ran the typed-successor snippet and read the real
      `ValidationError` naming `str`, not the node
- [ ] **4.3** read · ran `nodegate.py --reject` and saw **`reply left the building: True`** after a
      human said no · ran `nodegate.py --guarded --reject` and saw it become **False** · ran the
      loose-vs-strict snippet and can say which of the four rows reaches a customer
- [ ] **4.4** read · ran all three arms of `rerun.py` · saw the stall: **body 2×, asked again, successor
      never ran** · can say what a node must do before yielding when `rerun_on_resume` is on
- [ ] **4.5** read · ran `nodetool.py` · saw the `ImportError` on the public path and
      **`'NodeTool' in __all__: False`** · saw `state_only` refused for having no `input_schema` · can
      name the two checks that show an API is unsupported

## Section 5 — the record

- [ ] **5.1** read · ran `trail.py` and `trail.py --reject` · saw the record change to
      `approved: false` / `refused` / **`effects: []`** with no audit code anywhere · can say why a
      `log.info` beside the send would be worse
- [ ] **5.2** read · matched all **six** rows of the table against the printed record · ran the
      policy-version drift snippet and saw **3 against 4** · can say why the version is stamped when
      the question is asked rather than when the effect runs

## Section 6 — wiring the desk

- [ ] **6.1** read · ran `desk.py`, `desk.py --ticket 4655`, `desk.py --ticket 4655 --reject` · saw
      **6 stations / 0 humans**, then **`gate -> gate -> send`**, then **`park`** with `effects: []` ·
      can say why the gate sits after `draft` and before `send`
- [ ] **6.1** broke it: ran `norerun.py --plain` and `norerun.py --mismatch` · saw both stop after
      `gate` with `effects: []`, one with a warning and one silent · can name the three situations that
      look identical from outside
- [ ] **6.2** read · ran `bypass.py` · saw **1 of 3** routes honour a policy that answered `True` ·
      grepped the lab for every `close_ticket` call site and counted the mediated ones
- [ ] **6.3** read · ran `gate.py` and saw **0/6, exit 1** with checks *skipped* · ran the weak-vs-strong
      snippet and saw **`True` / `False` on the same run** · can name, for each of the six checks, the
      innocent edit that turns it red

## Section 7 — in production

- [ ] **7.1** read · ran `latency.py` and `latency.py --all-writes` · saw **4 of 24** against
      **14 of 24**, peak depth **2** against **5**, and **0** against **2** still pending at the end ·
      changed `CAPACITY` to 4 and can say whether that rescues the naive policy
- [ ] **7.2** read · read the last line of both arms and saw the mean wait barely move (3.0 → 3.7)
      while **2 proposals went stale** · ran the stale-approval snippet and saw a proposal **20 slots**
      past an **8-slot** deadline still send · can name the four options and what each costs
- [ ] **7.3** read · ran the gate-body inspection and saw it reads `approved` and `by` and **nothing
      else** · ran the `by=` arms and saw **4 of 4** send, including `by=None` · can name the three
      questions inside "who approved this"

## The build brief

- [ ] `sutra/approval_policy.json` written — one row per action, `because` on **every** row including
      the ungated ones
- [ ] `sutra/approval.py` written — `needs_approval` pure and raising on an unknown action, `pending`
      carrying all six fields from 5.2, `decide` using `is True` and idempotent on 3.5's key
- [ ] `tests/test_approval.py` written — one test per check in §5
- [ ] **Break it, watch it go red, fix it:** remove the idempotency key from `decide`, run
      `uv run python days/day-64-approval-gates-build/lab/gate.py`, see **check 6 go red**, put it back,
      see it go green
- [ ] `uv run python days/day-64-approval-gates-build/lab/gate.py; echo "exit: $?"` is **6/6, exit 0**
- [ ] You can state the two gaps this day deliberately leaves open — expiry (7.2) and authorisation
      (7.3) — and why each is a decision rather than a default

## Gates

- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean
- [ ] `uv run python -m pytest -q -m "not live"` green
- [ ] `./m depth 64` green — 25 parts
- [ ] `./m trace` shows day 64 closing exactly **ADK-48, ADK-76**
- [ ] Request budget confirmed **0** — no provider was called

## Ledger & commit

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real hash filled in after committing
- [ ] No `docs/PACKAGES.md` row — confirmed `git diff pyproject.toml uv.lock` is empty
- [ ] No `docs/PAPERS.md` row — this day teaches no paper of its own
- [ ] Committed as `day 64: approval gates, built — closes ADK-48, ADK-76`
