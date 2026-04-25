# Skill Review Rubric

Use this checklist to review a Codex skill.

## Frontmatter

- `name` is lowercase hyphen-case and matches the folder.
- `description` includes capability, trigger contexts, user phrases, and output contract.
- Frontmatter contains only `name` and `description`.

## Body

- The first screen explains what to do, not why skills are useful.
- Instructions are imperative and task-specific.
- The workflow has a clear start, decision points, execution steps, and validation.
- The skill tells the agent when to ask the user and when to proceed.
- Safety boundaries are explicit for secrets, external systems, account actions, and overwrites.

## Progressive Disclosure

- `SKILL.md` is lean enough to load often.
- Long examples, schemas, provider notes, and style systems live in `references/`.
- Every reference is linked from `SKILL.md` with a clear read condition.
- There are no deep reference chains required to discover important files.

## Resources

- Scripts exist only when deterministic execution or repeated fragile code justifies them.
- Scripts have a clear CLI, no hard-coded secrets, and useful errors.
- Assets are templates or source materials used in outputs.
- Placeholder files from scaffolding are removed.

## Validation

- Run `scripts/audit_skill.py <skill-folder>`.
- Run the platform validator when available.
- Test at least three realistic prompts: happy path, ambiguous request, and edge/risk case.

## Common Fixes

- Move generic explanations out.
- Strengthen the frontmatter description.
- Replace long inline examples with reference files.
- Add a script for repeated brittle operations.
- Add explicit output and overwrite rules.
