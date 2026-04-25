# Novice Skill Builder

Novice Skill Builder helps business experts and non-technical users turn repeatable AI workflows into high-quality Codex skills.

It is a novice-facing demand triage skill: it first decides whether a request is suitable for a skill, then translates plain-language needs into task type, inputs, outputs, execution mechanism, risk boundary, and a draft skill structure.

## Who It Is For

- Business operators who know their workflow but do not know how to write skills.
- Consultants, creators, researchers, and founders who repeat similar AI tasks.
- AI power users who want a safer way to turn prompts into reusable skill frameworks.

## What It Produces

For a suitable workflow, the skill outputs:

- Demand understanding card
- Pattern match card
- `SKILL.md` draft
- Suggested `references/`, `scripts/`, `assets/`, and configuration
- Three test prompts
- Risks, assumptions, and next improvement steps

If the request is not a good single-skill fit, it recommends a better container such as a normal prompt, checklist, script, local app, or multiple coordinated skills.

## Install

Copy the skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse .\skills\write-quality-skills "$env:USERPROFILE\.codex\skills\write-quality-skills"
```

Then use it in Codex:

```text
Use $write-quality-skills to turn this workflow into a high-quality Codex skill:

I want AI to help me turn each long article into a WeChat-style draft with title ideas, section headings, pull quotes, formatting suggestions, and cover-image prompt ideas.
```

## Example Requests

See [examples/README.md](examples/README.md) for copy-ready prompts.

## Project Structure

```text
skills/write-quality-skills/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/audit_skill.py
examples/
README.md
NOTICE.md
LICENSE
```

## Attribution

This project was inspired by [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills), a high-quality public skill collection by Baoyu.

This repository is not an official baoyu-skills project, mirror, fork, or redistribution. It does not include baoyu-skills source code, screenshots, full skill texts, or publishing scripts. It only provides an independently written novice-guided skill design workflow inspired by publicly visible skill design patterns.

See [NOTICE.md](NOTICE.md) for details.

## License

MIT. See [LICENSE](LICENSE).

## Disclaimer

This project provides workflow and skill-design guidance. It is not legal, security, or professional advice. Review any generated skill before using it with accounts, secrets, paid APIs, public posting, destructive file operations, or regulated business processes.
