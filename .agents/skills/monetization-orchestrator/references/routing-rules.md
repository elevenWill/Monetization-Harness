# Project lifecycle and evidence-based routing rules

Apply project lifecycle rules first, then the Market Reality Gate, then the Why-Now Gate, and only then Thinking Skill routes. For an active project, apply the first matching high-priority correction, then add at most one lens that produces the needed action. These are state rules, not keyword rules.

## Project lifecycle routes

| Conversation state | Runtime route | Workspace behavior |
| --- | --- | --- |
| General knowledge, Harness usage, one-off generic discussion, or a passing brainstorm with no clear intent to continue | No Project | Answer normally; do not create, match, or mutate a project |
| One existing project's idea, customer, problem, goal, evidence, or ongoing action clearly matches | Project Resume | Read its `IDEA.md` and `STATE.md`; continue without creating a duplicate |
| Concrete monetization direction worth continued exploration and no existing project clearly matches | Project Bootstrap | Generate a slug, create only `IDEA.md` + `STATE.md`, update `_index.md`, and continue the answer |
| Two or more projects remain materially plausible and the choice affects durable state | Project Conflict | Analyze provisionally without writing; ask only if ownership is necessary |

Passing idea versus project is a judgment about continuity, not message length. “What pricing models exist?” is normally No Project. “I keep seeing lawyers struggle with case files and want to investigate whether I can sell a solution” establishes a resumable thread.

Match by meaning, not a single shared word. Prefer, in order: an explicit project reference; continuity within the current conversation; a distinctive customer/problem or evidence event; the same goal/offer/domain; then recency. Before creating, inspect `_index.md`, enumerate actual project roots, and read plausible project `IDEA.md`/`STATE.md` files. Treat the registry as navigation rather than proof that no other project exists. Never create `topic-2` merely because the user phrased the existing topic differently.

## Bootstrap rules

- Derive a lowercase ASCII short-kebab-case slug from the idea, such as `AI 带货短视频` → `ai-commerce-short-video`.
- Treat the slug as the stable internal ID. The user does not choose it, and a display-name change does not rename it.
- If the slug is occupied by the same topic, resume it. If it is a genuinely different project, append the first available deterministic suffix (`-2`, `-3`, ...).
- Create only `IDEA.md` and `STATE.md` during bootstrap. Do not copy a template tree or create a Stage directory.
- Default to `opportunity_discovery` only when no stronger evidence supports a later stage. Use `unknown` instead of inventing customers, payment counts, or goals.
- Add the registry entry and continue the user's substantive discussion in the same turn.

The bootstrap operation itself ends after those two project files and the registry update. If the Market Reality Gate then requires a quick scan or deeper research, treat that as a separate same-turn operation: conduct real research first, then create the current stage's non-empty `research/` directory together with its first `Rxxx` artifact. Do not pre-create the directory or add empty market fields during bootstrap.

## Market Reality Gate

Run the gate after the largest unknown and framing check are known, but before choosing Thinking Skills. Market research supplies evidence to the lenses; it is not a lens, does not consume the normal lens allowance, and is never a substitute for stage-specific behavioral or transaction evidence.

### Mandatory research route

Invoke `market-reality-researcher` when the immediate judgment materially depends on one or more of these current external claims:

- whether a market, paid behavior, exact precedent, or credible adjacent precedent exists;
- platform, policy, format, distribution, account, API, payment, or legal-operability constraints;
- current competitors, substitutes, prices, supply density, content patterns, acceptance, or negative market signals;
- whether a copied case or market-entry plan transfers to the project's geography, platform, customer, and content type;
- a major spend, long commitment, resignation, all-in move, or critical dependency whose downside changes with market reality;
- an external claim for which no relevant research exists, or whose prior evidence is stale, materially incomplete, contradicted, or mismatched in scope.

Time-sensitive claims about platform rules, prices, availability, policy, and competitive conditions require a fresh check even when an older artifact exists. Prefer first-party sources for rules and policies and observed market artifacts for actual behavior. Record inaccessible channels and degraded fallbacks; never infer inaccessible-channel results from a general web search.

