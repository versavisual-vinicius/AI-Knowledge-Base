---
name: verificacao-com-evidencias
description: Validar mudanças com checks proporcionais e separar código, ambiente, Git, publicação e resultado visível.
---

# Verificação com evidências

Use antes de declarar uma etapa ou projeto concluído.

1. Classifique o risco: rápida, normal ou crítica.
2. Execute somente checks pertinentes: diff, lint, tipos, testes, build,
   navegador, banco ou deployment conforme o caso.
3. Revise arquivos fora do escopo, regressões e dados sensíveis.
4. Registre comando, resultado e o que ficou sem validação.
5. Diferencie arquivo alterado, commit, push, deployment e resultado público.
6. Só marque a etapa como aprovada após evidência e revisão humana.

Consulte os gates do [START_PROJECT.md](../../06_PLAYBOOKS/START_PROJECT.md).
