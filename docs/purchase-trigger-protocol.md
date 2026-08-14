# Purchase Trigger and Cost-of-Delay protocol

This protocol makes “why would the buyer act now?” a first-class gate. It does not treat urgency, anxiety, popularity, or a seller's countdown as proof of demand. It identifies a concrete Buying Situation, records the evidence and uncertainty, and then tests whether that situation can produce a safe, reachable, repeatable transaction.

## Runtime position

For a material opportunity whose judgment depends on external reality, use this order:

```text
Conversation
↓
Project discovery / resume / bootstrap
↓
Read IDEA.md + STATE.md
↓
Market Reality Gate
↓
External market facts and cases
↓
Purchase Trigger research
↓
Why-Now Gate
↓
Business Filter (counts as one Thinking Skill)
↓
Optional additional Thinking Skill (normally 1–2 total)
↓
Replication experiment
↓
Transaction evidence
```

The Market Reality Gate asks what is actually happening in the market. The Why-Now Gate asks what event, if any, causes a buyer to seek and pay for a result within a specific window. Neither gate may promote a model inference or Skill judgment to FACT.

`business-filter` remains one of the five Thinking Skills and consumes one lens slot. It always runs first for each leading concrete Opportunity after the Why-Now Gate, including when the evidence-bound outcome is `no_clear_why_now`. “Thinking Skills” after it means only the minimum optional additional lens, with the normal total still one or two.

## Core concepts

### Purchase Trigger

A Purchase Trigger is a real event or situation that moves someone from knowing a problem exists to actively seeking and buying a solution. “The user feels anxious” is not sufficient. The trigger must be connected to observable behavior, a consequence, or a bounded opportunity.

### Cost of Delay

Cost of Delay is what the affected party actually bears by waiting a day or a week, or by missing the relevant cutoff. It can include:

- lost money, orders, customers, or traffic;
- a fine, compliance exposure, or contractual breach;
- missed delivery, launch, inventory, application, or seasonal opportunity;
- accountability to a manager or customer and resulting reputation loss;
- additional manual work or another concrete opportunity cost.

Record the unit and time horizon when evidence supports them. Do not invent a monetary value. If the consequence, likelihood, owner, or amount is not known, say `unknown`.

### Buying Situation

A Buying Situation is one concrete, verifiable situation that may produce purchase behavior. It follows this chain:

```text
Trigger Event
↓
Deadline / Time Window
↓
Consequence of Delay
↓
Consequence Owner
↓
Buyer / Payer
↓
Current Workaround
↓
Purchase Window
↓
Trust Requirement
↓
Bought Result
```

One Project may contain multiple Buying Situations. For example, a short-video service could serve a merchant preparing 50 SKU videos for a campaign, a cross-border seller localizing a launch, or an agency with a temporary delivery-capacity shortfall. Compare those situations independently: their payer, time window, acquisition channel, price, trust barrier, liability, recurrence, and automation value can differ even when the proposed product is the same.

Persist a decision-relevant Buying Situation as the `BSxxx` object defined in [`object-protocol.md`](object-protocol.md). Do not collapse it into the abstract Idea.

## Deadline types

Use exactly one of these values for `deadline_type`:

```text
hard_external
hard_internal
rolling_operational
opportunity_window
soft_social
seller_created
fabricated
none
unknown
```

- `hard_external`: set by an outside event that the buyer cannot readily move, such as a regulation, court date, tender, platform event, tax filing, examination, application cutoff, or customer contract.
- `hard_internal`: set by a formal organizational commitment such as a release, customer delivery, board meeting, event launch, or performance review. Verify that it is not routinely movable.
- `rolling_operational`: recurring operating pressure such as a daily SLA, weekly publication, month-end close, product launch, campaign, or order batch.
- `opportunity_window`: value falls materially after a period such as a trend, season, platform traffic event, inventory window, or creative's useful life.
- `soft_social`: pressure mainly from a manager, customer expectation, peers, face, or status. It is not automatically payment pressure.
- `seller_created`: a genuine promotional period created by the seller. It is a marketing tactic, not proof of buyer-native demand.
- `fabricated`: false scarcity, inventory, or countdown. Never recommend or use it as an experiment tactic.
- `none`: evidence indicates no meaningful deadline for this Buying Situation.
- `unknown`: current evidence cannot classify the deadline.

