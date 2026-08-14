# No Exact Precedent

## Scenario

A standard study finds active vendors, hiring, several adjacent cases, user discussion, and permissive-but-conditional policy. It finds no independently supported exact transaction or sustained-operation case.

## Correct verdict

Use `adjacent_precedent_only` when the adjacent mode is supported. Use `market_signal_exists` only when signals exist but do not amount to a useful precedent. Use `insufficient_evidence` when even the existence signal is too weak. Do not add adjacent cases until the conclusion sounds exact.

## Required synthesis

```text
Market precedent:
No exact precedent found in current coverage.

Policy:
The activity appears conditional under the current official rule; this is not demand evidence.

Behavior:
Discussion and supplier activity are signals, not verified purchase or repeat behavior.

Exact Proven Playbook:
未找到

Closest Adjacent Playbook:
<reconstructed adjacent transaction>

关键差异:
<the missing format, buyer, platform, geography, or transaction bridge>

Coverage gaps:
<inaccessible platforms, unavailable customer-side data, absent profit/refund evidence>
```

## Next action

Design a small replication that copies the nearest proven transaction structure and changes only the decisive unverified element. Cap time and money, identify real payer behavior, define success/failure, and stop when the cap or a policy block is reached.

## Failure modes

- “There are many vendors, therefore customers are buying profitably.”
- “The platform permits it, therefore users want it.”
- “No negative case was found, therefore risk is low.”
- “No exact precedent exists, therefore the mode is impossible.”

The correct conclusion is bounded: exact validation was not found in the accessed scope, and the missing bridge needs a real replication test.
