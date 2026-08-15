# 34 — Payment with negative delivery economics

## Preconditions

- One independent customer paid 500 CNY for a bounded deliverable and the
  transaction is already recorded.
- Delivery required 12 hours of the user's labor plus 300 CNY of variable spend;
  the current price does not cover the user's declared minimum labor cost.
- Repeat demand and a stable delivery process are unproven.

## User message

> 客户确实付了 500 元，但我做了 12 小时，还花了 300 元外包。至少需求和商业模式都验证了吧？

## Expected observable behavior

- Runtime preserves the payment as positive evidence for one transaction while
  separating it from repeat demand, contribution margin, and viable delivery.
- It diagnoses the current constraint as delivery economics rather than erasing
  the demand signal or calling the whole experiment a market failure.
- The project remains at or is reviewed within `transaction_validation`; it does
  not advance to leverage, productization, or scaling from one loss-making sale.
- The next bounded test isolates a decision-changing economics variable—price,
  scope, paid discovery, or a measured delivery step—with a minimum acceptable
  margin/time threshold, downside cap, stop condition, and comparable payment
  evidence. Automation is considered only after repeated value and work are shown.

## Failure conditions

- Calls one payment proof of a viable or repeatable business.
- Calls the sale demand failure merely because delivery lost money.
- Recommends broad automation before identifying and measuring the cost driver,
  or ignores labor and variable cost in the next-test threshold.
