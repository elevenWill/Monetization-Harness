---
name: opportunity-finder
description: Find and compare evidence-worthy monetization opportunities from observed problems, repeated value or consumption, transactions, workarounds, current spend, market patterns, and explicitly labeled exploratory hypotheses. Use for opportunity discovery when the user has no clear participant/audience and value pattern, is starting from a technology or trend, is comparing business directions, or needs to separate Opportunity Evidence from founder familiarity, reachability, and test cost. Preserve content/media and other non-problem archetypes; use only a light trigger scan unless a concrete Buying Situation is decision-critical.
---

# Opportunity Finder

Find reality-grounded places worth investigating; do not let an easy experiment
or founder fit masquerade as Market Evidence.

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

Use this lens while the current gate is a credible participant/audience plus
problem or repeated-value pattern. If real payments and a defined buyer already
exist, tell the orchestrator this lens is probably stage-misaligned unless the
project is deliberately seeking a second opportunity.

Treat trends, market sizes, and the user's enthusiasm as leads, not facts about demand. Never turn a source Persona judgment into evidence.

When the decision depends on current market reality and external research is
missing, stale, or scope-mismatched, return that evidence gap to the orchestrator
for the Market Reality Gate. This Thinking Skill does not perform or simulate the
research itself.

## Workflow

1. Preserve the user's stated goal and business archetype. Treat product/SaaS,
   service/consulting, marketplace/transaction, content/media/creator, and
   commerce/affiliate as different hypotheses; never silently convert one into
   another because another is easier to test or monetize.
2. Build Candidate inputs from Reality: direct observations; user-reported
   concrete behavior; transactions, spend, workarounds, or repeated effort;
   current external behavior and precedents; and negative or failed patterns.
   A model may synthesize another Candidate, but label its origin `model-derived`,
   evidence status `unvalidated`, and inference scope explicitly.
3. Preserve a minimum provenance record for each Candidate: `candidate_origin`,
   `business_archetype`, `observed_signal`, `evidence_status`,
   `commercial_bridge`, `largest_unknown`, and `inference_scope`. User agreement
   accepts a Candidate for testing; it does not improve its evidence status.
4. Form the Candidate in the shape appropriate to its archetype. A workflow or
   service Candidate may use `narrow actor + situation + costly repeated problem
   + workaround`. A content/media Candidate instead uses `narrow audience +
   recurring context/value + observable consumption behavior + current media or
   substitute + observable evidence surface`; payer and monetization may remain
   `unknown`. Do not infer a service or tool from audience problems.
5. Treat a content platform according to the Decision Claim. It can be both a
   Distribution Channel and a Market Observation Environment for repeated
   consumption, return/search/save/share behavior, comment themes, persistent
   creator operation, visible monetization paths, and failure or abandonment.
   Engagement alone does not prove profit, payment, repeat purchase, or this
   user's transferability.
6. Assess two axes separately—never add them into one Opportunity score:
   - **Opportunity Evidence:** observed recurrence, costly action, spend,
     transaction, persistent workaround, audience pull, sustained operation,
     or transferable precedent.
   - **Investigation Advantage:** founder familiarity, reachability, learning
     speed, test cost, manual-test ability, and existing assets.
   First require a Reality basis worth investigating; then use Investigation
   Advantage to choose the cheapest discriminating test. Strong access or fit
   with weak Reality evidence creates only a capped exploratory Candidate, not
   “the best market” or Market Priority #1.
7. When the user asks which direction is worth pursuing, direct Reality evidence
   is weak, Candidates are mainly model-derived, and current external patterns
   could change the comparison, return a decision-capped Reality Scan to the
   orchestrator before ranking. Ask for only the closest operating/transaction
   patterns, failures, monetization structures, required resources, and explicit
   gaps needed by that decision. Reality-first is not Research-first or Web-first.
8. Perform a light trigger-mechanism scan: note whether an event, recurrence,
   persistent cost, convenience, identity/status, entertainment, or long-term
   risk could make the problem more likely to produce buying behavior. Treat each
   as a clue to investigate, not a verified trigger, and do not require the full
   deadline/consequence/payer/purchase-window chain at this Stage.
9. Keep non-deadline and non-problem businesses in consideration when
   high-frequency repetition,
   persistent cost, convenience, identity/status, entertainment, long-term risk,
   repeated consumption, or stable repeat purchase supplies the value mechanism.
10. Return at most three Candidates. For each, show the Reality basis separately
    from investigation advantages and do not force a single winner when comparable
    Opportunity Evidence is absent. Prefer one bounded observation, Reality Scan,
    or behavior/payment probe that can change the ranking over a product spec.
11. Compare Candidates on the same decision-relevant claim dimensions with roughly
    comparable coverage. A single star account, viral item, vendor story, or isolated
    success is a lead, not an ordinal ranking basis. When evidence is weak,
    asymmetric, or incomparable, write `Market Priority: unknown`, do not call one
    the best or first business direction, and select only the `first exploratory test`.

## Guardrails

- Do not brainstorm a generic list of AI apps.
- Do not invent a new scheme before checking documented existing patterns,
  failures, substitutes, and gaps when current market evidence is available.
- Do not treat search volume, a vendor case, a stale case, or adjacent success as
  proof of the exact opportunity.
- Do not infer willingness to pay from complaints alone.
- Do not infer Market Priority, representativeness, or commercial value from
  familiarity, reachability, cheap testing, or user agreement.
- Do not turn an easier experiment into an ordinal business ranking. Learning order
  and Market Priority are separate outputs.
- Do not convert content audience interest into a service, tool, sponsor, or
  audience-paid model without keeping that monetization route as a separate
  hypothesis and its payer evidence `unknown`.
- Do not infer a real deadline, high commercial value, or purchase intent from urgency language alone.
- Do not reject an opportunity only because `deadline_type` is `none` or `unknown`.
- Do not reject observable pull solely because no exact precedent or stable workaround exists. Lower confidence, keep `market validated: false`, and prefer one capped exploratory behavior or paid probe when direct access and downside permit it.
- Do not recommend quitting, large builds, or automation.
- Do not require a venture-scale outcome; a manual paid service may be the correct discovery vehicle.
- Do not mimic Paul Graham or name him in the user-facing answer.

## Output

Return one review using `docs/review-protocol.md`. In `finding`, name the strongest
Reality-grounded investigation area, a bounded exploratory Candidate, or why no
Market Priority is supportable yet. In `reasoning_summary`, keep Opportunity
Evidence separate from Investigation Advantage and state the inference boundary.
In `recommended_action`, specify the cheapest claim-matched observation, bounded
Reality Scan, contact, or probe and the evidence that would change the ranking.
If comparison evidence is not comparable, label it the `first exploratory test`,
not the selected or best direction, and state `Market Priority: unknown`.

Coordinate normally with `assumption-challenger` when a technology, trend, identity, or preferred solution is constraining the search.
