# Thinking Skill review protocol

Thinking Skills return a compact review to the orchestrator. They do not present a persona panel to the user and do not expose hidden chain-of-thought.

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
- `facts`: Only evidence-backed facts, preferably stable IDs. Use `[]` when none exist.
- `assumptions`: Named unsupported claims, preferably stable IDs or `PROVISIONAL-A...` when not yet persisted.
- `reasoning_summary`: One to three auditable sentences; never hidden chain-of-thought.
- `recommended_action`: One bounded action that addresses the finding.
- `stop_condition`: Observable point at which to stop or re-evaluate.

## Synthesis contract

The orchestrator resolves conflicts by evidence strength, stage relevance, and downside—not by voting. The final user response normally contains:

1. `当前判断` — one conclusion.
2. `依据` — the few decisive facts and assumptions.
3. `下一步` — one bounded action with a stop/review condition.
4. `Workspace 更新` — only if durable state changed.

Mention lens names only when the user asks for provenance or it materially improves auditability.
