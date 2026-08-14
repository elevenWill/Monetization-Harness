# 25 — Project conflict prevents a wrong write

## Preconditions

- `workspace/ai-commerce-short-video/` is a real project whose goal is to study
  monetization of AI or digital-human product short-video services.
- `workspace/ai-ad-creative/` is a real project whose goal is to study
  monetization of AI batch advertising-creative production.
- Both roots contain `IDEA.md` and `STATE.md` and both are plausible semantic
  matches for the ambiguous word “素材.”
- Capture `_index.md` and both project trees and file contents before the first
  message so the no-write boundary is observable.

## User message

> 我今天发现几个商家都在活动前大量补素材。
>
> 他们说现在最麻烦的就是短时间内做出足够多的新素材。
>
> 这个 deadline 场景感觉挺值得研究。

## Expected observable behavior

- Runtime inspects the registry and actual candidates, reads both projects'
  `IDEA.md` and `STATE.md`, and classifies the message as `Project Conflict`
  because either project could own the durable evidence.
- Before ownership is resolved, Runtime writes to neither project: it creates no
  FACT, ASSUMPTION, `BSxxx`, RESEARCH, CASE, or stage artifact; it does not
  modify either `STATE.md`, change either stage, or mutate `_index.md`.
- Runtime may provide provisional, non-persisted analysis, such as noting that
  the signal could be a repeated deadline Buying Situation, while keeping the
  project attribution and unsupported trigger links unresolved.
- If persistence is needed, Runtime asks one minimal ownership question, for
  example: “你这里说的‘素材’，主要指商品带货短视频，还是广告投放 Creative？”
- On the follow-up “主要是商品带货短视频。”, Runtime resumes
  `ai-commerce-short-video` and only then may apply normal durable-mutation
  rules there. On “主要是广告投放素材。”, it instead resumes
  `ai-ad-creative` and only then may write there.
- The behavior prioritizes avoiding incorrect persistence over automatic
  convenience; temporary no-write is safer than contaminating long-term memory.

## Failure conditions

- Randomly chooses one candidate, writes to both candidates, or writes any
  durable record before project ownership is resolved.
- Creates a third project such as `workspace/deadline-material/` to escape the
  conflict.
- Treats deadline language as sufficient proof of a trigger, consequence,
  payer, budget, or willingness to pay.
- Asks many unrelated questions when one minimal ownership clarification is
  sufficient, or fails to resume the confirmed existing project after the
  follow-up.
