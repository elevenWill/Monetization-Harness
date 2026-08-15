# 50 — Leverage preserves the paid judgment kernel

## Preconditions

- A project is at `leverage_discovery` with four auditable paid deliveries
  of the same compliance-report outcome across three independent customers.
- Customers accepted the reports, but the founder spent six hours per delivery:
  four hours gathering and formatting evidence, one hour interpreting ambiguous
  exceptions, and one hour on customer review.
- The interpretation step changed the accepted conclusion in two deliveries.
- The user asks whether to build a self-serve AI SaaS that automates the entire
  report.

## User message

> 这套报告已经卖了四次。我每次都要花六小时，想直接做成全自动 AI SaaS，
> 从资料收集到最终结论都不给人工介入。这样最有杠杆，对吧？

## Expected observable behavior

- Runtime confirms `leverage_discovery` because paid value and materially similar
  delivery have repeated; it does not reopen generic opportunity discovery or
  remain in `transaction_validation`.
- It identifies the accepted compliance report as the value kernel and separates
  stable evidence gathering/formatting from exception interpretation and review.
- It treats the two conclusion-changing exceptions as evidence that
  interpretation is still accountable judgment, not a mechanism ready for
  unsupervised automation.
- It rejects “full AI SaaS” as the first mode and selects a lower-commitment
  assisted asset for the stable mechanism, such as an evidence-ingestion and
  draft-formatting tool that records inputs, exceptions, founder decisions, and
  accepted outcomes.
- It names the compounding residue: a consent-safe labeled exception library,
  verified formatting rules, or tests that improve future assisted deliveries.
- It defines review evidence in leverage terms: marginal operator time per
  accepted report, quality hold versus the manual reference, reuse ratio, and a
  threshold that returns output to human handling. The first step remains one
  bounded asset, not a complete product roadmap.
- Existing SLA, liability, market-case, or unit-economic constraints are consumed
  if present; the lens does not repeat those reviews unless this asset contradicts
  them.

## Failure conditions

- Equates AI or code with leverage and recommends end-to-end automation because
  the service has repeated.
- Treats all six delivery hours as one repeatable unit and fails to distinguish
  customer value, mechanical work, and conclusion-changing judgment.
- Produces only generic advice to “automate one bottleneck, measure a baseline,
  and roll back if needed” without selecting a replication mode or naming the
  compounding residue and accountability loop.
- Re-runs buyer, price, outreach, broad market research, or a generic experiment
  design as the primary answer despite auditable repeated paid delivery.
- Calls a static per-customer prompt or report template a compounding asset when
  it neither increases reuse nor captures reusable learning.
- Removes the founder from exception decisions before acceptance-linked quality
  and a failure-to-system feedback path exist.
