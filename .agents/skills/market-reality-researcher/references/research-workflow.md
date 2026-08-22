# Research Workflow

Use this workflow for every new or refreshed `Rxxx`.

## 1. Define the decision

Write one decision question and the claim whose truth would change the next action. Fix the scope: geography, platform, content type, actor/customer, payer, offer, bought result, and time sensitivity. List scope distinctions that could turn a result into merely adjacent evidence.

For a comparison, first identify the decision role of every supplied item. Do not
issue head-to-head queries across tools/capabilities, topics, formats, channels,
audiences, monetization mechanisms, business structures, and offers. If the
question is how the user can earn, define peer monetization structures and map
those lower-level components only after their money mechanisms are reconstructed.

If the decision depends on why a buyer acts now, define the candidate purchase-trigger chain and the exact link being tested: event, deadline/time window, consequence of delay, consequence owner, buyer/payer, workaround, purchase window, trust requirement, bought result, or recurrence. Do not treat urgency language as a completed chain.

Check the project for a fresh, scope-matched `Rxxx`. Reuse it if sufficient. Refresh when policy, admission rules, AI disclosure, account requirements, price, competitor state, API/platform capability, traffic, ads, or content rules could have changed enough to alter the decision.

## 2. Select depth and stop conditions

Record `research_depth` as exactly `quick`, `standard`, or `deep`, including for a targeted freshness refresh. Record `purpose: policy_refresh` or a similarly scoped research question separately; do not create a fourth depth value such as `targeted_refresh`.

- `quick`: reconnaissance for a new public-market project or whether deeper work is warranted.
- `standard`: viability, precedent, experiment, or material commitment decision.
- `deep`: explicit depth, major commitment, or multi-platform entry.

Record a maximum reasonable search scope. Normally stop when the evidence can distinguish exact precedent, adjacency, contradiction, policy constraint, and remaining unknowns. For a transaction-led proven-path request, stop only when at least one transaction-bearing Case exposes payer, bought result, credible transaction/money signal, and delivery well enough for transferability, or when the declared query/time/channel budget is exhausted. In the latter case state `playbook evidence blocked`, list the missing fields, and do not default to cold discovery. Do not keep searching to manufacture certainty. If critical platforms cannot be accessed, use `research_blocked` when the gap prevents a decision; otherwise report the bounded verdict and gap.

## 3. Build the query plan

Read [query-playbook.md](query-playbook.md). Generate separate query groups for:

1. exact successful transactions or sustained operation;
2. adjacent precedents, explicitly labeled;
3. failure and negative evidence;
4. current official policy;
5. user behavior and acceptance;
6. competitors, prices, substitutes, and real buying signals.

Record the actual queries used, not only the planned keywords.

For trigger-dependent work, also read [trigger-event-search.md](trigger-event-search.md) and [deadline-signal-search.md](deadline-signal-search.md). Add query groups for the event source, buyer-originated urgent behavior, delay consequences, workarounds, purchase timing, accepted rush pricing, trust/liability failures, and recurrence. Include a non-urgent control query.

## 4. Choose sources and channels

Read [source-strategy.md](source-strategy.md). Match source authority to each claim. For deadline research, use the claim-specific source table in [deadline-signal-search.md](deadline-signal-search.md); an official calendar can verify a date but not willingness to pay. Route Agent Reach, AnySearch, their combination, and Runtime fallbacks by evidence surface as documented in `docs/integrations/agent-reach.md`. Record the capability plus channel/backend actually used and every relevant inaccessible surface as a `coverage_gap`.

Do not treat snippets as read pages. Open the original source, capture its URL, publisher, publication date when available, access date, and the narrow claim it can support.

## 5. Collect both directions

Collect supporting and contradicting evidence. A standard study covers successful cases, negative cases, official policy, user behavior, and competitors/substitutes. Search negative terms intentionally. Record `no negative case found in current coverage` if applicable; do not convert search failure into evidence of safety.

When why-now is in scope, collect both buyer-originated and seller-originated urgency signals. Search late delivery, extension, rescheduling, no consequence, planned procurement, incumbent workaround, rejected delegation, refunds, disputes, and liability. A provider's rush offer is supply evidence until a buyer accepts or pays.

Store raw tool output only under `/tmp`. Retain in the durable artifact only structured claims, brief necessary excerpts or faithful paraphrases, source metadata, classifications, and gaps.

