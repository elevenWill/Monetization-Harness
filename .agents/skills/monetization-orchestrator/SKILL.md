---
name: monetization-orchestrator
description: Discover, match, bootstrap, resume, determine the evidence-derived Stage and earliest uncertainty, select decision-changing reality evidence, route the minimum Stage-applicable Thinking Skills, and synthesize monetization work. Use for every material opportunity, validation, first-sale, productization, leverage, scaling, or project-resumption conversation in this repository; especially when deciding whether a conversation needs a project, correcting a stage mismatch, deciding whether current external or direct evidence is required, conditionally analyzing a Buying Situation, selecting one or two Thinking Skills, or persisting durable change.
---

# Monetization Orchestrator

Make the conversation primary and the workspace its durable memory. Produce one evidence-grounded judgment and next action. Do not run a persona meeting or ask the user to manage project mechanics.

## Run the project lifecycle

First classify an obvious general-knowledge, Harness-usage, or one-off generic message as **No Project** from the conversation alone; answer it without loading project state or routing references. For a potentially durable monetization thread, read [references/state-assessment.md](references/state-assessment.md), then run the remaining lifecycle:

1. **No Project:** For general knowledge, Harness usage, one-off generic discussion, or a passing brainstorm that is not a concrete resumable monetization thread, answer normally without workspace writes.
2. **Project Matching:** Read `workspace/_index.md`, enumerate actual project roots under `workspace/*/`, then inspect `IDEA.md` and `STATE.md` for plausible candidates. Match semantic continuity in the idea, customer, problem, goal, evidence, and recent conversational context—not keywords alone. Do not assume the registry is complete.
3. **Project Resume:** When one project clearly matches, read its `IDEA.md` and `STATE.md` completely. Follow only links needed for the current gate; do not load all history.
4. **Project Bootstrap:** When no project matches and the user has established a concrete direction worth continuing, generate a stable short kebab-case slug and create only `workspace/<slug>/IDEA.md` and `STATE.md`. Record only user-grounded content, mark missing fields `unknown`, update `workspace/_index.md`, and continue the current answer. Do not request a name, slug, command, template, or manual Stage choice.
5. **Project Conflict:** If multiple projects remain plausible and a mistaken write would matter, give a provisional analysis without writing. Ask for ownership only when persistence or project-specific evidence requires it.

The bootstrap operation never pre-creates stage directories. A stage directory may appear later in the same turn only if that turn contains a separate durable artifact that genuinely belongs there.

After one project is resolved and its Stage is recomputed, read [references/routing-rules.md](references/routing-rules.md). Do not front-load the Stage matrix, object completion schema, Purchase Trigger protocol, market-research references, or unrelated Thinking Skills before their entry condition fires.

## Assess before routing

1. Extract evidence-backed transaction count, repeat-customer count, customer/problem clarity, active experiment, proposed commitment, dependencies, and current stage.
2. Classify decision-relevant records under `docs/object-protocol.md`, loading only the sections for object types active in this decision. Load the completed Experiment/Evidence Ledger section only when reviewing a result; do not front-load every schema.
3. Recompute the stage from `docs/stage-model.md`. Treat the stored stage as a claim to verify and `STATE.md` as the authoritative current-stage location; never infer stage from directories.
4. Find the earliest unsupported gate and name one largest unknown.
5. Decide whether the user's explicit question resolves that unknown. If not, challenge the framing before offering downstream implementation.
6. Read an active `BSxxx` only when it is relevant to the earliest uncertainty. Run its full trigger, deadline, consequence, owner, purchase-window, reachability, trust, recurrence, and liability assessment only when the conditional Why-Now entry rule below is met.

## Select Reality Evidence

After Stage assessment, identify the exact claim that could change the immediate decision and choose the cheapest safe evidence capable of resolving it. Reuse fresh scope-matched evidence first. Prefer the project's own observation, workflow, offer, behavior, payment, usage, delivery, and repeat-customer evidence for claims about this project's demand or transferability. Use the Market Reality Gate only for decision-critical current external facts; it is not a Stage and cannot advance a project by itself.

