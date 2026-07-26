#!/usr/bin/env python3
"""Testes determinísticos dos contratos públicos do repositório."""

from __future__ import annotations

import json
import os
import stat
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

from scripts import package_core
from scripts import validate_adapters
from scripts import validate_knowledge_base


ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_repository_contracts_pass(self) -> None:
        self.assertEqual(validate_knowledge_base.main(), 0)
        self.assertEqual(validate_adapters.main(), 0)

    def test_invalid_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".codex-plugin").mkdir()
            (root / ".codex-plugin/plugin.json").write_text("{invalid", encoding="utf-8")
            with patch.object(validate_knowledge_base, "ROOT", root):
                self.assertEqual(validate_knowledge_base.main(), 1)

    def test_broken_markdown_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[quebrado](missing.md)\n", encoding="utf-8")
            errors: list[str] = []
            with patch.object(validate_adapters, "ROOT", root):
                validate_adapters.validate_markdown_links(errors)
            self.assertTrue(any("broken Markdown link" in error for error in errors))

    def test_hook_without_json_context_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            hook = root / "hooks/session-start"
            hook.parent.mkdir()
            hook.write_text("#!/bin/sh\nprintf 'not-json\\n'\n", encoding="utf-8")
            hook.chmod(hook.stat().st_mode | stat.S_IXUSR)
            errors: list[str] = []
            with patch.object(validate_adapters, "ROOT", root):
                validate_adapters.validate_executable_hook(errors)
            self.assertTrue(any("invalid executable hook" in error for error in errors))

    def test_package_contains_public_contract_and_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.zip"
            second = Path(directory) / "second.zip"
            package_core.write_archive(first)
            package_core.write_archive(second)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with ZipFile(first) as archive:
                names = set(archive.namelist())
            for required in (
                "README.md",
                "LICENSE",
                "SPEC_PUBLIC_EXPANSION.md",
                "docs/public-gap-matrix.md",
                "tests/test_contracts.py",
            ):
                self.assertIn(required, names)


if __name__ == "__main__":
    unittest.main()
