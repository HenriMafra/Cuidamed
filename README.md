# ARQUIVO DE ENTREGA FINAL - PROJETO CUIDAMED

# 1. INFORMAÇÕES PARA O PDF DE ENTREGA (COPIAR E COLAR NO SEU DOCUMENTO)
# -----------------------------------------------------------------------
# Nome: Henri Felipe Marques Mafra
# Disciplina: Bootcamp Entrega Inicial - Etapa 1
# Projeto: CuidaMed
# Resumo: Aplicação CLI em Python para gestão de medicamentos voltada a idosos e cuidadores. 
# Resolve a dor do esquecimento e erro de dosagem através de persistência local em JSON, 
# contando com testes automatizados e pipeline de CI (GitHub Actions).
# Link do Repositório: https://github.com/HenriMafra/cuidamed
# -----------------------------------------------------------------------

# 2. CONTEÚDO INTEGRAL DOS ARQUIVOS DO REPOSITÓRIO (README, CÓDIGO, TESTES, CI)

# --- ARQUIVO: README.md ---
# # CuidaMed
# 
# ![CI](https://github.com/HenriMafra/cuidamed/actions/workflows/ci.yml/badge.svg)
# 
# Gerenciador de horarios de medicamentos via linha de comando (CLI), voltado para idosos, cuidadores e familiares que precisam organizar rotinas de medicacao de forma simples e confiavel.
# 
# ---
# 
# ## Problema Real
# 
# No Brasil, erros na administracao de medicamentos sao uma das principais causas de internacoes entre idosos. Esquecer horarios, tomar doses duplicadas ou interromper tratamentos sao situacoes comuns, especialmente quando ha multiplos medicamentos envolvidos. Cuidadores e familiares muitas vezes nao tem uma ferramenta simples para organizar e consultar essa rotina.
# 
# ## Proposta de Solução
# 
# O CuidaMed oferece uma interface CLI simples para cadastrar, listar, buscar e remover medicamentos com seus respectivos horarios e doses diarias. Os dados sao salvos localmente em um arquivo JSON, garantindo a privacidade dos dados de saude e o funcionamento offline, sem necessidade de internet ou conta em servico externo.
# 
# ## Publico-alvo
# 
# - Idosos com rotina de medicacao ativa
# - Cuidadores e tecnicos de enfermagem domiciliar
# - Familiares responsaveis pela medicacao de parentes
# 
# ---
# 
# ## Funcionalidades
# 
# - Adicionar medicamento com nome, horario inicial e doses por dia
# - Listar todos os medicamentos cadastrados de forma organizada
# - Remover medicamento por nome para encerrar tratamentos
# - Buscar medicamento por nome ou parte do nome
# - Persistencia automatica de dados em arquivo JSON local
# 
# ---
# 
# ## Tecnologias
# 
# - Python 3.9+
# - pytest — testes automatizados
# - ruff — linting e analise estatica
# - GitHub Actions — integracao continua (CI)
# 
# ---
# 
# ## Instalação
# 
# ```bash
# git clone [https://github.com/HenriMafra/cuidamed.git](https://github.com/HenriMafra/cuidamed.git)
# cd cuidamed
# python -m venv venv
# source venv/bin/activate
# # No Windows: venv\Scripts\activate
# pip install -r requirements.txt
# ```
# 
# ---
# 
# ## Execucão
# 
# ```bash
# python src/main.py
# ```
# 
# Voce vera o menu interativo:
# 
# ```
# CuidaMed v1.0.0 - Gerenciador de Medicamentos
# 
#   1. Adicionar medicamento
#   2. Listar medicamentos
#   3. Remover medicamento
#   4. Buscar medicamento
#   0. Sair
# ```
# 
# ### Exemplo de Uso (Demonstração):
# 
# ```text
# Escolha uma opção: 1
# Nome do Medicamento: Dipirona
# Horário da primeira dose: 08:00
# Doses por dia: 3
# 
# [+] 'Dipirona' adicionado com sucesso! Dados salvos localmente.
# ```
# 
# ---
# 
# ## Testes
# 
# ```bash
# pytest tests/ -v
# ```
# 
# ---
# 
# ## Lint
# 
# ```bash
# ruff check src/ tests/
# ```
# 
# ---
# 
# ## Estrutura do Projeto
# 
# ```
# cuidamed/
# ├── src/
# │   ├── main.py
# │   └── medicamentos.py
# ├── tests/
# │   └── test_medicamentos.py
# ├── .github/
# │   └── workflows/
# │       └── ci.yml
# ├── .gitignore
# ├── CHANGELOG.md
# ├── pyproject.toml
# ├── requirements.txt
# └── README.md
# ```
# 
# ---
# 
# ## Versão
# 
# 1.0.0 — Padrão Semântico MAJOR.MINOR.PATCH (veja CHANGELOG.md)
# 
# ---
# 
# ## Licença
# 
# Este projeto está sob a Licença MIT.
# 
# ---
# 
# ## Autor
# 
# Henri Felipe Marques Mafra
# Ciencia de Dados e Machine Learning — UniCEUB
# 3 Semestre — 2026
# Brasília, DF - Brasil

