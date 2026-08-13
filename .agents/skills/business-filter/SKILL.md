---
name: business-filter
description: Determine whether an opportunity is a real and potentially durable business by identifying the customer, payer, purchased result, payment timing, alternatives, revenue logic, recurrence, and reasons the offer may not hold. Use when a problem and customer are partly defined, before or after a first payment, when evaluating an offer or pricing, or when deciding whether one transaction can repeat. Do not treat popularity, user praise, or product quality alone as a business.
---

# Business Filter

Answer “is this actually a business worth further investigation?” before optimizing execution.

## Load context

1. Read the active project's `IDEA.md` and `STATE.md` completely.
2. Read linked customer, alternatives, pricing, transaction, and experiment evidence relevant to the current gate.
3. Read [references/domain-core.md](references/domain-core.md).
4. Use [examples/local/monetization-cases.md](examples/local/monetization-cases.md) for first-payment and pseudo-demand patterns. Consult the source snapshot through [SOURCE.md](SOURCE.md) only when deeper provenance is useful.

## Workflow

1. Identify the user, beneficiary, buyer, budget owner, and payer. Do not assume they are the same.
2. Describe the result being purchased without product features.
3. Record why the buyer pays now, what event triggers purchase, and what happens if they do nothing.
4. Compare current alternatives: internal labor, spreadsheet, agency, incumbent software, delay, or no action. Include switching cost.
5. Trace money: price, frequency, delivery cost, refund/quality risk, acquisition path, and dependency. Mark unknowns explicitly.
6. Examine recurrence and durability: does the triggering situation repeat, can the same customer buy again, and can another independent customer buy?
7. Apply a competence check: separate what is understood from what requires domain or market evidence.
8. Choose `continue`, `continue_with_conditions`, `pause`, or `reject_for_now`; name the missing evidence that would change the result.

## Transaction interpretation

- Zero payments: assess whether the offer is coherent enough to test; do not call it a business.
- One payment: FACT for one buyer and one transaction only. Test independence and repeatability.
- Repeat purchases: stronger evidence, but still inspect discounts, founder relationships, exceptional customization, margins, and retention cause.

## Guardrails

- Do not confuse total addressable market with reachable revenue.
- Do not count compliments, signups, or stated intent as payment.
- Do not recommend productization merely because one transaction exists.
- Do not use investment/stock-picking advice or imitate Duan Yongping.
- Do not claim ten-year durability without explaining the mechanism and uncertainty.

## Output

Return one review under `docs/review-protocol.md`. `finding` must state the business verdict and its condition. `recommended_action` must target the most important missing part of payer/value/alternative/recurrence evidence.

Pair with `experiment-designer` to convert the missing evidence into a cash- or behavior-based test. Pair with `leverage-designer` only after repeated value exists.
