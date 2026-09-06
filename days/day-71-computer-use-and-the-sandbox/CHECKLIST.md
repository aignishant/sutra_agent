# Day 71 — Definition of done

`./m done 71` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it. This is the first day in a long time that adds a package, so
the setup boxes matter more than usual.

## Before you start

- [ ] Day 70's parts and checklist are done.
- [ ] `uv add "playwright==1.62.0"` run, and the version came from
      `pypi.org/pypi/playwright/json` on **your** date rather than from this document (P7).
- [ ] `uv run playwright install chromium` run, and you know why it is a separate step from
      `uv sync` — a checkout with the package and no browser fails at `chromium.launch()`.
- [ ] `docs/PACKAGES.md` row appended, including the second-step trap.
- [ ] `lab/` scaffolded per §3 — eight Python files, two HTML fixtures, two under
      `lab/papers/native-client/`.
- [ ] `git check-ignore -v days/day-71-computer-use-and-the-sandbox/lab/site/status.html` prints a
      matching rule. A browser run writes cache and profile data and none of it belongs in git (P9).
- [ ] `uv run python days/day-71-computer-use-and-the-sandbox/lab/gate.py; echo "exit: $?"` is
      **red** on all six checks before you write anything.
- [ ] You read `lab/_computer.py` before any part. Every measurement in this day is a count over its
      `Trace`.

## Section 1 — no API

- [ ] **1.1** read · served the fixture with `_site.py` and opened it in your own browser · can name
      the five rungs of the ladder and say why computer use is the last one
- [ ] **1.2** read · ran `look.py --both` · recorded **28165** and **14323** screenshot bytes · can
      name the two fields `ComputerState` has, and say what it does **not** carry
- [ ] You saw the `[EXPERIMENTAL] feature FeatureName.COMPUTER_USE is enabled` warning on stderr and
      can say what Preview status means for shipping this
- [ ] **1.3** read · ran `surface.py` · recorded **declared 15, used 1** and can name at least ten of
      the fifteen · triggered the abstract-class `TypeError` yourself and read it

## Section 2 — driving it

- [ ] **2.1** read · can describe the loop in one sentence and name the earlier day whose loop it is
- [ ] You can say why the model is scripted here and what is **not** simulated — the browser, the
      toolset, the runtime and the plugin hooks are all real
- [ ] **2.2** read · found `_normalize_x` in the installed `google-adk==2.7.1` source · saw
      `click_at(120, 300)` recorded as **(153,280)** · can say why a sandbox rule written in raw
      pixels is written in the wrong units
- [ ] **2.3** read · can give all three reasons the fixture is local, and say which one is about
      safety rather than convenience

## Section 3 — the door

- [ ] **3.1** read · ran `door.py` and `door.py --open` · recorded **3 of 5** against **5 of 5**
      actions reaching the browser, and that the secret is typed only in the second · can say why the
      door is a plugin rather than a check inside `navigate`
- [ ] You noticed the off-origin navigation in the undoored run carries
      `net::ERR_NAME_NOT_RESOLVED`, and can say why that does **not** make the run safe
- [ ] **3.2** read · read ADK's own guard in
      `google/adk/tools/computer_use/computer_use_toolset.py` · can say what it does about a
      backslash in the authority and why resolving the hostname matters
- [ ] You noticed the guard reports by **logging a warning** and returning `{"error": ...}`, not by
      raising, and can say what that means for a caller watching for exceptions
- [ ] **3.3** read · ran `guard.py` and `guard.py --opt-out` · recorded **0 of 3** against **3 of 3**
      · can name the two targets besides the fixture and say why each one matters
- [ ] **3.4** read · ran `door.py` and read its refusal lines · can say what a refusal must carry to
      be usable during an incident rather than only during the request

## Section 4 — in production

- [ ] **4.1** read · found `_verdict`'s `return ""` default · can say what happens to the sandbox the
      day the framework adds a sixteenth action, and what you would change
- [ ] **4.2** read · can name the hosted sandboxes that are 🅿️ **parked** and say why (an account is
      required, and Addendum 02 forbids a required account-gated service) · can name at least two
      isolation layers that are free and real here
- [ ] **4.3** read · can state what computer use buys and what it costs, using this day's own numbers
      on both sides

## The paper — read it last

- [ ] `papers/01-native-client.md` read **after** the parts, not before
- [ ] Ran the demo both ways from `lab/papers/native-client/`: `demo.py` executes **4 of 6** and
      exits 0; `demo.py --off` executes **6 of 6** and exits 1
- [ ] Can say what the ablation proves — the stream is identical and unobfuscated in both runs, so
      the only variable is whether anything decided before executing
- [ ] Can name this day's two layers and say which of the paper's two they each correspond to

## Build brief

- [ ] `sutra/browser_sandbox.py` written: a `BasePlugin`, `ALLOWED_ORIGINS` as data, hook parameters
      named `(tool, tool_args, tool_context)`, and a refusal that carries rule, origin and run
- [ ] You decided the default for an unknown action name and defended it in the module docstring
- [ ] `tests/test_browser_sandbox.py` written, including the test that fails when the declared action
      list grows
- [ ] `uv run python gate.py; echo "exit: $?"` re-run · you can say which of the six cleared

## Repo hygiene

- [ ] `./m depth 71` green — thirteen parts and one paper
- [ ] `./m trace` green, and AG-31, SEC-14 and ADK-50 close on this day and no others
- [ ] `./m wiki` run, so `docs/WIKI.md` and `docs/wiki/day-71.md` are not stale
- [ ] `uv run ruff format --check days/day-71-computer-use-and-the-sandbox` clean
- [ ] `uv run ruff check days/day-71-computer-use-and-the-sandbox/lab` clean
- [ ] `git diff pyproject.toml uv.lock` shows **only** the playwright addition
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real commit hash and the `⚠️` the
      gate actually earned — no rounding up (P10)
- [ ] `docs/PAPERS.md` row for `doi:10.1109/SP.2009.25` present and dated, with the record checked
      live rather than recalled (P7, §17.4.1)
