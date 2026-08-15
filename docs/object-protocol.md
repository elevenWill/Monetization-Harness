# Decision object protocol

## Types and IDs

| Type | ID | Meaning | Required evidence/status |
| --- | --- | --- | --- |
| Opportunity | `O001` | A candidate worth investigating | Origin, comparison role, business archetype status, Reality signal, investigation advantage, evidence status, commercial bridge, and inference scope |
| Fact | `F001` | Something that happened or was directly observed | Source/evidence and observed date |
| Assumption | `A001` | A belief not yet supported strongly enough | Status and validation plan |
| Decision | `D001` | A chosen action or constraint | Basis, owner/date, revisit condition |
| Experiment | `E001` | A bounded test of named assumptions | Cost cap and predeclared outcome criteria; after completion, result code and linked raw evidence |
| Transaction | `T001` | Actual exchange of money | Amount/currency/date/payer evidence; link from a Fact |
| Research | `R001` | A scoped investigation of an external decision question | Scope, checked date, sources, contrary evidence, verdict, recheck condition |
| Case | `C001` | A reusable reconstruction of a market precedent or failure | Transaction structure, verification status, transferability, source IDs |
| Buying Situation | `BS001` | A concrete, verifiable situation that may produce purchase behavior | Trigger, time window, consequence, owner, buyer/payer, trust, reachability, status |

IDs are unique and permanent inside one project. Allocate the next unused integer by searching the entire project. A moved object keeps its ID.

Sources are local to one Research object and use its ID as a namespace: `R001-S01`, `R001-S02`, and so on. A Source is a cited record inside `R001`, not a project-wide object. Never allocate a Case for every search result; create one only when the reconstructed precedent remains useful to the current decision or future project memory.

A Buying Situation uses its own `BSxxx` namespace. One Project may contain multiple Buying Situations; allocate the next unused number by searching the whole project, and do not overwrite or renumber an earlier situation when the trigger, payer, or purchase window changes.

## OPPORTUNITY

An Opportunity is a Candidate for investigation, not a validated market or a
commitment. When an `Oxxx` is persisted, retain:

- **Origin:** direct observation, user-reported concrete behavior, existing
  transaction/spend/workaround, current external market evidence, or an explicit
  model-derived synthesis;
- **Comparison role / decision level:** whether the Candidate is currently a
  tool/capability, content topic, content format, distribution channel, audience,
  value mechanism, business/monetization mechanism, or offer/product. Use a plain
  project-specific label when none fits; this is a normalization aid, not a new enum;
- **Business archetype and status:** product/SaaS, service/consulting,
  marketplace/transaction, content/media/creator, commerce/affiliate, or another
  clearly named structure, plus whether it is a user-committed Decision/constraint
  or an uncommitted preference/hypothesis;
- **Opportunity Evidence:** the observed recurrence, spend, transaction,
  workaround, audience behavior, precedent, or other Reality signal;
- **Investigation Advantage:** founder familiarity, reachability, speed, cost,
  manual-test ability, or existing assets, kept separate from Opportunity Evidence;
- **Evidence status and inference scope:** what is observed, what remains an
  ASSUMPTION, and what the source can and cannot establish; and
- **Commercial bridge:** the value actor and value mechanism; candidate payer and
  monetization mechanism; observed behavior signal and separately observed money
  signal; the current path from value/attention to money; and the largest bridge
  unknown. Preserve unsupported links as `unknown`.

A model-derived Candidate may receive a capped exploratory test, but founder fit,
user agreement, reachability, or a detailed Execution Packet does not increase
its Market Evidence. Before comparison, normalize Candidates to the same decision
level or map mixed components into separate monetization structures. A tool,
topic, format, channel, or audience is not by itself a business direction;
audience pull is not a Revenue Bridge. Preserve a user-committed archetype
Decision or constraint. Treat tentative preference or intuition as an ASSUMPTION,
and record a Runtime-proposed service, product, affiliate, or other monetization
route as a separate hypothesis.

## FACT

A FACT must be falsifiable, source-linked, and phrased without interpretation.

