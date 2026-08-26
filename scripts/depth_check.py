#!/usr/bin/env python
"""Enforce the master plan's §17 depth contract on a day folder.

A day is written when it is a hub plus one document per subtopic (Principle 16), each taken from
zero prior knowledge through to production (Principle 18), with no clock anywhere (Principle 17).
This script is the machine-readable half of that contract. It cannot judge whether an explanation
is any good - that is what §17.8 and reading are for - but it can refuse a day that has no parts,
a numbering gap, a missing required section, a code block nobody walked through, a smuggled-in
time estimate, a part loose outside its section folder, a folder whose name is a bare number with no
slug saying what is in it, or a hub that quietly went back to teaching.

    uv run python scripts/depth_check.py          # every day that has a parts/ directory
    uv run python scripts/depth_check.py 0        # just day 0
    uv run python scripts/depth_check.py 4 5 6    # several days

Exit code 0 means every checked day satisfies the contract. Anything else is a failure list.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAYS = ROOT / "days"

# parts/<NN>-<slug>/<section>.<subtopic>-<kebab-slug>.md
#   ->  "parts/02-repo-skeleton/2.3-gitignore-before-secrets-exist.md"
PART_NAME_RE = re.compile(r"^(\d+)\.(\d+)-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")

# A section folder is the section number zero-padded to two digits, then what the section is about:
# 01-toolchain, 02-repo-skeleton, ... (plan §17.2). The number is the identity; the slug is a label
# on it, so nothing downstream reads the slug and a folder can be renamed to a better one freely.
SECTION_DIR_RE = re.compile(r"^(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")

# papers/<NN>-<paper-slug>.md  ->  "papers/01-subword-units.md" (plan §17.4.2). Papers sit beside
# parts/, not inside it: a paper is not a subtopic of a section, and a reader looking for where the
# day's ideas came from is on a different errand from one reading the day itself.
PAPER_NAME_RE = re.compile(r"^(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")

# days/day-<NN>-<slug>/  ->  "day-01-bootstrap-and-map". Same rule, one level up.
DAY_DIR_RE = re.compile(r"^day-(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")

# The twelve required sections of a part document (plan §17.4). Section 1 is the frontmatter,
# checked separately; these are the eleven that appear in the body, in this order.
PART_SECTIONS = [
    ("one-line answer", re.compile(r"^#{2,3}\s.*one[- ]line answer", re.I | re.M)),
    ("the story", re.compile(r"^#{2,3}\s.*the story", re.I | re.M)),
    ("the idea in plain language", re.compile(r"^#{2,3}\s.*idea in plain language", re.I | re.M)),
    ("why Sutra needs it", re.compile(r"^#{2,3}\s.*why sutra needs it", re.I | re.M)),
    ("the paper behind it", re.compile(r"^#{2,3}\s.*the paper behind it", re.I | re.M)),
    ("the mechanism", re.compile(r"^#{2,3}\s.*mechanism", re.I | re.M)),
    ("line by line", re.compile(r"^#{2,3}\s.*line by line|^\*\*Line by line:?\*\*", re.I | re.M)),
    ("the paper in one demo", re.compile(r"^#{2,3}\s.*paper in one demo", re.I | re.M)),
    ("when it breaks", re.compile(r"^#{2,3}\s.*when it breaks", re.I | re.M)),
    ("in production", re.compile(r"^#{2,3}\s.*in production", re.I | re.M)),
    ("check yourself", re.compile(r"^#{2,3}\s.*check yourself", re.I | re.M)),
]

# Three of the twelve sections are conditional (plan §17.4); the other nine are unconditional.
# Each is required exactly when its trigger is present, and is never asked for otherwise.
#
#   "the paper behind it" - the idea has a citable origin document. No script can decide that, so
#       the writer declares it: the section is required exactly when the frontmatter carries a
#       non-empty `papers` list, and the list is required exactly when the section is there. The
#       pair is checkable even though the question behind it is not.
#   "line by line" - explains code, so a part with no code to explain cannot have one. A `concept`
#       part (plan §17.7) may legitimately carry no runnable block at all.
#   "the paper in one demo" - a paper part owes the reader the paper made runnable and stripped to
#       nothing but itself (§17.4.2). Only a paper part does, so the trigger is `paper` (singular).
CONDITIONAL_SECTIONS: dict[str, Callable[[str, dict[str, str]], bool]] = {
    "the paper behind it": lambda content, meta: bool(paper_ids(meta.get("papers", ""))),
    "line by line": lambda content, meta: has_explainable_code(content),
    "the paper in one demo": lambda content, meta: bool(paper_ids(meta.get("paper", ""))),
}

# "Line by line" is written as a `**Line by line:**` list immediately after each code block, so it
# has no single position: on most parts the first one falls in the mechanism, but on a paper part
# whose mechanism is a table and a diagram, the first code block is in the demo. Its real
# enforcement is unexplained_code_blocks(), which checks every fence individually - so it is
# excluded from the order comparison rather than pinned to a place it does not have.
ORDER_EXEMPT = {"line by line"}

PART_FRONTMATTER_KEYS = ["day", "part", "title", "ids", "level", "prerequisites", "prev", "next"]

# A paper document carries a part's frontmatter minus `part` - it has no section number, because
# it is not a subtopic of anything - and plus `paper`, the one identifier it teaches.
PAPER_FRONTMATTER_KEYS = ["day", "paper", "title", "ids", "level", "prerequisites", "prev", "next"]

# A citation is an identifier, never a person (plan §18.1 rule 5). Two forms are accepted: an arXiv
# ID - `arXiv:YYMM.NNNNN` post-2007, or the pre-2007 archive form `arXiv:cs/0701001` - and a DOI,
# written with its `doi:` prefix so it can be found in prose without guessing where it ends.
PAPER_ID_RE = re.compile(
    r"arXiv:\d{4}\.\d{4,5}(?:v\d+)?"
    r"|arXiv:[a-z-]+(?:\.[A-Z]{2})?/\d{7}"
    r"|doi:10\.\d{4,9}/[^\s)\]|,;\"'`>*<]+",
    re.I,
)

# Anything shaped like a citation. A malformed identifier simply would not match PAPER_ID_RE, so it
# would never be checked at all - this catches it and says so (§17.4.1 rule 5, never invent one).
PAPER_ID_LOOSE_RE = re.compile(r"(?:arxiv|doi)\s*:\s*\S+", re.I)

PAPERS_LEDGER = ROOT / "docs" / "PAPERS.md"

# Principle 18: every part declares where it leaves the reader.
LEVELS = {"foundation", "working", "production"}

# Principle 17: a day is a unit of subject, not a unit of time. Nothing in a day folder may suggest
# a duration or a pace - not "takes 20 minutes", not the v1 "estimated hours" field, not a pace.
TIME_BANS = [
    (
        re.compile(
            r"^\s*(reading_minutes|duration|time_estimate|minutes|est_time|estimated_hours"
            r"|estimated hours)\s*:",
            re.I | re.M,
        ),
        "a duration field in frontmatter",
    ),
    (
        re.compile(r"\b\d+\s*[-–]?\s*\d*\s*(minutes?|mins?|hours?|hrs?)\b(?!\s*(of |the ))", re.I),
        "a time estimate in the prose",
    ),
    (re.compile(r"\*\*(Time|Estimated hours):?\*\*", re.I), "a **Time:** line"),
    (re.compile(r"should take (about |around |roughly )?\w+", re.I), "a 'should take ...' pace"),
]

HUB_FRONTMATTER_KEYS = [
    "day",
    "phase",
    "phase_name",
    "title",
    "ids",
    "principles",
    "kind",
    "plan_version",
    "parts",
    "generated",
    "status",
    "lab_scaffolded",
    "commit",
]

# The eleven numbered hub sections (plan §17.5). Frontmatter and the yesterday/today/tomorrow
# blockquote are checked separately.
HUB_SECTIONS = [
    (1, "Where we are"),
    (2, "The map"),
    (3, "Setup"),
    (4, "Build brief"),
    (5, "The eval"),
    (6, "Request budget"),
    (7, "Traps"),
    (8, "Verify before you code"),
    (9, "Say it in an interview"),
    (10, "Done when"),
    (11, "Ledger & commit"),
]

# Fences whose contents are output, a diagram or a config dump - they need no walkthrough.
NO_WALKTHROUGH_LANGS = {"", "text", "console", "traceback", "mermaid", "json", "toml", "yaml"}

# Headings under which a code block is evidence, not teaching, so no walkthrough is required.
EXEMPT_HEADINGS = re.compile(
    r"when it breaks|check yourself|verify|request budget|ledger|the map", re.I
)

PLAN_VERSION = "v2.2.1"


@dataclass
class Report:
    day: int
    failures: list[str] = field(default_factory=list)
    parts: int = 0
    papers: int = 0

    @property
    def ok(self) -> bool:
        return not self.failures

    def fail(self, where: str, message: str) -> None:
        self.failures.append(f"{where}: {message}")


def frontmatter(text: str) -> dict[str, str] | None:
    """Return the YAML-ish frontmatter as a flat dict, or None when there is none."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    out: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def paper_ids(value: str) -> list[str]:
    """Every well-formed paper identifier in a string, in the order it appears.

    Used on a `papers:`/`paper:` frontmatter value and on a whole document alike - the frontmatter
    parser keeps values as raw strings, so `papers: ["arXiv:1706.03762"]` arrives here as its own
    source text and the regex is what turns it into a list.
    """
    return [m.group(0) for m in PAPER_ID_RE.finditer(value)]


