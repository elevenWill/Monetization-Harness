# Evidence-based routing rules

Apply the first matching high-priority correction, then add at most one lens that produces the needed action. These are state rules, not keyword rules.

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

- Zero customers + “design the database”: `assumption-challenger` + `experiment-designer`, not database design.
- Programmer with no direction: `opportunity-finder` + `assumption-challenger`.
- One CNY 500 lawyer payment: `business-filter` + `experiment-designer`, not `leverage-designer`.
- Eight repeat buyers, similar delivery: `leverage-designer`; add `business-filter` only if margins or independence are unclear.
- Productization stage but repeat purchases disappear: regress to `business_validation`; route `business-filter` + `experiment-designer`.

## Non-routes

Do not route from the presence of words such as “risk,” “business,” “AI,” or “scale.” A risk question about a repeatedly purchased workflow may need leverage; a “scale” request with zero payments needs challenge and experiment. State wins over vocabulary.
