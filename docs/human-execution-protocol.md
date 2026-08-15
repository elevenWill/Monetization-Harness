# Human Execution Protocol

This protocol turns one selected next action into a bounded Reality Contact that a
person can execute. It is a runtime contract, not a Thinking Skill, Persona,
sales methodology, CRM, funnel system, or new Stage. It does not select the
project Stage or replace experiment design; it starts only after the Runtime has
identified the earliest unresolved uncertainty and chosen human action as the
best next evidence source.

## Entry and exit

Generate one minimum Execution Packet when all of these are true:

1. the immediate decision depends on project-specific observation, contact,
   offer, payment, delivery, or operating evidence;
2. a person must perform or supervise the next bounded action;
3. the action can be stated safely enough to execute now, or one blocking
   `unknown` can be resolved by a smaller acquisition step; and
4. the action has a review point and can change a named assumption or decision.

This can occur in any Stage. Typical uses are:

- `opportunity_discovery`: find and observe reachable people or workflows;
- `problem_validation`: test whether the claimed problem and workaround occur;
- `business_validation`: present a bounded result and real price to qualified
  buyer or payer candidates;
- `experiment_validation`: run the accepted bounded test;
- `transaction_validation`: repeat a comparable offer and delivery;
- `leverage_discovery`, `productization`, or `scaling`: execute one bounded
  operator, product, acquisition, capacity, or dependency test when human work
  is actually required.

Do not generate a Packet for:

- No Project discussion, general knowledge, brainstorming, or an unaccepted
  recommendation;
- state reconciliation, document classification, or analysis with no human
  reality-contact step;
- a decision already answered by fresh, scope-matched evidence;
- an external-policy, market, price, competitor, or precedent question whose
  next step is bounded research rather than human contact;
- routine execution that is already concrete and whose outcome cannot change a
  current assumption or decision;
- an unsafe, deceptive, unlawful, privacy-violating, or unbounded action; or
- a repeated copy of a still-current Packet when no decision-relevant field has
  changed.

If external research is needed before contact can be safe or interpretable, run
that research first. If a critical field cannot yet be known, produce only the
smaller `unknown`-acquisition step described below; do not disguise a generic
instruction as an executable Packet.

## Reality Evidence First is not Web First

Select evidence by the exact claim that would change the immediate decision and
its information value relative to total downside, including founder attention,
elapsed time, money, reputation, and opportunity cost. Among evidence paths that
can resolve the decision safely, prefer the cheapest fresh route. Use this order:

1. Reuse existing project or external evidence when it is fresh, scope-matched,
   and sufficient.
2. Ask whether only the project's own behavior can answer the claim. Reach,
   observed workflow, offer comprehension, willingness to pay, delivery quality,
   and repeatability normally require direct field evidence.
3. Ask whether a current external fact controls safety or validity. Platform
   policy, law, operability, current prices, competitors, availability, and
   exact or adjacent precedent normally require bounded external research.
4. If both are needed, check the minimum external constraint first, then contact
   reality; do not let research substitute for the field result.
5. If neither route is currently available, record `unknown` and choose the
   cheapest safe access step instead of browsing ceremonially.

| Decision-changing claim | Preferred first evidence |
| --- | --- |
| A current platform, legal, policy, availability, or market constraint | Current authoritative external research |
| Whether the named customer or workflow is reachable and the problem occurs | Direct sourcing, observation, or contact |
| Whether a qualified buyer will pay this price for this result | A real offer, real price, and usable payment path |
| Whether the result can be delivered safely and acceptably | One bounded manual or assisted delivery |
| Whether payment and delivery repeat | Comparable offers, payments, and deliveries with independent or repeat buyers |
| Whether a content theme has repeated audience pull | Bounded observation of qualified audience behavior on relevant platforms or direct usage contexts |

Web evidence can establish external conditions and precedents. It cannot by
itself establish transferability, this project's willingness to pay, delivery
quality, or repeatability. Direct contact likewise cannot replace a current
policy or legal check when violating it would invalidate the test or create
material harm.

## Evidence fit before contact

