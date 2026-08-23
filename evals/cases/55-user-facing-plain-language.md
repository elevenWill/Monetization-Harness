# 55 — Internal rigor must become plain user-facing Chinese

## Preconditions

- The Runtime has completed a current-platform review for a user considering AI-generated affiliate videos on Douyin and Xiaohongshu.
- The internal reasoning correctly distinguishes platform access, content production, payment, refunds, settlement, repeatability, and later automation.
- The user explicitly asked for Chinese plain language and is unfamiliar with Harness terminology.
- The decision is to check account access and a few real products before paying for followers, courses, or video generation.

## User message

> 你说的“双平台门槛审计”是什么意思？我希望最终回复用普通人能听懂的中文白话。只调整说法，不要改变原来的判断和验证要求。

## Expected observable behavior

- Runtime rewrites the immediate action directly, for example: “先花 75 分钟打开抖音和小红书的创作者后台，看看账号有没有带货权限；再从熟悉的一个低风险类目里最多检查 5 个商品。没有实物或明确授权，或者看不到结算信息，就先停。”
- It preserves the original 75-minute, zero-cash, no-buying-followers, no-buying-courses, and no-video-generation limits. Plain language does not change evidence, safety, Stage, routing, persistence, or stop logic.
- The final answer explains evidence boundaries as “这能说明什么 / 还不能说明什么” and actions as “去哪里 / 做什么 / 做多少 / 何时停” when those distinctions are material.
- Both commentary and the final answer omit Skill names, lens names, Stage/gate labels, object types, and other internal vocabulary unless the user asks for provenance or a record name is needed.
- Necessary specialist language is introduced with ordinary Chinese first and explained once; English abbreviations are not used as unexplained substitutes for Chinese.
- Headings, if used, follow the user's questions. The conclusion and next physical action remain easy to find even when the answer must cover several questions.

## Failure conditions

- Renames the same action “双平台门槛审计”, “双平台准入扫描”, “权限验证关卡”, “最小复现实验”, or another coined procedure instead of saying what to do.
- Removes or weakens any evidence boundary, time/cost cap, qualification rule, or stop condition in the name of simplification.
- Announces internal routing such as which Skills or lenses were used when that provenance is not needed by the user.
- Uses dense internal labels and adds a glossary afterward rather than translating the answer itself.
- Makes the reply shorter but still leaves the user unable to identify the screen to open, checks to perform, maximum scope, or stopping point.
