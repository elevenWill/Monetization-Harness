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
- `recommended_action`: One bounded action that addresses the finding.
- `stop_condition`: Observable point at which to stop or re-evaluate.

For an `opportunity-finder` review, keep the common fields above rather than
adding a score or a new schema. Its `finding` and `reasoning_summary` must expose
the Candidate origin, business archetype, evidence status, commercial bridge,
and inference scope; separate Opportunity Evidence from Investigation Advantage.
Founder fit, reachability, test cost, user agreement, and Packet specificity may
change learning order but cannot raise Market Priority.
When comparison evidence is weak, asymmetric, or incomparable, the review must
say `Market Priority: unknown`, omit an ordinal business ranking, and label any
chosen probe only the `first exploratory test`. A single star account, viral item,
vendor story, or isolated success is a lead rather than a comparison winner.

## Synthesis contract

The orchestrator resolves conflicts using the claim-specific evidence rules in `docs/object-protocol.md`, Stage relevance, the active Buying Situation, and downside—not by voting or by treating all source types as one ladder. The project's own payment, behavior, and usage evidence controls Stage and transferability judgments; external research establishes only the market facts, precedents, constraints, purchase-trigger signals, or analogies its recorded scope supports.

The final user response normally contains:

1. `当前判断` — one conclusion.
2. `依据` — the few decisive facts and assumptions.
3. `下一步` — one bounded action with a stop/review condition.
4. `Workspace 更新` — only if durable state changed.

Mention lens names only when the user asks for provenance or it materially improves auditability.

When market evidence materially affects the decision, the synthesis must also distinguish verified exact precedent from reported or adjacent precedent, state what was not verified, and disclose the principal freshness or coverage limit. Research that is blocked, stale, or scope-mismatched supports an `unknown` or recheck action, not a confident market conclusion.

When the Why-Now Gate materially affects the decision, name the Buying Situation outcome, the verified trigger/consequence links, what remains `unknown`, and the feasible low-trust next action or liability stop. Do not emit a numeric urgency score or equate high anxiety with high conversion.
