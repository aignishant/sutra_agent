# Day 62 — Definition of done

`./m done 62` refuses to commit until every box is ticked. Tick a box only when you have actually
run the thing, not when you have read it.

## Before you start

- [ ] Day 61's parts and checklist are done, and you can say what a checkpoint has to contain
      without looking it up. Today parks a run on purpose; yesterday made that possible (P2).
- [ ] `uv run python days/day-62-human-in-the-loop/lab/gate.py; echo "exit: $?"` is **red** before
      you write anything, and you have read which of the six checks it names.
- [ ] `lab/` scaffolded per §3 — twenty-one scripts plus `papers/ironies-of-automation/` — and
      `sutra/hitl.py` and `tests/test_hitl.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — the shape of the wait

- [ ] **1.1** read · ran `ask.py` and `ask.py --choice` · saw `long_running_tool_ids` name the
      pending call in both · ran `approve.py --reject` and saw the entire content of a "no" ·
      can name the four patterns and say what each does while it waits
- [ ] **1.2** read · ran `waiting.py` and `waiting.py --slots 8` · saw **held finish 5 and never
      start 5** against **stored finish 9 holding no slots** · saw four times the capacity buy
      what parking had for nothing · changed `HORIZON` to `60` and wrote down both numbers
- [ ] **1.3** read · ran `unreliable.py` · saw the naive handler send **twice** on a double answer
      and send **after the deadline** on a late one · saw two of the guarded handler's four
      outcomes be the word *ignored* · added a fifth history where the person answers `False`
      then `True` and can say which behaviour you would want on a send action

## Section 2 — approve or reject

- [ ] **2.1** read · ran `approve.py` and `approve.py --reject` · saw one call become two and the
      pause carry `originalFunctionCall` and `toolConfirmation` · can say what the anchor is for
- [ ] **2.2** read · ran `perticket.py` · saw ticket **4633 with refund 2400 stop** and **4610 with
      refund 0 go straight through**, same tool, same wiring · can say why a threshold beats
      gating the tool
- [ ] **2.3** read · ran `retry.py` and `retry.py --reason` · saw the reason **discarded** and the
      person asked **twice** in both arms · can say what a rejection must write instead

## Section 3 — edit

- [ ] **3.1** read · ran `edit.py` and `edit.py --asis` · saw **156 characters drafted and 132
      sent** · printed the tool declaration and saw `tool_context` absent from it · can say why a
      tool that omits the parameter fails open silently
- [ ] **3.2** read · ran all four arms of `tamper.py` · saw `ValueError: Function call arguments
      mismatch` and `Function call name mismatch ... history has 'send_reply', confirmation has
      'refund'` · saw `--ungated` refused for the same reason · can say what ADK compared
- [ ] **3.3** read · ran `audit.py --thin` and `audit.py` · saw **2 of 5** questions answerable
      against **5 of 5** · added a sixth question about editing and named the field that answers it
- [ ] can state, in one sentence, why every record saying "the agent sent this reply" is false
      under the edit pattern

## Section 4 — ask a question

- [ ] **4.1** read · ran `ask.py` beside `approve.py` and compared the two `args` lines · verified
      `request_input` and `get_user_choice` are both `LongRunningFunctionTool` with
      `is_long_running = True` · can give the one-sentence difference between approve and ask
- [ ] **4.2** read · ran `ask.py --choice` · removed `neither` from `OPTIONS`, ran it again, and
      wrote down what a reviewer whose real answer was "neither" would have to do
- [ ] **4.3** read · ran `avoidable.py` · saw **5 of 7** questions already answered by the ticket ·
      added an eighth question of your own and decided whether it maps to a field or to `None`

## Section 5 — take over

- [ ] **5.1** read · ran `takeover.py` · saw **still open: 0 and replies sent: 1** together · can
      say why a system with a boolean `decision` cannot express this outcome
- [ ] **5.2** read · ran `takeover.py --naive` · saw **still open: 1** and no error anywhere ·
      printed both versions of `pending/4633.json` and listed every field that differs · can say
      why a leaked run gets more dangerous after somebody adds a timeout policy

## Section 6 — nobody answered

- [ ] **6.1** read · ran `default.py` · saw **approve send 2 wrongly**, **reject hold back 2**, and
      **escalate leave 4 open** · flipped one ground truth and watched the columns move · chose a
      policy for `send_reply` and a different one for a refund, and can defend both
- [ ] **6.2** read · ran `stale.py` and `stale.py --guard` · saw the digest go **41b4d09f1d1b →
      a0ecddf0b4d6** and the unguarded arm tell a customer something untrue · added `subject` to
      `snapshot()` and can give your rule for which fields belong in a digest
- [ ] **6.3** read · ran `roundtrip.py` · saw **three pids for one run** and `sent.log` written by
      a process that never saw the draft · ran `resume 9999` and saw no work and no error ·
      deleted `draft` from the record `ask` writes and can say exactly where it failed

## Section 7 — what the human sees

- [ ] **7.1** read · ran `stamp.py` · saw **1/8, 5/8, 8/8** · ran
      `stamp.py --fields ticket,body` and saw **4/8 with a disjoint blind spot** · can state the
      ceiling claim in one sentence
- [ ] **7.2** read · ran `card.py` · saw the `Checks:` block turn two numbers twenty lines apart
      into `they disagree YES` · changed `CLAIMED_REFUND` to `2400` and said what the reviewer's
      job becomes · can give the rule for removing a check from a card
- [ ] **7.3** read · printed `ToolConfirmation.model_fields` and saw **three fields** · read the
      rejection branch in the installed source · can name three things a working gate needs that
      ADK does not provide, and say why it is right that it does not

## Section 8 — in production

- [ ] **8.1** read · ran `backlog.py` and `backlog.py --gate-rate 0.25` · saw the queue go
      **2 → 20 → 40 → 60** at 100% gated and stay **flat at 0** at 25% · ran `--gate-rate 0.5` and
      found where one reviewer stops coping · can say what a reviewer does when the queue gets long
- [ ] **8.2** read · can name the three numbers and the silent failure each one makes loud · can
      say why queue depth catches none of them

## The paper

- [ ] [Ironies of automation](papers/01-ironies-of-automation.md) read **after** the parts
- [ ] ran `demo.py` and `demo.py --no-automation` · saw the operator's error rate go **59.4% → 0%**
      while the system's went **26.8% → 50.0%** · can say why both being true at once is the point
- [ ] changed `THRESHOLD` to `0.30`, predicted three numbers before running, and found out which
      prediction was wrong
- [ ] can answer out loud: *what did this paper actually claim, and what do we do differently now?*

## The build

- [ ] `sutra/hitl.py` written: `ask`, `digest`, `answer`, `resume`, `EXPIRED`, `ON_TIMEOUT`, an
      outcome enum wider than a boolean, and `agent_sent`
- [ ] `oldest_open` and `yield_rate` written, and `oldest_open` run against the store
      `takeover.py --naive` leaves behind — you have decided whether the missing `asked_at` is a
      bug in the record or in the function, and can defend the answer
- [ ] `tamper.py` has `anchor_only()` and 3.2's exercise runs
- [ ] `ask.py` has a `--wrong` arm, and you have seen that nothing objects
- [ ] `tests/test_hitl.py` written, including a test that asserts the **pause happened** rather
      than that the tool returned (3.1's silent failure)

## Gates

- [ ] `uv run python days/day-62-human-in-the-loop/lab/gate.py; echo "exit: $?"` is **green**
- [ ] **break it on purpose:** delete `EXPIRED` from `sutra/hitl.py`, watch `gate.py` go red, name
      which check failed, put it back
- [ ] `uv run python -m pytest -q -m "not live"` passes
- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean
- [ ] `./m depth 62` green — 22 parts and 1 paper
- [ ] `./m trace` shows day 62 closing exactly `AG-23, ADK-46`

## Budget

- [ ] request budget confirmed **0** to every provider. If any script called a network, find out
      why before continuing (P15)

## Ledger & commit

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real hash
- [ ] `docs/PAPERS.md` row present for `doi:10.1016/0005-1098(83)90046-8`
- [ ] no `docs/PACKAGES.md` row needed, and `git diff pyproject.toml uv.lock` is still empty
- [ ] committed as `day 62: human-in-the-loop patterns - closes AG-23, ADK-46`
