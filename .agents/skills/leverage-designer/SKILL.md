---
name: leverage-designer
description: Convert repeatedly validated customer value and repeated delivery work into SOPs, reusable knowledge, automation, code, media, and compounding assets with lower marginal delivery cost. Use when repeat customers or repeated paid delivery exist, when the workflow is materially similar across customers, or when deciding what to automate after transaction validation. Do not use to justify productization before real repeat evidence.
---

# Leverage Designer

Turn proven labor into assets without automating away the value customers pay for.

## Load context

1. Read the active project's `IDEA.md` and `STATE.md` completely.
2. Read repeat-payment evidence, completed experiment results, process notes, delivery costs, and customer feedback.
3. Read [references/domain-core.md](references/domain-core.md).
4. Use [examples/local/monetization-cases.md](examples/local/monetization-cases.md) for sequencing. Use [SOURCE.md](SOURCE.md) when deeper provenance is relevant.

## Entry gate

Require at least one of:

- `transactions.repeat_customers > 0` with linked evidence;
- the same valued paid delivery repeated across independent customers;
- explicit evidence that a repeated internal step, rather than the overall offer, is stable enough to standardize.

If none exists, return a high-severity stage mismatch and route to `business-filter` or `experiment-designer`. Do not treat code written, users signed up, or a founder repeating a task as proof that customer value repeats.

## Workflow

1. Separate the proven customer outcome from the current delivery method.
2. Map each delivery step: input, operator judgment, time/cost, variance, failure modes, and customer-visible value.
3. Identify specific knowledge: the judgment that differentiates the result and should be captured or protected rather than blindly automated.
4. Classify steps as `keep_human`, `standardize`, `template`, `delegate`, `ai_assist`, `automate_with_code`, or `publish_as_media`.
5. Sequence leverage: manual service → documented process → SOP/template → assisted execution → tested automation → bounded product.
6. Estimate the effect on marginal cost, quality, cycle time, learning, dependency, and customer outcome.
7. Automate one bottleneck at a time and compare against a pre-automation baseline. Keep a rollback path.

## Guardrails

- Do not automate unresolved customer discovery or sales.
- Do not optimize volume before quality and economics are visible.
- Do not erase high-value judgment merely because it is hard to encode.
- Do not introduce brittle single-platform/API dependency without a fallback.
- Do not imitate Naval or turn the answer into general lifestyle philosophy.

## Output

Return one review using `docs/review-protocol.md`. Name the first leverageable bottleneck, the asset to create, the baseline metric, and the review/rollback condition. Prefer one asset-building step over a full product roadmap.

Pair with `business-filter` if repeatability or unit economics remain doubtful. Productization follows proven SOPs; it is not the starting point.
