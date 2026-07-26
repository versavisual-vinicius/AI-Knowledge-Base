# Matriz de gap público

- Spec: `SPEC_PUBLIC_EXPANSION.md`
- Status: Approved — P1 approved by Vini, 2026-07-26
- Referência comparativa: [obra/superpowers](https://github.com/obra/superpowers)

Esta matriz compara maturidade pública e operacional. Não é autorização para
copiar estrutura, skills, assets ou código de terceiros.

| Área | Estado atual | Gap | Prioridade | Decisão |
|---|---|---|---|---|
| Fonte de verdade e bootstrap | Implementado | Nenhum estrutural | Manter | Preservar `BOOTSTRAP.md`, `SPEC.md` e skills próprias |
| Skills de governança VersaVisual | 5 skills implementadas | Cobertura menor que frameworks gerais | P5 | Expandir só por dor confirmada |
| Adapters | 7 adapters documentados | Runtime pendente em 5 harnesses | P4 | Aceitar evidência dos usuários; não declarar compatibilidade antecipada |
| Manifestos e instalação | Manifests locais e guia existem | Metadados públicos e atualização podem ser mais claros | P2 | Completar sem marketplace obrigatório |
| Testes determinísticos | Validadores, smoke eval e CI existem | Falta suíte `tests/` com falhas intencionais | P3 | Criar testes sem chamadas de LLM |
| Evals comportamentais | 14 casos e executor existem | Falta coleta end-to-end por harness | P4 | Usar transcripts sanitizados dos usuários |
| Runtime Codex/Antigravity | Evidência local registrada | Melhorar transcripts/reprodução | P4 | Registrar evidência mínima reproduzível |
| Runtime dos demais harnesses | Não executado localmente | Sem evidência de runtime | P4 | Marcar `pending` até contribuição real |
| README e onboarding | Documentação funcional | Falta porta de entrada pública mais completa | P2/P6 | Explicar problema, limites, instalação e exemplos |
| Licença e terceiros | MIT própria e aviso Superpowers | Falta política pública de contribuição externa | P2/P7 | Criar regras de origem/licença |
| Releases e versionamento | Versão em manifests e ZIP local | Falta changelog e release reproduzível | P2/P7 | Adicionar release notes e checklist |
| Segurança e contribuição | Regras internas existentes | Faltam documentos públicos dedicados | P2 | Criar somente conteúdo aplicável |
| Assets e identidade | Sem assets próprios relevantes | Falta apresentação visual opcional | P6 | Criar somente se melhorar descoberta/compreensão |
| CI | Workflow público sem custo e sem segredos | Nenhum gap obrigatório | Manter | Não incluir chamadas pagas |
| Marketplace/registry | Não publicado | Distribuição ainda manual por GitHub/ZIP | Opcional | Só publicar após demanda e aprovação |
| Subagentes/worktrees/TDD geral | Não incluídos | Não são necessários ao núcleo atual | Rejeitado por enquanto | Não importar metodologia inteira do Superpowers |

## Prioridade de execução

1. P1: esta matriz e o contrato público;
2. P2: metadados, releases, segurança, contribuição e instalação;
3. P3: testes determinísticos negativos e cobertura de contratos;
4. P4: evidências de runtime e evals end-to-end por harness;
5. P5: skills adicionais somente com dor comprovada;
6. P6: README público, exemplos e identidade própria;
7. P7: release reproduzível e rotina de manutenção.

## Gate de aprovação

Esta matriz não aprova nenhuma implementação. Vini deve confirmar:

- prioridades e itens rejeitados;
- escopo de suporte público;
- se a expansão deve continuar focada na VersaVisual ou aceitar contribuições
  externas;
- autorização para iniciar P2.
