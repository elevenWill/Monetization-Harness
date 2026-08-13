---
name: experiment-designer
description: Turn an unverified monetization assumption into the cheapest, fastest, reversible real-world experiment with capped downside, explicit ruin checks, behavioral or payment evidence, success and failure criteria, and a stop condition. Use before large builds or commitments, whenever transactions are zero and development is proposed, for resignation/all-in/major-spend decisions, or whenever a project depends on one customer, platform, API, or irreversible bet.
---

# Experiment Designer

Protect the ability to keep trying while obtaining stronger evidence quickly.

## Load context

1. Read the active project's `IDEA.md` and `STATE.md` completely.
2. Read active assumptions, planned/running experiments, and relevant transaction evidence.
3. Read [references/domain-core.md](references/domain-core.md).
4. Consult [examples/local/monetization-cases.md](examples/local/monetization-cases.md) for standard experiment patterns. Use [SOURCE.md](SOURCE.md) for deeper source context.

## Workflow

1. Name the single decision-changing assumption. Reject experiments that test several unrelated uncertainties.
2. Define the desired evidence before designing activity. Prefer cash, costly commitment, observed behavior, or real usage.
3. Run a ruin check: maximum money/time/reputation/legal/privacy loss, irreversibility, concentration, and what happens after failure.
4. Remove unnecessary components via subtraction. Consider direct offer, pre-sale, paid discovery, concierge, Wizard of Oz, manual delivery, narrow prototype, or reversible smoke test.
5. Preserve upside: choose a test that can reveal unexpected demand or learning while the loss remains capped.
6. Write success, failure, invalid-result, deadline, budget, and stop criteria. A result must update a named assumption or decision.
7. Specify evidence capture and the next review point. Do not declare a stage transition in advance.

## Hard rules

- Any resignation, all-in bet, multi-month build, major spend, long contract, large procurement, or single dependency requires an explicit smaller-alternative comparison.
- If `transactions.total == 0`, prefer a real offer before a full product unless a small technical artifact is strictly necessary for the buyer to evaluate the result.
- A survey asking “would you pay?” does not validate payment willingness.
- Never expose users to deceptive, unlawful, unsafe, privacy-violating, or financially harmful tests.

## Experiment record

Use the `E001` schema in `docs/object-protocol.md`. The downside cap and stop condition are required. Link evidence after completion and update the tested assumption status.

## Output

Return one review under `docs/review-protocol.md`. `reasoning_summary` must compare the proposed action's downside/evidence to the smaller test. `recommended_action` should be executable within a clear time, count, and budget.

Coordinate with `assumption-challenger` for wrong-question/build-avoidance cases and `business-filter` when the missing evidence concerns payer, price, or repeatability.
