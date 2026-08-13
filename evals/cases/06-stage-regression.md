# 06 — Productization stage regression

## Preconditions

- `STATE.md` says `productization` and historical productization material exists.
- The product has launched, but customers are not purchasing or using it again.

## User message

> 产品上线了，但没有人重复购买。下一版应该加什么功能？

## Expected observable behavior

- Runtime treats missing recurrence as evidence against the repeat-value
  assumption and moves the authoritative `STATE.md` stage back to
  `business_validation`.
- `business-filter` plus `experiment-designer` investigates why the purchased
  result did not recur instead of supplying a feature roadmap.
- The regression, invalidated assumption, new largest unknown, and next gate are
  persisted; old `07-productization/` material remains as history.
- Directory presence does not override `STATE.md`, and no empty directory is added.

## Failure conditions

- Treats stages as one-way or infers stage from existing directories.
- Recommends features before resolving repeat value.
- Deletes or rewrites historical productization evidence.
