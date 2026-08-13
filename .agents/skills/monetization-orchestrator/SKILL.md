---
name: monetization-orchestrator
description: Route and synthesize monetization decisions from the active workspace project's goal, evidence, assumptions, stage, transactions, risks, and next gate. Use for every material opportunity, validation, first-sale, productization, leverage, scaling, or project-resumption conversation in this repository; especially when deciding whether to answer the user's requested solution, selecting one or two Thinking Skills, correcting a stage mismatch, or persisting durable state.
---

# Monetization Orchestrator

Produce one evidence-grounded decision and next action. Do not run a persona meeting.

## Restore context

1. Identify the active `workspace/<project>/` from the request or `workspace/_index.md`.
2. Read `IDEA.md` and `STATE.md` completely before routing.
3. Follow links only for evidence needed by the current gate; do not load the entire project history.
4. Read [references/routing-rules.md](references/routing-rules.md) and [references/state-assessment.md](references/state-assessment.md).
5. If no project is active, run a provisional review without writes. Ask for a project only when persistence or project-specific facts are necessary.

## Assess before routing

1. Extract evidence-backed transaction count, repeat-customer count, customer/problem clarity, active experiment, proposed commitment, dependencies, and current stage.
2. Classify every decision-relevant new claim as FACT, ASSUMPTION, DECISION, or EXPERIMENT under `docs/object-protocol.md`.
3. Recompute the stage from `docs/stage-model.md`. Treat the stored stage as a claim to verify.
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

Follow `docs/workspace-protocol.md`. Before writing, distinguish an accepted decision from a suggestion. When a trigger occurs:

1. write detailed evidence/object records in the owning stage directory;
2. update the current snapshot in `STATE.md`;
3. update `workspace/_index.md` when stage/status/next gate/date changes;
4. verify stable IDs, evidence links, project-root invariants, and link resolution.

Do not silently rewrite `IDEA.md`; record major direction changes and their reasons in stage history.

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
<files/objects changed, only when writes occurred>
```

The final answer must remain understandable if internal Skill reviews are hidden.
