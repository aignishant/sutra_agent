"""Day 2 — LLM mechanics probes: tokens, context, sampling.

Importable with no side effects. Run a demo with:
    uv run python -m sutra.mechanics ask
"""

from __future__ import annotations

import re
import time

from google import genai

# A private path, deliberately: as of google-genai 2.19.0 the errors raised by
# client.interactions.create live only here. google.genai.errors exports the LEGACY
# hierarchy, and issubclass(compat_errors.RateLimitError, errors.APIError) is False -
# catching the public name catches nothing. tests/test_mechanics.py pins this so an SDK
# move goes red on a laptop. See docs/adr/ADR-0007-interactions-error-hierarchy.md.
from google.genai._gaos.lib import compat_errors

from sutra.config import load_env

# Pinned explicitly, never an alias (see 1.3). Verified callable on this key
# 2026-08-24 against ai.google.dev/gemini-api/docs/models.
MODEL = "gemini-3.7-flash"
MAX_TRIES = 4

# The 429 states the server's own delay, in one of two spellings: the Interactions
# surface writes "Please retry in 52.3s", the legacy surface "'retryDelay': '47s'".
# Both verified 2026-08-25; see docs/adr/ADR-0007-interactions-error-hierarchy.md.
_RETRY_DELAY = re.compile(
    r"(?:retryDelay['\"]?\s*:\s*['\"]?|retry in )(\d+(?:\.\d+)?)s", re.IGNORECASE
)


def _retry_wait(error: compat_errors.APIError, attempt: int) -> float:
    """Seconds to wait: the server's stated delay if it gave one, else backoff.

    Example:
        a 429 saying "Please retry in 52.3s"  -> 53.3  (their number, plus margin)
        a 429 carrying "'retryDelay': '47s'"  -> 48.0  (the legacy surface's spelling)
        a 429 with no stated delay, attempt 2 -> 4.0   (the 2 ** attempt fallback)
    """
    match = _RETRY_DELAY.search(str(error))
    if match:
        return float(match.group(1)) + 1.0
    return float(2**attempt)


def ask(
    client: genai.Client,
    prompt: object,
    *,
    tools: list[dict] | None = None,
    config: dict | None = None,
    store: bool = False,
) -> object:
    """The ONLY way Sutra calls a model: retry on 429, then fail honestly.

    Args:
        client: an authenticated genai.Client.
        prompt: a string, or a structured history list (see 3.2).
        tools: function declarations for this interaction (Day 4, 1.2). Tools are
            interaction-scoped, not client-scoped, so they must be passed on every call
            that needs them. Day 2's callers pass nothing and are untouched.
        config: generation settings — temperature, thinking_level (see 4.2).
        store: whether the provider persists this interaction (see 3.3).

    Raises:
        compat_errors.APIError: on any non-429 error, and on 429 after MAX_TRIES.
    """
    for attempt in range(MAX_TRIES):
        try:
            return client.interactions.create(
                model=MODEL,
                input=prompt,
                tools=tools,
                generation_config=config,
                store=store,
            )
        except compat_errors.APIError as error:
            if error.status_code != 429 or attempt == MAX_TRIES - 1:
                raise
            wait = _retry_wait(error, attempt)
            print(f"429: quota hit — waiting {wait:.0f}s (attempt {attempt + 1}/{MAX_TRIES})")
            time.sleep(wait)
    raise AssertionError("unreachable: the loop always returns or raises")


def demo_ask(client: genai.Client) -> None:
    """One prompt in, one answer out — plus the receipt nobody reads."""
    interaction = ask(client, "Write a haiku about the color blue.", config={"temperature": 0.7})
    print("text :", interaction.output_text)
    print("usage:", interaction.usage)


def demo_tokens(client: genai.Client) -> None:
    """Estimate first, then measure — and compare the two.

    Usage:  uv run python -m sutra.mechanics tokens     (1 model call)
    """
    prompt = "Why is the sky blue? Answer in one sentence."

    print(f"estimate before the call : ~{len(prompt) // 4} input tokens")

    interaction = ask(client, prompt)
    usage = interaction.usage

    print(f"model said               : {interaction.output_text}")
    print(f"input tokens (measured)  : {usage.total_input_tokens}")
    print(f"output tokens (visible)  : {usage.total_output_tokens}")
    print(f"thought tokens (unseen)  : {usage.total_thought_tokens}")
    print(f"total tokens (the bill)  : {usage.total_tokens}")


