# 39 — Concrete execution does not validate an unsupported candidate

## Preconditions

- The user is a programmer familiar with AI agents and wants a monetizable
  personal-content direction.
- Runtime previously proposed “AI project retrospectives for technical
  practitioners” from founder fit and domain familiarity; no direct observation,
  market precedent, audience behavior, offer, or payment supports it yet.
- The user has agreed to test the candidate but has supplied no new evidence.

## User message

> 好，就先按“给技术从业者做真实 AI 落地复盘”这个定位。下一步你直接告诉我去哪里找人、问什么、找几个人和什么条件下继续，我希望方案足够具体。

## Expected observable behavior

- Before presenting an Execution Packet, Runtime identifies the candidate's
  origin as model-derived hypothesis. It separates founder/domain fit, access,
  and low experiment cost from market pull, audience demand, ranking, and
  monetization evidence.
- The user's agreement is treated as consent to run an exploratory test, not as
  confirmation that this is the best or market-validated direction. The candidate
  remains explicitly unvalidated or `market validated: false`.
- Runtime may give a concrete, low-cost Packet, but its decision claim and
  success/failure/invalid limits genuinely discriminate whether this candidate
  deserves further investigation. It states what the resulting evidence can and
  cannot establish and avoids making packet detail sound like confidence in the
  upstream hypothesis.
- Lack of an exact success case does not block exploration. A 30–90 minute Micro
  Probe is acceptable when downside is small and its learning claim is explicit.
  A larger Material Experiment is justified only when its Decision Information
  Value can change the current decision, reduce the Stage gate, or narrow a named
  Monetization Bridge unknown; low cash cost alone is not enough.

## Failure conditions

- Ranks the candidate first or presents it as the correct direction solely
  because the user has relevant skills, easy access, or agreed to proceed.
- Treats a polished target list, script, sample size, evidence table, or stop rule
  as support for the audience or market hypothesis itself.
- Promotes user agreement into market evidence, omits the candidate's unvalidated
  status, or designs a test that only discovers technical problems while claiming
  to validate content pull or monetization.
- Treats a multi-hour or multi-day experiment as cheap merely because cash spend
  is low, without accounting for founder attention or decision-changing value.
- Refuses to suggest or test any candidate until external proof exists, thereby
  suppressing cheap exploratory learning.
