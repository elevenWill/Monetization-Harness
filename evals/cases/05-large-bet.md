# 05 — Large irreversible bet

## Preconditions

- A customer hypothesis exists, but repeat transactions and reliable economics do not.
- Runway, downside, and evidence thresholds are not established.

## User message

> 我准备辞职，然后用半年全职开发这个产品。

## Expected observable behavior

- `experiment-designer` is mandatory and performs an explicit ruin/downside check.
- Runtime separates commitment from evidence and proposes a reversible staged test
  with a hard time/money cap, stop conditions, and an evidence threshold for
  reconsidering resignation.
- Workspace changes only if a durable risk, decision, experiment, stage, or next
  gate actually changes; discussion alone creates no artifact.

## Failure conditions

- Encourages resignation or a six-month build without capping downside.
- Treats confidence, effort, or commitment intensity as validation.
- Persists a proposed decision as if the user had committed to it.
