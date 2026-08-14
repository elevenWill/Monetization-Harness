# Policy Conflict

## Scenario

An old creator tutorial says AI avatars are permitted without disclosure. A newer official platform rule requires labeling some synthetic content, while a regional help page uses different wording. The user plans to publish next week.

## Correct workflow

1. Reopen current official rules; do not rely on the stored summary or search snippet.
2. Record platform, region, exact content type, publication/effective dates, `checked_at`, official URL, and status for each applicable rule.
3. Compare rule hierarchy, locale, content scope, effective date, and whether one source supersedes another.
4. Treat the old tutorial as stale or superseded context, not current policy authority.
5. Preserve unresolved conflicts and choose `policy_conditional` or `research_blocked` if they prevent safe advice.
6. Update the time-qualified policy FACT only after resolving what the official source actually says.

## Example records

```yaml
current_rule:
  authority: official
  verification: directly_observed
  freshness: current
  scope_match: exact
  direction: neutral
old_tutorial:
  authority: user_generated
  verification: single_source_reported
  freshness: stale
  scope_match: adjacent
  direction: contradicts
```

Policy FACT shape:

```text
As checked on <date>, <platform>'s official rule for <region> and <content_type> states <narrow requirement>, subject to <conditions>. Official URL: <url>.
```

## Failure modes

- Reusing last year's policy because it remains in `STATE.md`.
- Taking a vendor compliance blog over a current official rule.
- Omitting region or content type.
- Saying “allowed” when the rule is conditional on disclosure, account status, category, or claims.
