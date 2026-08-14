# 23 — No project for ordinary monetization discussion

## Preconditions

- `workspace/` contains only `_index.md`; no project exists.
- Each message below is an independent ordinary knowledge question, not a
  concrete monetization direction the user wants to pursue over time.
- Capture the initial contents of `_index.md` so the no-write result can be
  inspected after each variant.

## User message

Run the scenario independently with each message:

### Variant A

> Naval 和 Taleb 在商业决策中最大的区别是什么？

### Variant B

> 现在常见的 SaaS 收费方式有哪些？

### Variant C

> 为什么 Deadline 会提高某些需求的商业价值？

## Expected observable behavior

- Runtime classifies each variant as `No Project` and answers the knowledge
  question normally; mentioning business, monetization, a named thinker, SaaS,
  or a Harness concept is not by itself a durable monetization thread.
- Project handling stops after that classification. Runtime does not bootstrap,
  resume, or invent a project merely to save the discussion.
- `workspace/_index.md` remains byte-for-byte unchanged, and `workspace/`
  contains no new project root, `IDEA.md`, `STATE.md`, or stage directory.
- The observable result reflects that Workspace is long-term project memory,
  not a transcript or general-purpose chat log.

## Failure conditions

- Creates `workspace/naval-taleb/`, `workspace/saas-pricing/`,
  `workspace/deadline-business/`, or any other project for a variant.
- Modifies `_index.md` or creates an `IDEA.md`, `STATE.md`, or stage artifact to
  record the ordinary discussion.
- Refuses to answer, demands a project slug, or forces the user through project
  setup because the question uses monetization vocabulary.