## 6. Classify evidence

For each source, set `authority`, `verification`, `freshness`, `scope_match`, and `direction` using the exact enums in `SKILL.md`. Explain the source-to-claim inference. A vendor claim proves that the vendor made a claim unless independently corroborated; it does not directly prove the reported customer outcome.

Keep policy, market-existence, acceptance, and user-transferability evidence ladders separate. Time-qualify every current claim.

Keep trigger-event evidence separate too. Classify source quality with the existing enums, then record deadline type, source, consequence, owner, buying behavior, and missing links as structured findings. Do not add trigger-specific values to the Research depth, source-quality, case-status, or verdict enums.

## 7. Reconstruct cases

Read [case-reconstruction.md](case-reconstruction.md). Promote a candidate to `Cxxx` only when it is useful for the current decision or future comparison. Assign exactly one case verification status. Do not upgrade adjacent cases because they are numerous.

Separate evidence that only reconstructs audience attention from evidence that
reconstructs revenue. Unknown payer, paid result, or money signal remains
`unknown`; an attention case cannot become a monetization pattern by inference.

Use plain working labels without changing the Case status enum: a **Lead** shows
only demand/supply interest; a **Transaction-bearing Case** exposes payer,
bought result, transaction mechanism, credible paid signal, and delivery; a
**Replication-grade Playbook** additionally contains enough conditions and gaps
to design a transferability-checked action. Unknown fields remain explicit.

## 8. Test transferability

Read [transferability-check.md](transferability-check.md). Classify every mechanism or advantage as `Copyable`, `Context-dependent`, `Non-copyable`, or `Unknown`. Distinguish market existence from the current user's ability to reproduce the result.

## 9. Decide the verdict

Choose one allowed research verdict. State separately:

- whether an exact precedent exists;
- whether current policy permits or conditions the activity;
- whether observed behavior supports acceptance;
- whether the closest case is transferable;
- whether the user possesses the required conditions.

When applicable, also state whether the event and deadline are verified, whether delay has an observed consequence and owner, whether the buyer or payer took costly action, whether the purchase window is reachable, and whether urgency raises a blocking trust or delivery-liability constraint. These are evidence findings, not new research verdict values.

Prefer `insufficient_evidence` over a synthesized yes/no when evidence is weak. Use `adjacent_precedent_only` whenever no exact case is supported but adjacent modes exist.

## 10. Produce playbook and replication basis

Output the Closest Proven Playbook: value actor, repeated value, observed
behavior, payer, monetization mechanism, bought result, money signal, acquisition,
delivery, trust, critical conditions, platform constraints, copyable pieces,
non-copyable pieces, and user gaps. If exact precedent is absent, explicitly name
the nearest adjacent playbook and its decisive mismatch.

For a trigger-dependent decision, include the closest evidenced buying situation: trigger, deadline, consequence owner, workaround, purchase window, trust requirement, frequency, and the exact missing link. Do not create a `BSxxx`; pass supported fields and source IDs to the orchestrator, which owns workspace object classification and persistence.

Hand the evidence to the orchestrator before Thinking Skills run. Give `experiment-designer` a replication basis naming the relevant `Cxxx`, copied mechanism, omitted advantages, migration assumption, maximum exposure, success criterion, failure criterion, and stop condition.

If transaction-led research ends blocked, map each decision-critical missing
field to the cheapest remaining evidence source. Prefer public transaction
surfaces, buyer briefs, seller offers/packages, quotes, portfolios, delivery
descriptions, reviews, modification/refund records, repeat postings, or continued
buyer/seller operation before Human Contact. If public evidence is reasonably
exhausted, hand off one exact field and question—not generic market discovery.

## 11. Persist only when authorized

Follow the repository workspace mutation rules. Create a Stage `research/` or `cases/` directory only in the same write as its first real artifact. Do not put research entry files at the project root. Update `STATE.md` only if research was actually completed and the current snapshot materially changed.

When a completed study changes the snapshot, the optional state shape is:

```yaml
market_evidence:
  status: not_started | partial | current | stale | blocked
  scope:
    primary_market:
    platforms:
    content_type:
  last_checked_at:
  latest_research:
  exact_precedent:
  policy_status:
  coverage_gaps:
```

Use these fields only after market research exists; do not populate empty market blocks in every new project.
