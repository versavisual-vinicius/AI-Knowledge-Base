# Status de implementação

## Etapa 1 — Contrato e mapa de adapters

- Status: Approved
- Escopo: contrato comum e matriz dos sete harnesses
- Critério de aceite: documentação define fonte de verdade, capacidades,
  limitações, estados e validação por harness
- Evidência: `adapters/README.md` e `docs/compatibility-matrix.md`
- Aprovação humana: Approved — Vini, 2026-07-26

## Etapa 2 — Adapters mínimos por harness

- Status: Approved
- Escopo: sete integrações mínimas apontando para a fonte única de verdade
- Fora do escopo: workflows específicos, assets, hooks adicionais e publicação
- Critério de aceite: cada harness possui integração executável ou entrypoint
  nativo documentado com bootstrap, instalação local, limitações e validação
  prevista
- Evidência local: manifests JSON, plugin Antigravity, hooks SessionStart,
  plugin OpenCode e extensão Pi criados; sintaxe e bootstrap validados
- Validação real pendente: somente `codex` e `agy` estão instalados neste Mac;
  Claude, Gemini CLI, OpenCode, Kimi e Pi não foram executados localmente
- Aprovação humana: Approved — Vini, 2026-07-26

## Etapa 3 — Validação multiplataforma

- Status: Approved
- Escopo: validação determinística dos manifestos, entrypoints, adapters,
  skills e hooks
- Fora do escopo: execução em harnesses não instalados e publicação
- Critério de aceite: um comando local identifica arquivos ausentes, JSON
  inválido, placeholders, adapters incompletos e referências quebradas
- Evidência: `scripts/validate_adapters.py` valida JSON, Markdown, hook
  executável/JSON e `node --check` do plugin OpenCode
- Aprovação humana: Approved — Vini, 2026-07-26

## Etapa 4 — Evals por harness e dor

- Status: Approved
- Escopo: catálogo machine-readable de cenários de seleção, bloqueio,
  reutilização, ferramentas e verificação
- Fora do escopo: executar chamadas pagas ou autenticar sete LLMs
- Critério de aceite: cada harness e cada dor recorrente possuem cenário,
  prompt e comportamento esperado
- Evidência: `evals/cases.json` e `evals/README.md`
- Limitação: execução real disponível apenas para Codex e Antigravity neste
  ambiente; os demais casos aguardam os respectivos CLIs
- Aprovação humana: Approved — Vini, 2026-07-26

## Etapa 5 — Licenças e instalação

- Status: In Progress
- Escopo: atribuição de terceiros e instruções curtas de instalação por harness
- Fora do escopo: publicação em marketplace e configuração automática de contas
- Critério de aceite: origem/licença dos componentes registrada e instalação
  local documentada sem expor credenciais
- Aprovação humana: Pending
