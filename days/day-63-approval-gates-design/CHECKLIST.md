# Day 63 — Definition of done

`./m done 63` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 62's parts and checklist are done, and you can name its four human-in-the-loop patterns
      without looking: approve or reject, edit, answer a question, take over (P2).
- [ ] `uv run python days/day-63-approval-gates-design/lab/gate.py; echo "exit: $?"` is **red** before
      you write anything, and you have read all **six** findings rather than only counted them.
- [ ] `lab/` scaffolded per §3 — twenty-seven files, two of them under `lab/papers/`.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — the gate that means nothing

- [ ] **1.1** read · ran `everything.py` · saw **41 asked, caught 2 of 6** against **11 asked, caught
      4 of 4** · ran `everything.py --careful 41` and saw gating everything win **6 to 4** · ran
      `--careful 10` and wrote down both rows · can say why a gate on every write can be less safe
      than one on a quarter of them **without using the word fatigue**
- [ ] **1.2** read · ran `permission.py` · can state what an approval does that an allowlist cannot,
      and name one thing an allowlist does better
- [ ] **1.3** read · ran `four.py` · can recite the four questions — which actions, what evidence,
      whom, and what a "no" means — and say which one this day answers in each section

## Section 2 — sorting the actions

- [ ] **2.1** read · ran `undo.py` · can say why `close_ticket` is `reversible: True` in the facts and
      gated anyway, and which rule ordering makes that happen
- [ ] **2.2** read · ran `radius.py` · can name the four radius values and give a Sutra action at each
- [ ] **2.3** read · ran `visible.py` · can explain why `detect_hours` is a claim about people rather
      than a property of the code
- [ ] **2.4** read · ran `volume.py` · can say why frequency is deliberately **not** one of
      `suggest()`'s five rules, and what would go wrong if it were

## Section 3 — the policy table

- [ ] **3.1** read · ran `inventory.py` · saw **10 actions, 10 policy rows, no differences** and the
      two rows *written before the tool exists* · added an action to `_actions.py` with no `POLICY`
      row and watched it appear in a difference list · removed it again
- [ ] **3.2** read · ran `table.py --suggest` and `table.py` · saw **one row out of ten** where the
      decision overrules the arithmetic · applied the disagreement test to one `never` row's `because`
      · can say what would be lost by tuning `suggest()` until it always agrees
- [ ] **3.3** read · ran `free.py` · saw the ungated writes cost **28 approvals a night** that nobody
      is asked for and let **2** mistakes through · flipped `record_triage` to `always`, re-ran
      `everything.py`, watched the policy row get worse, and put it back
- [ ] **3.4** read · ran `unknown.py` and `unknown.py --open` · saw **52 asked / 0 unreviewed** against
      **0 asked / 52 unreviewed, 3 of them wrong** · reached `KeyError: 'merge_duplicate_tickets'` on
      purpose · can say what `POLICY.get(action, NEVER)` claims, in a sentence fit for a design doc

## Section 4 — what the approver sees

- [ ] **4.1** read · ran `bind.py` (**exit 1**, `ApprovalMismatch`) and `bind.py --by-reference`
      (**exit 0**, wrong reply sent) · made the two drafts identical and confirmed it stops raising ·
      can explain the failure using the words *resume* and *at-least-once*
- [ ] **4.2** read · ran `diff.py` · saw **0/3 detectable from the request screen, 3/3 from the diff**
      · noticed that **all three tells are in unchanged fields** · deleted `linked_bug` from
      `ticket:4623`'s `before` dict, re-ran, and can say why the summary still printed `3/3`
- [ ] **4.3** read · ran `duty.py` · saw **two signatures, zero catches** on the middle arrangement ·
      picked one pair and decided whether the agent's sentence was false or merely a conclusion drawn
      from less than the reviewer had
- [ ] **4.4** read · ran `record.py` · saw the four shapes answer **0, 1, 2 and 4** of four · can name
      the four questions in the order an incident review asks them · can say what a `session_id`
      actually proves after a resume

## Section 5 — when nobody answers

- [ ] **5.1** read · ran `absent.py` · saw **one of four** actions fail open · wrote both halves of
      `refund_order`'s pair in your own words and named the property that decides between them
- [ ] **5.2** read · ran `timeout.py` (**11 answered by a constant**) and `timeout.py --hours 12`
      (**11 answered by the rota**) · found the smallest `--hours` at which at least one is answered by
      the rota · can say what real-world fact that number measures
