# Antigravity

- Versão mínima conhecida: Antigravity com suporte a extensões locais.
- Integração: `plugin.json`, `hooks.json`, `skills/` e `hooks/session-start`.
- Bootstrap: extensão ou instrução de sessão apontando para `BOOTSTRAP.md`.
- Fonte: `skills/`, `00_SYSTEM/` e `SPEC.md`; referências em `references/`.
- Instalação local: usar o mecanismo de plugin/extensão local do Antigravity.
- Validação: executar `agy plugin install <caminho-local>` em ambiente de teste,
  verificar bootstrap, seleção de skill e parada sem aprovação.
- Limitação atual: formato final da extensão depende da versão instalada.
- Estado: Draft — manifest e hook local implementados; CLI ainda não validado.
