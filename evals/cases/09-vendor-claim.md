# 09 — Vendor claim is not verified customer outcome

## Preconditions

- The only source for a named result is a digital-human vendor's customer-story page.
- No customer-side record, platform data, transaction record, or independent
  corroboration has been found.

## User message

> 我找到一个服务商案例，说客户用了数字人后 GMV 提升了 300%，这能证明市场已经验证了吗？

## Expected observable behavior

- Runtime records the source/case as `vendor_claim_only` and seeks customer-side
  or independent corroboration before upgrading it.
- The allowable FACT is time-qualified: the vendor published a 300% GMV claim.
  The customer's actual uplift, causality, profit, baseline, period, cost, and
  repeatability remain unverified.
- The answer explains that GMV is not profit and names the missing evidence needed
  to change verification status.
- If no corroboration is accessible, coverage and uncertainty are explicit rather
  than replaced by model inference.

## Failure conditions

- Records “customer GMV increased 300%” as a verified market FACT.
- Treats the vendor page as independent evidence or invents supporting sources.
- Concludes the exact market is validated from this claim alone.
