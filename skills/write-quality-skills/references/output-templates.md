# Output Templates

Use these sections when responding to a novice user.

## Demand Understanding Card

- What you want to repeat:
- What you provide each time:
- What AI should produce:
- Rules that must stay stable:
- Human confirmation points:
- Main risk:

## Pattern Match Card

- Suitability:
- Primary task type:
- Execution mechanism:
- Risk level:
- Recommended structure:
- Why this pattern:

## Skill Draft Skeleton

```markdown
---
name: skill-name-here
description: [Capability]. Use when the user asks to [trigger contexts and common phrases]. Supports [inputs or modes]. Output is [contract].
---

# Skill Title

Use this skill to [plain-language job].

## Workflow

1. [First step]
2. [Decision point]
3. [Execution step]
4. [Validation step]

## Resources

- Read `references/example.md` when [condition].
- Run `scripts/example.py` when [condition].

## Safety

- Ask before [risky action].
- Never [forbidden action].

## Output

- Produce [artifact].
- Save to [location or naming rule].
```

## Resource Plan

- `SKILL.md`: core flow and constraints.
- `references/`: only if long examples, style rules, schemas, or rubrics are needed.
- `scripts/`: only if deterministic execution is needed.
- `assets/`: only if reusable templates or source materials are needed.
- Configuration: only if user preferences, credentials, or environment settings matter.

## Test Prompts

Provide exactly three:

1. Happy path request.
2. Ambiguous request that should trigger clarification.
3. Risky or unsuitable request that should trigger a boundary.

## Final Notes

- Assumptions:
- Risks:
- Next improvement:
