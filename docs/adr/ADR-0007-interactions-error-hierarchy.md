# ADR-0007 — Catch the Interactions API's own error hierarchy, and parse the delay it actually sends

- **Date:** 2026-08-25
- **Day:** 2
- **Phase:** 1
- **Status:** accepted
- **Related:** ADR-0006 · plan §5.1 trap #4 · Addendum 02 §"429" · CHANGELOG_PLAN.md 2026-08-25 ·
  `days/day-02-llm-mechanics/parts/01-first-contact/1.5-the-only-door-429.md`

## Context

ADR-0006 moved Sutra's teaching surface to `client.interactions.create(...)`. Day 2's retry door in
part 1.5 was written against the error shapes the *legacy* `generate_content` surface raises —
`google.genai.errors.ClientError`, `.code`, and a body carrying `'retryDelay': '47s'`. Those shapes
are real; they are simply not the ones the Interactions surface produces.

Four facts, verified on **2026-08-25** against the pinned `google-genai==2.19.0` in this project's
own `.venv`, and against one live 429 from `gemini-3.7-flash`:

1. **The Interactions surface raises its own hierarchy.** `client.interactions.create(...)` errors
   come from `google.genai._gaos.lib.compat_errors`: `GeminiNextGenAPIClientError` → `APIError` →
   `APIStatusError` → `RateLimitError` (429), `AuthenticationError` (401), `BadRequestError` (400),
   `NotFoundError` (404), `InternalServerError`.
2. **It is not the legacy hierarchy, and not a subclass of it.**
   `issubclass(compat_errors.RateLimitError, google.genai.errors.APIError)` is `False`. A door
   written as `except errors.APIError` therefore catches **nothing** the Interactions surface throws.
   Reproduced with a fake client: the 429 escaped after **one** call, with zero retries.
3. **The status attribute is `.status_code`, not `.code`.** `hasattr(err, "code")` is `False` on the
   compat classes, so even a corrected `except` clause would have died on an `AttributeError` inside
   the handler.
4. **The 429 body does not contain a `retryDelay` field.** The live text is
   `Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,
   limit: 20, model: gemini-3.7-flash` followed by **`Please retry in 52.320368558s.`** Against that
   string, part 1.5's regex does not match and `_retry_wait` returns **1.0 second** — the textbook
   1-2-4 backoff that the whole part exists to argue against.

Findings 1 and 2 are the serious ones: the day's central claim — *every model call goes through one
door that listens to the server* — was false against the SDK the day pins. Findings 3 and 4 are what
you meet next once the `except` clause starts firing.

Two things were checked and found **not** to be problems, and are recorded here so nobody re-opens
them: `gemini-3.7-flash` is callable on this key (a live call returned text before the quota ran
out), and `temperature` — absent from the typed `GenerationConfigParam` in 2.19.0 — still reaches
the wire, because `GenerationConfig` is declared `extra: "allow"` and round-trips the field.

## Options considered

- **Leave the day as written.** Rejected outright. Principle 11 says an eval must be able to go RED,
  and Principle 10 says errors surface; a door that silently fails to retry violates both while
  claiming the opposite in prose.
- **Catch `Exception` and duck-type the status** with `getattr(error, "status_code", None) or
  getattr(error, "code", None)`. Version-proof and provider-proof. Rejected: a bare `except
  Exception` in the one function every later day calls would swallow programming errors in the call
  itself, which is the exact failure part 1.5 warns about eight lines further down. Robustness bought
  by blindness is not robustness.
- **Catch both hierarchies as a tuple.** Cheap, and would cover a future day that calls the legacy
  surface through the same door. Rejected for now: nothing in Sutra calls `generate_content` — part
  6.1 parks it deliberately — so the second element would be handling a case that cannot occur.
  Day 9's multi-provider work is where a wider door earns its keep.
- **Catch the compat hierarchy's root, and pin the assumption with a test (chosen).**

## Decision

**Sutra's door catches the error hierarchy the Interactions API actually raises, and reads the delay
the server actually sends.**