1. **Mandatory research:** Read and invoke `.agents/skills/market-reality-researcher/SKILL.md` when the answer depends materially on current market existence, exact or adjacent precedents, platform or policy feasibility, current price/competition/supply, acceptance patterns, real trigger/deadline/rush-purchase behavior, Cost of Delay, or a large commitment whose downside depends on those claims. Also invoke it when relevant stored research is absent, stale, or mismatched in market, geography, platform, content type, Buying Situation, or decision scope.
2. **Opportunity quick scan when warranted:** For a newly bootstrapped public-market project, run a bounded scan only when the immediate judgment depends on current market existence, exact/adjacent precedent, platform constraint, visible supply, price, competition, or material negative evidence. Public-market status alone is not a search requirement; when accessible users or workflows can answer the earliest uncertainty directly, take the observation/contact route.
3. **No-search route:** Skip research for Harness-usage questions, internal workspace/state interpretation, user-reported experiment or transaction results, execution details that do not depend on current external facts, or when a fresh scope-matched `Rxxx` already supports the immediate decision. State the no-search basis internally; do not browse merely for ceremony.
4. **Coverage and freshness:** Reuse research only when its checked date, primary market, geography, platforms, content type, and decision scope still match. Recheck time-sensitive platform, price, policy, or competition claims. If a required channel is inaccessible, continue with available evidence but record the actual channels checked and the coverage gap; never imply full-market coverage.
5. **Evidence handoff:** When research runs, classify and persist its material results before routing lenses. Research creates auditable evidence; it does not decide the project stage or replace the project's own behavioral and transaction evidence.

The market researcher is an evidence-producing capability, not a Thinking Skill. It never consumes one of the normal one-or-two lens slots, and its findings must be available to the selected lenses rather than appended after their conclusions. It cannot establish this project's willingness to pay, transferability, repeatability, or delivery economics. When a decision-critical trigger claim depends on external facts, include Event-First searches for real events, deadlines, rush purchases, workarounds, delay consequences, and complaints; distinguish buyer-originated signals from seller-created urgency.

## Run the Why-Now Gate

The full gate is conditional. Run it when purchase timing is material to the earliest uncertainty: normally during `business_validation`, or in any Stage when a concrete Buying Situation, trigger/deadline claim, purchase-window qualification, Deadline Replication Experiment, or deadline-shaped SLA/liability decision controls the action. During `opportunity_discovery`, use only a light scan for an event, recurrence, persistent cost, convenience, identity, entertainment, or risk mechanism unless one of those full-gate conditions is already present. The gate is not a Stage, Persona, or separate agent.

When the full gate is entered, analyze a concrete `BSxxx` or explicit Buying-Situation hypothesis and check all 15 questions in `docs/purchase-trigger-protocol.md`: trigger event; required result date; deadline source and reality; consequence and certainty; consequence owner; alignment with buyer, payer, or budget influencer; current workaround and ability to defer; purchase-window length; reachability inside that window; trust barrier and low-trust entry; recurrence; and delivery liability. Do not create a generic product-level `BSxxx` merely to satisfy routing.

Use `why_now_status: unknown` when evidence is missing. Do not infer `commercial_value: high` from anxiety, urgency language, a seller promotion, or an arbitrary internal target. Classify fabricated scarcity as prohibited. A deadline is a strong signal, not a universal requirement: preserve viable cases based on high-frequency repetition, persistent cost, identity/status, entertainment, convenience, long-term risk, or stable repeat purchase.

When multiple Buying Situations matter, compare them rather than averaging them into a product-level claim. Select `business-filter` when buyer, payer, bought result, offer, alternative, price, recurrence, or the concrete Buying Situation is the current Stage uncertainty; the gate itself does not make that lens globally mandatory.

## Route lenses

Use the eight-Stage matrix in [references/routing-rules.md](references/routing-rules.md). Select its Stage-applicable primary lens, then only the minimum optional lens needed for an independent material uncertainty. The normal total is one or two. Read each selected Skill's `SKILL.md` completely and follow its resource-routing instructions.

- `opportunity-finder`: primary for `opportunity_discovery` when no credible customer/problem pair exists.
- `assumption-challenger`: primary for `problem_validation` and stage-mismatch/framing corrections when unsupported certainty, avoidance, or solution-as-goal blocks the earliest gate.
- `business-filter`: primary for business/offer/repeatability uncertainty—payer, bought result, alternatives, budget, price, recurrence, or a concrete Buying Situation—not a universal first lens.
- `experiment-designer`: primary for experiment validity and scaling bets; required for resignation, major/irreversible commitments, or critical dependencies. Prefer a Deadline Replication Experiment only for a real Buying Situation.
- `leverage-designer`: primary after repeated value/delivery when the uncertainty concerns SOP, automation, capacity, assets, productization, or marginal cost.

