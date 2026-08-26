# Day 1 — CHECKLIST

**IDs closed:** AG-01, OPS-01, OPS-02, OPS-03
**Principles served:** 1, 2, 4, 5, 7, 9, 10, 13, 14, 15, 16, 17, 18
**Parts:** 14 across 4 sections

> `./m done 1` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: `OK all green`, then `traceability: 4/199 closed, 0 problem(s)`, then one commit reading
`day 01: bootstrap & the map — closes AG-01, OPS-01, OPS-02, OPS-03`.

---

## AG-01 — what makes a system agentic (section 1)

- [x] Can define an agentic system in one sentence **without** using "autonomous", "intelligent" or
      "AI"
- [x] Can name the four parts of an agent, and say which one beginners forget
- [x] Can name three things autonomy **costs**, and describe the option between workflow and agent
- [x] Wrote out Sutra's six-row stage table (decider · outcome space · bound · blast radius) from
      [1.4](parts/01-what-is-an-agent/1.4-sutra-on-the-spectrum.md) **from memory**, then checked it
- [x] Can say which two Sutra stages are genuinely agentic, and how each is bounded — one by *what
      it can do*, one by *how long it can do it*

## OPS-01 — the repo is the memory (section 2)

- [x] Filled in the four-line "what Sutra is" template from
      [2.1](parts/02-repo-as-memory/2.1-what-sutra-actually-is.md), in your own words
- [x] Read `docs/adr/ADR-0001-plan-reconstruction.md` — the scar this project is built on
- [x] Can state the precedence order, and which addendum wins on which subject
- [x] Resolved the `gemini-2.5-flash` vs `gemini-3.5-flash` collision by hand, and can say why the
      honest answer is **neither document**
- [x] **Wrote `docs/adr/ADR-0005-provider-roles.md`** with all six sections
- [x] ADR-0005's *What would make us change our minds* contains at least one **number**
- [x] `grep -c "^## " docs/adr/ADR-0005-provider-roles.md` prints **6**

## OPS-02 — keys that cannot leak (section 3)

- [x] `git check-ignore -v .env` printed the rule **before** `.env` was created
- [x] All three keys created — Gemini, Groq, OpenRouter. **No card on file for any of them.**
- [x] Read your Gemini project's own rate-limit view and **wrote the numbers down**
- [x] `.env` written with `<<'EOF'` (quoted), no quotes around values, and
      `GOOGLE_GENAI_USE_VERTEXAI=FALSE`
- [x] `.env.example` updated with the **same names** and no values
- [x] `git status --porcelain` shows nothing `.env`-shaped; `--ignored` shows `!! .env`
- [x] `.env` and `.env.example` declare identical variable names (the `diff` in
      [3.2](parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md))
- [x] **`sutra/config.py` written** — `load_env`, `require`, `describe`, `ConfigError`
- [x] `describe()` reports presence and length and **never** a value
- [x] Can say why `load_env` uses `setdefault` and what breaks in a container if it does not

## OPS-03 — completeness you can compute (section 4)

- [x] Can name the two kinds of ledger and the one rule each has
- [x] Proved the "never edit a generated file" rule: appended a fake row to `TRACEABILITY.md`, ran
      `trace.py`, watched it vanish
- [x] **Wrote `days/day-01-bootstrap-and-map/lab/trace_mine.py`** — typed, not pasted
- [x] Yours and `scripts/trace.py` report the **same** `closed/total`
- [x] Read `scripts/trace.py` and can name the **four** things its extra lines buy
- [x] Can say which of those four is the difference between a check and a report

## Read the parts — one box each

Tick only when you have **read it, run its Check yourself, and answered its out-loud question**.

