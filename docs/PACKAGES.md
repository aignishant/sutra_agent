# Package Ledger — Project Sutra

Append-only. Principle 7: **never invent a version number.** Every install gets a row here with the
version actually observed, the date it was observed, the day that added it, and why. If a version
could not be looked up, the row says `TODO(<the exact lookup command>)` — never a guess.

*(Reset at plan v2.0.0. The v1.2.1-R package ledger is frozen at `legacy/ledgers/PACKAGES.md`.)*

| Package | Version | Date | Day | Why |
| ------- | ------- | ---- | --- | --- |
| git | 2.54.0.windows.1 | 2026-08-23 | 0 | Version control + Git Bash, the shell every day document is written for. Observed with `git --version`. |
| uv | 0.12.3 | 2026-08-23 | 0 | One binary owns the environment: venv + install + lock + run. Observed with `uv --version`. |
| python | 3.12.13 | 2026-08-23 | 0 | Runtime — 3.12 per plan §5 (the stability pick inside ADK's 3.10–3.14 window). Newest 3.12 patch offered by `uv python list`. |
| ruff | 0.16.4 | 2026-08-23 | 0 | Lint + format, one tool. Resolved with `uv pip compile` against PyPI. Dev dependency. |
| pytest | 9.1.1 | 2026-08-23 | 0 | The test runner behind `./m check`. Read from `pypi.org/pypi/pytest/json`. Dev dependency. |
| python | 3.12.12 | 2026-08-24 | 0 | **Correction to the 2026-08-23 row.** `uv python list` *offers* 3.12.13 but it is `<download available>`, not installed; the interpreter this venv actually runs is 3.12.12 (`uv run python -c "import sys; print(sys.version)"`). Principle 7 records the version observed, not the version available. |
| google-genai | 2.19.0 | 2026-08-24 | 0 | |
| google-genai | 2.19.0 | 2026-08-24 | 2 | Raw Gemini SDK — Sutra's first model calls. Looked up on PyPI before pinning (uploaded 2026-08-19, requires Python >=3.10). **Completes the empty 2026-08-24 Day 0 row above**, which recorded the version but neither the day that added it nor why. ADK arrives Day 5. |
| gemini-3.7-flash (model) | free tier; **20 requests per day** on `generativelanguage.googleapis.com/generate_content_free_tier_requests` | 2026-08-25 | 2 | Primary brain. Repinned from gemini-3.5-flash per CHANGELOG_PLAN.md 2026-08-24; the model Google's own current quickstart uses. Verified callable by live call, not by listing. The quota number is not from a table — no public one exists — it was read off a live 429. **Per day, not per minute**: 28 requests across 15 minutes, each obeying the stated `Please retry in ~53s`, were all refused, so the hint is a backoff suggestion and not a window reset (part 1.5, ADR-0007). |
| google-adk | 2.7.1 | 2026-08-26 | 5 | The agent framework. Plan §5's baseline was 2.6.3 (observed 2026-08-12); §5 instructs re-verification on install day and this is it — a dated observation superseding a dated observation, not a Principle 14 amendment. Uploaded 2026-08-17, requires Python >=3.10 (read from `pypi.org/pypi/google-adk/2.7.1/json`); `google.adk.__version__` on the installed package agrees. **Behaviour note (Day 5, part 7.1):** 2.7.x's `AgentLoader` treats any directory containing an `agent.py` as a single-agent directory, so `adk run sutra/desk` fails with `Agent not found: 'desk'. In single agent mode, only 'sutra' is accessible.` — `sutra/agent.py` (Day 4) is what triggers it. `adk web sutra/desk` accepts the same path and works. |
