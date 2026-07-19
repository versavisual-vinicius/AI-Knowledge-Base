# Architecture

## Objetivo

Definir uma arquitetura padrão para aplicações web de negócio da VersaVisual, com foco em manutenção, segurança, integração e evolução gradual.

## Diretrizes

- Preferir arquitetura modular em vez de microsserviços prematuros.
- Separar interface, aplicação, domínio e infraestrutura.
- Tratar integrações externas como adaptadores substituíveis.
- Centralizar autenticação, autorização, logs e tratamento de erros.
- Manter decisões específicas dentro do projeto correspondente.

## Camadas recomendadas

1. **Presentation**: páginas, componentes, rotas e handlers.
2. **Application**: casos de uso e orquestração.
3. **Domain**: regras de negócio, entidades e políticas.
4. **Infrastructure**: banco, storage, filas, serviços externos e observabilidade.

## Multi-tenancy

- Toda entidade pertencente a uma organização deve possuir `tenant_id` ou equivalente.
- O tenant atual deve ser derivado da sessão autenticada, nunca confiado diretamente ao cliente.
- Políticas no banco devem reforçar o isolamento sempre que a plataforma permitir.

## Integrações

Cada integração deve documentar:

- finalidade;
- autenticação;
- variáveis de ambiente;
- limites e custos;
- webhooks;
- estratégia de retry;
- tratamento de falhas;
- dados armazenados localmente.

## Evolução

Comece com uma aplicação modular e extraia serviços somente quando houver necessidade comprovada de escala, isolamento operacional ou ciclos independentes de implantação.
