# Day 65 — Definition of done

`./m done 65` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. This is a gate day, so several boxes ask you to record a number
or a verdict rather than to see something pass — a gate that finds nothing has not looked.

## Before you start

- [ ] Day 64's parts and checklist are done, and the triage graph's write step files an approval
      before it executes. If it does not, there is nothing for today's criterion 2 to test.
- [ ] `uv run python days/day-65-kill-it-mid-run/lab/gate.py; echo "exit: $?"` is **red** before you
      write anything, and you have read all of the findings rather than only counted them.
- [ ] `lab/` scaffolded per §3 — fourteen files — and `lab/state/` created.
- [ ] `git check-ignore -v days/day-65-kill-it-mid-run/lab/state/closed.jsonl` prints a matching
      rule. Nothing under `state/` may reach git (P9).
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — a drill, not a review

- [ ] **1.1** read · ran `drill.py` and saw all four kills · ran `drill.py --kill K3` and saw
      **`exit 1` with no traceback** because the signal came from outside · can say why a gate that
      finds nothing has either finished a phase or failed to look
- [ ] **1.2** read · ran `budget.py` and `budget.py --naive` · saw the naive count make a killed run
      look **1 request cheaper** than a clean one · rebuilt `n2` with `runner.py` and found the two
      `spent` lines for `research` that prove it · can turn "it recovers correctly" into a criterion
      by answering the four questions
- [ ] **1.3** read · ran the seven runbook steps by hand, in order, without `drill.py` · got
      `closes: 1` at the end · can say why step 5 names the approver

## Section 2 — the instrument

- [ ] **2.1** read · ran `drill.py --kill K1` and read `state/runs/k1.log` · found the **two
      `spent research` lines with one `stage research`** between the crash and the resume · ran
      `tear.py` and reached the real `json.decoder.JSONDecodeError: Unterminated string` · ran
      `tear.py --tolerant` and saw **12 events recovered** · can say what `fsync` buys over `flush`
- [ ] **2.2** read · ran `deaths.py` · saw **`raise` and `sysexit` both recover the unflushed line and
      `oshard` reach the file with nothing** · can say which of the three is what a crash looks like
- [ ] **2.3** read · ran `runner.py start 4610 --run-id m1 --kill-at research` · saw **`exit: 137`
      and `spend: 1`** · can name the four moments and the question only each one answers

## Section 3 — four kills

- [ ] **3.1 (K1)** read · ran `drill.py --kill K1` · saw the resume print **`spent 3 requests`** and
      the run close once · can explain why the log knows about a request no output mentions
- [ ] **3.2 (K2)** read · ran `drill.py --kill K2` · saw the resume print **`spent 1 requests`** ·
      ran `runner.py resume z2 --no-skip` and saw it become **`spent 4 requests`** · ran
      `runner.py resume z3 --done-from-spend` and reached the real **`KeyError: 'draft'` raised inside
      `_desk.review`, not in `file_approval`** · can say why it raises there
- [ ] **3.3 (K3)** read · ran `drill.py --kill K3` · saw the first resume cost **`spent 0 requests`**
      · counted the lines in `k3.log` against the `12 events on disk` the resume reported · can give
      the difference between waiting as a process and waiting as a state
- [ ] **3.4 (K4)** read · ran `drill.py --kill K4` · saw **`closes for this intent: 1`** and
      `close applied` · looked at `state/effects.jsonl` and found it **empty** in `keyed` mode · can
      name the three orders and the failure each produces
- [ ] **3.5** read · ran `drill.py --kill K4 --mode unsafe` and saw **2 close rows with identical
      keys, exit 0** · ran `--mode drop` and saw **`close replayed`, 0 close rows, exit 0** · found
      the line in `drill.py` that turns the count into an exit code · can say why a process cannot
      detect that it has performed an effect for the second time

## Section 4 — the trail

- [ ] **4.1** read · ran `trail.py` and got **4 of 4 answered** · read
      `state/approvals/appr-t1.json` and found, from those rows alone, what text the operator saw ·
      can state the four questions in order and say which one most approval systems fail
