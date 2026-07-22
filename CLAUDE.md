# Review standards for this repo
When reviewing a PR, focus on:
- Input validation and error handling on all external inputs
- Structured logging (no bare prints) for Cloud Functions
- No secrets or credentials in code
- Idempotency and safe retries for event-triggered functions
- Clear, actionable comments — cite the line and suggest a fix
Group findings by severity: Blocking / Should-fix / Nit. Be concise.
