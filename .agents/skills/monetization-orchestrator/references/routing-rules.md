# Project lifecycle and Stage-first routing rules

Apply the orchestrator's project lifecycle first. For a matched project, determine the evidence-derived Stage and earliest unresolved uncertainty before choosing evidence or Thinking Skills. These are state rules, not keyword rules.

## Project lifecycle routes

| Conversation state | Runtime route | Workspace behavior |
| --- | --- | --- |
| General knowledge, Harness usage, one-off generic discussion, or passing brainstorm with no clear continuity | No Project | Answer normally; do not create, match, or mutate a project |
| One existing project's idea, customer, problem, goal, evidence, or current action clearly matches | Project Resume | Read its complete `IDEA.md` and `STATE.md`; do not duplicate it |
| Concrete monetization direction worth continuing and no project clearly matches | Project Bootstrap | Generate a stable slug, create only `IDEA.md` + `STATE.md`, update `_index.md`, and continue |
| Multiple projects remain materially plausible and ownership affects durable state | Project Conflict | Analyze provisionally without writing; ask only if ownership is necessary |

Match by semantic continuity, not isolated words. Bootstrap creates no Stage directory. If a later same-turn research, Buying Situation, experiment, transaction, or other durable artifact is actually completed or accepted, persist it separately under its owning canonical Stage.

## Reality Evidence selector

After Stage assessment, name the exact claim that could change the immediate
decision, choose evidence capable of resolving it, then minimize total downside:

1. Reuse fresh, scope-matched project or external evidence when it already supports that claim.
2. Prefer direct observation, workflow artifacts, qualified offers, behavior, payments, usage, delivery, and repeat-customer evidence for claims about this project's problem, willingness to pay, transferability, repeatability, or economics.
3. Invoke `market-reality-researcher` before judgment when the claim depends materially on current market existence, exact/adjacent precedent, platform or policy feasibility, price, competition, supply, acceptance, external trigger behavior, legal constraint, or a major commitment's external downside.
4. In Opportunity Discovery, first normalize Candidates to one decision level.
   Tools, topics, formats, channels, audiences, monetization mechanisms, business
   structures, and offers are not peer directions. Preserve the canonical
   Decision Frame; compare Reality/Opportunity signals separately from founder
   fit, reachability, speed, cost, and assets. If an income-direction comparison
   otherwise rests mainly on model synthesis and current external patterns could
   change it, use a decision-capped scan of observed monetization structures
   before assigning Market Priority.
   Use problem-led evidence when the user has direct actor/workflow experience.
   When the user instead asks for a proven or copyable income path and lacks
   direct domain evidence, reconstruct transaction-bearing cases before cold
   discovery; a Buyer Lead is not a completed playbook.
5. Use a bounded Opportunity quick scan only when one of those current external claims is decision-relevant. A new public-market project does not require search by status alone, and strong direct evidence does not require a ceremonial market scan.
6. Take the no-search route for internal state interpretation, user-reported behavior/transaction results, direct execution that does not depend on current external facts, or fresh scope-matched research with no change signal.

Research is evidence production, not a Thinking Skill. It does not consume a lens slot or promote Stage, and it cannot replace the project's own behavior, payment, repeatability, or delivery evidence. Persist completed decision-relevant research before lens selection; record actual scope, freshness, sources, negative evidence, inaccessible channels, and coverage gaps.

## Trigger routing

During `opportunity_discovery`, perform only a light scan: is there an event, recurrence, persistent cost, convenience, identity, entertainment, or risk mechanism that could make the problem worth investigating? A clue is not a verified Purchase Trigger and does not require a `BSxxx`.

Run the full Why-Now Gate only when purchase timing is material to the earliest uncertainty:

- normally during `business_validation`, where buyer, payer, bought result, alternative, budget, timing, reachability, trust, recurrence, and liability are being resolved;
- in any Stage when a concrete Buying Situation or trigger/deadline claim controls the decision;
- when qualifying buyers inside a purchase window is necessary for a valid offer or transaction test;
- for a Deadline Replication Experiment; or
- for deadline-shaped capacity, SLA, trust, or delivery-liability decisions.

When entered, read `docs/purchase-trigger-protocol.md` and the active `BSxxx`, or use an explicit hypothesis with unsupported links marked `unknown`. Never create a generic product-level Buying Situation for routing ceremony. A deadline is a strong signal, not a requirement; recurring convenience, entertainment, identity, persistent cost, or long-term risk may support purchase without one.

## Canonical Stage routes

The primary and optional lenses are defaults. Select the minimum set that resolves the earliest uncertainty; an optional lens must address an independent material issue.

