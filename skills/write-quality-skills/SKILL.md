---
name: write-quality-skills
description: Guide non-expert users from a plain-language workflow need to a high-quality Codex skill draft. Use when the user wants to turn a vague repeatable AI task into a skill, decide whether a task is suitable for a skill, classify the need with MECE skill patterns, generate a novice-friendly demand brief, choose SKILL.md/scripts/references/assets/configuration/safety boundaries, or review and improve an existing skill framework.
---

# Write Quality Skills

Use this skill as a novice-facing demand triage system for creating high-quality Codex skills.

## Core Rule

Do not make the user learn skill terminology first. Translate their plain-language need into task type, inputs, outputs, execution mechanism, risk boundary, and file structure.

## Workflow

1. Run the suitability gate.
   - Read `references/suitability-gate.md`.
   - Decide whether the request should become a skill, a normal prompt, a checklist, a script, a local app, or multiple coordinated skills.
   - If the task is not suitable for a single skill, explain the better container and stop before drafting a misleading skill.

2. Collect novice-friendly requirements.
   - Read `references/novice-questionnaire.md`.
   - Ask at most 3-5 high-impact questions when the answer changes the skill design.
   - If the user cannot answer, proceed with conservative defaults and mark them as assumptions.

3. Route the request to a MECE pattern.
   - Read `references/pattern-router.md`.
   - Classify the primary task type, execution mechanism, and risk level separately.
   - Use Baoyu-style patterns as examples, not as the whole solution space.

4. Produce the novice-facing output.
   - Read `references/output-templates.md`.
   - Output a demand understanding card, pattern match card, skill draft, resource plan, three test prompts, and risk/next-step notes.
   - Use Chinese explanations by default unless the user asks otherwise.

5. Add validation.
   - Run the bundled `scripts/audit_skill.py <skill-folder>` for structural checks.
   - Run the platform validator if available.
   - Test at least one normal request, one ambiguous request, and one unsuitable-or-risky request.

## Pattern References

- Read `references/suitability-gate.md` before drafting.
- Read `references/novice-questionnaire.md` before asking the user questions.
- Read `references/pattern-router.md` before choosing resources.
- Read `references/output-templates.md` before presenting the result.
- Read `references/review-rubric.md` when reviewing or tightening an existing skill.

## Output Shape

When creating a new skill for a novice user, always include:

- Demand understanding card.
- Pattern match card.
- `SKILL.md` draft with valid frontmatter.
- Recommended `references/`, `scripts/`, `assets/`, and configuration, only when justified.
- Three realistic test prompts.
- Risks, assumptions, and the next improvement step.
