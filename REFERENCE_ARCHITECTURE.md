# Reference Architecture

## High-level chain

```text
user input
  -> fast LLM lane
       -> immediate response from last committed state
  -> background SLM lane
       -> extract hard facts
       -> merge into shared ledger
       -> recompute prompt packet + tool permissions
  -> deterministic tools
       -> run only when ledger permits
  -> UI / logs
       -> render same ledger and tool state
```

## Fast lane

The fast lane is optimized for responsiveness.

Responsibilities:

- speak or reply immediately
- acknowledge the user
- ask the next question from the prompt packet
- follow confirmation instructions
- avoid drifting from the ledger priority

The fast lane should not:

- wait for the SLM
- run heavy searches before first response
- decide that a candidate is confirmed on its own

## Slow lane

The slow lane is optimized for consistency.

Responsibilities:

- read a compact transcript window
- extract explicit facts
- carry prior facts forward
- detect corrections
- update the hard-fact section of the ledger

The slow lane should not:

- own the user-facing tone
- decide empathy wording
- control tool side effects directly

## Shared ledger

Recommended sections:

- `hard_facts`
- `soft_state`
- `priority`
- `tool_gate`
- `provenance`

The ledger is the source of truth.
The prompt packet is only a projection of the ledger.

## Tool gating

Only the runtime should decide when tools are allowed.

Examples:

- do not geocode a vague location clue
- do not create side effects from candidate-only IDs
- do not send CRM updates until user identity is confirmed
- do not dispatch/route until location is meaningful enough

## Confirmation loops

Every domain should define its own confirmation ladder.

Example pattern:

1. Ask for the main entity.
2. Ask for the exact form if the answer is too vague.
3. Repeat candidate and ask for yes/no confirmation.
4. Ask for spelling or nearest anchor if still unclear.
5. Accept best-effort fallback if dead end is reached.

## Common domain adaptations

- **Emergency dispatch**
  - location and injury state dominate
- **Healthcare intake**
  - patient identity, symptoms, severity, contraindications
- **Support triage**
  - account identity, issue type, urgency, prior actions
- **Field operations**
  - site, asset, risk condition, crew count, access constraints
