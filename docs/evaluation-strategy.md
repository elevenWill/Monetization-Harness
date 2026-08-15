# Harness-vs-Baseline A/B Evaluation Protocol

This protocol asks whether Monetization Harness improves real monetization
decisions over a strong model with the same Web access. It complements the
human-auditable behavior scenarios in `evals/`; it does not replace them or score
mere rule compliance.

This document is an evaluation design, not an automated runner. The repository
contains no generated fixtures, run outputs, or claimed results, and reviewers
must not present hypothetical scores as observed evidence.

## Comparison and unit of evaluation

Use two fresh, independent tasks for every scenario:

- **Arm A — Baseline:** the selected strong model plus Web access, without
  Monetization Harness instructions, Skills, project state, or Harness-specific
  examples.
- **Arm B — Harness:** the same model plus Web access, with the repository's
  normal Harness runtime, relevant Skills, and a scenario-matched project state
  when one is part of the test.

The evaluation unit is the complete decision trajectory, not one polished reply.
It includes the initial recommendation, the human-executable action, subsequent
Reality Feedback, diagnosis, persistence when applicable, and the revised next
decision. A scenario may have no Workspace in Arm A; judges compare the decision
quality and continuity, not file-count symmetry.

## Scenario construction

Sample concrete cases across project lifecycle, all eight evidence-derived
Stages, current-market uncertainty, deadline and non-deadline buying mechanisms,
first and repeated transactions, delivery economics, large commitments, failed
reachability or qualification, and contradictory buyer feedback. Include both
cases where research is decision-critical and cases where direct field evidence
is the cheaper source.

Prompts should sound like real user messages and must not teach the expected
Harness vocabulary. Predeclare for each scenario:

- the hidden evidence record and which statements are FACT, ASSUMPTION, or
  deliberately unknown;
- the earliest unresolved uncertainty and plausible simpler alternative paths;
- safety or ruin boundaries;
- the staged Reality Feedback to reveal after each human action;
- terminal evidence, success/failure conditions, and when stopping the project is
  a legitimate recommendation.

Do not assume Arm B should win. Include negative controls where ordinary model
judgment is sufficient and creativity, restraint, or a simpler path matters more
than protocol depth.

## Matched controls

Match the two arms on everything except access to Harness:

- exact user messages and feedback order, language, dates, geography, currency,
  and hidden facts;
- model family, snapshot, reasoning setting, sampling parameters, token budget,
  turn limit, and wall-clock budget;
- fresh-task status and prior conversation context; neither arm may see the other
  response or judge rubric;
- Web availability, search providers, authentication state, permitted domains,
  tool permissions, and tool-use time budget;
- attachment contents and any non-Harness project facts needed to act.

Tool availability is matched; tool-call counts are not forced to match because
deciding whether to search is part of the behavior under test. Record outages,
blocked pages, rate limits, model changes, and material latency. If one arm loses
access to a decision-critical source, invalidate or rerun the pair rather than
scoring the outage as reasoning quality.

Whenever Arm B receives Workspace or another structured evidence source, give Arm A a neutral factual brief containing the same underlying user evidence, dates, and unknowns while withholding Harness labels and prescriptions. Record the evidence-equivalence mapping before either response. This equalizes evidence without leaking the treatment and applies to every scenario, not only project resumption.

## Multi-turn Reality Feedback procedure

1. Send the identical initial user message to both fresh tasks.
2. Let each arm recommend an action. A human operator records whether the action
   is executable, safe, and specific enough to perform without filling material
   gaps by inference.
3. Reveal the same predeclared Reality Feedback that corresponds to equivalent
   action exposure. If the actions differ materially, use the scenario's branch
   table to reveal outcome-equivalent evidence; do not reward an arm with easier
   facts merely because it requested them.
4. Continue for at least one diagnosis-and-revision turn. Use additional rounds
   when reachability, offer comprehension, payment, delivery, or recurrence only
   becomes distinguishable over time.
5. Stop at the predeclared terminal condition: the key decision is resolved, an
   explicit safe stop/pivot is warranted, the turn/time budget is exhausted, or
   further feedback would no longer distinguish the arms.

Reality Feedback must be authored before seeing responses and must include
unfavorable or contradictory outcomes. Never fabricate actual interviews,
payments, metrics, or execution; synthetic scenario evidence must remain labeled
as such. A real-field study must use consented, independently recorded evidence.

## Blind judging

Remove arm labels, Harness vocabulary that is not essential to meaning, file
paths, and other treatment-identifying metadata from the review transcript.
Randomize answer order per scenario. At least two judges independently review the
complete trajectory; a third resolves material disagreement. Judges disclose
Harness authorship or other conflicts before scoring.

Each dimension receives `0` (harmful or absent), `1` (major miss), `2` (mixed),
`3` (good), or `4` (excellent), with a one-sentence evidence citation to the
transcript. Judges may mark a dimension `N/A` only when the predeclared scenario
cannot expose it; do not convert `N/A` to zero. Report per-dimension paired
differences, medians, disagreement, and scenario-level qualitative findings
before any aggregate.

