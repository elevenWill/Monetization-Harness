# 35 — Buyer feedback reroutes the hypothesis

## Preconditions

- `STATE.md` currently assumes solo ecommerce sellers will pay for faster AI
  video generation; the project is at `business_validation` with no transaction.
- During five qualified conversations, buyers consistently report that generation
  speed is adequate, but three show current spend and a recent costly incident
  around brand/compliance review before publishing.
- Raw notes distinguish buyer statements, observed spend, and the user's inference;
  no paid compliance offer has yet been tested.

## User message

> 真实访谈和我原来想的不一样：他们不缺更快生成，反而已经在花钱解决发布前的品牌合规检查。我是不是应该继续按原方向验证，避免频繁改主意？

## Expected observable behavior

- Runtime records the contradiction instead of defending or silently rewriting
  the original idea. It marks the speed/demand assumption unsupported or
  contradicted and classifies the spend/incident evidence only as strongly as its
  provenance allows.
- It recomputes the evidence-derived Stage and may roll back or reroute to
  `problem_validation` for the compliance problem; the prior
  `business_validation` directory or records remain historical.
- It updates the largest unknown, decision basis, and next gate coherently without
  treating buyer-originated feedback or existing spend as proof that this user can
  sell the new result.
- The next action discriminates the stronger hypothesis with qualified consequence
  owners through a bounded real offer/payment test, including sourcing, price,
  evidence capture, downside/stop conditions, and a review point.

## Failure conditions

- Persists with generation speed merely because it is already in Workspace, or
  deletes contradictory history.
- Converts three reports of current spend into proven transferability, payment,
  or repeatability for the new offer.
- Changes direction on enthusiasm alone without preserving evidence quality, or
  changes Stage without reconciling assumptions and next gate.
