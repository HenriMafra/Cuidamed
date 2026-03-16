# CuidaMed

[![CI](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml/badge.svg)](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml)

Gerenciador de horarios de medicamentos via linha de comando (CLI) e interface web, voltado para idosos, cuidadores e familiares que precisam organizar rotinas de medicacao de forma simples e confiavel.

**Aplicacao publicada:** [COLE O LINK DO DEPLOY AQUI]

---

## Problema Real

No Brasil, erros na administracao de medicamentos sao uma das principais causas de internacoes entre idosos. Esquecer horarios, tomar doses duplicadas ou interromper tratamentos sao situacoes comuns, especialmente quando ha multiplos medicamentos envolvidos. Cuidadores e familiares muitas vezes nao tem uma ferramenta simples para organizar e consultar essa rotina.

## Proposta de Solucao

O CuidaMed oferece uma interface CLI simples e uma interface web (Streamlit) para cadastrar, listar, buscar e remover medicamentos com seus respectivos horarios e doses diarias. A versao 1.1.0 adiciona integracao com a API publica OpenFDA para consultar informacoes tecnicas sobre medicamentos. Os dados sao salvos localmente em um arquivo JSON, sem necessidade de internet ou conta em servico externo.

## Publico-alvo

* Idosos com rotina de medicacao
* Cuidadores e tecnicos de enfermagem domiciliar
* Familiares responsaveis pela medicacao de parentes

---

## Funcionalidades

* Adicionar medicamento com nome, horario e doses por dia
* Listar todos os medicamentos cadastrados
* Remover medicamento por nome
* Buscar medicamento por nome ou parte do nome
* Persistencia de dados em arquivo JSON local
* **[NOVO]** Consultar informacoes de medicamentos via API publica OpenFDA
* **[NOVO]** Interface web disponivel online via Streamlit

---

## Tecnologias

* Python 3.9+
* requests — consumo de API REST (OpenFDA)
* streamlit — interface web para deploy
* pytest — testes automatizados
* ruff — linting e analise estatica
* GitHub Actions — integracao continua (CI)

---

## Instalacao

```
git clone https://github.com/HenriMafra/cuidamed.git
cd cuidamed

# Opcional: ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

## Execucao CLI

```
python src/main.py
```

Voce vera o menu interativo:

```
CuidaMed v1.1.0 - Gerenciador de Medicamentos

  1. Adicionar medicamento
  2. Listar medicamentos
  3. Remover medicamento
  4. Buscar medicamento
  5. Consultar informacoes do medicamento (API)
  0. Sair
```

## Execucao Web (local)

```
streamlit run app.py
```

---

## Testes

```
pytest tests/ -v
```

---

## Lint

```
ruff check src/ tests/
```

---

## API Utilizada

**OpenFDA** — base de dados publica da Food and Drug Administration (EUA).

* Endpoint: `https://api.fda.gov/drug/label.json`
* Sem necessidade de chave de API
* Retorna: nome generico, fabricante, via de administracao, indicacoes e advertencias

---

## Estrutura do Projeto

```
cuidamed/
├── src/
│   ├── main.py
│   ├── medicamentos.py
│   └── api.py
├── tests/
│   ├── test_medicamentos.py
│   └── test_integracao.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── .gitignore
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Versao

1.1.0 — veja CHANGELOG.md

---

## Autor

Henri
Ciencia de Dados e Machine Learning — UniCEUB
3 Semestre — 2026
