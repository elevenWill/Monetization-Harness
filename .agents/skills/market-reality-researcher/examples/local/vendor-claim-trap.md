# Vendor Claim Trap

## Scenario

A digital-human software provider publishes: “Customer B increased GMV by 300% after using our avatars.” No customer-side account, platform record, methodological detail, or independent source is available.

## Source record

```yaml
id: R001-S04
source_type: customer_case_page
authority: vendor_marketing
verification: single_source_reported
freshness: current
scope_match: exact
direction: supports
claim: The provider states that Customer B's GMV increased 300%.
notes: No independent corroboration; baseline, period, spend, profit, attribution, and customer confirmation are missing.
```

`scope_match: exact` means the described format matches; it does not make the outcome verified.

## Case treatment

```text
Verification status: vendor_claim_only
Defensible FACT: Provider A published a claim that Customer B's GMV rose 300%.
Not a FACT: Customer B's GMV rose 300% because of the digital human.
```

Search for:

- customer-side statement and identifiable actor;
- independent reporting or observable platform operation;
- baseline and measurement period;
- orders, conversion, refunds, costs, discounts, ad spend, and profit;
- attribution method and other simultaneous changes;
- repetition after the reported period.

If no corroboration appears, retain the source as a lead, include it under uncertainty, and do not use it to declare `exact_precedent_verified` or market profitability.

## Failure mode

Incorrect:

> A customer achieved 300% growth, proving the solution works.

Correct:

> A vendor markets a 300% GMV claim; current coverage does not independently verify the customer's outcome, profitability, or attribution.
