# Project lifecycle and evidence-based routing rules

Apply project lifecycle rules before Thinking Skill routes. For an active project, apply the first matching high-priority correction, then add at most one lens that produces the needed action. These are state rules, not keyword rules.

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

## Priority overrides

| State condition | Required routing | Correction |
| --- | --- | --- |
| Plausible ruin, resignation, all-in, major/long commitment, single critical dependency | `experiment-designer` mandatory; add `assumption-challenger` if the commitment rests on an unsupported premise | Compare a survivable staged alternative before proceeding |
| `transactions.total == 0` and user proposes full SaaS/system/UI/database/agent architecture or months of development | `assumption-challenger` + `experiment-designer` | The largest unknown is transaction/demand, unless the small technical work is necessary to test it |
| Any ASSUMPTION is represented as FACT, or implementation becomes the goal | `assumption-challenger` mandatory; add the stage lens that produces evidence | Reclassify the claim and rebuild the question |

## Stage routes

| Evidence state | Primary routing | Goal |
| --- | --- | --- |
| No clear customer, problem, or only a broad trend | `opportunity-finder` + usually `assumption-challenger` | Find an observable problem and reachable user |
| Customer/problem plausible, zero payment, no premature-build override | `business-filter` + `experiment-designer` | Make a coherent offer and test the decisive assumption |
| Exactly one or only exceptional first payment; no repeat customer | `business-filter` + `experiment-designer` | Determine whether payment can repeat independently |
| Repeated purchases or repeated paid delivery, asking about process/automation | `leverage-designer`; add `business-filter` only if recurrence/economics are doubtful | Convert stable work into a measured reusable asset |
| Product launched but no repeat purchase/value | `business-filter` + `experiment-designer`; regress to `business_validation` or earlier | Repair repeat value, not features |
| Repeatable product value and plausible economics | Lens tied to the largest scaling uncertainty; keep `experiment-designer` for large bets | Test acquisition/economics without hidden ruin |

## Lens count

- One lens when one uncertainty dominates and no correction is needed.
- Two lenses when one diagnoses and one creates the next action, or when business logic and experiment design are inseparable.
- Three lenses only if a critical downside, an independent framing error, and an independent business-model unknown all materially affect the immediate decision. Record the reason. Never add a lens for “completeness.”

## Routing examples

- New concrete short-video direction with no existing match: bootstrap only `IDEA.md` + `STATE.md`, then use `opportunity-finder` and, if trend implies assumed demand, `assumption-challenger`.
- Existing lawyer project + a newly reported CNY 500 payment: resume it; record the payment durably; route `business-filter` + `experiment-designer`, not `leverage-designer`.
- Zero customers + “design the database”: `assumption-challenger` + `experiment-designer`, not database design.
- Programmer with no direction: `opportunity-finder` + `assumption-challenger`; create a project only after a concrete thread is established.
- Eight repeat buyers, similar delivery: `leverage-designer`; add `business-filter` only if margins or independence are unclear.
- Productization stage but repeat purchases disappear: regress to `business_validation`; route `business-filter` + `experiment-designer`.

## Non-routes

Do not route or match from isolated words such as “risk,” “business,” “AI,” “lawyer,” or “scale.” A risk question about a repeatedly purchased workflow may need leverage; a “scale” request with zero payments needs challenge and experiment. State and semantic continuity win over vocabulary.
