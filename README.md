# CuidaMed

[![CI](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml/badge.svg)](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml)

Gerenciador de horários de medicamentos via linha de comando (CLI) e interface web, voltado para idosos, cuidadores e familiares que precisam organizar rotinas de medicação de forma simples e confiável.

**Aplicação publicada:** [https://cuidamed.streamlit.app/](https://cuidamed.streamlit.app/)

---

## Problema Real

No Brasil, erros na administração de medicamentos são uma das principais causas de internações entre idosos. Esquecer horários, tomar doses duplicadas ou interromper tratamentos são situações comuns, especialmente quando há múltiplos medicamentos envolvidos. Cuidadores e familiares muitas vezes não têm uma ferramenta simples para organizar e consultar essa rotina.

## Proposta de Solução

O CuidaMed oferece uma interface CLI simples e uma interface web (Streamlit) para cadastrar, listar, buscar e remover medicamentos com seus respectivos horários e doses diárias. A versão 1.1.0 adiciona integração com a API pública OpenFDA para consultar informações técnicas sobre medicamentos. Os cadastros do usuário são salvos localmente em um arquivo JSON (garantindo o funcionamento offline e a privacidade), enquanto a consulta avançada de bulas via API exige conexão com a internet.

## Público-alvo

* Idosos com rotina de medicação
* Cuidadores e técnicos de enfermagem domiciliar
* Familiares responsáveis pela medicação de parentes

---

## Funcionalidades

* Adicionar medicamento com nome, horário e doses por dia
* Listar todos os medicamentos cadastrados de forma organizada
* Remover medicamento por nome para encerrar tratamentos
* Buscar medicamento por nome ou parte do nome
* Persistência automática de dados em arquivo JSON local
* **[NOVO]** Consultar informações de medicamentos via API pública OpenFDA
* **[NOVO]** Interface web disponível online via Streamlit

---

## Tecnologias

* Python 3.9+
* requests — consumo de API REST (OpenFDA)
* streamlit — interface web para deploy
* pytest — testes automatizados
* ruff — linting e análise estática
* GitHub Actions — integração contínua (CI)

---

## Instalação

Para configurar o projeto localmente, utilize:

```bash
git clone [https://github.com/HenriMafra/cuidamed.git](https://github.com/HenriMafra/cuidamed.git)
cd cuidamed

# Opcional: ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
Execução CLI
Para iniciar a aplicação no terminal:

Bash
python src/main.py
Você verá o menu interativo:

Plaintext
CuidaMed v1.1.0 - Gerenciador de Medicamentos

  1. Adicionar medicamento
  2. Listar medicamentos
  3. Remover medicamento
  4. Buscar medicamento
  5. Consultar informações do medicamento (API)
  0. Sair
Execução Web (local)
Para rodar a interface web na sua máquina:

Bash
streamlit run app.py
Testes
Comando para rodar os testes:

Bash
pytest tests/ -v
Lint
Comando para rodar a análise estática:

Bash
ruff check src/ tests/
API Utilizada
OpenFDA — base de dados pública da Food and Drug Administration (EUA).

Endpoint: https://api.fda.gov/drug/label.json

Sem necessidade de chave de API

Retorna: nome genérico, fabricante, via de administração, indicações e advertências

Estrutura do Projeto
Plaintext
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
Versão
1.1.0 — Padrão Semântico MAJOR.MINOR.PATCH (veja CHANGELOG.md)

Licença
Este projeto está sob a Licença MIT.

Autor
Henri Felipe Marques Mafra
Ciência de Dados e Machine Learning — UniCEUB
3º Semestre — 2026
Brasília, DF - Brasil
