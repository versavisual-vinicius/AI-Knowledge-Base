---
name: execucao-orientada-a-spec
description: Conduzir projetos por especificação aprovada, etapas curtas e aprovação humana entre incrementos.
---

# Execução orientada a spec

Use em projetos novos e mudanças relevantes.

1. Crie `SPEC.md` com objetivo, escopo, fora do escopo, requisitos, ferramentas,
   critérios de aceite e aprovação.
2. Aguarde revisão e aprovação humana; `Approved` é obrigatório.
3. Divida em etapas de objetivo único e resultado observável.
4. Nunca crie etapas longas como “implementar o sistema”.
5. Execute uma etapa por vez, estritamente dentro do spec.
6. Valide, registre evidências e aguarde aprovação humana da etapa.
7. Se surgir mudança de escopo, pause e atualize o spec antes de continuar.

Use o playbook [START_PROJECT.md](../../06_PLAYBOOKS/START_PROJECT.md) e o
modelo [project-spec-template.md](../../references/project-spec-template.md).
