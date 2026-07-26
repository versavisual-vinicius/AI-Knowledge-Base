# SPEC — Núcleo compatível da AI Knowledge Base

- Data: 2026-07-26
- Status: Approved
- Repositório canônico: `versavisual-vinicius/AI-Knowledge-Base`

## Objetivo

Evoluir a AI Knowledge Base para um núcleo reutilizável de skills, bootstrap,
adapters, scripts, referências, documentação e evals que possa orientar agentes
em diferentes harnesses, preservando as dores e regras operacionais da
VersaVisual.

## Harnesses da primeira versão

- Codex;
- Claude Code;
- Antigravity;
- Gemini CLI;
- OpenCode;
- Kimi;
- Pi.

A compatibilidade deve ser baseada em conteúdo portátil e adapters pequenos,
nunca em dependência de uma ferramenta proprietária específica.

## Dores que o núcleo deve resolver

1. agir antes de consultar memória, base e projetos relacionados;
2. criar soluções paralelas quando já existe algo reaproveitável;
3. iniciar construção sem mapa de ferramentas, serviços, assinaturas e limites;
4. começar sem `SPEC.md` aprovado;
5. criar etapas longas e difíceis de revisar;
6. executar sem aprovação humana entre etapas;
7. declarar conclusão sem evidências proporcionais;
8. perder decisões, contexto e critérios entre agentes diferentes.

## Escopo incluído

### Conteúdo portátil

- bootstrap inicial que instrui consulta e seleção de skills;
- skills da AI Knowledge Base organizadas por dor recorrente;
- regras de contexto, reutilização, ferramentas, spec e aprovação;
- templates e schemas de `SPEC.md`, decisões e etapas;
- documentação curta de instalação, uso e compatibilidade;
- evals comportamentais com casos reais do EventManager e VersaVisual Educação.

### Adapters por harness

Criar somente os arquivos mínimos necessários para:

- Codex: plugin manifest, skills e instrução de bootstrap;
- Claude Code: `CLAUDE.md` ou configuração equivalente, sem duplicar o núcleo;
- Antigravity: extensão/configuração de inicialização;
- Gemini CLI: `GEMINI.md` ou extensão equivalente;
- OpenCode: instrução de instalação/bootstrap compatível;
- Kimi: documentação/configuração de plugin;
- Pi: pacote/configuração de skills.

Cada adapter deve apontar para a mesma fonte de verdade e explicar suas
limitações. Não criar sete versões independentes das regras.

### Scripts determinísticos

- validação de estrutura, manifestos, skills, links e placeholders;
- empacotamento do núcleo para os harnesses suportados;
- checagem de arquivos obrigatórios e compatibilidade documental.

Scripts que façam publicação, alteração de console, deploy ou envio externo
ficam fora desta primeira versão.

## Fora do escopo

- copiar toda a estrutura, assets, planos, extensões ou testes do Superpowers;
- reproduzir integralmente workflows que não correspondam às dores da base;
- incluir brainstorm visual, servidor web, worktree automation ou subagents como
  requisito inicial;
- instalar ou configurar ferramentas externas automaticamente;
- publicar em marketplaces ou fazer deploy;
- prometer compatibilidade sem teste no harness correspondente;
- criar uma skill genérica quando uma skill existente puder ser estendida.

## Estrutura-alvo inicial

```text
.codex-plugin/
agents/
adapters/
  antigravity/
  claude/
  codex/
  gemini-cli/
  kimi/
  opencode/
  pi/
skills/
scripts/
references/
evals/
docs/
BOOTSTRAP.md
SPEC.md
```

## Reutilização obrigatória

Antes de criar qualquer componente, consultar:

- memória autorizada;
- `00_SYSTEM/`, `01_ARCHITECTURE/`, `05_PROJECTS/` e `06_PLAYBOOKS/`;
- os repositórios EventManager e VersaVisual Educação;
- o núcleo de skills já existente;
- a estrutura pública do Superpowers apenas como referência de compatibilidade.

Registrar no plano de implementação o que será reutilizado, adaptado,
substituído ou deliberadamente excluído.

## Licença e atribuição

O Superpowers auditado declara licença MIT. A MIT permite usar, copiar,
modificar, distribuir, sublicenciar e vender software, inclusive em produto
comercial, desde que o aviso de copyright e o texto da licença acompanhem as
cópias ou partes substanciais. A licença também fornece o software “como está”,
sem garantia.

Para qualquer código, documentação ou asset efetivamente incorporado:

- preservar `LICENSE` e avisos de copyright do Superpowers;
- registrar a origem e o caminho incorporado;
- separar componentes de terceiros com licença própria;
- não sugerir endosso de obra, autor ou projeto original;
- não remover avisos por reescrita ou adaptação;
- fazer revisão jurídica se a distribuição comercial ou algum asset tiver
  licença diferente.

Esta especificação autoriza apenas a análise e o planejamento da adaptação,
não a incorporação automática de todos os arquivos do Superpowers.

## Critérios de aceite do núcleo

- os sete harnesses possuem instrução de entrada ou adapter documentado;
- as regras centrais continuam em uma única fonte de verdade;
- cada adapter funciona sem exigir copiar o repositório inteiro;
- as skills passam nos validadores oficiais;
- o plugin Codex passa no validador oficial;
- scripts detectam estrutura inválida e placeholders;
- evals comprovam seleção de skill, bloqueio sem aprovação e verificação;
- EventManager e VersaVisual Educação aparecem como casos de contexto, sem
  transformar suas decisões em regras universais;
- nenhum componente externo é incorporado sem atribuição e revisão de licença.

## Etapas propostas

As etapas serão detalhadas somente após aprovação deste spec e deverão ser
curtas, independentes e aprováveis:

1. congelar contrato documental e mapa de adapters;
2. criar adapters mínimos por harness;
3. expandir scripts e validação multiplataforma;
4. criar evals por harness e por dor recorrente;
5. revisar atribuição/licenças e documentação de instalação;
6. validar o núcleo em casos reais e preparar pacote local.

## Aprovação humana

- Revisor: Vini
- Data: 2026-07-26
- Status: Approved
- Observações: Núcleo compatível aprovado para execução em etapas curtas.
