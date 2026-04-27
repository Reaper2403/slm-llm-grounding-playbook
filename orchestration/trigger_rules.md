# Trigger Rules

## Why triggers matter

If you run the SLM too often, you lose latency and stability.
If you run it too rarely, the ledger goes stale.

## Recommended trigger policy

Run the SLM:

- every 2-3 substantive user turns
- immediately on high-signal turns
- immediately on semantic corrections

## High-signal turns

Examples:

- explicit location clues
- explicit entity IDs
- `gun`
- `not breathing`
- `bleeding`
- `fire`
- `trapped`
- `account is 48217`
- `order number is AX-93`

## Semantic corrections

Examples:

- `actually it is Donau Strasse`
- `no bleeding`
- `not trapped`
- `sorry, there are two people`

## Do not trigger on trivial shards

Examples:

- `yes`
- `no`
- `okay`
- `hello`
- `hmm`
- `uh`

Special rule:

- bare `yes/no` should not trigger a standalone SLM run
- if possible, attach it to the active runtime question target and let the next bundled SLM pass see it in context
