"""Regenerate docs/days/TRACEABILITY.md.

Sources of truth:
  - master plan §14: which IDs each day must close
  - docs/days/day_NNN.md headers: which IDs a day doc claims
  - PROGRESS.md: which days are actually green (only those count as closed)
Never edit TRACEABILITY.md by hand.

Usage (from the repo root):
    python tools/trace.py
    # prints e.g.:  traceability: 4/199 closed, 0 problem(s)
"""
from __future__ import annotations

import re                      # regular expressions — how we find IDs in text
from datetime import date      # to stamp the file with today's date
from pathlib import Path       # modern, clean file paths (house style)

ROOT = Path(__file__).resolve().parents[1]      # tools/trace.py -> repo root
PLAN = ROOT / "docs" / "00_MASTER_PLAN.md"      # where the day->ID map lives
DAYS = ROOT / "docs" / "days"                   # day docs + the ledgers
# One pattern matches every concept ID we use: AG-01, ADK-73, MCP-26, ...
ID_RE = re.compile(r"\b(?:AG|ADK|MCP|SK|OPS|SEC)-\d{2}\b")


def plan_map() -> dict[int, dict]:
    """Read §14 of the master plan into {day: {'phase': int, 'ids': [...]}}.

    Example:
        >>> plan_map()[4]
        {'phase': 1, 'ids': ['AG-04']}
    """
    out: dict[int, dict] = {}
    phase, in_map = None, False                 # tiny state machine, two flags
    for line in PLAN.read_text(encoding="utf-8").splitlines():
        if line.startswith("## 14"):            # found the §14 heading:
            in_map = True                       #   start paying attention
        elif in_map and line.startswith("## "): # next big heading:
            break                               #   §14 is over, stop reading
        elif in_map:
            if m := re.match(r"### Phase (\d+)", line):
                phase = int(m.group(1))         # remember the current phase
            elif (m := re.match(r"\|\s*(\d+)\s*\|", line)) and phase is not None:
                # a table row that starts with a day number -> record its IDs
                out[int(m.group(1))] = {"phase": phase, "ids": ID_RE.findall(line)}
    return out


def green_days() -> set[int]:
    """The day numbers that have a row in PROGRESS.md (i.e. finished days).

    Example:
        >>> green_days()
        {1, 2, 3}
    """
    text = (DAYS / "PROGRESS.md").read_text(encoding="utf-8")
    # every line that starts like "| 3 |" is a finished day's row
    return {int(m.group(1)) for m in re.finditer(r"^\|\s*(\d+)\s*\|", text, re.M)}


def doc_claims(day: int) -> list[str]:
    """The IDs a day doc's header claims to close (empty if no doc yet).

    Example:
        >>> doc_claims(1)
        ['AG-01', 'OPS-01', 'OPS-02', 'OPS-03']
    """
    f = DAYS / f"day_{day:03d}.md"              # e.g. day_001.md (zero-padded)
    if not f.exists():
        return []                               # day not generated yet — fine
    for line in f.read_text(encoding="utf-8").splitlines():
        if "IDs closed:" in line:               # the header row we standardize on
            return ID_RE.findall(line)          # pull every ID out of that line
    return []


def main() -> None:
    """Cross-check plan vs docs vs progress; rewrite TRACEABILITY.md."""
    plan, green = plan_map(), green_days()
    lines = [                                   # the file we are about to write
        "# Traceability (regenerated; do not edit by hand)",
        f"_Generated {date.today().isoformat()} by tools/trace.py_",
        "",
        "| ID | Phase | Planned day | Status |",
        "| --- | --- | --- | --- |",
    ]
    total = closed = 0
    problems: list[str] = []                    # anything suspicious lands here
    for day in sorted(plan):                    # walk all 96 planned days
        claimed = set(doc_claims(day))
        for cid in plan[day]["ids"]:            # every ID the plan assigns
            total += 1
            if day in green and cid in claimed:     # finished AND documented:
                closed += 1
                status = f"✅ closed day {day}"      #   properly closed
            elif day in green:                      # finished but not claimed:
                status = "🐛 green day, ID missing from doc"   # that's a bug
                problems.append(f"{cid}: day {day} is green but its doc does not claim it")
            else:
                status = "⬜ open"                   # not reached yet — normal
            lines.append(f"| {cid} | {plan[day]['phase']} | {day} | {status} |")
        # the reverse check: a doc claiming IDs the plan never gave that day
        if day in green and (extra := claimed - set(plan[day]["ids"])):
            problems.append(f"day {day} claims IDs not assigned by the plan: {sorted(extra)}")
    lines += ["", f"**{closed} / {total} IDs closed.**"]
    if problems:                                # problems get their own section
        lines += ["", "## 🐛 Problems", *[f"- {p}" for p in problems]]
    (DAYS / "TRACEABILITY.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"traceability: {closed}/{total} closed, {len(problems)} problem(s)")


if __name__ == "__main__":                      # run as a script, not on import
    main()