- `ask` catches **`compat_errors.APIError`** — the root of the Interactions hierarchy — and branches
  on **`error.status_code`**.
- The import is `from google.genai._gaos.lib import compat_errors`. **This is a private path**, and
  that is stated in the code rather than hidden: the SDK exposes no public alias for these classes
  as of 2.19.0 (`google.genai.errors` exports only the legacy hierarchy).
- **The private path is pinned by a test.** `test_the_interactions_error_hierarchy_is_where_we_think`
  asserts the module imports, that `RateLimitError.status_code == 429`, and that it is *not* a
  subclass of the legacy `errors.APIError`. When the SDK moves this, a test goes red on a laptop
  instead of a 429 escaping unretried in production.
- **`_RETRY_DELAY` accepts both phrasings** — `retryDelay: '47s'` and `Please retry in 52.3s` — with
  the same capture and the same `+ 1.0` margin. The exponential fallback stays exactly where it was:
  last resort, not main path.
- **Part 1.5 is rewritten to teach this**, including the real 429 body verbatim in *When it breaks*,
  and the hub's §5, §7 and §8 follow it. The story, the argument and the structure are unchanged —
  only the shapes are corrected.

## Consequences

- **Day 2's eval count changes from four tests to six.** The two additions are the hierarchy pin
  above and a `_retry_wait` case for the live `retry in 52.320368558s` body. `CHECKLIST.md` and the
  hub's §5 are updated; `pytest -q -m "not live"` now reports **10 passed**, not 8.
- **One private import exists in `sutra/mechanics.py`,** and every later day inherits it. That is a
  known liability with a named tripwire, which is better than the alternative it replaces.
- **Day 72 (SEC-15, OPS-13) has more to build on than planned.** Jitter, shared retry budgets and
  cross-provider failover were already its subject; it now also owns the question of what a
  provider-neutral error taxonomy looks like, since Day 9 will meet three more of them.
- **Seven other parts still quote `google.genai.errors.ClientError` tracebacks, and they are left
  standing** — in 1.3, 1.4, 2.1, 3.1, 3.2, 3.3 and 4.2. Those are genuine error texts from the
  *legacy* surface, and what the Interactions surface prints for a 400 or a 404 has **not** been
  observed: the day's quota was spent proving the 429. They are therefore **claims, not
  observations**, exactly like the 429 was until it was tested. Part 1.5 now says so explicitly, and
  re-verifying them — one deliberate 400, one 404 — is an open item for the next day this key has
  quota. **Not fixing them today is a decision, not an oversight**: guessing at seven error texts
  would repeat the mistake this ADR exists to record.
- **Part 6.1 gains accidental value.** The two hierarchies sitting side by side — legacy
  `ClientError` against Interactions `RateLimitError` — is the clearest possible argument for why
  the parked part exists at all.
- **A risk we are accepting:** `_gaos` is private and may be renamed in any release. The pinning test
  is the mitigation, not a guarantee.
- **Principle 8 is reaffirmed in its strongest form.** Every shape in this ADR was read off the
  installed package or a live response. A documentation page would not have surfaced any of it,
  because the docs describe the API and this is a fact about the client library.

## What would make us change our minds

- **The SDK publishes these classes on a public path** (`google.genai.errors`, or an
  `interactions.errors` module) — then the private import goes away and the pinning test relaxes to
  a one-line import check.
- **The compat layer is retired and Interactions raises `google.genai.errors.ClientError`** — then
  the day reverts to what it originally said, and the pinning test is what tells us.
- **A second provider's 429 arrives with a third phrasing** (Day 9 will find out) — then delay
  parsing moves out of a regex and into a small per-provider function, which is Day 72's territory.
- **The free tier stops stating a delay at all**, which would promote the exponential fallback from
  last resort to main path and change what this part teaches.

## Cold read

*(Re-read this a day later, with your reviewer hat on. Sign here.)*
Reviewed on YYYY-MM-DD — still stands / amended because ______
