---
name: business-filter
description: Determine whether an opportunity and concrete Buying Situation form a real, purchasable, potentially durable business by identifying the trigger, deadline reality, cost of delay, consequence owner, customer, payer, purchased result, trust, reachability, liability, alternatives, revenue logic, and recurrence. Use when a problem and customer are partly defined, at the Why-Now Gate, before or after a first payment, when evaluating an offer or pricing, or when deciding whether one transaction can repeat. Do not treat popularity, anxiety, user praise, or product quality alone as a business.
---

# Business Filter

Answer “is this actually a business worth further investigation?” before optimizing execution.

## Load context

1. Read the active project's `IDEA.md` and `STATE.md` completely.
2. Read linked customer, alternatives, pricing, transaction, and experiment evidence relevant to the current gate.
3. Read the latest in-scope `Rxxx` and relevant `Cxxx`: exact cases, payer and
   bought result, competitor/alternative pricing, negative cases, current policy
   constraints, source verification, and transferability limits. Do not silently
   substitute an adjacent case for the target model.
4. Read the active `BSxxx` and `docs/purchase-trigger-protocol.md` when a concrete Buying Situation exists. Missing fields remain `unknown`; do not complete them from intuition.
5. Read [references/domain-core.md](references/domain-core.md). Apply only the
   entry-matched Signature Decision Operators; do not run them as a generic
   checklist. If they do not change the provisional judgment, record
   `decision_delta: none`.
6. Use [examples/local/monetization-cases.md](examples/local/monetization-cases.md) for first-payment and pseudo-demand patterns. Consult the source snapshot through [SOURCE.md](SOURCE.md) only when deeper provenance is useful.

If the verdict depends on current market, price, competitor, or policy facts and
the linked research is absent, stale, or out of scope, return the evidence gap to
the orchestrator for the Market Reality Gate. Do not fill it with model knowledge.

## Workflow

1. Use a concrete Buying Situation as the unit of analysis, not the abstract Project. Identify only archetype-relevant roles and do not assume they are the same: normally user, beneficiary, buyer, budget owner, payer, and consequence owner; for content/media, consider audience/consumer/subscriber, operator/creator, advertiser/sponsor/merchant/platform when relevant.
2. Preserve an explicit current business-archetype commitment; treat a tentative
   preference as an ASSUMPTION that may be compared with alternatives. Describe
   the value or result without product features. For content/media, trace the
   audience value/attention flow separately from the payer, paid result, and money
   flow, and allow entertainment, identity, information, education, or decision
   support without rewriting it as a service problem.
3. Apply the entry-matched source-derived operator before completing the business
   audit. Then audit Trigger Event, Deadline Reality and source, Cost of Delay and
   certainty, Purchase Window, Budget Path, Trust Barrier, Low-Trust Entry,
   Reachability, Frequency, and Delivery Liability. A preferred date, anxiety,
   or a seller countdown is insufficient. Pre-replication transferability and
   readiness remain an orchestrator hard gate rather than a Lens contribution.
4. Compare current alternatives using project and external evidence: internal
   labor, spreadsheet, agency, incumbent software, delay, or no action. Include
   observed price and switching cost while retaining source freshness and scope.
5. Trace money: price, frequency, delivery cost, refund/quality risk, acquisition path, and dependency. Mark unknowns explicitly. GMV, traffic, likes, or a vendor claim are not profit or durable demand.
6. Examine recurrence and durability: does the triggering situation repeat, can the same customer buy again, can another independent customer buy, and do synchronized deadlines create an operational peak rather than scalable demand?
7. Compare positive precedent with failure cases, complaints, policy limits, and
   the resources the apparent winner uniquely possesses.
8. Apply a competence check: separate what is understood from what requires domain or market evidence.
9. Classify the purchase mechanism as exactly one primary outcome: `real_urgent_buying_situation`, `urgent_but_low_trust`, `deadline_without_consequence`, `high_value_but_unreachable`, `one_off_rush_service`, `recurring_deadline_opportunity`, `recurring_non_deadline_purchase`, `manufactured_urgency`, `high_liability_opportunity`, or `no_clear_why_now`. Use `recurring_non_deadline_purchase` only when observed repeat payment/usage, a persistent value mechanism, reachable payer, and plausible economics support purchase without a deadline. Do not combine outcomes into a numeric score or manufacture urgency to avoid `no_clear_why_now`.
10. Choose `continue`, `continue_with_conditions`, `pause`, or `reject_for_now`; name the missing evidence that would change the result.

## Transaction interpretation

- Zero payments: assess whether the offer is coherent enough to test; do not call it a business.
- One payment: FACT for one buyer and one transaction only. Test independence and repeatability.
- Repeat purchases: stronger evidence, but still inspect discounts, founder relationships, exceptional customization, margins, and retention cause.

## Guardrails

- Do not confuse total addressable market with reachable revenue.
- Do not silently convert a content/media opportunity into consulting, a tool,
  or a service because that path is easier to price. Treat it as a separate
  monetization hypothesis and keep its payer/result evidence scoped.
- Do not count compliments, signups, or stated intent as payment.
- Do not recommend productization merely because one transaction exists.
- Do not use investment/stock-picking advice or imitate Duan Yongping.
- Do not claim ten-year durability without explaining the mechanism and uncertainty.
- Do not equate a deadline with commercial value unless consequence, budget, reachability, trust, and feasible delivery align.
- Do not reject a business only because it lacks a deadline; inspect other supported repeat-purchase mechanisms.
- Never recommend fabricated scarcity or a deceptive deadline.
- External precedent proves at most that a market structure existed in its
  recorded scope. Only the user's own payment and delivery experiments can
  establish that it transfers to this project.

## Output

Return one review under `docs/review-protocol.md`. `finding` must name the primary Buying Situation outcome and the business verdict with its condition. `recommended_action` must target the most important missing part of trigger/consequence/payer/trust/reachability/value/alternative/recurrence evidence.

Pair with `experiment-designer` to convert the missing evidence into a cash- or behavior-based test. Pair with `leverage-designer` only after repeated value exists.
