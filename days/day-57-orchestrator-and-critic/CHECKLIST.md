# Day 57 — Definition of done

`./m done 57` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 56's parts and checklist are done, and you can state what replanning does when a plan's
      precondition stops holding.
- [ ] `python -c "from google.adk import Workflow; from google.adk.workflow import BaseNode; print(issubclass(Workflow, BaseNode))"`
      prints `True`. If it does not, the installed ADK is not 2.7.1 and §6 needs re-verifying (P8).
- [ ] `uv run python days/day-57-orchestrator-and-critic/lab/gate.py; echo "exit: $?"` is **red**
      (`0/5`, exit 1) before you write anything, and you have read all five findings.
- [ ] `lab/` scaffolded per §3 — twenty-two scripts plus the two-file paper demo — and
      `tests/test_critique.py` created empty.
- [ ] `git diff pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — when to split

- [ ] **1.1** read · ran `onehead.py` · saw **1 rule dropped at five duties and 3 at seven**, with the
      two newest among them · set `ATTENTION` to `7` and can say what that does to the case for a
      second agent
- [ ] **1.2** read · ran `onehead.py --split` · saw **0 dropped across the pair** for the same seven
      rules · added an eighth rule restating the seventh and watched it join the dropped list · can
      explain why adding words to an ignored rule usually makes it worse
- [ ] **1.3** read · applied the three questions to the four boundaries in Day 58's flow · wrote the
      table · can name, for each boundary you would keep, the rule the second head rescues

## Section 2 — the orchestrator

- [ ] **2.1** read · ran `owns.py` and `owns.py --works` · saw **33/50/36/35 against 61/190/199/331**
      · can say why the second column is a line and the first is flat
- [ ] **2.2** read · ran `router.py` and `router.py --route` · saw **5/5 stages against 1/5** · can
      state the one thing a router structurally cannot do, and the production symptom of an
      accidental transfer
- [ ] **2.3** read · ran `overlap.py` and `overlap.py --sharp` · saw **4/10 with 10/10 ties** become
      **9/10 with 1/10 ties** · renamed the two specialists and watched accuracy move to 6/10 with
      nothing else changed · added a third specialist and counted the new pairs
- [ ] **2.4** read · ran `owns.py` · counted the four orchestration calls as **40% of a ten-call
      ticket** · marked Day 58's transitions as branching or fixed and worked out the call count

## Section 3 — the critic

- [ ] **3.1** read · ran `selfgrade.py` and `selfgrade.py --all` · saw **5 of 5 drafts shipped on the
      writer's own verdict with 15 of 25 rubric lines failing** · asked the same writer about `short`
      by name and got the right answer · added a sixth rule outside `_INTENT` and can say what the
      self-check reports about it
- [ ] **3.2** read · ran `rubric.py` · saw **four thoughtful notes move zero rubric lines** and one
      named verdict move three, 2/5 → 5/5 · added a rule with no `test` and watched it always pass ·
      wrote a `why` line for a rule of your own
- [ ] **3.3** read · ran `evidence.py` and `evidence.py --shown` · saw the **same failing draft go
      from revise to accept** · can state the rule for what a critic may see and why the round count
      is withheld from it but known to the graph
- [ ] **3.4** read · ran `steer.py` and `steer.py --prose` · saw the parser read **'This is not
      something I would reject'** as a rejection and **'I would accept this once the jargon is gone'**
      as an unconditional accept · added two phrasings of your own and scored them

## Section 4 — stopping

- [ ] **4.1** read · ran `never.py` · saw the standard satisfied at **round 2** and the loop still
      running at **round 25, 50 model calls** · added an unsatisfiable rubric line and watched the
      loop oscillate, reintroducing `short` at round 3 · can say why the critic is not malfunctioning
- [ ] **4.2** read · ran `brake.py` · saw **50 calls against 6** for the same limit in two places ·
      moved the limit check above the accept branch and can say what information that loses
- [ ] **4.3** read · ran `escalate.py` and `escalate.py --two` · saw the two-verdict arm **send a
      draft it had already failed** · saw the unwired-route demonstration strand the ticket · raised
      `MAX_ROUNDS` to 10 and can say whether `ticket:5044` converges

## Section 5 — does it help

- [ ] **5.1** read · ran `improve.py` · saw **10/25 → 24/25 for 23 calls across five replies**, and
      the `ticket:5044` row costing **7 calls for 4/5** · ran `improve.py --sycophant` and saw **10
      calls, nothing gained** · saw the sycophant score **5/5 against the honest critic's 0/5** when
      scored by the critic's own verdict · set `MAX_ROUNDS` to 1 and wrote down the new totals
- [ ] **5.2** read · ran `price.py` · saw **250 unreviewed replies a day against 62 reviewed**, and
      **35** at the brake · looked up your own provider's current free-tier limits from the page in
      §8 and re-ran with `--rpm` and `--rpd` · can say why a request limit is a wall and a token
      budget is a slope

## Section 6 — the ADK box

- [ ] **6.1** read · ran `box.py` · saw the outer graph declare **`['intake', 'draft_review',
      'send']`** while the run emitted **7 events** · confirmed `issubclass(Workflow, BaseNode)`
      yourself · added a second copy of the box to the chain and can say what happened to the round
      counter
- [ ] **6.2** read · ran `steer.py` · saw the verdict branch the graph with **no orchestration node
      in it** · ran the unmatched-route demonstration and read the real warning: *"none were matched
      by the emitted route(s): escalate. The branch will end."* with **exit code zero** · changed a
      route to `"accepted"` and can say what monitoring would have to watch
- [ ] **6.3** read · ran `box.py --full` · saw **`reply@1/draft_review@1/critic@2`** and can say what
      the `@2` tells you · wrote the one-liner that counts model calls from the events and checked it
      against §5.2's "pair, measured" row

## Section 7 — the failure lab

- [ ] **7.1** read · ran `sycophant.py` · saw a draft failing **three rules** approved in **one
      round for two calls**, with every dashboard green · wrote a canary that fails exactly one rule
      and ran it against both critic modes
- [ ] **7.2** read · ran `rewrite.py` · saw the rewrite score **1/5 against the draft's 2/5** while
      reading better · ran the no-route demonstration and saw the warning report `route(s): None` ·
      can state the rule that replaces "the critic must not produce text"
- [ ] **7.3** read · ran `gaming.py` · saw **eleven words of filler score 5/5**, identically to a
      real 54-word reply and shorter · found a string of **four words** that scores 5/5 · added a
      rubric line that rejects it without rejecting the honest reply

## Section 8 — in production

- [ ] **8.1** read · ran `blame.py` · saw two different bugs produce **identical text, identical
      score, identical failing rules** and **4 calls against 2** · wrote the rule you would use to
      detect "the writer is ignoring the verdict" from event paths alone, and said what it does to a
      healthy one-round run
- [ ] **8.2** read · ran `heads.py` · saw **five agents buy 27 tickets a day** and **eight agents
      need 28 description pairs kept distinct** · listed Day 58's stages as agents and crossed out
      the ones whose owned rule you cannot name

## The paper — after the parts

- [ ] **`papers/01-self-refine.md`** read · ran `refine.py` (**3/3 in 2 generate calls**) and
      `refine.py --ablate` (**1/3 in 4 generate calls**) · can say why the ablation deliberately
      spends *more* calls · deleted the `REQUIRED` lookup from `feedback` and re-ran · can state what
      the paper claimed, the one property of a task the claim depends on, and why §3.1 does not
      contradict it

## Build brief

- [ ] `sutra/critique.py` written: `RUBRIC` as data with `key`, `why` and an executable `test`
- [ ] `review()` returns one of **three** verdicts plus the failing keys, and has **no field a draft
      could live in**
- [ ] The brake is evaluated by the loop, not by `review()`, and returns `escalate` when it fires
- [ ] `tests/test_critique.py` written, including the canary and the terminates-against-a-never-accepting-critic test
- [ ] Every rubric line has an executable `test`, and you have checked the shortest string that scores
      full marks

## Tests and gates

- [ ] `uv run python -m pytest tests/test_critique.py -q` passes
- [ ] **Break it, watch it go red, fix it:** move `MAX_ROUNDS` inside `review()` and confirm
      `gate.py` check three goes red, then put it back
- [ ] `uv run python days/day-57-orchestrator-and-critic/lab/gate.py; echo "exit: $?"` is **green**
      (`5/5`, exit 0)
- [ ] `./m depth 57` green — 24 parts + 1 paper
- [ ] `./m trace` shows day 57 closing exactly `AG-19, AG-20, ADK-40`

## Request budget

- [ ] Model calls made today: **0**. If you made any, write down which provider and why.

## Ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and commit hash
- [ ] `docs/PAPERS.md` row for `arXiv:2303.17651` present
- [ ] `git diff pyproject.toml uv.lock` still empty
- [ ] Committed as `day 57: multi-agent design — orchestrator, Writer↔Critic — closes AG-19, AG-20, ADK-40`
