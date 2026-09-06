# Day 68 — Definition of done

`./m done 68` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. Several boxes ask you to record a number or a list, because a
permission you cannot state is a permission you have not granted deliberately.

## Before you start

- [ ] Day 67's parts and checklist are done. Today builds the control its last part said was needed:
      a rule that never reads the text.
- [ ] `lab/` scaffolded per §3 — thirteen files, plus two under `lab/papers/confused-deputy/`.
- [ ] `git check-ignore -v days/day-68-least-privilege-tools/lab/state/private/payroll.csv` prints a
      matching rule. Nothing under `state/` reaches git (P9).
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.
- [ ] `uv run python days/day-68-least-privilege-tools/lab/gate.py; echo "exit: $?"` is **red** before
      you write anything, and you have read all six findings rather than counted them.

## Section 1 — the deputy

- [ ] **1.1** read · ran `deputy.py` · can say in one sentence which half of *"acts on instructions
      you do not control while holding authority you do control"* is yours to change
- [ ] **1.2** read · ran `deputy.py` · can say why a tool does not know what it was for, and what
      that means for a tool whose arguments came out of a ticket
- [ ] **1.3** read · ran `whose.py` and `whose.py --scoped` · can say why `tool_context` is invisible
      to the model, and why the two refusals in the scoped version are deliberately identical
- [ ] **1.4** read · can say why an instruction in the prompt is advice and a missing tool is a
      boundary, and name the earlier day that measured what instructions are worth

## Section 2 — three questions

- [ ] **2.1** read · ran `table.py` · can state the three questions a grant must answer and say why
      the read/write line is the one that matters most
- [ ] **2.2** read · ran `whose.py` · can say what a capability with no scope is a capability over
- [ ] **2.3** read · ran `rate.py` · recorded the rates in `permissions.json` — **60/min**, **20/min**,
      **10/min** — and can say why rate is a permission rather than an operational setting
- [ ] **2.4** read · ran `table.py` and read `permissions.json` · can name all five columns and say
      which two questions the table makes askable

## Section 3 — absent, not forbidden

- [ ] **3.1** read · ran `absent.py` · can say why an allowlist and a trimmed list agree today and
      diverge the day a tool is added
- [ ] **3.2** read · ran `absent.py --senior` · saw the offered list change with who is asking
- [ ] **3.3** read · ran `absent.py` and reached the real `ValueError` from the runtime · can say why
      that is correct and why it is not free
- [ ] **3.4** read · ran `handover.py` · recorded what the helper was offered under **`sub_agent`**
      and under **`agent_as_tool`**, and can name the one tool that differs between them

## Section 4 — the argument

- [ ] **4.1** read · ran `escape.py` · can name the three ways to constrain an argument and say which
      is weakest and why
- [ ] **4.2** read · ran `escape.py` against `../private/payroll.csv` · can say why resolving the path
      first is the only check that survives every spelling
- [ ] **4.3** read · ran `recipient.py` · can state the rule as it appears in the table's `scope`
      column — *the address on the ticket, never an address from its body*
- [ ] **4.4** read · ran `where.py` and `where.py --plugin` · saw the identical two requests come out
      differently · can quote what adk.dev says about plugin hooks being global
- [ ] **4.5** read · ran `leak.py` and `leak.py --opaque` · recorded **4 of 6** and **3 of 6** · can
      say precisely what the opaque refusal buys and what it does not, and where the reason has to go
      instead

## Section 5 — failure lab

- [ ] **5.1** read · ran `where.py` · saw `update_ticket` close ticket **9001** after `close_ticket`
      was refused · can say how you would find this class of bug (enumerate effects, not tools)
- [ ] **5.2** read · ran `table.py` and `table.py --drift` · saw **`['export_tickets']`** appear as a
      tool with no row · can say why the two directions of the diff are different findings
- [ ] **5.3** read · ran `handover.py` · saw the chain `desk -> researcher -> desk` end with
      **`tools actually called: ['refund']`** · can state the conclusion: a permission table is a
      property of the system, not of one agent in it

## Section 6 — in production

- [ ] **6.1** read · read the `credential` column in `permissions.json` · can say why a credential
      that does not exist cannot be wrong, and name the operational cost of one credential per tool
- [ ] **6.2** read · ran `table.py --used` · recorded **granted and never used: `['read_note']`** ·
      can say why *used and not granted* is a different finding that should page somebody

## The paper — read it last

- [ ] `papers/01-the-confused-deputy.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/confused-deputy/`: `demo.py` **exits 0** with
      `billing intact`, `demo.py --by-name` **exits 1** with `billing destroyed`
- [ ] Can say what is identical between the two runs and what the one difference is — a filename
      versus a capability the caller already held
- [ ] Can name one thing the paper's approach does **not** solve

## Build brief

- [ ] `sutra/permissions.py` written: the table loaded as data, a `BasePlugin` fence, argument-level
      checks, and rate enforcement
- [ ] You decided where the rate counter lives and wrote the reason in the module docstring
- [ ] `tests/test_permissions.py` written, including the test that a tool with **no row** is refused
- [ ] `uv run python gate.py; echo "exit: $?"` re-run after the build brief, and you can say which
      findings cleared

## Repo hygiene

- [ ] `./m depth 68` green — twenty-two parts and one paper
- [ ] `./m trace` green, and SEC-10 and SEC-11 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-68.md` are not stale
- [ ] `uv run ruff format --check days/day-68-least-privilege-tools` clean — Python inside fences is
      formatted like Python anywhere else
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1145/54289.871709` present and dated, with the record checked
      live rather than recalled (P7, §17.4.1)