Never choose all five or routinely use three. A premature-build framing error plus material commitment normally routes to `assumption-challenger + experiment-designer`; a runtime correction does not require adding `business-filter`. Source Persona names never affect routing.

## Synthesize

1. Collect structured reviews under `docs/review-protocol.md`.
2. Resolve conflicts using the claim-specific evidence rules in `docs/object-protocol.md`, the earliest gate, the active Buying Situation, and downside. Never vote or average opinions. External market cases prove only the claims their scope supports; they do not substitute for this project's trigger, payment, behavior, usage, or repeatability evidence.
3. Return one judgment, the decisive facts/assumptions, and one bounded next action with a stop/review condition. When that action requires a person to observe, source, contact, offer, collect payment, deliver, or run an operating test, read [`docs/human-execution-protocol.md`](../../../docs/human-execution-protocol.md) and emit its minimum Execution Packet. The Packet expands this one action; it does not add a parallel action or default workspace artifact. Keep sourcing, role, channel, price, and qualification unknowns explicit rather than inventing them.
4. Do not list every lens or imitate a Persona. Explain selected lens names only if the user asks or auditability requires it.
5. When current evidence cannot support a conclusion, say exactly what is unknown and design the next evidence-producing action. For deferred implementation, name the evidence that would unlock the smallest necessary technical artifact. For repeated `invalid` or `inconclusive` tests, enforce the accepted claim-level evidence budget and trigger a pause/pivot review when it is exhausted.

## Persist only durable change

Follow `docs/workspace-protocol.md`. Before writing, distinguish an accepted decision from a suggestion. A new project is a mutation trigger; casual discussion is not. When another trigger occurs:

1. decide whether the change needs a standalone artifact or only a snapshot update; completed decision-relevant market research requires an `Rxxx` artifact, a reusable market case requires a linked `Cxxx` artifact, and a concrete decision-relevant Buying Situation requires a `BSxxx` artifact;
2. if an artifact is needed, resolve the exact canonical Stage directory from `docs/workspace-protocol.md`, then create its subdirectory and artifact in the same write—`research/` for RESEARCH, `cases/` for CASE, `buying-situations/` for BUYING SITUATION, and never an empty directory, abbreviated Stage directory, or project-root market/urgency file;
3. update the current snapshot in `STATE.md`, then reconcile older active assumption, decision, market-evidence, and purchase-trigger summaries against the new evidence; when `market_evidence:` is present, also maintain the required current-evidence, latest-research, closest-pattern, policy-status, and coverage-gap Markdown headings; time-qualify historical bases, mark stale or superseded evidence explicitly, and remove contradictory present-tense claims;
4. update `workspace/_index.md` when project/stage/status/next gate/date changes;
5. verify stable IDs, evidence names or links, research scope/freshness/coverage, transaction counters, assumption statuses, decision bases, largest unknown, project-root invariants, empty-directory absence, and link resolution.

Do not silently rewrite `IDEA.md`; record major direction changes and their reasons in stage history. Do not materialize directories merely because `STATE.md` names a stage. Add optional `market_evidence` state only after real research exists and optional `purchase_trigger` state only after a Buying Situation is actually analyzed. During a new-project turn, finish the minimal `IDEA.md` + `STATE.md` bootstrap first; later same-turn Research or Buying Situation writes are separate durable operations in the owning Stage.

## Final response shape

Use compact prose, normally:

```markdown
当前判断：
<one decision>

依据：
<decisive facts and assumptions>

下一步：
<one bounded action and review condition>

Workspace 更新：
<project created or files/objects changed, only when writes occurred>
```

When market research materially affected the answer, also state the closest verified precedent or constraint, what remains unverified, and the main coverage/freshness limitation. Do not claim “the market” was searched when only a subset of channels was accessible.

The final answer must remain understandable if internal Skill reviews are hidden.

When a Human Execution Packet is required, keep its user-visible core concrete even if the surrounding prose is compact: decision claim; qualified target; verified sourcing/query/channel; exact action/message or offer/price; sample/time/cost cap; evidence; stop/review. Do not compress it back to “contact potential users.”
