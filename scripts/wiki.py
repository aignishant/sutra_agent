#!/usr/bin/env python
"""Regenerate docs/WIKI.md and docs/wiki/ - a compact index over days/.

Sources of truth (every line written is copied from one of these, never generated):
  - days/day-NN-<slug>/parts/**/*.md and papers/*.md: frontmatter, plus the paragraph under
    `## One-line answer`

Three tiers, so a session reads what it needs and nothing else:
  - docs/WIKI.md          one row per day
  - docs/wiki/day-NN.md   one day's parts and papers, each with its one-line answer
  - docs/wiki/ENTITIES.md every curriculum ID and every paper, with where they are taught

Never edit these by hand - the next `./m check` overwrites you. Nothing here is a substitute for
the day itself: the wiki says what a part answers, the part says why.

    uv run python scripts/wiki.py           # regenerate
    uv run python scripts/wiki.py --check   # fail if the wiki is out of date with days/
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAYS = ROOT / "days"
DOCS = ROOT / "docs"

# Frontmatter here is simple `key: value`, where a value is a scalar or a JSON-ish list of strings.
# That is narrow enough to read directly and saves a yaml dependency the project does not otherwise
# need - the same call trace.py makes.
_KV = re.compile(r"^([a-z_]+):\s*(.*)$")
_QUOTED = re.compile(r'"([^"]*)"')
_ANSWER = re.compile(r"^## One-line answer\s*\n+(.+?)(?=\n\s*\n|\n---)", re.S | re.M)


def parse_front(text: str) -> dict[str, object]:
    """Read the leading `---` fenced block into a dict, keeping list values as lists."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    out: dict[str, object] = {}
    for line in text[3:end].splitlines():
        if m := _KV.match(line.strip()):
            key, raw = m.group(1), m.group(2).strip()
            out[key] = _QUOTED.findall(raw) if raw.startswith("[") else raw.strip('"')
    return out


def one_line_answer(text: str) -> str:
    """The paragraph under `## One-line answer`, flattened to one line and stripped of emphasis."""
    if not (m := _ANSWER.search(text)):
        return ""
    return re.sub(r"\*\*|\*|`", "", " ".join(m.group(1).split()))


@dataclass
class Doc:
    """One part or one paper document, read down to the two things the index needs."""

    path: Path
    front: dict[str, object]
    answer: str

    @property
    def number(self) -> str:
        return str(self.front.get("part") or self.front.get("paper") or "")

    @property
    def title(self) -> str:
        return str(self.front.get("title", self.path.stem))

    @property
    def ids(self) -> list[str]:
        value = self.front.get("ids", [])
        return value if isinstance(value, list) else []

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


@dataclass
class Day:
    """One day folder: its parts in numbering order, then its papers in reading order."""

    number: int
    folder: Path
    parts: list[Doc] = field(default_factory=list)
    papers: list[Doc] = field(default_factory=list)

    @property
    def ids(self) -> list[str]:
        # dict, not set: the hub's map orders the IDs and that order is worth keeping.
        seen: dict[str, None] = {}
        for doc in self.parts:
            for cid in doc.ids:
                seen[cid] = None
        return list(seen)

    @property
    def title(self) -> str:
        hub = self.folder / "LESSON.md"
        if hub.exists():
            front = parse_front(hub.read_text(encoding="utf-8", errors="replace"))
            if front.get("title"):
                return str(front["title"])
        return self.folder.name


def collect() -> list[Day]:
    """Every written day, with its parts and papers read into Docs."""
    days: list[Day] = []
    for folder in sorted(DAYS.glob("day-*")):
        if not (m := re.match(r"day-(\d+)", folder.name)):
            continue
        day = Day(number=int(m.group(1)), folder=folder)
        for md in sorted(folder.glob("parts/*/*.md")):
            text = md.read_text(encoding="utf-8", errors="replace")
            day.parts.append(Doc(md, parse_front(text), one_line_answer(text)))
        for md in sorted(folder.glob("papers/*.md")):
            text = md.read_text(encoding="utf-8", errors="replace")
            day.papers.append(Doc(md, parse_front(text), one_line_answer(text)))
        days.append(day)
    return days


def render_top(days: list[Day]) -> str:
    """Tier 1: one row per day. No generation date, so `--check` can compare byte for byte."""
    lines = [
        "# Sutra wiki - tier 1 (regenerated; do not edit by hand)",
        "",
        "One row per day. For a day's parts open `docs/wiki/day-NN.md`; open the day folder itself",
        "only to write it. Cross-day lookups live in `docs/wiki/ENTITIES.md`.",
        "",
        "| Day | Subject | IDs closed | Parts | Papers |",
        "| --- | ------- | ---------- | ----- | ------ |",
    ]
    for day in days:
        ids = ", ".join(day.ids) or "-"
        papers = ", ".join(str(p.front.get("paper", "")) for p in day.papers) or "-"
        lines.append(
            f"| [{day.number:02d}](wiki/day-{day.number:02d}.md) | {day.title} | {ids} "
            f"| {len(day.parts)} | {papers} |"
        )
    return "\n".join(lines) + "\n"


