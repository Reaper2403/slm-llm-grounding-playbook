# SLM + LLM Grounding Playbook

Patterns for combining a fast conversational LLM with a smaller grounding model (SLM) that tracks hard facts in the background.

This repo is not tied to one product vertical. It packages a reusable architecture for teams who want:

- real-time conversation without blocking on slower reasoning
- stronger factual carry-forward than a prompt-only LLM loop
- safer tool use through explicit state and permissions
- a clean split between dialogue quality and evidence tracking

## Core idea

Use two lanes:

- **Fast voice/chat lane**: the LLM speaks immediately from the last committed state.
- **Slow grounding lane**: the SLM runs in the background, extracts hard facts, updates a shared ledger, and tells the LLM what matters next.

The user experiences one assistant. Under the hood:

- the **LLM** owns delivery, tone, ambiguity handling, and adaptive questioning
- the **SLM** owns evidence-only fact extraction and state carry-forward
- the **runtime** owns priority, permissions, confirmation loops, and tool gating
- the **tools** own deterministic actions like search, lookup, and side effects

## Why this exists

Pure prompt growth eventually fails. As transcripts get longer and tool state grows, the main LLM starts to:

- repeat itself
- forget resolved facts
- treat guesses like confirmed data
- drift away from the most important missing information
- over-call tools or ignore them entirely

This playbook keeps the LLM conversational while moving rigid state-tracking into a background grounding layer.

## What is in this repo

- [PLAYBOOK.md](./PLAYBOOK.md): the end-to-end method
- [FINE_TUNING.md](./FINE_TUNING.md): when to fine-tune, what to fine-tune, and how
- [REFERENCE_ARCHITECTURE.md](./REFERENCE_ARCHITECTURE.md): system shape and data flow
- [ANTI_PATTERNS.md](./ANTI_PATTERNS.md): what usually goes wrong
- [schemas](./schemas): copyable JSON schemas
- [prompts](./prompts): reusable prompt templates
- [orchestration](./orchestration): trigger, merge, and scheduling rules
- [examples](./examples): domain-specific adaptations
- [evaluation](./evaluation): what to measure
- [evaluation/training_strategy.md](./evaluation/training_strategy.md): rollout and dataset strategy
- [starter_sdk/python](./starter_sdk/python): tiny reference implementation

## Recommended mental model

Think of the SLM as a strict smart diary:

- it reads the conversation
- writes down only what is explicitly known
- carries those facts forward consistently
- highlights what is still missing
- gives the LLM the next highest-priority fact to collect

The LLM stays natural because it no longer has to be the diary, the voice actor, the state machine, and the tool router all at once.

## When to use this pattern

This pattern is most useful when:

- conversation quality matters
- transcripts are noisy or fragmented
- a few facts are much more important than everything else
- tool calls should only happen after certain facts are grounded
- you need better factual consistency without turning the whole system into a rigid workflow

Good fits:

- emergency dispatch
- healthcare intake
- support triage
- field ops copilots
- compliance-heavy customer workflows

## Quick start

1. Start with the schemas in [schemas](./schemas).
2. Use the prompts in [prompts](./prompts) as a base.
3. Adopt the scheduling rules in [orchestration/scheduler.md](./orchestration/scheduler.md).
4. Wire a shared ledger into your session state.
5. Feed your LLM only the compact prompt packet, not the full transcript state blob.
6. Gate tools off the ledger, not off raw LLM confidence.

## Fine-tuning guidance

This repo now includes a dedicated [fine-tuning guide](./FINE_TUNING.md).

Short version:

- fine-tune the **background SLM** first
- keep its job narrow and evidence-only
- use real transcript failures plus synthetic coverage
- evaluate system outcomes, not just schema validity

## Design principles

- Keep the **voice path** fast.
- Keep the **grounding path** strict.
- Never let the **slow path** block first response.
- Keep **confirmed facts** separate from guesses.
- Treat the **shared ledger** as the source of truth.
- Let tools act only when permissions are explicitly open.

## License

MIT
