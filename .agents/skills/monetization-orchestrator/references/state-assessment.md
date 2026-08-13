# Project and state assessment checklist

## Discovery decision

Ask in order before reading or writing a project:

1. Is this a substantive monetization thread, rather than knowledge, Harness usage, or generic one-off discussion?
2. Is the topic concrete enough that the user is likely to benefit from resuming it later?
3. Does an explicit reference or semantic continuity identify one existing project?
4. If several projects match, can current conversation context resolve ownership safely?
5. If none match, did the user establish enough direction to bootstrap without inventing the idea, goal, or customer?

No Project is a valid result. A provisional analysis under conflict must not mutate any candidate.

## Candidate matching

Read `workspace/_index.md`, enumerate actual `workspace/*/` project roots, then inspect the full `IDEA.md` and `STATE.md` of plausible candidates. A missing or stale registry row must not cause duplicate bootstrap. Compare:

- explicit project or stable-slug references;
- customer and payer;
- problem and purchased result;
- direction, offer, and current goal;
- distinctive facts, transactions, experiments, or next action;
- current-conversation continuity and registry recency.

A single domain word is insufficient. Prefer resuming a high-confidence match over creating a near-duplicate; prefer no write over a low-confidence match that could corrupt history.

## Minimum bootstrap state

Create `IDEA.md` with only:

- stable project slug and display name;
- creation date and active status;
- the user's initial idea;
- current goal;
- currently believed customer;
- decision-relevant initial assumptions.

Create `STATE.md` with discoverable:

- project, evidence-derived stage, active status, and updated date;
- total transactions and repeat customers (`0` only when supported; otherwise `unknown`);
- current goal and next gate;
- evidence-backed facts and active assumptions;
- draft/confirmed decisions, if any;
- largest unknown and material risk;
- active experiment, if any;
- one next action and its reason;
- last state change and relevant links.

Use `unknown` instead of filling gaps. Preserve the user's wording or a faithful paraphrase. Do not manufacture validation. During bootstrap, decision-relevant claims may be summarized with stable IDs directly in `STATE.md` without creating a Stage directory solely to make the project skeleton look complete.

## Minimum recoverable resumed state

On resume, the same fields must be discoverable from `STATE.md`. If an older project lacks one, preserve it as uncertainty and repair the snapshot only when doing so is a durable, evidence-grounded change.

## Snapshot coherence after new evidence

Treat a durable update as a state-wide consistency event, not a local counter edit. Re-read the complete updated `STATE.md` and reconcile:

- transaction totals and repeat-customer counts;
- active assumption status and basis;
- decision basis and revisit conditions;
- Stage, largest unknown, material risk, next gate, and next action;
- present-tense words such as `current`, `still`, `none`, `zero`, or `unvalidated` that new evidence may have made stale.

Preserve history without presenting it as current. Write “when D001 was made, transactions were 0,” not “transactions are still 0” after `T001`. A first payment may partially support willingness-to-pay assumptions while leaving independence and repeatability unproven; reflect both parts explicitly.

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

Determine Stage from evidence, never from directory existence. When computed stage differs from stored stage:

- explain the evidence conflict;
- prefer the earlier unsupported gate;
- do not change files until the new evidence or user decision is durable;
- if changed, record `from`, `to`, trigger Fact IDs, invalidated Assumption IDs, date, and Decision ID.
