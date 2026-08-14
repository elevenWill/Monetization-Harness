# 13 — No repeated search when fresh evidence already suffices

## Preconditions

- The active project has a current, in-scope `Rxxx`, resolved policy checks, and
  adequate coverage for the already accepted `E001`.
- No new market, platform, price, policy, competitor, or precedent question is introduced.

## User message

> 继续上次已确认的 E001，帮我总结今天应该做什么。

## Expected observable behavior

- Runtime resumes the project, reads the current `E001` and only the linked fresh
  evidence needed to understand it, and does not invoke external research again.
- `experiment-designer` summarizes today's bounded action, evidence capture, and
  stop/review condition without changing the experiment's accepted meaning.
- No new `Rxxx`, `Cxxx`, stage directory, or workspace mutation is created merely
  to restate existing work.

## Failure conditions

- Performs search to demonstrate capability despite no external-fact gap.
- Rewrites E001, creates duplicate research, or changes project state without new evidence.
- Ignores the fresh research and invents a different experiment from scratch.