A deadline is a strong signal, not a requirement for every valid business. High-frequency use, persistent cost, convenience, entertainment, identity or status, long-term risk, and stable repeat purchase can support a business without a deadline. Conversely, a close deadline does not prove willingness to pay.

## Why-Now Gate

For every leading opportunity, answer with evidence or `unknown`:

1. What event starts active search or purchase?
2. When must the buyer receive the result?
3. Who or what sets the deadline, and can it move?
4. What happens if the buyer delays or does nothing?
5. How certain and material is that consequence?
6. Who bears it?
7. Is that person the Buyer, Payer, or Budget Influencer?
8. What workaround is used now?
9. Can the buyer keep delaying?
10. How long is the purchase window?
11. Can this Runtime's user observe and reach the buyer within it?
12. Will the buyer entrust this urgent task to an unfamiliar provider?
13. Is there a low-trust entry, such as a sample, bounded pilot, or non-sensitive input?
14. Does the situation recur?
15. What liability does failed or late delivery create?

If the evidence is insufficient, use:

```yaml
why_now_status: unknown
```

Do not infer `commercial_value: high`. In particular, do not equate anxiety with purchase intent, a seller-created deadline with native demand, one rush job with a repeatable business, or a large rush fee with safe delivery economics.

When useful, distinguish these qualitative outcomes rather than assigning a single numeric score:

```text
real_urgent_buying_situation
urgent_but_low_trust
deadline_without_consequence
high_value_but_unreachable
one_off_rush_service
recurring_deadline_opportunity
manufactured_urgency
high_liability_opportunity
no_clear_why_now
```

The label summarizes a bounded judgment; it does not replace the linked evidence or the `BSxxx` status.

## Researching triggers and consequences

Search event-first, not only product-first. Combine the task or product term with event, deadline, consequence, and buying-behavior terms. Depending on the market, useful signals include official or platform calendars, policy dates, tender cutoffs, procurement and rush-outsourcing requests, temporary hiring, merchant help posts, complaints, rush pricing, launches, filings, examinations, and month-, quarter-, or year-end processes.

Example query modifiers include `加急`, `当天`, `24小时`, `来不及`, `截止`, `延期`, `罚款`, `活动前`, `上线前`, `上新`, `投标`, `急招`, `代做`, `外包`, and `报价`; English equivalents include `urgent`, `deadline`, `rush service`, `same day`, `due tomorrow`, `missed deadline`, `penalty`, `last minute`, and `outsourcing`.

Separate user demand signals from provider marketing. Seek both supporting and negative evidence:

- who posts a real rush request and who pays a rush price;
- which tasks regularly miss deadlines and what happens afterward;
- what workaround is chosen before the deadline;
- complaints, refunds, missed delivery, trust objections, or provider liability;
- whether the trigger recurs and whether demand concentrates into an unsafe capacity peak.

Record inaccessible channels as coverage gaps. Research can support the existence or shape of a Buying Situation, but only the user's own observed behavior and transaction evidence can establish transferability to the current Project.

## State and persistence

Do not add Purchase Trigger boilerplate to every new Project. Bootstrap still creates only `IDEA.md` and `STATE.md`. Only after a real Buying Situation is being analyzed may `STATE.md` add the optional `purchase_trigger` snapshot described in [`workspace-protocol.md`](workspace-protocol.md).

The detailed object belongs to the Stage whose decision it informs, created lazily with its directory, for example:

```text
03-business-validation/
└── buying-situations/
    └── BS001-campaign-video-deadline.md
```

Never create a project-root `DEADLINE.md`, `HUMAN-NATURE.md`, `URGENCY.md`, or `BUYING-SITUATIONS.md`.

## Deadline replication experiment

When the trigger hypothesis is the largest unknown, test it during a real trigger and deadline window. A Deadline Replication Experiment must name:

```text
Buying Situation
Real Trigger
Real Deadline
Purchase Window
Replicated transaction structure
Maximum investment
Maximum delivery liability
Low-trust entry
Success condition
Failure condition
Stop condition
```

Measure whether a qualified buyer pays to receive the required result on time, not whether respondents say they might buy. Cap scope and responsibility; stop if delivery quality cannot be assured, sensitive access is required without safeguards, or liability exceeds the stated limit. Never create false urgency for the test.

For recurring deadline opportunities, also inspect simultaneous capacity peaks, response-time expectations, advance booking, tiered SLAs, rush fees, input constraints, standardized acceptance, required human review, refund and lateness liability, and whether automation would amplify errors. A high ticket price alone does not make a deadline business scalable.
