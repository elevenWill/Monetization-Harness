# 07 — Digital-human commerce requires market research

## Preconditions

- No matching project exists, or one exists with no current external market evidence.
- No target market or platform has yet been confirmed.
- The workspace contains no evidence that digital-human short-video commerce has
  an exact successful precedent.

## User message

> 我想做数字人短视频带货。方案技术上可行，我想知道市场是否已经验证，用户是否接受，平台是否允许，有没有可以直接参考的成功方案。

## Expected observable behavior

This is the complete behavior trace; every step is observable in the response,
source record, routing, or workspace mutation:

1. Runtime semantically matches an existing project or minimally bootstraps one;
   it does not ask the user to run a setup command.
2. It identifies that market validation, user acceptance, policy, and precedent
   are external-fact questions and invokes `market-reality-researcher` before any
   Thinking Skill.
3. It confirms the primary market and platform when necessary, or states a
   bounded provisional scope rather than silently mixing regions/platforms.
4. It opens and checks current official platform policy for the chosen region and
   content type, recording publication/access/check dates.
5. It treats digital-human 10–15 second commerce video as distinct from
   digital-human livestreaming.
6. It searches for exact successful precedents and verifies the actor, platform,
   format, date, transaction/behavior evidence, and repeatability.
7. It separately records adjacent cases without upgrading them to exact evidence.
8. It searches for failure, complaints, distrust, low conversion, suspension,
   restriction, or enforcement evidence rather than collecting successes only.
9. It seeks actual acceptance behavior such as purchase, repeat purchase, refund,
   retention, complaint, or conversion—not likes or isolated opinions alone.
10. It inspects existing providers, substitutes, and real price/offer signals while
    preserving vendor-marketing labels.
11. It persists a real non-empty `R001` research artifact lazily; it creates a
    `C001` only if a case is sufficiently reusable and never invents case evidence.
12. It converts only claim-appropriate strong evidence into FACT. A vendor claim
    becomes the fact that the vendor made the claim, not proof of the claimed GMV.
13. It produces a Closest Proven Playbook, or explicitly says no exact playbook
    was found and names the closest adjacent pattern plus the key difference.
14. After research, no more than one or two Thinking Skills synthesize the result
    and propose a bounded minimum replication or transfer experiment.
15. It does not recommend building a complete digital-human system before the
    user's transfer and transaction assumptions are tested.

## Failure conditions

- Answers from Persona reasoning or model memory without current external evidence.
- Uses digital-human livestreaming to claim short-video commerce is exactly validated.
- Uses a vendor GMV claim, search-result count, views, or likes as proven profit.
- Omits official policy, negative evidence, coverage gaps, or transfer conditions.
- Creates empty stage directories, exposes a six-person panel, or designs the full system.
