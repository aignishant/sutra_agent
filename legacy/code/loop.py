"""Day 3 — the agent loop: think→act→observe, hand-rolled.

No framework, no native function calling (that arrives Day 4). The model
"acts" by writing a line this loop parses; the loop executes the tool and
reports back an OBSERVATION. Importable without side effects. Run demos:
    python -m sutra.loop triage     # the happy path: lookup -> KB -> answer
    python -m sutra.loop unknown    # a lookup that fails; honesty check
    python -m sutra.loop goldfish   # failure lab: act without observe (§5)
"""
from __future__ import annotations

import sys                                 # for the command-line demo picker

from google import genai                   # the raw Gemini SDK (Day 2)
from google.genai import types             # Content/Part — transcript pieces

from sutra.config import load_env          # .env loader (Day 2)
from sutra.mechanics import ask            # the 429-honest call wrapper (Day 2)

# Containment: at 5 RPM (observed Day 2), a runaway loop burns the day's
# quota fighting the minute's limit. The brake is not optional.
MAX_STEPS = 6

# Synthetic desk data — never real personal/employer data (Principle 9).
TICKETS = {
    "4521": "Title: Keeps getting logged out. Body: I keep getting logged out "
            "of the dashboard every few minutes. Started yesterday. Plan: Pro.",
    "4522": "Title: CSV export empty. Body: Exporting my project as CSV gives "
            "an empty file. Small projects work; the big one does not.",
}

KB = {
    "logout": "KB-104 'Unexpected logouts': cookies set with SameSite=Strict plus "
              "an http:// dashboard URL end sessions early; fix is forcing https.",
    "export": "KB-201 'Large exports time out': exports over 10k rows hit the 30s "
              "worker limit and return an empty file; use the async export API.",
}


def lookup_ticket(ticket_id: str) -> str:
    """Return the raw text of a ticket, or a not-found message.

    Example:
        >>> lookup_ticket("4521")
        "Title: Keeps getting logged out. ..."
        >>> lookup_ticket("9999")
        "No ticket with id '9999'."
    """
    # A miss returns a MESSAGE, not an exception — the model must be able
    # to read the failure and react to it (see the design note below).
    return TICKETS.get(ticket_id.strip(), f"No ticket with id {ticket_id!r}.")


def search_kb(query: str) -> str:
    """Naive keyword match over the KB; returns the first matching article.

    Example:
        >>> search_kb("user keeps getting logged out")
        "KB-104 'Unexpected logouts': ..."
    """
    q = query.lower()                        # match case-insensitively
    for keyword, article in KB.items():      # first keyword found wins
        if keyword in q:
            return article
    return f"No KB article matched {query!r}."


# The dispatch table: action name -> real function. The ONE door between
# the model's wishes and the real world (Principle 13 lives here).
TOOLS = {"lookup_ticket": lookup_ticket, "search_kb": search_kb}

# The contract — written in prose, enforced by politeness (see doc §3a).
SYSTEM = """You are Sutra, a support-ticket triage assistant. You cannot see any
data directly. To act, reply with exactly two lines:

THOUGHT: one sentence on what you need next and why
ACTION: <tool_name> <argument>

Available tools:
- lookup_ticket <ticket_id>   -> returns the raw ticket text
- search_kb <query>           -> returns the best-matching KB article

After each ACTION you will receive an OBSERVATION message with the result.
When you can answer the user, reply instead with:

THOUGHT: one sentence on why you are done
FINAL: your answer to the user

Never invent ticket contents or KB articles; if a lookup fails, say so in FINAL.
"""


def _line_after(reply: str, prefix: str) -> str | None:
    """The text after the first line starting with prefix, else None.

    Example:
        >>> _line_after("THOUGHT: need data\\nACTION: lookup_ticket 4521", "ACTION:")
        'lookup_ticket 4521'
    """
    for line in reply.splitlines():          # scan the reply line by line
        line = line.strip()
        if line.upper().startswith(prefix):  # tolerate case drift ("Action:")
            return line[len(prefix):].strip()  # keep only the part after it
    return None                              # the model ignored the format


def _dispatch(action: str) -> str:
    """Execute 'tool_name argument'; errors come back as observations.

    Example:
        >>> _dispatch("lookup_ticket 4521")
        "Title: Keeps getting logged out. ..."
        >>> _dispatch("send_email boss@corp")
        "Unknown tool 'send_email'. Available: lookup_ticket, search_kb."
    """
    name, _, argument = action.partition(" ")   # split on the FIRST space only
    tool = TOOLS.get(name.strip())              # look it up on OUR table
    if tool is None:                            # not on the menu?
        return f"Unknown tool {name.strip()!r}. Available: {', '.join(TOOLS)}."
    return tool(argument.strip())               # run it, return the result


