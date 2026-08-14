# Digital-Human Short-Video Commerce

## User input

> 我想做数字人短视频带货。方案技术上可行，我想知道市场是否已经验证，用户是否接受，平台是否允许，有没有可以直接参考的成功方案。

## Correct behavior

1. Let the orchestrator match or bootstrap the project; do not ask the user to initialize it.
2. Recognize that precedent, acceptance, price, and policy are external facts.
3. Infer a provisional primary market and target platforms from context, or ask only if the choice would materially change the research.
4. Choose `standard` depth because the user asks for viability and cases.
5. Search current official policy for the exact platform, region, and short-video content type, including AI disclosure, synthetic likeness, misleading expertise, commerce claims, and pre-recorded-content restrictions.
6. Define the exact mode as digital-human, 10-15 second, recorded short-video product commerce—not livestreaming, human-presented short video, education, or brand advertising.
7. Search exact transaction or sustained-operation cases.
8. Search adjacent cases separately: digital-human livestream commerce, human short-video commerce, digital-human informational content, other platforms, and other markets.
9. Search failures, low conversion, distrust, refunds, complaints, enforcement, throttling, shutdown, and unsuccessful replacement of human presenters.
10. Inspect behavioral acceptance signals such as purchase, retention, refund, complaint, and disclosure response across at least two independent channel types.
11. Search current providers, substitutes, service quotes, software prices, marketplace offers, and evidence of actual transactions.
12. If the claim includes an activity, launch, or rush deadline, route to [digital-human-deadline.md](digital-human-deadline.md) and search the event, buyer-originated urgency, delay consequence, purchase window, trust, liability, and recurrence separately.
13. Create `R001` only after actual research; convert only strong narrowly worded evidence to FACT.
14. Create `C001` only if a reconstructed exact or useful adjacent case has durable reuse value.
15. Produce the Closest Proven Playbook and classify its components as Copyable, Context-dependent, Non-copyable, or Unknown.
16. Give `experiment-designer` a minimal replication basis; do not recommend a full digital-human platform before the migration assumption has transaction evidence.

## Required scope controls

```yaml
proposed_scope:
  format: recorded short video
  duration: 10-15 seconds
  presenter: digital human
  result: product purchase
  market: inferred or confirmed target geography
  platform: inferred or confirmed target platform
not_exact:
  - digital-human livestream commerce
  - human-presented short-video commerce
  - digital-human education or brand content
  - a case from another platform or regulatory market
```

If research finds only livestream cases:

```text
Verdict: adjacent_precedent_only

Exact Proven Playbook:
未找到

Closest Adjacent Playbook:
数字人直播间持续讲解商品并导向平台内成交。

关键差异:
直播的停留、实时互动、平台流量入口和成交链路不能证明 10-15 秒预录短视频能产生同样行为。
```

## Example evidence treatment

- Official platform rule opened and checked today: may support a time-qualified policy FACT with all required policy fields.
- Vendor says a client increased GMV 300%: `authority: vendor_marketing`, `verification: single_source_reported`; FACT only that the vendor published the claim.
- A customer confirms dates, format, platform, orders, and continued operation, with an independent source: candidate for `exact_corroborated` or `exact_verified` depending on direct evidence.
- Comments saying avatars feel untrustworthy: negative risk signal; do not generalize to the entire market without behavior or broader evidence.

## Closest Proven Playbook output

Name the actor, payer, bought result, acquisition, delivery, trust mechanism, platform constraints, price/transaction evidence, repeatability, copyable mechanics, unique advantages, and user gaps. Link each decisive claim to `R001-Sxx` and any durable `Cxxx`.

## Replication experiment basis

```text
Reference Case: a real Cxxx created only when the reconstructed exact or adjacent case has durable reuse value
Mechanism copied: one product, a small batch of 10-15 second demonstrations, existing platform checkout
Unique advantages not copied: established audience, official placement, exclusive supply chain
Migration assumption: a disclosed digital presenter can generate qualified purchase behavior for the target category
Maximum exposure: a predeclared small money and time cap
Success: predeclared transaction or high-intent behavior threshold
Failure: no qualified behavior, unacceptable distrust/refund signal, or policy constraint
Stop: cap reached or policy blocks the exact content form
```

If no durable `Cxxx` exists, do not invent a Case ID or label the proposal a formal Replication Experiment. Keep it as an adjacency-transfer test basis linked to `R001` until a reusable Case is actually reconstructed.

## Incorrect behavior

- “数字人现在很火，所以市场可行。”
- “淘宝数字人直播不错，因此抖音数字人短视频带货已验证。”
- “某服务商称客户 GMV 提升，所以该模式必然赚钱。”
- Building a full generation, database, publishing, or analytics system before a bounded replication test.
