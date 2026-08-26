"""Tool declarations - what the model is told about Sutra's functions (Day 4, AG-04).

The functions themselves live in sutra.loop (Day 3). A declaration describes a
function to the provider; it never contains or imports one.

Verified against ai.google.dev/gemini-api/docs/function-calling on 2026-08-25.
"""

LOOKUP_TICKET = {
    "type": "function",
    "name": "lookup_ticket",
    "description": (
        "Fetch the full text of one support ticket by its id. "
        "Use this first whenever the user names or implies a specific ticket, "
        "before offering any diagnosis. "
        "Returns the ticket's title and body, or a message saying no such ticket exists."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "ticket_id": {
                "type": "string",
                "description": "The ticket's id as it appears in the request, e.g. '4521'.",
            }
        },
        "required": ["ticket_id"],
    },
}

# Written from the shape of LOOKUP_TICKET (1.2). `query` gets no `enum`: the symptom words
# come out of a ticket body nobody has read yet, so the set of valid values is not knowable
# in advance. An enum here would reject every real symptom that is not on the list, which is
# the opposite of what this tool is for. `enum` belongs on a closed set - a status, a plan
# tier - not on free text.
SEARCH_KB = {
    "type": "function",
    "name": "search_kb",
    "description": (
        "Search the internal knowledge base for a known issue matching a symptom. "
        "Use this after reading a ticket, with the symptom words from the ticket "
        "body. Returns one article, or a message saying nothing matched. "
        "Do not use this to look up a ticket - use lookup_ticket for that."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "Symptom words taken from the ticket, e.g. 'keeps getting logged out'."
                ),
            }
        },
        "required": ["query"],
    },
}

# The list sent on every call. Tools are interaction-scoped, not client-scoped (3.1).
DECLARATIONS = [LOOKUP_TICKET, SEARCH_KB]