| Stage | Earliest uncertainty | Reality evidence | Primary lens | Optional lens | Human action | Artifact | Promotion signal | Rollback signal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `opportunity_discovery` | Is there a narrow participant/audience plus reality-grounded problem, repeated-value, or transaction pattern worth investigating? | Problem-led: observed actor/workflow, spend, workarounds, or repeated behavior. Transaction-led: transaction surface, payer, bought result, paid signal, delivery, repeat/continuation, and transferable precedent. Investigation Advantage remains separate | `opportunity-finder` | `assumption-challenger` for model/trend/technology/solution-implies-demand framing | Problem-led: observe or contact the claim-relevant workflow. Transaction-led: reconstruct a case; use targeted contact only for a named playbook gap after bounded public evidence | `Oxxx` with origin, archetype, Reality signal, evidence status, commercial bridge, and inference scope; optional `Rxxx`/`Cxxx` only if research ran; `BSxxx` only if already decision-critical | `defined_problem_and_customer` supported by actor + repeated problem/value, or payer + bought result + transaction-bearing context + meaningful/repeated value; reachability proves testability only | Candidate remains model-/trend-/technology-/vanity-metric-led, changes archetype silently, treats a Lead as a playbook, or conflates audience behavior with payer evidence |
| `problem_validation` | Does the claimed problem occur and matter in observed behavior? | Direct observation, workflow artifacts, workaround use, existing effort/spend, falsifying interviews | `assumption-challenger` | `experiment-designer` for a bounded behavior/falsification test | Observe the workflow or run one test against the named problem assumption | Updated `Fxxx`/`Axxx`; accepted `E001`-series record only for a real experiment | `problem_evidence` from observed project-specific behavior | Evidence contradicts the problem or customer; return to Opportunity or redefine |
| `business_validation` | Who buys and pays, for what result, versus what alternative, through what budget and purchase mechanism? | Real buyer/payer evidence, alternatives/spend, concrete offer/price response; current external price/policy/competition facts when gating; full Why-Now normally applies | `business-filter` | `experiment-designer` for an offer test, or `assumption-challenger` for an independent framing error; never both routinely | Put a bounded result and real price before qualified buyer/payer candidates | Concrete `BSxxx` when analyzed; relevant `Axxx`/`Dxxx`; accepted `E001`-series offer test | `credible_offer` with identifiable payer/result/alternative and falsifiable transaction mechanism | Buyer, value, result, or payment logic becomes unclear; regress to earliest invalid gate |
| `experiment_validation` | What bounded safe test yields enough information to discriminate the single decision-changing assumption? | Qualified exposure, costly commitment, observed use, real offer/payment attempt, validity evidence; current constraints only when test safety/validity depends on them | `experiment-designer` | `business-filter` if payer/price blocks validity, or `assumption-challenger` if the experiment tests the wrong question | Run the accepted bounded experiment with downside cap and review/stop condition | `E001`-series record and linked evidence | `transaction_attempt`: a real interpretable offer/behavior/payment attempt | Test measures interest or an easy proxy instead of the key assumption, or is otherwise invalid/uninterpretable |
| `transaction_validation` | Can real payment and delivery repeat independently under comparable conditions? | Payments, qualified refusals, prices shown, delivery quality/cost, refunds, repeat use and relationship/discount checks | `business-filter` | `experiment-designer` for a replication offer/test | Repeat the bounded offer and delivery with an independent qualified buyer or genuine repeat customer | `Txxx`/`Fxxx`; replication `E001`-series record when accepted; update `BSxxx` only if changed | `repeat_payment` plus materially similar valued delivery | First payment is friendly, subsidized, exceptional, refunded, or undeliverable; return to Business or Experiment Validation |
| `leverage_discovery` | Which repeated delivery step is stable enough to standardize without erasing value or hiding bad economics? | Process timing, judgment, defects, quality, marginal cost, capacity, SLA/liability across repeated paid delivery | `leverage-designer` | `business-filter` for gating recurrence/economics, or `experiment-designer` for a material automation/dependency test | Baseline one bottleneck and test one SOP, template, assisted step, or reusable asset | Non-empty leverage analysis/SOP/asset; optional accepted experiment | `repeatable_delivery_system` preserves result/quality with measured improvement | Repeatability disappears or automation harms value, quality, economics, or survivability |
| `productization` | What minimum product boundary preserves the proven paid result and delivery? | Paid pilots, product-mediated repeat use/purchase, support, quality, retention, cost versus manual baseline | `leverage-designer` | `experiment-designer` for the smallest paid product test; if repeat value already failed, roll back first | Productize one proven step/result and compare it with the manual baseline | Bounded productization analysis plus accepted experiment; no roadmap as evidence | `repeatable_product_value` with plausible economics | Product users do not repeat, pay, or obtain the result; return to `business_validation` or earlier |
| `scaling` | Which acquisition or operating constraint can grow without breaking retention, quality, economics, or survivability? | Channel economics, cohort retention/payment, contribution margin, quality/capacity, refunds, concentration and dependency under a bounded test | `experiment-designer` | `business-filter` for economics/recurrence, or `leverage-designer` for capacity/operations | Run one capped acquisition, capacity, pricing, or dependency-diversification test | Bounded scaling experiment and non-empty economics/capacity analysis | `sustainable_growth` across a larger bounded cohort/channel | Economics, retention, quality, capacity, or dependency breaks; return to earliest invalid Stage |