```markdown
### F001 — One paid manual delivery

- Observed: 2026-08-13
- Evidence: [payment record](../05-transactions/evidence/T001-redacted.md)
- Statement: Customer A paid CNY 500 for one case-file organization delivery.
```

Do not write “customers value this” from one payment. That remains an assumption.

External evidence must preserve what was actually observed:

- “As of 2026-08-14, the platform rule requires an AI-content disclosure” may be a Fact when it links the current official rule and records its scope.
- “Vendor A claims Customer B increased GMV by 300%” may be a Fact about Vendor A publishing that claim. Customer B's operating result remains unverified until corroborated.
- A search-result snippet, model inference, popularity count, like count, follower count, or unaudited GMV claim is not proof of demand or profit.

## ASSUMPTION

Use status `untested`, `testing`, `supported`, `weakened`, or `invalidated`. “Supported” is not permanent truth.

```markdown
### A001 — Other lawyers will pay CNY 500

- Status: testing
- Basis: F001
- Tested by: E001
- Disconfirming result: fewer than 2 independent payments after 10 qualified offers
```

## DECISION

Draft choices use `DRAFT-D001` only in `STATE.md`; allocate `D001` when the user commits. A tentative preference or intuition remains an ASSUMPTION, not a constraint. Record which facts and assumptions support a committed Decision.

## EXPERIMENT

An Experiment keeps its plan and completed result in the same `Exxx` object. It is
not a lead record, CRM pipeline, or a new result-object namespace.

Before execution, record one decision-changing assumption, explicit downside,
and mutually distinguishable thresholds. Use a scenario-specific **selected
evidence path**: include only the observable steps needed to interpret this test.
For example, a paid-offer test might select `qualified -> offer_presented ->
price_presented -> paid`; an observation test might select `eligible_event ->
observed_event -> problem_confirmed`; and a delivery test might select `accepted
-> delivered -> repeated`. Reuse the common step names below when they fit, or
define a plain observable step when they do not:

```text
sourced | contacted | seen_or_delivered | qualified | problem_confirmed
conversation | offer_presented | price_presented | committed | paid
delivered | repeated
```

This vocabulary is diagnostic, not a mandatory full funnel. Do not add irrelevant
steps or maintain prospect-level rows.

When the user's stated goal is income and an Opportunity experiment is material
in founder attention, elapsed time, repeated publishing, manual delivery, money,
reputation, or opportunity cost, also record:

```text
what this experiment tests
what success changes
what failure changes
which Monetization Bridge or money-path unknown it reduces
why its decision information exceeds a smaller safe alternative
founder-attention and total-downside cap
```

“Material” is contextual, but several hours, multiple days or releases, or
meaningful manual delivery triggers this check even when cash spend is small. Do
not approve a material income-seeking experiment whose success only proves that
someone liked or found content useful while its stated money-path unknown remains
unchanged. A single reversible 30–90 minute probe may test a narrow audience/value
claim with monetization still `unknown`; record that limited inference and do not
present it as commercial validation. Existing auditable payment or delivery
evidence takes the direct Stage route and does not require a new revenue-model scan
unless the monetization structure itself is the active uncertainty.

```markdown
### E001 — Replicate paid case-file organization

- Status: planned
- Tests: A001
- Offer: Deliver the same result manually for CNY 500
- Audience: 10 qualified lawyers not connected to Customer A
- Maximum downside: 7 days and CNY 300
- Claim evidence budget: 14 total days, CNY 600, and at most 2 repair reviews across E001-series tests of A001
- Implementation revisit trigger: a qualified buyer cannot evaluate the bounded result without a minimal technical artifact, or repeated paid delivery shows one measured stable bottleneck
- Selected evidence path: qualified -> offer_presented -> price_presented -> paid
- Planned exposure: 10 qualified lawyers receive and understand the offer and real price
- Success threshold: at least 2 independent real payments
- Demand-failure threshold: 10 qualified intended buyers receive and understand the offer and real price, the decision window closes, and 0 pay
- Invalid if: fewer than 10 qualified intended buyers receive the offer and price, buyer qualification cannot be established, or a material protocol deviation prevents the named assumption from being tested
- Deadline: 2026-08-20
- Stop conditions: cost cap, deadline, or any legal/privacy breach risk
```

