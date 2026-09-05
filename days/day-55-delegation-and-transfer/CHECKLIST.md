# Day 55 — Definition of done

`./m done 55` refuses to commit until every box is ticked. Tick a box only when you have actually
run the thing, not when you have read it.

## Before you start

- [ ] Day 54's parts and checklist are done, and you can say in one sentence what a graph edge is.
- [ ] `python -c "from google.adk.tools import AgentTool, TransferToAgentTool, transfer_to_agent; print('ok')"`
      prints `ok`. If it does not, stop and check the installed version before writing anything (P8).
- [ ] `uv run python days/day-55-delegation-and-transfer/lab/gate.py; echo "exit: $?"` is **red**
      before you write anything, and you have read the finding it reports.
- [ ] `lab/` scaffolded per §3 — fifteen scripts plus `papers/contract-net/` — and
      `sutra/delegation.py` **not** created yet.
- [ ] `git diff --stat pyproject.toml uv.lock` is empty and stays empty. No package is added today.

## Section 1 — why split the desk

- [ ] **1.1** read · ran `select.py` and `select.py --split` · saw **4/8 contended fall to 3/8**,
      and saw `what does ticket 4521 say` go from **`close_ticket`** to `lookup_ticket` · added a
      thirteenth tool and can say what it did to `this is urgent, raise the priority` · can name the
      one ambiguity splitting does **not** fix
- [ ] **1.2** read · counted the conditional words in `sutra/desk/agent.py`'s `INSTRUCTION` and wrote
      the number down · wrote a four-job `# Honesty` section on paper and counted again · can explain
      why dilution produces a **flaky** test rather than a failing one
- [ ] **1.3** read · re-derived all six rows of the edge/call/hand-over table from the three
      questions alone · ran one step from your own work through the procedure · can state the single
      question that separates a call from a hand-over

## Section 2 — call or hand-over

- [ ] **2.1** read · ran `staff.py` and `staff.py --single-turn` · saw `kb_specialist` move from
      **transfer targets** to **`[('_SingleTurnAgentTool', 'kb_specialist')]`** · predicted, then
      checked, what happens when `archive_specialist` is also `single_turn` · know that the default
      mode is `chat`
- [ ] **2.2** read · ran `lost.py` and `lost.py --single-turn` · saw **3/5 turns answered by the
      wrong desk** fall to **0/5** · added a sixth billing turn and can say what each version costs ·
      can name the three ways control comes back and which the framework guarantees
- [ ] **2.3** read · listed which rules in `sutra/desk/agent.py`'s `# Honesty` are claims about the
      whole system and which are about that one agent · can name the four things that swap on a
      hand-off · can give the duplicate-honesty / keep-scope-local rule

## Section 3 — the description routes

- [ ] **3.1** read · ran `staff.py` and read the **exact injected block** · deleted a `description=`
      and re-ran to see `Agent description:` empty · can say who reads `description` and who reads
      `instruction`
- [ ] **3.2** read · ran `describe.py` and `describe.py --fixed` · saw **intrusion 4/5 → 0/5**, the
      **1-point** win become 4–0, and the alphabetical tie disappear · added an "anything urgent"
      colleague and re-ran · can say why "routed to the wrong colleague" is the wrong headline metric
- [ ] **3.3** read · wrote, for every exclusion in `_desk.py`'s two specialists, the exact request it
      turns away · deleted any you could not write one for · can name the four parts of a routing
      description in order and say which does the work

## Section 4 — transfer in 2.x

- [ ] **4.1** read · ran `handover.py` · saw `transfer_to_agent` return **`None`** and set
      `actions.transfer_to_agent` · passed `"a_name_nobody_has"` and saw it accepted · can name the
      one place a transfer can still be stopped
- [ ] **4.2** read · saw the declaration carry
      **`'enum': ['kb_specialist', 'archive_specialist']`** · added a third sub-agent and saw the
      enum grow with no list edited by hand · can name the three places the valid names appear and
      which one is enforced
- [ ] **4.3** read · ran `reach.py` · saw the **default** give each specialist its parent *and its
      peer* · saw `disallow_transfer_to_parent=True` leave **only the peer edges** · added a third
      specialist and counted the two-agent cycles · can say which switch is the dangerous one
- [ ] **4.4** read · ran `astool.py` and read section 3 · drew Day 58's five stations and counted the
      routing decisions · can state trap #1 in one sentence and say what `mode="task"` cannot be used
      inside

## Section 5 — agent-as-tool

- [ ] **5.1** read · saw the wrapper named **after the agent** · made two sub-agents share a name and
      saw what `lead.tools` looked like · can say which list a `single_turn` sub-agent leaves
- [ ] **5.2** read · ran `astool.py` · saw the default **`{'request': {'type': 'string'}}`** become
      named fields with `required: ['symptom', 'product_area']` · added an optional third field and
      can say why it is not in `required` · can give the rule for what belongs in `required`
