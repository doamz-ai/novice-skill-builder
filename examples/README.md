# Example Prompts

Use these prompts after installing `write-quality-skills`.

## 1. WeChat Article Workflow

```text
Use $write-quality-skills to turn this workflow into a high-quality Codex skill:

I want AI to help me turn each long article into a WeChat-style draft. Every time, I will provide a Markdown article or pasted text. I want title ideas, section headings, pull quotes, formatting suggestions, a summary, and cover-image prompt ideas. I do not want AI to publish anything automatically.
```

## 2. YouTube Notes Workflow

```text
Use $write-quality-skills to turn this workflow into a high-quality Codex skill:

I want AI to help me organize YouTube video notes. I will provide a video URL or transcript. I want a Chinese summary, key ideas, timestamps if available, action items, vocabulary notes, and a short social-media post draft.
```

## 3. API Tool Workflow

```text
Use $write-quality-skills to turn this workflow into a high-quality Codex skill:

I have an API tool that takes a keyword and returns product research data. I want AI to help me design a repeatable skill so that each run collects the data, checks missing fields, summarizes opportunities, and outputs a Markdown report. API keys must not be hard-coded.
```

## 4. Existing Skill Review

```text
Use $write-quality-skills to review this skill:

[Paste or attach the skill folder.]

Please tell me whether it is suitable for novice users, whether the trigger description is clear, whether references/scripts/assets are justified, and what I should improve first.
```

## 5. Not A Single-Skill Fit

```text
Use $write-quality-skills to evaluate this idea:

I want AI to build a complete customer management system for my team, with user login, customer records, follow-up reminders, dashboards, permissions, and long-term history.
```

Expected behavior: the skill should explain that this is not a good single-skill fit and recommend a local app or multiple coordinated skills.