def run_loop(
    client: genai.Client,
    question: str,
    *,
    forget_observations: bool = False,
    max_steps: int = MAX_STEPS,
) -> str | None:
    """Think->act->observe until FINAL or max_steps.

    forget_observations is the failure-lab switch (doc §5): tools still run,
    but nothing is written back to the transcript.

    Args:
        client: an authenticated genai.Client.
        question: the user's request, plain text.
        forget_observations: if True, stage the goldfish disaster on purpose.
        max_steps: the hard brake (default MAX_STEPS = 6).

    Returns:
        The model's FINAL answer, or None if the brake tripped.

    Example:
        >>> load_env()
        >>> client = genai.Client()
        >>> run_loop(client, "Ticket 4521 came in. What is wrong?")
        '...answer citing KB-104...'      # after ~3 model calls
    """
    # The dossier starts with just the question. From here on, WE are the
    # model's memory — every call re-sends everything (Day 2's lesson).
    transcript = [types.Content(role="user", parts=[types.Part(text=question)])]
    config = types.GenerateContentConfig(system_instruction=SYSTEM, temperature=0.0)

    for step in range(1, max_steps + 1):     # the brake is built into the loop
        # THINK: the model reads the whole dossier, proposes the next move.
        reply = (ask(client, transcript, config).text or "").strip()
        print(f"\n--- step {step} ---")
        print(reply)                         # THOUGHT + ACTION/FINAL: audit trail

        final = _line_after(reply, "FINAL:")
        if final is not None:                # the model says it's done
            return final                     # success path ends here

        # ACT: find the requested action and execute it (or explain the miss).
        action = _line_after(reply, "ACTION:")
        if action is None:                   # neither ACTION nor FINAL?
            observation = ("Protocol error: no ACTION: or FINAL: line. "
                           "Reply using the exact format.")   # coach it back
        else:
            observation = _dispatch(action)  # the one door to the real world
        print(f"OBSERVATION: {observation}")

        if forget_observations:              # the failure-lab switch:
            continue                         # nothing written back — the
                                             # dossier never grows (see §5)

        # OBSERVE: write BOTH sides into the dossier for the next call —
        # what the model said, and what the world answered.
        transcript.append(types.Content(role="model", parts=[types.Part(text=reply)]))
        transcript.append(
            types.Content(role="user", parts=[types.Part(text=f"OBSERVATION: {observation}")])
        )

    # The brake tripped. Say so honestly; never dress it up as an answer.
    print(f"\nNo FINAL within {max_steps} steps — stopping. That is containment, not success.")
    return None


TRIAGE_QUESTION = ("Ticket 4521 just came in. What is likely going wrong, "
                   "and what should we tell the user?")


def demo_triage(client: genai.Client) -> None:
    """The loop earns its keep: lookup -> KB search -> answer.

    Usage:  python -m sutra.loop triage      (~3 model calls)
    """
    print("\nANSWER:", run_loop(client, TRIAGE_QUESTION))


def demo_unknown(client: genai.Client) -> None:
    """A lookup that fails; the agent must say so, not invent a ticket.

    Usage:  python -m sutra.loop unknown     (~2 model calls)
    """
    print("\nANSWER:", run_loop(client, "Summarize ticket 9999 for the morning standup."))


def demo_goldfish(client: genai.Client) -> None:
    """Failure lab: act without observe. See doc §5 before running.

    Usage:  python -m sutra.loop goldfish    (4 model calls — expect a 429 pause)
    """
    print("\nANSWER:", run_loop(client, TRIAGE_QUESTION, forget_observations=True, max_steps=4))


def main() -> None:
    """Tiny demo dispatcher: `python -m sutra.loop <name>`."""
    demos = {"triage": demo_triage, "unknown": demo_unknown, "goldfish": demo_goldfish}
    name = sys.argv[1] if len(sys.argv) > 1 else "triage"
    if name not in demos:
        print(f"usage: python -m sutra.loop [{'|'.join(demos)}]")
        raise SystemExit(2)
    load_env()                               # keys from .env, never from code
    demos[name](genai.Client())


if __name__ == "__main__":                   # run as a script, not on import
    main()
