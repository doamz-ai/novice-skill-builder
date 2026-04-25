# Novice Skill Builder

## Quick Start / 30 秒上手

This is a Codex Skill package. It is not a normal desktop app or a website; install `skills/write-quality-skills` into your Codex skills directory, then call `$write-quality-skills` in Codex.

这是一个需要安装到 Codex skills 目录的 Skill 包，不是普通软件，也不是网页应用。安装 `skills/write-quality-skills` 后，在 Codex 里用 `$write-quality-skills` 调用。

**For non-technical users, copy this to Codex:**

```text
Please install this Codex Skill:
https://github.com/doamz-ai/novice-skill-builder/tree/main/skills/write-quality-skills

I am a non-technical user. Please download it, install it into my Codex skills directory, then teach me how to use $write-quality-skills. After installation, run the first example in examples/README.md with me.
```

**给 IT 小白朋友：复制下面这段发给 Codex：**

```text
请帮我安装这个 Codex Skill：
https://github.com/doamz-ai/novice-skill-builder/tree/main/skills/write-quality-skills

我是 IT 小白。请下载安装到我的 Codex skills 目录，然后教我如何使用 $write-quality-skills。安装完成后，请用 examples/README.md 里的第一个示例带我跑一遍。
```

## How to Use / 如何使用

After installation, use this pattern in Codex:

```text
Use $write-quality-skills to turn this workflow into a high-quality Codex skill:
[describe your repeated workflow here]
```

安装后，在 Codex 里这样说：

```text
使用 $write-quality-skills，把下面这个重复工作流程变成高质量 Codex Skill：
[在这里描述你的重复工作]
```

## Manual Install / 手动安装

Use this only if you have already downloaded or cloned this repository. If you do not understand the command, use the copy-paste prompt above.

如果你已经下载了这个仓库，可以用下面的命令手动安装；如果看不懂命令，直接用上面的复制提示词即可。

```powershell
Copy-Item -Recurse .\skills\write-quality-skills "$env:USERPROFILE\.codex\skills\write-quality-skills"
```

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
