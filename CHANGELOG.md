# Changelog

## [1.1.0] - 2026-03-16

### Adicionado
- Integracao com API publica OpenFDA para consulta de informacoes de medicamentos
- Interface web via Streamlit (app.py) com suporte a deploy em nuvem
- Teste de integracao (tests/test_integracao.py) validando comunicacao com API externa
- Nova opcao no menu CLI: "5. Consultar informacoes do medicamento (API)"
- Dependencias: requests, streamlit

## [1.0.0] - 2026-03-09

### Adicionado
- Interface CLI com menu interativo
- Funcionalidades: adicionar, listar, remover e buscar medicamentos
- Persistencia de dados em arquivo JSON local
- Testes automatizados com pytest
- Linting com ruff
- Pipeline de CI com GitHub Actions
