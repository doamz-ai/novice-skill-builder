#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")


def parse_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, ["SKILL.md must start with YAML frontmatter delimiter ---"]
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text, ["SKILL.md frontmatter is not closed with ---"]
    data = {}
    warnings = []
    for line in lines[1:end]:
        if not line.strip():
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            warnings.append(f"Unparsed frontmatter line: {line}")
            continue
        data[match.group(1)] = match.group(2).strip().strip('"').strip("'")
    return data, "\n".join(lines[end + 1:]), warnings


def audit(path: Path):
    errors = []
    warnings = []
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return {"path": str(path), "errors": ["Missing SKILL.md"], "warnings": []}

    text = skill_md.read_text(encoding="utf-8", errors="replace")
    frontmatter, body, parse_warnings = parse_frontmatter(text)
    warnings.extend(parse_warnings)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    extra_keys = sorted(k for k in frontmatter if k not in {"name", "description"})

    if not name:
        errors.append("Missing frontmatter name")
    elif not NAME_RE.match(name):
        errors.append("name must use lowercase letters, digits, and hyphens only")
    elif path.name != name:
        warnings.append(f"Folder name '{path.name}' does not match frontmatter name '{name}'")

    if not description:
        errors.append("Missing frontmatter description")
    elif len(description) < 120:
        warnings.append("description is probably too short to trigger reliably")
    else:
        trigger_terms = ["use when", "when", "asks", "wants", "trigger"]
        if not any(term in description.lower() for term in trigger_terms):
            warnings.append("description should include trigger contexts such as 'Use when ...'")

    if extra_keys:
        warnings.append("Codex skills should keep frontmatter to name and description only: " + ", ".join(extra_keys))

    if len(body.strip()) < 300:
        warnings.append("Body is very short; confirm it contains enough procedural guidance")
    if len(body.splitlines()) > 500:
        warnings.append("Body exceeds 500 lines; move detail into references/")

    for match in re.findall(r"`([^`]+/(?:[^`]+)\.md)`", body):
        ref = path / match
        if not ref.exists():
            warnings.append(f"Referenced markdown file does not exist: {match}")

    for folder in ["scripts", "references", "assets"]:
        root = path / folder
        if root.exists():
            files = [p for p in root.rglob("*") if p.is_file()]
            if not files:
                warnings.append(f"{folder}/ exists but is empty")

    return {
        "path": str(path),
        "name": name,
        "description_length": len(description),
        "body_lines": len(body.splitlines()),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a Codex skill folder.")
    parser.add_argument("skill_folder", type=Path)
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    args = parser.parse_args()

    result = audit(args.skill_folder)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Skill audit: {result['path']}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARN: {warning}")
        if not result["errors"] and not result["warnings"]:
            print("OK: no issues found")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
