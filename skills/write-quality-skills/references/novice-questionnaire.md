# Novice Questionnaire

Use plain language. Do not ask the user to choose between `SKILL.md`, `scripts`, `references`, or `assets`.

## Ask These First

1. What do you want AI to help you do repeatedly?
2. What will you give AI each time: text, files, links, screenshots, keywords, data, or account access?
3. What should AI hand back: a document, images, code, a checklist, a draft, a published post, or a decision?
4. What rules must stay consistent every time: tone, structure, style, brand, data format, naming, quality bar, or review standard?
5. What actions should AI never do without asking: posting publicly, spending money, deleting files, overwriting files, using credentials, or contacting external services?

## Ask Only If Needed

- If output quality depends on taste, ask for 2-3 examples the user likes.
- If the task touches an account or API, ask where secrets should live and whether the final action needs confirmation.
- If the task has many steps, ask which steps are fixed and which steps require judgment.
- If the task has high failure cost, ask what a bad result would look like.

## Conservative Defaults

- Output Chinese explanations for Chinese-speaking users.
- Prefer a skill draft over a full local app unless the request needs state, UI, database, or repeated background jobs.
- Prefer references over scripts until deterministic execution is clearly needed.
- Stop before public posting, paid calls at scale, deletion, or overwrites unless explicitly confirmed.
