"""Environment loading for Sutra.

Configuration reaches this program through the environment, never through a committed file
(Day 1, part 3.2). `.env` is a laptop convenience that populates the environment; in a
container the platform does it and nothing here reads a file at all.

Stdlib only, by design: hand-roll the mechanism once, then the library is a convenience
rather than a mystery (Principle 4).

Usage:
    from sutra.config import load_env, require

    load_env()                       # laptop: copy .env into os.environ
    key = require("GOOGLE_API_KEY")  # raises ConfigError if absent or empty
"""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ConfigError(RuntimeError):
    """A required configuration value is missing or empty.

    Its own type so callers can catch exactly this, rather than every RuntimeError.
    """


def load_env(path: Path | None = None) -> None:
    """Copy KEY=value lines from .env into os.environ, without overwriting.

    Real environment variables always win: in CI and in production the platform sets them,
    and a stray .env must never override the platform.

    Args:
        path: an alternative .env location. Tests pass one; nothing else should.

    Example:
        >>> load_env()
        >>> "GOOGLE_API_KEY" in os.environ
        True
    """
    env_file = path if path is not None else ROOT / ".env"
    if not env_file.exists():
        return  # no .env is normal in production - the platform already set the environment

    for raw in env_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def require(name: str) -> str:
    """Return an environment variable, or raise ConfigError naming it.

    Example:
        >>> require("PATH")            # doctest: +ELLIPSIS
        '...'
        >>> require("NOPE_NOT_SET")
        Traceback (most recent call last):
        sutra.config.ConfigError: NOPE_NOT_SET is not set. Add it to .env (see .env.example).
    """
    value = os.environ.get(name, "").strip()
    if not value:
        raise ConfigError(f"{name} is not set. Add it to .env (see .env.example).")
    return value


def describe(name: str) -> str:
    """Report a variable's presence and length. NEVER its value.

    Example:
        >>> describe("NOPE_NOT_SET")
        'NOPE_NOT_SET: MISSING'
    """
    value = os.environ.get(name, "")
    return f"{name}: set ({len(value)} chars)" if value else f"{name}: MISSING"


# sutra/config.py - one more function, beside load_env and require
def require_free_tier() -> None:
    """Fail loudly if this process would talk to a billing-account backend.

    Principle 15: never write code that requires a billing account. A real
    environment variable beats .env (load_env uses setdefault), so the intent
    written in .env is not enough on its own - it has to be checked.
    """
    if os.environ.get("GOOGLE_GENAI_USE_VERTEXAI", "FALSE").upper() != "FALSE":
        raise ConfigError(
            "GOOGLE_GENAI_USE_VERTEXAI is "
            f"{os.environ['GOOGLE_GENAI_USE_VERTEXAI']!r} - Sutra is free-tier only "
            "(Addendum 02, Principle 15). Unset it in your shell, not just in .env."
        )
