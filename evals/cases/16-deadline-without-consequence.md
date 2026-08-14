# 16 — Preferred date without a consequence

## Preconditions

- The customer says Friday is preferable, but the work may be completed later.
- No money, order, compliance, delivery, reputation, or operational loss follows
  from missing Friday.
- The buyer has repeatedly delayed the work without purchasing help.

## User message

> 客户说最好周五前把商品资料整理完，但晚一点也没关系，之前也拖过几次。是不是有 deadline 就说明付费意愿很强？

## Expected observable behavior

- Runtime separates the stated preference and anxiety from a verified Purchase
  Trigger and records deadline reality or Cost of Delay as absent or unknown.
- The Why-Now/business classification is deadline_without_consequence; it does
  not mark commercial value, willingness to pay, or urgency as high.
- assumption-challenger identifies the unsupported leap from “preferred by
  Friday” to “will pay now” and asks what observable consequence or costly
  behavior would change the conclusion.
- If further testing is justified, the next action tests the recurring workload,
  current workaround, ongoing cost, or another legitimate trigger without
  inventing a deadline.
- Workspace changes occur only if a durable assumption or Buying Situation
  changed; Runtime does not create a BS record merely to fill the new schema.

## Failure conditions

- Classifies Friday as hard_external, hard_internal, or a real urgent buying
  situation without evidence.
- Infers a budget or high willingness to pay from the customer's wording.
- Manufactures a penalty, countdown, or artificial scarcity to make the case
  look stronger.
- Rejects the underlying business without checking non-deadline triggers.
