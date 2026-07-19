# Authentication and Authorization

## Princípios

- Autenticação confirma identidade.
- Autorização confirma permissão.
- Toda verificação crítica ocorre no servidor.
- O cliente nunca é fonte confiável para papel, tenant ou ownership.

## Requisitos mínimos

- Sessões seguras e com expiração.
- Proteção contra reutilização indevida de tokens.
- RBAC ou políticas equivalentes.
- Isolamento de tenant.
- Recuperação de conta segura.
- Auditoria de ações críticas.

## Papéis

Cada projeto deve definir papéis reais e suas capacidades em `PROJECT_CONTEXT.md` ou documento específico. Evite papéis genéricos sem vínculo com regras de negócio.

## Autorização

Antes de cada ação protegida, validar:

1. usuário autenticado;
2. tenant ativo;
3. papel ou permissão;
4. vínculo com o recurso;
5. estado permitido da entidade.

## Integrações

Quando usar provedores externos, documentar callbacks, webhooks, claims utilizadas, sincronização de usuários e comportamento em caso de indisponibilidade.
