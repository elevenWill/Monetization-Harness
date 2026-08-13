# Behavior acceptance scenarios

V0 evals are human-auditable **Harness Behavior Acceptance Scenarios**. They are
not an automated LLM evaluation framework, and the repository does not treat
hand-written answers as if they were Runtime output.

Use these scenarios when changing `AGENTS.md`, the orchestrator, Thinking Skills,
stage rules, or workspace persistence:

1. Start a fresh Codex task in this repository with the scenario's preconditions.
2. Send the user message exactly as written.
3. Inspect both the reply and any workspace changes.
4. Compare only observable behavior with the expectations and failure conditions.

The six cases cover the minimum V0 regression surface:

- automatic project discovery, minimal bootstrap, and lazy workspace growth;
- interruption of premature product building;
- first-payment recording without premature productization;
- repeated payment and leverage routing;
- downside control for a large commitment;
- evidence-driven stage regression.

`scripts/validate_repo.py` is an optional development-only static validator. It
checks that this scenario corpus is present and structurally valid; it does not
run Codex, score responses, or replace the manual behavior review above.
