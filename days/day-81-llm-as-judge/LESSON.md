---
day: 81
phase: 12
phase_name: "Evals"
title: "LLM-as-judge and honest baselines"
ids: ["AG-27", "ADK-61"]
principles: [1, 2, 7, 8, 10, 11, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 81 — LLM-as-judge and honest baselines

> **Yesterday (Day 80):** rubrics arrived, and with them the seam that lets a judged metric run at zero
> cost — the judge resolves through `LLMRegistry`, so a scripted one can be registered there. Two
> findings: reword four rubric lines and a conversation that refunded 2,400 without approval scores
> 1.00, and on `google-adk==2.7.1` the judge is shown four tool calls as zero.
> **Today:** the judge itself is the subject. `final_response_match_v2` for real, its three named
> biases measured on Sutra's own answers, and the question that decides whether any of it means
> anything — what does a procedure that does nothing score on the same data? On this fixture: **83.3%**,
> which is exactly what a judge that never read an answer achieved.
> **Tomorrow (Day 82):** regression discipline. Evals in CI, full runs on the Day 73 nightly, and the
> comparison that needs every number this day insisted on recording.

---

## §1 Where we are

The school sports day where one teacher judges every event.

He is good at it. He has done it for years, he is fair, and nobody has ever seriously complained. The
hundred metres is easy — there is a finish line — but the long jump needs somebody to call the board,
the shot put needs a mark, and the fancy-dress needs an opinion, and he supplies all of them.

Two things are true at once. Without him there is no sports day, because nobody else is going to stand
in the sun for four hours making three hundred judgements. And nobody has ever checked his judgements
against anybody else's, so the school has no idea whether *first place in fancy dress* means what it
appears to mean or means *the one that caught his eye*.

The problem is not the teacher. It is that a measurement everybody relies on has never been measured.

Day 79 gave Sutra two metrics that cost nothing and found the wall: ROUGE scored a true sentence at
0.353 and its negation at 0.941. Day 80 brought a reader in and kept it scripted, so that everything
around the reader could be tested for free. Today the reader is the thing under test.

`final_response_match_v2` runs for real — its prompt template, its label parser, its majority vote, its
threshold — against twenty-four answers a person labelled first. The three biases the paper behind this
day named are measured on Sutra's own desk: position, where twelve confident verdicts become zero once
each pair is shown both ways round; verbosity, where one polite sentence turns four wrong answers into
passes; and self-enhancement, where two answers that both say *eleven days* are graded oppositely
because one is phrased the way the judge phrases things.

And then the finding that gives the day its second half. A judge that answers the same question five
times and splits three-two on **every** case — a rater that never read anything — agrees with the human
labels on **20 of 24**. Because twenty of the twenty-four are valid, and the majority vote always lands
on valid, and 83.3% is the base rate. Remove one column from the report and it reads: *"both judges
agree with us most of the time; ship it."*

---

## §2 The map

Five sections. Section 1 is the judged metric, run for real, and what it depends on. Section 2 is the
three named biases, one measurement each. Section 3 is the correction — what a number has to be better
than. Section 4 is the bill and the question of when to use a judge at all. Section 5 is calibration
and the list.

### 1 — The judge is a system

*A metric whose output comes from a model you did not write.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A judge is a model with a job description](parts/01-the-judge-is-a-system/1.1-a-judge-is-a-model-with-a-job.md) | `final_response_match_v2` run for real, and the label vocabulary that hides a policy | `working` |
| 1.2 | [The judge disagreed with itself](parts/01-the-judge-is-a-system/1.2-the-judge-disagreed-with-itself.md) | 💥 A 3–2 coin agrees with the human on 20 of 24 | `production` |
| 1.3 | [What the judge is shown](parts/01-the-judge-is-a-system/1.3-what-the-judge-is-shown.md) | 5,029 characters, of which the case is three lines | `working` |

### 2 — The judge has biases