- [x] [1.1 Who decides the next step](parts/01-what-is-an-agent/1.1-who-decides-the-next-step.md)
- [x] [1.2 Goal, tools, loop, stop condition](parts/01-what-is-an-agent/1.2-goal-tools-loop-stop.md)
- [x] [1.3 When an agent is the wrong answer](parts/01-what-is-an-agent/1.3-when-an-agent-is-the-wrong-answer.md)
- [x] [1.4 Sutra on the spectrum](parts/01-what-is-an-agent/1.4-sutra-on-the-spectrum.md)
- [x] [2.1 What Sutra actually is](parts/02-repo-as-memory/2.1-what-sutra-actually-is.md)
- [x] [2.2 The docs tree, and which document wins](parts/02-repo-as-memory/2.2-the-docs-tree-and-precedence.md)
- [x] [2.3 The ADR that survives a cold read](parts/02-repo-as-memory/2.3-the-adr-that-survives-a-cold-read.md)
- [x] [3.1 The three free doors](parts/03-keys-and-env/3.1-the-three-free-doors.md)
- [x] [3.2 `.env`, and the environment as an interface](parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md)
- [x] [3.3 Loading keys, and failing loudly](parts/03-keys-and-env/3.3-loading-keys-failing-loudly.md)
- [x] [3.4 The rotation drill](parts/03-keys-and-env/3.4-the-rotation-drill.md)
- [x] [4.1 The diary and the scoreboard](parts/04-ledgers/4.1-the-diary-and-the-scoreboard.md)
- [x] [4.2 Build the generator yourself](parts/04-ledgers/4.2-build-the-generator-yourself.md)
- [x] [4.3 Reading the shipped generator](parts/04-ledgers/4.3-reading-the-shipped-generator.md)

### Added after this day was committed — plan v2.2.0, ADR-0008

*Day 1 shipped under plan v2.1.0, which had no paper parts. The commit stands and `PROGRESS.md` is
unchanged; this is reading the day gained afterwards, so the box is honestly open rather than
back-dated.*

- [x] [*Intelligent agents: theory and practice*](papers/01-intelligent-agents.md)
      — read it, run the demo **both ways**, and say which half of the paper survived

## Break it on purpose — watch it go red, then fix it

- [x] **RED 1:** ran `pytest tests/test_config.py` **before** writing `sutra/config.py` and watched
      it fail on the import
- [x] **RED 2:** changed `setdefault` to `os.environ[key] = value` and watched
      `test_load_env_does_not_overwrite_the_real_environment` fail — then put it back
- [x] **RED 3:** edited Day 1's hub to claim `AG-99`, ran both generators, saw **two** problems
      reported (green-but-unclaimed **and** claimed-but-unassigned) — then restored it
- [x] **RED 4:** observed that `scripts/trace.py` exits `1` on a problem and `trace_mine.py` exits
      `0` — and can say why that single difference matters
- [x] **THE DRILL:** revoked a real Groq key, saw `HTTP 401` with the body, rotated it, and verified
      **both** that the new key returns 200 and the old one does not
- [x] `.env.bak` deleted after the rotation

## Tests

- [x] `tests/test_config.py` written, all three tests green
- [x] `TODO(me)` fourth test added: `require` rejects a whitespace-only value
- [x] `uv run python -m pytest -q -m "not live"` reports **4 passed** (not `no tests ran`)

## Request budget

- [x] **0 model inference calls** today. Cost: **$0**.
- [x] The handful of `GET /models` probes were metadata endpoints, not inference — and you can say
      why that distinction matters

## Ledger & commit

- [x] `docs/PROGRESS.md` row **appended** with `>>` (never `>`), listing exactly the four IDs
- [x] `docs/PACKAGES.md` — **no rows**, and you can say why
- [x] `uv run python scripts/trace.py` prints `4/199 closed, 0 problem(s)`
- [x] `./m check` prints `OK all green`
- [x] `git status --porcelain` prints **nothing**
- [x] `git ls-files | grep -E "^\.env$"` prints **nothing**
- [x] Committed as `day 01: bootstrap & the map — closes AG-01, OPS-01, OPS-02, OPS-03`
- [x] Commit hash written back into the `PROGRESS.md` row

## Understanding check — answer out loud

- [x] What makes a system agentic, and what does that property cost you?
- [x] Why is the human gate on Sutra's *write* stage rather than at the end of the diagram?
- [x] Which addendum wins on model choice, and why was the plan not simply edited to match?
- [x] What are the six sections of an ADR, and which one do most people leave out?
- [x] Why does holding three keys from three organisations differ from three keys from one?
- [x] Why must a `401` never be retried when a `429` always should be?
- [x] Name the three things that must all agree before `trace.py` calls an ID closed.
- [x] Why does a check script need a non-zero exit code to be worth anything?

## Tomorrow

- [x] Cold-read `ADR-0005`, sign the last line, change `Status: proposed` → `accepted`
      *(deliberately not today — the gap is the point)*
