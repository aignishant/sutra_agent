"""Day 2 — LLM mechanics probes: tokens, statelessness, sampling.

Importable without side effects. Run demos with:
    python -m sutra.mechanics ask        # first call: one prompt, one answer
    python -m sutra.mechanics tokens     # see the meter: counts + usage bill
    python -m sutra.mechanics memory     # see the amnesia: history vs none
    python -m sutra.mechanics sampling   # see the dial: temp 0.0 vs 1.5
    python -m sutra.mechanics capped     # failure lab: the thinking tax
"""
from __future__ import annotations

import re                                  # to read the delay out of 429 text
import sys                                 # for the command-line demo picker
import time                                # to actually wait between retries

from google import genai                   # the raw Gemini SDK (Day 2 install)
from google.genai import errors, types     # error classes + request types

from sutra.config import load_env          # our ten-line .env loader (step 3)

# Free-tier pin — repinned 2026-08-13: gemini-2.5-flash returns 404 for new
# accounts ("no longer available to new users"); gemini-3.5-flash verified
# working on this project's key. See CHANGELOG_PLAN.md.
MODEL = "gemini-3.5-flash"
MAX_TRIES = 4                              # after 4 tries: give up HONESTLY

# 429 messages state the server's own delay, e.g. "Please retry in 36.5s."
_RETRY_IN = re.compile(r"retry in ([\d.]+)s", re.IGNORECASE)


def _retry_wait(e: errors.APIError, attempt: int) -> float:
    """The server's stated retry delay when present, else exponential backoff.

    Example:
        a 429 saying "Please retry in 36.5s"  -> returns 37.5 (their delay + 1)
        a 429 with no stated delay, attempt 2 -> returns 4.0  (2 ** 2)
    """
    if e.message and (m := _RETRY_IN.search(e.message)):
        return float(m.group(1)) + 1.0     # trust the server; +1s of margin
    return float(2**attempt)               # fallback: 1, 2, 4, 8 seconds


def ask(
    client: genai.Client,
    contents: object,
    config: types.GenerateContentConfig | None = None,
) -> types.GenerateContentResponse:
    """generate_content with honest 429 handling: back off, then surface.

    This wrapper is the ONLY door Sutra uses to call the model — so 429
    honesty protects every future day (the loop on Day 3 imports it).

    Args:
        client: an authenticated genai.Client.
        contents: a prompt string, or a list of types.Content (history).
        config: optional GenerateContentConfig (temperature, system, tools…).

    Returns:
        The full response object (text, usage metadata, candidates…).

    Example:
        >>> load_env()
        >>> client = genai.Client()
        >>> ask(client, "Say hi in three words.").text
        'Hi there, friend!'
    """
    for attempt in range(MAX_TRIES):
        try:
            return client.models.generate_content(
                model=MODEL, contents=contents, config=config
            )
        except errors.APIError as e:
            # Anything that is NOT a quota hit — or our LAST allowed try —
            # gets re-raised: never swallow errors (Principle 10).
            if e.code != 429 or attempt == MAX_TRIES - 1:
                raise
            wait = _retry_wait(e, attempt)             # how long to pause
            print(f"429: quota hit — waiting {wait:.0f}s, attempt {attempt + 1}/{MAX_TRIES}")
            time.sleep(wait)                           # actually wait it out
    raise AssertionError("unreachable")                # loop always returns/raises


def demo_ask(client: genai.Client) -> None:
    """The first call: one prompt in, one message out.

    Usage:  python -m sutra.mechanics ask     (1 model call)
    """
    response = ask(client, "In one sentence: what is a support-ticket triage desk?")
    print(response.text)                       # Sutra's first words


def demo_tokens(client: genai.Client) -> None:
    """Count tokens before a call; read the real bill after it.

    Usage:  python -m sutra.mechanics tokens  (1 model call + 1 free count)
    """
    prompt = "Why is the sky blue? Answer in one sentence."
    print("count_tokens before the call:")     # the "how big is this?" check
    print(" ", client.models.count_tokens(model=MODEL, contents=prompt))
    response = ask(client, prompt)
    print("model said:", response.text)
    print("usage metadata (the actual bill):")  # note thoughts_token_count!
    print(" ", response.usage_metadata)


def demo_memory(client: genai.Client) -> None:
    """Prove statelessness: no history → amnesia; history → recall.

    Usage:  python -m sutra.mechanics memory  (3 model calls)
    """
    setup = "My favorite color is teal. Reply with just: OK."
    first = ask(client, setup)                 # meeting 1: tell it a fact
    print("call 1:", first.text)

    second = ask(client, "What is my favorite color?")   # meeting 2: NO notes
    print("call 2, NO history:", second.text)  # it cannot know — desk was wiped

    history = [                                # meeting 3: bring the dossier —
        types.Content(role="user", parts=[types.Part(text=setup)]),        # what we said
        types.Content(role="model", parts=[types.Part(text=first.text or "OK.")]),  # what it said
        types.Content(role="user", parts=[types.Part(text="What is my favorite color?")]),  # new question
    ]
    third = ask(client, history)               # re-reads everything, fresh
    print("call 3, WITH history:", third.text)  # now it "remembers": teal


def demo_sampling(client: genai.Client) -> None:
    """Same prompt, two temperatures, three runs each.

    Usage:  python -m sutra.mechanics sampling  (6 model calls — mind the RPM!)
    """
    prompt = "Name a color. Reply with one word only."
    for temperature in (0.0, 1.5):             # boring dice, then wild dice
        answers = [
            (ask(client, prompt, types.GenerateContentConfig(temperature=temperature)).text or "").strip()
            for _ in range(3)                  # three rolls at each setting
        ]
        print(f"temperature={temperature}: {answers}")


def demo_capped(client: genai.Client) -> None:
    """Failure lab: a tiny max_output_tokens meets a thinking model.

    Usage:  python -m sutra.mechanics capped  (1 model call; read doc §5 first)
    """
    response = ask(
        client,
        "Explain why the sky is blue.",
        types.GenerateContentConfig(max_output_tokens=16),   # a hard 16-token wall
    )
    print("text:", repr(response.text))        # likely None — thoughts ate it
    print("usage metadata:", response.usage_metadata)        # the receipt


def main() -> None:
    """Tiny demo dispatcher: `python -m sutra.mechanics <name>`."""
    demos = {
        "ask": demo_ask,
        "tokens": demo_tokens,
        "memory": demo_memory,
        "sampling": demo_sampling,
        "capped": demo_capped,
    }
    name = sys.argv[1] if len(sys.argv) > 1 else "ask"
    if name not in demos:                      # unknown name -> print usage
        print(f"usage: python -m sutra.mechanics [{'|'.join(demos)}]")
        raise SystemExit(2)
    load_env()                                 # keys from .env, never from code
    demos[name](genai.Client())                # build a client, run the demo


if __name__ == "__main__":                     # run as a script, not on import
    main()
