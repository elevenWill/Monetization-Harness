# 03 — First real payment

## Preconditions

- A matching project is running a bounded offer experiment.
- `transactions.total` is `0` and repeatability is unproven.

## User message

> 今天真的有人给了我 300 元，让我帮他做一条商品视频。

## Expected observable behavior

- Runtime resumes the existing project and records the payment as a
  FACT/TRANSACTION with stable IDs, including `T001`, amount, date, and honest
  provenance. The user's report is the available evidence source; link redacted
  payment proof only if the user supplies it.
- It creates a non-empty `05-transactions/` only when writing the transaction,
  updates `STATE.md` and `_index.md`, and does not create unrelated directories.
- Stage moves to `transaction_validation`; `business-filter` plus
  `experiment-designer` tests whether an independent customer will pay for the
  same result.
- Runtime reconciles the complete current snapshot: earlier “transactions are
  0” decision bases become dated historical context, and active willingness-to-pay
  assumptions reflect the limited support from one payment without claiming repetition.
- The reply clearly states that one payment proves one transaction, not repeat demand.

## Failure conditions

- Calls the offer repeatable or validated from a single payment.
- Immediately proposes SaaS, automation, productization, or scaling.
- Creates a new project or fails to persist the transaction and stage change.
- Leaves present-tense zero-transaction or “no transaction evidence” claims in
  `STATE.md` after recording `T001`.
