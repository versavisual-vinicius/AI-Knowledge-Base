#!/usr/bin/env python3
"""Valida a estrutura mínima do plugin e detecta placeholders."""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / ".codex-plugin/plugin.json",
    ROOT / "BOOTSTRAP.md",
    ROOT / "agents/openai.yaml",
    ROOT / "references/project-spec-template.md",
    ROOT / "references/schemas/spec.schema.json",
]


def main() -> int:
    errors = [f"missing: {path.relative_to(ROOT)}" for path in REQUIRED if not path.is_file()]
    manifest_path = ROOT / ".codex-plugin/plugin.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text())
            if manifest.get("name") != "ai-knowledge-base":
                errors.append("manifest name must be ai-knowledge-base")
            if manifest.get("skills") != "./skills/":
                errors.append("manifest skills path must be ./skills/")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid manifest JSON: {exc}")

    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skills) < 5:
        errors.append("expected at least five skills")
    for skill in skills:
        text = skill.read_text()
        if "[TODO:" in text:
            errors.append(f"placeholder found: {skill.relative_to(ROOT)}")
        if not (skill.parent / "agents/openai.yaml").is_file():
            errors.append(f"missing metadata: {skill.parent.relative_to(ROOT)}/agents/openai.yaml")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"OK knowledge base plugin: {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
