"""Day 2 — the retry door, tested offline (AG-02).

Not one model call: `_retry_wait` is a pure function, and `ask`'s honesty is provable with a
fake client. That is the whole reason the client is a parameter rather than a global.
"""

import httpx
import pytest
from google.genai import errors
from google.genai._gaos.lib import compat_errors

from sutra.mechanics import _retry_wait, ask


class FakeError(Exception):
    """Stands in for an APIError carrying a server-stated delay."""

    def __init__(self, body: str) -> None:
        self.body = body

    def __str__(self) -> str:
        return self.body


def test_prefers_the_server_stated_delay() -> None:
    assert _retry_wait(FakeError("{'retryDelay': '47s'}"), 0) == 48.0


def test_falls_back_to_exponential_when_silent() -> None:
    assert _retry_wait(FakeError("no delay in this body"), 2) == 4.0


def test_decimal_delays_are_parsed() -> None:
    assert _retry_wait(FakeError("{'retryDelay': '36.5s'}"), 0) == 37.5


def test_reads_the_interactions_surfaces_own_phrasing() -> None:
    """The spelling this key actually sends, observed on a live 429 (ADR-0007).

    The Interactions surface states the delay as prose in the message rather than as a
    `retryDelay` field. Before this case existed, the parser missed it and every wait fell
    back to 1-2-4 seconds - the exact anti-pattern part 1.5 argues against.
    """
    assert _retry_wait(FakeError("Please retry in 52.320368558s."), 0) == 53.320368558


def test_the_interactions_error_hierarchy_is_where_we_think() -> None:
    """Pins the private import `ask` depends on, so an SDK move fails here first.

    `_gaos` is private and may be renamed in any release. When it is, this test goes red on
    a laptop - which is cheap - instead of a 429 escaping unretried in a running system.
    """
    assert compat_errors.RateLimitError.status_code == 429
    assert not issubclass(compat_errors.RateLimitError, errors.APIError)


class _RaisingInteractions:
    """The one method `ask` touches, wired to fail the way a bad key fails."""

    def __init__(self, error: Exception) -> None:
        self.error = error
        self.calls = 0

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        raise self.error


class FakeClient:
    """A client-shaped object. No key, no network, no quota."""

    def __init__(self, error: Exception) -> None:
        self.interactions = _RaisingInteractions(error)


def _status_error(status: int, message: str) -> compat_errors.APIError:
    """Build the error the Interactions surface would raise for `status`."""
    request = httpx.Request("POST", "https://generativelanguage.googleapis.com/v1/interactions")
    response = httpx.Response(status, request=request)
    return compat_errors.APIError.generate(status, None, message, response)


def test_ask_raises_on_a_non_429_instead_of_returning() -> None:
    """A 401 must surface, immediately and untouched (Principle 10, 1.x->2.x trap #4).

    Returning a placeholder string here is how a bad key becomes a mysterious quality
    problem three layers downstream. And a 401 must not be retried: it will be just as
    invalid next time, so `calls == 1` is as much of the promise as the raise.
    """
    client = FakeClient(_status_error(401, "API key not valid. Please pass a valid API key."))

    with pytest.raises(compat_errors.APIError, match="API key not valid"):
        ask(client, "anything")

    assert client.interactions.calls == 1
