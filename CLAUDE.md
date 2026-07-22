# Review standards for this repo

   When reviewing a PR, focus on:
   - Input validation and error handling on all external inputs
   - Structured logging (no bare prints) for Cloud Functions
   - No secrets or credentials in code
   - Idempotency and safe retries for functions triggered by events
   - Clear, actionable comments — cite the line and suggest a fix

   Keep the review concise. Group findings by severity: Blocking / Should-fix / Nit.