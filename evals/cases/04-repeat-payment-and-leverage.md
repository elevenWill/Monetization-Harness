# 04 — Repeat payment and leverage

## Preconditions

- Multiple independent or repeat payments are linked in the existing project.
- The delivered customer result and major delivery steps are materially similar.
- Delivery time, bottleneck, or margin still needs measurement.

## User message

> 已经有 8 个客户连续购买，而且每次交付流程大体一样。现在该自动化吗？

## Expected observable behavior

- Runtime verifies that the repetition claim has transaction/delivery evidence
  before treating it as FACT.
- Stage may advance to `leverage_discovery`; `leverage-designer` maps and measures
  the repeated process before selecting one SOP, reusable asset, or assisted step.
- `business-filter` is added only if delivery economics or recurrence still gates
  the decision.
- `06-leverage/` appears only when a real leverage artifact is written and is
  non-empty; historical non-contiguous directories remain valid.

## Failure conditions

- Automates the full workflow without a measured process baseline.
- Treats compliments, users, or one-off delivery as repeated paid value.
- Requires every earlier stage directory to exist before leverage work can begin.
