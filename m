#!/usr/bin/env bash
# Project Sutra daily driver. Replaces `make` (which is not installed on Windows).
# Written on Day 0; every later day assumes it. See days/day-00/parts/03/.
set -euo pipefail

DAY="${2:-}"
pad() { printf "%02d" "$1"; }

# A day folder is days/day-NN-<slug>/ (plan §17.2). The number is the identity and the slug is a
# label on it, so resolve by number and accept whatever slug follows - that is what lets a folder be
# renamed to a better slug without breaking any of this.
daydir() {
  local n d
  n="$1"
  for d in "days/day-$(pad "$n")-"*; do
    [ -d "$d" ] && { echo "$d"; return; }
  done
  if [ -d "days/day-$(pad "$n")" ]; then echo "days/day-$(pad "$n")"
  elif [ -d "days/day-$n" ]; then echo "days/day-$n"
  else echo ""; fi
}

case "${1:-help}" in
  start)
    [ -z "$DAY" ] && { echo "usage: ./m start <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no day $DAY yet - see docs/TRACKER.md for what is written"; exit 1; }
    if [ -f "$D/LESSON.md" ] && [ -d "$D/parts" ]; then
      echo "-> open $D/LESSON.md   (the hub - read its §2 map, then the parts in order)"
      find "$D/parts" -name '*.md' | sort | sed "s|^$D/|     |"
    else
      echo "day $DAY has no hub + parts/ - it is not written (plan §17.2)"; exit 1
    fi
    ;;

  parts)
    [ -z "$DAY" ] && { echo "usage: ./m parts <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -d "$D/parts" ] || { echo "day $DAY has no parts/ - not written (plan §17.2)"; exit 1; }
    find "$D/parts" -name '*.md' | sort | sed "s|^$D/parts/||"
    ;;

  depth)
    if [ -n "$DAY" ]; then uv run python scripts/depth_check.py "$DAY"
    else uv run python scripts/depth_check.py; fi
    ;;

  scaffold)
    [ -z "$DAY" ] && { echo "usage: ./m scaffold <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no day $DAY yet - the day is written before its lab"; exit 1; }
    mkdir -p "$D/lab"
    echo "-> created $D/lab"
    ;;

  trace)
    uv run python scripts/trace.py
    ;;

  tracker)
    uv run python scripts/tracker.py
    ;;

  status)
    uv run python scripts/tracker.py --summary
    ;;

  check)
    uv run ruff check .
    uv run ruff format --check .
    # pytest exits 5 for "no tests collected". Before Day 23 there are none, and an empty suite
    # is not a failure - so 0 and 5 pass and everything else stops the gate.
    uv run python -m pytest -q -m "not live" || [ $? -eq 5 ]
    uv run python scripts/depth_check.py
    uv run python scripts/trace.py
    echo "OK all green"
    ;;

  done)
    [ -z "$DAY" ] && { echo "usage: ./m done <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no day folder for $DAY"; exit 1; }
    C="$D/CHECKLIST.md"
    [ -f "$C" ] || { echo "FAIL no $C"; exit 1; }
    if grep -q '^- \[ \]' "$C"; then
      echo "FAIL unticked boxes remain in $C"; grep -n '^- \[ \]' "$C"; exit 1
    fi
    "$0" check
    uv run python scripts/tracker.py
    git add -A && git commit -m "day-$(pad "$DAY"): complete"
    echo "OK day $DAY committed"
    ;;

  *)
    cat <<'USAGE'
usage: ./m <command> [day]

  status         one line: how many days are written / complete
  tracker        regenerate docs/TRACKER.md
  trace          regenerate docs/TRACEABILITY.md from the day hubs vs plan §14
  start N        point at day N's hub and list its parts/
  parts N        list day N's sub-topic documents
  depth [N]      check day N (or every written day) against plan §17, the depth contract
  scaffold N     create days/day-NN-<slug>/lab/
  check          ruff + ruff format + offline pytest + depth contract + traceability
  done N         refuse unless the checklist is ticked and checks are green, then commit
USAGE
    ;;
esac
