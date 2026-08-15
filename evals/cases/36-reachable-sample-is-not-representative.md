# 36 — Reachable sample is not automatically decision-relevant

## Preconditions

- A personal-content monetization project is at `opportunity_discovery`.
- The user has no validated content direction, audience, payer, or transaction.
- Previous outreach was mostly to nearby programmer peers, whom the user reports
  are highly competitive and generally unwilling to pay.
- No fresh evidence yet shows which content market has durable audience pull or
  monetization potential.

## User message

> 我是程序员，想靠持续分享真实 AI 项目、失败和成本做自媒体，最后能赚钱。但我以前主动联系的基本都是身边程序员同行，比较卷，付费意愿也不高。我现在不知道做什么内容，是不是先在微信里找 5～8 个技术朋友聊聊，再用他们共同提到的问题定主要内容方向？

## Expected observable behavior

- Runtime separates reachability from sample selection and decision relevance.
  It explains that nearby technical peers can provide useful evidence about
  technical workflows, recurring AI problems, current workarounds, and time or
  effort costs without treating them as a representative content market.
- It limits the inference from that sample: shared problems among a few peers do
  not by themselves establish durable content demand, the best audience,
  willingness to pay, or a viable monetization model.
- Runtime may still use a small peer sample as a cheap exploratory
  `problem_validation` action, but names the narrow claim being tested and keeps
  content-market and payment claims `unknown`. It does not reject small samples
  merely because they cannot represent an entire market.
- The selected next evidence matches the immediate decision claim. If the next
  claim is content pull or monetization, Runtime uses a more decision-relevant
  audience, behavior, platform, buyer, or payer source—or explicitly states the
  proxy gap before using peers as an indirect source.

## Failure conditions

- Chooses technical peers as the main commercial sample only because they are
  easy to reach, without naming selection bias or the evidence-scope limit.
- Promotes a problem mentioned by several friends directly into the main content
  direction, audience, market demand, or monetization thesis.
- Treats the peer sample as useless because it is not market-representative,
  rather than using it for the narrower problem-discovery claim it can answer.
- Produces a detailed interview packet whose success threshold still lets a
  reachable but decision-irrelevant sample answer the content-business question.
