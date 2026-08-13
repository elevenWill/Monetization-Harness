# Decision object protocol

## Types and IDs

| Type | ID | Meaning | Required evidence/status |
| --- | --- | --- | --- |
| Opportunity | `O001` | A candidate worth investigating | Origin and reason to inspect |
| Fact | `F001` | Something that happened or was directly observed | Source/evidence and observed date |
| Assumption | `A001` | A belief not yet supported strongly enough | Status and validation plan |
| Decision | `D001` | A chosen action or constraint | Basis, owner/date, revisit condition |
| Experiment | `E001` | A bounded test of named assumptions | Cost cap, success/failure criteria, deadline |
| Transaction | `T001` | Actual exchange of money | Amount/currency/date/payer evidence; link from a Fact |

IDs are unique and permanent inside one project. Allocate the next unused integer by searching the entire project. A moved object keeps its ID.

## FACT

A FACT must be falsifiable, source-linked, and phrased without interpretation.

```markdown
### F001 — One paid manual delivery

- Observed: 2026-08-13
- Evidence: [payment record](../05-transactions/evidence/T001-redacted.md)
- Statement: Customer A paid CNY 500 for one case-file organization delivery.
```

Do not write “customers value this” from one payment. That remains an assumption.

## ASSUMPTION

Use status `untested`, `testing`, `supported`, `weakened`, or `invalidated`. “Supported” is not permanent truth.

```markdown
### A001 — Other lawyers will pay CNY 500

- Status: testing
- Basis: F001
- Tested by: E001
- Disconfirming result: fewer than 2 independent payments after 10 qualified offers
```

## DECISION

Draft choices use `DRAFT-D001` only in `STATE.md`; allocate `D001` when the user commits. Record which facts and assumptions support it.

## EXPERIMENT

```markdown
### E001 — Replicate paid case-file organization

- Tests: A001
- Offer: Deliver the same result manually for CNY 500
- Audience: 10 qualified lawyers not connected to Customer A
- Maximum downside: 7 days and CNY 300
- Success: at least 2 independent real payments
- Failure: 10 qualified offers and 0 payments
- Deadline: 2026-08-20
- Stop conditions: cost cap, deadline, or any legal/privacy breach risk
```

Do not use likes, compliments, surveys, or model opinions as substitutes for the behavior named in the success criterion.

## TRANSACTION

Redact personal/payment secrets. Record enough evidence to distinguish paid, refunded, discounted, barter, or promised transactions. `transactions.total` counts completed monetary transactions; `repeat_customers` counts customers who completed more than one transaction.

## Updating state

Store detailed objects in the relevant stage directory. Keep only active or decision-critical summaries and links in `STATE.md`. When an assumption changes status or a decision is reversed, preserve the original record and add the new evidence and date.
