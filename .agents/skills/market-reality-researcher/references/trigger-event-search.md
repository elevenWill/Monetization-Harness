# Trigger-Event Search

Use event-first search when the decision depends on why a buyer would act now. Search for an observed transition from a known problem to active workaround, procurement, outsourcing, or payment. A deadline claim is a hypothesis until its source, consequence, owner, and buying behavior are evidenced.

## Contents

- [Frame the buying event](#frame-the-buying-event)
- [Build event-first queries](#build-event-first-queries)
- [Search in evidence order](#search-in-evidence-order)
- [Separate buyer signals from seller urgency](#separate-buyer-signals-from-seller-urgency)
- [Capture auditable findings](#capture-auditable-findings)
- [Interpret missing evidence](#interpret-missing-evidence)

## Frame the buying event

Define the candidate chain before searching:

```text
Trigger event -> deadline or time window -> consequence of delay
-> consequence owner -> buyer / payer -> current workaround
-> purchase window -> trust requirement -> bought result
```

Fix the task, actor, geography, platform, and time period. State which link is unknown. Do not begin with the product name alone; the same product may serve different buying situations with different payers, consequences, prices, and recurrence.

## Build event-first queries

Combine terms from these families:

```text
task or product + event + deadline + consequence + purchase behavior
```

Not every query needs all five terms. Each query must test one link in the chain rather than restating the proposed solution.

Chinese query families:

```text
"<任务>" 加急 | 当天 | 24小时 | 来不及 | 截止 | 延期
"<任务>" 罚款 | 违约 | 客户流失 | 错过活动 | 库存积压
"<任务>" 活动前 | 上线前 | 上新 | 投标 | 月末 | 申报
"<任务>" 急招 | 代做 | 外包 | 采购 | 报价 | 加急费
"<角色>" 求助 "<事件>"
```

English query families:

```text
"<task>" urgent | deadline | same day | due tomorrow | last minute
"<task>" missed deadline | penalty | breach | lost sales | launch delay
"<task>" rush service | outsourcing | procurement | quote | emergency hire
"<role>" needs help before "<event>"
```

Add the exact event and actor once discovered: a named campaign, filing period, tender, launch, contract delivery, inventory window, or recurring operating cycle. Record actual queries in the `Rxxx` query log.

## Search in evidence order

1. Locate the event or time window in official calendars, rules, contracts, tenders, or first-party operating material.
2. Seek buyer-side behavior: urgent requests, procurement notices, outsourcing orders, paid rush work, emergency hiring, or repeated workaround use.
3. Identify the consequence and its owner through penalties, missed orders, SLA breaches, delayed launches, complaints, refunds, or documented extra labor.
4. Find the current workaround and whether it is used before the event rather than advertised after it.
5. Inspect quoted and transacted rush prices separately; a provider's surcharge proves an offer exists, not that buyers accept it.
6. Search delivery failures, late work, disputes, refunds, and liability to test whether urgency raises the trust barrier.
7. Search a control formulation without urgency terms to distinguish normal demand from deadline-specific behavior.

Read [deadline-signal-search.md](deadline-signal-search.md) to classify and verify the deadline source.

## Separate buyer signals from seller urgency

Label every trigger lead by origin:

| Origin | What it can support | What it cannot support alone |
| --- | --- | --- |
| Buyer, payer, or consequence owner | Active demand, workaround, budget path, or purchase window when the behavior is concrete | Population demand or repeatability from one post |
| Official event owner or regulator | The date, rule, eligibility, or external consequence | Willingness to buy a particular solution |
| Operator retrospective or customer record | A trigger-to-action sequence when dates and behavior are explicit | Independent truth when the account is promotional or uncorroborated |
| Provider rush listing or surcharge | Supply, offered SLA, and advertised price | Customer-native urgency, transacted price, or acceptance |
| Seller countdown, scarcity copy, or lead-generation page | That the seller used urgency language | A real buyer deadline or cost of delay |

Treat seller-created promotions as seller-created unless buyer-side evidence shows an independent event and consequence. Never convert a fabricated countdown or unverifiable scarcity claim into a recommended tactic.

## Capture auditable findings

Within the existing `Rxxx` schema, retain trigger findings under supporting or contradicting evidence and remaining unknowns. For each decision-relevant trigger source record:

```text
trigger event; actor; evidence origin; deadline source; date or window;
deadline type; consequence; consequence owner; buyer; payer;
observed buying or workaround behavior; purchase window; budget path;
reachability before the event; trust requirement; low-trust entry;
frequency; delivery liability; source IDs; coverage limitation
```

Use `unknown` rather than inferring missing links. An urgent request does not prove payment; a payment does not prove recurrence; a repeated deadline does not prove the user can reach or safely serve the buyer.

## Interpret missing evidence

State search scope and channel access before concluding that no trigger exists. Use bounded language such as `no buyer-originated rush request found in the accessed channels`. Record inaccessible procurement systems, closed merchant groups, private order histories, missing contract terms, and unavailable transaction data as `coverage_gap` entries.

Absence of a deadline does not invalidate a business. Demand may instead come from repeated use, continuous cost, convenience, entertainment, identity, status, risk reduction, or durable recurring value. Report `no verified deadline trigger in current coverage` without turning it into `no commercial demand`.
