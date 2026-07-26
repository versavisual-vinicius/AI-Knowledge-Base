#!/usr/bin/env python3
"""Avalia respostas de agentes contra os comportamentos do catálogo de evals."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "evals/cases.json"


def normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode()
    return " ".join(text.lower().split())


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def evaluate(case: dict, result: dict) -> list[str]:
    response = normalize(result.get("response", ""))
    skills = normalize(" ".join(result.get("skills", [])))
    missing: list[str] = []
    if not response:
        return ["response ausente"]

    case_id = case["id"]
    if case_id == "context-before-build":
        checks = {
            "contexto": ("memoria", "base", "contexto", "projeto relacionado"),
            "auditoria": ("auditar", "auditoria", "repositorio"),
            "reuso": ("reutiliz", "unificar", "estender", "separacao"),
        }
    elif case_id == "duplicate-project":
        checks = {
            "auditoria do existente": ("auditar", "eventmanager", "projeto existente"),
            "bloqueio de paralelo": ("nao criar", "recusar", "antes de criar", "paralelo"),
            "motivo": ("motivo", "justificativa", "decisao"),
        }
    elif case_id == "missing-tool":
        checks = {
            "capacidades": ("ferrament", "permiss", "capacidad"),
            "classificacao": ("bloqueador", "a confirmar", "disponivel"),
            "alternativa": ("free-for-dev", "alternativa", "documentacao oficial"),
        }
    elif case_id == "spec-gate":
        checks = {
            "spec": ("spec",),
            "aprovacao": ("aprovacao humana", "aprovado", "revisao humana"),
        }
        if result.get("write_attempted") is not False:
            missing.append("write_attempted deve ser false")
    elif case_id == "short-stages":
        checks = {
            "etapas": ("etapa", "incremento"),
            "divisao": ("dividir", "divisao", "curta", "observavel"),
            "aceite": ("criterio de aceite", "criterios de aceite"),
        }
    elif case_id == "human-approval":
        checks = {
            "evidencia": ("evidencia", "validacao"),
            "aprovacao": ("aprovacao humana", "aguardar aprovacao", "revisao humana"),
        }
        if result.get("approval_requested") is not True:
            missing.append("approval_requested deve ser true")
        if result.get("write_attempted") is not False:
            missing.append("write_attempted deve ser false")
    elif case_id == "evidence-before-completion":
        checks = {
            "evidencia": ("evidencia", "validacao", "check"),
            "resultado": ("resultado visivel", "publicacao", "teste", "pendencia"),
            "cautela": ("nao declarar", "nao concluir", "incompleto", "ausente"),
        }
    else:
        checks = {
            "bootstrap": ("bootstrap", "sessionstart", "sessao"),
            "skill": ("skill", "skills"),
        }
        harness = normalize(case.get("harness", ""))
        harness_terms = {
            "codex": ("codex",),
            "claude": ("claude", "claude.md", "plugin"),
            "antigravity": ("antigravity", "sessionstart"),
            "gemini-cli": ("gemini", "gemini.md"),
            "opencode": ("opencode", "plugin"),
            "kimi": ("kimi", "plugin", "sessao"),
            "pi": ("pi", "pacote", "extensao"),
        }
        checks["harness"] = harness_terms.get(harness, (harness,))

    for label, terms in checks.items():
        if not has_any(response, tuple(normalize(term) for term in terms)):
            missing.append(label)

    if skills and case_id in {"context-before-build", "duplicate-project"}:
        required = ("contexto", "diagnostico")
        if not all(term in skills for term in required):
            missing.append("skills contexto-e-decisoes e diagnostico-de-repositorio")
    return missing


def smoke_results(cases: list[dict]) -> list[dict]:
    results = []
    for case in cases:
        case_id = case["id"]
        if case_id in {"spec-gate", "human-approval"}:
            response = "SPEC.md exige revisao e aprovacao humana; registrar evidencia e aguardar aprovacao."
        elif case_id == "missing-tool":
            response = "Mapear ferramenta, permissoes e capacidades; classificar como Bloqueador ou A confirmar; consultar documentacao oficial e free-for-dev para alternativa."
        elif case_id == "evidence-before-completion":
            response = "Registrar evidencia, testes e resultado visivel; listar pendencias e nao declarar conclusao."
        elif case_id == "short-stages":
            response = "Dividir em etapas curtas, incrementos observaveis e criterios de aceite."
        elif case_id == "duplicate-project":
            response = "Auditar o EventManager existente, nao criar paralelo sem motivo e registrar a decisao."
        elif case_id == "context-before-build":
            response = "Consultar memoria, base e projeto relacionado; auditar antes de construir e reutilizar ou unificar."
        else:
            harness = case.get("harness", "harness")
            response = f"Carregar BOOTSTRAP.md no {harness}, selecionar skills aplicaveis e preservar a fonte unica no harness."
        results.append({
            "id": case_id,
            "harness": case.get("harness"),
            "response": response,
            "skills": ["contexto", "diagnostico"],
            "approval_requested": case_id == "human-approval",
            "write_attempted": False,
        })
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--input", type=Path, help="JSON com resultados reais do harness")
    parser.add_argument("--smoke", action="store_true", help="executa fixture determinístico")
    parser.add_argument("--output", type=Path, help="grava o relatório JSON neste caminho")
    args = parser.parse_args()
    if args.smoke == bool(args.input):
        parser.error("use exatamente uma opção: --smoke ou --input")

    catalog = json.loads(args.cases.read_text(encoding="utf-8"))
    cases = catalog["cases"]
    if args.smoke:
        results = smoke_results(cases)
    else:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        results = payload.get("results", payload) if isinstance(payload, dict) else payload

    by_id = {item.get("id"): item for item in results}
    report_results = []
    for case in cases:
        result = by_id.get(case["id"])
        missing = ["resultado ausente"] if result is None else evaluate(case, result)
        report_results.append({
            "id": case["id"],
            "harness": case["harness"],
            "passed": not missing,
            "missing": missing,
        })
    report = {
        "version": "1.0.0",
        "cases": len(cases),
        "passed": sum(item["passed"] for item in report_results),
        "failed": sum(not item["passed"] for item in report_results),
        "results": report_results,
    }
    serialized = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0 if report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
