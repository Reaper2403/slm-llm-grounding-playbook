# Playbook

## 1. Split responsibilities on purpose

Do not ask one model to do everything.

Use this split:

- **LLM**
  - tone
  - empathy
  - adaptive questioning
  - conversational repair
  - soft reasoning and provisional guesses
- **SLM**
  - explicit fact extraction
  - hard-fact carry-forward
  - contradiction-sensitive updates
  - missing-field identification
- **Runtime**
  - priority ordering
  - confirmation loops
  - tool permissions
  - candidate locking
  - escalation rules
- **Tools**
  - deterministic lookup
  - map/search/CRM/database actions
  - side effects

## 2. Create one shared ledger

Everyone reads one shared object.

Not everyone writes every field.

Recommended ownership:

- `hard_facts.*` -> SLM or deterministic tools only
- `soft_state.*` -> LLM/runtime only
- `priority.*` -> runtime only
- `tool_gate.*` -> runtime only
- `ui.*` -> derived view, never source of truth

The ledger is the coordination layer between the fast and slow lanes.

## 3. Keep the slow path off the critical path

The slow path should never block the assistant's first acknowledgment.

Use this sequence:

1. User speaks.
2. LLM responds from the last committed ledger.
3. Background SLM runs on a compact transcript slice.
4. Runtime merges the result.
5. The next LLM turn uses the updated prompt packet.

This is a stale-while-refresh pattern for conversational AI.

## 4. Give the LLM a tiny packet, not a giant state dump

The LLM should not ingest the entire ledger and transcript on every turn.

Send only:

- what is known
- what is missing
- what the next question should target
- which actions are blocked
- whether any candidate needs confirmation now

This preserves latency and keeps the LLM adaptable instead of brittle.

## 5. Treat candidate confirmation as a first-class flow

A grounded candidate is not the same as a confirmed fact.

Use this flow:

1. SLM or runtime notices a meaningful clue.
2. Tools may preflight a background lookup.
3. Result becomes `candidate_only`.
4. Runtime forces the LLM to confirm it.
5. Only after confirmation does the tool gate open for stronger actions.

This keeps tools useful without letting them silently lock mistakes.

## 6. Schedule SLM runs intentionally

Do not run the SLM on every turn.

Good triggers:

- every 2-3 substantive user turns
- explicit location clues
- corrections such as `actually` or `no bleeding`
- high-signal facts such as `gun`, `trapped`, `not breathing`, `fire`

Bad triggers:

- bare `yes`
- bare `no`
- `okay`
- `hello`
- filler-only STT shards

## 7. Merge conservatively

A weak new pass should not erase a stronger old fact.

Rules:

- keep confirmed facts until explicitly corrected
- do not let empty SLM output wipe a useful prior field
- do not promote guesses into confirmed fields
- carry forward prior hard facts by default

## 8. Let the LLM stay good at being an LLM

If you over-constrain the model, it becomes robotic.

If you under-constrain the model, it becomes inconsistent.

The sweet spot is:

- strict state
- flexible language

The ledger defines the destination.
The LLM chooses the natural words.

## 9. Evaluate the pattern, not just the model

Success is not only extraction quality.

Measure:

- first-response latency
- re-ask rate
- contradiction recovery
- candidate confirmation rate
- tool gating precision
- percent of resolved sessions with grounded lookup before side effects

## 10. Use domain templates, not domain lock-in

The pattern is generic.
Only the ledger schema, trigger rules, and confirmation ladders should be domain-specific.
