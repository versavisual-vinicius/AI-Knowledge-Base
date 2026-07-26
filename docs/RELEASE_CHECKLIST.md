# Checklist de release

## Antes da versão

- [ ] SPEC e etapas aprovados humanamente.
- [ ] Duas revisões por etapa e auditoria final registradas.
- [ ] `python3 scripts/validate_knowledge_base.py` passou.
- [ ] `python3 scripts/validate_adapters.py` passou.
- [ ] `python3 scripts/run_evals.py --smoke` passou.
- [ ] `python3 -m unittest discover -s tests` passou.
- [ ] Pacote ZIP reproduzido duas vezes com o mesmo hash.
- [ ] Versões dos manifestos e `package.json` alinhadas.
- [ ] Runtime de cada harness marcado como validado, pendente ou bloqueado.

## Publicação

- [ ] Criar tag semver correspondente à versão aprovada.
- [ ] Anexar o ZIP gerado e suas evidências à release.
- [ ] Publicar somente após aprovação humana explícita.
- [ ] Confirmar checkout limpo e URL pública da release.

## Pós-release

- [ ] Atualizar `RELEASE-NOTES.md` e `CHANGELOG.md`.
- [ ] Registrar limitações e próximos passos.
- [ ] Reabrir o ciclo somente para uma mudança de escopo aprovada.
