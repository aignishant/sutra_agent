# Paper Ledger — Project Sutra

Append-only. §17.4.1 rule 5: **never invent a citation.** Every paper a day cites gets a row here
with the title copied from the record, the identifier that resolves to it, and the date the record
was actually opened — not the date it was remembered.

This is Principle 7 pointed at the literature, and it bites harder than the version case. A wrong
version pin fails loudly the next time someone runs `uv sync`. A plausible arXiv ID attached to the
wrong title fails **silently, for years**, and the person who discovers it is a reader who followed
it into a search engine and found something else. So the rule is the same as for a version: if it
could not be looked up, the row says `TODO(<the exact lookup command>)` — never a guess.

**A paper is taught once in the curriculum** (§17.4.2). *Taught in* is the paper part that explains
it; every later day that leans on the same idea cites it in its own §6 and links to that part rather
than re-teaching it. To find every part citing a paper:

```bash
grep -rl "arXiv:1706.03762" days/
```

**How to cite** (§18.1 rule 5): by **title and identifier, never by authors**. An arXiv ID is
written `arXiv:1706.03762`; a DOI is written with its prefix, `doi:10.1145/3442188.3445922`, so it
can be found in prose without guessing where it ends.

| Paper | Identifier | Year | Verified | Day | Taught in |
| ----- | ---------- | ---- | -------- | --- | --------- |
| Intelligent agents: theory and practice | doi:10.1017/S0269888900008122 | 1995 | 2026-08-25 | 1 | `days/day-01-bootstrap-and-map/papers/01-intelligent-agents.md` |
| Neural Machine Translation of Rare Words with Subword Units | arXiv:1508.07909 | 2015 | 2026-08-25 | 2 | `days/day-02-llm-mechanics/papers/01-subword-units.md` |
| Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | arXiv:2201.11903 | 2022 | 2026-08-25 | 2 | `days/day-02-llm-mechanics/papers/02-chain-of-thought-prompting.md` |
| Large Language Models are Zero-Shot Reasoners | arXiv:2205.11916 | 2022 | 2026-08-25 | 2 | *(not taught — named in `papers/02-chain-of-thought-prompting.md` as the paper CoT is confused with)* |
| The Curious Case of Neural Text Degeneration | arXiv:1904.09751 | 2019 | 2026-08-25 | 2 | `days/day-02-llm-mechanics/papers/03-neural-text-degeneration.md` |
| ReAct: Synergizing Reasoning and Acting in Language Models | arXiv:2210.03629 | 2022 | 2026-08-25 | 3 | `days/day-03-loop-hand-rolled/papers/01-react.md` |
| Toolformer: Language Models Can Teach Themselves to Use Tools | arXiv:2302.04761 | 2023 | 2026-08-25 | 4 | `days/day-04-tools-by-hand/papers/01-toolformer.md` |
| Training language models to follow instructions with human feedback | arXiv:2203.02155 | 2022 | 2026-08-26 | 6 | `days/day-06-instructions-and-personas/papers/01-instructgpt.md` |
| RouteLLM: Learning to Route LLMs with Preference Data | arXiv:2406.18665 | 2024 | 2026-08-26 | 9 | `days/day-09-four-free-providers/papers/01-routellm.md` |
| FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance | arXiv:2305.05176 | 2023 | 2026-08-26 | 9 | *(not taught — named in `papers/01-routellm.md` as the cascade the router is contrasted with)* |
| Efficient Guided Generation for Large Language Models | arXiv:2307.09702 | 2023 | 2026-08-27 | 12 | `days/day-12-structured-output/papers/01-guided-generation.md` |
| Aspect-oriented programming | doi:10.1007/BFb0053381 | 1997 | 2026-08-30 | 14 | `days/day-14-plugins-one-layer-up/papers/01-aspect-oriented-programming.md` |
| Implementing remote procedure calls | doi:10.1145/2080.357392 | 1984 | 2026-08-30 | 15 | `days/day-15-toolsets-and-openapi/papers/01-implementing-remote-procedure-calls.md` |
| PAL: Program-aided Language Models | arXiv:2211.10435 | 2022 | 2026-09-03 | 16 | `days/day-16-built-in-tools-with-brakes/papers/01-program-aided-language-models.md` |
| Lost in the Middle: How Language Models Use Long Contexts | arXiv:2307.03172 | 2023 | 2026-09-03 | 19 | `days/day-19-context-engineering-selection/papers/01-lost-in-the-middle.md` |
| MemGPT: Towards LLMs as Operating Systems | arXiv:2310.08560 | 2023 | 2026-09-03 | 20 | `days/day-20-context-engineering-compaction/papers/01-memgpt.md` |
| End-to-end arguments in system design | doi:10.1145/357401.357402 | 1984 | 2026-09-03 | 21 | `days/day-21-errors-surface-not-swallow/papers/01-end-to-end-arguments.md` |
| Time, clocks, and the ordering of events in a distributed system | doi:10.1145/359545.359563 | 1978 | 2026-09-03 | 22 | `days/day-22-structured-logging/papers/01-time-clocks-ordering.md` |
| Mock roles, not objects | doi:10.1145/1028664.1028765 | 2004 | 2026-09-04 | 23 | `days/day-23-testing-tools-and-callbacks/papers/01-mock-roles-not-objects.md` |
| New directions in communications (or which way to the information age?) | doi:10.1109/MCOM.1986.1092946 | 1986 | 2026-09-04 | 24 | `days/day-24-token-accounting-and-budgets/papers/01-the-leaky-bucket.md` |
| Reflections on trusting trust | doi:10.1145/358198.358210 | 1984 | 2026-09-04 | 29 | `days/day-29-sourcing-and-auditing-skills/papers/01-reflections-on-trusting-trust.md` |
| Hints on Test Data Selection: Help for the Practicing Programmer | doi:10.1109/C-M.1978.218136 | 1978 | 2026-09-04 | 30 | `days/day-30-skill-testing-and-versioning/papers/01-hints-on-test-data-selection.md` |
| Principled design of the modern Web architecture | doi:10.1145/514183.514185 | 2002 | 2026-09-04 | 32 | `days/day-32-mcp-stateless-core/papers/01-modern-web-architecture.md` |
| Principled design of the modern Web architecture (ICSE 2000, the earlier and shorter version) | doi:10.1145/337180.337228 | 2000 | 2026-09-04 | 32 | *(not taught - named in `papers/01-modern-web-architecture.md` as the version not to cite; the 2002 TOIT paper is the canonical one)* |
| Promises: linguistic support for efficient asynchronous procedure calls in distributed systems | doi:10.1145/53990.54016 | 1988 | 2026-09-04 | 36 | `days/day-36-long-jobs-and-tasks/papers/01-promises.md` |
| OAuth 2.0 Authorization Server Issuer Identification | doi:10.17487/RFC9207 | 2022 | 2026-09-04 | 37 | `days/day-37-auth-and-elicitation/papers/01-issuer-identification.md` |
| The OAuth 2.0 Authorization Framework | doi:10.17487/RFC6749 | 2012 | 2026-09-04 | 37 | *(not taught - named in `papers/01-issuer-identification.md` as the framework RFC 9207 patches; itself updated by RFC 8252, RFC 8996 and RFC 9700)* |
| Best Current Practice for OAuth 2.0 Security | doi:10.17487/RFC9700 | 2025 | 2026-09-04 | 37 | *(not taught - named in `papers/01-issuer-identification.md` as what supersedes parts of RFC 6749's advice)* |
| OAuth 2.0 Protected Resource Metadata | doi:10.17487/RFC9728 | 2025 | 2026-09-04 | 37 | *(not taught - named in `papers/01-issuer-identification.md` as what an MCP server actually publishes)* |
| Maintaining Robust Protocols | doi:10.17487/RFC9413 | 2023 | 2026-09-04 | 38 | `days/day-38-failure-and-migration-lab/papers/01-maintaining-robust-protocols.md` |
| A Relational Model of Data for Large Shared Data Banks | doi:10.1145/362384.362685 | 1970 | 2026-09-04 | 39 | `days/day-39-database-tools/papers/01-relational-model.md` |
| A Relational Model of Data for Large Shared Data Banks (the 1983 CACM reprint) | doi:10.1145/357980.358007 | 1983 | 2026-09-04 | 39 | *(not taught - named in `papers/01-relational-model.md` as the reprint that is not the citation)* |
| The protection of information in computer systems | doi:10.1109/PROC.1975.9939 | 1975 | 2026-09-04 | 40 | `days/day-40-filtering-and-allowlists/papers/01-protection-of-information.md` |
| A note on distributed computing | doi:10.1007/3-540-62852-5_6 | 1997 | 2026-09-04 | 42 | `days/day-42-serving-agents-over-mcp/papers/01-a-note-on-distributed-computing.md` |
| The tail at scale | doi:10.1145/2408776.2408794 | 2013 | 2026-09-04 | 44 | `days/day-44-client-hardening/papers/01-the-tail-at-scale.md` |
| Generative Agents: Interactive Simulacra of Human Behavior | arXiv:2304.03442 | 2023 | 2026-09-04 | 46 | `days/day-46-sessions-vs-memory/papers/01-generative-agents.md` |
| Principles of transaction-oriented database recovery | doi:10.1145/289.291 | 1983 | 2026-09-04 | 47 | `days/day-47-persistent-sessions/papers/01-transaction-oriented-recovery.md` |