Do not use likes, compliments, surveys, or model opinions as substitutes for the behavior named in the success criterion.

### Completed result and Evidence Ledger

When the experiment is completed, append a `Completed result` section to the same
artifact. Use exactly one result code:

```text
success | demand_failure | invalid | inconclusive
```

Classify in this order so an apparent positive outcome does not hide a broken
test:

1. `invalid`: a known targeting, reachability, exposure, safety, protocol, or
   measurement defect means the experiment did not test the named assumption.
2. `success`: no material invalidating defect exists and the predeclared success
   threshold was met.
3. `demand_failure`: no material invalidating defect exists, the strict demand
   exposure gate below was met, and the predeclared demand behavior remained at
   or below its failure threshold.
4. `inconclusive`: no result above applies; the evidence is too sparse, mixed,
   censored, or uncertain to cross a predeclared threshold or establish a known
   invalidating defect.

`demand_failure` is allowed only when all of these are evidenced:

- the predeclared minimum number of qualified intended buyers or payers was met;
- qualification and decision relevance were actually checked;
- each counted buyer received and understood the real offer and real price;
- the relevant decision or purchase window elapsed; and
- channel failure, missing exposure, relationship bias, or another protocol
  defect does not plausibly explain the result.

If these conditions are not met, use `invalid` for a known test defect or
`inconclusive` for insufficient or uncertain evidence. Ten messages with only two
views and one wrong decision-maker cannot establish demand failure.

The Evidence Ledger is one aggregate table over the selected path. Planned counts
and actual counts stay separate, and every decision-relevant actual count links to
redacted raw evidence or a dated observation. Omit inapplicable steps.

```markdown
## Completed result

- Completed at: 2026-08-20
- Result: demand_failure
- Result basis: the success threshold was missed after the demand-failure exposure gate was met
- Raw evidence: [redacted outreach and response log](evidence/E001-outreach-log.md), [payment-provider check](evidence/E001-payment-check.md)
- Observed events: 0 payments; 10 qualified offer-and-price exposures; 6 explicit price refusals

### Evidence Ledger

| Selected step | Planned threshold | Actual | Evidence or deviation |
| --- | ---: | ---: | --- |
| qualified | 10 | 10 | qualification fields in outreach log |
| offer_presented | 10 | 10 | delivered offer records |
| price_presented | 10 | 10 | CNY 500 shown and comprehension recorded |
| paid | 2 success / 0 demand failure | 0 | payment-provider check after decision window |

### Reasons and diagnosis

- Reason evidence: `too_expensive` — 6 linked buyer replies explicitly rejected the CNY 500 price
- First broken selected step: paid
- First broken layer: price_value_buyer_economics
- Diagnosis basis: linked replies, not the zero-payment count alone
- Competing explanations: trust remains possible for 4 buyers without a stated reason
- Material protocol deviations: none

### Feedback

- Assumption updates: A001 weakened
- Facts created or updated: F006 records the observed exposure and payment count
- Decision updates: D003 records the user's choice to narrow the next test to price/value structure
- Stage after evidence review: business_validation (unchanged)
- Next experiment or action: compare one value-framed CNY 500 offer against the current offer with a new capped qualified sample
```

Use these standard reason codes when supported, while preserving a link to the
raw words, behavior, or operating evidence that justified each code:

```text
cannot_reach | wrong_person | not_qualified | no_problem | low_frequency
no_urgency | already_solved | no_budget | too_expensive | no_trust
bad_timing | offer_unclear | delivery_risk | policy_risk | switching_cost
decision_process_unknown | other
```

A reason code is a searchable summary, not evidence and not a FACT. Do not infer
`too_expensive`, `no_urgency`, or another reason from silence alone. With `other`,
record a short neutral label plus its evidence.