Before choosing a sample, check five items: the exact Decision Claim; the
Evidence Population qualified to answer it; the Sample Source; what observations
from that source can prove; and what they cannot prove given material selection
or proxy bias. Reachability is an evidence-acquisition advantage. It is not
representativeness, market importance, commercial value, or willingness to pay.

For example, nearby technical creators may reveal their own recurring production
problems and workarounds. They cannot by themselves establish platform-wide
content pull, the best audience, a payer, or the best business direction. A small
sample remains valid for the narrower claim it can answer. Make this boundary
user-visible only when it changes interpretation or prevents a misleading action.

Candidate provenance also remains visible internally. User acceptance means the
Candidate was accepted for testing, not that its Market Evidence improved. A
more concrete Packet improves execution and later attribution; it does not upgrade Candidate credibility, evidence status, business archetype, or Market
Priority.

### Material income-seeking experiments

When the user's goal is income and the proposed action requires several hours,
multiple days or releases, meaningful manual delivery, or comparable attention,
money, reputation, or opportunity cost, verify before producing the Packet:

- the single claim tested and what success changes;
- what failure changes;
- the current Monetization Bridge and largest bridge unknown;
- which money-path unknown the result can reduce; and
- why this action has more decision information than a smaller safe alternative.

Do not treat low cash spend as low cost when founder attention is material. Do
not approve a material content experiment whose success criteria only establish
likes, usefulness, or continued interest while the income decision depends on an
unchanged payer or monetization link. A single reversible 30–90 minute probe may
test narrow audience or value behavior with the bridge still `unknown`; cap its
inference accordingly. This exception permits discovery, not commercial claims.
When direct payment or delivery evidence already answers the current gate, use it
instead of inserting a monetization-structure scan.

## Minimum Execution Packet

The Packet is conditional, not a form to fill completely. Include only fields
needed to let a person act and later interpret the result. Every included value
must be evidenced, user-supplied, or explicitly marked `unknown` with an
acquisition step.

Default to a seven-part **Micro Packet** for a low-risk first contact or observation: `(1)` decision claim, `(2)` qualified target, `(3)` verified place/query/channel, `(4)` exact action or message, `(5)` sample/time/cost cap, `(6)` evidence to record, and `(7)` stop/review rule. Expand into the full fields below only when a real offer/price, meaningful trust or delivery risk, accepted experiment, or multi-step validity path makes the extra detail necessary. Do not show an empty form to the user.

```yaml
objective:
decision_claim:
stage:
candidate_basis_and_evidence_status:
evidence_population:
inference_scope:
decision_change_if_success:
decision_change_if_failure:
money_path_unknown_reduced:
why_higher_information_value_than_smaller_alternatives:
founder_attention_cap:

action:
operator:
timebox:
target:
qualification:

sourcing:
  locations:
  queries_or_filters:
  entity_to_find:
  person_or_role_to_reach:
  channel_priority:
  planned_sample_funnel:

interaction:
  opening_message:
  offer:
  price:
  trust_reduction:
  real_deadline_or_purchase_window:

limits:
  max_time:
  max_cost:
  reputation_privacy_legal_limits:
  maximum_delivery_liability:

evidence:
  record:
  success_condition:
  failure_condition:
  invalid_conditions:

stop_condition:
next_review_trigger:
implementation_revisit_trigger:
claim_evidence_budget:
  max_total_time:
  max_total_cost:
  max_repair_reviews:
```

### Always required

- `objective` and `decision_claim`: one decision-changing assumption or claim;
  do not combine discovery, audience pull, pricing, delivery, and repeatability
  into one action. Internally retain the Candidate basis/evidence status,
  claim-qualified Evidence Population, and maximum inference scope; show them
  when selection or proxy bias is material.
- For a material income-seeking experiment, include
  `decision_change_if_success`, `decision_change_if_failure`,
  `money_path_unknown_reduced`,
  `why_higher_information_value_than_smaller_alternatives`, and
  `founder_attention_cap`. Omit these fields for a non-material action when they
  add no decision value; the Micro Packet exception above still requires a narrow
  inference scope.
- `action`, `operator`, and `timebox`: the next physical or communicative step,
  who will perform or supervise it, and an executable count or time boundary.