def malformed_paper_ids(text: str) -> list[str]:
    """Citation-shaped strings that are not valid identifiers - what a shape check alone misses."""
    out = []
    for loose in PAPER_ID_LOOSE_RE.finditer(text):
        found = loose.group(0)
        if not PAPER_ID_RE.match(found):
            out.append(found.rstrip(".,;:)]"))
    return out


@cache
def ledger_ids() -> frozenset[str]:
    """Every identifier with a row in docs/PAPERS.md, lowercased for comparison.

    Cached because every part in every day asks the same question, and the ledger does not change
    while the check runs.
    """
    if not PAPERS_LEDGER.is_file():
        return frozenset()
    text = PAPERS_LEDGER.read_text(encoding="utf-8")
    rows = [line for line in text.splitlines() if line.lstrip().startswith("|")]
    return frozenset(i.lower() for row in rows for i in paper_ids(row))


@cache
def paper_parts() -> dict[str, list[str]]:
    """identifier -> the paper documents teaching it, as paths relative to days/.

    A paper is taught once in the whole curriculum (plan §17.4.2), so a key with two values is a
    failure, not a list. Scanning every day - not just the one being checked - is deliberate: a
    Day 66 part may cite a paper taught on Day 2, and that citation must still resolve.
    """
    out: dict[str, list[str]] = {}
    for path in sorted(DAYS.glob("day-*/papers/*.md")):
        meta = frontmatter(path.read_text(encoding="utf-8"))
        for identifier in paper_ids(meta.get("paper", "") if meta else ""):
            rel = str(path.relative_to(DAYS)).replace("\\", "/")
            out.setdefault(identifier.lower(), []).append(rel)
    return out


