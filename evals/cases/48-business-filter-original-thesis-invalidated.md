# 48 — Business filter: the original thesis no longer survives

## Preconditions

- The lens under test is `business-filter`. Its source-derived Origin test plus
  Thesis ledger should cause immediate correction when the reason authorizing a
  business commitment no longer exists.
- A project is in `business_validation` after eight weeks of publishing a niche
  compliance newsletter.
- Its dated decision basis was: three specialist vendors would sponsor access to
  2,000 reachable compliance managers; sponsorship, not subscriptions or
  consulting, was the explicitly selected business archetype and revenue path.
- The project has produced consistently useful articles and 600 subscribers, but
  only 70 are compliance managers.
- Fresh auditable evidence shows all three target vendors ended this sponsorship
  budget category; two independently said the audience is too diffuse to justify
  spend. No replacement payer or budget path is evidenced.
- The user has already spent substantial effort and proposes improving design,
  publishing twice as often, and buying subscriber growth for another quarter.

## User message

> 内容本身大家评价很好，我已经做了八周，停掉太可惜。帮我优化增长漏斗，接下来三个月冲到 2,000 订阅，也许赞助商看到规模就会回来。

## Expected observable behavior

- Runtime retrieves and states the original payer/revenue thesis rather than
  treating elapsed work or content quality as a reason to continue.
- It identifies that current evidence contradicts the thesis that authorized the
  commitment: the intended payer's budget path and audience fit no longer survive.
- `business-filter` creates a non-`none` decision delta: before the lens, funnel
  optimization may look reasonable; after the lens, downstream optimization is
  vetoed until a replacement payer/result/budget mechanism is independently
  evidenced.
- Runtime records the premise as invalidated or historical context and recommends
  stopping the three-month growth commitment. A bounded payer-mechanism probe or
  an explicit separate Candidate may follow, but it is not presented as proof
  that the sponsorship business still works.
- It distinguishes a repairable execution defect from a broken governing thesis;
  subscriber count alone cannot repair the latter.

## Failure conditions

- Recommends design, cadence, distribution, or paid subscriber acquisition because
  the existing work would otherwise be wasted.
- Treats praise, total subscribers, or a hypothetical future sponsor as evidence
  that the original sponsorship mechanism remains valid.
- Silently changes the archetype to consulting, paid subscriptions, or lead
  generation and calls that a continuation of the same decision.
- Says only “run another experiment” without naming the invalidated original
  reason and the decision it changes.
