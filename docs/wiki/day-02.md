# Day 02 - LLM mechanics for agent builders

IDs closed: AG-02 · source: `days/day-02-llm-mechanics/`

## Parts

### 1.1 - The call that forgets you — what one model request actually is
`days/day-02-llm-mechanics/parts/01-first-contact/1.1-the-call-that-forgets-you.md` · level `foundation` · ids AG-02

A model request is a single, self-contained transaction — you send everything the model is allowed to know, it sends back words, and then it discards every trace of you — which means every appearance of memory in every chat product you have ever used is somebody re-sending the transcript.

### 1.2 - Pinning before installing — the version you looked up, not the one you remember
`days/day-02-llm-mechanics/parts/01-first-contact/1.2-pinning-before-installing.md` · level `working` · ids AG-02

Sutra installs its first package today, and the rule that governs it is the version goes in the command, the lookup happens before the command, and the observation goes in a ledger — because a dependency you cannot name the version of is a dependency you cannot debug a year from now.

### 1.3 - Listed is not callable — choosing a free model with a live call
`days/day-02-llm-mechanics/parts/01-first-contact/1.3-listed-is-not-callable.md` · level `working` · ids AG-02

A model appearing in the documentation, in the pricing page, or in your own models.list() output is not evidence that your key can call it — only a live call is — and this is the single most reliable way to lose an evening at the start of an LLM project.

### 1.4 - The first interaction — Sutra's first words
`days/day-02-llm-mechanics/parts/01-first-contact/1.4-the-first-interaction.md` · level `working` · ids AG-02

One call — client.interactions.create(model=..., input=...) — returns an object carrying the model's text and a receipt, and learning to care about the second one as much as the first is the difference between someone who uses an LLM and someone who operates one.

### 1.5 - The only door — 429 handling that listens to the server
`days/day-02-llm-mechanics/parts/01-first-contact/1.5-the-only-door-429.md` · level `production` · ids AG-02

Every model call in this project goes through one function, and that function backs off using the delay the server stated rather than a number you invented — then, when it runs out of tries, it raises instead of returning something plausible.

### 2.1 - What a token is — why nothing is counted in words
`days/day-02-llm-mechanics/parts/02-tokens-the-meter/2.1-what-a-token-is.md` · level `foundation` · ids AG-02

A token is a chunk of text — often a fragment of a word rather than a whole one — and it is the unit in which every limit, every quota and every bill in this field is denominated, which makes "how many tokens is that?" the most practical question you can learn to estimate.

### 2.2 - Reading the receipt — what interaction.usage actually tells you
`days/day-02-llm-mechanics/parts/02-tokens-the-meter/2.2-reading-the-receipt.md` · level `working` · ids AG-02

Every response carries a usage object that is the true, measured account of what the call cost — input, output, and a third number most people do not know exists — and reading it is the only way to replace estimates with facts.

### 2.3 - The thinking tax — output you pay for and never see
`days/day-02-llm-mechanics/parts/02-tokens-the-meter/2.3-the-thinking-tax.md` · level `production` · ids AG-02

Modern Gemini Flash models reason before they answer, by default, and that reasoning is billed as output while remaining invisible to you — so the tokens you are charged for can be several times the tokens you can read.

### 3.1 - The desk that gets wiped — the context window, and what fits on it
`days/day-02-llm-mechanics/parts/03-context-and-memory/3.1-the-desk-that-gets-wiped.md` · level `foundation` · ids AG-02

The context window is the total amount of text a model can consider in one request — everything you send plus everything it generates, measured in tokens — and it is not a memory, because it is emptied completely the moment the request ends.

### 3.2 - History is a list you own — proving the amnesia, then curing it
`days/day-02-llm-mechanics/parts/03-context-and-memory/3.2-history-is-a-list-you-own.md` · level `working` · ids AG-02

Tell the model a fact, ask about it in a separate call, and it will not know — until you send the earlier exchange back as part of the new request, at which point it "remembers" instantly, because the memory was never in the model; it was in the list you built.