def body(text: str) -> str:
    """The document with its frontmatter removed, so heading checks cannot match inside it."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :]
    return text


def find_day(number: int) -> Path | None:
    """The folder for a day, whatever slug follows its number (plan §17.2).

    The number is the identity, so `day-01`, `day-1` and `day-01-bootstrap-and-map` all resolve to
    day 1 and a folder may be renamed to a better slug without breaking anything that reads it.
    """
    exact = [DAYS / f"day-{number:02d}", DAYS / f"day-{number}"]
    slugged = sorted(p for p in DAYS.glob(f"day-{number:02d}-*") if p.is_dir())
    return next((p for p in [*slugged, *exact] if p.is_dir()), None)


def unexplained_code_blocks(text: str) -> list[int]:
    """Line numbers of code fences that no 'Line by line' walkthrough follows.

    Walks the document once, tracking the current heading. A fence is exempt when its language
    carries no logic (plain output, a diagram, a config dump) or when it sits under a heading whose
    job is showing evidence rather than teaching.
    """
    lines = text.splitlines()
    offenders: list[int] = []
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line
            i += 1
            continue
        fence = re.match(r"^(`{3,})(\w*)\s*$", line)
        if not fence:
            i += 1
            continue

        # A fence may be longer than three backticks so it can contain a shorter one - which is how
        # a lesson shows the contents of a Markdown file. The closing fence must be at least as long
        # as the opening one, so a nested block cannot end the outer one.
        ticks = len(fence.group(1))
        closing = re.compile(rf"^`{{{ticks},}}\s*$")
        lang = fence.group(2).lower()
        start = i
        i += 1
        while i < len(lines) and not closing.match(lines[i]):
            i += 1
        i += 1  # step over the closing fence

        if lang in NO_WALKTHROUGH_LANGS or EXEMPT_HEADINGS.search(heading):
            continue

        # Look ahead for a walkthrough before the next fence or the next heading of the same rank.
        j = i
        explained = False
        while j < len(lines):
            nxt = lines[j]
            if re.search(r"line by line", nxt, re.I):
                explained = True
                break
            if re.match(r"^`{3,}\w", nxt) or nxt.startswith("## "):
                break
            j += 1
        if not explained:
            offenders.append(start + 1)
    return offenders


def has_explainable_code(text: str) -> bool:
    """True when the body holds at least one fence that the contract expects a walkthrough for.

    Mirrors the exemptions in unexplained_code_blocks: a language that carries no logic (plain
    output, a diagram, a config dump) does not need explaining, and neither does a fence under a
    heading whose job is showing evidence rather than teaching.
    """
    lines = text.splitlines()
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line
            i += 1
            continue
        fence = re.match(r"^(`{3,})(\w*)\s*$", line)
        if not fence:
            i += 1
            continue
        ticks = len(fence.group(1))
        closing = re.compile(rf"^`{{{ticks},}}\s*$")
        lang = fence.group(2).lower()
        i += 1
        while i < len(lines) and not closing.match(lines[i]):
            i += 1
        i += 1
        if lang not in NO_WALKTHROUGH_LANGS and not EXEMPT_HEADINGS.search(heading):
            return True
    return False


def check_no_clocks(text: str, where: str, report: Report) -> None:
    """Principle 17: no time estimates anywhere in a day folder.

    Content is never trimmed to fit a schedule, so no document may imply one. Code fences are
    stripped first - a real command may legitimately mention a timeout.
    """
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    for pattern, description in TIME_BANS:
        hit = pattern.search(prose)
        if hit:
            snippet = hit.group(0).strip().replace("\n", " ")
            report.fail(where, f"{description} ({snippet!r}) - a day has no clock (Principle 17)")


def check_part(path: Path, day: int, report: Report) -> tuple[int, int] | None:
    """Validate one parts/<NN>/ document. Returns its (section, subtopic) numbers."""
    where = f"parts/{path.parent.name}/{path.name}"
    match = PART_NAME_RE.match(path.name)
    if not match:
        report.fail(where, "filename must be <section>.<subtopic>-<kebab-slug>.md")
        return None
    section, subtopic = int(match.group(1)), int(match.group(2))

    folder = path.parent.name
    folder_match = SECTION_DIR_RE.match(folder)
    if folder_match and int(folder_match.group(1)) != section:
        report.fail(
            where,
            f"lives in parts/{folder}/ but its number says section {section} - "
            f"it belongs in parts/{section:02d}-<slug>/",
        )

    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail(where, "no YAML frontmatter")
    else:
        missing = [k for k in PART_FRONTMATTER_KEYS if k not in meta]
        if missing:
            report.fail(where, f"frontmatter missing {', '.join(missing)}")
        if meta.get("day") not in {str(day), f'"{day}"'}:
            report.fail(where, f"frontmatter day is {meta.get('day')!r}, expected {day}")
        if meta.get("part", "").strip('"') != f"{section}.{subtopic}":
            report.fail(where, f"frontmatter part should be {section}.{subtopic}")
        level = meta.get("level", "").strip('"').lower()
        if level and level not in LEVELS:
            report.fail(where, f"level is {level!r}, must be one of {sorted(LEVELS)}")

    content = body(text)
    check_sections(content, meta or {}, where, report)

    for line_no in unexplained_code_blocks(content):
        report.fail(where, f"code block at line {line_no} has no 'Line by line' walkthrough")

    check_papers(path, text, meta or {}, content, where, report)
    check_no_clocks(text, where, report)
    return section, subtopic


def check_sections(content: str, meta: dict[str, str], where: str, report: Report) -> None:
    """The twelve required sections, present when they apply and in contract order (plan §17.4).

    Shared by parts and papers: a paper document is written to the same contract, so the check that
    enforces it should be the same code rather than a second copy that can drift.
    """
    seen_at: list[int] = []
    ordered = 0
    for name, pattern in PART_SECTIONS:
        applies = CONDITIONAL_SECTIONS.get(name)
        if applies is not None and not applies(content, meta):
            continue  # its trigger is absent, so asking for it would be empty ceremony
        if name not in ORDER_EXEMPT:
            ordered += 1
        found = pattern.search(content)
        if not found:
            report.fail(where, f"missing required section: {name}")
        elif name not in ORDER_EXEMPT:
            seen_at.append(found.start())
    if len(seen_at) == ordered and seen_at != sorted(seen_at):
        report.fail(where, "required sections are out of contract order (plan §17.4)")


def check_papers(
    path: Path, text: str, meta: dict[str, str], content: str, where: str, report: Report
) -> None:
    """The §17.4 row 6 and §17.4.2 rules: a citation is declared, resolvable and verified.

    Four separate promises, and the failures are kept separate because they mean different things:
    a missing ledger row is an unverified citation (Principle 7), while a citation that resolves to
    no paper part is a reader sent to an address with nothing at it (the no-shortcut test).
    """
    cited = paper_ids(meta.get("papers", ""))
    taught = paper_ids(meta.get("paper", ""))

    # Row 6 and the `papers` key are required exactly when the other is present.
    has_section = any(
        name == "the paper behind it" and pattern.search(content) for name, pattern in PART_SECTIONS
    )
    if cited and not has_section:
        report.fail(where, "declares papers: but carries no 'The paper behind it' section (§17.4)")
    if has_section and not cited:
        report.fail(where, "carries 'The paper behind it' but declares no papers: (§17.4)")

    # A paper part teaches exactly one paper, and every paper is taught exactly once (§17.4.2).
    if len(taught) > 1:
        report.fail(where, f"paper: declares {len(taught)} identifiers - a paper part teaches one")
    for identifier in taught:
        others = [p for p in paper_parts().get(identifier.lower(), []) if not path.match(f"*{p}")]
        if others:
            report.fail(
                where,
                f"{identifier} is already taught in {others[0]} - a paper is taught once (§17.4.2)",
            )

    # Every citation resolves to the paper part teaching it, and the section links that part.
    for identifier in cited:
        teachers = paper_parts().get(identifier.lower(), [])
        if not teachers:
            report.fail(where, f"cites {identifier} but no paper part teaches it (§17.4.2)")
        elif not any(Path(t).name in content for t in teachers):
            report.fail(where, f"cites {identifier} without linking {teachers[0]} (§17.4 row 6)")

    # Nothing is cited that was not verified against the record on the day it was written.
    known = ledger_ids()
    for identifier in {*cited, *taught, *paper_ids(content)}:
        if identifier.lower() not in known:
            report.fail(where, f"{identifier} has no row in docs/PAPERS.md (§17.4.1 rule 5)")

    for malformed in malformed_paper_ids(text):
        report.fail(where, f"{malformed!r} is not a valid arXiv ID or DOI (§17.4.1 rule 5)")


def check_paper(path: Path, day: int, report: Report) -> int | None:
    """Validate one papers/<NN>-<slug>.md document. Returns its reading-order number.

    A paper document is a part in every respect except its address (plan §17.4.2), so the section
    contract, the walkthrough rule and the no-clocks rule are the same checks the parts get.
    """
    where = f"papers/{path.name}"
    match = PAPER_NAME_RE.match(path.name)
    if not match:
        report.fail(where, "filename must be <NN>-<paper-slug>.md, two digits from 01")
        return None

    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail(where, "no YAML frontmatter")
    else:
        missing = [k for k in PAPER_FRONTMATTER_KEYS if k not in meta]
        if missing:
            report.fail(where, f"frontmatter missing {', '.join(missing)}")
        if "part" in meta:
            report.fail(where, "a paper carries no `part:` - it is not a subtopic of a section")
        if meta.get("day") not in {str(day), f'"{day}"'}:
            report.fail(where, f"frontmatter day is {meta.get('day')!r}, expected {day}")
        level = meta.get("level", "").strip('"').lower()
        if level and level not in LEVELS:
            report.fail(where, f"level is {level!r}, must be one of {sorted(LEVELS)}")

    content = body(text)
    check_sections(content, meta or {}, where, report)
    for line_no in unexplained_code_blocks(content):
        report.fail(where, f"code block at line {line_no} has no 'Line by line' walkthrough")
    check_papers(path, text, meta or {}, content, where, report)
    check_no_clocks(text, where, report)
    return int(match.group(1))


def check_paper_numbering(numbers: list[int], report: Report) -> None:
    """Papers are numbered from 01 upward with no gaps - the same rule the parts live under."""
    if not numbers:
        return
    expected = list(range(1, len(numbers) + 1))
    if sorted(numbers) != expected:
        report.fail("papers/", f"numbering is {sorted(numbers)}, expected {expected}")


def check_numbering(numbers: list[tuple[int, int]], report: Report) -> None:
    """Sections start at 1 and are contiguous; so are the subtopics inside each section."""
    if not numbers:
        return
    sections = sorted({s for s, _ in numbers})
    if sections[0] != 1:
        report.fail("parts/", f"section numbering starts at {sections[0]}, must start at 1")
    expected = list(range(1, len(sections) + 1))
    if sections != expected:
        report.fail("parts/", f"section numbering has a gap: {sections} (expected {expected})")
    for section in sections:
        subs = sorted(sub for s, sub in numbers if s == section)
        if subs != list(range(1, len(subs) + 1)):
            report.fail(
                "parts/", f"section {section} subtopics are {subs}, expected 1..{len(subs)}"
            )


def check_hub(folder: Path, part_count: int, report: Report) -> None:
    hub = folder / "LESSON.md"
    if not hub.is_file():
        report.fail("LESSON.md", "missing - every day needs a hub")
        return

    text = hub.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail("LESSON.md", "no YAML frontmatter")
    else:
        missing = [k for k in HUB_FRONTMATTER_KEYS if k not in meta]
        if missing:
            report.fail("LESSON.md", f"frontmatter missing {', '.join(missing)}")
        declared = meta.get("parts", "").strip('"')
        if declared.isdigit() and int(declared) != part_count:
            report.fail(
                "LESSON.md", f"frontmatter says parts: {declared}, parts/ holds {part_count}"
            )
        if meta.get("plan_version", "").strip('"') != PLAN_VERSION:
            report.fail("LESSON.md", f"plan_version must be {PLAN_VERSION}")

    content = body(text)
    for number, name in HUB_SECTIONS:
        if not re.search(rf"^##\s*§{number}\b", content, re.M):
            report.fail("LESSON.md", f"missing section §{number} ({name})")

    if not re.search(r"^>\s*\*\*Yesterday", content, re.M | re.I):
        report.fail("LESSON.md", "missing the yesterday / today / tomorrow blockquote")

    if re.search(r"line by line", content, re.I):
        report.fail("LESSON.md", "the hub must not teach - move the walkthrough into a part")

    check_no_clocks(text, "LESSON.md", report)

    linked = set(re.findall(r"parts/([\w.\-]+/[\w.\-]+\.md)", content))
    on_disk = {
        f"{d.name}/{f.name}"
        for d in (folder / "parts").iterdir()
        if d.is_dir()
        for f in d.glob("*.md")
    }
    for name in sorted(on_disk - linked):
        report.fail("LESSON.md", f"§2 map does not link parts/{name}")

    papers_dir = folder / "papers"
    if papers_dir.is_dir():
        linked_papers = set(re.findall(r"papers/([\w.\-]+\.md)", content))
        for name in sorted({f.name for f in papers_dir.glob("*.md")} - linked_papers):
            report.fail("LESSON.md", f"§2 map does not link papers/{name}")


def check_day(number: int) -> Report:
    report = Report(day=number)
    folder = find_day(number)
    if folder is None:
        report.fail("days/", f"no folder for day {number}")
        return report

    if not DAY_DIR_RE.match(folder.name):
        report.fail(
            f"days/{folder.name}/",
            "a day folder is day-NN then a kebab-case slug saying what it teaches, "
            "e.g. days/day-01-bootstrap-and-map/ (plan §17.2)",
        )

    parts_dir = folder / "parts"
    if not parts_dir.is_dir():
        report.fail("parts/", "missing - a day with no parts/ is not written (plan §17.2)")
        return report

    for stray in sorted(parts_dir.glob("*.md")):
        report.fail(
            f"parts/{stray.name}",
            "loose in parts/ - every part lives in its section folder, e.g. parts/01/",
        )

    for entry in sorted(parts_dir.iterdir()):
        if entry.is_dir() and not SECTION_DIR_RE.match(entry.name):
            report.fail(
                f"parts/{entry.name}/",
                "a section folder is the section number zero-padded to two digits, then a "
                "kebab-case slug saying what the section is about, e.g. parts/02-repo-skeleton/",
            )

    files = sorted(
        (f for d in parts_dir.iterdir() if d.is_dir() for f in d.glob("*.md")),
        key=lambda f: (f.parent.name, f.name),
    )
    if not files:
        report.fail("parts/", "empty - no section folders holding part documents")
        return report

    report.parts = len(files)
    numbers = [n for f in files if (n := check_part(f, number, report)) is not None]
    check_numbering(numbers, report)

    # papers/ is optional - most days teach a tool, a command or a convention and have no
    # literature behind them (plan §17.4.2). When it exists it is checked like parts/.
    papers_dir = folder / "papers"
    papers = sorted(papers_dir.glob("*.md")) if papers_dir.is_dir() else []
    report.papers = len(papers)
    check_paper_numbering(
        [n for f in papers if (n := check_paper(f, number, report)) is not None], report
    )

    check_hub(folder, len(files), report)

    if not (folder / "CHECKLIST.md").is_file():
        report.fail("CHECKLIST.md", "missing")
    else:
        check_no_clocks(
            (folder / "CHECKLIST.md").read_text(encoding="utf-8"), "CHECKLIST.md", report
        )
    return report


def written_days() -> list[int]:
    """Every day that has attempted the hub + parts/ shape, so an unwritten day is not a failure."""
    found: list[int] = []
    for folder in sorted(DAYS.glob("day-*")):
        if not (folder / "parts").is_dir():
            continue
        digits = re.search(r"day-(\d+)", folder.name)
        if digits:
            found.append(int(digits.group(1)))
    return sorted(found)


def main(argv: list[str]) -> int:
    requested = [int(a) for a in argv if a.isdigit()]
    days = requested or written_days()
    if not days:
        print("no day has a parts/ directory yet - nothing to check")
        return 0

    reports = [check_day(d) for d in days]
    failed = [r for r in reports if not r.ok]

    for report in reports:
        if report.ok:
            papers = f" + {report.papers} papers" if report.papers else ""
            print(f"OK   day {report.day:>3}  {report.parts} parts{papers}")
        else:
            print(f"FAIL day {report.day:>3}  {len(report.failures)} problems")
            for failure in report.failures:
                print(f"       - {failure}")

    print()
    if failed:
        print(f"depth contract: {len(reports) - len(failed)}/{len(reports)} days pass")
        return 1
    print(f"depth contract: all {len(reports)} checked days pass")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
