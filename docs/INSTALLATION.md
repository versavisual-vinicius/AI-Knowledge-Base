# Instalação local

O repositório é uma fonte única de skills e adapters. Instale somente no
harness que será usado e valide antes de iniciar um projeto.

## Codex

Use o plugin Codex local/marketplace e confirme com:

```bash
python3 scripts/validate_knowledge_base.py
codex plugin list
```

## Claude Code

Instale o plugin local ou carregue `CLAUDE.md`. Confirme que `skills/` e
`hooks/hooks.json` foram descobertos; reinicie a sessão após atualizar o plugin.

## Antigravity

No diretório do repositório:

```bash
agy plugin validate .
agy plugin install .
```

O segundo comando altera o perfil local do Antigravity e deve ser executado
somente quando a instalação for desejada.

## Gemini CLI

```bash
gemini extensions link .
gemini extensions list
```

O `gemini-extension.json` carrega `GEMINI.md`; reinicie a sessão após alterar a
extensão.

## OpenCode

Carregue o repositório como plugin local. O entrypoint é
`.opencode/plugins/ai-knowledge-base.js` e as skills ficam em `skills/`.

## Kimi Code

Instale o plugin local pelo gerenciador do Kimi e recarregue a sessão. O
manifesto é `.kimi-plugin/plugin.json`.

## Pi

Carregue o repositório como pacote local do Pi. O `package.json` declara as
skills e a extensão `.pi/extensions/ai-knowledge-base.ts`.

## Regra de segurança

Não inserir tokens, chaves, cookies ou credenciais nos arquivos do repositório.
Validar o harness real antes de declarar compatibilidade concluída.
