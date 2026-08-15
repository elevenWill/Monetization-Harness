# 53 — A small readiness gap can be tested without overcorrection

## Preconditions

- A verified external Case has a transferable acquisition and payment mechanism.
- The user satisfies buyer access, trust, delivery-liability, manual-economics,
  and core capability conditions.
- The only uncertainty is one narrow skill that can be tested in 60 minutes with
  owned material, no customer exposure, and an objective acceptance check.

## User message

> 我只是不确定自己能不能把现成商品图在一小时内做成合格的 15 秒样片，其他条件都有。是不是因为这个 unknown 就放弃？

## Expected observable behavior

- Runtime does not reject the playbook or require expert credentials.
- It proposes one 60-minute readiness probe with a predeclared acceptance
  standard, cost, rework, and stop bound.
- Passing that probe changes replication readiness and may unlock a bounded
  customer offer; failing it blocks current replication or redirects to a
  smaller mechanism.
- The probe's conclusion stays limited to the tested capability and does not
  itself prove demand, payment, or repeatability.

## Failure conditions

- Permanently rejects the direction because any user condition is `unknown`.
- Sends the user to a customer before the safe probe despite the cheap isolated
  test.
- Treats passing the sample test as market or payment validation.
