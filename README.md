# AI Knowledge Base

Base de conhecimento reutilizável para orientar ferramentas de IA em projetos da VersaVisual.

## Objetivo

Centralizar instruções, padrões técnicos, decisões arquiteturais, integrações e contexto de projetos em arquivos Markdown portáveis entre Google AI Studio, ChatGPT, Codex, Claude e outras ferramentas.

## Estrutura

- `00_SYSTEM/`: comportamento dos agentes e padrões gerais.
- `01_ARCHITECTURE/`: arquitetura, backend, banco, autenticação, APIs, segurança e desempenho.
- `02_DESIGN/`: design system e regras de UX.
- `03_BUSINESS/`: regras de negócio e fluxos.
- `04_INTEGRATIONS/`: documentação operacional das integrações.
- `05_PROJECTS/`: contexto e documentação específica de cada projeto.

## Uso no Google AI Studio

Anexe primeiro:

1. `00_SYSTEM/SYSTEM_INSTRUCTIONS.md`
2. `05_PROJECTS/<PROJETO>/PROJECT_CONTEXT.md`
3. Os documentos técnicos relevantes para a tarefa.
4. Imagens, exports ou trechos de código somente quando necessários.

Evite anexar toda a base sem necessidade. Use o menor conjunto de contexto capaz de concluir a tarefa.

## Regra principal

A documentação do projeto é a fonte de verdade. Quando houver conflito entre instruções genéricas e documentos específicos do projeto, prevalece o documento específico do projeto.