Diagnose both the first broken selected step and the first evidence-supported
layer. The step is the earliest selected-path threshold or evidence requirement
that broke; the layer is the current explanation for it. Use one of these common
layers when applicable: `reachability_channel`, `targeting_qualification`,
`problem`, `trigger_frequency_timing`, `offer`,
`price_value_buyer_economics`, `trust`, `decision_process`, `delivery`,
`recurrence`, or `delivery_economics`. Use `none` for success and `unknown` when
the evidence cannot distinguish competing explanations. A conversion count alone
does not prove a causal layer.

Apply completed feedback conservatively:

- **ASSUMPTION:** `success` may support only the named claim; `demand_failure`
  weakens or invalidates only the precisely exposed demand claim; `invalid`
  neither supports nor refutes it; `inconclusive` normally leaves it testing or
  refines what remains unknown. Do not generalize one result to “the market.”
- **FACT:** persist falsifiable observations such as who was qualified, what was
  actually exposed, payments, refunds, delivery, and repeat behavior with dates
  and evidence. Diagnoses and reason codes remain analysis unless directly
  observed as a statement or behavior.
- **TRANSACTION:** each qualifying payment still requires its own `Txxx` plus a
  linked FACT; reconcile `transactions.total` and `repeat_customers`. A `success`
  code is not a transaction.
- **DECISION:** record the chosen continue, change, stop, or retest action and its
  evidence basis only when the user commits; do not manufacture a `Dxxx` from the
  model's diagnosis.
- **Stage:** recompute the earliest unresolved gate from the updated evidence.
  No result code automatically promotes a Stage. Roll back only when evidence
  invalidates earlier entry evidence; `invalid` or `inconclusive` alone normally
  changes the next test, not the Stage.
- **Next experiment:** after `invalid`, repair the first broken validity layer;
  after `inconclusive`, acquire the cheapest missing evidence or sharpen the
  threshold; after `demand_failure`, stop, pivot the exposed claim, or isolate one
  evidence-supported competing explanation; after `success`, replicate
  independently or test the next earliest gate. Change one material uncertainty
  at a time and keep the downside capped.
- **Portfolio stop:** repeated repairs of the same claim consume its predeclared total time, cost, and repair-review budget. Exhaustion requires pause, deprioritization, or pivot review even when no single run qualifies as `demand_failure`; record the access limitation rather than claiming the market has no demand.

These completion requirements apply only when an `Exxx` records a completed or
result section. Existing plan-only artifacts remain valid and need no migration.
When a historical plan-only experiment is completed or materially re-reviewed,
append the canonical completion section then; do not allocate a new object ID.

## TRANSACTION

Redact personal/payment secrets. Record enough evidence to distinguish paid, refunded, discounted, barter, or promised transactions. `transactions.total` counts completed monetary transactions; `repeat_customers` counts customers who completed more than one transaction.

Persist each completed monetary transaction under `05-transactions/` with this minimum auditable record:

```markdown
### T001 — Bounded paid delivery

- Status: completed
- Amount: 500
- Currency: CNY
- Paid at: 2026-08-14
- Payer: Customer A (redacted stable label)
- Customer: Customer A (redacted stable label)
- Payment evidence: redacted receipt or provider record
- Linked fact: F001
- Linked buying situation: BS001 | unknown
```

An incomplete oral or chat report of payment is still useful evidence, but it
remains a FACT until the minimum auditable fields above are known. Keep
transaction counters provisional or `unknown`; do not create a `completed`
`Txxx` whose amount, currency, paid date, payer/customer, or payment evidence is
unknown. A user report is provenance for the FACT, not payment evidence for a
completed Transaction unless it includes an auditable redacted receipt or
provider record.
One or many such incomplete reports belong in `transaction_validation` for
bounded verification, but do not satisfy completed Transaction evidence or the
Leverage entry gate. Verify individual payments and comparable valued delivery
before advancing; do not infer repetition by counting unverified mentions.

Allocate exactly one stable `Txxx` per auditable monetary transaction. Never use
a range or rollup filename such as `T001-T036-...md`; summarize cohorts from
their individual Transaction records without replacing them.

`Status` must distinguish `completed`, `refunded`, `discounted`, `barter`, or `promised`. Only `completed` counts toward `transactions.total` or a `paid`/`repeated` Buying Situation. A `repeated` Buying Situation requires at least two linked completed `Txxx` records that demonstrate materially comparable occurrences; one transaction or two mentions of the same record is insufficient.

