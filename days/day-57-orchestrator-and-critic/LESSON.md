---
day: 57
phase: 8
phase_name: "Workflows and multi-agent"
title: "Multi-agent design — orchestrator, Writer↔Critic"
ids: ["AG-19", "AG-20", "ADK-40"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 24
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 57 — Multi-agent design: the orchestrator and the Writer↔Critic pair

> **Yesterday (Day 56):** planning patterns. A plan became a data structure with steps and a success
> condition, and replanning became the thing that happens when the world stops matching the plan.
> **Today:** the day that decides **how many agents Sutra actually gets**. Not "how do I build a
> multi-agent system" but "is there something wrong with these replies that a second head would fix,
> and is it worth four times the requests?" Both halves of that question get a number.
> **Tomorrow (Day 58):** the triage graph v1 — intake, classify, research, draft, review — end to
> end, with today's pair as one of its stages.

---

## §1 Where we are

Days 53 to 55 handed you the machinery: nodes and edges, the three shapes, and the difference between
a call that comes back and a hand-over that does not. Day 56 gave a plan somewhere to live. All of it
is mechanism, and none of it says how many agents you should have or where the seams go.

Here is the day as a scene.

A tailor at the end of a market street works alone, and works well. He cuts, pins, presses and hands
the trousers over in a paper bag with your name on the corner. Nobody has ever suggested he needs a
team, and if you asked him he would look at you strangely, because pinning and pressing are not two
jobs — they are one job held in one head, and the head that pinned it knows why the press goes where
it goes.

Then he agrees to take parcels for the courier. Then he holds keys for the flats upstairs. Then he
answers the phone about the parcels. None of these replaced anything, and the trousers you collected
last month had the fold pressed slightly off. He was surprised when you mentioned it, because he
remembers pressing them carefully. What he stopped doing was the *checking*, which was never a task
he could point at — it lived in the quiet gap between pinning and pressing, and the gap now has a
phone in it.

So he hires someone. The argument in the shop is about what she should do, and his first idea is that
she should sew too, so twice as much gets sewn. His second idea is the one that changes the shop: she
stands at the counter when a finished garment goes into the bag, and checks it against the docket the
customer signed. She did not cut it. She does not know what was hard about it. **That is exactly why
she catches things** — he sees the difficulty and how well he handled it, and she sees a garment and
a docket that says an inch and a half.

Today is that second hire, made deliberately and priced honestly. The desk currently writes a reply
*and decides the reply is good enough to send*, which is one head grading its own homework. We will
measure what that costs, build the pair that fixes it, measure what **that** costs, and then spend
three parts trying to break it — because the version of this pair that quietly stops working improves
every number on your dashboard while it does so.

---

## §2 The map

Twenty-four parts in eight sections, then one paper. The day climbs `foundation → working →
production`, and the last three sections are where it earns its keep.

### Section 1 — When to split *(the case for and against a second agent, argued with numbers)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [One agent is usually the right answer](parts/01-when-to-split/1.1-one-agent-is-usually-the-right-answer.md) | What does a second agent actually cost, and why is the burden of proof on the split? | foundation |
| 1.2 | [What a second duty costs the first](parts/01-when-to-split/1.2-what-a-second-duty-costs-the-first.md) | Why does adding a rule make an *existing* rule stop working? | working |
| 1.3 | [The three questions that decide a split](parts/01-when-to-split/1.3-the-three-questions-that-decide-a-split.md) | Judgement, evidence, consequences — which one justifies this boundary? | working |

### Section 2 — The orchestrator *(AG-19: the agent that decides what happens next, and nothing else)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [An orchestrator owns the flow, not the work](parts/02-the-orchestrator/2.1-an-orchestrator-owns-the-flow-not-the-work.md) | What happens to context when the router starts doing the job? | foundation |
| 2.2 | [Orchestrator or router](parts/02-the-orchestrator/2.2-orchestrator-or-router.md) | Why can a router not run a five-stage pipeline? | working |
| 2.3 | [Two descriptions that overlap are one bug](parts/02-the-orchestrator/2.3-two-descriptions-that-overlap-are-one-bug.md) | Why is routing accuracy sometimes a coin toss with a number on it? | working |
| 2.4 | [The orchestrator's own bill](parts/02-the-orchestrator/2.4-the-orchestrators-own-bill.md) | Why does adding one stage add two requests? | production |

### Section 3 — The critic *(AG-20: what makes a second reader worth its model call)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A check you never ran cannot fail](parts/03-the-critic/3.1-a-check-you-never-ran-cannot-fail.md) | Why does a writer approve its own failing draft without lying? | foundation |
| 3.2 | [A critic needs something it can fail against](parts/03-the-critic/3.2-a-critic-needs-something-it-can-fail-against.md) | Why does correct criticism change nothing without a named rule? | working |
| 3.3 | [What the critic is allowed to see](parts/03-the-critic/3.3-what-the-critic-is-allowed-to-see.md) | What does showing the critic the writer's reasoning do to its verdict? | working |
| 3.4 | [The verdict is a list, not a paragraph](parts/03-the-critic/3.4-the-verdict-is-a-list-not-a-paragraph.md) | Who reads a verdict, and what shape do they need it in? | working |

### Section 4 — Stopping *(a critic will always find something, so the loop needs a way out)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A critic will always find something](parts/04-stopping/4.1-a-critic-will-always-find-something.md) | Why does an open question produce a loop that cannot terminate? | working |
| 4.2 | [The brake belongs to the graph](parts/04-stopping/4.2-the-brake-belongs-to-the-graph.md) | Why is a limit in the critic's prompt not a limit? | production |
| 4.3 | [The third verdict](parts/04-stopping/4.3-the-third-verdict.md) | What must a two-verdict critic do when the brake fires? | production |

### Section 5 — Does it help? *(the honest before-and-after, and the price)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Did the critic actually help?](parts/05-does-it-help/5.1-did-the-critic-actually-help.md) | How do you measure a reviewer without letting it score itself? | production |
| 5.2 | [What the pair costs in requests](parts/05-does-it-help/5.2-what-the-pair-costs-in-requests.md) | 250 unreviewed replies a day, or 62 reviewed ones — which? | production |

### Section 6 — The ADK box *(ADK-40: the pair assembled in the 2.x graph runtime)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [A workflow is a node](parts/06-the-adk-box/6.1-a-workflow-is-a-node.md) | How does a three-node loop become one node in a bigger graph? | working |
| 6.2 | [The verdict steers the edges](parts/06-the-adk-box/6.2-the-verdict-steers-the-edges.md) | How does the critic branch the graph without an orchestration call? | working |
| 6.3 | [What escapes the box](parts/06-the-adk-box/6.3-what-escapes-the-box.md) | What does nesting hide, and what does it not? | production |

### Section 7 — The failure lab *(three ways the pair stops working, none of which raise)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The critic that approves everything](parts/07-failure-lab/7.1-the-critic-that-approves-everything.md) | Why does a broken reviewer improve every metric you have? | production |
| 7.2 | [The critic that rewrites](parts/07-failure-lab/7.2-the-critic-that-rewrites.md) | What happens when the reviewer becomes the writer? | production |
| 7.3 | [Five out of five, and worse](parts/07-failure-lab/7.3-five-out-of-five-and-worse.md) | What does a revision loop do to a proxy it is pointed at? | production |

### Section 8 — In production *(what changes when this runs for real)*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 8.1 | [Six calls, one answer, one bug](parts/08-in-production/8.1-six-calls-one-answer-one-bug.md) | Two different bugs, identical output — how do you tell them apart? | production |
| 8.2 | [How many heads is too many](parts/08-in-production/8.2-how-many-heads-is-too-many.md) | What grows linearly when you add an agent, and what grows as a square? | production |

### The paper — read **after** the parts

Principle 4 at the scale of a day: build the pair, watch a self-grader pass its own failing draft, and
*then* read the strongest published argument that one head is enough.

| # | Paper | Why it is here |
| --- | --- | --- |
| 01 | [Self-Refine: Iterative Refinement with Self-Feedback](papers/01-self-refine.md) — `arXiv:2303.17651` | It says one model, asked three times, improves its own output by ~20 points absolute. That contradicts §3.1 until you see which failure each of them fixes. |

---

## §3 Setup — run this

```bash
mkdir -p days/day-57-orchestrator-and-critic/lab/papers/self-refine
cd days/day-57-orchestrator-and-critic/lab

touch _desk.py _flow.py
touch onehead.py owns.py router.py overlap.py
touch selfgrade.py rubric.py evidence.py steer.py
touch never.py brake.py escalate.py
touch improve.py price.py
touch box.py
touch sycophant.py rewrite.py gaming.py
touch blame.py heads.py gate.py
touch papers/self-refine/model.py papers/self-refine/refine.py

touch ../../../tests/test_critique.py
```

**No package is added today.** `google-adk==2.7.1` is already pinned from Day 5 and is the only
dependency any of this uses. Confirm nothing moved:

```bash
git diff pyproject.toml uv.lock    # must be empty, and stay empty
```

---

## §4 Build brief

The learner writes `sutra/critique.py`. The lab scripts are teaching material and are given complete;
this is the rep.

1. **`sutra/critique.py` — the standard as data.** A `RUBRIC` of named checks, each with a `key`, a
   `why` and an executable `test`. `TODO(me)`: decide which of Sutra's rules can be deterministic
   functions and which genuinely need a model. §3.2 argues three of five need no model at all.
2. **`review(draft, ticket) -> Verdict`.** Returns a verdict from a **closed set of three** —
   `accept`, `revise`, `escalate` — plus the failing rule keys. `TODO(me)`: it must not have a field a
   replacement draft could live in (§7.2), and it must not receive the writer's reasoning (§3.3).
3. **The brake, outside the reviewer.** A `MAX_ROUNDS` the loop evaluates, never the critic (§4.2).
   `TODO(me)`: when it fires, return `escalate`, not `accept`, and make sure something is wired to
   receive it (§4.3, §6.2).
4. **`tests/test_critique.py`.** `TODO(me)`: at least a canary — a known-bad draft the reviewer must
   reject (§7.1) — and a test that the loop terminates against a critic that never accepts (§4.2).

Do not wire this into a graph today. Day 58 does that.

---

## §5 The eval that must be able to fail

```bash
cd days/day-57-orchestrator-and-critic/lab
uv run python gate.py; echo "exit: $?"
```

Red before the build brief is done, and it checks the four things this day argued for rather than
merely that a file exists:

```text
  FAIL  sutra/critique.py exists  - not written yet (build brief step 1)
  FAIL  the standard is data, not if-statements  - sutra/critique.py missing
  FAIL  the brake lives outside the critic  - sutra/critique.py missing
  FAIL  there is a third verdict  - sutra/critique.py missing
  FAIL  tests/test_critique.py exists  - not written yet (build brief step 3)

0/5 checks pass
exit: 1
```

**Break it on purpose once it is green:** move `MAX_ROUNDS` inside `review()` and watch check three
go red.

---

## §6 Request budget

**Zero.** No provider is called anywhere on this day — not by a lab script, not by the paper demo.

| Provider | RPM used | RPD used |
| --- | --- | --- |
| Gemini (AI Studio, free) | 0 | 0 |
| Groq | 0 | 0 |
| OpenRouter (`:free`) | 0 | 0 |
| Ollama (local) | 0 | 0 |

Every writer, critic and orchestrator in the lab is a deterministic Python function, which is what
lets §5.1's 24-out-of-25 and §5.2's 62-replies-a-day be numbers from a run rather than estimates. The
free-tier figures in `price.py` and `heads.py` are **placeholders the learner replaces** with their
provider's real limits — see §8.

---

## §7 Traps

1. **Trap #1 (1.x → 2.x, the node model).** Multi-agent design in 1.x meant a `sub_agents` tree with
   an orchestrating parent. In 2.x the graph is the composition layer, an agent is one node type, and
   — the part that matters today — **a `Workflow` is itself a `BaseNode`**, so the pair nests as one
   node (§6.1). Do not reach for an agent tree to express a loop.
2. **The limit in the prompt.** Asking the critic to stop after three rounds is asking the component
   that will not stop to stop itself: 50 model calls against 6 (§4.2).
3. **Two verdicts.** `accept` and `revise` alone force the brake to ship a failing draft, and to log
   it as a success (§4.3).
4. **The route with no edge.** Adding `escalate` to the enum is the easy half. Without an edge, 2.7.1
   logs a warning, ends the branch, and **exits zero** — the ticket is gone and nothing you alert on
   fires (§6.2).
5. **Scoring the critic by its own approval rate.** On that metric a critic that approves everything
   scores 5 out of 5 and the working one scores 0 (§5.1).
6. **A rubric line with no executable test.** It always passes, or always fails, depending on which
   way the default falls — and both are silent (§3.2, §4.1).
7. **State keys inside a nested box are not namespaced.** Two review boxes both writing `rounds`
   collide with no error (§6.3).

---

## §8 Verify before you code

Fetched on **2026-09-05**, and every symbol also introspected against installed `google-adk==2.7.1`:

- `https://adk.dev/graphs/` — the node model; `Workflow`, `Edge`, `START`, `FunctionNode`.
- `https://adk.dev/graphs/routes/` — routes on edges and events; the statement that **a graph cycle
  is not bounded automatically**, which is §4.2's whole argument.
- `https://arxiv.org/abs/2303.17651` — the Self-Refine record. Title copied from it; row added to
  `docs/PAPERS.md`.

Checked by running, not by reading — these are in the parts with their output:

```bash
python -c "from google.adk import Workflow; from google.adk.workflow import BaseNode; print(issubclass(Workflow, BaseNode))"
python -c "from google.adk.workflow import BaseNode; print(list(BaseNode.model_fields))"
```

**A discrepancy worth recording.** Plan §5 names `google-adk` **2.6.3** as the baseline; the repo pins
**2.7.1** (`docs/PACKAGES.md`). A patch ahead is what Principle 7 expects rather than an amendment
case, but the day is written against 2.7.1 and says so wherever a symbol is used.

**Before you run `price.py` or `heads.py` for real**, look up your own free-tier limits — Addendum 02
forbids inventing them and the rosters move:

- Gemini free tier: `https://ai.google.dev/gemini-api/docs/rate-limits` (Day 52 recorded that the
  per-model RPM/RPD have moved behind an AI Studio session — if you cannot read them, treat the
  numbers as configuration you supply).
- Groq: `https://console.groq.com/settings/limits`
- OpenRouter: `https://openrouter.ai/models` filtered to `:free`

---

## §9 Say it in an interview

> "The thing I got wrong first was thinking multi-agent was an architecture decision. It is a quota
> decision. On my support desk the pair took the reply standard from 10 rubric lines out of 25 to 24
> out of 25 — that is real, and I measured it by running the same tickets with and without the
> reviewer and scoring both with the rubric rather than with the reviewer. But it cost four requests
> per reply against one, and seven when the round cap was hit, which took a day's free-tier allowance
> from 250 replies to 62. So the honest framing is that I bought a quality improvement with three
> quarters of my throughput, and whether that is right depends entirely on how many tickets come in.
> The part I would want to be asked about is how I know the reviewer still works. It is not the
> approval rate — a critic that approves everything scores 100% on that, runs one round instead of
> two, has zero escalations and costs half as much, so every dashboard I had got *better* when I
> broke it deliberately. What catches it is a canary: a known-bad draft that the reviewer must
> reject, in CI. And I keep the without-reviewer arm running on a schedule, because the day the
> reviewer is the only path is the day I lose the ability to answer the question at all."

---

## §10 Done when

`CHECKLIST.md` is fully ticked, `./m depth 57` is green, and `lab/gate.py` has gone from red to green
because you wrote `sutra/critique.py` — not because you edited the gate.

The understanding test is §5.1 and §7.1 together: you can state what the pair bought, what it cost,
and how you would find out if it silently stopped working.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append verbatim, filling the date and hash after committing:

```text
| 57 | <date> | AG-19, AG-20, ADK-40 | 24 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PAPERS.md`** — already appended when the day was written:

```text
| Self-Refine: Iterative Refinement with Self-Feedback | arXiv:2303.17651 | 2023 | 2026-09-05 | 57 | `days/day-57-orchestrator-and-critic/papers/01-self-refine.md` |
```

**`docs/PACKAGES.md`** — no rows. No package was added today.

**`SKILL_PROVENANCE.md`** — no rows. No third-party skill was sourced today.

**The commit:**

```text
day 57: multi-agent design — orchestrator, Writer↔Critic — closes AG-19, AG-20, ADK-40
```