## Seventeen judge dimensions

1. **Corrects the question:** notices when the requested solution or question is
   not the decision the user currently needs.
2. **Earliest uncertainty:** identifies the earliest unresolved claim that could
   stop or redirect the project.
3. **Fact discipline:** separates observations, user reports, assumptions,
   inferences, decisions, and unknowns with provenance appropriate to each claim.
4. **Reality evidence:** obtains or reuses the cheapest decision-changing market
   or first-party evidence rather than defaulting to thought or ceremonial search.
5. **Negative evidence:** actively seeks failures, complaints, refunds,
   enforcement, rejection, or other counterevidence when it could change the call.
6. **Policy and platform risk:** checks current authoritative constraints when
   relevant and preserves access, scope, and freshness gaps.
7. **Real precedents:** finds and verifies exact or adjacent cases using behavior,
   transaction, or operating evidence rather than popularity or vendor copy.
8. **Transferability:** states what a precedent establishes, what differs here,
   and which project-specific transfer claim still needs testing.
9. **Build restraint:** avoids development, automation, scaling, or irreversible
   commitment before the relevant demand, repetition, delivery, or economics gate.
10. **Executable action:** proposes a bounded real action with evidence, downside,
    invalid/failure, stop, and review conditions.
11. **Next-day clarity:** a human knows where to go, whom to contact, how to
    qualify them, what to say or offer, and what to record the next day.
12. **Payment test quality:** uses a real result, price and payment terms,
    qualified buyer exposure, a decision window, and honest success criteria.
13. **Failure diagnosis:** distinguishes invalid, inconclusive, and strict demand
    failure; locates the first broken observable step without inventing a cause.
14. **Model creativity:** preserves useful synthesis and can find a simpler,
    smarter, scenario-specific path instead of mechanically replaying a template.
15. **Constraint proportionality:** loads and applies only relevant protocol;
    avoids needless gates, documents, searches, questions, or funnel steps.
16. **Stop recommendation:** clearly recommends stopping, narrowing, or abandoning
    the direction when downside or accumulated evidence crosses the declared bar.
17. **Reality-led revision:** changes assumptions, Stage/direction, and next action
    when new field evidence contradicts the original idea.

## Outcome-first decision rule

Predeclare three primary measures before running a study:

1. **Decision quality:** did the trajectory choose the soundest continue, test, narrow, stop, or rollback decision supported by the revealed evidence?
2. **Next-day executability:** could the operator act safely without inventing a decision-critical source, role, qualification, offer, price, or stop rule?
3. **Time-to-decision-changing evidence and harm:** how much operator time, search, build effort, money, exposure, and avoidable downside were spent before obtaining evidence that changed or resolved the decision?

The seventeen dimensions are diagnostic explanations, not seventeen equally weighted votes for Harness vocabulary. Predeclare the paired-winner rule, tie rule, treatment of `N/A`, and whether a primary-measure conflict means “no winner” before unblinding. Apply the over-constraint penalty after judging the primary measures. Baseline wins whenever it reaches a materially better primary outcome through a simpler safe path, regardless of Harness compliance or diagnostic-dimension count.

## Over-constraint penalty

Apply a separate penalty to either arm, with special scrutiny of Arm B, when
process burden causes a material decision error that Dimension 15 alone would
understate:

- `0` — no material over-constraint;
- `-2` — avoidable friction or irrelevant protocol, but the same useful path
  remains executable;
- `-5` — the arm materially delays or obscures a simpler decision-changing path;
- `-8` — the arm rejects, misses, or makes unsafe a clearly superior simple path
  because it follows rules mechanically.

The judge must name the missed alternative and cite the transcript. Length,
formatting, or use of Harness terminology alone is not a penalty. If Baseline
finds a simpler, safer, more creative route and Harness misses it because of its
rules, Harness loses that paired comparison even if its acceptance compliance is
higher.

## Analysis and stopping recommendations

Keep primary outcomes, raw dimension scores, penalties, judge rationales, tool/access incidents, and trajectory notes separable. Do not invent an aggregate after seeing results or claim a general Harness benefit from a single total. Report the predeclared paired winner or no-winner result, then which scenario families improve, regress, or remain uncertain; inspect regressions for rule-loading cost or lost creativity.

Before running a study, declare the number of scenario pairs and review point.
After that point, recommend one of: keep the Harness behavior, narrow a rule,
remove a rule, design a discriminating follow-up, or stop the evaluated direction.
Stop adding runs when the predeclared evidence threshold is met, a safety issue
requires intervention, matched controls are repeatedly broken, or additional
pairs no longer change the decision. Expanding the sample after seeing favorable
scores requires a new declared study, not silent continuation.

Acceptance cases remain the regression guardrail for required behavior. This A/B
protocol answers a different question: whether those constraints help a real
human make a better next decision than the same model could make without them.
