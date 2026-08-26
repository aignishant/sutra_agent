#!/usr/bin/env python
"""Regenerate docs/TRACKER.md from the master plan's §14 day map plus what is on disk.

The single source of truth for the day list is the plan; this script never invents a day. Status is
read from the filesystem and the checklists, so the tracker cannot drift from reality.

Under plan v2.2.1 a day counts as *written* only when it has the hub **and** a non-empty parts/
directory (Principle 16, plan §17). The part count is reported per day, which is what makes a thin
day visible from the progress table alone.

    uv run python scripts/tracker.py            # rewrite docs/TRACKER.md
    uv run python scripts/tracker.py --summary  # one-line progress, no file written
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs" / "00_MASTER_PLAN.md"
TRACKER = ROOT / "docs" / "TRACKER.md"
DAYS = ROOT / "days"

PHASE_RE = re.compile(r"^### Phase (\d+) — (.+?)\s*\((?:Days?\s*)?([\d\-–]+)\)\s*$")
ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*$")
ID_RE = re.compile(r"\b(?:AG|ADK|MCP|SK|OPS|SEC)-\d{2}\b")


@dataclass
class Day:
    number: int
    title: str
    ids: str
    phase: int
    phase_name: str
    written: bool = False
    has_checklist: bool = False
    complete: bool = False
    open_boxes: int = 0
    folder: str = ""
    parts: int = 0
    legacy: bool = False


@dataclass
class Phase:
    number: int
    name: str
    span: str
    days: list[Day] = field(default_factory=list)


def parse_plan() -> list[Phase]:
    """Read §14 of the master plan and return its phases in order."""
    if not PLAN.exists():
        sys.exit(f"missing {PLAN} - the tracker has nothing to track")

    phases: list[Phase] = []
    current: Phase | None = None
    in_map = False

    for line in PLAN.read_text(encoding="utf-8").splitlines():
        if line.startswith("## 14"):
            in_map = True
            continue
        if in_map and line.startswith("## "):
            break
        if not in_map:
            continue
        if header := PHASE_RE.match(line):
            current = Phase(int(header.group(1)), header.group(2), header.group(3))
            phases.append(current)
            continue
        if current is None:
            continue
        if row := ROW_RE.match(line):
            title = row.group(2).replace("**", "")
            if title.strip("- ") in {"Title", ""}:
                continue
            ids = ", ".join(ID_RE.findall(row.group(3))) or "—"
            current.days.append(
                Day(
                    number=int(row.group(1)),
                    title=title,
                    ids=ids,
                    phase=current.number,
                    phase_name=current.name,
                )
            )
    return phases


def find_folder(number: int) -> Path | None:
    """The folder for a day, whatever slug follows its number (plan §17.2).

    The number is the identity and the slug is a label on it, so `day-01`, `day-1` and
    `day-01-bootstrap-and-map` all resolve to day 1.
    """
    exact = [DAYS / f"day-{number:02d}", DAYS / f"day-{number}"]
    slugged = sorted(p for p in DAYS.glob(f"day-{number:02d}-*") if p.is_dir())
    return next((p for p in [*slugged, *exact] if p.is_dir()), None)


def inspect(day: Day) -> Day:
    """Fill in on-disk status for one day."""
    legacy_doc = ROOT / "legacy" / "days" / f"day_{day.number:03d}.md"
    day.legacy = legacy_doc.is_file()

    folder = find_folder(day.number)
    if folder is None:
        return day
    day.folder = folder.relative_to(ROOT).as_posix()
    parts_dir = folder / "parts"
    day.parts = len(list(parts_dir.glob("*/*.md"))) if parts_dir.is_dir() else 0
    # A hub without parts/ is not a written day (plan §17.2).
    day.written = (folder / "LESSON.md").is_file() and day.parts > 0

    checklist = folder / "CHECKLIST.md"
    day.has_checklist = checklist.is_file()
    if day.has_checklist:
        text = checklist.read_text(encoding="utf-8")
        day.open_boxes = len(re.findall(r"^- \[ \]", text, flags=re.M))
        ticked = len(re.findall(r"^- \[x\]", text, flags=re.M | re.I))
        day.complete = day.open_boxes == 0 and ticked > 0
    return day


def badge(day: Day) -> str:
    if day.complete:
        return "✅ done"
    if day.written and day.has_checklist:
        return "📄 written"
    if day.written:
        return "⚠️ no checklist"
    if day.legacy:
        return "🗃️ legacy"
    return "⬜ pending"


def bar(done: int, total: int, width: int = 40) -> str:
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def row(day: Day) -> str:
    title = day.title if len(day.title) <= 78 else day.title[:75] + "…"
    boxes = str(day.open_boxes) if day.has_checklist else "—"
    parts = str(day.parts) if day.parts else "—"
    return f"| {day.number} | {title} | {day.ids} | {badge(day)} | {parts} | {boxes} |"


def build(phases: list[Phase]) -> tuple[str, dict[str, int]]:
    for phase in phases:
        phase.days = [inspect(d) for d in phase.days]
    all_days = [d for p in phases for d in p.days]

    stats = {
        "total": len(all_days),
        "written": sum(d.written for d in all_days),
        "complete": sum(d.complete for d in all_days),
        "legacy": sum(d.legacy and not d.written for d in all_days),
        "parts": sum(d.parts for d in all_days),
    }
    stats["pending"] = stats["total"] - stats["written"]
    total = stats["total"] or 1

    out: list[str] = [
        "---",
        "name: tracker",
        "plan: sutra",
        f'generated: "{date.today().isoformat()}"',
        "generator: scripts/tracker.py",
        "---",
        "",
        "# 📊 TRACKER — Project Sutra",
        "",
        "> **Do not edit this file by hand.** It is regenerated by `./m tracker` (and "
        "automatically by `./m done N`) from the master plan's §14 day map plus what is on disk.",
        "",
        "> **Plan v2.2.1.** A day counts as *written* only when it has a hub **and** a non-empty "
        "`parts/` directory (Principle 16 · plan §17). Days marked 🗃️ legacy still have their "
        "v1.2.1-R single-file lesson at `legacy/days/day_NNN.md`; that document is a correctness "
        "source to mine, not a day (see `legacy/README.md`).",
        "",
        "## Progress",
        "",
        "| | Count | Of total |",
        "|---|---|---|",
        f"| 📄 Days written in the hub + parts/ shape | **{stats['written']}** |"
        f" {100 * stats['written'] / total:.1f}% |",
        f"| 📚 Sub-topic documents in `parts/` | **{stats['parts']}** | — |",
        f"| ✅ Days completed (checklist fully ticked) | **{stats['complete']}** |"
        f" {100 * stats['complete'] / total:.1f}% |",
        f"| 🗃️ Legacy days awaiting regeneration | **{stats['legacy']}** |"
        f" {100 * stats['legacy'] / total:.1f}% |",
        f"| ⬜ Never written | **{stats['pending'] - stats['legacy']}** |"
        f" {100 * (stats['pending'] - stats['legacy']) / total:.1f}% |",
        f"| Total days in plan | {stats['total']} | (Day 0 + Days 1–96) |",
        "",
        "```",
        f"written  {bar(stats['written'], total)}  {stats['written']}/{stats['total']}",
        f"complete {bar(stats['complete'], total)}  {stats['complete']}/{stats['total']}",
        f"legacy   {bar(stats['legacy'], total)}  {stats['legacy']}/{stats['total']}",
        "```",
        "",
        "**Legend:** ✅ done (checklist fully ticked) · 📄 written (hub + `parts/` + checklist) · "
        "⚠️ no checklist · 🗃️ legacy (v1 lesson only, needs regenerating) · ⬜ pending",
        "",
        "## By phase",
        "",
        "| Phase | Theme | Days | Written | Parts | Done |",
        "|---|---|---|---|---|---|",
    ]

    for phase in phases:
        out.append(
            f"| {phase.number} | {phase.name} | {phase.span} | "
            f"{sum(d.written for d in phase.days)}/{len(phase.days)} | "
            f"{sum(d.parts for d in phase.days)} | "
            f"{sum(d.complete for d in phase.days)}/{len(phase.days)} |"
        )

    out += ["", "## Every day", ""]
    for phase in phases:
        out += [
            f"### Phase {phase.number} — {phase.name} (Days {phase.span})",
            "",
            "| Day | Title | IDs | Status | Parts | Open boxes |",
            "|---|---|---|---|---|---|",
        ]
        out += [row(d) for d in phase.days]
        out.append("")

    out += ["## Next up", ""]
    pending = [d for d in all_days if not d.written]
    if pending:
        out.append("The next ten days to write, in order:")
        out.append("")
        out += [
            f"- **Day {d.number}** — {d.title} `({d.ids})`"
            + ("  ·  🗃️ has a v1 lesson to mine" if d.legacy else "")
            for d in pending[:10]
        ]
    else:
        out.append("Every day is written. 🎉")
    out.append("")
    return "\n".join(out), stats


def main() -> int:
    phases = parse_plan()
    content, stats = build(phases)
    if "--summary" in sys.argv:
        print(
            f"Sutra: {stats['written']}/{stats['total']} days in the hub + parts/ shape "
            f"({stats['parts']} sub-topic docs), {stats['complete']} completed, "
            f"{stats['legacy']} legacy to regenerate, "
            f"{stats['pending'] - stats['legacy']} never written."
        )
        return 0
    TRACKER.write_text(content + "\n", encoding="utf-8")
    print(f"wrote {TRACKER.relative_to(ROOT)} - {stats['written']}/{stats['total']} written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
