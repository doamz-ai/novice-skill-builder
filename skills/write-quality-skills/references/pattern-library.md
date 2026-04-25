# Skill Pattern Library

These patterns are distilled from the local Baoyu Skills study sample.

## 1. Trigger Description Pattern

Use this shape:

`Capability. Use when the user asks for [task/context/phrases]. Supports [inputs/modes]. Output is [contract].`

A good description lets the runtime decide whether to load the skill before the body is visible.

## 2. Pure Instruction Skill

Use when the task is mainly reasoning, review, planning, writing, or taste. Keep all essential workflow in `SKILL.md`. Do not add scripts just to look complete.

## 3. Reference-Backed Skill

Use when the skill has long style systems, schemas, platform differences, examples, or domain rules. Keep `SKILL.md` as a router. Link every reference directly and say when to read it.

## 4. Script-Backed Skill

Use when repeated code would otherwise be rewritten: API calls, browser automation, image processing, document conversion, linting, validation, batch jobs, or fragile file formats.

The body should explain how to choose parameters and how to interpret failures. The script should own deterministic execution.

## 5. Asset-Backed Skill

Use when outputs need stable templates, starter projects, images, icons, fonts, or sample files. Assets are for use, not for loading into context by default.

## 6. Configuration Layer

Use project-level config before user-level config when the workflow has durable preferences. Good candidates: models, providers, accounts, visual themes, publish defaults, output locations.

Document:
- search order
- default behavior
- secret handling
- what happens on first run

## 7. Confirmation Points

Ask the user only at high-value forks:
- irreversible changes
- account publishing
- first-time credential setup
- title/style/layout selection
- risk consent
- ambiguous scope

## 8. Output Contract

State exact output format, naming, location, overwrite policy, and whether the artifact is self-contained. Strong contracts prevent low-quality improvisation.

## 9. Risk Boundary

For browser login, cookies, unofficial APIs, paid API usage, destructive writes, or public posting, put warnings near the execution step and stop before the irreversible action unless the user explicitly asked to continue.

## 10. Baoyu Pattern Limits

Baoyu-style skills are strongest for creator workflows, content transformation, information capture, platform posting, API-backed generation, and repeatable file operations.

They are weaker as a complete pattern for:
- one-off conversations
- large business applications
- long-running multi-user systems
- heavy compliance workflows
- workflows where state, permissions, and monitoring matter more than prompt procedure

For these cases, use a skill as the guide layer only, or recommend a local app, backend service, or multiple coordinated skills.