def render_day(day: Day) -> str:
    """Tier 2: one day's parts and papers, each with its own one-line answer."""
    source = day.folder.relative_to(ROOT).as_posix()
    lines = [
        f"# Day {day.number:02d} - {day.title}",
        "",
        f"IDs closed: {', '.join(day.ids) or '-'} · source: `{source}/`",
        "",
        "## Parts",
        "",
    ]
    for doc in day.parts:
        level, ids = doc.front.get("level", "?"), ", ".join(doc.ids) or "-"
        lines += [
            f"### {doc.number} - {doc.title}",
            f"`{doc.rel}` · level `{level}` · ids {ids}",
            "",
            doc.answer or "_(no one-line answer found - the part is incomplete)_",
            "",
        ]
    if day.papers:
        lines += ["## Papers - read after the parts", ""]
        for doc in day.papers:
            lines += [
                f"### {doc.front.get('paper', '?')} - {doc.title}",
                f"`{doc.rel}`",
                "",
                doc.answer or "_(no one-line answer found - the paper doc is incomplete)_",
                "",
            ]
    return "\n".join(lines) + "\n"


def render_entities(days: list[Day]) -> str:
    """Tier 3: cross-day lookups - which day teaches an ID, where a paper is taught and cited."""
    by_id: dict[str, list[tuple[Day, Doc]]] = {}
    by_paper: dict[str, list[tuple[Day, Doc]]] = {}
    for day in days:
        for doc in day.parts:
            for cid in doc.ids:
                by_id.setdefault(cid, []).append((day, doc))
            cited = doc.front.get("papers", [])
            for pid in cited if isinstance(cited, list) else []:
                by_paper.setdefault(pid, []).append((day, doc))
        for doc in day.papers:
            if pid := str(doc.front.get("paper", "")):
                by_paper.setdefault(pid, []).insert(0, (day, doc))

    lines = [
        "# Sutra wiki - entities (regenerated; do not edit by hand)",
        "",
        "Cross-day lookups. Answers 'which day taught this?' without opening a day folder.",
        "",
        "## By curriculum ID",
        "",
    ]
    for cid in sorted(by_id):
        where = ", ".join(
            f"[{d.number:02d}/{doc.number}](day-{d.number:02d}.md)" for d, doc in by_id[cid]
        )
        lines.append(f"- **{cid}** - {len(by_id[cid])} parts: {where}")

    lines += ["", "## By paper", "", "A paper is taught once in the whole curriculum.", ""]
    for pid in sorted(by_paper):
        taught = [(d, doc) for d, doc in by_paper[pid] if "/papers/" in doc.path.as_posix()]
        cites = [(d, doc) for d, doc in by_paper[pid] if "/papers/" not in doc.path.as_posix()]
        title = taught[0][1].title if taught else "?"
        home = f"day {taught[0][0].number:02d}" if taught else "**not taught anywhere**"
        cited_by = ", ".join(f"{d.number:02d}/{doc.number}" for d, doc in cites) or "no parts"
        lines += [f"- **{pid}** - {title}", f"  - taught in {home}; cited by {cited_by}"]
    return "\n".join(lines) + "\n"


def render_all(days: list[Day]) -> dict[Path, str]:
    """Every file the wiki owns, as {path: content}. Writing and checking share this."""
    out = {DOCS / "WIKI.md": render_top(days), DOCS / "wiki" / "ENTITIES.md": render_entities(days)}
    for day in days:
        out[DOCS / "wiki" / f"day-{day.number:02d}.md"] = render_day(day)
    return out


def main() -> int:
    days = collect()
    files = render_all(days)

    if "--check" in sys.argv[1:]:
        stale = [
            path.relative_to(ROOT).as_posix()
            for path, content in files.items()
            if not path.exists() or path.read_text(encoding="utf-8") != content
        ]
        if stale:
            print(f"wiki: STALE - {len(stale)} file(s) differ from days/; run ./m wiki")
            for name in sorted(stale)[:10]:
                print(f"  {name}")
            return 1
        print(f"wiki: up to date ({len(days)} days, {len(files)} files)")
        return 0

    (DOCS / "wiki").mkdir(exist_ok=True)
    for path, content in files.items():
        path.write_text(content, encoding="utf-8")
    parts = sum(len(d.parts) for d in days)
    papers = sum(len(d.papers) for d in days)
    missing = sum(1 for d in days for doc in d.parts + d.papers if not doc.answer)
    note = f", {missing} without a one-line answer" if missing else ""
    print(f"wiki: {len(days)} days, {parts} parts, {papers} papers indexed{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
