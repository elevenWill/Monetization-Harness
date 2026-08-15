---
name: experiment-designer
description: Turn an unverified monetization or Purchase Trigger assumption into a reversible real-world experiment with high decision information per total downside, explicit ruin checks, behavioral or payment evidence, success and failure criteria, and a stop condition. Use before large builds or commitments, for Deadline Replication Experiments inside real purchase windows, whenever transactions are zero and development is proposed, for resignation/all-in/major-spend decisions, or whenever a project depends on one customer, platform, API, or irreversible bet.
---

# Experiment Designer

Protect the ability to keep trying while obtaining stronger evidence quickly.

## Load context

1. Read the active project's `IDEA.md` and `STATE.md` completely.
2. Read active assumptions, planned/running experiments, and relevant transaction evidence.
3. Read the latest in-scope `Rxxx` plus any reusable `Cxxx`, including the case's
   verification status, transaction mechanism, negative evidence, policy
   constraints, required resources, and transferability analysis.
4. Read the referenced `BSxxx` when trigger timing is material; preserve its deadline source, cost of delay, purchase window, trust barrier, and delivery liability.
5. Read [references/domain-core.md](references/domain-core.md).
6. Consult [examples/local/monetization-cases.md](examples/local/monetization-cases.md) for standard experiment patterns. Use [SOURCE.md](SOURCE.md) for deeper source context.

## Workflow

1. Name the single decision-changing assumption. Reject experiments that test several unrelated uncertainties.
2. Define the desired evidence before designing activity. State what success and
   failure would change and how the result distinguishes live hypotheses. Prefer
   cash, costly commitment, observed behavior, or real usage.
3. Run a ruin check: maximum money/time/reputation/legal/privacy loss,
   irreversibility, concentration, and what happens after failure. Count founder
   attention and foregone alternatives as real costs even when cash spend is low.
4. Prefer a **Replication Experiment** when a sufficiently relevant case exists:
   reproduce the smallest verified transaction or delivery mechanism rather than
   inventing a more complex product. Link the real `Cxxx`; never invent a case ID.
5. State which mechanism from `Cxxx` is copied, which unique resources are not
   copied, and the single transfer assumption being tested. If only adjacent
   evidence exists, label the experiment as an adjacency-transfer test rather
   than replication of an exact precedent.
6. Compare the test's decision information with a smaller alternative, then
   remove unnecessary components via subtraction. Consider direct offer, pre-sale,
   paid discovery, concierge, Wizard of Oz, manual delivery, narrow prototype, or
   reversible smoke test. Cheap is a denominator, not the objective: first require
   enough information to change the current decision, then minimize total downside.
7. Prefer a **Deadline Replication Experiment** when a real Buying Situation can be observed. Record the referenced `BSxxx`, real Trigger Event, real Deadline, Purchase Window, copied transaction structure, maximum input, maximum delivery liability, and Low-Trust Entry. Make the offer while the trigger is actually present; do not ask only whether the buyer would hypothetically pay.
8. Preserve upside: choose a test that can reveal unexpected demand or learning while the loss remains capped.
9. Predeclare `success`, `demand_failure`, and `invalid` thresholds, plus the deadline, experiment cap, claim-level total evidence budget, maximum repair reviews, and stop criteria. `inconclusive` is the fallback when a validly interpretable result crosses neither success nor demand-failure thresholds. Repeated invalid/inconclusive repairs consume the shared claim budget rather than resetting it. Stop when that budget is exhausted, quality cannot be assured, protected/core access is required, or liability exceeds the cap.
10. Treat several hours or days, repeated production/publication, meaningful
    manual delivery, or material reputation/opportunity cost as a material action.
    When the project explicitly seeks income, such an experiment must reduce a
    named unknown in the commercial bridge. If success would show only audience
    interest while leaving the money path unchanged, shrink it to a single
    low-cost reversible micro probe or choose a more discriminating test. Unknown
    monetization does not block a micro probe with useful scoped learning.
11. Select only the observable evidence-path steps needed for this scenario and set the minimum exposure at decision-critical steps. A demand test must separate qualified buyer, offer exposure, price exposure, and the target behavior; it must not treat message count as offer exposure.
12. Specify privacy-safe raw evidence capture and the next review point. Reason codes may summarize linked raw words or behavior but may not replace them. Do not declare a Stage transition in advance.
13. After completion, apply the classification precedence and Evidence Ledger in `docs/object-protocol.md`: rule out `invalid`, then test `success`, then the strict `demand_failure` gate, otherwise use `inconclusive`. Diagnose the first broken selected step and the first evidence-supported layer; use `unknown` when causes remain confounded.
14. When the experiment defers implementation, state `implementation_revisit_trigger`: the evidence that would make the smallest technical artifact necessary for valid exposure or a measured repeated-delivery bottleneck. Do not use “after validation” as an unspecified unlock.
15. Feed the result back into the named ASSUMPTION, evidence-backed FACTS, any user-committed DECISION, the active Buying Situation when trigger timing was tested, and the next experiment. Recompute Stage from its entry evidence rather than from the result code.

## Hard rules

- Any resignation, all-in bet, multi-month build, major spend, long contract, large procurement, or single dependency requires an explicit smaller-alternative comparison.
- If `transactions.total == 0`, prefer a real offer before a full product unless a small technical artifact is strictly necessary for the buyer to evaluate the result.
- A survey asking “would you pay?” does not validate payment willingness.
- Never classify `demand_failure` unless the predeclared qualified intended-buyer minimum actually received and understood the real offer and real price, the decision window elapsed, and no material protocol defect explains the result.
- Silence is not a reason code. Preserve linked raw evidence and state competing explanations instead of inferring price, urgency, trust, or problem absence from a count alone.
- Never expose users to deceptive, unlawful, unsafe, privacy-violating, or financially harmful tests.
- Never create a false deadline, false inventory, deceptive countdown, or fabricated urgency as an experiment mechanism.
- Refresh time-sensitive policy evidence before a platform-facing test when the
  linked research is stale or incomplete; do not test by risking an account ban.

## Experiment record

Use the `E001` schema in `docs/object-protocol.md`. Follow its material-action
Decision Information fields rather than duplicating their definitions here. The
downside cap, selected evidence path, predeclared outcome thresholds, deadline,
and stop condition are required. For a Replication Experiment, also record
`reference_case: Cxxx`, `copied_mechanism`, `resources_not_copied`, and
`transfer_assumption`. For a Deadline Replication Experiment, also record
`reference_buying_situation: BSxxx`, `real_trigger`, `real_deadline`,
`purchase_window`, `copied_transaction_structure`,
`maximum_delivery_liability`, and `low_trust_entry`.

After completion, append the result and aggregate Evidence Ledger to the same `Exxx`; do not create a result ID, lead table, or CRM artifact. Use exactly one of `success`, `demand_failure`, `invalid`, or `inconclusive`, link raw evidence, record supported reason codes, diagnose the first broken step/layer, and state the feedback to assumptions, facts, decisions, Stage review, and next test. Plan-only historical artifacts remain valid until a completed/result section is added.

## Output

Return one review under `docs/review-protocol.md`. `reasoning_summary` must compare
the proposed action's decision information and total downside with the smaller
test. `recommended_action` should be executable within a clear time, count, and
budget.

Coordinate with `assumption-challenger` for wrong-question/build-avoidance cases and `business-filter` when the missing evidence concerns payer, price, or repeatability.
