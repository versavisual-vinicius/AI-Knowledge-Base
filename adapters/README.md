# Adapters por harness

Os adapters traduzem o mesmo núcleo de regras para cada agente. Eles não devem
duplicar `SYSTEM_INSTRUCTIONS.md`, skills, templates ou decisões.

## Contrato de um adapter

Cada adapter futuro deve declarar:

- nome do harness e versão mínima conhecida;
- arquivo ou mecanismo de bootstrap;
- como descobrir/carregar `skills/`;
- como referenciar `references/` e `SPEC.md`;
- limitações de ferramentas, hooks e subagentes;
- comando de instalação local;
- comando ou procedimento de validação;
- estado: `Planned`, `Draft`, `Validated` ou `Blocked`.

## Fonte de verdade

O adapter deve apontar para:

1. `BOOTSTRAP.md`;
2. `00_SYSTEM/SYSTEM_INSTRUCTIONS.md`;
3. a skill aplicável;
4. `SPEC.md` e documentos do projeto;
5. `references/` somente quando necessário.

Se o harness não suportar uma capacidade, documentar a limitação e oferecer um
fallback explícito. Não simular hooks, memória, subagentes ou ferramentas que o
harness não disponibiliza.
