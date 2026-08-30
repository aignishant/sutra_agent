# Day 14 - Plugins — one layer up

IDs closed: ADK-16 · source: `days/day-14-plugins-one-layer-up/`

## Parts

### 1.1 - The rule nobody has to remember
`days/day-14-plugins-one-layer-up/parts/01-where-a-plugin-lives/1.1-the-rule-nobody-has-to-remember.md` · level `foundation` · ids ADK-16

A plugin is a rule you attach to the whole application instead of to one agent, so it applies to every agent in it — including the agents nobody has written yet.

### 1.2 - The App is what plugins belong to
`days/day-14-plugins-one-layer-up/parts/01-where-a-plugin-lives/1.2-the-app-is-what-plugins-belong-to.md` · level `working` · ids ADK-16

Plugins are declared on an App — the object that names the whole application and holds its root agent — and passing them to Runner instead still works, is deprecated, and is the one way to install a plugin that silently installs nothing.

### 1.3 - A name, and only one of it
`days/day-14-plugins-one-layer-up/parts/01-where-a-plugin-lives/1.3-a-name-and-only-one-of-it.md` · level `working` · ids ADK-16

Every plugin carries a required name, no two plugins in one application may share one, and the check happens when the Runner is built rather than when the App is — so the error arrives one line later than you expect.

### 2.1 - Fourteen doors, and six you already know
`days/day-14-plugins-one-layer-up/parts/02-the-fourteen-doors/2.1-fourteen-doors-six-you-already-know.md` · level `working` · ids ADK-16

A plugin in google-adk 2.7.1 can override fourteen hooks — the six an agent already has, four that only exist at this layer, two more error hooks, and two that are notification-only — and the published documentation still lists twelve.

### 2.2 - The four doors an agent cannot have
`days/day-14-plugins-one-layer-up/parts/02-the-fourteen-doors/2.2-the-four-doors-an-agent-cannot-have.md` · level `working` · ids ADK-16

Four hooks — on_user_message_callback, before_run_callback, on_event_callback and after_run_callback — wrap the whole request rather than one agent's turn, and they exist only at the plugin layer because no agent is in a position to answer a question about the request as a whole.

### 2.3 - The names moved
`days/day-14-plugins-one-layer-up/parts/02-the-fourteen-doors/2.3-the-names-moved.md` · level `working` · ids ADK-16

The plugin hooks take the same information as yesterday's agent callbacks under different parameter names — tool_args for args, result for tool_response — so a working callback copied into a plugin class raises a TypeError at the first tool call.

### 2.4 - Fifteen firings, one run
`days/day-14-plugins-one-layer-up/parts/02-the-fourteen-doors/2.4-fifteen-firings-one-run.md` · level `working` · ids ADK-16

One question that causes one tool call fires ten distinct plugin hooks fifteen times, and the order is not the order they are listed in — the model doors fire twice, on_event_callback fires three times, and the run-level pair brackets everything.

### 3.1 - `is not None`, and this time it means it
`days/day-14-plugins-one-layer-up/parts/03-the-rule-at-this-layer/3.1-is-not-none-and-this-time-it-means-it.md` · level `production` · ids ADK-16

The plugin chain stops at the first hook returning anything that is not None — which is the rule as documented, and the opposite of the agent-callback chain you measured yesterday, where an empty dict does not stop the chain but the last value assigned still replaces the tool.

### 3.2 - The two hooks that cannot stop anything
`days/day-14-plugins-one-layer-up/parts/03-the-rule-at-this-layer/3.2-the-two-hooks-that-cannot-stop-anything.md` · level `production` · ids ADK-16

on_agent_error_callback and on_run_error_callback are notification-only: every plugin is always told, their return values are discarded, the original exception is always re-raised, and a plugin that raises inside one of them has its own error swallowed so it cannot mask the real failure.

### 3.3 - A plugin that raises takes the run with it
`days/day-14-plugins-one-layer-up/parts/03-the-rule-at-this-layer/3.3-a-plugin-that-raises-takes-the-run-with-it.md` · level `production` · ids ADK-16

