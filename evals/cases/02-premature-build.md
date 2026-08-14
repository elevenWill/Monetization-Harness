# 02 — Premature full-platform build

## Preconditions

- A matching project exists at `opportunity_discovery` or `problem_validation`.
- Customer demand and transaction evidence are absent.
- `transactions.total` is `0`.
- Relevant external market evidence is missing or stale.

## User message

> 我准备先花一个月做完整的视频 Agent 平台。

## Expected observable behavior

- Runtime resumes the existing project rather than bootstrapping another one.
- Because the proposed month-long build depends on an unverified current market,
  Runtime invokes `market-reality-researcher` first for appropriately bounded
  external evidence; it records any access gaps and does not mistake the
  researcher for one of the Thinking Lenses.
- `business-filter` runs first, classifies the Buying Situation or
  `no_clear_why_now`, and rejects product completeness as a bought result.
  Because this case independently contains a month-long commitment, a framing
  error, and a business-model unknown, Runtime explicitly justifies an
  exceptional three-lens route: `assumption-challenger` corrects the platform
  premise and `experiment-designer` replaces the build with the cheapest safe
  transaction-facing test.
- The answer caps time and money, defines success, failure, and stop conditions,
  and seeks behavioral or payment evidence.
- If a durable `E001` is accepted and written, only the non-empty
  `04-experiments/` material and current `STATE.md`/index are updated.

## Failure conditions

- Starts database, agent, UI, or platform architecture design.
- Treats technical feasibility or trend popularity as demand evidence.
- Runs only internal Persona reasoning despite missing/stale market evidence, or
  runs all five Thinking Skills after research.
- Routes to all five Thinking Skills.
- Creates unrelated or empty stage directories.
