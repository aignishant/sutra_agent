# Day 60 — Definition of done

`./m done 60` refuses to commit until every box is ticked. Tick a box only when you have actually
run the thing, not when you have read it.

## Before you start

- [ ] Day 59's parts and checklist are done, and the triage graph runs end to end on one ticket.
- [ ] `grep google-adk pyproject.toml` and
      `uv run python -c "import google.adk; print(google.adk.__version__)"` **agree**. If they do
      not, stop and fix the pin before anything else (P7).
- [ ] `uv run python days/day-60-durable-execution/lab/gate.py; echo "exit: $?"` is **red**
      (`exit: 1`, one finding) before you write a line.
- [ ] `lab/` scaffolded per §3 — twenty-five scripts plus `lab/papers/distributed-snapshots/` —
      and `tests/test_durable.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — what a run is

- [ ] **1.1** read · ran `nolog.py` and `nolog.py --log` · saw **5 model calls against 3**, and
      **2 wasted against 0** · `cat nolog.jsonl` and can say what one line contains · moved the
      `record` call to before the stage and can say what that does to `review`
- [ ] **1.2** read · ran `died.py` and `died.py --bad-input` · saw `stage_finished` /
      `resumable: True` against `run_failed` / `resumable: False` · can say why a killed process
      writes nothing on its way out · can explain why catching `BaseException` in the failure
      handler is the dangerous version
- [ ] **1.3** read · ran `safe.py` and saw **two closure rows for one ticket with nothing
      raised** · ran `nokey.py` and `nokey.py --compensate` and watched the inbox go **2 → 3** ·
      added a sixth stage marked `pure` that writes to a file and can name the column that
      catches the lie

## Section 2 — the log is the run

- [ ] **2.1** read · ran `whatstate.py` · saw **5 state fields rebuilt from 3 lines** · ran
      `whatstate.py --stage review` · deleted the middle line of `whatstate.jsonl` by hand and
      can say which of the four answers changed
- [ ] **2.2** read · ran `replay.py` — **0 model calls, 7/7 fields identical, one closure row** ·
      ran `replay.py --truncate 2` and saw 5 fields and 2 stages left · ran `rebuild.py` and
      `rebuild.py --durable-guard` and watched replies go **2 → 1** · can say why the in-memory
      guard ran correctly both times
- [ ] **2.3** read · ran `clock.py` and `clock.py --seeded` · saw `sample` go from `8886/6718` to
      `7337/7337` while `stamp` stayed `NO` in both arms · ran `--seeded` twice and compared
      across runs · can say why the clock has no seed
- [ ] **2.4** read · ran `secondopinion.py` and saw **`auth-bug` then `data-loss`, two queues** ·
      ran `--recorded` and saw one label · ran `--recorded --stale-context --loose-key` and saw a
      **silent wrong hit** · ran `--recorded --stale-context` and read the `ValueError` naming
      both prompt hashes · `grep model secondopinion.jsonl`
- [ ] **2.5** read · ran `cut.py` — **11 on every row for a desk that holds 10** · ran
      `cut.py --consistent` — **10 on every row, with the in-transit ticket named** · ran
      `cut.py --verify` and saw the `AssertionError` fire on the first row · reversed the two
      counts in the two-moment arm and can say which way the error goes

## Section 3 — doing it twice

- [ ] **3.1** read · ran `inflight.py` — log says `draft`, world has **1 closure**, they disagree,
      resume closes it twice · ran `inflight.py --record-first` — log says `review` finished,
      world has **0 closures**, *"the ticket is never closed and nothing complains"* · can say
      which of the two you would rather ship and why
- [ ] **3.2** read · ran `natural.py` and saw `closed/closed/closed` against `1/2/3` against
      `1/1/1` · ran `natural.py --stamp` and saw **`close -> customer told: -5.31 h`** · ran
      `--stamp --coalesce` and saw it return to `+0.00` · added a fourth insert-if-absent column
      and can say which group it really belongs to
- [ ] **3.3** read · ran `keys.py` — **3 closure rows** — and `keys.py --derived` — **1** · can
      recite the three components of the key and say why each one is there · dropped the step
      name from the key, added a second write, and can say which write disappeared
- [ ] **3.4** read · ran `atomic.py` — **closures=1 keys=0 after the crash, then 2 closures** ·
      ran `atomic.py --atomic` — **1 and 1, second attempt refused** · ran `atomic.py --race` and
      read the `IntegrityError` · moved the crash before the closure insert and wrote down both
      counts
- [ ] **3.5** read · ran `atleastonce.py` and `atleastonce.py --dedupe` · saw **3 delivered in
      both arms** and **effects 3 → 1** · noticed the caller receives `closure_seq: 3` in one arm
      and `closure_seq: 1, replayed: True` in the other · can state the at-least-once equation
      out loud

## Section 4 — the ADK surface

- [ ] **4.1** read · ran `adk.py --arm config` · read the docstring's two caveats **out of the
      installed package** · removed `resumability_config` from `build()`, ran `--arm resume`, and
      can say which caveat you stopped being protected by
- [ ] **4.2** read · ran `adk.py --arm refuse` · noticed the **same error with the switch on and
      off** · ran `--arm resume --carry-on-state` twice and compared the two invocation ids · can
      say what a supervisor would need to resume that run tomorrow
- [ ] **4.3** read · ran `adk.py --arm events` · found `classify` at **status 3** and `research`
      frozen at **status 2** · can name what statuses 2 and 3 mean without looking · added a
      fourth node and counted the events and the size of the last `agent_state`
- [ ] **4.4** read · ran `adk.py --arm rerun` and saw **`False → research 1, draft saw neighbour
      False`** against **`True → research 2, saw neighbour True`** · ran `--arm resume` and read
      the `ValidationError: input_value=None` · ran `--arm resume --carry-on-state` · set
      `rerun_on_resume=True` on `draft` too and can explain why `draft runs` did not change

## Section 5 — the triage graph made durable

- [ ] **5.1** read · can put all five stages in their class **from memory** and give the
      obligation each class carries · noticed that `safe.py`'s `2nd run identical` column says
      `True` for `classify` and can explain why that is measuring the stub
- [ ] **5.2** read · ran `resume.py` and can read the staircase against the flat `restart`
      column · ran `size.py` — **618 bytes** — and `size.py --keep-output` — **831** · worked out
      how many runs a day make the untrimmed log cost more than one model request

## Section 6 — the failure lab

- [ ] **6.1** read · ran `version.py` and saw **`drafted against ticket=None` with nothing
      raised** · ran `version.py --stamped` and saw the refusal · set `CODE_VERSION` to `1` and
      then to `3` and can say which is more likely in a real incident
- [ ] **6.2** read · ran `kills.py` — four clean rows and **`inside review: 4 requests, 2
      closures, honest NO`** · ran `kills.py --keyed` — **2 closures → 1, honest yes, requests
      still 4** · can say why the request count did not change · added a kill inside `draft` and
      can explain the result using section 5's classes

## Section 7 — in production

- [ ] **7.1** read · ran `size.py` both ways · ran the `nolog.py --log` / `rm nolog.jsonl` /
      `nolog.py` sequence and watched a resume become a restart · wrote the **three** retention
      rules as three numbers and can say which one you are least sure about
- [ ] **7.2** read · answered all six questions about Sutra out loud without looking · can say
      which three are about the record and which three are about the effect · found the one you
      could not answer and named the part it belongs to

## The paper

- [ ] **01 — Distributed snapshots** read, **after** the parts · ran
      `demo.py` (**consistent, total 6, exit 0**) and `demo.py --no-markers`
      (**IMPOSSIBLE, lost 2, exit 1**) · disarmed rule 3 in `snapshot.py` and saw
      **total 5, lost 1** · can answer *what did it claim, and what do we do differently now*

## Build brief

- [ ] `sutra/durable.py` written: `record_step`, `finished_steps`, `resume`, `idempotency_key`
- [ ] `resume` imports **no** stage function — check it, do not assume it
- [ ] `idempotency_key` returns the **same** string for the same run, step and subject
- [ ] `close_ticket` takes a `request_id` and is added to `IDEMPOTENT_TOOLS`
- [ ] resumability turned on in the **app factory**, so tests and the worker share it
- [ ] `rerun_on_resume` set **explicitly on every node** of the triage graph
- [ ] a schema version on every event, and a resume that refuses on mismatch

## Tests and the gate

- [ ] `tests/test_durable.py` written: a resume test, an idempotency test, and a
      kill-inside-the-write test that asserts **one** closure row
- [ ] `uv run python -m pytest tests/test_durable.py -q` green
- [ ] `uv run python days/day-60-durable-execution/lab/gate.py; echo "exit: $?"` → `exit: 0`
- [ ] **break it, watch it go red, fix it:** change `idempotency_key` to append
      `str(time.time())`, re-run `gate.py`, confirm it **fails**, then put it back
- [ ] `uv run python scripts/depth_check.py 60` green
- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean for everything you wrote
      (the pre-existing `tests/test_persona.py` `I001` from Day 15 is not yours)

## Request budget

- [ ] **0** requests to every provider, confirmed: no arm of any script today makes a network
      call, and `git diff pyproject.toml uv.lock` is still empty

## Ledger and commit

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PAPERS.md` row for `doi:10.1145/214451.214456` present
- [ ] no `docs/PACKAGES.md` row, because no package was added
- [ ] committed as `day 60: durable execution — resume, replay, idempotency — closes AG-22, ADK-43`
