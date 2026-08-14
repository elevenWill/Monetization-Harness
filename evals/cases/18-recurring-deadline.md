# 18 — Recurring operational deadline

## Preconditions

- Several customers complete the same reconciliation at every month-end.
- Past records show repeat purchases or costly internal overtime during the
  monthly close.
- The delivery steps are materially similar, but peak capacity, SLA, error rate,
  and margin are not yet understood.

## User message

> 这些客户每月关账都缺人，已经重复找我做同一种对账。既然 deadline 每个月都有，我是不是该马上自动化？

## Expected observable behavior

- Runtime identifies a rolling_operational Trigger and classifies the Buying
  Situation as recurring_deadline_opportunity based on linked repeat evidence,
  not on the calendar pattern alone.
- business-filter checks payer, recurring budget path, purchase window, current
  overtime/workaround, Cost of Delay, consequence owner, trust, reachability,
  margins, refunds, and delivery liability.
- Repeat purchases and repeated delivery raise recurrence and
  leverage-designer investigation priority, but do not by themselves authorize
  full automation.
- leverage-designer examines synchronized month-end demand, hidden manual review,
  capacity peaks, booking, tiered SLA, rush pricing, input constraints, acceptance
  standards, and whether automation would amplify errors.
- The next experiment or leverage artifact measures one repeated step under a
  real close window with an explicit quality/liability stop condition.

## Failure conditions

- Automates the full workflow merely because the deadline recurs.
- Treats all monthly deadlines as equivalent without verifying repeat payments,
  process similarity, capacity, or economics.
- Ignores simultaneous customer peaks, human review, error consequences, or SLA.
- Invents recurrence when only one deadline or one customer exists.
