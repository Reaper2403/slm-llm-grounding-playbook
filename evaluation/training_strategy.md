# Training and Evaluation Strategy

## Recommended rollout order

### Stage 1: prompt-only baseline

Build:

- a narrow ledger schema
- a simple runtime merge
- a compact LLM prompt packet

Measure where prompt-only extraction breaks.

### Stage 2: fine-tune the SLM

Fine-tune only the background hard-fact extractor.

Success criteria:

- better carry-forward
- fewer false positives
- better correction handling
- better candidate discipline

### Stage 3: harden tool gating

Use the improved SLM output to gate:

- search
- lookup
- pinning
- side effects

### Stage 4: optional LLM specialization

Only if needed, improve tone or vertical-specific flow later.

## Dataset slices you should explicitly track

- clean direct facts
- fragmented facts across turns
- contradicting/corrected facts
- low-signal turns
- vague-but-not-actionable cues
- semantically similar but wrong candidates
- dead-end confirmation ladders

## Minimal benchmark set

For each domain, keep a small but honest benchmark with:

- 25 easy examples
- 25 medium examples
- 25 noisy examples
- 25 known failure cases

This is more useful than a large but unrealistic test set.
