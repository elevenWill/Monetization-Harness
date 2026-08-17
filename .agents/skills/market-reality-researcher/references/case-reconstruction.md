# Case Reconstruction

Create a `Cxxx` only for a successful or failed case that materially informs the decision or has durable comparison value. A webpage is a source, not automatically a Case.

## Required Case fields

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
Transaction surface
Acquisition channel
Delivery model
Acceptance / rework evidence
Price or revenue evidence
Repeat / continuation evidence
Reported outcome
Verification status
Source IDs
Required resources
Platform dependency
What appears to work
Failure or risk signals
Economics signals
Copyable components
Context-dependent components
Non-transferable advantages
Relevance to current project
Unknowns
```

Set Case `Scope match` to `exact`, `adjacent`, or `weak_analogy`. Do not create an `irrelevant` Case; leave irrelevant sources in the Research record instead.

## Reconstruct the mechanism

Answer with evidence rather than a celebratory summary:

1. Who is the customer and who pays?
2. What result is bought?
3. Through which acquisition channel does the customer arrive?
4. What content, product, or service is delivered?
5. Which platform and geography apply?
6. When did transactions or operation occur?
7. How long did the outcome persist, and did it repeat?
8. What behavioral or financial numbers exist, and who reported them?
9. Which independent source verifies the actor, activity, and outcome?
10. What costs, refunds, churn, complaints, or losses are visible?
11. Does the case rely on existing traffic, brand trust, official platform cooperation, supply chain, or heavy manual operations?
12. Which mechanism most plausibly caused the bought result, and what alternative explanations remain?
13. What acceptance, revision, refund, or rework evidence is visible?
14. Is continuation visible through repeat purchase, repeated requests, retained clients, or sustained seller operation?

For content/media, explicitly separate two partial reconstructions:

```text
Attention Structure: value actor -> repeated value -> observed audience behavior
Revenue Structure: payer -> paid result -> monetization mechanism -> money evidence
```

An Attention Structure may be useful with every Revenue link `unknown`. Do not
upgrade it into a Revenue Structure from views, followers, engagement, or a
headline that someone “made money.”

For transaction-led use, distinguish three plain evidence levels without adding
statuses or a numeric score:

- **Lead:** a buyer request, seller offer, or other demand/supply signal without a
  visible transaction skeleton.
- **Transaction-bearing Case:** payer, bought result, transaction mechanism,
  credible money/paid signal, and delivery are visible.
- **Replication-grade Playbook:** the Case also exposes enough acquisition,
  trust, acceptance, repeat/economics, required-resource, and transferability
  conditions to design a minimum replication action.

Missing fields may remain `unknown`. The label controls the next evidence action;
it does not replace `Verification status` or prove transferability.

## Output structures

```text
Transaction Structure: payer -> offer -> bought result -> payment/transaction evidence
Value Structure: value actor -> repeated value -> observed behavior
Acquisition Structure: channel -> audience -> conversion path -> dependencies
Delivery Structure: work performed -> automation/manual split -> cost and repeatability
Trust Structure: brand, person, proof, disclosure, guarantees, or platform endorsement
Platform Dependency: rules, account state, traffic, integrations, official access
Resource Dependency: capital, audience, supply chain, labor, data, technology, relationships
```

## Verification status

Choose exactly one:

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

- `exact_verified`: exact business form; real actor; explicit time/platform; behavioral or transaction evidence; not solely vendor promotion.
- `exact_corroborated`: exact form and key claim corroborated across independent evidence, but not all reported operating detail is directly observed.
- `exact_reported`: exact concrete case rests mainly on first-party account, media report, or unverifiable operating figures.
- `adjacent_verified` / `adjacent_reported`: evidence is credible or reported but differs materially in format, platform, geography, customer, payer, or transaction.
- `vendor_claim_only`: customer result appears only in provider/software/agency marketing without customer-side or independent support.
- `stale_case`: the case may have existed but age undermines the current decision.
- `contradicted`: stronger evidence conflicts with the core claim.
- `insufficient_evidence`: actor, activity, outcome, or relevance cannot be established.

Do not translate `vendor_claim_only` into a verified customer FACT. Record instead that the vendor published a claim and list the missing corroboration.

## Preserve negative cases

Reconstruct failed or stopped cases with the same rigor. Capture the failure boundary, duration, sunk cost, complaint/refund behavior, enforcement, and whether failure came from demand, trust, economics, delivery, policy, or platform dependency. Absence of a discovered failure case is a coverage statement, not evidence of safety.
