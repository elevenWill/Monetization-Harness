# 02 — Premature full-platform build

## Preconditions

- A matching project exists at `opportunity_discovery` or `problem_validation`.
- Customer demand and transaction evidence are absent.
- `transactions.total` is `0`.

## User message

> 我准备先花一个月做完整的视频 Agent 平台。

## Expected observable behavior

- Runtime resumes the existing project rather than bootstrapping another one.
- `assumption-challenger` identifies “a complete platform is needed” as an
  ASSUMPTION; `experiment-designer` replaces the build with the cheapest safe
  transaction-facing test.
- The answer caps time and money, defines success, failure, and stop conditions,
  and seeks behavioral or payment evidence.
- If a durable `E001` is accepted and written, only the non-empty
  `04-experiments/` material and current `STATE.md`/index are updated.

## Failure conditions

- Starts database, agent, UI, or platform architecture design.
- Treats technical feasibility or trend popularity as demand evidence.
- Routes to all five Thinking Skills.
- Creates unrelated or empty stage directories.
