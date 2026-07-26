# Matriz de compatibilidade — núcleo inicial

Status desta etapa: `Approved`; os sete adapters foram implementados e
validados estruturalmente. A validação em runtime ainda depende da instalação
de cada harness.

| Harness | Bootstrap previsto | Skills nativas | Hooks/extensão | Estado |
|---|---|---:|---:|---|
| Codex | plugin manifest + `BOOTSTRAP.md` | Sim | Plugin | Implemented; runtime validated |
| Claude Code | `CLAUDE.md` ou plugin | Sim | Configuração/plugin | Implemented; runtime pending |
| Antigravity | extensão ou instrução de sessão | A confirmar | Extensão | Implemented; runtime validated |
| Gemini CLI | `GEMINI.md` ou extensão | A confirmar | Extensão | Implemented; runtime pending |
| OpenCode | instrução de instalação própria | A confirmar | Plugin | Implemented; runtime pending |
| Kimi | plugin ou comando de instalação | A confirmar | Plugin | Implemented; runtime pending |
| Pi | pacote com skills | Sim | Extensão opcional | Implemented; runtime pending |

## Regras de validação

- validar cada adapter no harness real ou declarar `Blocked`;
- não declarar compatibilidade apenas por existir um arquivo de configuração;
- testar bootstrap, seleção de skill e leitura do `SPEC.md`;
- testar o caso de bloqueio: construção sem aprovação deve parar;
- registrar limitações e evidências por harness;
- manter o núcleo agnóstico de fornecedor.

## Próxima etapa autorizável

Executar a validação em runtime nos harnesses ainda pendentes, sem adicionar
workflows específicos, assets ou automações de publicação.
