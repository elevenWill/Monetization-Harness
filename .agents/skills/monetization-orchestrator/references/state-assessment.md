# State assessment checklist

## Minimum recoverable state

A `STATE.md` snapshot must make these fields discoverable:

- project, stage, status, updated date;
- total transactions and repeat customers;
- current goal and next gate;
- evidence-backed facts and active assumptions;
- draft/confirmed decisions;
- largest unknown and largest risk;
- active experiment and next action;
- reason for the next action;
- last state change and relevant links.

If a field is unknown, preserve `unknown`/“未知” rather than inferring it.

## Claim classification

Ask in order:

1. Did this happen, and is there a source? → FACT.
2. Is this an exchange of money? → TRANSACTION plus a linked FACT.
3. Is this believed but not sufficiently evidenced? → ASSUMPTION.
4. Has the user committed to an action? → DECISION.
5. Is it a bounded test with criteria and a stop? → EXPERIMENT.
6. Is it only a Skill suggestion? → analysis; do not persist as any of the above.

## Largest unknown test

The largest unknown is the earliest unanswered question whose answer could stop or substantially redirect the current plan. Common ordering:

1. Is there a concrete costly problem for a reachable user?
2. Will a buyer make a costly commitment or pay for the result?
3. Can payment and delivery repeat independently?
4. Which delivery work is stable enough to systematize?
5. Does the product preserve repeat value and economics?
6. Can acquisition and operations scale without ruin or quality collapse?

## Stage correction

When computed stage differs from stored stage:

- explain the evidence conflict;
- prefer the earlier unsupported gate;
- do not change files until the new evidence or user decision is durable;
- if changed, record `from`, `to`, trigger Fact IDs, invalidated Assumption IDs, date, and Decision ID.
