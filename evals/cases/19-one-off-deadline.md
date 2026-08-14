# 19 — Valuable one-off rush service

## Preconditions

- A company has one externally fixed acquisition-closing date.
- Missing the date would forfeit a material but non-ruinous deal benefit.
- The required document organization is a one-time task and no repeat trigger or
  repeat customer evidence exists.

## User message

> 客户并购交割只剩三天，需要一次性整理完资料，愿意付很高的加急费。这个是不是能做成长期产品？

## Expected observable behavior

- Runtime recognizes a real hard_external Buying Situation and classifies it as
  one_off_rush_service, preserving the evidence that a high-priced service may
  be legitimate.
- business-filter separates the one payment opportunity from recurrence,
  identifying buyer/payer, bought result, Cost of Delay, purchase window,
  acquisition path, trust requirement, delivery cost, margin, and liability.
- The answer says a one-off deadline can support a premium service but cannot
  establish a sustainable product, repeat purchase, or predictable demand.
- Any bounded experiment or accepted delivery caps scope and liability and uses
  human review; a separate recurring trigger must be observed before leverage or
  productization is inferred.
- Workspace state records one-time evidence without promoting repeatability or
  creating unused productization material.

## Failure conditions

- Equates one urgent high-priced job with durable recurring demand.
- Rejects the service solely because it is one-off.
- Recommends SaaS or scale before identifying an independently recurring Buying
  Situation and repeated payment.
- Omits the short purchase window, trust burden, or failure liability.