An exception in any of the twelve non-notification hooks is re-raised as a RuntimeError naming the plugin and the hook, killing the whole request for every agent — so a plugin's error handling is application-wide error handling whether you wrote it that way or not.

### 4.1 - Counting what a run costs
`days/day-14-plugins-one-layer-up/parts/04-the-meter/4.1-counting-what-a-run-costs.md` · level `working` · ids ADK-16

Two hooks — before_model_callback and before_tool_callback — are the only two places where quota is actually spent, so counting there gives you the true cost of a request, and a question needing two tools costs three model calls rather than one.

### 4.2 - The bill at the exit door
`days/day-14-plugins-one-layer-up/parts/04-the-meter/4.2-the-bill-at-the-exit-door.md` · level `working` · ids ADK-16

after_run_callback is the one hook that knows the request is over, so it is where the bill is printed — and it fires after the caller already has the answer, its return value is discarded, and it cannot change anything.

### 4.3 - One instance, every run
`days/day-14-plugins-one-layer-up/parts/04-the-meter/4.3-one-instance-every-run.md` · level `production` · ids ADK-16

A plugin is constructed once and reused for the lifetime of the application, so a counter stored on self accumulates across every request — reporting 2, 4, 6 for three identical runs in sequence, and 6, 6, 6 for three at the same time.

### 5.1 - The door documented to stop the run, and does not
`days/day-14-plugins-one-layer-up/parts/05-where-the-layer-bites/5.1-the-door-documented-to-stop-the-run.md` · level `production` · ids ADK-16

before_run_callback returning a types.Content is documented to halt the request and answer with that content — and on an LlmAgent root, which is every agent Sutra has, the return value is discarded and the agent runs anyway.

### 5.2 - The bill that never prints
`days/day-14-plugins-one-layer-up/parts/05-where-the-layer-bites/5.2-the-bill-that-never-prints.md` · level `production` · ids ADK-16

after_run_callback fires only when the request succeeded, so a meter built on it reports nothing for failed runs — which still spent their quota — and leaks one dictionary entry each; the fix is to report from on_run_error_callback as well.

### 6.1 - 💥 The rule that broke an agent nobody was looking at
`days/day-14-plugins-one-layer-up/parts/06-failure-lab/6.1-the-rule-that-broke-an-agent-nobody-was-looking-at.md` · level `production` · ids ADK-16

Promoting a correct per-agent policy to an application-wide plugin applies it to agents it was never written for — so a guard that was right for the triage desk silently disables the one agent whose actual job is the thing being blocked.

### 7.1 - The plugins ADK already ships
`days/day-14-plugins-one-layer-up/parts/07-in-production/7.1-the-plugins-adk-already-ships.md` · level `production` · ids ADK-16

google-adk 2.7.1 ships nine working plugins in google/adk/plugins/, and reading two of them — ReflectAndRetryToolPlugin and ContextFilterPlugin — confirms from the framework's own source the two rules this day derived by measurement.

### 7.2 - Testing a plugin without a model
`days/day-14-plugins-one-layer-up/parts/07-in-production/7.2-testing-a-plugin-without-a-model.md` · level `production` · ids ADK-16

A plugin cannot be tested by calling its hooks directly the way an agent callback can, because every interesting thing about it — that it is installed, that it covers every agent, that it cleans up on failure — is a fact about a whole run, so the suite drives a real Runner against a scripted model and asserts on outcomes rather than on hooks having fired.

### 7.3 - Which layer does this rule belong to
`days/day-14-plugins-one-layer-up/parts/07-in-production/7.3-which-layer-does-this-rule-belong-to.md` · level `production` · ids ADK-16

One question decides it — if somebody adds an agent next quarter and forgets this rule, is that a bug or a choice? — and the answer is written down next to the code, because the layer is a decision and an undocumented decision gets reversed by the next person.

## Papers - read after the parts

### doi:10.1007/BFb0053381 - Aspect-oriented programming
`days/day-14-plugins-one-layer-up/papers/01-aspect-oriented-programming.md`

Some concerns cannot be put in a module of their own no matter how you decompose a program, because they cut across the decomposition — and the paper's proposal was to write each such concern once, separately, and have a mechanism apply it at named points in the code it affects.

