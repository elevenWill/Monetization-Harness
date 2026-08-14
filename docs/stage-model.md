# Stage model

Stage describes the next uncertainty to resolve, not how polished the artifact looks. It is evidence-driven and reversible. The `stage` field in `STATE.md` is the authoritative current value; directory presence is only historical evidence that material was once recorded there.

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

Do not infer Stage from directory names and do not create a directory merely because a Project enters that Stage. Stage directories materialize only when a real artifact is written, may be non-contiguous, and may remain after the current Stage moves forward or backward.

## Market Reality Gate is not a Stage

The Market Reality Gate is a pre-lens routing and evidence-freshness check. It decides whether the immediate judgment needs current external research; it is not a ninth Stage, a Stage transition, or a replacement for `next_gate`.

Store a resulting `Rxxx` under the `research/` directory of the Stage whose question it informs, and a reusable `Cxxx` under that Stage's `cases/` directory. Those directories remain historical material and do not determine the current Stage. Completing research or finding an exact/adjacent precedent does not advance the project by itself.

External research can establish scoped facts such as market existence, current platform policy, competitors, price signals, or a precedent's reported outcome. It cannot establish that the same result transfers to this project. Stage determination therefore continues to prioritize the project's own transactions, observed behavior, usage, repeat customers, and other linked entry evidence. Advance only when the table's entry evidence is actually met; otherwise use the research to refine an ASSUMPTION, risk, experiment, or next action.

## Why-Now Gate is not a Stage

The Why-Now Gate is a cross-stage purchase-timing and Buying-Situation check. It asks what real event moves a buyer to seek and pay for a result inside a concrete window, what delay costs, who bears the consequence, whether the payer is reachable, what trust is required, and whether delivery liability is bounded. It is not a tenth Stage, a Stage transition, a Persona, or a replacement for `next_gate`.

Store a decision-relevant `BSxxx` under the `buying-situations/` directory of the Stage whose decision it informs. One Project can have multiple Buying Situations in different Stages. Creating or evidencing a `BSxxx` does not advance the Project by itself; payment, repeatability, and the other Stage entry evidence in the table still control transitions. A business without a deadline may advance when its actual recurrence, behavior, transaction, and economics evidence meets those gates.

## Stage transition record

When the transition needs a durable history artifact, write it in the relevant stage directory (creating only the directory that will immediately contain that artifact), then summarize it in `STATE.md`:

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
