# Stage model

Stage describes the next uncertainty to resolve, not how polished the artifact looks. It is evidence-driven and reversible. The `stage` field in `STATE.md` is the authoritative current value; directory presence is only historical evidence that material was once recorded there.

| Stage | Entry evidence | Primary question | Typical next gate | Regression signal |
| --- | --- | --- | --- | --- |
| `opportunity_discovery` | No clear participant/audience and repeated value pattern | Which same-level reality-grounded value or monetization pattern is worth investigating, and which tools/topics/formats/channels are only components of it? | `defined_problem_and_customer` | Candidate remains model-, trend-, technology-, or vanity-metric-led, or mixed-level components are ranked as business directions |
| `problem_validation` | A participant/audience plus problem or desired-value hypothesis exists | Does the claimed problem, desired value, or consumption pattern occur and matter in observed reality? | `problem_evidence` | Observation or behavior contradicts the participant/value definition |
| `business_validation` | Problem evidence exists | Who pays, for what result, why now, and versus what alternative? | `credible_offer` | Buyer, value, or payment logic becomes unclear |
| `experiment_validation` | A falsifiable offer or assumption exists | Which safe test produces the most decision-changing information relative to total downside? | `transaction_attempt` | Experiment tests interest, not the key assumption or income path |
| `transaction_validation` | At least one real payment exists | Can the payment and delivery be repeated? | `repeat_payment` | First transaction proves exceptional or non-repeatable |
| `leverage_discovery` | Repeated purchase or repeated valued delivery exists | Which repeated work can become an SOP or reusable asset? | `repeatable_delivery_system` | Automation reduces the value or repeatability disappears |
| `productization` | Repeatable delivery and a bounded scope exist | What minimum product preserves the proven result? | `repeatable_product_value` | Product users do not repeat or pay; return to business validation |
| `scaling` | Repeatable value, delivery, and plausible economics exist | Which acquisition and operating system can grow without hidden ruin? | `sustainable_growth` | Economics, retention, quality, or dependency breaks |

`defined_problem_and_customer` and `problem_evidence` remain stable compatibility
gate IDs. For content/media, entertainment, education, identity, information, or
other non-pain businesses, read them as a defined audience plus repeated value or
consumption hypothesis, followed by observed evidence that the pattern occurs.
Do not force the pattern into a service problem, and keep its payer and
monetization bridge `unknown` until evidence supports them.

During Opportunity comparison, first distinguish business or monetization
structures from their components: tool/capability, topic, format, channel,
audience, value mechanism, and offer. Normalize Candidates to the decision level
the user's question requires; do not rank mixed-level components. Preserve an
explicit user-committed archetype constraint, while treating tentative archetype
preference as an ASSUMPTION rather than Stage evidence.

## Stage determination

1. Start from transactions, repeat customers, observed behavior, and linked evidence in `STATE.md`.
2. Select the earliest unresolved gate. Do not infer stage from code, a launch, or the user's confidence.
3. Record a transition only when the entry evidence changes.
4. When evidence invalidates an earlier gate, move backward to the earliest invalidated stage and record why.

An incomplete user report of one or many payments remains useful FACT evidence
and routes to `transaction_validation` for bounded verification. It does not
satisfy completed Transaction evidence or the Leverage entry gate until the
minimum auditable Transaction fields and comparable delivery evidence are
verified.

Do not infer Stage from directory names and do not create a directory merely because a Project enters that Stage. Stage directories materialize only when a real artifact is written, may be non-contiguous, and may remain after the current Stage moves forward or backward.

## Market Reality Gate is not a Stage

The Runtime first selects safe Reality Evidence by decision-changing information relative to total downside, then prefers the cheapest route among evidence paths capable of changing the immediate decision: reuse fresh evidence, seek the project's own observation/behavior/payment/delivery evidence, or use the Market Reality Gate when current external facts are decision-critical. Founder attention and opportunity cost are part of downside. The Gate checks whether external research is needed and fresh enough; it is not the whole reality loop, a ninth Stage, a Stage transition, or a replacement for `next_gate`. A newly bootstrapped public-market project does not require research by status alone, and existing auditable payment or delivery evidence does not require a new revenue-model landscape unless that structure is the active uncertainty.

Store a resulting `Rxxx` under the `research/` directory of the Stage whose question it informs, and a reusable `Cxxx` under that Stage's `cases/` directory. Those directories remain historical material and do not determine the current Stage. Completing research or finding an exact/adjacent precedent does not advance the project by itself.

External research can establish scoped facts such as market existence, current platform policy, competitors, price signals, or a precedent's reported outcome. It cannot establish that the same result transfers to this project. Stage determination therefore continues to prioritize the project's own transactions, observed behavior, usage, repeat customers, and other linked entry evidence. Advance only when the table's entry evidence is actually met; otherwise use the research to refine an ASSUMPTION, risk, experiment, or next action.

## Why-Now Gate is not a Stage

The Why-Now Gate is a conditional purchase-timing and Buying-Situation check available across Stages. Run it fully when purchase timing is material to the earliest uncertainty: normally in `business_validation`, or when a concrete Buying Situation, trigger/deadline claim, purchase-window qualification, Deadline Replication Experiment, or deadline-shaped SLA/liability decision controls the action. `opportunity_discovery` otherwise uses only a light trigger-mechanism scan. The full Gate asks what real event moves a buyer to seek and pay for a result inside a concrete window, what delay costs, who bears the consequence, whether the payer is reachable, what trust is required, and whether delivery liability is bounded. It is not a tenth Stage, a universal step, a Stage transition, a Persona, or a replacement for `next_gate`.

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