*Three named failure modes, measured on Sutra's own answers.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Position](parts/02-the-judge-has-biases/2.1-position.md) | 12 of 12 verdicts become 0 once each pair is shown both ways | `production` |
| 2.2 | [Verbosity](parts/02-the-judge-has-biases/2.2-verbosity.md) | 💥 One polite sentence turns 0 of 4 into 4 of 4 | `production` |
| 2.3 | [Self-enhancement](parts/02-the-judge-has-biases/2.3-self-enhancement.md) | 💥 Same fact, two house styles, opposite verdicts | `production` |

### 3 — Honest baselines

*What a number has to be better than before it is a number.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A number needs something to be better than](parts/03-honest-baselines/3.1-a-number-needs-a-baseline.md) | Why accuracy is most misleading where the stakes are highest | `foundation` |
| 3.2 | [Three baselines you can always build](parts/03-honest-baselines/3.2-three-baselines-you-can-always-build.md) | Majority class, a coin, and the previous version — and which one is hard | `working` |
| 3.3 | [The 83.3% that was free](parts/03-honest-baselines/3.3-the-eighty-seven-that-was-eighty-three.md) | 💥 Remove one column and the report says "ship it" | `production` |

### 4 — What it buys

*The bill, and when not to pay it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Priced against the allowance](parts/04-what-it-buys/4.1-priced-against-the-allowance.md) | 240 requests for 24 cases, and the factor of twenty that buys meaning | `working` |
| 4.2 | [When a judge is the wrong tool](parts/04-what-it-buys/4.2-when-a-judge-is-the-wrong-tool.md) | Five instruments, one claim, and the question that picks | `production` |

### 5 — In production

*Calibration, and what is still missing.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Calibrating a judge against people](parts/05-in-production/5.1-calibrating-a-judge.md) | The set that makes every other number mean something, parked three times | `production` |
| 5.2 | [What a real judged suite adds](parts/05-in-production/5.2-what-a-real-judged-suite-adds.md) | Nine items, three of which cost nothing and one of which saves money | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [Judging the judge — agreement, and the three biases](papers/01-judging-the-judge.md) | `arXiv:2306.05685` — over 80% agreement with humans, *the same level humans reach with each other*, and the three biases that come with it. The demo reports 100% of committed pairs and 68.8% of all pairs; the ablation reports 87.5% and hides that five of sixteen were the ordering |

---

## §3 Setup — run this

