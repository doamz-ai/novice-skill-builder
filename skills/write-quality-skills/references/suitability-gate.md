# Suitability Gate

Use this gate before drafting a skill.

## Good Skill Fit

A request is suitable for a skill when most of these are true:

- The task repeats.
- The input and output can be described.
- The user has a preferred method, style, or quality standard.
- Another agent would benefit from procedural memory.
- The result can be validated with examples or checks.

## Poor Skill Fit

Do not force a single skill when the request is:

- a one-off question or casual conversation
- a full product requiring UI, database, auth, state, or background jobs
- a vague life goal with no repeatable workflow
- a task where requirements change every time
- a high-risk automation without a clear human confirmation point
- a domain that requires licensed professional judgment without user-provided rules

## Better Containers

- Use a normal prompt for one-off thinking.
- Use a checklist for a human process.
- Use a script for a narrow deterministic operation.
- Use a local app for UI, state, history, uploads, or daily use.
- Use multiple skills when one workflow has distinct roles such as research, drafting, review, and publishing.

## Decision Output

Always state:

- Fit: good skill fit, partial skill fit, or not a single-skill fit.
- Reason: one sentence in plain language.
- Container: skill, prompt, checklist, script, local app, or multiple skills.