- [ ] **5.3** read · saw `_SingleTurnAgentTool` use **`run_node`** and `AgentTool` build its own
      **`InMemorySessionService`** · found the `state_delta` forwarding loop in the installed source ·
      can say what does and does not cross that boundary
- [ ] **5.4** read · ran `swallow.py` and `swallow.py --checked` · saw **all three results with
      `type=str`**, including the 429 · decided what `looks_like_failure` should do with an empty
      string · can name the two places the real fix belongs

## Section 6 — the price of a hand-off

- [ ] **6.1** read · ran `price.py` and `price.py --tickets 20` · saw **1 / 2 / 3 requests** per
      ticket and **20 / 40 / 60** over twenty · added a five-request nested shape and wrote down the
      windows figure · can name the request people forget
- [ ] **6.2** read · ran `depth.py` and `depth.py --verbatim` · saw **100 / 55 / 20 / 10 per cent**
      become 100 at every hop · rewrote the depth-2 summary yourself in twelve words and measured it ·
      can name the class of detail lost first

## Section 7 — the failure lab

- [ ] **7.1** read · ran `pingpong.py` and saw **12 requests, 6 each, nothing answered** · ran
      `--no-peers` and saw **1 request, answered** · rewrote `AUTH_DESCRIPTION` so it no longer defers
      and wrote down the hop count · can say what ADK's default transfer-depth limit is
- [ ] **7.2** read · ran `stalled.py` and saw **3/5 stations, 0 errors raised** · ran `--call` and saw
      **5/5 for 6 requests instead of 4** · moved the consultation to `draft` and can say whether the
      reply is more or less dangerous · can name the one field that distinguishes a completed run

## Section 8 — in production

- [ ] **8.1** read · ran `depth.py` both ways and can point at the hop where the trade turns bad
      (**2 → 3: one request, thirty-five points**) · added a fifth link and decided what you would
      tell a colleague who proposed it
- [ ] **8.2** read · ran `audit.py` and `audit.py --thin` · saw the **`"chosen": null`** record and
      the **margin 0** count · added a fifth request you expected to tie and checked · wrote the one
      sentence that would break that tie

## The paper — after the parts

- [ ] **`papers/01-contract-net-protocol.md`** read · ran `demo.py` (**exit 0, awarded to
      `archive_node`**) and `demo.py --no-bids` (**exit 1, `FAILED - node has no index`**) · set
      `kb_node`'s `has_index` to `True` and ran both again, and wrote down what that says about when
      each design pays · found the two message types FIPA added
      (<https://www.fipa.org/specs/fipa00029/>) · can answer *what did this paper claim, and what do
      we do differently now?*

## Build brief

- [ ] `sutra/delegation.py` created, and the model pinned to a **named constant** holding a free-tier
      string you looked up today (ADK-73, Addendum 02)
- [ ] `kb_specialist` and `archive_specialist` written, `mode="single_turn"`, with **reciprocal**
      exclusions — neither claims the other's territory
- [ ] `billing_agent` written as a `chat` transfer target with `disallow_transfer_to_peers=True`
- [ ] `triage_lead` written with all three as `sub_agents`, and its own description excluding what the
      specialists claim
- [ ] `HOP_LIMIT` and a `before_tool_callback` that refuses `transfer_to_agent` past it, counting in
      `temp:` state
- [ ] The caller checks its tool results for the failure shape — a sub-agent failure is a **string**

## Tests and the gate

- [ ] `uv run python days/day-55-delegation-and-transfer/lab/gate.py; echo "exit: $?"` is **green**
- [ ] **Break it, watch it go red, fix it:** delete `disallow_transfer_to_peers` from
      `sutra/delegation.py`, re-run `gate.py`, see it go **red** on
      *"peers are still reachable - the ping-pong is open"*, then put it back and see it go green
- [ ] `uv run python -m pytest -q -m "not live"` passes
- [ ] `uv run ruff check .` and `uv run ruff format --check .` are clean
- [ ] `./m depth 55` passes
- [ ] `./m trace` shows ADK-38, ADK-39 and AG-16 closed, and no more

## Budget

- [ ] The day's lab spent **zero** model calls, and you can say why that was possible
- [ ] If you ran the build brief's demos live: **2 requests** for the transfer demo, **3** for the
      tool demo, run once each, with 429 handled by `retry-after` + backoff

## Ledger and commit

- [ ] `docs/PROGRESS.md` row appended, verbatim from §11
- [ ] `docs/PAPERS.md` carries the Contract Net row (appended 2026-09-05)
- [ ] No `docs/PACKAGES.md` row — confirm `git diff pyproject.toml uv.lock` is still empty
- [ ] Committed as `day 55: delegation, transfer and agent-as-tool - closes ADK-38, ADK-39, AG-16`
