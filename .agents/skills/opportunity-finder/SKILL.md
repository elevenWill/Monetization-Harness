---
name: opportunity-finder
description: Find evidence-worthy monetization opportunities in observed problems, repeated manual work, trigger or recurrence clues, existing workarounds, current spend, and domains the user understands. Use for opportunity discovery when the user does not know what to sell, has no clear customer/problem pair, is starting from a technology or trend, or needs to rank problems before validation. Use only a light trigger-mechanism scan unless a concrete Buying Situation is already decision-critical. Do not invent feature-first AI products or productize an already validated repeated transaction.
---

# Opportunity Finder

Find places worth investigating; do not declare a market proven.

## Load context

1. If a project is active, read its `IDEA.md` and `STATE.md` completely.
2. Read the latest linked `Rxxx` market research and decision-relevant `Cxxx`
   cases when they exist. Prefer current exact-scope evidence; keep adjacent,
   vendor-only, stale, and contradicted material labeled as such.
3. Read active `BSxxx` Buying Situations when they exist and preserve unknown trigger, deadline, consequence, reachability, trust, or frequency fields.
4. Read [references/domain-core.md](references/domain-core.md).
5. Read [examples/local/monetization-cases.md](examples/local/monetization-cases.md) when candidate generation or ranking is requested.
6. Consult the preserved source examples/research only when a subtle source model, limitation, or provenance question matters. Start from [SOURCE.md](SOURCE.md).

## Preconditions

Use this lens while the current gate is a credible customer/problem pair. If real payments and a defined buyer already exist, tell the orchestrator this lens is probably stage-misaligned unless the project is deliberately seeking a second opportunity.

Treat trends, market sizes, and the user's enthusiasm as leads, not facts about demand. Never turn a source Persona judgment into evidence.

When the decision depends on current market reality and external research is
missing, stale, or scope-mismatched, return that evidence gap to the orchestrator
for the Market Reality Gate. This Thinking Skill does not perform or simulate the
research itself.

## Workflow

1. Inspect current exact precedents and paid transaction structures in the latest
   market research before inventing a new offer.
2. Inspect negative cases, failed attempts, policy constraints, and incumbent
   alternatives; identify a specific unmet or poorly served gap rather than
   treating category activity as opportunity.
3. Inventory direct access: work the user has done, people they can observe or contact, workflows they understand, and buyers they can reach.
4. Look for behavior: repeated complaints plus continued use, spreadsheets, WeChat/manual coordination, copy-paste, rework, waiting, compliance burden, services already purchased, and tasks someone cannot simply stop doing.
5. Separate observations from interpretations. Label unverified statements provisional assumptions. Never upgrade an adjacent case into an exact precedent.
6. Form small candidates as `narrow customer + concrete situation + costly problem + current workaround + reachable evidence source`.
7. Perform a light trigger-mechanism scan: note whether an event, recurrence,
   persistent cost, convenience, identity/status, entertainment, or long-term
   risk could make the problem more likely to produce buying behavior. Treat each
   as a clue to investigate, not a verified trigger, and do not require the full
   deadline/consequence/payer/purchase-window chain at this Stage.
8. Rank candidates by observed problem cost and repetition, current
   spend/effort, workaround persistence, reachable evidence source, speed to a
   behavioral test, founder/domain fit, and—when current evidence exists—the
   transferability of a paid pattern. A real trigger, reachable payer, or
   low-trust deliverable can strengthen a candidate without becoming a universal
   prerequisite. Do not rank by technical novelty or popularity.
9. Keep non-deadline businesses in consideration when high-frequency repetition,
   persistent cost, convenience, identity/status, entertainment, long-term risk,
   or stable repeat purchase supplies the buying mechanism.
10. Return at most three candidates. Prefer the closest proven, transferable
   transaction structure and one observation/interview/service action over a
   product specification.

## Guardrails

- Do not brainstorm a generic list of AI apps.
- Do not invent a new scheme before checking documented existing patterns,
  failures, substitutes, and gaps when current market evidence is available.
- Do not treat search volume, a vendor case, a stale case, or adjacent success as
  proof of the exact opportunity.
- Do not infer willingness to pay from complaints alone.
- Do not infer a real deadline, high commercial value, or purchase intent from urgency language alone.
- Do not reject an opportunity only because `deadline_type` is `none` or `unknown`.
- Do not reject observable pull solely because no exact precedent or stable workaround exists. Lower confidence, keep `market validated: false`, and prefer one capped exploratory behavior or paid probe when direct access and downside permit it.
- Do not recommend quitting, large builds, or automation.
- Do not require a venture-scale outcome; a manual paid service may be the correct discovery vehicle.
- Do not mimic Paul Graham or name him in the user-facing answer.

## Output

Return one review using `docs/review-protocol.md`. In `finding`, name the best investigation area or explain why no candidate is evidence-worthy. In `recommended_action`, specify whom to observe/contact, what to learn, a small count or timebox, and what evidence would justify business validation.

Coordinate normally with `assumption-challenger` when a technology, trend, identity, or preferred solution is constraining the search.
