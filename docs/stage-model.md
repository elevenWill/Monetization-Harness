# Stage model

Stage describes the next uncertainty to resolve, not how polished the artifact looks. It is evidence-driven and reversible.

| Stage | Entry evidence | Primary question | Typical next gate | Regression signal |
| --- | --- | --- | --- | --- |
| `opportunity_discovery` | No clear customer/problem pair | Where is a painful, repeated, already-tolerated problem? | `defined_problem_and_customer` | Candidate remains trend- or technology-led |
| `problem_validation` | A customer/problem hypothesis exists | Does this problem occur and matter in observed reality? | `problem_evidence` | Interviews/behavior contradict the problem definition |
| `business_validation` | Problem evidence exists | Who pays, for what result, why now, and versus what alternative? | `credible_offer` | Buyer, value, or payment logic becomes unclear |
| `experiment_validation` | A falsifiable offer or assumption exists | What is the cheapest safe test using real behavior? | `transaction_attempt` | Experiment tests interest, not the key assumption |
| `transaction_validation` | At least one real payment exists | Can the payment and delivery be repeated? | `repeat_payment` | First transaction proves exceptional or non-repeatable |
| `leverage_discovery` | Repeated purchase or repeated valued delivery exists | Which repeated work can become an SOP or reusable asset? | `repeatable_delivery_system` | Automation reduces the value or repeatability disappears |
| `productization` | Repeatable delivery and a bounded scope exist | What minimum product preserves the proven result? | `repeatable_product_value` | Product users do not repeat or pay; return to business validation |
| `scaling` | Repeatable value, delivery, and plausible economics exist | Which acquisition and operating system can grow without hidden ruin? | `sustainable_growth` | Economics, retention, quality, or dependency breaks |

## Stage determination

1. Start from transactions, repeat customers, observed behavior, and linked evidence in `STATE.md`.
2. Select the earliest unresolved gate. Do not infer stage from code, a launch, or the user's confidence.
3. Record a transition only when the entry evidence changes.
4. When evidence invalidates an earlier gate, move backward to the earliest invalidated stage and record why.

## Stage transition record

Write a durable transition in the relevant stage `analysis/` directory, then summarize it in `STATE.md`:

```yaml
from: productization
to: business_validation
date: 2026-08-13
trigger_facts:
  - F014
invalidated_assumptions:
  - A006
decision: D009
```

Never erase the earlier transition. A regression is new evidence, not failure of the state model.
