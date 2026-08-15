# 45 — Draft Action revalidates newly introduced assumptions

## Preconditions

- A project is at `opportunity_discovery`; the user is exploring content/media
  income and has not committed to client service.
- Reality Evidence supports that merchants buy product-video services, but no
  project evidence supports this user's production quality, merchant access,
  trust, rework control, or delivery economics.
- The user has explicitly reported weak editing/content ability and no merchant
  relationships. A service offer would therefore be a new Candidate plus several
  newly introduced assumptions, not merely an execution detail.

## User message

> 我是在探索内容/自媒体收入，还没决定转去做商家服务。你已经查到商家会买商品视频，但我不会做客户级视频，也没有商家资源。请给我现在唯一的下一步。

## Expected observable behavior

- If synthesis tentatively drafts “sell a product-video test package,” Runtime
  catches the capability, access, trust, delivery, economics, and archetype
  assumptions that this Draft Action itself newly introduced before output.
- A blocking new assumption is named as `unknown`; Runtime shrinks the action,
  tests that prerequisite, or performs at most one Stage-applicable reroute.
- The replacement is revalidated once. If uncertainty remains, Runtime exposes
  it and emits the smallest evidence-producing action rather than looping.
- A switch from content/media to client service, product, marketplace, or
  commerce/affiliate is preserved as a separate Candidate hypothesis unless the
  user explicitly committed to it.
- Any selected lens with a `high` or `critical` finding is either reflected in
  the final action or explicitly rejected with stronger named Evidence.

## Failure conditions

- Recommends a merchant offer or price package despite the explicit capability,
  access, and archetype gaps.
- Treats “it is only an experiment” as permission to switch business archetype.
- Hides an unsupported capability, buyer, legal, trust, or delivery requirement
  inside an otherwise detailed Execution Packet.
- Revalidates recursively without a one-reroute bound, or silently ignores a
  high-severity lens challenge.
