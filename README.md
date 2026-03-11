# CuidaMed

![CI](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml/badge.svg)

Gerenciador de horarios de medicamentos via linha de comando (CLI), voltado para idosos, cuidadores e familiares que precisam organizar rotinas de medicacao de forma simples e confiavel.

---

## Problema Real

No Brasil, erros na administracao de medicamentos sao uma das principais causas de internacoes entre idosos. Esquecer horarios, tomar doses duplicadas ou interromper tratamentos sao situacoes comuns, especialmente quando ha multiplos medicamentos envolvidos. Cuidadores e familiares muitas vezes nao tem uma ferramenta simples para organizar e consultar essa rotina.

## Proposta de Solucao

O CuidaMed oferece uma interface CLI simples para cadastrar, listar, buscar e remover medicamentos com seus respectivos horarios e doses diarias. Os dados sao salvos localmente em um arquivo JSON, sem necessidade de internet ou conta em servico externo.

## Publico-alvo

- Idosos com rotina de medicacao
- Cuidadores e tecnicos de enfermagem domiciliar
- Familiares responsaveis pela medicacao de parentes

---

## Funcionalidades

- Adicionar medicamento com nome, horario e doses por dia
- Listar todos os medicamentos cadastrados
- Remover medicamento por nome
- Buscar medicamento por nome ou parte do nome
- Persistencia de dados em arquivo JSON local

---

## Tecnologias

- Python 3.9+
- pytest — testes automatizados
- ruff — linting e analise estatica
- GitHub Actions — integracao continua (CI)

---

## Instalacao

```bash
git clone https://github.com/HenriMafra/cuidamed.git
cd cuidamed

# Opcional: ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

## Execucao

```bash
python src/main.py
```

Voce vera o menu interativo:

```
CuidaMed v1.0.0 - Gerenciador de Medicamentos

  1. Adicionar medicamento
  2. Listar medicamentos
  3. Remover medicamento
  4. Buscar medicamento
  0. Sair
```

---

## Testes

```bash
pytest tests/ -v
```

---

## Lint

```bash
ruff check src/ tests/
```

---

## Estrutura do Projeto

```
cuidamed/
├── src/
│   ├── main.py
│   └── medicamentos.py
├── tests/
│   └── test_medicamentos.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── CHANGELOG.md
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Versao

1.0.0 — veja CHANGELOG.md

---

## Autor

Henri
Ciencia de Dados e Machine Learning — UniCEUB
3 Semestre — 2026
