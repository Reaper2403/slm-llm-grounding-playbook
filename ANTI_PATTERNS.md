# Anti-patterns

## Giant prompt blob

Do not keep adding state, tools, policy, and transcript into one growing LLM prompt.

Failure mode:

- latency grows
- attention drifts
- state gets inconsistent

## SLM on every tiny turn

Do not run the SLM on every shard.

Failure mode:

- higher cost
- higher latency pressure
- low-signal garbage updates

## Free-form shared state writes

Do not let the LLM overwrite confirmed hard facts freely.

Failure mode:

- guesses turn into truth
- confirmed state gets corrupted

## Tool results as confirmation

Do not let a tool's returned lat/lon or entity ID become confirmation by itself.

Failure mode:

- semantically wrong but syntactically valid locks
- silent bad automation

## Empty-pass erasure

Do not let weak or empty SLM output wipe a stronger prior fact.

Failure mode:

- state oscillation
- repeated questioning
- confusing UI

## Hidden priority fights

Do not let the LLM, runtime, and tools each carry their own idea of what matters next.

Failure mode:

- user hears one question
- UI shows another priority
- tool side effects follow a third logic

## No distinction between candidate and confirmed

Do not collapse "possible" and "confirmed" into one field.

Failure mode:

- premature side effects
- misleading UI
- bad user trust

## Over-automating side effects

Do not fire expensive or risky actions just because one clue exists.

Failure mode:

- spam
- wrong dispatches
- incorrect records

## Treating the SLM as a mini general LLM

Do not ask the SLM to own tone, empathy, policy, routing, and extraction all together.

Failure mode:

- high latency
- brittle small-turn behavior
- overlap with the main LLM
