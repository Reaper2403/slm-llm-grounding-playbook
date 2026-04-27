# Evaluation

## Measure the system, not only the model

### Latency

- first-response latency
- time-to-next-question after user turn
- background SLM turnaround

### Grounding quality

- hard-fact precision
- hard-fact carry-forward accuracy
- contradiction update accuracy
- candidate confirmation rate

### Conversation quality

- repeated-question rate
- stacked-question rate
- interruption rate
- recovery quality after noisy turns

### Tool quality

- tool gate precision
- false-positive side effects
- percent of lookups done before confirmation
- percent of correct candidates confirmed

## Suggested replay harness

For each saved conversation:

1. replay transcript turns through the scheduler
2. record ledger versions
3. record prompt packets
4. record candidate and confirmation flows
5. compare final hard facts against annotated truth
