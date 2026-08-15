# 33 — Building will not test payment

## Preconditions

- Repeated direct observations support a painful workflow and current external
  constraints are already fresh enough for a test.
- A target buyer and manually deliverable result are defined, but no one has seen
  a real offer or paid.
- The user can deliver the first three outcomes manually without a database,
  agent architecture, or platform.

## User message

> 我还是想先把数据库、Agent 编排和管理后台搭起来，做完整一点再去报价。

## Expected observable behavior

- Runtime identifies willingness to pay—not technical architecture—as the
  earliest unresolved uncertainty and explains why the proposed build does not
  observe it.
- It does not reopen research or run a full business audit when current evidence
  already supports a safe manual test.
- It replaces development with a concrete, capped human-execution experiment:
  qualified targets and sourcing, a manual bounded result, real price/payment
  terms, planned and actual exposure fields, delivery cap, success/failure/invalid
  conditions, stop, and review.
- It states the evidence threshold that would make the smallest technical
  investment decision-relevant; until then, product architecture remains deferred.

## Failure conditions

- Designs schemas, agents, APIs, UI, or a month-long prototype before the real
  offer test.
- Merely says “validate first” without an executable packet for tomorrow.
- Treats technical feasibility, a working demo, or observed pain as payment
  evidence.
