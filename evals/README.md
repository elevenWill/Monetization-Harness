# Behavior acceptance scenarios

V0 evals are human-auditable **Harness Behavior Acceptance Scenarios**. They are
not an automated LLM evaluation framework, and the repository does not treat
hand-written answers as if they were Runtime output.

Use these scenarios when changing `AGENTS.md`, the orchestrator, the Market
Reality Layer, the Why-Now Gate, Thinking Skills, evidence/stage rules, or
workspace persistence:

1. Start a fresh Codex task in this repository with the scenario's preconditions.
2. Send the user message exactly as written.
3. Inspect both the reply and any workspace changes.
4. Compare only observable behavior with the expectations and failure conditions.

The twenty-five cases cover the V0 regression surface:

- complete project-lifecycle routing: no project/no write, semantic resume,
  minimal bootstrap with lazy growth, and conflict/no wrong write;
- interruption of premature product building;
- first-payment recording without premature productization;
- repeated payment and leverage routing;
- downside control for a large commitment;
- evidence-driven stage regression;
- required research before market-dependent judgment;
- exact-versus-adjacent precedent discipline;
- vendor-claim and policy-freshness handling;
- transferability checks and Agent Reach fallback;
- deliberate reuse of fresh research without unnecessary search;
- proven-pattern-first replication instead of invented complexity;
- real versus weak, one-off, recurring, seller-created, or fabricated deadlines;
- cost-of-delay ownership, buying windows, reachability, and trust barriers;
- valid recurring businesses without deadlines and urgent work with high
  delivery liability.

## Project Lifecycle

Four scenarios jointly verify whether Runtime manages Workspace lifecycle rather
than merely creating projects:

- `01-new-project-auto-bootstrap.md` — **New Project Bootstrap** for a concrete,
  durable direction with no existing semantic match.
- `23-no-project-no-write.md` — **No Project / No Write** for ordinary knowledge
  discussion or a passing idea that is not a durable thread.
- `24-existing-project-resume.md` — **Existing Project Resume** when one existing
  project clearly matches the goal, problem, customer, transaction context, and
  current state despite changed wording.
- `25-project-conflict-no-wrong-write.md` — **Project Conflict / No Wrong Write**
  when multiple projects plausibly match and a wrong choice would contaminate
  durable state.

The routing model is:

```text
Conversation
└── Is this a durable monetization thread?
    ├── No  → No Project / No Write
    └── Yes → Does one existing project clearly match?
              ├── Yes      → Existing Project Resume
              ├── No       → New Project Bootstrap
              └── Multiple → Project Conflict → No Write Until Resolved
```

Avoiding incorrect persistence takes priority over automation convenience. A
clear match should resume automatically, a clearly new durable direction should
bootstrap automatically, ordinary discussion should not create a project, and a
material conflict should remain unwritten until a minimal clarification resolves
ownership. Workspace is long-term project memory, not a chat log.

The Purchase Trigger cases ask why a buyer would act now: what event occurred,
when the result is needed, what delay actually costs, who bears that consequence,
whether that person controls budget, whether the buyer is reachable inside the
purchase window, and what proof is required before an urgent task can be trusted
to a new provider. High anxiety or a nearby date alone is not commercial proof.
A deadline becomes useful evidence only when its source and consequence are real
and the purchase, trust, reachability, and delivery constraints also hold. A
business with repeat purchases or another durable trigger is not rejected merely
because no deadline exists.

`market-reality-researcher` is an evidence-producing Skill, not a sixth Thinking
Lens. A case may require it before the normal one-or-two Thinking Skills. Review
the sources actually opened, scope labels, coverage gaps, workspace artifacts,
and user-visible conclusion; the mere presence of links or a research-looking
answer is not a pass.

`scripts/validate_repo.py` is an optional development-only static validator. It
checks that this scenario corpus is present and structurally valid; it does not
run Codex, access markets, score responses, or replace the manual behavior review above.
