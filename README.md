# CuidaMed

![CI](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml/badge.svg)

Gerenciador de horarios de medicamentos via linha de comando (CLI), voltado para idosos, cuidadores e familiares que precisam organizar rotinas de medicacao de forma simples e confiavel.

---

## Problema Real

No Brasil, erros na administracao de medicamentos sao uma das principais causas de internacoes entre idosos. Esquecer horarios, tomar doses duplicadas ou interromper tratamentos sao situacoes comuns, especialmente quando ha multiplos medicamentos envolvidos. Cuidadores e familiares muitas vezes nao tem uma ferramenta simples para organizar e consultar essa rotina.

## Proposta de Solução

O CuidaMed oferece uma interface CLI simples para cadastrar, listar, buscar e remover medicamentos com seus respectivos horarios e doses diarias. Os dados sao salvos localmente em um arquivo JSON, garantindo a privacidade dos dados de saude e o funcionamento offline, sem necessidade de internet ou conta em servico externo.

## Publico-alvo

- Idosos com rotina de medicacao ativa
- Cuidadores e tecnicos de enfermagem domiciliar
- Familiares responsaveis pela medicacao de parentes

---

## Funcionalidades

- Adicionar medicamento com nome, horario inicial e doses por dia
- Listar todos os medicamentos cadastrados de forma organizada
- Remover medicamento por nome para encerrar tratamentos
- Buscar medicamento por nome ou parte do nome
- Persistencia automatica de dados em arquivo JSON local

---

## Tecnologias

- Python 3.9+
- pytest — testes automatizados
- ruff — linting e analise estatica
- GitHub Actions — integracao continua (CI)

---

## Instalação

Para configurar o projeto localmente, utilize:

git clone https://github.com/HenriMafra/cuidamed.git
cd cuidamed
python -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate (Windows)
pip install -r requirements.txt

---

## Execucão

Para iniciar a aplicacao:
python src/main.py

Exemplo de interacao no terminal:

CuidaMed v1.0.0 - Gerenciador de Medicamentos
1. Adicionar medicamento
2. Listar medicamentos
3. Remover medicamento
4. Buscar medicamento
0. Sair

Escolha uma opção: 1
Nome do Medicamento: Dipirona
Horário da primeira dose: 08:00
Doses por dia: 3

[+] 'Dipirona' adicionado com sucesso! Dados salvos localmente.

---

## Testes

Comando para rodar os testes:
pytest tests/ -v

---

## Lint

Comando para rodar a analise estatica:
ruff check src/ tests/

---

## Estrutura do Projeto

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

---

## Versão

1.0.0 — Padrão Semântico MAJOR.MINOR.PATCH (veja CHANGELOG.md)

---

## Licença

Este projeto está sob a Licença MIT.

---

## Autor

Henri Felipe Marques Mafra
Ciencia de Dados e Machine Learning — UniCEUB
3 Semestre — 2026
Brasília, DF - Brasil
