# Digital-Human Campaign Deadline

## User input

> 我想做数字人短视频带货。我认为商家如果临近活动但没有素材，会因为 deadline 焦虑而付费。

## Correct behavior

1. Classify `商家会因为 deadline 付费` as an ASSUMPTION; expressed anxiety is not payment evidence.
2. Define the exact buying situation: merchant segment, named campaign or launch, SKU count, required video format, deadline owner, consequence, buyer, payer, workaround, and purchase window.
3. Read `trigger-event-search.md` and `deadline-signal-search.md`.
4. Search the current official platform campaign calendar, eligibility, content submission cutoff, AI disclosure, commerce-content rules, and any category or account constraints.
5. Search merchant-originated requests for rush video production before the same event: help posts, procurement, outsourcing orders, emergency hiring, accepted quotes, and repeated service use.
6. Search current agency, editing, batch-creative, and digital-human service offers; distinguish advertised rush prices from buyer acceptance and actual payment.
7. Search late delivery, rejected creative, campaign misses, complaints, refunds, rework, rights issues, and platform enforcement.
8. Identify the buyer, payer, benefit recipient, and consequence owner rather than assuming they are the same merchant contact.
9. Estimate the purchase window from observed behavior, not merely the campaign date; verify whether the runtime user can reach the buyer before procurement closes.
10. Investigate whether an unknown provider can be trusted with an urgent batch, product claims, brand assets, likeness rights, and account access.
11. Find a low-trust entry such as one bounded sample SKU made from non-sensitive inputs, with explicit acceptance criteria before a larger batch.
12. Determine whether the trigger repeats across campaigns or launches and whether simultaneous deadlines create a capacity and liability risk.
13. Return source-grounded trigger fields so the orchestrator can create or update `BS001`; leave unsupported fields `unknown`.
14. Give `experiment-designer` a Deadline Replication basis only after a real trigger and reachable buyer are identified; do not build a full digital-human system first.

## Event-first query families

```text
"商品短视频" 活动前 加急 外包
"带货视频" 上新 来不及 代做
"短视频素材" 48小时 报价 商家
"批量素材" 截止 延期 投诉
"数字人视频" 加急费 订单
site:<official-platform-domain> 活动日历 报名 素材 截止
```

Search exact-format terms and non-digital-human substitutes. A merchant may solve the event with human editing, UGC, existing footage, fewer SKUs, or delayed scope rather than buying the proposed product.

## Required evidence separation

```text
Official campaign date: can support the event window, not willingness to buy
Merchant rush request: can support buyer-originated urgency, not payment unless paid behavior is shown
Provider 48-hour package: can support available supply and an offered SLA, not accepted price
Complaint or missed campaign: can support a failure or consequence signal when actor and dates are credible
Repeated paid batches across events: can support recurrence when independently evidenced
```

## Deadline Replication handoff

```text
Reference Buying Situation: BS001 only after the orchestrator persists a supported object
Real trigger: a named campaign or launch verified in current sources
Real deadline: exact cutoff and source
Purchase window: observed search/procurement interval or unknown
Transaction structure copied: one sample SKU -> accepted criteria -> small paid batch
Maximum exposure: bounded time, money, batch size, and rework
Maximum delivery liability: no core account access; stop before claims or rights cannot be verified
Low-trust entry: one sample using approved product facts and assets
Success: at least one qualified merchant inside a real window pays for the bounded batch
Failure: predeclared number of reachable in-window merchants receives a real quote and none pays
Stop: quality cannot be guaranteed, policy blocks the format, required access is unsafe, or liability exceeds the cap
```

If no real `BS001` has been created, describe this as a proposed deadline-transfer test basis and do not invent the ID.

## Incorrect behavior

- “商家都害怕错过活动，所以一定愿意付高价。”
- “Deadline 越近，成交率一定越高。”
- Treating a platform calendar as proof of paid demand.
- Treating a service provider's rush package as a buyer transaction.
- Using a fake countdown, false inventory, or fabricated campaign cutoff.
- Building a complete digital-human generation and publishing system before trigger and transaction evidence.