### Bootstrap quick-scan route

For a newly bootstrapped project that targets a public market, perform a bounded scan before the Thinking Skills assess the opportunity. Seek only enough evidence to answer:

1. Is there at least one exact precedent? If not, what is the closest adjacent precedent and why is it not exact?
2. Is there an obvious platform, policy, or delivery constraint?
3. Is visible supply already dense or commoditized in the scoped market?
4. Is there material negative or contradictory evidence?
5. Does the largest unknown justify deeper research now?

This is a quick scan, not a claim of exhaustive coverage. Persist it only after actual research as an `Rxxx` artifact, with any reusable `Cxxx` cases linked from it.

### No-search route

Do not invoke the researcher when the answer is limited to:

- Harness usage, Skill distinctions, repository protocol, or internal project-state interpretation;
- user-reported experiment, interview, delivery, transaction, or metric results that need classification rather than external verification;
- an execution detail whose correctness does not depend on current external market facts;
- a decision already supported by a fresh `Rxxx` whose market, geography, platforms, content type, and decision scope match, with no material time-sensitive change.

Record the no-search basis in the internal route. “Research would be nice” is not enough to search, and “we researched before” is not enough to reuse stale or scope-mismatched evidence.

### Research handoff

Research must finish before lens selection. Classify durable results as `Rxxx`, `Cxxx`, and supported or contradicted FACT/ASSUMPTION updates; reconcile `STATE.md` freshness and coverage; then give those results to the Thinking Skills. If required research cannot achieve essential coverage, the correct conclusion may be “unknown” plus a bounded access or field-test action.

## Why-Now Gate

Run after research handoff and before lens selection for every material opportunity. Read `docs/purchase-trigger-protocol.md` and any active `BSxxx`. If no concrete situation exists, hold it as a hypothesis rather than forcing a generic product-level answer. Then run `business-filter` as the first Thinking Skill against that object or hypothesis; do not skip it merely because the result may be `no_clear_why_now`.

Check, in order: trigger event; required result date/window; deadline source and whether it can move; consequence of delay and its certainty; consequence owner; alignment with buyer/payer/budget influencer; workaround and ability to defer; purchase-window length; reachability before it closes; trust requirement and low-trust entry; recurrence; and delivery liability. Missing evidence means `why_now_status: unknown`, not high commercial value.

Classify the situation with the smallest fitting business-filter outcome:

| Evidence state | Why-now route |
| --- | --- |
| Real recurring trigger, meaningful consequence, aligned/reachable payer, viable trust entry | `recurring_deadline_opportunity` and `business-filter` |
| Real one-time trigger and purchasable result | `one_off_rush_service`; test price without inferring durable recurrence |
| Urgent task but stranger access or proof burden blocks purchase | `urgent_but_low_trust`; design low-trust entry or stop |
| Preferred date with no material consequence | `deadline_without_consequence` |
| Valuable outcome but payer cannot be reached in-window | `high_value_but_unreachable` |
| Seller-created promotion or fabricated scarcity | `manufactured_urgency`; never recommend deception |
| Severe buyer consequence plus unacceptable delivery downside | `high_liability_opportunity`; cap scope/liability or stop |
| No supported trigger or non-deadline purchase mechanism yet | `no_clear_why_now`; retain `unknown` and test |

Deadlines are not required for every valid business. A repeat purchase driven by persistent cost, convenience, entertainment, identity/status, or long-term risk can continue through the normal business route when supported by evidence.

## Priority overrides

| State condition | Required routing | Correction |
| --- | --- | --- |
| Plausible ruin, resignation, all-in, major/long commitment, single critical dependency | `business-filter` first, then `experiment-designer`; add `assumption-challenger` as an exceptional third total lens only when an independent framing error and an independent business-model unknown also affect the decision | Compare a survivable staged alternative before proceeding |
| `transactions.total == 0` and user proposes full SaaS/system/UI/database/agent architecture or months of development | `business-filter` first, then `assumption-challenger` and `experiment-designer` as an explicit exceptional three-lens route: the business-model unknown, framing error, and material commitment downside are independent | The largest unknown is transaction/demand, unless the small technical work is necessary to test it |
| Any ASSUMPTION is represented as FACT, or implementation becomes the goal | `business-filter` first, then `assumption-challenger`; add `experiment-designer` only when a material commitment downside and an independent business-model unknown also affect the decision, and state all three reasons for the exceptional route | Reclassify the claim and rebuild the question |

