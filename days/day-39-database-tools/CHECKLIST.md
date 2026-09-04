# Day 39 — definition of done

`./m done 39` refuses to commit until every box is ticked. Tick a box only after you have actually
run the thing it names.

## Read

- [ ] All twenty parts read, in order, sections 1 → 6.
- [ ] The paper read **after** the parts: `papers/01-relational-model.md`.
- [ ] You can say, without the page open, what each of the five brakes stops **and** what it does
      not stop.

## The archive

- [ ] `sutra/data/` exists, and you confirmed `.gitignore` already carries `*.sqlite3` — no new line
      was added.
- [ ] `sutra_mcp/db_tools.py` exists and exports `ARCHIVE`, `build_archive`, `connect_readonly`,
      `lookup_ticket`, `search_tickets`, `register_db_tools`.
- [ ] `build_archive()` runs and produces `sutra/data/tickets.sqlite3` with the Day 3 tickets in it.
- [ ] `git status` shows no `.sqlite3` file staged or untracked-and-noisy.
- [ ] `sutra/loop.py` is unchanged. Today does not edit it.
- [ ] `build_server()` is not redefined — `register_db_tools(server)` registers into Day 34's server.

## The five brakes, in `sutra_mcp/db_tools.py`

- [ ] Every statement is a literal and every value is bound with `?`. No f-string, `+` or `%` builds
      SQL anywhere in the file.
- [ ] `connect_readonly()` is the only place `sqlite3.connect` is called on the read path, and it
      uses `file:...?mode=ro` **with `uri=True`**.
- [ ] An authorizer is installed, allowing `SQLITE_SELECT`, `SQLITE_READ` and `SQLITE_FUNCTION` and
      denying everything else.
- [ ] `search_tickets` clamps `limit` in code **and** binds it into `LIMIT ?`, asks for one row more
      than it returns, and reports `truncated`.
- [ ] A work budget is installed — `set_progress_handler` — and the counter is per call, not
      module-level.
- [ ] The connection is opened inside each tool and closed in a `finally`. There is no module-level
      connection object in the file.

## The evals (each one actually run, exit code read)

- [ ] `uv run python days/day-39-database-tools/lab/brake_audit.py` → `findings: 0`, `exit: 0`.
- [ ] You saw it RED first: `findings: 6`, `exit: 1`, before the file existed.
- [ ] `uv run python days/day-39-database-tools/lab/brakes.py` → five HELD, `exit: 0`, and brake 0
      FAILED with `attack returned 205`.
- [ ] You broke one brake on purpose and watched the exit code become 1.
- [ ] `uv run python days/day-39-database-tools/lab/drift.py` → you fixed `DESCRIPTION` and reached
      `findings: 0`, `exit: 0`.
- [ ] `uv run python days/day-39-database-tools/lab/injection.py` → you read the five rows the
      formatted version returned, including the two marked `closed`.
- [ ] `uv run python days/day-39-database-tools/lab/flood.py` → you read `173.0% of the window` and
      the `LIMIT 200` line beside it.
- [ ] `uv run python days/day-39-database-tools/lab/undo.py` → you read the three lines that close
      the three ways of getting the rows back.
- [ ] `uv run python days/day-39-database-tools/lab/hold.py` → you saw `database is locked` on arm B
      and nowhere else.
- [ ] `uv run python days/day-39-database-tools/lab/adk_tools.py` → you read the declaration and
      found the docstring inside it, whole.
- [ ] `uv run python days/day-39-database-tools/lab/toolset_shape.py` → you saw `execute_sql` and
      `list_tables` dropped by the filter, and the `MCPToolset` deprecation warning.

## The paper demo, both arms

- [ ] `LAYOUT=v1 uv run python answer.py` → both `navigate` and `query` SURVIVED.
- [ ] `LAYOUT=v2 uv run python answer.py` → `navigate` WRONG ANSWER `[]`, `query` SURVIVED.
- [ ] You can say why `navigate` returned an empty list rather than raising.

## Toolbox and the extras (🅿️ parked — nothing installed)

- [ ] You read the real prebuilt SQLite configuration and found `execute_sql` and its six-word
      description.
- [ ] You can state Sutra's decision and the trigger that expires it, in your own words.
- [ ] `grep -ci "^Provides-Extra" .venv/Lib/site-packages/google_adk-2.7.1.dist-info/METADATA`
      prints `23`, and you can name five extras and what each is for.
- [ ] No binary was downloaded. No extra was installed.

## The `TODO(me)` items

- [ ] All eleven `TODO(me)` markers in the hub's §4 have been read, and you have decided which ones
      you are doing today and which are recorded as open.
- [ ] The decision in **4.2** is written down somewhere durable — an ADR is the right home.

## Gates

- [ ] `git diff pyproject.toml uv.lock` prints nothing. Today installs nothing.
- [ ] `./m depth 39` is green.
- [ ] `./m check` is green.
- [ ] `docs/PROGRESS.md` has the day 39 row from the hub's §11, with the real date and commit hash.
