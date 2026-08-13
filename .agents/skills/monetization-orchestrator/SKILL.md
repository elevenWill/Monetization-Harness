---
name: monetization-orchestrator
description: Discover, match, bootstrap, resume, route, and synthesize monetization work from the conversation and workspace evidence. Use for every material opportunity, validation, first-sale, productization, leverage, scaling, or project-resumption conversation in this repository; especially when deciding whether a conversation needs a project, matching it to an existing project, creating minimal IDEA.md and STATE.md state, correcting a stage mismatch, selecting one or two Thinking Skills, or persisting durable change.
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
2. Classify every decision-relevant new claim as FACT, ASSUMPTION, DECISION, or EXPERIMENT under `docs/object-protocol.md`.
3. Recompute the stage from `docs/stage-model.md`. Treat the stored stage as a claim to verify and `STATE.md` as the authoritative current-stage location; never infer stage from directories.
4. Find the earliest unsupported gate and name one largest unknown.
5. Decide whether the user's explicit question resolves that unknown. If not, challenge the framing before offering downstream implementation.

## Route lenses

Select the minimum sufficient set—normally one or two. Read each selected Skill's `SKILL.md` completely and follow its resource-routing instructions.

- `opportunity-finder`: no credible customer/problem pair.
- `assumption-challenger`: unsupported certainty, wrong question, avoidance, or solution-as-goal.
- `business-filter`: payer, bought result, alternatives, price, recurrence, or business-model uncertainty.
- `experiment-designer`: turn the largest assumption into a cheap safe test; mandatory for large commitments or ruin risk.
- `leverage-designer`: repeat value/delivery exists and the question concerns SOP, automation, assets, productization, or marginal cost.

Never choose all five. Use three only when three independently material conditions exist and omitting one creates a decision error; state that reason in the internal synthesis. Source Persona names never affect routing.

## Synthesize

1. Collect structured reviews under `docs/review-protocol.md`.
2. Resolve conflicts using evidence strength, earliest gate, and downside. Never vote or average opinions.
3. Return one judgment, the decisive facts/assumptions, and one bounded next action with a stop/review condition.
4. Do not list every lens or imitate a Persona. Explain selected lens names only if the user asks or auditability requires it.
5. When current evidence cannot support a conclusion, say exactly what is unknown and design the next evidence-producing action.

## Persist only durable change

Follow `docs/workspace-protocol.md`. Before writing, distinguish an accepted decision from a suggestion. A new project is a mutation trigger; casual discussion is not. When another trigger occurs:

1. decide whether the change needs a standalone artifact or only a snapshot update;
2. if an artifact is needed, create its owning stage directory and the artifact in the same write—never create an empty directory;
3. update the current snapshot in `STATE.md`, then reconcile older active assumption and decision summaries against the new evidence; time-qualify historical bases and remove contradictory present-tense claims;
4. update `workspace/_index.md` when project/stage/status/next gate/date changes;
5. verify stable IDs, evidence names or links, transaction counters, assumption statuses, decision bases, largest unknown, project-root invariants, empty-directory absence, and link resolution.

Do not silently rewrite `IDEA.md`; record major direction changes and their reasons in stage history. Do not materialize directories merely because `STATE.md` names a stage.

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

The final answer must remain understandable if internal Skill reviews are hidden.