### 3.3 - The server will remember for you — and why Sutra says no
`days/day-02-llm-mechanics/parts/03-context-and-memory/3.3-the-server-will-remember.md` · level `production` · ids AG-02

The Interactions API will hold your conversation on Google's servers and let you continue it with previous_interaction_id — which is genuinely useful, is on by default, and is a decision this project makes deliberately in the other direction.

### 4.1 - The probability list nobody shows you
`days/day-02-llm-mechanics/parts/04-sampling-the-dial/4.1-the-probability-list.md` · level `foundation` · ids AG-02

A model does not produce a word — it produces a score for every word it could possibly say next — and something separate then picks one from that list, which is why the same prompt can give different answers and why "the model decided" is usually the wrong description of what happened.

### 4.2 - Turning the dial — temperature, top_p, top_k, and watching them move
`days/day-02-llm-mechanics/parts/04-sampling-the-dial/4.2-turning-the-dial.md` · level `working` · ids AG-02

Temperature reshapes the probability list to make underdogs more or less likely, while top_p and top_k delete the tail of the list before anything is drawn — and the reason to know all three is that they solve different problems and are routinely confused for each other.

### 4.3 - Stability is not reproducibility — why temperature 0 is not a guarantee
`days/day-02-llm-mechanics/parts/04-sampling-the-dial/4.3-stability-is-not-reproducibility.md` · level `production` · ids AG-02

temperature=0 removes the deliberate randomness and gives you output that is stable in practice — but it is not a contractual promise of identical bytes, because floating-point arithmetic, serving infrastructure and model updates can all shift the front-runner, which is why tests that assert exact strings eventually fail for reasons nobody deployed.

### 5.1 - 💥 Failure lab — the cap that ate the answer
`days/day-02-llm-mechanics/parts/05-the-failure-lab/5.1-the-cap-that-ate-the-answer.md` · level `production` · ids AG-02

Set max_output_tokens small on a thinking model and you will get a successful call with no answer in it — because the reasoning spends the budget before the visible text gets any, and the cap is a wall rather than an instruction.

### 6.1 - 🅿️ generate_content — the door every tutorial walks through
`days/day-02-llm-mechanics/parts/06-the-legacy-door/6.1-generate-content-parked.md` · level `production` · ids AG-02

client.models.generate_content(...) is the older Gemini surface — not deprecated, still fully supported, and relabelled "Legacy" in the documentation — and because virtually every tutorial, blog post and older repository uses it, being unable to read it is a real handicap even if you never type it.

## Papers - read after the parts

### arXiv:1508.07909 - Neural Machine Translation of Rare Words with Subword Units — why a token is not a word
`days/day-02-llm-mechanics/papers/01-subword-units.md`

The reason your bill is counted in fragments rather than words is a 2015 translation paper that solved a completely different problem — running out of vocabulary — and its fix, chop rare words into re-usable pieces, is why gemini-3.7-flash can read a word that has never existed before.

### arXiv:2201.11903 - Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — the tax you pay for
`days/day-02-llm-mechanics/papers/02-chain-of-thought-prompting.md`

The invisible tokens on your bill in [part 2.3](../parts/02-tokens-the-meter/2.3-the-thinking-tax.md) are a 2022 finding turned into a product feature: making a model write out its intermediate steps makes it dramatically better at multi-step problems, and once that was known, providers stopped waiting to be asked.

### arXiv:1904.09751 - The Curious Case of Neural Text Degeneration — why the most likely word is the wrong word
`days/day-02-llm-mechanics/papers/03-neural-text-degeneration.md`

top_p exists because of a 2019 finding that reads like a paradox — always choosing the most likely next word produces text no human would write — and the fix, cutting off the tail of the probability list instead of reshaping it, is the dial you turned in [part 4.2](../parts/04-sampling-the-dial/4.2-turning-the-dial.md).

