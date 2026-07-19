# Coding Standards

## Princípios

- Clareza antes de abstração.
- Tipagem forte sempre que disponível.
- Funções pequenas e com responsabilidade única.
- Nomes explícitos e consistentes.
- Tratamento de erros previsível.
- Sem duplicação relevante de regras de negócio.
- Comentários apenas quando explicarem o motivo, não o óbvio.

## TypeScript

- Use `strict`.
- Evite `any`; prefira tipos explícitos, generics ou `unknown` com narrowing.
- Valide entradas externas com schema.
- Separe domínio, acesso a dados e transporte HTTP.
- Não misture regras de negócio diretamente em componentes de interface.

## Banco de dados

- Toda alteração de schema deve ser uma migration.
- Use constraints, índices e chaves estrangeiras quando aplicáveis.
- Operações financeiras ou múltiplas escritas relacionadas devem usar transações.
- Em sistemas multi-tenant, toda consulta deve preservar isolamento por tenant.

## APIs

- Use respostas e erros consistentes.
- Valide autenticação e autorização no servidor.
- Torne operações críticas idempotentes quando possível.
- Não retorne dados internos ou sensíveis desnecessários.

## Testes

- Teste regras de negócio e fluxos críticos.
- Inclua casos de erro, autorização e isolamento.
- Não declare conclusão sem executar as verificações disponíveis.