- [ ] **5.3** read · ran `breakglass.py` and `breakglass.py --quiet` · noticed `reason: same` on three
      of four rows and can say why that is the useful signal · checked the three override ticket
      numbers against 4.2's wrong closes and wrote down what break-glass did **not** prevent

## Section 6 — gates that are decoration

- [ ] **6.1** read · ran `around.py` · saw **6 tickets closed, 3 approvals asked**, nothing bypassed
      and no error raised · counted by hand which `record_triage` calls closed a ticket · can say why
      the fail-closed default from 3.4 does not fire here
- [ ] **6.2** read · ran `talkpast.py` and `talkpast.py --independent` · saw **2 wrong pages → 0** with
      the predicate unchanged · named a field in Sutra the agent does not write that could decide the
      same case
- [ ] **6.3** read · ran `shopping.py` (**3 attempts, approved**) and `shopping.py --once`
      (**1 attempt, rejected**) · wrote down the two refusal reasons · named the Sutra **feature**, not
      an attacker, that would re-file the request on its own
- [ ] **6.4** read · ran `stamp.py` · saw the policy column go **flat from `careful_for=11`** while
      gate-everything moves **0 → 6** across the range · found the smallest value at which the policy
      column peaks and compared it with the queue length · can state the difference between a design
      being right and a design being insensitive

## Section 7 — the two doors

- [ ] **7.1** read · ran `doors.py` · saw the predicate answer `False` at P1 and `True` at P3 · saw
      `TypeError: by_severity() missing 1 required positional argument: 'severity'` and can say where
      the predicate's arguments come from · saw the `[EXPERIMENTAL]` warning · can name the documented
      limitation that rules this door out for Sutra
- [ ] **7.2** read · ran `doors.py` · can name the four `RequestInput` fields and say **where the
      human's reply goes by default** · added a `response_schema` and confirmed it appears · can say
      what the framework does if a reply does not match it
- [ ] **7.3** read · ran `gate.py` · picked one `cannot check` line and traced it back to the part that
      argued for it · can state what Day 64 finishing means as a command, and name the one thing this
      check cannot verify

## The paper — read after the parts

- [ ] **papers/01** read · ran `demo.py` (**refused, mallory 0, exit 0**) and `demo.py
      --no-separation` (**mallory 90000, exit 1**) · found the audit-log line that is a complete and
      honest record of a fraud · changed the executor to `dave` and can say whether the fraud is
      prevented and what that shows about which rule is doing the work
- [ ] Can answer out loud: what did this paper claim, which rule survived into everyday practice, and
      what replaced the half that did not

## Build brief

- [ ] `sutra/approvals.py` created; `POLICY`, `Row`, `gate_for()` and `threshold_allows()` ported with
      the `because` sentences **verbatim**
- [ ] Decided whether `suggest()` comes across, and wrote the reason in the module docstring
- [ ] `fails_open` added as a **column**, three closed and one open — not a module constant
- [ ] `timeout_hours` added as a column, set from the rota's real reading time rather than a
      comfortable-sounding number
- [ ] `tests/test_approvals.py` created with one test per `cannot check` line — five of them
- [ ] **Broke one on purpose:** deleted a `because`, watched the test go **RED**, put it back
- [ ] The gate is **not** wired into the triage graph. That is Day 64.

## Gates

- [ ] `uv run python scripts/depth_check.py 63` → `OK day 63 25 parts + 1 papers`
- [ ] `uv run ruff check .` and `uv run ruff format --check .` clean over this day
- [ ] Every relative link in the day resolves — the cross-day ones into days 22, 40, 47, 49, 50 and 60
      were checked with `ls`, not assumed
- [ ] `lab/gate.py` still exits **1** until the build brief is done, and exits **0** after

## Request budget

- [ ] **0 requests** to every provider. No model was called. If you called one, say which and why in
      the commit message rather than leaving the table wrong.

## Ledger & commit

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real hash after committing
- [ ] `docs/PAPERS.md` already carries the `doi:10.1109/SP.1987.10001` row — confirmed, not duplicated
- [ ] `docs/PACKAGES.md` unchanged — no package added
- [ ] Committed as `day 63: approval gates - design (what needs a human, and why) - closes SEC-05, ADK-47`
