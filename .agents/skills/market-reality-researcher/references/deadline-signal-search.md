# Deadline Signal Search

Verify whether a claimed deadline is externally anchored, operationally real, movable, seller-created, or fabricated. A date becomes commercially relevant only when delay has a concrete consequence, the consequence has an owner, and buying can occur inside the available window.

## Contents

- [Classify the deadline](#classify-the-deadline)
- [Choose deadline sources](#choose-deadline-sources)
- [Verify the causal chain](#verify-the-causal-chain)
- [Detect manufactured urgency](#detect-manufactured-urgency)
- [Check trust, reachability, and liability](#check-trust-reachability-and-liability)
- [Record coverage gaps](#record-coverage-gaps)

## Classify the deadline

Use exactly one candidate type and retain `unknown` until its source is established:

```text
hard_external | hard_internal | rolling_operational | opportunity_window
soft_social | seller_created | fabricated | none | unknown
```

| Type | Meaning | Verification focus |
| --- | --- | --- |
| `hard_external` | A regulator, court, tender, tax, exam, application, platform event, or customer contract fixes the window | Current authoritative date, scope, consequence, timezone, and whether extensions exist |
| `hard_internal` | A formal launch, delivery, board, campaign, or performance commitment fixes the date | Who approved it, whether it can move, and what actually happens if it moves |
| `rolling_operational` | The pressure repeats with an SLA, daily queue, weekly release, month end, restock, campaign, or batch | Observed cadence, backlog behavior, and repeated workaround or spend |
| `opportunity_window` | Value falls materially after a trend, season, inventory, campaign, or creative window | Evidence of value decay and whether the buyer can act before it closes |
| `soft_social` | Pressure mainly comes from expectation, status, peers, a manager, or appearance | Whether it causes budgeted action rather than expressed anxiety |
| `seller_created` | A seller sets a genuine promotion or capacity window | Treat as a sales mechanism, not customer-native demand, unless an independent buyer trigger exists |
| `fabricated` | The countdown, inventory, or scarcity is false or deliberately misleading | Reject as evidence and never recommend creating it |
| `none` | Evidence supports that no material time window controls the decision | Look for non-deadline demand mechanisms instead |
| `unknown` | The source, consequence, or window has not been verified | Preserve uncertainty and design a bounded check |

## Choose deadline sources

Match the source to the claimed deadline:

| Claim | Preferred sources | Useful secondary signals | Common limitation |
| --- | --- | --- | --- |
| Regulation, filing, application, exam | Current regulator or official program page | Credible reporting linked to the original | Old calendars, wrong jurisdiction, extension not checked |
| Platform campaign or policy date | Current official platform calendar, rule center, merchant academy | Merchant notices and operator posts | Seller summaries may omit eligibility or update dates |
| Tender or procurement | Original tender, procurement notice, buyer request | Contractor discussion | Closing date does not prove a budget for this solution |
| Contract or customer delivery | Contract term or authorized customer statement | Project records, dispute reports | Often private; do not infer unseen terms |
| Launch, restock, campaign, month/quarter end | First-party operating schedule plus observed behavior | Temporary hiring, outsourcing, help posts, service-market orders | A recurring calendar does not prove delay cost or payment |
| Rush demand and price | Buyer-originated urgent order, accepted quote, marketplace transaction | Provider rush offer or advertised surcharge | Offered urgency and price are not buyer acceptance |
| Consequence of delay | Penalty schedule, lost-order record, SLA breach, complaint, refund, documented extra labor | Operator retrospective | Hypothetical harm may be marketing copy |

Also inspect creator and merchant communities, app reviews, customer complaints, temporary job posts, service marketplaces, and public help requests when they are relevant and accessible. Follow the Skill's Agent Reach and safe-acquisition rules; inaccessible or login-only sources remain coverage gaps.

## Verify the causal chain

For each deadline claim answer:

1. Who or what controls the date?
2. What is the exact date, duration, timezone, and eligibility scope?
3. Can the date move, reset, or receive an extension?
4. What observable consequence follows delay, and how certain is it?
5. Who owns that consequence?
6. Is that owner the buyer, payer, budget influencer, or none of them?
7. What workaround is used, and is there evidence of spend or costly behavior?
8. When does search or procurement begin and end?
9. Can the runtime user reach the buyer and deliver inside that window?
10. Does the event repeat, and is the cadence evidenced rather than assumed?

Do not infer willingness to pay from anxiety, traffic volume, a deadline date, or cost of delay alone. Preserve each missing link as an assumption.

## Detect manufactured urgency

Treat these as warning signs:

- a countdown resets, differs by visitor, or has no named event owner;
- stock or capacity claims have no observable basis;
- the only deadline source is the seller's landing page;
- the claimed consequence is merely losing a discount created by the same seller;
- buyer-side channels show ordinary planned demand rather than urgent action;
- a provider's rush surcharge is cited as proof that buyers pay it;
- urgency language changes, but the offer remains continuously available.

`seller_created` may describe a real promotion; it still does not prove a customer-native purchase trigger. `fabricated` urgency is deceptive and must not be proposed as an experiment, acquisition tactic, or recommendation.

## Check trust, reachability, and liability

Urgency can reduce evaluation time while increasing perceived delivery risk. Investigate:

- whether the buyer will delegate to an unfamiliar provider;
- required credentials, approvals, account access, data access, or brand/IP rights;
- low-trust entry points such as one sample, a bounded paid diagnostic, escrow, staged access, or work on non-sensitive inputs;
- whether the buyer can be identified and contacted before the window closes;
- refund, rework, breach, compliance, and downstream-loss exposure if delivery is late or wrong;
- whether a repeatable deadline creates predictable demand or simultaneous capacity spikes and continuous firefighting.

A real urgent event can still be `urgent but unbuyable` or too liable to serve safely. Record that conclusion separately from deadline reality.

## Record coverage gaps

Name the specific missing evidence, for example:

```text
official campaign calendar checked, but merchant-only eligibility notices inaccessible
public rush listings checked, but accepted quotes and payments unavailable
deadline date verified, but contract penalty and consequence owner unknown
buyer help posts checked, but closed operator groups and private procurement not accessed
provider rush prices observed, but no buyer-originated acceptance evidence found
```

Never write that a whole market lacks a deadline or urgency signal when only public or indexed channels were checked.
