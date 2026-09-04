# Day 28 — CHECKLIST

**IDs closed:** SK-09, SK-10, SK-11
**Principles served:** 1, 2, 4, 10, 11, 13, 15, 16, 17, 18
**Parts:** 16 across 5 sections, no paper

> `./m done 28` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python -c "from sutra.loop import TOOLS, KB; print(sorted(TOOLS), len(KB), 'kb articles')"
cd days/day-28-progressive-disclosure-design/lab
uv run python price_the_shelf.py
uv run python audit_the_shelf.py
uv run python routing_gate.py; echo "exit: $?"
uv run python crowd.py
uv run python containers.py
uv run python boundary_cases.py
uv run python misfile_cost.py
uv run python refactor.py
uv run python suspects.py
uv run python forty_skills.py
cd -
./m depth 28 && ./m check && ./m trace && git log --oneline -1
```

Expected: `['lookup_ticket', 'search_kb'] 2 kb articles`; then cards of **93** and **109**, bodies of
**654** and **375**, one reference at **142** and an index total of **214**; coverage with one
`(nothing)` row, four shared filler words and 17/24 words of their own; `worst margin: 1 (threshold 1)`
and `exit: 0`; `ties: 0` then `ties: 1` with one request won by `ticket-helper`; four containers holding
2, 2, 1 and 1; `20 / 8 / 0` deliveries against `0 / 3 / 0` chances to be skipped, and 2 KB articles;
**13080** against **5232** and **1704** against **2272** with 4 extra generations; two routing tables
with the **same** worst margin and the same `ties: 0`; `suspects: 4`; then 42 skills, `~4212` tokens,
861 pairs, `ties: 1` and an empty shared-filler set. Then `OK day 28 16 parts`, `OK all green`,
`traceability: 57/199 closed, 0 problem(s)`, and one commit.

## Setup

- [ ] The lab folder exists with **twelve** files, and `route.py` was written **first**
- [ ] Step 7's two commands were run and their output written down **before** any script was written
- [ ] **No `uv add` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] Nothing under `sutra/` was edited today

## Section 1 — `01-the-price-list`

- [ ] **1.1** read · redid the five-turn table for **both** skills activated and for **none** · said out
      loud which rung multiplies and which one costs a whole model round trip
- [ ] **1.2** read · wrote your guess for all six numbers **before** running it · ran it and noted the
      one you were most wrong about · **changed `refs` to print each reference separately**
- [ ] **1.3** read · applied the three questions to every section of `kb-answer-style` and wrote a
      verdict **and a reason** for each · said out loud which question can end the discussion alone
- [ ] **1.4** read · **made the move, re-priced, and got 473 / 231** · ran the preflight and saw the
      orphan finding once · reverted and deleted `references/worked-example.md`

## Section 2 — `02-descriptions-as-routing`

- [ ] **2.1** read · printed your own index as XML and underlined the deciding word for each of the six
      requests · **found a word in both descriptions and confirmed it decides nothing**
- [ ] **2.2** read · ran the audit · added two more negative requests and confirmed both score zero ·
      **added `reply` to `ticket-triage` and watched which of the three blocks noticed**
- [ ] **2.3** read · wrote `route.py` and `routing_gate.py` · **added `ticket` to `STOP` and counted how
      many margins moved at once** · decided whether it stays and wrote the reason
- [ ] **2.4** read · ran `crowd.py` and saw no score change and every margin drop · **deleted three
      decoys and measured what the last one does alone** · rewrote one decoy into a real job

## Section 3 — `03-four-containers`

- [ ] **3.1** read · wrote `containers.py` and got four containers holding six items · **routed the five
      items at the end of the part, saying the property out loud for each** · put the table in
      `skills/README.md` with Sutra's own files in the fourth column
- [ ] **3.2** read · wrote `boundary_cases.py` · **grepped both bodies for `never`, `must` and `always`
      and assigned a tier to every hit** · said what a callback version of one of them would check
- [ ] **3.3** read · ran `misfile_cost.py` · **re-ran with `CONVERSATIONS = 12` and `TRIAGES = 10` and
      said which finding flipped** · wrote the three unpriced rows for your own system with *who finds
      out and how*

## Section 4 — `04-the-three-axes`

- [ ] **4.1** read · ran all three instruments back to back and **wrote your three-line reading down** ·
      predicted the three lines for one change before making it and noted which you got wrong
- [ ] **4.2** read · wrote `overloaded.py` and `refactor.py` · **saw the same worst margin and the same
      tie count on both shelves** · shortened `DESCRIPTION` to the one-sentence merge and confirmed the
      coverage failure
- [ ] **4.3** read · wrote `suspects.py` and got four suspects on the specimen · **pointed `review()` at
      `skills/` and answered every suspect it raised in one line** · decided where those answers live

## Section 5 — `05-in-production`

- [ ] **5.1** read · ran `forty_skills.py` · **found the shelf size at which the worst margin first
      reaches zero and the size at which the shared-filler set first empties** · said out loud why
      search beats hierarchy on a rate-limited tier
- [ ] **5.2** read · partitioned the forty subjects into four shelves **by what a person would ask** ·
      ran `forty_skills.py` on one partition and found the skill whose margin got **worse** · decided
      whether `build_desk` gains a `shelf` parameter today and wrote the reason either way

## The build

- [ ] `route.py` has no side effects at import — running it prints nothing
- [ ] `overloaded.py` has no side effects at import either, and `refactor.py` and `suspects.py` both
      import from it
- [ ] `misfile_cost.py` prints `not in tokens` for the three unpriced rows and **does not invent a
      number for any of them**
- [ ] `suspects.py` has **no exit code** and every message it prints ends in a question mark
- [ ] `skills/README.md` carries the four-container table **and** the weight-flows-down rule
- [ ] The three-line reading — price, routing, placement — is written down for today's shelf
- [ ] `git status` is clean of `references/worked-example.md` and of every temporary description edit

## The eval

- [ ] `routing_gate.py` printed `worst margin: 1 (threshold 1)` and `exit: 0`
- [ ] **Break it, watch it go red, fix it:** append `Use when a reply is needed.` to `ticket-triage`'s
      description, re-run the gate, read `worst margin: 0 (threshold 1)` and `exit: 1`, then remove the
      sentence and confirm `exit: 0` again
- [ ] `crowd.py` printed `ties: 0` then `ties: 1`, and you can name the request that flipped
- [ ] `refactor.py` printed the **same** worst margin for both shelves, and you can say why that is the
      finding rather than a disappointment
- [ ] `suspects.py` printed `suspects: 4` on the specimen
- [ ] `forty_skills.py` printed an **empty** shared-filler set, and you can say why that is the audit
      failing rather than the shelf improving

## The budget

- [ ] Total generations spent: **0 of 20**
- [ ] `price_the_shelf.py` was the only script that touched the network, on `count_tokens`
- [ ] You did **not** fall back to a character estimate when a token count was unavailable

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**
- [ ] `docs/PAPERS.md` — **no new row**; `arXiv:2406.18665` is cited from 2.1 and taught on Day 9
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**; the decoys and the specimen exist only in code
- [ ] `./m depth 28` green · `./m trace` prints `57/199 closed, 0 problem(s)` · `./m check` green
- [ ] `git status` shows no `.env`; commit message is the one in §11
