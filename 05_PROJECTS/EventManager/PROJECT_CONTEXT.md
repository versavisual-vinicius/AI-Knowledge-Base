# EventManager — Project Context

## Visão

EventManager é uma plataforma de gestão operacional para cerimonialistas e planejadores de eventos. O sistema deve centralizar planejamento, equipe, fornecedores, finanças, convidados e acompanhamento da execução.

## Objetivo principal

Construir uma fundação integrada e utilizável, evitando manter o produto em estado de demonstração. A prioridade é validar fluxos reais de ponta a ponta antes de ampliar o escopo.

## Direção técnica atual

- Aplicação web moderna.
- Backend com TypeScript/Node.js por padrão, salvo decisão posterior registrada.
- PostgreSQL como banco relacional.
- Arquitetura multi-tenant.
- Implantação compatível com Vercel.
- Supabase é candidato preferencial para banco, autenticação e recursos complementares, sujeito à validação no repositório real.

## Domínios principais

- Agências ou workspaces.
- Usuários, membros e papéis.
- Eventos.
- Tarefas, checklists e equipe.
- Fornecedores e propostas.
- Orçamento, pagamentos e fluxo financeiro.
- Convidados e RSVP.
- Documentos, contratos e arquivos.
- Notificações e automações.

## Papéis iniciais

- `admin`: administração completa do workspace.
- `planner`: gestão dos eventos atribuídos.
- `assistant`: acesso operacional limitado, incluindo visualização e conclusão de tarefas autorizadas.

Os papéis devem ser refinados conforme os fluxos reais do produto.

## Regras obrigatórias

- Toda entidade de negócio pertencente a uma agência deve preservar isolamento por tenant.
- Operações financeiras críticas devem usar transações.
- Endpoints públicos de RSVP devem usar tokens únicos, expiráveis ou revogáveis quando aplicável.
- O sistema não deve depender de dados fictícios ou `localStorage` como persistência definitiva.
- Antes de criar novas funcionalidades, inspecionar o repositório e reutilizar implementações existentes.

## Direção visual

- Identidade: Operational Excellence.
- Paleta principal: deep navy e azul vibrante.
- Tipografia: Inter.
- Interface profissional, clara e orientada à operação.

## Prioridade atual

1. Mapear o estado real do código.
2. Definir banco e autenticação reais.
3. Implementar o fluxo mínimo de ponta a ponta.
4. Substituir mocks e persistência temporária.
5. Validar permissões, multi-tenancy e deploy.

## Integrações candidatas

- Supabase.
- Vercel.
- GitHub.
- Google Drive ou storage equivalente.
- Google Calendar.
- Gmail.
- n8n.

Nenhuma integração deve ser considerada implementada sem confirmação no código ou em `DECISIONS.md`.