- `target` and `qualification`: who or what is eligible, the observable inclusion
  and exclusion criteria, and whether the operator must find an organization,
  workflow, individual, buyer, payer, or decision-influencing role.
- `sourcing`: enough detail to find the sample, as specified below.
- `limits`: explicit survivable time and money caps plus any material reputation,
  privacy, legal, platform, delivery, or concentration boundary.
- `evidence`, `stop_condition`, and `next_review_trigger`: what will be captured,
  when execution stops, and when evidence is reviewed before expansion.
- `implementation_revisit_trigger`: required when code/building is deferred; name the evidence that would make the smallest technical artifact necessary for the next valid exposure or for a measured repeated-delivery bottleneck.
- `claim_evidence_budget`: required when a claim may need repeated sourcing/channel/qualification repairs. Cap total time, cost, and repair reviews across experiments; exhausting it triggers pause, deprioritization, or pivot review without pretending the whole market was disproved.

### Required only when the action uses them

- `opening_message`: required for outreach, observation requests, interviews, or
  offers. Keep it transparent and short: relevant context, honest request or
  bounded result, real next step, and no fabricated urgency or social proof.
- `offer`: required when testing a bought result, transaction, or replication.
  State scope, delivery, exclusions, and what the recipient must actually do.
- `price`: required whenever the inference concerns willingness to pay, offer
  viability, or repeat payment. State a real amount, currency, payment timing,
  and refund/cancellation terms when relevant. A survey about hypothetical price
  does not qualify. If price is unknown, first obtain current comparables or run
  a bounded price test; do not silently omit price and claim demand validation.
- `trust_reduction`: required when access, unfamiliarity, privacy, proof,
  procurement, or delivery risk may prevent a qualified buyer from evaluating
  the offer. Use the smallest honest mechanism—sample, milestone, narrow scope,
  reversible trial, redacted proof, clear terms—not invented credentials.
- `real_deadline_or_purchase_window`: include only when buyer timing is material
  and evidenced. The Packet's own timebox is always required; a buyer deadline
  is not. Never manufacture scarcity, a countdown, or a false deadline.
- `maximum_delivery_liability`: required when missed timing, quality failure,
  account access, sensitive data, refunds, or downstream harm can exceed the
  ordinary time and money cap.

## Sourcing and the sample funnel

“Contact 10 users” is not executable. The `sourcing` block must answer, to the
minimum level relevant to the action:

1. **Where:** exact accessible source types or locations, such as an existing
   contact list, public directory, named marketplace category, event exhibitor
   list, relevant job or outsourcing board, customer community, or observable
   workflow. Do not claim access to a private source that has not been authorized.
2. **What to search:** concrete query strings, categories, filters, dates,
   geography, company attributes, role titles, problem signals, or workaround
   signals. A broad market label alone is not a sourcing query.
3. **How to qualify:** observable inclusion and exclusion rules matched to the
   claim, including a problem/situation, audience-behavior, or independence
   signal. Interest, likes, or job title alone do not qualify a buyer/payment
   claim. Repeated qualified consumption may support a scoped audience-pull
   claim, but it does not prove payment or profit.
4. **Whom to reach:** distinguish the organization or workflow to find from the
   operator, user, buyer, payer, approver, or consequence owner to contact.
5. **Which channel first:** name the authorized channel and why it is reachable
   and proportionate. Do not assume that a channel is effective because it is
   popular.
6. **How many at each step:** give a bounded planned funnel, not only a final
   contact count.

Use only the funnel steps needed by the action. For example:

```text
30 sourced records
-> 15 meeting the stated qualification rules
-> 10 contacted through the named channel
-> 6 confirmed delivered/seen where observable
-> 4 substantive conversations
-> 3 qualified buyers receiving the offer and real price
-> payment or refusal evidence recorded
```

An observation action may instead use `workflows sourced -> eligible workflows ->
observations completed -> workaround artifacts captured`. A delivery action may
start at `paid or committed buyer -> delivery attempted -> accepted/reworked ->
repeat requested`. This vocabulary diagnoses exposure; it is not a mandatory
sales pipeline.

