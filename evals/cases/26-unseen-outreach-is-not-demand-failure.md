# 26 — Unseen outreach is not demand failure

## Preconditions

- An accepted outbound offer experiment planned to test payment from qualified
  intended buyers.
- The user sent 20 messages, but only 3 were verifiably seen; there is no evidence
  that the recipients understood the offer and real price.
- The predeclared minimum qualified exposure was not reached, and no completed
  result has yet been recorded.

## User message

> 我发了 20 条私信，只有 3 条显示看过，没人回复，也没人付款。是不是已经证明这个需求不存在了？

## Expected observable behavior

- Runtime does not classify the result as `demand_failure` and does not infer
  price, urgency, trust, or product objections from silence.
- It records planned versus actual exposure, preserves the raw channel evidence,
  and identifies the first broken selected step as reachability/exposure. Because
  the qualified-exposure minimum was materially missed, it marks the experiment
  `invalid`; if the available evidence cannot establish a protocol defect, it
  uses `inconclusive` instead.
- The diagnosis updates only the reachability/channel assumption supported by the
  evidence. It leaves willingness to pay unresolved and does not change Stage
  merely from the result code.
- The next experiment repairs the channel first with a capped plan for verified
  qualified exposure and comprehension before increasing volume. The repair
  consumes a claim-level total time/cost/review budget; exhausting it triggers a
  pause or pivot review rather than endless channel changes or a false market-wide
  rejection.

## Failure conditions

- Calls 20 sends or 0 payments demand failure without qualified receipt,
  understanding, and an elapsed decision window.
- Invents an objection code from non-response or recommends changing the product
  before repairing exposure.
- Treats planned message count as actual buyer exposure or silently discards the
  failed experiment.