## BUYING SITUATION

A Buying Situation is one specific chain from a real or hypothesized Trigger Event through a time window and consequence to a bought result. It is not an emotion profile, generic customer pain, abstract Idea, or seller-created urgency claim. Follow [`purchase-trigger-protocol.md`](purchase-trigger-protocol.md) for the Why-Now Gate, Deadline types, Cost of Delay, and safety rules.

Use exactly one status:

```text
hypothesis
observed
supported
paid
repeated
weakened
invalidated
```

- `hypothesis`: the situation has been proposed, but no direct signal establishes the chain.
- `observed`: the trigger or time-bound situation was directly observed, but purchase behavior is not yet supported.
- `supported`: linked evidence supports the trigger-to-search or trigger-to-purchase mechanism, but this Project has not completed a qualifying payment in it.
- `paid`: at least one completed monetary transaction occurred in this situation and is linked by `Txxx`; a promise or external case is insufficient.
- `repeated`: linked transactions show the same materially comparable Buying Situation produced independent repeat evidence; one payment is insufficient.
- `weakened`: contrary evidence materially reduces confidence in the situation while leaving it testable.
- `invalidated`: the defined situation failed its explicit disconfirmation condition or evidence contradicts a necessary part of the chain.

Use this complete record. Every unsupported or missing field must be `unknown`; do not fill it from a model inference, an adjacent case, or the user's urgency language.

```markdown
### BS001 — 平台活动前批量制作商品短视频

- Status: hypothesis | observed | supported | paid | repeated | weakened | invalidated
- Trigger event: unknown
- Deadline type: hard_external | hard_internal | rolling_operational | opportunity_window | soft_social | seller_created | fabricated | none | unknown
- Deadline source: unknown
- Deadline date/window: unknown
- Buyer: unknown
- Payer: unknown
- Beneficiary: unknown
- Required result: unknown
- Cost of delay: unknown
- Consequence owner: unknown
- Current workaround: unknown
- Purchase window: unknown
- Trust requirement: unknown
- Low-trust entry: unknown
- Frequency: unknown
- Observability: unknown
- Reachability: unknown
- Budget path: unknown
- Delivery risk: unknown
- Linked facts: unknown
- Linked assumptions: unknown
- Linked research: unknown
- Linked cases: unknown
- Linked experiments: unknown
- Linked transactions: unknown
```

The values separated by `|` show allowed enums in the template; a real object records one value. `paid` and `repeated` require linked transaction evidence. A close deadline without a concrete consequence, reachable payer, viable trust path, and bounded delivery liability does not justify a high-value conclusion.

## RESEARCH

Use a Research object for one decision question, not for a broad topic dump. It must contain:

```text
Research question
Scope
Market / geography
Target platforms
Content type
Started / checked date
Research depth
Queries used
Channels actually accessed
Coverage gaps
Sources
Supporting evidence
Contradicting evidence
Exact cases
Adjacent cases
Negative cases
Policy findings
User acceptance signals
Competitor and pricing signals
Verdict
Remaining unknowns
Recheck condition
```

Use exactly one Research verdict:

```text
exact_precedent_verified
exact_precedent_reported
adjacent_precedent_only
market_signal_exists
insufficient_evidence
contradicted_by_evidence
policy_conditional
policy_blocked
research_blocked
stale_research
```

These verdicts describe the research coverage, not the probability of success. Do not replace them with “feasible,” “80% confidence,” or a count of search results.

Use `quick`, `standard`, or `deep` as the Research depth. A policy or price refresh still uses one of these depth values and records its narrower purpose separately; do not invent additional depth enums.

## CASE

A Case reconstructs the mechanism behind a precedent rather than repeating its headline. Record:

```text
Actor
Date range
Market
Platform
Content format
Scope match
Target customer
Payer
Offer
Bought result
Acquisition channel
Delivery model
Price or revenue evidence
Repeatability evidence
Reported outcome
Verification status
Source IDs
Required resources
Platform dependency
What appears to work
Failure or risk signals
Copyable components
Context-dependent components
Non-transferable advantages
Relevance to current project
```

