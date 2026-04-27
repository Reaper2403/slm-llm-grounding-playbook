# Social and Blog Copy

## One-line description

An SLM + LLM architecture pattern where the LLM stays conversational while a background SLM maintains a strict fact ledger and tool permissions.

## Short post

We found that making one big LLM prompt smarter was not enough for noisy, stateful workflows. The better pattern was a split system: a fast LLM for conversation and a background SLM for evidence-only grounding. The SLM updates a shared ledger of confirmed facts, while the LLM stays adaptive and uses that ledger to decide what to ask next.

## Why it matters

- keeps first response fast
- improves factual carry-forward
- reduces repeated questions
- gates tools off grounded state instead of raw model confidence

## Credit framing

This pattern is especially useful with fine-tuned small models that can replace part of a general LLM's state-tracking burden without taking over the whole user-facing experience.