- [ ] **4.2** read · ran `trail.py --thin` and saw **2 of 4 unanswerable** with the run itself
      completely unaffected · noticed that question 2 prints a plausible-looking string rather than a
      blank · can explain why a pointer that still resolves is worse than one that is broken
- [ ] **4.3** read · went through all nine fields of the approval record and named the question each
      one answers · accounted for the fields that answer none of the four · can say what is wrong
      with a field that answers no question, without using the word "clutter"

## Section 5 — seven criteria

- [ ] **5.1** read · ran `drill.py > /dev/null; echo $?` and got **0** · ran `--mode unsafe` and got
      **1** · ran `--kill K1 --mode unsafe` and got **0**, and can explain why that is the argument
      against trimming a drill for speed
- [ ] **5.2** read · ran `bypass.py` (**0 findings**) and `bypass.py --trust-state`
      (**1 finding, the executed payload was not the approved payload**) · noticed that attempts 1, 2
      and 3 print identically in both runs · can describe the payload swap without using the word
      "hash"
- [ ] **5.3** read · ran `trail.py` (exit 0) and `trail.py --thin` (exit 1) · ran `drill.py`
      afterwards and saw it still green, and can say what that proves about the other criteria
- [ ] **5.4** read · ran `budget.py` · recorded the four scenario costs and the **durability premium
      of 1 request** · can say why a rejected run costs full price and what that implies for gating a
      high-volume action
- [ ] **5.5** read · ran `fresh.py` · read both findings · decided what the correct response to the
      `google-adk` finding is, and can say in one sentence why it is not "upgrade it", citing a
      principle by number
- [ ] **5.6** read · ran `written.py` · for any day whose row says `NO`, named which of the two
      conditions it fails · can say why the check parses the plan instead of globbing `days/`
- [ ] **5.7** read · ran `ids.py` · read the open list as a worklist rather than a complaint · can
      give the difference between an ID being declared and a concept being taught, and name the tool
      that checks each
- [ ] **5.8** read · ran `gate.py; echo "exit: $?"` · sorted the findings into "clears when the phase
      finishes" and "needs a decision" · can state the Phase 9 verdict in one sentence a colleague
      could act on, without using the word "mostly"

## Section 6 — in production

- [ ] **6.1** read · ran `deaths.py` again with 2.2's table in mind · temporarily changed
      `os._exit(KILLED)` to `sys.exit(KILLED)` in `runner.py`, re-ran `drill.py`, recorded which
      criterion noticed, **and changed it back** · can say why a graceful shutdown that overruns its
      grace period is indistinguishable from a crash
- [ ] **6.2** read · picked one row from the table of next criteria and wrote the label and the one
      command it would need · can say why a finding that has been red for three gates is worse than
      one going red for the first time

## The build brief

- [ ] `sutra/gate.py` written by hand — `Criterion`, `run_gate`, no early exit
- [ ] the `accepted` field implemented, so a decided finding stops being red and carries its reason
- [ ] the red-alarm test generalised: every criterion with an `ablation` command is asserted to fail
- [ ] `tests/test_gate.py` written — `run_gate` returns non-zero when any criterion does, and reports
      **all** failing labels
- [ ] **break it on purpose:** delete the `and row["closes"] == 1` from `drill.py`'s verdict, run
      `drill.py --mode unsafe`, watch it go **green**, and put it back. That is the one-line version
      of the bug this whole phase exists to prevent.

## Gates

- [ ] `uv run python scripts/depth_check.py 65` → `OK day 65 24 parts`
- [ ] `./m trace` — day 65 claims exactly `OPS-11`, no more and no fewer
- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean over this day's files
- [ ] `uv run python days/day-65-kill-it-mid-run/lab/gate.py` run, and its verdict — **not your
      impression of it** — written into the ledger row

## Ledger & commit

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real commit hash and the gate column set to
      the colour the gate actually reported
- [ ] `docs/PACKAGES.md` row for `mcp` pasted from §11, after re-reading the pin in `pyproject.toml`
- [ ] no `docs/PAPERS.md` row (this day teaches no paper) and no `SKILL_PROVENANCE.md` row
- [ ] committed as `day 65: phase gate - kill it mid-run; durable triage with human approval - closes OPS-11`
