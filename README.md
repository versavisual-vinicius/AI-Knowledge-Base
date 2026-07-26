# AI Knowledge Base

Base pública e reutilizável de skills, contexto e gates para orientar agentes
de IA em projetos da VersaVisual.

[![Validate AI Knowledge Base](https://github.com/versavisual-vinicius/AI-Knowledge-Base/actions/workflows/validate.yml/badge.svg)](https://github.com/versavisual-vinicius/AI-Knowledge-Base/actions/workflows/validate.yml)

Repositório: https://github.com/versavisual-vinicius/AI-Knowledge-Base

## Objetivo

Centralizar instruções, padrões técnicos, decisões arquiteturais, integrações e contexto de projetos em arquivos Markdown portáveis entre Google AI Studio, ChatGPT, Codex, Claude e outras ferramentas.

## Estrutura

- `00_SYSTEM/`: comportamento dos agentes e padrões gerais.
- `01_ARCHITECTURE/`: arquitetura, backend, banco, autenticação, APIs, segurança e desempenho.
- `02_DESIGN/`: design system e regras de UX.
- `03_BUSINESS/`: regras de negócio e fluxos.
- `04_INTEGRATIONS/`: documentação operacional das integrações.
- `05_PROJECTS/`: contexto e documentação específica de cada projeto.
  - `EventManager/`: produto separado, em reposicionamento para noivas.
  - `VersaVisual-Educacao/`: unificação do curso, simulador e fontes editoriais no site oficial.

## Uso no Google AI Studio

Anexe primeiro:

1. `00_SYSTEM/SYSTEM_INSTRUCTIONS.md`
2. `05_PROJECTS/<PROJETO>/PROJECT_CONTEXT.md`
3. Os documentos técnicos relevantes para a tarefa.
4. Imagens, exports ou trechos de código somente quando necessários.

Evite anexar toda a base sem necessidade. Use o menor conjunto de contexto capaz de concluir a tarefa.

## Regra principal

A documentação do projeto é a fonte de verdade. Quando houver conflito entre instruções genéricas e documentos específicos do projeto, prevalece o documento específico do projeto.

## Plugin e skills

Este repositório também é um plugin Codex instalável. O núcleo fica em:

- `skills/`: uma skill por dor recorrente;
- `scripts/`: validações determinísticas;
- `references/`: contratos, templates, schemas e decisões;
- `BOOTSTRAP.md`: seleção das skills antes de agir;
- `.codex-plugin/plugin.json`: manifesto do plugin.

### Início rápido público

```bash
git clone https://github.com/versavisual-vinicius/AI-Knowledge-Base.git
cd AI-Knowledge-Base
python3 scripts/validate_knowledge_base.py
python3 scripts/validate_adapters.py
python3 scripts/run_evals.py --smoke
```

Depois, leia `BOOTSTRAP.md`, selecione o adapter do seu harness e consulte
`docs/INSTALLATION.md`. O núcleo é agnóstico de fornecedor, mas o runtime de
cada harness deve ser validado no ambiente que o utiliza.

### Instalação local

No diretório pai do repositório, adicione-o ao marketplace local ou instale o
plugin pelo fluxo disponível na sua versão do Codex. Para validar antes:

```bash
python3 scripts/validate_knowledge_base.py
```

Se o ambiente possuir o validador oficial de skills, execute-o para cada pasta
em `skills/`. O uso do plugin começa pelo `BOOTSTRAP.md`; depois carregue apenas
as skills correspondentes à dor atual.

### Uso recomendado

1. Consulte memória, esta base e projetos relacionados.
2. Audite o repositório real.
3. Monte o inventário de ferramentas.
4. Crie e aprove o `SPEC.md`.
5. Execute etapas curtas com validação e aprovação humana.

## Limites e contribuição

Esta base orienta o agente; não substitui memória, permissões, ferramentas ou
validação real do harness. Consulte `SECURITY.md`, `CONTRIBUTING.md` e
`RELEASE-NOTES.md` antes de colaborar.

Licença: [MIT](LICENSE).
