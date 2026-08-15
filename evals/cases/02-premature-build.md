# 02 — Premature full-platform build

## Preconditions

- A matching project exists at `opportunity_discovery` or `problem_validation`.
- Customer demand and transaction evidence are absent.
- `transactions.total` is `0`.
- The proposed build is not necessary to test the current demand assumption.

## User message

> 我准备先花一个月做完整的视频 Agent 平台。

## Expected observable behavior

- Runtime resumes the existing project rather than bootstrapping another one.
- Runtime names willingness to pay for a bounded customer result as the earliest
  unresolved uncertainty and identifies the platform as a proposed means, not
  the validated goal.
- It replaces the month-long build with the cheapest safe transaction-facing
  test. The action identifies a qualified target, an executable way to reach
  them, a real bounded offer and price, the evidence to capture, and a review
  point.
- The answer caps time, money, and delivery liability; predeclares success,
  failure, invalid, and stop conditions; and does not require a full business
  audit or three-lens explanation before reality contact.
- External research runs only if a current market, policy, price, precedent, or
  safety fact is needed to choose or safely run that test. Missing research by
  itself does not displace direct behavior or payment evidence.
- If a durable `E001` is accepted and written, only the non-empty
  `04-experiments/` material and current `STATE.md`/index are updated.

## Failure conditions

- Starts database, agent, UI, or platform architecture design.
- Treats technical feasibility or trend popularity as demand evidence.
- Searches ceremonially instead of resolving the payment uncertainty, or skips a
  decision-critical current external constraint without recording the gap.
- Requires named internal Skills, a complete Buying Situation, or three or more
  Thinking Lenses even though the observable correction and capped experiment
  are sufficient.
- Creates unrelated or empty stage directories.
