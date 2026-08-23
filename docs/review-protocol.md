# Thinking Skill review protocol

Thinking Skills return a compact review to the orchestrator. They do not present a persona panel to the user and do not expose hidden chain-of-thought.

Before requesting a review, the orchestrator selects the decision-changing Reality Evidence. `market-reality-researcher` is an evidence-producing capability, not a Thinking Skill: it does not emit a lens review and does not consume one of the normal one-or-two lens slots. When external research runs, the orchestrator must classify and persist the material evidence first, then hand the selected Thinking Skills a compact market-evidence packet containing the relevant `Rxxx`/`Cxxx` links, scope, checked date, exact-versus-adjacent status, supporting and contradicting findings, policy status, and coverage gaps. When direct or existing project evidence is sufficient, no market packet or ceremonial search is required.

When purchase timing is material and the full Why-Now Gate runs, the orchestrator gives the selected Skills the active `BSxxx` or an explicit hypothesis packet: trigger, deadline source/type, Cost of Delay, consequence owner, buyer/payer, workaround, purchase window, reachability, trust barrier, low-trust entry, frequency, evidence status, and delivery liability. Missing fields remain `unknown`; a review must not convert urgency language into FACT. Opportunity discovery otherwise passes only any light trigger-mechanism clues relevant to candidate ranking.

```yaml
lens: assumption-challenger
severity: high
finding: "The proposed admin dashboard is being treated as a requirement without user evidence."
facts:
  - "F004: No customer has paid."
assumptions:
  - "A007: A management dashboard is necessary before a customer can buy."
reasoning_summary: "The build request addresses product completeness while the current gate is first payment."
decision_delta: "Replaces a dashboard build with a qualified manual offer against the first-payment gate."
recommended_action: "Offer the result manually to five qualified buyers before specifying a dashboard."
stop_condition: "Stop after five qualified offers or the first payment, then review evidence."
```

## Field rules

- `lens`: Skill directory name.
- `severity`: `low`, `medium`, `high`, or `critical`. Critical means plausible ruin, unlawful/harmful action, or irreversible loss; high means the current direction targets the wrong gate.
- `finding`: One decision-relevant conclusion.
- `facts`: Only evidence-backed facts, preferably stable IDs. An external FACT must cite its `Rxxx`, `Cxxx`, or local source ID and stay within that evidence's scope. Use `[]` when none exist.
- `assumptions`: Named unsupported claims, preferably stable IDs or `PROVISIONAL-A...` when not yet persisted.
- `reasoning_summary`: One to three auditable sentences; never hidden chain-of-thought.
- `decision_delta`: What changed from the orchestrator's pre-lens provisional judgment. Use `none` when the lens confirms it; never invent a difference to justify the Skill.
- `recommended_action`: One bounded action that addresses the finding.
- `stop_condition`: Observable point at which to stop or re-evaluate.

For an `opportunity-finder` review, keep the common fields above rather than
adding a score or a new schema. Its `finding` and `reasoning_summary` must expose
the Candidate origin, comparison role/decision level, business archetype and
whether it is committed or hypothetical, evidence status, commercial bridge,
largest bridge unknown, and inference scope; separate Opportunity Evidence from
Investigation Advantage. Normalize mixed tool/topic/format/channel/audience/
monetization/offer components before comparison; do not rank them as if they were
business directions at one level.
Founder fit, reachability, test cost, user agreement, and Packet specificity may
change learning order but cannot raise Market Priority.
When comparison evidence is weak, asymmetric, or incomparable, the review must
say `Market Priority: unknown`, omit an ordinal business ranking, and label any
chosen probe only the `first exploratory test`. A single star account, viral item,
vendor story, or isolated success is a lead rather than a comparison winner.

For a material income-seeking experiment, the review must also state what success
and failure change, which Monetization Bridge or money-path unknown the result can
reduce, the founder-attention/total-downside cap, and why its decision information
exceeds a smaller safe alternative. A single reversible 30–90 minute probe may
leave monetization `unknown`, but its finding must remain a narrow audience/value
inference rather than commercial validation. Existing auditable payment or
delivery evidence follows the direct Stage route without a ceremonial revenue-
model scan.

## Synthesis contract

The orchestrator records a provisional judgment before requesting a lens, then resolves conflicts using the claim-specific evidence rules in `docs/object-protocol.md`, Stage relevance, the active Buying Situation, and downside—not by voting or by treating all source types as one ladder. The project's own payment, behavior, and usage evidence controls Stage and transferability judgments; external research establishes only the market facts, precedents, constraints, purchase-trigger signals, or analogies its recorded scope supports. Every `high` or `critical` lens finding must be explicitly accepted in the final judgment/action or rejected with stronger named Evidence; synthesis must not silently dilute it.

Before output, treat the candidate next action as a Draft Action and revalidate
the prerequisites it newly introduces: capability, access, trust, delivery,
economics, legal/policy, business archetype, buyer/payer, and critical
dependencies. If a new blocking assumption appears, shrink the action, test that
assumption, or reroute once. Revalidate the replacement once; if uncertainty
remains, expose it and choose the smallest evidence action. A Draft Action cannot
silently switch business archetypes or make a customer absorb an untested
delivery-learning risk.

The final user response normally contains the following information, but these are information slots rather than required labels:

1. `当前判断` — one conclusion.
2. `依据` — the few decisive facts and assumptions.
3. `下一步` — one bounded action with a stop/review condition.
4. `项目记录` — only if durable state changed.

Translate internal review language before output. The user-facing answer should name the concrete situation and action rather than Stage, gate, Candidate, Reality Evidence, Market Priority, Buying Situation, Execution Packet, Draft Action, lens, or a newly coined Chinese procedure name. Keep the underlying distinction by saying what the available information can and cannot show. Keep the full action contract by saying where to act, what to do, how much to do, what to record, and when to stop. If a specialist term is necessary, explain it once in ordinary Chinese. This applies to commentary as well as the final answer and does not alter evidence, routing, safety, persistence, or review requirements.

Mention lens names only when the user asks for provenance or it materially improves auditability.

When market evidence materially affects the decision, the synthesis must also distinguish verified exact precedent from reported or adjacent precedent, state what was not verified, and disclose the principal freshness or coverage limit. Research that is blocked, stale, or scope-mismatched supports an `unknown` or recheck action, not a confident market conclusion.

When the Why-Now Gate materially affects the decision, name the Buying Situation outcome, the verified trigger/consequence links, what remains `unknown`, and the feasible low-trust next action or liability stop. Do not emit a numeric urgency score or equate high anxiety with high conversion.
