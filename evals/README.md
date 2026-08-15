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

The thirty-nine cases cover the V0 and VNext regression surface:

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
  delivery liability;
- Human Execution packets that make sourcing, qualification, exposure, offer,
  price, evidence, downside, stop, and review executable rather than saying only
  “find users”;
- Experiment diagnosis that distinguishes invalid or inconclusive execution from
  strict demand failure, keeps transactions separate from result codes, and uses
  the first broken selected step to shape the next test;
- reality-feedback corrections for relationship-biased payment, negative delivery
  economics, research or development avoidance, and buyer evidence that changes
  the original hypothesis;
- evidence-fit checks that separate reachability from decision relevance,
  content audience from payer, content platforms from distribution-only framing,
  and execution quality from hypothesis quality.

## Human Execution and Experiment Diagnosis

Cases 26–35 extend the corpus from advice quality into the full reality-feedback
loop:

- `26-unseen-outreach-is-not-demand-failure.md` — insufficient receipt and
  comprehension is a reachability break, not demand failure.
- `27-wrong-buyer-is-not-market-failure.md` — exposure to non-decision-makers
  invalidates a buyer test without rejecting the market.
- `28-compliments-without-payment.md` — praise is not an offer, payment, or
  transaction.
- `29-problem-evidence-is-not-business-evidence.md` — repeated pain can support a
  problem gate while buyer, result, price, and payment remain unresolved.
- `30-friend-payment-has-limited-transfer.md` — a real friendship payment is
  recorded while independent-market transfer remains confounded.
- `31-executable-customer-sourcing.md` — the next-day action specifies where,
  whom, how, qualification, funnel counts, evidence, limits, and review.
- `32-more-research-will-not-test-payment.md` — fresh sufficient research gives
  way to bounded reality contact when payment is the unknown.
- `33-building-will-not-test-payment.md` — an executable manual offer replaces
  architecture work that cannot observe willingness to pay.
- `34-payment-with-negative-delivery-economics.md` — a transaction can coexist
  with unvalidated or negative delivery economics.
- `35-buyer-feedback-reroutes-the-hypothesis.md` — contradictory field evidence
  can update assumptions and reroute or roll back Stage.

These cases score observable replies, evidence classification, next actions, and
workspace effects. Named Skill invocation is not itself a pass condition.

## Evidence Fit and Content-Market Roles

Cases 36–39 freeze four distinct failures observed in a real creator-business
dogfooding session:

- `36-reachable-sample-is-not-representative.md` — a nearby sample may answer a
  narrow problem-discovery question without representing content demand or
  monetization.
- `37-content-audience-is-not-automatically-payer.md` — audience pull does not
  identify the customer, buyer, payer, sponsor, platform, or bought result unless
  evidence links those roles.
- `38-content-platform-can-be-market-evidence.md` — a content platform may be a
  conditional observation environment for content pull and creator patterns, not
  only a future distribution channel and not a mandatory Web First route.
- `39-execution-does-not-validate-candidate.md` — founder fit, user agreement, and
  a concrete Execution Packet do not upgrade a model-derived candidate from
  hypothesis to market evidence, while cheap exploration remains allowed.

Together they ask whether a real evidence source is qualified to answer the
current decision claim. They do not require representative population research,
force platform search, prohibit small exploratory samples, or assume that an
audience and payer must be different actors.

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

For comparative outcome evaluation beyond this acceptance corpus, use the manual
[Harness-vs-Baseline A/B protocol](../docs/evaluation-strategy.md). It defines a
matched, blinded comparison and does not claim that any run has occurred.
