# Evidência de runtime por harness

Use este registro para provar uma execução real do núcleo em um harness. Não
inclua tokens, cookies, transcripts completos ou dados pessoais.

## Registro mínimo

- Harness e versão:
- Sistema operacional:
- Commit ou versão do AI Knowledge Base:
- Data:
- Instalação/entrada usada:
- Prompt de bootstrap usado:
- Resultado esperado:
- Resultado observado:
- Evals executados:
- Limitações ou falhas:
- Evidência sanitizada:

## Estados permitidos

- `runtime validated`: comando real executado e resultado observado registrado;
- `runtime pending`: adapter disponível, mas sem execução real registrada;
- `runtime skipped`: execução conscientemente fora do escopo desta versão;
- `blocked`: execução impedida por ausência, erro ou permissão do harness.

## Evidências já registradas

### Codex

- Estado: `runtime validated`.
- Execução: `codex exec --ephemeral --sandbox read-only`.
- Resultado: bootstrap, manifesto, `SPEC.md` e cinco skills foram lidos sem
  alteração do repositório.

### Antigravity

- Estado: `runtime validated`.
- Execução: `agy plugin validate .`.
- Resultado: 5 skills, 1 agent e 1 hook processados com sucesso.

Os demais harnesses permanecem `runtime pending` até que um usuário registre
uma execução real seguindo este formato.
