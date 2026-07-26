# SPEC — Expansão pública e maturidade multiplataforma

- Data: 2026-07-26
- Status: Draft — Pending Approval
- Repositório canônico: `versavisual-vinicius/AI-Knowledge-Base`
- Spec base: `SPEC.md`
- Referência comparativa: `obra/superpowers`

## Objetivo

Elevar o núcleo aprovado da AI Knowledge Base ao nível de um pacote público
reutilizável, testável e mantido, preservando o foco nas dores operacionais da
VersaVisual e evitando copiar integralmente metodologias ou assets de terceiros.

## Resultado esperado

- instalação pública clara e versionada;
- testes determinísticos de infraestrutura;
- evidências de runtime por harness, sem prometer compatibilidade não testada;
- documentação de contribuição, segurança e releases;
- skills adicionais somente quando resolverem uma dor confirmada;
- identidade visual e assets próprios ou devidamente licenciados.

## Fora do escopo

- copiar a estrutura ou as skills do Superpowers;
- incorporar assets, código ou textos de terceiros sem atribuição;
- criar suporte artificial para harnesses não testados;
- adicionar subagentes, worktrees, servidor web ou serviços pagos como requisito;
- executar chamadas de LLM pagas em CI;
- publicar automaticamente em marketplaces ou registries.

## Regras de execução

- Cada etapa tem objetivo único, resultado observável e duração curta.
- Nenhuma etapa inicia sem aprovação humana da etapa anterior.
- Cada etapa terá duas revisões: conformidade com o spec e qualidade/evidência.
- Mudança de escopo exige atualização e nova aprovação deste spec.
- Runtime de harness ausente será validado por contribuição do usuário, com
  transcript sanitizado e resultado do `scripts/run_evals.py`.

## Etapas propostas

### Etapa P1 — Fechamento do gap público

- Mapear cada diferença entre o núcleo atual e o pacote público desejado.
- Classificar item como obrigatório, útil, opcional ou rejeitado.
- Definir o contrato público de instalação, versão e suporte.
- Aceite: matriz de gap aprovada e sem cópia indevida de terceiros.

### Etapa P2 — Metadados, releases e instalação pública

- Completar metadados de homepage, repositório, licença, keywords e versão.
- Criar `RELEASE-NOTES.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md` e guia de
  contribuição somente com conteúdo pertinente ao projeto.
- Documentar instalação pública e atualização por harness.
- Aceite: uma pessoa nova consegue instalar, validar e identificar a versão.

### Etapa P3 — Suíte determinística de testes

- Criar `tests/` para manifestos, links, hooks, empacotamento e contratos.
- Cobrir falhas intencionais: arquivo ausente, JSON inválido, placeholder,
  hook sem saída JSON e pacote incompleto.
- Integrar os testes ao GitHub Actions sem chamadas de LLM.
- Aceite: testes reproduzíveis falham quando o contrato é quebrado.

### Etapa P4 — Evidência de runtime por harness

- Registrar transcript mínimo e resultado dos evals para Codex e Antigravity.
- Criar um formato de contribuição para Claude, Gemini CLI, OpenCode, Kimi e
  Pi, executado pelos usuários que possuírem esses harnesses.
- Marcar cada harness como `runtime validated`, `pending` ou `blocked`.
- Aceite: nenhuma matriz declara runtime sem transcript e evidência correspondente.

### Etapa P5 — Expansão seletiva de skills

- Auditar dores reais ainda não cobertas.
- Priorizar apenas skills com benefício claro, como planejamento, debugging,
  TDD ou code review adaptados às regras da VersaVisual.
- Criar uma skill por dor, com metadata, caso de eval e documentação curta.
- Aceite: cada nova skill tem caso real, não duplica uma existente e passa nos
  validadores.

### Etapa P6 — Documentação pública e identidade própria

- Reescrever o README como porta de entrada pública: problema, instalação,
  limites, exemplos e contribuição.
- Criar assets próprios mínimos, se necessários, e screenshots reais apenas
  quando melhorarem a compreensão.
- Registrar origem, licença e caminho de qualquer material externo.
- Aceite: documentação permite avaliar o projeto sem conhecer a conversa interna.

### Etapa P7 — Release e manutenção

- Definir checklist de release, versionamento semântico e changelog.
- Gerar pacote local/release e validar o artefato final.
- Publicar somente após aprovação humana explícita.
- Aceite: release reproduzível, evidências anexadas e pendências declaradas.

## Critérios globais de aceite

- O núcleo VersaVisual continua sendo a fonte de verdade.
- Nenhum harness é declarado compatível apenas por possuir um manifesto.
- CI permanece sem chamadas pagas ou segredos.
- Toda contribuição externa possui licença e origem verificáveis.
- Cada etapa possui duas revisões registradas antes da aprovação.

## Aprovação humana

- Revisor: Vini
- Status: Approved — P1, P2, P3, P4, P5 e P6 aprovadas por Vini, 2026-07-26
- Observações: auditoria final dupla P1–P6 concluída em 2026-07-26; publicação
  continua condicionada a autorização explícita.
  a revisão e aprovação humana próprias.

## Estado das etapas

- P1 — Fechamento do gap público: Approved — Vini, 2026-07-26
- P2 — Metadados, releases e instalação pública: Approved — Vini, 2026-07-26
- P3 — Testes determinísticos e evals públicos: Approved — Vini, 2026-07-26
- P4 — Evidência de runtime por harness: Approved — Vini, 2026-07-26
- P5 — Expansão seletiva de skills: Approved — Vini, 2026-07-26
- P6 — Documentação pública e identidade própria: Approved — Vini, 2026-07-26
- P7 — Release e manutenção: Prepared — release 0.3.0 local, 2026-07-26

## Auditoria final P1–P6

- Passagem 1: contratos, 6 skills, 7 adapters, 15/15 evals, 5 testes, sintaxe
  OpenCode e estados das etapas validados.
- Passagem 2: pacote reproduzido deterministicamente, 60 arquivos obrigatórios
  conferidos e diff sem inconsistências.
- Resultado: todas as etapas P1–P6 aprovadas e P7 preparada localmente; a
  publicação da release e a manutenção contínua permanecem condicionadas.
