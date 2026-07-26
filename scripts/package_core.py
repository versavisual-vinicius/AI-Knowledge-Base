#!/usr/bin/env python3
"""Cria um pacote ZIP determinístico do núcleo reutilizável."""

from __future__ import annotations

import argparse
from pathlib import Path
import stat
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DIRECTORIES = (
    ".claude-plugin",
    ".codex-plugin",
    ".kimi-plugin",
    ".opencode",
    ".pi",
    "adapters",
    "agents",
    "docs",
    "evals",
    "hooks",
    "references",
    "scripts",
    "skills",
    "tests",
)
ROOT_FILES = (
    "BOOTSTRAP.md",
    "CLAUDE.md",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "GEMINI.md",
    "LICENSE",
    "README.md",
    "RELEASE-NOTES.md",
    "SECURITY.md",
    "SPEC.md",
    "SPEC_PUBLIC_EXPANSION.md",
    "THIRD_PARTY_NOTICES.md",
    "gemini-extension.json",
    "hooks.json",
    "package.json",
    "plugin.json",
)
EXCLUDED_PARTS = {".git", "__pycache__", "node_modules", "dist"}


def files_to_package() -> list[Path]:
    paths: set[Path] = set()
    for relative in ROOT_FILES:
        path = ROOT / relative
        if path.is_file():
            paths.add(path)
    for directory in DIRECTORIES:
        base = ROOT / directory
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if path.is_file() and not EXCLUDED_PARTS.intersection(path.parts):
                paths.add(path)
    return sorted(paths, key=lambda path: path.relative_to(ROOT).as_posix())


def write_archive(output: Path) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    files = files_to_package()
    if not files:
        raise SystemExit("no package files found")
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            data = path.read_bytes()
            info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IMODE(path.stat().st_mode) << 16) | 0o100000
            archive.writestr(info, data)
    print(f"Package created: {output} ({len(files)} files)")
    return len(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "dist/ai-knowledge-base-core.zip",
        help="caminho do ZIP de saída",
    )
    args = parser.parse_args()
    write_archive(args.output.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
