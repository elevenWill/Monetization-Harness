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

Do not add empty market-research headings or `market_evidence` fields during bootstrap. For a public-market project, finish this minimum bootstrap first; a Market Reality quick scan is a separate same-turn operation and may create a stage `research/` directory only together with a completed `Rxxx` artifact.

## Minimum recoverable resumed state

On resume, the same fields must be discoverable from `STATE.md`. If an older project lacks one, preserve it as uncertainty and repair the snapshot only when doing so is a durable, evidence-grounded change.

## Market evidence assessment

Run this assessment at the Market Reality Gate before selecting Thinking Skills:

1. Does the immediate judgment depend materially on current external market, platform, policy, price, competitor, content, acceptance, or precedent evidence?
2. If an `Rxxx` exists, does its scope match the current primary market, geography, platforms, content type, customer, and decision?
3. Is it fresh enough for the claim? Volatile platform, policy, price, availability, and competition claims age faster than durable historical cases; there is no universal freshness interval.
4. Does the artifact name the actual channels and source types checked, including first-party sources where a rule or policy is claimed?
5. Are material coverage gaps, inaccessible channels, negative findings, and contradictions explicit?

Classify market evidence as `not_started`, `partial`, `current`, `stale`, or `blocked`. `current` means fresh and scope-matched for the immediate decision, not exhaustive. `blocked` means a decision-critical channel or source could not be accessed and available evidence cannot support the conclusion. A different geography, platform, content type, customer, or decision scope is a mismatch, not reusable proof.

Only after real research exists, `STATE.md` may include a compact optional block such as:

```yaml
market_evidence:
  status: current
  scope:
    primary_market: "<market>"
    geography: "<geography>"
    platforms: ["<platform>"]
    content_type: "<type>"
    decision: "<decision supported>"
  last_checked_at: "<YYYY-MM-DD>"
  latest_research: "<repo-relative link to Rxxx>"
  exact_precedent: "<Cxxx link or none found in covered channels>"
  policy_status: "<time-qualified scope-specific summary or linked current finding>"
  coverage_gaps: ["<material gap>"]
```

When the `market_evidence:` block is present, also maintain the five current Markdown sections required by `docs/workspace-protocol.md`: current external evidence, latest research, closest verified pattern, current policy status, and research coverage gaps. Omit the block and all five headings when no real research exists; within an active snapshot, use `unknown` or a scoped negative finding rather than inventing facts. “No exact precedent found” must always be limited to the stated channels and search scope.

## Purchase Trigger assessment

After the Market Reality Gate, run the Why-Now Gate against each material opportunity and any active `BSxxx`. Read `docs/purchase-trigger-protocol.md`; do not infer a trigger from the abstract project name.

1. What real event starts active solution-seeking?
2. When must the bought result exist, who or what controls that date, and can it move?
3. What happens after delay, how certain is it, and who owns the consequence?
4. Is that owner the buyer, payer, or budget influencer with a usable budget path?
5. What workaround or no-action route exists, and how long can the buyer defer?
6. How long is the purchase window, and can the Runtime user identify and reach the buyer inside it?
7. What trust proof is required for an urgent task, and what low-trust entry avoids core-system access or unacceptable exposure?
8. Does the trigger repeat, at what frequency, and does it create predictable demand or synchronized capacity spikes?
9. What liability follows from late or incorrect delivery, and is it survivable?

Use `why_now_status: unknown` when the evidence is missing. Anxiety is at most a user-reported state; it is not evidence of a real consequence, budget, purchase, or willingness to pay. Seller-created promotions are marketing mechanics, and fabricated urgency is prohibited. Absence of a deadline does not invalidate a business supported by another recurrent purchase mechanism.

Only after a real Buying Situation is analyzed may `STATE.md` contain optional `purchase_trigger` state, linked to an actual `BSxxx`. The bootstrap operation remains only `IDEA.md` and `STATE.md` with no empty trigger block or stage directory.

## Snapshot coherence after new evidence

Treat a durable update as a state-wide consistency event, not a local counter edit. Re-read the complete updated `STATE.md` and reconcile:

- transaction totals and repeat-customer counts;
- active assumption status and basis;
- decision basis and revisit conditions;
- Stage, largest unknown, material risk, next gate, and next action;
- latest market-research link, scope, checked date, freshness status, exact-versus-adjacent precedent, policy status, and coverage gaps when market evidence exists;
- active Buying Situation, trigger and deadline classification, delay consequence and owner, purchase window, trust barrier, low-trust entry, evidence status, recurrence, reachability, and delivery liability when purchase-trigger state exists;
- present-tense words such as `current`, `still`, `none`, `zero`, or `unvalidated` that new evidence may have made stale.

Preserve history without presenting it as current. Write “when D001 was made, transactions were 0,” not “transactions are still 0” after `T001`. A first payment may partially support willingness-to-pay assumptions while leaving independence and repeatability unproven; reflect both parts explicitly. Likewise, when `R002` supersedes or contradicts `R001`, keep the old artifact as dated history, link the current one, mark the old conclusion stale or superseded in the snapshot, and reconcile affected FACT, ASSUMPTION, DECISION, risk, and next-action summaries.

## Claim classification

Ask in order:

1. Did this happen, and is there a source? → FACT.
2. Is this an exchange of money? → TRANSACTION plus a linked FACT.
3. Is this believed but not sufficiently evidenced? → ASSUMPTION.
4. Has the user committed to an action? → DECISION.
5. Is it a bounded test with criteria and a stop? → EXPERIMENT.
6. Is it a completed external investigation with explicit scope, checked date, sources, findings, and coverage gaps? → RESEARCH.
7. Is it a structured external precedent worth reusing independently of one research run? → CASE linked to its supporting RESEARCH and source IDs.
8. Is it a concrete trigger-to-bought-result chain being analyzed for why-now behavior? → BUYING SITUATION with a stable `BSxxx`; preserve each unsupported link as `unknown`.
9. Is it only a Skill suggestion, unsupported interpretation, or model inference? → analysis; do not persist as any of the above.

An external source does not automatically create a FACT. Persist only decision-relevant claims, cite their supporting source or `Rxxx`/`Cxxx`, and apply the claim-specific evidence rules in `docs/object-protocol.md`. An exact or adjacent external case can support market existence or a constraint, but cannot by itself establish this project's willingness to pay, repeatability, or stage.

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

The Market Reality Gate is a routing and evidence-freshness check, and the Why-Now Gate is a Buying-Situation check; neither is a Stage or next gate. Completing research, creating `Rxxx`/`Cxxx`/`BSxxx`, finding a precedent, or classifying a deadline does not advance the project unless the project's Stage criteria are independently met by the required evidence.
