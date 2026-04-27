# Merge Rules

## Goals

Merges should be conservative and monotonic when possible.

You want the ledger to get better over time, not oscillate.

## Recommended rules

### 1. Carry forward by default

If the new SLM pass does not explicitly change a field, keep the old field.

### 2. Do not erase with emptiness

If a new pass returns `null`, `unknown`, or empty arrays for a field that was previously meaningful, do not wipe the stronger prior value unless the user clearly corrected it.

### 3. Separate confirmed from guessed

Never let soft guesses overwrite confirmed hard facts.

### 4. Require explicit correction for destructive updates

Examples:

- `no bleeding` may flip `bleeding_status`
- `actually we are three` may replace `count_confirmed`

But a weak new pass should not erase a previously confirmed field silently.

### 5. Lock confirmed candidates

Once the user confirms a candidate:

- copy it into the confirmed field
- mark the gate as confirmed
- ignore later weaker candidates unless the caller explicitly corrects the location/entity

### 6. Tool outputs are not user confirmations

Tool results may create candidates.
They should not silently become confirmed fields unless your domain explicitly allows exact deterministic matches.
