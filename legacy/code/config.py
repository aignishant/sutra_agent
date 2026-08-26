"""Environment loading for Sutra.

Reads KEY=VALUE lines from the repo-root .env into os.environ. Real
environment variables win over .env values. Stdlib only, by design.

Usage:
    from sutra.config import load_env
    load_env()          # now os.environ has GOOGLE_API_KEY etc.
"""
from __future__ import annotations

import os                      # the environment we are loading INTO
from pathlib import Path       # clean path handling (house style)

ROOT = Path(__file__).resolve().parents[1]   # sutra/config.py -> repo root


def load_env(path: Path | None = None) -> None:
    """Load .env into os.environ without overwriting existing variables.

    Args:
        path: an alternative .env location (tests use this); default is
            the repo root's .env.

    Example:
        >>> load_env()
        >>> "GOOGLE_API_KEY" in os.environ
        True
    """
    env_file = path if path is not None else ROOT / ".env"
    if not env_file.exists():                # no .env? fine — maybe the real
        return                               # environment already has the keys
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()                  # ignore surrounding whitespace
        if not line or line.startswith("#") or "=" not in line:
            continue                         # skip blanks, comments, junk
        key, value = line.split("=", 1)      # split ONLY on the first '='
        # setdefault = "write only if absent": real env vars keep priority
        os.environ.setdefault(key.strip(), value.strip())
