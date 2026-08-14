# 24 — Resume an existing project through semantic identity

## Preconditions

- `workspace/_index.md` and the actual project root
  `workspace/ai-commerce-short-video/` already exist.
- `IDEA.md` records: “研究利用 AI / 数字人生产 10～15 秒商品短视频的变现机会。”
- `STATE.md` has `stage: opportunity_discovery`, an active assumption that
  merchants may need batch production of product videos, and the largest
  unknown: which concrete Buying Situation produces real payment.
- No other project is a plausible semantic match for this message.

## User message

> 我今天又看了一批商品视频。
>
> 发现商家真正头疼的可能不是单条视频生成，
> 而是在活动前一次要做几十个 SKU，
> 人工根本来不及。

## Expected observable behavior

- Runtime inspects `_index.md`, enumerates actual project roots, reads the
  candidate `IDEA.md` and `STATE.md` completely, and identifies a single clear
  semantic match with `ai-commerce-short-video`.
- It resumes that stable project instead of treating changed wording such as
  “几十个 SKU” or “活动前” as a new project identity. Matching considers the
  goal, problem, customer, transaction context, conversation, and current state,
  not exact keyword equality.
- Runtime distinguishes what the user actually observed from the inference that
  this is the merchants' real pain. It may classify durable new material as an
  observation, an ASSUMPTION, or a candidate Buying Situation without promoting
  an unverified inference to FACT.
- If the message materially changes durable state, Runtime updates only the
  existing project and reconciles `STATE.md` and `_index.md` under their normal
  mutation rules. If a real `BS001` is formed, it is persisted under the owning
  canonical stage, for example
  `03-business-validation/buying-situations/BS001-*.md`, with unknown links kept
  explicit and no empty directories created.
- If the information is not yet durable enough to write, Runtime may analyze it
  without mutation; either path preserves the existing project identity and
  continues the conversation in the same turn.

## Failure conditions

- Creates `workspace/sku-video/`, `workspace/batch-video/`,
  `workspace/commerce-video-2/`, `workspace/ai-video-new/`, or any duplicate
  project because the user's wording changed.
- Chooses a project from `_index.md` without inspecting the actual project root
  and its complete `IDEA.md` and `STATE.md`.
- Records the inferred merchant pain, deadline consequence, payer, budget, or
  willingness to pay as FACT without evidence.
- Creates a project-root Buying Situation file, an empty stage directory, or
  unrelated workspace material while resuming the existing project.
