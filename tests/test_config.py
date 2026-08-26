"""Day 1 — the first tests in this repository (OPS-02).

They pin three promises `sutra.config` makes: a missing variable fails loudly and names
itself, `describe()` never prints a secret, and a real environment variable always beats
a `.env` file.
"""

import os

import pytest

from sutra.config import ConfigError, describe, load_env, require


def test_require_raises_when_missing():
    """A missing variable must fail loudly, naming itself."""
    os.environ.pop("SUTRA_TEST_ABSENT", None)
    with pytest.raises(ConfigError, match="SUTRA_TEST_ABSENT"):
        require("SUTRA_TEST_ABSENT")


def test_describe_never_leaks_the_value():
    """describe() reports presence and length, never the secret itself."""
    os.environ["SUTRA_TEST_SECRET"] = "hunter2-not-a-real-key"
    out = describe("SUTRA_TEST_SECRET")
    assert "hunter2" not in out
    assert "22 chars" in out


def test_load_env_does_not_overwrite_the_real_environment(tmp_path):
    """A real environment variable always wins over .env.

    Why: in CI and in production the platform sets the environment, and a stray .env that
    survived a copy must never silently override it. `setdefault` is what buys this.
    """
    os.environ["SUTRA_TEST_WINS"] = "from-the-real-environment"
    env = tmp_path / ".env"
    env.write_text("SUTRA_TEST_WINS=from-the-file\n", encoding="utf-8")
    load_env(env)
    assert os.environ["SUTRA_TEST_WINS"] == "from-the-real-environment"


def test_require_rejects_a_whitespace_only_value():
    """A variable set to spaces is absent in every way that matters.

    This passes without changing config.py, because `require` calls `.strip()` before the
    emptiness test - so "   " becomes "" and takes the same branch as never-set.
    """
    os.environ["SUTRA_TEST_BLANK"] = "   "
    with pytest.raises(ConfigError, match="SUTRA_TEST_BLANK"):
        require("SUTRA_TEST_BLANK")
