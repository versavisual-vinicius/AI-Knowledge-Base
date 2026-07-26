# Instalação local

O repositório é uma fonte única de skills e adapters. Instale somente no
harness que será usado e valide antes de iniciar um projeto.

## Pré-validação pública

Em qualquer ambiente com Git e Python 3:

```bash
git clone https://github.com/versavisual-vinicius/AI-Knowledge-Base.git
cd AI-Knowledge-Base
python3 scripts/validate_knowledge_base.py
python3 scripts/validate_adapters.py
python3 scripts/run_evals.py --smoke
```

Esses comandos não exigem tokens, chamadas de LLM ou dependências npm.

## Codex

Use o plugin Codex local/marketplace ou abra o checkout como projeto. Confirme
com:

```bash
python3 scripts/validate_knowledge_base.py
codex plugin list
```

## Claude Code

No diretório raiz do repositório, carregue o plugin na sessão local:

```bash
claude --plugin-dir "$PWD"
```

Dentro da sessão, confirme as skills com `/help` e recarregue após alterações
com `/reload-plugins`. `CLAUDE.md` é fallback de contexto do projeto; o plugin
é o caminho recomendado para carregar `skills/` e `hooks/hooks.json`.

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

No diretório raiz do repositório, valide a sintaxe e inicie o OpenCode:

```bash
node --check .opencode/plugins/ai-knowledge-base.js
opencode
```

O OpenCode carrega automaticamente plugins JavaScript de
`.opencode/plugins/`; confirme no início da sessão que o bootstrap e as skills
foram carregados.

## Kimi Code

Abra o Kimi no diretório do repositório e instale pelo gerenciador de plugins:

```bash
kimi
```

Na sessão, execute `/plugins install https://github.com/versavisual-vinicius/AI-Knowledge-Base`,
confirme o plugin e reinicie a sessão. O manifesto é `.kimi-plugin/plugin.json`.

## Pi

No diretório raiz do repositório, instale o pacote local no escopo do projeto:

```bash
pi install -l ./
pi list
```

Para testar sem persistir a instalação, use `pi -e ./`. O `package.json`
declara as skills e a extensão `.pi/extensions/ai-knowledge-base.ts`.

## Regra de segurança

Não inserir tokens, chaves, cookies ou credenciais nos arquivos do repositório.
Validar o harness real antes de declarar compatibilidade concluída.

## Empacotamento local

Para gerar um ZIP determinístico do núcleo, execute na raiz do repositório:

```bash
python3 scripts/package_core.py --output /tmp/ai-knowledge-base-core.zip
```

O pacote inclui manifestos, adapters, skills, referências, evals, scripts e
documentação. O diretório `dist/` e artefatos temporários não são incluídos.

## Atualização

Para atualizar um checkout público:

```bash
git pull --ff-only origin main
python3 scripts/validate_knowledge_base.py
python3 scripts/validate_adapters.py
```

Reinicie o harness após atualizar plugins, skills ou hooks.
