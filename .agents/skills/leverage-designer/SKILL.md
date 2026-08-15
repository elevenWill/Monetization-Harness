---
name: leverage-designer
description: Convert repeatedly validated customer value and repeated delivery work into SOPs, reusable knowledge, automation, code, media, and compounding assets with lower marginal delivery cost. Use when repeat customers or repeated paid delivery exist, when recurring deadline demand or a materially similar workflow is evidenced, or when deciding what to automate after transaction validation. Audit capacity peaks, SLA, liability, and automation error before productizing deadline work. Do not use to justify productization before real repeat evidence.
---

# Leverage Designer

Turn proven labor into assets without automating away the value customers pay for.

## Load context

1. Read the active project's `IDEA.md` and `STATE.md` completely.
2. Read repeat-payment evidence, completed experiment results, process notes, delivery costs, and customer feedback.
3. When an external playbook informs the leverage decision, read its latest
   `Rxxx`/`Cxxx`, verification status, disclosed process, required resources,
   platform dependency, failure signals, and transferability limits.
4. Read relevant repeated `BSxxx` records when the demand is trigger- or deadline-shaped.
5. Read [references/domain-core.md](references/domain-core.md).
6. Use [examples/local/monetization-cases.md](examples/local/monetization-cases.md) for sequencing. Use [SOURCE.md](SOURCE.md) when deeper provenance is relevant.

## Entry gate

Require at least one of:

- `transactions.repeat_customers > 0` with linked evidence;
- the same valued paid delivery repeated across independent customers;
- explicit evidence that a repeated internal step, rather than the overall offer, is stable enough to standardize.

If none exists, return a high-severity stage mismatch and route to `business-filter` or `experiment-designer`. Do not treat code written, users signed up, or a founder repeating a task as proof that customer value repeats.

## Workflow

1. Name the single leverage decision that is unclear: value boundary, judgment
   boundary, replication mode, compounding claim, or accountability.
2. Apply only the operator in `domain-core.md` whose trigger matches that
   decision. Use a second only when the first exposes a dependent material
   uncertainty; do not run all five as a lens-specific workflow.
3. Choose one smallest asset and inherit relevant capacity, SLA, liability,
   platform, and API constraints from upstream reviews. Reopen an upstream gate
   only when the proposed asset exposes a contradiction.

## Guardrails

- Do not automate unresolved customer discovery or sales.
- Do not optimize volume before quality and economics are visible.
- Do not erase high-value judgment merely because it is hard to encode.
- Do not introduce brittle single-platform/API dependency without a fallback.
- Do not infer code leverage merely because an external case uses AI.
- Do not infer scalable demand from high rush prices. Synchronized deadlines can create a capacity and liability trap.
- Do not imitate the source persona or turn the answer into general lifestyle philosophy.

## Output

Return one review using `docs/review-protocol.md`. Report the applied operator
and only the fields it changes, plus the smallest asset and review evidence.
Prefer one asset-building step over a full product roadmap; use
`decision_delta: none` when no operator changes the provisional decision.

Pair with `business-filter` if repeatability or unit economics remain doubtful. Productization follows proven SOPs; it is not the starting point.