# --- ARQUIVO: .github/workflows/ci.yml ---
# name: CI
# on:
#   push:
#     branches: [ main, master ]
#   pull_request:
#     branches: [ main, master ]
# jobs:
#   build:
#     runs-on: ubuntu-latest
#     steps:
#     - uses: actions/checkout@v4
#     - name: Set up Python
#       uses: actions/setup-python@v5
#       with:
#         python-version: '3.10'
#     - name: Install dependencies
#       run: |
#         python -m pip install --upgrade pip
#         pip install -r requirements.txt
#     - name: Run Linting (Ruff)
#       run: ruff check src/ tests/
#     - name: Run Tests (Pytest)
#       run: pytest tests/

# --- ARQUIVO: src/medicamentos.py ---
# import json
# import os
# class GerenciadorMedicamentos:
#     def __init__(self, db_path='medicamentos.json'):
#         self.db_path = db_path
#         self.medicamentos = self._carregar_dados()
#     def _carregar_dados(self):
#         if os.path.exists(self.db_path):
#             with open(self.db_path, 'r', encoding='utf-8') as f:
#                 return json.load(f)
#         return []
#     def _salvar_dados(self):
#         with open(self.db_path, 'w', encoding='utf-8') as f:
#             json.dump(self.medicamentos, f, indent=4, ensure_ascii=False)
#     def adicionar(self, nome, horario, doses):
#         if not nome or not horario or int(doses) <= 0:
#             raise ValueError("Dados inválidos para cadastro.")
#         medicamento = {"nome": nome, "horario": horario, "doses_dia": int(doses)}
#         self.medicamentos.append(medicamento)
#         self._salvar_dados()
#         return True
#     def listar(self):
#         return self.medicamentos
#     def remover(self, nome):
#         inicial = len(self.medicamentos)
#         self.medicamentos = [m for m in self.medicamentos if m['nome'].lower() != nome.lower()]
#         if len(self.medicamentos) < inicial:
#             self._salvar_dados()
#             return True
#         return False
#     def buscar(self, termo):
#         return [m for m in self.medicamentos if termo.lower() in m['nome'].lower()]

# --- ARQUIVO: src/main.py ---
# from medicamentos import GerenciadorMedicamentos
# def menu():
#     g = GerenciadorMedicamentos()
#     while True:
#         print("\nCuidaMed v1.0.0 - Gerenciador de Medicamentos")
#         print("1. Adicionar medicamento\n2. Listar medicamentos\n3. Buscar medicamento\n4. Remover medicamento\n0. Sair")
#         op = input("Escolha uma opção: ")
#         if op == '1':
#             n = input("Nome: "); h = input("Horário (HH:MM): "); d = input("Doses/dia: ")
#             try: g.adicionar(n, h, d); print("[+] Adicionado!")
#             except Exception as e: print(f"[-] Erro: {e}")
#         elif op == '2':
#             for m in g.listar(): print(f"{m['nome']} - {m['horario']} ({m['doses_dia']} doses/dia)")
#         elif op == '3':
#             t = input("Termo de busca: ")
#             for m in g.buscar(t): print(f"Encontrado: {m['nome']} às {m['horario']}")
#         elif op == '4':
#             n = input("Nome para remover: ")
#             if g.remover(n): print("[+] Removido!")
#             else: print("[-] Não encontrado.")
#         elif op == '0': break
# if __name__ == "__main__": menu()

# --- ARQUIVO: tests/test_medicamentos.py ---
# import pytest
# from src.medicamentos import GerenciadorMedicamentos
# @pytest.fixture
# def gerenciador(tmp_path):
#     d = tmp_path / "test_db.json"
#     return GerenciadorMedicamentos(str(d))
# def test_adicionar_medicamento_sucesso(gerenciador):
#     assert gerenciador.adicionar("Dipirona", "08:00", 3) is True
#     assert len(gerenciador.listar()) == 1
# def test_adicionar_medicamento_invalido(gerenciador):
#     with pytest.raises(ValueError):
#         gerenciador.adicionar("", "08:00", -1)
# def test_remover_medicamento(gerenciador):
#     gerenciador.adicionar("Remover", "10:00", 1)
#     assert gerenciador.remover("Remover") is True
#     assert len(gerenciador.listar()) == 0

# --- ARQUIVO: requirements.txt ---
# pytest==8.0.0
# ruff==0.3.0

# --- ARQUIVO: pyproject.toml ---
# [tool.ruff]
# line-length = 88
# select = ["E", "F", "W"]
# [tool.pytest.ini_options]
# pythonpath = ["."]

# --- ARQUIVO: CHANGELOG.md ---
# # Changelog
# ## [1.0.0] - 2026-04-06
# - Versão inicial funcional com CLI, JSON e CI.
