# EventManager — Project Context

## Visão

EventManager é um produto em reposicionamento para noivas. A direção anterior, focada em cerimonialistas e planejadores, deve ser tratada como contexto legado até a nova experiência ser especificada.

O novo produto deve centralizar a jornada da noiva: organização do casamento, decisões, orçamento, fornecedores, convidados, cronograma, referências e acompanhamento.

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

## Direção de produto

- Público primário: noivas e casais em organização do casamento.
- O fluxo deve reduzir ansiedade e carga de decisão, com linguagem clara e acolhedora.
- A arquitetura operacional anterior não deve ser portada automaticamente para a nova experiência.
- A nova jornada precisa ser especificada antes de redefinir entidades, navegação ou autenticação.

## Prioridade atual

1. Mapear o estado real do código e separar legado de funcionalidades reaproveitáveis.
2. Especificar a jornada da noiva e o primeiro fluxo funcional.
3. Definir banco e autenticação reais para a nova jornada.
4. Implementar o fluxo mínimo de ponta a ponta.
5. Substituir mocks e persistência temporária.
6. Validar permissões, multi-tenancy e deploy.

## Integrações candidatas

- Supabase.
- Vercel.
- GitHub.
- Google Drive ou storage equivalente.
- Google Calendar.
- Gmail.
- n8n.

Nenhuma integração deve ser considerada implementada sem confirmação no código ou em `DECISIONS.md`.