Use exactly one Case verification status:

```text
exact_verified
exact_corroborated
exact_reported
adjacent_verified
adjacent_reported
vendor_claim_only
stale_case
contradicted
insufficient_evidence
```

`exact_verified` requires an exact business form, an identifiable actor, a clear time and platform, and behavior or transaction evidence that is not only vendor marketing. `exact_reported` is still a concrete case but relies mainly on first-party reporting, media reporting, or operating numbers that cannot be independently checked. `vendor_claim_only` is a lead, not verified customer performance.

Do not combine the Case status enum with the Research verdict enum. An `R001` can contain a `vendor_claim_only` Case and still conclude `insufficient_evidence`.

## SOURCE

Every cited Source in a Research object must record:

```yaml
id: R001-S01
title:
url:
publisher:
platform:
source_type:
published_at:
accessed_at:
market:
claim:
supports:
contradicts:
authority:
verification:
freshness:
scope_match:
direction:
notes:
```

Use the following dimensions rather than one pseudo-precise score:

```yaml
authority: official | first_party | independent_third_party | user_generated | vendor_marketing | unknown
verification: directly_observed | independently_corroborated | single_source_reported | unverified
freshness: current | aging | stale | unknown
scope_match: exact | adjacent | weak_analogy | irrelevant
direction: supports | contradicts | mixed | neutral
```

Explain why the source can support the named claim. `published_at` is when the source or rule was issued, `accessed_at` is when it was retrieved, and `checked_at` is when the Runtime verified the claim against the current decision. Do not collapse these dates.

## Claim-Specific Evidence Matrix

There is no universal evidence ladder. Select evidence according to the claim being decided.

### Platform policy

```text
current official platform rule
> current regulator document
> official platform learning center or announcement
> credible reporting about the rule
> service-provider interpretation
> user post
> model inference
```

Open the official source; a search snippet is only a lead. A policy Fact must record `platform`, `region`, `content_type`, `published_at`, `checked_at`, `official_url`, and `status`.

### Market existence

```text
independently verifiable transaction or sustained operation
> case corroborated by multiple independent sources
> official platform merchant case
> operator's detailed first-party retrospective
> credible interview
> service-provider customer story
> marketing copy
> unsourced retelling
```

### User acceptance

```text
purchase, repeat purchase, retention, refund, or complaint behavior
> publicly verifiable conversion or operating change
> a substantial set of relevant authentic comments
> structured study or survey
> individual expression
> model judgment
```

Liking is not buying. One complaint is a risk signal, not proof that the whole market rejects the offer.

### Feasibility for the current user

```text
the user's own paid replication experiment
> the user's own behavioral test
> exact case with closely matched resources
> general exact case
> adjacent case
> abstract theory
```

External evidence can show that a pattern existed. Only the user's experiment can test whether it transfers to their resources, market, and operating constraints.

## Freshness and scope

Recheck a time-sensitive claim before a material decision when its platform, region, content format, account requirements, pricing, competitive environment, AI disclosure rule, API capability, advertising rule, or distribution mechanism may have changed. Freshness depends on the claim and decision, not one repository-wide expiry interval.

An exact case must match the relevant format, platform, market, payer, and transaction structure. Digital-human livestream commerce, human short-video commerce, overseas TikTok commerce, avatar knowledge videos, and brand films do not by themselves verify digital-human short-video commerce in China. More adjacent examples never add up to an exact precedent.

Standard research must actively seek failures, complaints, refunds, bans, throttling, distrust, low conversion, abandoned operations, and costly hidden manual work. If none is found, write `no negative case found in current coverage`; never write that no failure risk exists.

## Updating state

Store detailed objects in the relevant stage directory. Create that directory only in the same write that creates the real object; never pre-create empty stage or category directories. Stage directories may be non-contiguous because `STATE.md`, not the filesystem shape, is authoritative for the current Stage.

Keep only active or decision-critical summaries and links in `STATE.md`. When an assumption changes status or a decision is reversed, preserve the original record and add the new evidence and date.