## Priority and safety corrections

Apply these before answering a later-stage request, without replacing the Stage route:

| Condition | Route | Required correction |
| --- | --- | --- |
| ASSUMPTION presented as FACT, implementation-as-goal, research/build avoidance | `assumption-challenger`; add the Stage action lens only when needed | Reclassify the claim and rebuild the question around the earliest gate |
| Zero transactions plus full SaaS/system/UI/database/agent architecture or months of development | normally `assumption-challenger + experiment-designer` | Treat the build requirement as an assumption; cap a real problem/demand/payment test unless the technical artifact is strictly necessary |
| Resignation, all-in, major spend, long contract/build, critical platform/API/customer dependency, or other plausible ruin | `experiment-designer` is mandatory; `assumption-challenger` may be the second lens for a framing error | Compare a smaller survivable alternative; cap downside and define stop conditions |

Ruin checks are runtime safety, not permission to add a third lens. If business/offer coherence is itself the earliest uncertainty, `business-filter + experiment-designer` is valid; if framing is decisive, use `assumption-challenger + experiment-designer`. Never add a lens for completeness.

When the selected Human Action requires person-supervised Reality Contact, conditionally load `docs/human-execution-protocol.md`; its minimum Packet is the executable form of that one action. When implementation is deferred, name the evidence that unlocks the smallest technical artifact. Cap repeated validity repairs at the claim level so `invalid` or `inconclusive` cannot become an endless loop.

Absence of a precedent or stable workaround lowers confidence but does not reject observable novel pull. When direct access exists and downside is small, prefer one capped exploratory behavior or paid probe over more landscape research; keep `market validated: false` until evidence supports it.

Before any Human Reality Contact, match the Decision Claim, evidence population,
sample source, proof boundary, and material selection/proxy bias. Reachability is
an evidence-acquisition advantage, not representativeness or commercial value.
A more detailed Execution Packet improves attribution and execution only; it
cannot make a weak Candidate more credible. On a transaction-led route, contact
only after bounded public evidence is exhausted, and only to fill a named
decision-critical playbook field.

For Candidate comparison, require roughly comparable dimensions and coverage. A
single star account, viral item, vendor story, or isolated success is a lead. If
evidence is weak, asymmetric, or incomparable, use `Market Priority: unknown`,
omit an ordinal business ranking, and name only the `first exploratory test`.
Before this comparison, normalize mixed-level inputs. For an income goal, compare
observed money structures and map lower-level tools, topics, formats, and channels
into them; do not rank the components themselves as businesses.

For an explicit income goal, an action that consumes several hours or days,
repeated production/publication, meaningful delivery, or material reputation or
opportunity cost must reduce a named commercial-bridge unknown. Require the
success/failure decision change and compare its information value with a smaller
alternative. A single reversible micro probe may still explore audience or value
with monetization unknown. Direct payment/delivery evidence follows its current
Stage without a generic monetization-model scan.
Incomplete reports of several payments also skip that scan, but route first to
bounded transaction verification; do not infer Leverage from unverified counts.

## Lens-count rules

- `market-reality-researcher` is excluded from the count.
- Use one Thinking Skill when it can diagnose the earliest uncertainty and produce the action.
- Use two only for an independent framing, action-design, economics, or safety uncertainty.
- Do not routinely use three and never use all five. Source Persona names never affect routing.

## Derived examples

- New digital-human commerce direction asking whether the market and platform permit it: bootstrap minimally, run bounded external research because current market/policy claims control the judgment, then use `opportunity-finder` and only a light trigger scan. Do not force a full BS or `business-filter`.
- Creator goal with H3, serial drama, and commerce video as mixed-level inputs:
  treat an uncommitted content preference as a hypothesis, normalize to a bounded
  set of operating and failed monetization structures, map those inputs as tools,
  topics, or formats, then select a decision-informative test. Do not silently
  turn the project into a creator service or fund a material audience-only test
  merely because it is easiest.
- Accessible operators report a recurring manual workflow and the next question is whether the problem is real: take the observation route without ceremonial web research; use `assumption-challenger` and optionally a bounded behavior test.
- Zero customers plus “design the database”: use `assumption-challenger + experiment-designer`, not a global business-first three-lens route.
- One genuine payment: record it and enter transaction validation; `business-filter + experiment-designer` may test independent repetition.
- Eight comparable paid deliveries: route directly to `leverage-designer`; add `business-filter` only if recurrence or unit economics gates the decision.
- Product launched but no repeat purchase/value: regress to `business_validation`; investigate bought result and run a bounded offer test rather than adding features.
- Fresh scope-matched `R004` already covers the current platform rule: reuse it and take the no-search route.

## Non-routes

Do not route from isolated words such as “risk,” “business,” “AI,” “lawyer,” “deadline,” or “scale.” Semantic project continuity, evidence-derived Stage, earliest uncertainty, and downside control the route.
