# Fine-Tuning Guide

## Do you need fine-tuning at all?

Not always.

Start with prompt-only grounding if:

- your hard-fact schema is tiny
- the domain language is clean
- the transcript quality is stable
- the cost and latency of a larger model are acceptable

Fine-tune an SLM when:

- the same hard facts repeat across many conversations
- transcripts are noisy, fragmented, or domain-specific
- you need low latency and high consistency
- the LLM is spending too much effort repeating state-tracking work
- prompt-only extraction works sometimes but not reliably enough

## What to fine-tune

Fine-tune the **background grounding model**, not the main conversational model first.

Best first target:

- a small/medium decoder or structured-output model that updates the hard-fact ledger

Why:

- it is bounded
- it has a narrow job
- it is easier to evaluate than “overall conversation quality”

Do not start by fine-tuning the front-facing LLM for tone and empathy unless you have a very strong reason.

## What the SLM should learn

The SLM should learn:

- explicit fact extraction
- carry-forward from prior facts
- correction handling
- candidate vs confirmed discipline
- when a clue is meaningful enough to count as a candidate

The SLM should not be trained to do:

- empathy
- safety coaching tone
- general reasoning
- policy essays
- full conversation planning

## Best training target

Train the SLM to produce a strict **fact-ledger delta** or **merged hard-facts object**.

Good target shape:

- location/entity candidate
- candidate kind
- issue cues
- key binary states
- count if explicit
- optional note

Bad target shape:

- full agent answer
- long rationale
- severity essay
- “what the assistant should say next” in natural language

## Data strategy

Use three sources:

### 1. Human-real transcripts

These are the most important.

You need:

- noisy turns
- partial turns
- corrections
- low-information turns
- multi-turn carry-forward

### 2. Synthetic data

Use synthetic data to broaden coverage, not to replace real data.

Synthetic data is best for:

- rare but important patterns
- schema coverage
- spelling and wording variants
- explicit contradiction cases
- place/entity formatting variants

### 3. Replay-derived hard cases

Take failure cases from real conversations and turn them into targeted training rows.

This is often the highest ROI dataset slice.

## Training strategy

### Strategy A: narrow first-pass fact ledger

Train one model to output only hard facts.

Best for:

- first deployment
- smallest latency overhead
- simplest evaluation

### Strategy B: fact ledger + candidate strength

Add fields like:

- `candidate_only`
- `needs_confirmation`
- `location_kind`
- `search_allowed_hint`

Best for:

- tool gating
- map lookup gating
- entity resolution confirmation loops

### Strategy C: domain-specific variants

Keep the base ledger structure the same, but swap:

- issue cue vocab
- binary states
- confirmation ladders

Best for:

- multi-vertical reuse

## Synthetic data guidance

Use synthetic data for breadth, but make it realistic.

Include:

- STT-like misspellings
- fragmented answers
- bare confirmations next to known question targets
- corrections like `actually`, `no`, `sorry`
- vague cues that should stay vague
- semantically close but wrong candidates

Avoid:

- fully polished text only
- one-shot perfect user answers
- training the model to always over-extract

## Fine-tuning anti-patterns

### Training the SLM to be the whole assistant

This leads to:

- overlap with the LLM
- prompt bloat
- harder evaluation

### Training only on clean canonical sentences

This produces a model that fails on:

- live audio turns
- corrections
- fragmented utterances

### Treating synthetic data as truth

If the synthetic generator overstates certainty, the SLM will too.

### Mixing confirmed facts and guesses in labels

This destroys the exact value of the ledger.

## Evaluation strategy

Measure:

- schema validity
- exact-field precision and recall
- carry-forward accuracy
- correction accuracy
- candidate-vs-confirmed discipline
- false-positive tool-open rate

Also measure system-level impact:

- reduction in repeated questions
- faster time to meaningful candidate
- fewer premature tool side effects

## Practical training loop

1. Define the narrow ledger schema.
2. Build 100-200 gold examples from real transcripts.
3. Add synthetic coverage for missed edge cases.
4. Fine-tune the SLM.
5. Evaluate on real replay sessions.
6. Add failure-driven data.
7. Repeat.

## When to fine-tune the LLM

Only after the grounding layer is working well.

Fine-tune the LLM only if you have a strong need for:

- domain-specific spoken style
- special phrasing constraints
- specialized recovery behavior

Even then, keep the hard-fact job outside it if possible.
