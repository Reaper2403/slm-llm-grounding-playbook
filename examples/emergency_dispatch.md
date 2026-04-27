# Example: Emergency Dispatch

## Why this pattern fits

The assistant must sound calm and natural, but certain facts dominate everything:

- where the caller is
- what kind of incident is happening
- whether anyone is bleeding, trapped, or not breathing
- how many people are involved

## Recommended split

- **LLM**
  - calm questioning
  - reassurance
  - conversational recovery
- **SLM**
  - location clues
  - issue cues
  - victim count
  - breathing / bleeding / trapped state
- **Tools**
  - address lookup
  - candidate pinning
  - nearby responders
  - handoff packet generation

## Example location ladder

1. Where are you right now?
2. Do you know the exact address?
3. You said `X`. Is that correct?
4. Please spell it slowly.
5. What is the nearest landmark and what do you see around you?

## Why the ledger matters

It prevents the LLM from:

- losing the location thread
- treating vague clues as confirmed addresses
- re-asking bleeding or breathing repeatedly
- dispatching off guesses
