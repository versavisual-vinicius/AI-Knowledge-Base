#!/usr/bin/env python3
"""Valida a estrutura multiplataforma sem depender de CLIs externos."""

from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "codex": ".codex-plugin/plugin.json",
    "claude": ".claude-plugin/plugin.json",
    "antigravity": "plugin.json",
    "gemini-cli": "gemini-extension.json",
    "opencode": ".opencode/plugins/ai-knowledge-base.js",
    "kimi": ".kimi-plugin/plugin.json",
    "pi": ".pi/extensions/ai-knowledge-base.ts",
}
ADAPTER_FIELDS = (
    "Versão mínima conhecida:",
    "Bootstrap:",
    "Fonte:",
    "Instalação local:",
    "Validação:",
    "Limitação atual:",
    "Estado:",
)
MARKDOWN_LINK = __import__("re").compile(r"!??\[[^\]]*\]\(([^)]+)\)")


def load_json(relative: str, errors: list[str]) -> None:
    path = ROOT / relative
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing JSON: {relative}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON {relative}: {exc.msg}")


def validate_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        for raw_target in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            target = raw_target.strip().split("#", 1)[0].strip().strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not target_path.exists():
                errors.append(f"broken Markdown link: {path.relative_to(ROOT)} -> {target}")


def validate_executable_hook(errors: list[str]) -> None:
    hook = ROOT / "hooks/session-start"
    if not hook.is_file():
        errors.append("missing executable hook: hooks/session-start")
        return
    if not os.access(hook, os.X_OK):
        errors.append("hook is not executable: hooks/session-start")
        return
    try:
        result = subprocess.run([str(hook)], capture_output=True, text=True, check=True)
        payload = json.loads(result.stdout)
        if not isinstance(payload, dict) or not any(key in payload for key in ("additionalContext", "additional_context", "hookSpecificOutput")):
            errors.append("hook output does not contain a supported context field")
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        errors.append(f"invalid executable hook: {exc}")


def validate_node_plugin(errors: list[str]) -> None:
    plugin = ROOT / ".opencode/plugins/ai-knowledge-base.js"
    node = shutil.which("node")
    if not node:
        errors.append("node is required to validate .opencode/plugins/ai-knowledge-base.js")
        return
    result = subprocess.run([node, "--check", str(plugin)], capture_output=True, text=True)
    if result.returncode:
        errors.append(f"invalid OpenCode plugin: {result.stderr.strip()}")


def main() -> int:
    errors: list[str] = []

    for harness, relative in REQUIRED_FILES.items():
        if not (ROOT / relative).is_file():
            errors.append(f"missing {harness} entrypoint: {relative}")

    for relative in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json", ".kimi-plugin/plugin.json", "plugin.json", "gemini-extension.json", "package.json", "hooks.json", "hooks/hooks.json"):
        load_json(relative, errors)

    for harness in REQUIRED_FILES:
        adapter = ROOT / "adapters" / harness / "README.md"
        if not adapter.is_file():
            errors.append(f"missing adapter documentation: adapters/{harness}/README.md")
            continue
        content = adapter.read_text(encoding="utf-8")
        for field in ADAPTER_FIELDS:
            if field not in content:
                errors.append(f"missing `{field}` in adapters/{harness}/README.md")
        if "[TODO:" in content:
            errors.append(f"placeholder in adapters/{harness}/README.md")

    for path in ROOT.glob("skills/*/SKILL.md"):
        if "[TODO:" in path.read_text(encoding="utf-8"):
            errors.append(f"placeholder in {path.relative_to(ROOT)}")

    bootstrap = (ROOT / "BOOTSTRAP.md").read_text(encoding="utf-8")
    for skill in ("contexto-e-decisoes", "diagnostico-de-repositorio", "execucao-orientada-a-spec", "inventario-de-ferramentas", "verificacao-com-evidencias", "revisao-de-etapa"):
        if skill not in bootstrap:
            errors.append(f"bootstrap does not map skill: {skill}")

    validate_markdown_links(errors)
    validate_executable_hook(errors)
    validate_node_plugin(errors)

    if errors:
        print("Adapter validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Adapter validation passed: {len(REQUIRED_FILES)} harnesses")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
