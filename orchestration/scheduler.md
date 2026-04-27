# Scheduler

## Target behavior

The assistant should keep talking while the SLM works in the background.

## Reference loop

1. User turn arrives.
2. Runtime stores transcript fragment.
3. Runtime decides whether this turn should schedule the SLM.
4. If yes:
   - if no SLM job is running, queue one
   - if a job is already running, mark the session `dirty`
5. LLM responds immediately from the last committed prompt packet.
6. SLM finishes and updates the hard-fact ledger.
7. Runtime recomputes:
   - prompt packet
   - tool gate
   - follow-up/confirmation state
8. If the session was marked `dirty`, run the SLM once more on the newest snapshot.

## Important implementation detail

The queued SLM job should read a compact reconstructed turn window, not a raw event stream of tiny audio fragments.

## Suggested runtime state

- `running`: whether an SLM job is in progress
- `dirty`: whether new relevant user content arrived during the current job
- `last_user_turn_count`: last substantive turn index processed

## Performance guidance

- keep local matching cheap
- cache static lexicons in memory
- keep network lookup off the first-response path
- recompute the prompt packet only after ledger changes
