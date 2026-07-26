# Playbook — Iniciar e conduzir um projeto

## Objetivo

Garantir que todo projeto seja criado a partir de uma especificação aprovada, executado em etapas curtas e concluído somente quando cada etapa atender rigorosamente ao `SPEC.md` correspondente.

Este playbook é obrigatório para projetos novos e mudanças relevantes em projetos existentes.

## Fluxo obrigatório

```text
Criar SPEC.md
  ↓
Consultar memória, esta base e projetos existentes
  ↓
Mapear ferramentas, assinaturas, serviços e alternativas
  ↓
Revisão humana da especificação
  ↓
Aprovação humana da especificação
  ↓
Dividir o projeto em etapas curtas
  ↓
Aprovar o plano de etapas
  ↓
Preencher contexto e escopo
  ↓
Auditar o repositório real
  ↓
Registrar decisões confirmadas
  ↓
Selecionar perfil técnico
  ↓
Concluir a etapa atual conforme o SPEC
  ↓
Validar código e resultado visível
  ↓
Aprovação humana da etapa
  ↓
Criar a estrutura visual aprovada
  ↓
Iniciar a criação do projeto
  ↓
Dividir o restante em novas etapas curtas
  ↓
Repetir execução, validação e aprovação
  ↓
Atualizar status e pendências
  ↓
Arquivar versões obsoletas
```

## Regras obrigatórias

### 1. Especificação antes de execução

Antes de criar código, telas, banco, integrações ou estrutura visual, criar um `SPEC.md` contendo:

- objetivo, problema, público e escopo;
- resultado esperado e fluxos principais;
- requisitos funcionais e não funcionais;
- regras de negócio, permissões e dependências;
- restrições, riscos e suposições;
- critérios de aceite verificáveis;
- itens explicitamente fora do escopo.

Não iniciar implementação com especificação vaga, contraditória ou sem critérios de aceite.

### 2. Consulta obrigatória e reaproveitamento

Antes de fechar a especificação, consultar a memória autorizada, esta base e os
projetos existentes do usuário. Verificar especialmente projetos com o mesmo
domínio, público, finalidade ou segmentação.

Registrar no `SPEC.md`:

- fontes e projetos consultados;
- funcionalidades, componentes e documentos que serão reaproveitados;
- itens que serão aprimorados ou substituídos;
- motivo comprovado para criar algo novo quando houver solução semelhante.

A solução nova não deve duplicar um projeto existente sem justificar a
separação.

### 3. Mapa de ferramentas antes da aprovação

Antes da aprovação humana, elaborar um guia de ferramentas para todo o ciclo:

- construção e desenvolvimento;
- design e estrutura visual;
- banco, autenticação e storage;
- integrações e automações;
- testes, lint, tipos e build;
- observabilidade, deploy e manutenção.

Consultar as skills e ferramentas disponíveis, os serviços e assinaturas
autorizados pelo usuário e o que já existe nos projetos relacionados. Para cada
necessidade, registrar `Disponível`, `A confirmar`, `Alternativa` ou
`Bloqueador`, sem expor credenciais ou valores sensíveis.

Se faltar uma ferramenta essencial, pesquisar alternativas na documentação
oficial e no catálogo
`https://github.com/ripienaar/free-for-dev`. Comparar custo, limites,
privacidade, lock-in, manutenção e integração. O `SPEC.md` só pode ser
aprovado com ferramenta viável, alternativa aprovada ou adiamento explícito.

### 4. Revisão e aprovação humana

A especificação precisa ser revisada e aprovada antes da divisão ou execução. Registrar no documento:

```markdown
## Aprovação

- Revisor: Nome
- Data: YYYY-MM-DD
- Status: Pending | Approved | Changes Requested
- Observações:
```

Somente `Approved` autoriza o avanço. A aprovação não deve ser inferida por silêncio ou conversa incompleta.

### 5. Etapas curtas e aprováveis

Após a aprovação do `SPEC.md`, dividir o projeto em etapas independentes, verificáveis e pequenas. Cada etapa deve ter objetivo único, escopo, exclusões, dependências, critérios de aceite, evidência de validação e ponto de aprovação humana.

Nunca criar etapas longas ou genéricas, como “implementar o sistema”, “finalizar o backend” ou “criar toda a plataforma”. Se uma etapa envolver decisões, fluxos ou validações independentes, dividi-la novamente.

### 6. Contexto e auditoria

Antes da primeira etapa:

1. preencher `PROJECT_CONTEXT.md`;
2. auditar o repositório real;
3. identificar código, decisões e integrações reaproveitáveis;
4. separar legado, mocks e funcionalidades confirmadas;
5. registrar decisões aprovadas em `DECISIONS.md`;
6. selecionar o perfil técnico aplicável.

Nenhuma etapa deve ser planejada com base apenas em suposições.

### 7. Estrutura visual aprovada

Em projetos com interface, criar a arquitetura de navegação, wireframes ou telas-base, estados, responsividade, acessibilidade e componentes necessários depois da aprovação do spec e do plano de etapas, antes da implementação completa. Validar a estrutura visual contra o `SPEC.md`.

### 8. Execução e aprovação por etapa

Para cada etapa:

1. confirmar o escopo aprovado;
2. implementar somente o necessário;
3. validar os critérios de aceite e o resultado visível;
4. registrar arquivos alterados, evidências e limitações;
5. solicitar aprovação humana;
6. somente então iniciar a próxima etapa.

Se surgir algo fora do `SPEC.md`, pausar, registrar a mudança e solicitar revisão da especificação.

Registro mínimo:

```markdown
## Etapa 01 — Nome curto

- Status: Pending | In Progress | Validation | Approved | Changes Requested
- Objetivo:
- Escopo:
- Fora do escopo:
- Critérios de aceite:
- Evidências:
- Aprovação humana:
```

## Conclusão do projeto

Declarar o projeto concluído somente quando todas as etapas estiverem aprovadas, o resultado estiver alinhado ao `SPEC.md`, as verificações tiverem evidências, as pendências estiverem registradas, decisões obsoletas estiverem arquivadas e a aprovação final humana estiver registrada.

Build, lint ou testes verdes não substituem a revisão humana nem comprovam sozinhos o resultado visual ou operacional.

## Mudança de escopo

Qualquer alteração de objetivo, público, fluxo, arquitetura, permissões, dados, custo ou critério de aceite deve ser registrada no `SPEC.md`, revisada e aprovada antes de afetar a etapa atual. Mudanças maiores devem gerar novas etapas curtas.