def demo_thinking(client: genai.Client) -> None:
    """Same question, two thinking levels — watch the hidden half move.

    Usage:  uv run python -m sutra.mechanics thinking     (2 model calls)
    """
    prompt = "A train leaves at 14:05 and arrives at 17:40. How long is the journey?"

    for level in ("low", "high"):
        interaction = ask(client, prompt, config={"thinking_level": level})
        usage = interaction.usage
        thought = usage.total_thought_tokens or 0
        visible = usage.total_output_tokens or 0
        print(
            f"thinking_level={level:>7} | "
            f"thought={thought:>4} visible={visible:>4} "
            f"| hidden share={thought / max(thought + visible, 1):.0%}"
        )
        print(f"    answer: {interaction.output_text}")


def demo_memory(client: genai.Client) -> None:
    """Three calls: tell a fact, ask without history, ask with history.

    Usage:  uv run python -m sutra.mechanics memory     (3 model calls)
    """
    setup = "My favourite colour is teal. Reply with just: OK."
    question = "What is my favourite colour?"

    first = ask(client, setup)
    print("call 1 (told it)      :", first.output_text)

    second = ask(client, question)
    print("call 2 (no history)   :", second.output_text)

    # The turn shape was read off the installed SDK, not guessed (Principle 8):
    #   uv run python -c "print(type(first).__mro__); print(first)"
    # and google/genai/_gaos/types/interactions/{userinputstep,modeloutputstep,textcontent}.py
    # in google-genai 2.19.0 - a step is {"type": ..., "content": [text blocks]}.
    history = [
        {"type": "user_input", "content": [{"type": "text", "text": setup}]},
        # The model's own turn. Without it the list reads as two consecutive user
        # messages with the answer missing - the "forgotten append" of 3.2.
        {"type": "model_output", "content": [{"type": "text", "text": first.output_text or ""}]},
        {"type": "user_input", "content": [{"type": "text", "text": question}]},
    ]

    third = ask(client, history)
    print("call 3 (with history) :", third.output_text)


def demo_server_state(client: genai.Client) -> None:
    """The provider holds the conversation — the arrangement Sutra declines.

    Usage:  uv run python -m sutra.mechanics server     (2 model calls)
    """
    first = client.interactions.create(
        model=MODEL,
        input="My favourite colour is teal. Reply with just: OK.",
        store=True,
    )
    print("call 1:", first.output_text, "| id:", first.id)

    second = client.interactions.create(
        model=MODEL,
        input="What is my favourite colour?",
        previous_interaction_id=first.id,
        store=True,
    )
    print("call 2:", second.output_text)
    print("tokens sent on call 2:", second.usage.total_input_tokens)


def demo_sampling(client: genai.Client) -> None:
    """Same prompt, two temperatures, three runs each.

    Usage:  uv run python -m sutra.mechanics sampling     (6 model calls — mind the RPM)
    """
    prompt = "Invent a name for a new shade of blue paint. Two words, nothing else."

    for temperature in (0.0, 1.6):
        answers = []
        for _ in range(3):
            interaction = ask(
                client,
                prompt,
                config={"temperature": temperature, "thinking_level": "low"},
            )
            answers.append((interaction.output_text or "").strip())
        print(f"temperature={temperature}: {answers}")


def demo_capped(client: genai.Client) -> None:
    """Failure lab: a tiny max_output_tokens meets a thinking model.

    Usage:  uv run python -m sutra.mechanics capped     (3 model calls: two caps, then the fix)
    """
    prompt = "Explain why the sky is blue."

    for cap in (16, 400):
        interaction = ask(client, prompt, config={"max_output_tokens": cap})
        usage = interaction.usage
        print(f"--- max_output_tokens={cap} ---")
        print("  text          :", repr(interaction.output_text))
        print("  thought tokens:", usage.total_thought_tokens)
        print("  output tokens :", usage.total_output_tokens)

    # The right instrument: ask for brevity, and keep the cap as a runaway guard.
    interaction = ask(
        client,
        "Explain why the sky is blue. Answer in one short sentence.",
        config={"max_output_tokens": 400, "thinking_level": "low"},
    )
    print("  brief answer  :", interaction.output_text)


def main() -> None:
    """Run one named demo: uv run python -m sutra.mechanics <name>."""
    import sys

    demos = {
        "ask": demo_ask,
        "tokens": demo_tokens,
        "thinking": demo_thinking,
        "memory": demo_memory,
        "server": demo_server_state,
        "sampling": demo_sampling,
        "capped": demo_capped,
    }
    name = sys.argv[1] if len(sys.argv) > 1 else "ask"
    if name not in demos:
        print(f"usage: uv run python -m sutra.mechanics [{'|'.join(demos)}]")
        raise SystemExit(2)

    load_env()
    demos[name](genai.Client())


if __name__ == "__main__":
    main()