## Stage routes

| Evidence state | Primary routing | Goal |
| --- | --- | --- |
| No leading concrete Opportunity yet; no clear customer/problem or only a broad trend | `opportunity-finder`; after it identifies a leading concrete candidate, run its Buying Situation through `business-filter`; add `assumption-challenger` only for an independent framing error | Find an observable problem and reachable user, then test its buying logic |
| Customer/problem plausible, zero payment, no premature-build override | `business-filter` + `experiment-designer` | Make a coherent offer and test the decisive assumption |
| Exactly one or only exceptional first payment; no repeat customer | `business-filter` + `experiment-designer` | Determine whether payment can repeat independently |
| Repeated purchases or repeated paid delivery, asking about process/automation | `business-filter` first, then `leverage-designer` | Reconfirm recurrence/economics and convert stable work into a measured reusable asset |
| Product launched but no repeat purchase/value | `business-filter` + `experiment-designer`; regress to `business_validation` or earlier | Repair repeat value, not features |
| Repeatable product value and plausible economics | `business-filter` first, then the lens tied to the largest scaling uncertainty; use `experiment-designer` for large bets | Test acquisition/economics without hidden ruin |

## Lens count

- `market-reality-researcher` is an evidence capability and is excluded from this count.
- The Why-Now Gate is routing logic, not a lens. `business-filter` is the mandatory first lens for a leading concrete Opportunity and counts as one Thinking Skill.
- One lens when `business-filter` can both diagnose the Buying Situation and produce the next action.
- Two lenses when `business-filter` diagnoses and one additional lens creates the action or corrects an independent framing error.
- Three lenses only if a material commitment downside, an independent framing error, and an independent business-model unknown all affect the immediate decision. Record the reason. Never add a lens for “completeness.”

## Routing examples

- New concrete short-video direction with no existing match: bootstrap only `IDEA.md` + `STATE.md`; as a separate same-turn operation, run and persist the bounded public-market quick scan; run the leading Buying Situation through `business-filter`, then add `assumption-challenger` only if trend still implies assumed demand.
- Existing lawyer project + a newly reported CNY 500 payment: resume it; record the payment durably; route `business-filter` + `experiment-designer`, not `leverage-designer`.
- Zero customers + “design the database”: `business-filter` first. For a cheap sketch, add `assumption-challenger`; for a material build commitment, use the explicit exceptional `business-filter` + `assumption-challenger` + `experiment-designer` route and state the three independent reasons.
- Programmer with no direction: use `opportunity-finder` before a concrete project exists; after it identifies a leading concrete candidate, run `business-filter`, with `assumption-challenger` only if a separate framing error remains.
- Eight repeat buyers, similar delivery: `business-filter` first to confirm trigger/recurrence/economics, then `leverage-designer`.
- Productization stage but repeat purchases disappear: regress to `business_validation`; route `business-filter` + `experiment-designer`.
- Fresh scope-matched `R004` already covers the current platform rule and no change signal exists: reuse it, record the no-search route, and proceed to the minimum Thinking Skills.
- A six-month-old platform-policy claim controls a planned major spend: research is mandatory, then `business-filter`, then `experiment-designer`, even if the old artifact once had strong sources.

## Non-routes

Do not route or match from isolated words such as “risk,” “business,” “AI,” “lawyer,” or “scale.” A risk question about a repeatedly purchased workflow may need `business-filter` then leverage; a “scale” request with zero payments runs `business-filter` first, then challenge and experiment only under the explicit exceptional three-lens conditions above. State and semantic continuity win over vocabulary.
