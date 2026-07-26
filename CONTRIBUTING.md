# Contribuindo

## Fluxo

1. Abra uma issue ou descreva o problema antes de uma mudança relevante.
2. Consulte `BOOTSTRAP.md`, `SPEC.md` e `SPEC_PUBLIC_EXPANSION.md`.
3. Confirme se a solução deve estender algo existente antes de criar um novo
   adapter ou skill.
4. Faça uma mudança pequena, com critério de aceite e evidência.
5. Execute os validadores e o smoke test dos evals.
6. Atualize a documentação e explique limitações de runtime.
7. Envie um pull request com resumo, arquivos, testes e pendências.

## Regras

- Não adicione credenciais, transcripts brutos ou dados pessoais.
- Não copie skills, assets ou código de terceiros sem licença e atribuição.
- Não declare compatibilidade de harness sem evidência real.
- Não adicione dependências pagas ou chamadas de LLM ao CI.
- Mudanças de escopo exigem atualização do spec e aprovação humana.

## Validação local

```bash
python3 scripts/validate_knowledge_base.py
python3 scripts/validate_adapters.py
python3 scripts/run_evals.py --smoke
node --check .opencode/plugins/ai-knowledge-base.js
```
