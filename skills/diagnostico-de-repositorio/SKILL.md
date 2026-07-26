---
name: diagnostico-de-repositorio
description: Auditar um repositório real para separar legado, mocks, integrações e código reaproveitável antes da construção.
---

# Diagnóstico de repositório

Use antes de implementar uma feature, migrar um projeto ou decidir se algo deve
ser criado do zero.

1. Confirme checkout, branch e instruções locais.
2. Mapeie estrutura, scripts, dependências, documentação, testes e deploy.
3. Identifique código ativo, legado, mocks, duplicações e lacunas.
4. Relacione achados ao objetivo e ao `SPEC.md`.
5. Produza uma saída curta: reutilizar, alterar, isolar, substituir ou criar.
6. Registre riscos e evidências; não altere arquivos durante a auditoria.

Use `rg --files`, `rg`, status Git e os scripts existentes antes de adicionar
ferramentas novas.