Separate planned counts from actual outcomes. When conversion is unknown, choose
the smallest first batch that can reveal a sourcing or message defect and review
it before expanding. A failure condition about demand is interpretable only when
the required number of qualified recipients actually received and understood the
offer and price; otherwise the Packet's invalid conditions must catch the broken
exposure or qualification step.

## Unknown acquisition path

Never invent a location, decision maker, qualification rule, channel, price, or
trust mechanism. For every decision-critical `unknown`, record:

```yaml
unknown_field:
why_it_blocks_execution_or_inference:
cheapest_acquisition_action:
where_or_whom_to_check:
query_filter_or_question:
sample_time_and_cost_cap:
evidence_that_resolves_it:
review_trigger:
```

Choose the acquisition action by the claim: inspect current authoritative pages
for policy; compare current advertised, quoted, and transacted price evidence for
price; search a small named source and inspect profiles for reachability; ask an
existing trusted contact for the buyer/payer path; observe a workflow for problem
and workaround evidence; or place a real bounded offer when only behavior can
answer. The acquisition step must itself be capped. If it fails, retain the field
as `unknown`, record the access or coverage gap, and change the sourcing route or
decision—do not fill the blank with model inference.

## Evidence, stop, and review

Before action, define the minimum evidence that makes the result auditable:

- anonymized stable sample labels, date, source/channel, and qualification basis;
- the exact request, offer, price, terms, and material version changes actually
  shown;
- delivery/seen evidence when available, substantive response or refusal,
  objection, payment/commitment evidence, delivery acceptance, and deviations
  from the planned action as applicable;
- the count at each selected funnel step and why any record was excluded; and
- safety, privacy, policy, trust, or delivery incidents without storing secrets,
  credentials, unnecessary personal data, or raw private-message dumps.

Success and failure thresholds must be set before execution and map back to the
named claim. `invalid_conditions` must cover failures of access, qualification,
message or offer exposure, price presentation, payment path, test integrity, or
safety that would prevent the intended inference. Do not relabel an invalid or
underexposed action as demand failure.

Stop immediately at the first applicable cap or safety boundary. Otherwise stop
at the planned count, timebox, decisive threshold, or point where further actions
cannot change the decision. Review after the smallest diagnostic batch and again
at the final stop. The review must compare planned versus actual exposure,
inspect the first broken selected funnel step, contradicting evidence, and
deviations, then update only the named claim within the predeclared inference
scope. It must also state which adjacent market, audience, payer, or
business-archetype claims the evidence did not update, and must not predeclare a
Stage transition.

## Persistence boundary

An Execution Packet is ephemeral runtime output by default. An unaccepted plan,
draft message, lead list, or exploratory sourcing note causes no workspace write.

Only when the user accepts the Packet as an Experiment does it become durable:
fold the relevant fields into the existing `Exxx` contract in
[object-protocol.md](object-protocol.md#experiment), persist it under the
canonical Experiment location, and apply the mutation and lazy-materialization
rules in [workspace-protocol.md](workspace-protocol.md#mutation-triggers). Do not
create an `EPxxx` object, a standalone Packet/lead/funnel file, a CRM record type,
or a project-root execution file. Later evidence remains linked to that `Exxx`
and the existing decision objects; this protocol does not introduce a new
workspace artifact type or result vocabulary.

Repeated `invalid` or `inconclusive` outcomes do not reset the claim-level evidence budget. Carry forward cumulative time, cost, and repair-review count. Stop repairing the channel when the accepted budget is exhausted; “deprioritize because access was not established within the cap” is a valid decision and is different from `demand_failure`.

## Related authorities

- [Stage model](stage-model.md) owns Stage and the earliest unresolved gate.
- [Experiment Designer](../.agents/skills/experiment-designer/SKILL.md) owns safe
  test design, real-offer preference, downside caps, and experiment criteria.
- [Market Reality Researcher](../.agents/skills/market-reality-researcher/SKILL.md)
  owns decision-scoped external research; its
  [research workflow](../.agents/skills/market-reality-researcher/references/research-workflow.md)
  owns research source selection and coverage.
