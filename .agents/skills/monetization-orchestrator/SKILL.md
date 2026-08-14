---
name: monetization-orchestrator
description: Discover, match, bootstrap, resume, run the Market Reality and Why-Now Gates, route, and synthesize monetization work from conversation, workspace, and current external evidence. Use for every material opportunity, validation, first-sale, productization, leverage, scaling, or project-resumption conversation in this repository; especially when deciding whether a conversation needs a project, matching it to an existing project, creating minimal IDEA.md and STATE.md state, correcting a stage mismatch, deciding whether current market or purchase-trigger research is required, comparing Buying Situations, selecting one or two Thinking Skills, or persisting durable change.
---

# Monetization Orchestrator

Make the conversation primary and the workspace its durable memory. Produce one evidence-grounded judgment and next action. Do not run a persona meeting or ask the user to manage project mechanics.

## Run the project lifecycle

Read [references/routing-rules.md](references/routing-rules.md) and [references/state-assessment.md](references/state-assessment.md), then classify the message before selecting Thinking Skills:

1. **No Project:** For general knowledge, Harness usage, one-off generic discussion, or a passing brainstorm that is not a concrete resumable monetization thread, answer normally without workspace writes.
2. **Project Matching:** Read `workspace/_index.md`, enumerate actual project roots under `workspace/*/`, then inspect `IDEA.md` and `STATE.md` for plausible candidates. Match semantic continuity in the idea, customer, problem, goal, evidence, and recent conversational context—not keywords alone. Do not assume the registry is complete.
3. **Project Resume:** When one project clearly matches, read its `IDEA.md` and `STATE.md` completely. Follow only links needed for the current gate; do not load all history.
4. **Project Bootstrap:** When no project matches and the user has established a concrete direction worth continuing, generate a stable short kebab-case slug and create only `workspace/<slug>/IDEA.md` and `STATE.md`. Record only user-grounded content, mark missing fields `unknown`, update `workspace/_index.md`, and continue the current answer. Do not request a name, slug, command, template, or manual Stage choice.
5. **Project Conflict:** If multiple projects remain plausible and a mistaken write would matter, give a provisional analysis without writing. Ask for ownership only when persistence or project-specific evidence requires it.

The bootstrap operation never pre-creates stage directories. A stage directory may appear later in the same turn only if that turn contains a separate durable artifact that genuinely belongs there.

## Assess before routing

1. Extract evidence-backed transaction count, repeat-customer count, customer/problem clarity, active experiment, proposed commitment, dependencies, and current stage.
2. Classify every decision-relevant record under `docs/object-protocol.md`, including FACT, ASSUMPTION, DECISION, EXPERIMENT, TRANSACTION, RESEARCH, CASE, and BUYING SITUATION.
3. Recompute the stage from `docs/stage-model.md`. Treat the stored stage as a claim to verify and `STATE.md` as the authoritative current-stage location; never infer stage from directories.
4. Find the earliest unsupported gate and name one largest unknown.
5. Decide whether the user's explicit question resolves that unknown. If not, challenge the framing before offering downstream implementation.
6. Read any active `BSxxx` and assess its trigger, deadline, consequence, owner, purchase window, reachability, trust barrier, recurrence, and delivery liability under `docs/purchase-trigger-protocol.md`.

## Run the Market Reality Gate

Run this gate after stage assessment and before selecting Thinking Skills. The gate determines whether current external evidence is needed for the immediate judgment; it is not a Stage and cannot advance a project by itself.

1. **Mandatory research:** Read and invoke `.agents/skills/market-reality-researcher/SKILL.md` when the answer depends materially on current market existence, exact or adjacent precedents, platform or policy feasibility, current price/competition/supply, acceptance patterns, real trigger/deadline/rush-purchase behavior, Cost of Delay, or a large commitment whose downside depends on those claims. Also invoke it when relevant stored research is absent, stale, or mismatched in market, geography, platform, content type, Buying Situation, or decision scope.
2. **Bootstrap quick scan:** For a newly bootstrapped project aimed at a public market, run a bounded scan for one exact precedent, the most obvious platform constraint, visible supply saturation, material negative evidence, and whether deeper research is warranted. Do not turn the quick scan into an exhaustive landscape.
3. **No-search route:** Skip research for Harness-usage questions, internal workspace/state interpretation, user-reported experiment or transaction results, execution details that do not depend on current external facts, or when a fresh scope-matched `Rxxx` already supports the immediate decision. State the no-search basis internally; do not browse merely for ceremony.
4. **Coverage and freshness:** Reuse research only when its checked date, primary market, geography, platforms, content type, and decision scope still match. Recheck time-sensitive platform, price, policy, or competition claims. If a required channel is inaccessible, continue with available evidence but record the actual channels checked and the coverage gap; never imply full-market coverage.
5. **Evidence handoff:** When research runs, classify and persist its material results before routing lenses. Research creates auditable evidence; it does not decide the project stage or replace the project's own behavioral and transaction evidence.

