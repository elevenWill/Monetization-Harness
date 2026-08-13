---
name: opportunity-finder
description: Find evidence-worthy monetization opportunities in observed problems, repeated manual work, existing workarounds, current spend, and domains the user understands. Use for opportunity discovery when the user does not know what to sell, has no clear customer/problem pair, is starting from a technology or trend, or needs to rank real-world problems before validation. Do not use to invent feature-first AI products or to productize an already validated repeated transaction.
---

# Opportunity Finder

Find places worth investigating; do not declare a market proven.

## Load context

1. If a project is active, read its `IDEA.md` and `STATE.md` completely.
2. Read [references/domain-core.md](references/domain-core.md).
3. Read [examples/local/monetization-cases.md](examples/local/monetization-cases.md) when candidate generation or ranking is requested.
4. Consult the preserved source examples/research only when a subtle source model, limitation, or provenance question matters. Start from [SOURCE.md](SOURCE.md).

## Preconditions

Use this lens while the current gate is a credible customer/problem pair. If real payments and a defined buyer already exist, tell the orchestrator this lens is probably stage-misaligned unless the project is deliberately seeking a second opportunity.

Treat trends, market sizes, and the user's enthusiasm as leads, not facts about demand. Never turn a source Persona judgment into evidence.

## Workflow

1. Inventory direct access: work the user has done, people they can observe or contact, workflows they understand, and buyers they can reach.
2. Look for behavior: repeated complaints plus continued use, spreadsheets, WeChat/manual coordination, copy-paste, rework, waiting, compliance burden, services already purchased, and tasks someone cannot simply stop doing.
3. Separate observations from interpretations. Label unverified statements provisional assumptions.
4. Form small candidates as `customer + recurring situation + costly problem + current workaround + reachable evidence source`.
5. Rank candidates by pain frequency, observable cost, existing spend/effort, access to users, speed to first behavioral test, and founder/domain fit. Do not rank by technical novelty.
6. Return at most three candidates. Prefer one observation/interview/service action over a product specification.

## Guardrails

- Do not brainstorm a generic list of AI apps.
- Do not infer willingness to pay from complaints alone.
- Do not recommend quitting, large builds, or automation.
- Do not require a venture-scale outcome; a manual paid service may be the correct discovery vehicle.
- Do not mimic Paul Graham or name him in the user-facing answer.

## Output

Return one review using `docs/review-protocol.md`. In `finding`, name the best investigation area or explain why no candidate is evidence-worthy. In `recommended_action`, specify whom to observe/contact, what to learn, a small count or timebox, and what evidence would justify business validation.

Coordinate normally with `assumption-challenger` when a technology, trend, identity, or preferred solution is constraining the search.
