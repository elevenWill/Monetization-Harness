# 15 — Real deadline with an accountable buyer

## Preconditions

- Current official evidence confirms a recurring external filing deadline.
- Missing the deadline creates a documented fee and an interruption to the
  customer's operations.
- The operations lead bears the consequence, controls the relevant budget, and
  can be reached during the seven-day purchase window.
- No Buying Situation has yet been persisted for this trigger.

## User message

> 我们每月都要在 15 号前完成平台申报，晚了会收滞纳金，还可能暂停店铺。运营负责人有预算，通常提前一周找人救急。这个场景值得做吗？

## Expected observable behavior

- Runtime verifies or reuses fresh official evidence for the deadline and
  consequence rather than treating the user's urgency alone as proof.
- The Why-Now Gate identifies a real Trigger Event, a hard_external deadline,
  an explicit Cost of Delay, the consequence owner, buyer/payer, seven-day
  purchase window, current workaround, reachability, trust requirement,
  low-trust entry, frequency, budget path, and delivery liability.
- The business classification is recurring_deadline_opportunity, while price,
  demand volume, provider trust, and the user's ability to deliver remain
  evidence-bound rather than being labeled high value automatically.
- If the situation is durably persisted, Runtime creates a non-empty BS001 under
  the appropriate Stage's buying-situations directory, links its FACTS,
  ASSUMPTIONS, Research, Cases, and Experiments, writes unknown for missing
  fields, and adds no project-root urgency file or empty directory.
- business-filter evaluates the complete Buying Situation; any proposed
  Deadline Replication Experiment uses the real monthly window, a low-trust
  initial deliverable, explicit downside/liability caps, payment or costly
  behavior criteria, and stop conditions.

## Failure conditions

- Calls the opportunity valuable solely because a date or anxious buyer exists.
- Invents the deadline source, penalty, payer, budget, recurrence, or trust.
- Creates BS001 without a real Buying Situation, fills unknown fields by
  inference, or adds DEADLINE.md or another project-root note.
- Recommends a full system before a bounded real-window transaction test.
