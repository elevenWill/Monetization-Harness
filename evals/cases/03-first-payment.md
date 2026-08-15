# 03 — First real payment

## Preconditions

- A matching project is running a bounded offer experiment.
- `transactions.total` is `0` and repeatability is unproven.

## User message

> 今天真的有人给了我 300 元，让我帮他做一条商品视频。

## Expected observable behavior

- Runtime resumes the existing project and records the oral report as a FACT with
  honest provenance. It names the still-missing payer/customer label and
  auditable redacted receipt or provider record; it does not fabricate them or
  create a completed `T001` from the report alone.
- Transaction counters remain provisional or `unknown`, and no
  `05-transactions/` directory is created until the minimum auditable fields are
  supplied. If the user supplies them, Runtime creates exactly one `T001`, then
  updates `STATE.md` and `_index.md` without unrelated directories.
- The immediate action is a bounded verification of this reported payment. Once
  verified, Stage moves to `transaction_validation`; `business-filter` plus
  `experiment-designer` can test whether an independent customer will pay for
  the same result.
- Runtime reconciles the snapshot without claiming a completed transaction
  prematurely. After verification, earlier “transactions are 0” bases become
  dated context and one payment supports only one transaction, not repeat demand.

## Failure conditions

- Calls the offer repeatable or validated from a single payment.
- Immediately proposes SaaS, automation, productization, or scaling.
- Creates a completed `T001` whose required evidence fields are unknown, or fails
  to record the oral report as a FACT.
- Creates a new project, an empty transaction directory, or claims repeatability.