The market researcher is an evidence-producing capability, not a Thinking Skill. It never consumes one of the normal one-or-two lens slots, and its findings must be available to the selected lenses rather than appended after their conclusions. When why-now depends on external facts, include Event-First searches for real trigger events, deadlines, rush purchases, workarounds, delay consequences, and complaints; distinguish buyer-originated signals from seller-created urgency.

## Run the Why-Now Gate

Run this gate after relevant Market Reality evidence is available and before selecting Thinking Skills. It answers what would cause a buyer to purchase within a concrete window; it is not a Stage, Persona, or separate agent.

For each material opportunity, identify or create a hypothesis for a concrete `BSxxx` and check all 15 questions in `docs/purchase-trigger-protocol.md`: trigger event; required result date; deadline source and reality; consequence and certainty; consequence owner; alignment with buyer, payer, or budget influencer; current workaround and ability to defer; purchase-window length; reachability inside that window; trust barrier and low-trust entry; recurrence; and delivery liability.

Use `why_now_status: unknown` when evidence is missing. Do not infer `commercial_value: high` from anxiety, urgency language, a seller promotion, or an arbitrary internal target. Classify fabricated scarcity as prohibited. A deadline is a strong signal, not a universal requirement: preserve viable cases based on high-frequency repetition, persistent cost, identity/status, entertainment, convenience, long-term risk, or stable repeat purchase.

For each leading concrete Opportunity, run `business-filter` immediately after this gate, even when the trigger chain is incomplete and its correct outcome is `no_clear_why_now`. Pass the active `BSxxx` or an explicit Buying-Situation hypothesis with unsupported fields marked `unknown`. Compare multiple Buying Situations within one project rather than averaging them into a product-level claim. Prefer the situation combining a repeatable real trigger, material consequence, aligned budget owner, observable leading signal, reachable payer, feasible low-trust entry, and bounded delivery risk.

## Route lenses

`business-filter` is the first selected Thinking Skill for each leading concrete Opportunity and consumes one lens slot. After its outcome, select only the minimum optional additional lens needed to correct framing or create the action. The normal total remains one or two. Read each selected Skill's `SKILL.md` completely and follow its resource-routing instructions.

- `opportunity-finder`: no credible customer/problem pair.
- `assumption-challenger`: unsupported certainty, wrong question, avoidance, or solution-as-goal.
- `business-filter`: mandatory first lens for each leading concrete Opportunity—payer, bought result, trigger, deadline reality, cost of delay, consequence owner, purchase window, budget path, trust, reachability, liability, price, or recurrence; return `no_clear_why_now` rather than skipping it when evidence is absent.
- `experiment-designer`: turn the largest assumption into a cheap safe test; prefer a Deadline Replication Experiment for a real Buying Situation and require it for large commitments or ruin risk.
- `leverage-designer`: repeat value/delivery exists and the question concerns SOP, automation, deadline capacity peaks, SLA design, assets, productization, or marginal cost.

Never choose all five. Use three only when three independently material conditions exist and omitting one creates a decision error; state that reason in the internal synthesis. Source Persona names never affect routing.

## Synthesize

1. Collect structured reviews under `docs/review-protocol.md`.
2. Resolve conflicts using the claim-specific evidence rules in `docs/object-protocol.md`, the earliest gate, the active Buying Situation, and downside. Never vote or average opinions. External market cases prove only the claims their scope supports; they do not substitute for this project's trigger, payment, behavior, usage, or repeatability evidence.
3. Return one judgment, the decisive facts/assumptions, and one bounded next action with a stop/review condition.
4. Do not list every lens or imitate a Persona. Explain selected lens names only if the user asks or auditability requires it.
5. When current evidence cannot support a conclusion, say exactly what is unknown and design the next evidence-producing action.

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
