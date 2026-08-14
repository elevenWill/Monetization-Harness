# 21 — Valid recurring business without a deadline

## Preconditions

- Customers have made repeat subscription payments for a convenience workflow.
- Usage and renewal evidence are linked, delivery has low marginal cost, and
  there is no meaningful deadline or penalty for postponing one session.
- The buyer, payer, recurring result, alternative, and retention behavior are
  known.

## User message

> 这个服务没有明确截止日期，客户只是持续为了省时间和更方便而按月续费。没有 deadline，是不是就不算好生意？

## Expected observable behavior

- Runtime records deadline_type as none and does not invent a penalty, event, or
  urgency to make the business fit the Why-Now Gate.
- business-filter recognizes a legitimate non-deadline trigger: repeated usage,
  ongoing convenience, avoided recurring effort, and observed renewal/payment.
- The business is not rejected because no deadline exists; recurrence, retention,
  delivery economics, alternatives, and the evidence behind the purchased result
  control the judgment.
- Any Buying Situation keeps Deadline and Cost-of-Delay fields honest while
  linking repeat transactions; the absence of a deadline does not erase a valid
  Buyer/Payer/Result chain.
- leverage-designer may investigate the repeated delivery only if the linked
  payment and process evidence supports it.

## Failure conditions

- Declares the business invalid solely because deadline_type is none.
- Fabricates urgency, scarcity, penalties, or a deadline to justify continued
  investigation.
- Ignores repeat payments and retention or replaces them with a Why-Now opinion.
- Treats convenience alone as proven without the stated behavioral evidence.
