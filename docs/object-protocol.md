# Decision object protocol

## Types and IDs

| Type | ID | Meaning | Required evidence/status |
| --- | --- | --- | --- |
| Opportunity | `O001` | A candidate worth investigating | Origin and reason to inspect |
| Fact | `F001` | Something that happened or was directly observed | Source/evidence and observed date |
| Assumption | `A001` | A belief not yet supported strongly enough | Status and validation plan |
| Decision | `D001` | A chosen action or constraint | Basis, owner/date, revisit condition |
| Experiment | `E001` | A bounded test of named assumptions | Cost cap, success/failure criteria, deadline |
| Transaction | `T001` | Actual exchange of money | Amount/currency/date/payer evidence; link from a Fact |
| Research | `R001` | A scoped investigation of an external decision question | Scope, checked date, sources, contrary evidence, verdict, recheck condition |
| Case | `C001` | A reusable reconstruction of a market precedent or failure | Transaction structure, verification status, transferability, source IDs |
| Buying Situation | `BS001` | A concrete, verifiable situation that may produce purchase behavior | Trigger, time window, consequence, owner, buyer/payer, trust, reachability, status |

IDs are unique and permanent inside one project. Allocate the next unused integer by searching the entire project. A moved object keeps its ID.

Sources are local to one Research object and use its ID as a namespace: `R001-S01`, `R001-S02`, and so on. A Source is a cited record inside `R001`, not a project-wide object. Never allocate a Case for every search result; create one only when the reconstructed precedent remains useful to the current decision or future project memory.

A Buying Situation uses its own `BSxxx` namespace. One Project may contain multiple Buying Situations; allocate the next unused number by searching the whole project, and do not overwrite or renumber an earlier situation when the trigger, payer, or purchase window changes.

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

Draft choices use `DRAFT-D001` only in `STATE.md`; allocate `D001` when the user commits. Record which facts and assumptions support it.

## EXPERIMENT

```markdown
### E001 — Replicate paid case-file organization

- Tests: A001
- Offer: Deliver the same result manually for CNY 500
- Audience: 10 qualified lawyers not connected to Customer A
- Maximum downside: 7 days and CNY 300
- Success: at least 2 independent real payments
- Failure: 10 qualified offers and 0 payments
- Deadline: 2026-08-20
- Stop conditions: cost cap, deadline, or any legal/privacy breach risk
```

Do not use likes, compliments, surveys, or model opinions as substitutes for the behavior named in the success criterion.

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