```bash
mkdir -p days/day-81-llm-as-judge/lab/papers/mtbench
cd days/day-81-llm-as-judge/lab
touch _cases.py _judge.py judge.py bias.py baseline.py cost.py gate.py
touch papers/mtbench/arena.py papers/mtbench/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
everything this day uses is already in `google-adk==2.7.1`.

**What each file is for:**

- `_cases.py` is the file to read first: twenty-four answers the desk gave, each with the question, a
  reference answer, and **a verdict a person wrote down before any judge existed**. That last field is
  what every number in this day is measured against.
- `_judge.py` is the scripted rater, registered through `LLMRegistry` under `scripted-judge.*` — the
  same seam Day 80 part 2.1 established. It scripts *behaviours* rather than answers, because section 2
  is about behaviours.
- `judge.py` runs ADK's real `final_response_match_v2` and has the `--wobble` arm.
- `bias.py` holds section 2: `--verbosity`, `--self` and `--position`, with `--position-controlled` as
  the fix.
- `baseline.py` is section 3, with `--raw` as the ablation.
- `cost.py` is section 4's arithmetic; `gate.py` is the day's eval against `sutra/judge.py`.
- `papers/mtbench/` holds the paper's demo: `arena.py` is the pairwise comparison and the swap control,
  and nothing else.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-81-llm-as-judge/lab/_cases.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today's fixture is invented ticket text; a real
  calibration set holds real customer answers and the labels somebody wrote about them, which is Day
  69's subject and part 5.2 item 9's reason for parking the rationales.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that belongs
in the product. Day 79 promoted the eval suite, Day 80 the rubric; today promotes the judge and the
baselines.

**`sutra/judge.py`** — the desk's judged metric, and the numbers that make it readable.

- `TODO(me)`: `judge_criterion(model, samples)` building an `LlmAsAJudgeCriterion` with the judge model
  **pinned explicitly**. The default on 2.7.1 is `gemini-2.5-flash`, which is the desk's own lane —
  part 1.1, and the ADK-73 trap applied to a model call that does not look like one.
- `TODO(me)`: `labels(results)` returning the judge's verdict per case rather than one number. Part 1.2
  measured why: two judges with the same aggregate can be a reader and a coin.
- `TODO(me)`: `baselines(human)` returning the majority-class and alternating baselines, computed from
  the labels rather than hard-coded. Part 3.2 is the argument for computing rather than configuring.
- `TODO(me)`: `report(human, judge)` printing agreement, kappa **and** the margin over baseline, in one
  row. Part 3.3 measured what happens when the third column is dropped, and it exits 0.
- `TODO(me)`: `compare(a, b)` asking both ways round and returning `None` when the orderings disagree.
  Part 2.1 and the paper. Report both agreement figures — over committed pairs and over all pairs.
- `TODO(me)`: `refuse()` — decide what the suite does when no candidate beats its baseline by a margin
  worth having. Part 3.3's check-yourself shows the current script printing nothing in that case, which
  is a real gap you get to close.
- `TODO(me)`: the three no-cost columns from part 5.2 — judge model, whether the vote was unanimous,
  and the answer's length — on every results row.

**`tests/test_judge.py`**

- `TODO(me)`: a test that a constant-label "judge" scores no better than the majority-class baseline.
  That is part 1.2's coin as a test, and it is the one that would have caught it on day one.
- `TODO(me)`: a test that padding an answer does not change its verdict. Part 2.2 measured 0 of 4
  becoming 4 of 4; run it whenever the judge model changes, which is the moment the bias can move.
- `TODO(me)`: a test that `compare()` returns `None` when a judge prefers whichever answer comes first.
- `TODO(me)`: a test that `report()` refuses to print an accuracy with no baseline beside it.

**Two `TODO(me)`s that are not code:**

- **The calibration set.** Fifty answers, roughly half of them wrong, labelled by two people
  independently, with the human-human agreement recorded as the ceiling. Part 5.1. Parked on days 79,
  80 and 81; it is the item every number in this day rests on.
- **The allowance measurement**, now open for a fourth day: `gemini-2.5-flash-lite`'s daily allowance,
  measured with one controlled burn and given a dated `docs/PACKAGES.md` row. Part 4.1 prices this
  suite at 240 requests against a measured 20, and four separate lists are blocked on the same number.

---

## §5 The eval that must be able to fail

```bash
cd days/day-81-llm-as-judge/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/judge.py`, all red today because the module is the build brief. A check that
cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes red:

```bash
uv run python judge.py; echo "exit: $?"                    # 0 — 24 of 24, the control
uv run python judge.py --wobble; echo "exit: $?"           # 1 — 20 of 24, from a coin
uv run python bias.py --verbosity; echo "exit: $?"         # 1 — 0 of 4 becomes 4 of 4
uv run python bias.py --self; echo "exit: $?"              # 1 — same fact, opposite verdicts
uv run python bias.py --position; echo "exit: $?"          # 1 — 12 of 12 decided by ordering
uv run python bias.py --position-controlled; echo "exit: $?"  # 0 — 0 of 12 survive the swap
uv run python baseline.py; echo "exit: $?"                 # 1 — the coin judge is at +0.0%
uv run python baseline.py --raw; echo "exit: $?"           # 0 — "ship it"
```

Two of those belong in CI, and part 5.2 says which: **`baseline.py`**, because a judged score reported
without its baseline can be green for a reason that has nothing to do with the desk, and
**`bias.py --position`** wherever a pairwise comparison is used.

Note the pair at the end. The **honest** arm exits 1 and the **ablation** exits 0 — the report that
hides the finding is the one that passes. That inversion is the day's shape in two commands.

The paper's demo does the same for its own claim: `demo.py` exits `0` reporting 100% of committed pairs
and 68.8% of all pairs, and `demo.py --off` exits `1` reporting a clean 87.5% over sixteen verdicts of
which five were the ordering.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-06 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

`FinalResponseMatchV2Evaluator` is real and really ran: its prompt template, `_parse_critique`, the
majority-vote aggregation and the threshold are all ADK's own code, unmodified. What is scripted is the
rater's answer, because `LlmAsJudge._setup_auto_rater` resolves the judge through `LLMRegistry` — Day
80 part 2.1's seam.

That leaves the honest gap, and part 5.2 names it as the boundary of the whole day: **this day
measures the machinery around a judge and models the judge's behaviour.** Each bias in section 2 is a
scripted caricature of an effect the paper reports, isolated so it is legible. Whether a real judge
does any of these, and by how much, is not measured here — and part 5.1's calibration set is the only
thing that would answer it. It has now been parked three times.

The real cost, computed rather than spent: part 4.1 prices this suite at **240 requests** for
twenty-four cases and **1,800** for the sixty-case version with a pairwise arena, against the 20 per
day Day 78 measured for `gemini-3.7-flash` off a live 429. The Flash-Lite lane remains unmeasured —
Day 78's criterion 3, open for a fourth day.

---

## §7 Traps

1. **Reporting agreement without the base rate.** 83.3% on a suite that is 83.3% one class is what a
   constant achieves — part 3.1, and part 1.2 measured a judge doing exactly that.
2. **Not pinning the judge model.** `JudgeModelOptions.judge_model` defaults to `gemini-2.5-flash` on
   2.7.1, which is the desk's own lane. ADK-73's trap, applied to a model call that does not look like
   one — part 1.1.
3. **Cutting `num_samples` to save money.** It turns a majority into a single draw, and every
   borderline case becomes a coin that Day 82's nightly will report as a regression — parts 1.2 and 4.1.
4. **A pairwise comparison with no swap.** 12 of 12 verdicts, every one of them the ordering, and
   nothing in the output says so — part 2.1.
5. **Optimising against a judged score.** Verbosity is the one bias the *agent* can exploit, and any
   tuning loop will find it — part 2.2, where one polite sentence turned four wrong answers into passes.
6. **Judging your own family.** The default configuration, the only bias with no cheap control, and the
   one Sutra is most exposed to — part 2.3.
7. **Using a judge for a claim with one right answer.** A substring test is free, exact and unbiasable;
   judging it costs ten requests and adds a rater's biases to a question that had none — part 4.2.
8. **Comparing against random on skewed data.** The coin judge is +33.3 points against alternating and
   +0.0 against the majority class. The baseline has to be the strongest trivial procedure — part 3.2.
9. **Reading a `NOT_EVALUATED` case as a pass.** `Label.NOT_FOUND` gives a case with no score, and
   `partially valid` maps to `INVALID` — a hedge is recorded as a no, by somebody else's default —
   part 1.1.
10. **`UnicodeEncodeError` when printing the prompt.** The v2 template contains a `→` and Windows'
    default console codepage cannot encode it. `PYTHONIOENCODING=utf-8` — part 1.3.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| ADK evaluation criteria | <https://adk.dev/evaluate/criteria/> | `final_response_match_v2` *"uses a Large Language Model (LLM) as a judge to determine if the agent's final response is semantically equivalent to the provided reference response"*, sampling the judge multiple times per invocation with majority voting |
| ADK evaluation guide | <https://adk.dev/evaluate/> | lists `final_response_match_v2` among the criteria and directs judge configuration to the criteria page |
| Paper record | <https://arxiv.org/abs/2306.05685> | *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, first submitted 9 June 2023; *"over 80% agreement, the same level of agreement between humans"*; biases named as *"position, verbosity, and self-enhancement ... as well as limited reasoning ability"* |
| Gemini free-tier limits | <https://ai.google.dev/gemini-api/docs/rate-limits> | no free-tier RPM/RPD table published; limits *"can be viewed in Google AI Studio"* |

**ADK symbols verified against the installed `google-adk==2.7.1`**, not only against the docs:
`LlmAsAJudgeCriterion.model_fields` = `threshold, include_intermediate_responses_in_final,
judge_model_options`; `FinalResponseMatchV2Evaluator.__init__(eval_metric)` taking only the metric;
`Label` with `TRUE, INVALID, VALID, PARTIALLY_VALID, ALMOST, FALSE, NOT_FOUND` and `_parse_critique`
mapping `partially valid`/`almost`/`false` to `INVALID`; `aggregate_per_invocation_samples`' majority
vote and its documented tie rule; `_FINAL_RESPONSE_MATCH_V2_PROMPT`'s framing and its three
interpolated values; `JudgeModelOptions.judge_model` defaulting to `gemini-2.5-flash` with
`num_samples=5`; and `LlmAsJudge._setup_auto_rater` resolving through `LLMRegistry`.

**Both `LlmAsJudge` and `FinalResponseMatchV2Evaluator` carry ADK's `@experimental` decorator on
2.7.1** and warn on import. Pin the version and expect this surface to move; Principle 14 applies.

**The 1.x → 2.x trap this day names is ADK-73** — every agent pins its model explicitly. Part 4.2's
table is the general form: pick the cheapest instrument that answers the claim, and when the instrument
is a model, name it.

---

## §9 Say it in an interview

*"We had a metric that used an LLM to judge whether our desk's answers were correct, and the first
thing I did was ask what a procedure that does nothing would score on the same set. Our fixture was
twenty-four answers, twenty of them valid. So I scripted a judge that split three-two on every single
case — a rater that never reads anything — and its majority always landed on 'valid', which meant it
agreed with our human labels on twenty of twenty-four. Eighty-three point three per cent, from a coin,
which is exactly the base rate. A judge that actually read the answers scored ninety-five point eight.
Reported as accuracies those look like a good judge and a slightly better one; reported as margin over
the majority-class baseline they are plus zero and plus twelve and a half, and the difference is
obvious. I also measured the three biases from the LLM-as-judge literature on our own answers: a
pairwise judge that prefers whatever it sees first gave twelve confident verdicts out of twelve and
zero once every pair was shown both ways round; appending one polite sentence to four answers that were
factually wrong turned all four into passes without changing a fact; and two answers that both said
'eleven days' were graded oppositely because one was phrased the way the judge phrases things. The
uncomfortable conclusion is that judging your own model family is the default configuration and the one
bias with no cheap control — position you catch by swapping, verbosity you catch by logging length,
self-enhancement needs a second judge or human labels. So the thing I would insist on before anybody
quotes a judged number is a small, balanced, human-labelled calibration set, and the baseline printed
in the same row as the score. Take that column away and the same run reports 'both judges agree with us
most of the time; ship it'."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 81` refuses to commit until they are.

The day is finished when you can be handed any evaluation number and ask, before reacting to it, three
questions: what does a constant score on this data, what did the judge see, and which model was the
judge.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 81 | 2026-09-06 | AG-27, ADK-61 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth`, `./m trace` and `./m wiki --check` are green over
this day and every measurement in it was run. What is not green: `sutra/judge.py` is the build brief and
`lab/gate.py` reports 0 of 6, by design. Two findings carry forward — the Flash-Lite allowance is
unmeasured for a fourth day, and the human-labelled calibration set has now been parked on three
consecutive days while every number in this day depends on one.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one new row:

```text
| Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | arXiv:2306.05685 | 2023 | 2026-09-06 | 81 | `days/day-81-llm-as-judge/papers/01-judging-the-judge.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 81: llm-as-judge and honest baselines - closes AG-27, ADK-61
```
