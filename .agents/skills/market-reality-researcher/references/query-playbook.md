# Query Playbook

Build queries around decision subquestions and scope discriminators. Replace `<idea>`, `<official-domain>`, platform, region, content format, buyer, and product category with project-specific terms. Search in the target market's language and add other languages only at `deep` depth or when the market requires them.

## Contents

- [Exact successful precedents](#exact-successful-precedents)
- [Failure and counterevidence](#failure-and-counterevidence)
- [Current platform policy](#current-platform-policy)
- [User behavior and acceptance](#user-behavior-and-acceptance)
- [Competitors, prices, and buying signals](#competitors-prices-and-buying-signals)
- [Purchase triggers and deadlines](#purchase-triggers-and-deadlines)
- [Adjacent case control](#adjacent-case-control)
- [Query log](#query-log)

## Exact successful precedents

```text
"<idea>" 成功案例
"<idea>" 真实案例
"<idea>" 营收
"<idea>" 订单
"<idea>" 成交
"<idea>" 转化率
"<idea>" 复购
"<idea>" 商家
"<idea>" 客户案例
"<idea>" case study
"<idea>" revenue
"<idea>" conversion
```

Add exact discriminators for platform, region, content type, payer, offer, and time. Search candidate actors separately once discovered. Ask whether the result is a transaction, sustained operation, or only attention.

## Failure and counterevidence

```text
"<idea>" 失败
"<idea>" 踩坑
"<idea>" 投诉
"<idea>" 退款
"<idea>" 封号
"<idea>" 限流
"<idea>" 不信任
"<idea>" 转化低
"<idea>" 停止
"<idea>" failed
"<idea>" complaints
"<idea>" banned
```

Also search violation, no viewers, poor results, losses, stopped operation, and failed replacement of an incumbent process. Search the names of candidate actors, vendors, and platforms with negative terms.

## Current platform policy

```text
site:<official-domain> "<idea>"
site:<official-domain> "AI generated content"
site:<official-domain> "virtual human"
site:<official-domain> "digital avatar"
site:<official-domain> disclosure
site:<official-domain> prohibited
site:<official-domain> "content policy"
```

Prioritize regulator sites, rule centers, merchant academies, official help centers, and announcements. Add region and content type. Open the actual rule and inspect publication/effective/update dates; never cite the search snippet as policy.

## User behavior and acceptance

Select relevant channels such as Xiaohongshu, Bilibili, Zhihu, V2EX, X, Reddit, YouTube comments, App Store, commerce reviews, merchant forums, and creator communities. Ask:

```text
why users buy / why users distrust
why merchants adopt / why merchants stop
whether users know content is AI-generated
whether AI disclosure changes trust or behavior
which product categories fit / do not fit
refund, complaint, retention, repeat purchase, abandonment
```

Do not infer population acceptance from a few vivid comments. Record access boundaries and sampling limitations.

## Competitors, prices, and buying signals

Search provider quotes, SaaS pricing, commerce service marketplaces, outsourcing requests, procurement notices, tenders, merchant help posts, creator service listings, hiring/job posts, and currently paid substitutes. Distinguish advertised price from verified transactions and recurring fees from setup fees.

Hiring volume can show that organizations allocate resources to a capability; it cannot alone prove a standalone new product will sell.

## Purchase triggers and deadlines

When the decision asks why a buyer acts now, read [trigger-event-search.md](trigger-event-search.md) and [deadline-signal-search.md](deadline-signal-search.md). Build event-first queries from task/product terms plus event, deadline, consequence, and buying-behavior terms. Seek buyer requests, procurement, outsourcing, accepted rush work, emergency hiring, repeated workarounds, penalties, missed events, and delivery disputes—not only provider marketing.

Search the real event owner and deadline source separately from willingness to pay. A platform calendar, tender date, filing deadline, launch, or recurring close can verify a time window; it cannot prove that anyone buys the proposed solution. A provider's rush surcharge can verify an offered price; it cannot prove acceptance. Add a non-urgent control query and record missing private orders, accepted quotes, closed groups, eligibility notices, and transaction records as coverage gaps.

## Adjacent case control

Generate explicit contrast queries for each likely mismatch:

```text
short video vs livestream
AI avatar vs human presenter
commerce vs education/brand content
target platform vs other platform
target geography vs foreign market
new account vs established audience
merchant transaction vs vendor demonstration
```

Record the mismatch before using adjacent evidence. More adjacent results never convert adjacency into an exact precedent.

## Query log

For every `Rxxx`, retain:

```text
query text
date run
channel/backend
scope intent
useful source IDs
result limitation or coverage gap
```
