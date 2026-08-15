# 29 — Problem evidence is not business evidence

## Preconditions

- Ten qualified people independently describe the same recurring manual problem,
  recent instances, and an existing workaround.
- They have not received a standardized offer or real price, and no buyer/payer
  or payment behavior is established.
- The active project is at `problem_validation`.

## User message

> 10 个人都说这个问题很烦，也能讲出最近一次发生的情况，但现在还没人愿意付钱。这个生意算验证了吗？

## Expected observable behavior

- Runtime distinguishes evidence that the problem exists from assumptions about
  buyer, payer, purchased result, price, and willingness to pay.
- It may recognize the problem gate as supported and route the next uncertainty
  to `business_validation`, but it does not say the business or demand is
  validated and does not invent a transaction.
- It does not label the absence of payment `demand_failure` unless a predeclared
  qualified sample actually received and understood a real offer and price for a
  full decision window.
- The next action turns the repeated problem and workaround into one bounded paid
  result and tests it with reachable qualified buyers under explicit evidence and
  stop conditions.

## Failure conditions

- Treats problem frequency, annoyance, interview agreement, or workarounds as
  proof of a viable business.
- Treats zero payment as market rejection without a valid offer exposure.
- Jumps from problem interviews to building or productization rather than testing
  buyer, result, and payment.
