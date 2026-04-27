# Example: Customer Support

## High-value facts

- account identity
- issue type
- urgency
- what the user has already tried
- whether there is a production outage or billing impact

## Useful split

- **LLM**: empathy, de-escalation, adaptive troubleshooting
- **SLM**: account clues, product area, explicit errors, prior attempts
- **Tools**: CRM lookup, status pages, ticket creation

## Why not just prompt harder

Because long support chats drift:

- the LLM repeats verification
- the user gets annoyed
- tools are called too early or too late

The ledger keeps identity and issue state stable while the LLM remains friendly.
