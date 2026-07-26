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
- Validação real pendente: `codex` e `agy` foram executados neste Mac; Gemini
  CLI foi instalado, mas seu runtime foi deliberadamente pulado em favor do
  Antigravity; Claude, OpenCode, Kimi e Pi não foram executados localmente
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
- Evidência: `evals/cases.json`, `evals/README.md` e
  `scripts/run_evals.py`; smoke test executado com 14/14 casos aprovados
- Limitação: execução real concluída no Codex e no Antigravity neste ambiente;
  os demais casos aguardam os respectivos CLIs
- Aprovação humana: Approved — Vini, 2026-07-26

## Etapa 5 — Licenças e instalação

- Status: Approved
- Escopo: atribuição de terceiros e instruções curtas de instalação por harness
- Fora do escopo: publicação em marketplace e configuração automática de contas
- Critério de aceite: origem/licença dos componentes registrada e instalação
  local documentada sem expor credenciais
- Evidência: `LICENSE`, `THIRD_PARTY_NOTICES.md` e `docs/INSTALLATION.md`; a
  licença própria MIT e a atribuição MIT do Superpowers estão separadas
- Validação documental: comandos locais registrados para Claude Code,
  OpenCode, Kimi e Pi; nenhum login ou instalação externa foi executado
- Aprovação humana: Approved — Vini, 2026-07-26

## Etapa 6 — Validação real e pacote local

- Status: Approved
- Escopo: validar o núcleo nos harnesses disponíveis e gerar pacote local
  determinístico para distribuição controlada
- Fora do escopo: publicar em marketplace, instalar contas ou declarar runtime
  validado nos harnesses ausentes
- Critério de aceite: Codex e Antigravity têm validação local registrada; o
  pacote contém os componentes obrigatórios e exclui artefatos temporários
- Evidência: `codex exec --ephemeral --sandbox read-only` leu o bootstrap,
  manifesto, `SPEC.md` e cinco skills sem alterar arquivos; `agy plugin
  validate .`, validadores do núcleo e `scripts/package_core.py` produziram e
  verificaram um ZIP determinístico de 57 arquivos
- Limitações: Claude, OpenCode, Kimi e Pi ainda aguardam sessões reais; Gemini
  CLI permanece fora do escopo desta release; o executor automatiza a
  avaliação dos resultados, mas não substitui a execução do caso no harness do
  usuário
- Aprovação humana: Approved — Vini, 2026-07-26
