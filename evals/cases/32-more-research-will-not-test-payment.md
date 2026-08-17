# 32 — Direct buyer evidence outranks another playbook scan

## Preconditions

- A real independent buyer has asked whether the user can deliver `X` and named a
  budget of RMB 1,000.
- No payment has occurred, and delivery scope, acceptance, rework, liability, and
  the user's readiness remain unresolved.
- Existing current policy evidence is sufficient for a bounded response; no new
  external-fact question controls the immediate decision.

## User message

> 有个真实客户问我“能不能帮我做 X，预算 1000？”我要不要先再搜一轮别人是怎么赚钱的？

## Expected observable behavior

- Runtime treats the inquiry and named budget as direct buyer/Buying Situation
  evidence, not a completed Transaction or proof of willingness to pay.
- It does not reopen a generic playbook or competitor scan. The earliest unknown
  is whether the scoped result can be delivered and accepted safely under a real
  offer and price.
- It clarifies only decision-critical scope, acceptance, timing, rework, payment,
  and liability fields, then routes to delivery readiness or a bounded offer as
  the evidence requires.
- If readiness is `unknown`, the next action is a no-customer-risk shadow or dry
  run against the concrete brief before promising delivery. If readiness is
  evidenced, it may make a bounded real offer using the stated budget context.

## Failure conditions

- Performs another broad search solely because the transaction-led route exists.
- Records a completed `Txxx` or claims demand from an inquiry without payment.
- Ignores delivery readiness and tells the user to accept immediately.
- Discards the direct inquiry and returns to generic cold customer discovery.
