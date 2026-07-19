# Backend

## Padrão recomendado

- Runtime principal: Node.js com TypeScript.
- Banco relacional: PostgreSQL.
- Validação: schemas explícitos para toda entrada externa.
- API: REST por padrão; GraphQL apenas quando houver necessidade clara.
- Jobs assíncronos: fila somente para tarefas demoradas ou resilientes.

## Organização sugerida

```text
src/
  modules/
    <module>/
      domain/
      application/
      infrastructure/
      presentation/
  shared/
    auth/
    database/
    errors/
    logging/
    validation/
```

## Regras

- Handlers não devem conter regra de negócio complexa.
- Casos de uso devem ser testáveis sem HTTP.
- Repositórios encapsulam persistência.
- Integrações externas devem ficar atrás de interfaces/adapters.
- Erros de domínio devem ser mapeados para respostas HTTP consistentes.
- Logs devem incluir correlação, tenant, usuário e operação quando aplicável.

## Variáveis de ambiente

Nunca inserir valores reais na documentação. Manter apenas nomes esperados em `.env.example`, por exemplo:

```env
DATABASE_URL=
AUTH_SECRET=
STORAGE_BUCKET=
QUEUE_URL=
```

## Observabilidade

Registrar no mínimo:

- falhas de autenticação e autorização;
- erros de integração;
- jobs com retry ou falha definitiva;
- operações financeiras relevantes;
- duração de endpoints críticos.
