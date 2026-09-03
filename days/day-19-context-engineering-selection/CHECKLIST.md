# Day 19 — CHECKLIST

**IDs closed:** AG-08, AG-09
**Principles served:** 1, 2, 3, 4, 6, 8, 10, 11, 12, 15, 16, 17, 18
**Parts:** 16 across 6 sections, plus 1 paper

> `./m done 19` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-19-context-engineering-selection/lab
uv run python envelope.py
uv run python the_menu.py
uv run python history_grows.py
uv run python where_it_lands.py
uv run python distil.py
uv run python selection.py
uv run python organs.py
uv run python subscription.py
uv run python not_in_the_window.py
uv run python when_to_compact.py
uv run python weigh.py            # 3 count_tokens calls, 0 generations
uv run python three_costs.py      # 3 count_tokens calls, 0 generations
uv run python to_tokens.py        # 2 count_tokens calls, 0 generations
cd papers/lost-in-the-middle
POSITION=start  uv run python positions.py   # 3 generations
POSITION=middle uv run python positions.py   # 3 generations
POSITION=end    uv run python positions.py   # 3 generations
cd -
uv run python -m pytest tests/test_context.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: four numbers per turn with the tools column three and a half times the instruction; six tools
costing 1,855 characters; turn ten costing 21x turn one; a fact drifting from 81% to 11%; sixty log
lines becoming two; two packing strategies with very different totals; a state key that is present in
your code and absent from the request; and three positions that may or may not differ on your model.
Then `7 passed`, then `OK all green`, then `traceability: 36/199 closed, 0 problem(s)`, then one commit
reading `day 19: context engineering I - what earns a place in the window - closes AG-08, AG-09`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 18's count before you change anything
- [ ] Ran `envelope.py` **first**, before reading section 2's parts
- [ ] Can say which three scripts need a key, and why none of them spends generation quota
- [ ] Wrote down your prediction for `organs.py` **before** running it

## Section 1 — the window is a budget

- [ ] Ran `weigh.py` and can quote both token counts (1.1)
- [ ] Can name the three costs that grow with every token, and which has no error message (1.1, 1.2)
- [ ] Ran `three_costs.py` with a log line of your own and recorded the chars-per-token ratio (1.2)
- [ ] Ran `history_grows.py` and can explain both ratios at the bottom (1.3)
- [ ] Changed the range to 40 and looked again (1.3)
- [ ] Can say why the cumulative column is not a straight line (1.3)

## Section 2 — the anatomy

- [ ] Ran `envelope.py` and can explain all four columns (2.1)
- [ ] Deleted one tool, re-ran, and watched the tools column change (2.1)
- [ ] Noticed the line ADK appends after your instruction (2.1)
- [ ] Can name the six organs and who packed each one (2.2)
- [ ] Ran `organs.py` and compared the result with your written prediction (2.2)
- [ ] Ran `the_menu.py` and can quote the marginal cost of one tool (2.3)
- [ ] Understand why `str(request.config.tools)` is the wrong instrument (2.1, 2.3)
- [ ] Ran `subscription.py` with your own agent's instruction pasted in (2.4)
- [ ] Can give the one-sentence test for what belongs in an instruction (2.4)

## Section 3 — selection

- [ ] Can give the selection rule for each of the six organs from memory (3.1)
- [ ] Ran `selection.py` and can say which single rule saved the most (3.1)
- [ ] Ran `distil.py` and read the two surviving lines (3.2)
- [ ] Made the filter match `INFO` too and watched the ratio collapse (3.2)
- [ ] Can say where the evidence goes when you send only the finding (3.2)
- [ ] Ran `where_it_lands.py` and can explain why one column never changes (3.3)
- [ ] Can state the position finding in one sentence (3.3)

## Section 4 — the scale

- [ ] Ran `to_tokens.py` and recorded both chars-per-token ratios (4.1)
- [ ] Can say when to measure in characters and when to convert (4.1)
- [ ] Ran `weigh.py` with a real log of your own in place of the repeated line (4.2)
- [ ] Can state the caveat that makes the curated-versus-kitchen-sink comparison honest (4.2)

## Section 5 — the failure lab

- [ ] Ran `not_in_the_window.py` and saw three keys with one `True` (5.1)
- [ ] Added a second placeholder and watched a line change (5.1)
- [ ] Can name the only two ways a state key reaches the model (5.1)
- [ ] Can give the three-step diagnostic order for "the agent forgot something" (5.1)

## Section 6 — production

- [ ] `tests/test_context.py` written and green: `7 passed` (6.1)
- [ ] Made `weigh` return `0` for tools and confirmed a test goes red (6.1)
- [ ] Can name the two assertions in the file that are unusual, and why (6.1)
- [ ] Set the four `BUDGET` numbers from **your** measurements, with a sentence each (6.2)
- [ ] Raised the message budget, confirmed a test went green that should not have, then reverted (6.2)
- [ ] Can say why the budget alerts rather than blocks (6.2)
- [ ] Ran `when_to_compact.py` with your own measured per-turn increment (6.3)
- [ ] Wrote down the turn number at which compaction should run — tomorrow's input (6.3)

## The paper — after the parts

- [ ] Read `papers/01-lost-in-the-middle.md` **after** finishing the parts
- [ ] Ran the demo at all three positions, with as many questions as your quota allowed
- [ ] Pasted your real transcripts into your notes, including any 429
- [ ] Can say what the paper claimed, and what today's demo could and could not reproduce
- [ ] Can name one thing from the paper that survived and one thing that did not

## The build

- [ ] `sutra/context.py` written: every symbol in the hub's §4 table
- [ ] `weigh` measures four organs and the docstring says why not six
- [ ] `over_budget` returns names rather than a boolean, and you can say why
- [ ] `distil` has a cap, and you can say what happens on the day everything matches
- [ ] `git diff` confirms nothing under `sutra/desk/` changed unless you decided it should

## Request budget

- [ ] Generations spent today: **≤ 9 of 20** — write down the number you actually used
- [ ] `count_tokens` calls: **8** — and you can say why they are not generations
- [ ] No script invented a result when a call failed; every 429 exited non-zero

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the date and hash you actually observed
- [ ] `docs/PACKAGES.md` — no new rows, and you checked rather than assumed
- [ ] `docs/PAPERS.md` — the `arXiv:2307.03172` row is present
- [ ] `git status` glance: no `.env`, no pasted customer data in any lab script
- [ ] Committed as `day 19: context engineering I - what earns a place in the window - closes AG-08, AG-09`
