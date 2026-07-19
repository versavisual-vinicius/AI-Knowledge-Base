# Database

## Banco padrão

PostgreSQL é o banco relacional preferencial para aplicações de negócio com entidades relacionadas, operações financeiras, auditoria e multi-tenancy.

## Convenções

- Chaves primárias: UUID quando houver exposição pública ou sincronização distribuída.
- Datas: `timestamptz` em UTC.
- Valores monetários: tipos decimais ou inteiros em centavos; nunca ponto flutuante.
- Nomes: `snake_case` no banco.
- Exclusão lógica somente quando houver necessidade de histórico ou restauração.

## Integridade

- Use `NOT NULL`, `CHECK`, `UNIQUE` e foreign keys.
- Crie índices para filtros, joins e ordenações frequentes.
- Não use JSON como substituto automático de modelagem relacional.
- Registre migrations versionadas.

## Multi-tenancy

- Tabelas pertencentes a organizações devem incluir `tenant_id`.
- Índices compostos devem considerar `tenant_id` quando fizer parte dos filtros principais.
- Quando usar Supabase/Postgres com RLS, criar policies para leitura e escrita baseadas na sessão autenticada.
- Nunca aceitar o tenant apenas do body ou query string.

## Auditoria

Operações críticas devem registrar:

- ator;
- tenant;
- entidade e identificador;
- ação;
- estado anterior e posterior quando adequado;
- data e origem.

## Transações

Use transações para aprovações financeiras, criação de entidades dependentes, atualizações de estoque/capacidade e qualquer operação que não possa ficar parcialmente concluída.
