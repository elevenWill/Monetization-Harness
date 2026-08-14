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

1. Separate the proven customer outcome from the current delivery method.
2. Map each delivery step: input, operator judgment, time/cost, variance, failure modes, deadline, acceptance standard, and customer-visible value.
3. Reconstruct external cases skeptically: separate demonstrated leverage from
   hidden human operations, manual review, sales work, content work, subsidy, and
   undisclosed cost. Identify dependencies on platform distribution, brand trust,
   proprietary supply, privileged partnerships, capital, or existing audience.
4. Identify specific knowledge: the judgment that differentiates the result and should be captured or protected rather than blindly automated.
5. Classify steps as `keep_human`, `standardize`, `template`, `delegate`, `ai_assist`, `automate_with_code`, or `publish_as_media`.
6. Sequence leverage: manual service → documented process → SOP/template → assisted execution → tested automation → bounded product.
7. Estimate the effect on marginal cost, quality, cycle time, learning, dependency, and customer outcome.
8. For deadline-shaped work, test whether triggers are predictable or synchronized; whether the service becomes constant firefighting or 24-hour response; whether customers can pre-book; whether tiered SLA and rush pricing are feasible; whether inputs and acceptance can be standardized; which steps need human review; and what delay, refund, or consequential-loss exposure exists.
9. Automate one bottleneck at a time and compare against a pre-automation baseline. Check whether automation amplifies late or incorrect delivery and keep a rollback path.

## Guardrails

- Do not automate unresolved customer discovery or sales.
- Do not optimize volume before quality and economics are visible.
- Do not erase high-value judgment merely because it is hard to encode.
- Do not introduce brittle single-platform/API dependency without a fallback.
- Do not infer code leverage merely because an external case uses AI. Treat
  undisclosed labor and costs as unknown, not zero.
- Do not copy a case's leverage system until this project has independently
  reproduced the customer value and the required resources are transferable.
- Do not infer scalable demand from high rush prices. Synchronized deadlines can create a capacity and liability trap.
- Do not imitate Naval or turn the answer into general lifestyle philosophy.

## Output

Return one review using `docs/review-protocol.md`. Name the first leverageable bottleneck, the asset to create, the baseline metric, and the review/rollback condition. Prefer one asset-building step over a full product roadmap.

Pair with `business-filter` if repeatability or unit economics remain doubtful. Productization follows proven SOPs; it is not the starting point.
