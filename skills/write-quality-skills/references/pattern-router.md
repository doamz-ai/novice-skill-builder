# MECE Pattern Router

Classify the request on three axes: primary task type, execution mechanism, and risk level. This avoids mixing categories.

## Axis 1: Primary Task Type

Choose exactly one primary type:

1. Knowledge guidance: fixed reasoning, review, teaching, diagnosis, or decision support.
2. Content generation: articles, images, comics, covers, slides, diagrams, scripts, prompts.
3. Format transformation: markdown, HTML, translation, compression, layout, data reshaping.
4. Information capture: webpages, videos, social posts, notes, research material.
5. Publishing automation: WeChat, Weibo, X, CMS, newsletters, platform drafts.
6. API tool: model calls, databases, third-party services, internal tools.
7. Quality control: audit, acceptance, checklist, regression review, rubric-based improvement.
8. Project or business workflow: multi-step, multi-role, long-lived state, operational system.

## Axis 2: Execution Mechanism

- Pure instructions: use only `SKILL.md`.
- Knowledge references: add `references/`.
- Deterministic execution: add `scripts/`.
- Reusable source material: add `assets/`.
- Durable preferences: add configuration guidance or `.env.example`.
- Large workflow: split into multiple skills or recommend a local app.

## Axis 3: Risk Level

- Low: draft, summarize, classify, generate local files.
- Medium: read external URLs, call paid APIs, transform user files, batch operations.
- High: public posting, account login, cookies, unofficial APIs, deleting or overwriting files, sending messages.

## Routing Rules

- Knowledge guidance -> `SKILL.md` plus optional rubric reference.
- Content generation -> `SKILL.md + references/` for styles, examples, and output contract.
- Format transformation -> use `scripts/` if exact file handling matters.
- Information capture -> use `scripts/` for fetching and add risk/quality gates.
- Publishing automation -> require confirmation before final publish.
- API tool -> require config, secret handling, error behavior, and deterministic scripts.
- Quality control -> use review rubric plus optional audit script.
- Project or business workflow -> recommend a local app or multiple skills unless the user only wants a guide layer.
