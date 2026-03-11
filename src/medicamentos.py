import json
import os
from datetime import datetime

ARQUIVO = "dados.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(medicamentos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(medicamentos, f, ensure_ascii=False, indent=2)


def adicionar(nome, horario, doses_por_dia):
    if not nome or not nome.strip():
        raise ValueError("Nome do medicamento não pode ser vazio.")
    if doses_por_dia <= 0:
        raise ValueError("Doses por dia deve ser maior que zero.")
    try:
        datetime.strptime(horario, "%H:%M")
    except ValueError:
        raise ValueError("Horário inválido. Use o formato HH:MM.")

    medicamentos = carregar_dados()
    medicamento = {
        "nome": nome.strip(),
        "horario": horario,
        "doses_por_dia": doses_por_dia,
    }
    medicamentos.append(medicamento)
    salvar_dados(medicamentos)
    return medicamento


def listar():
    return carregar_dados()


def remover(nome):
    medicamentos = carregar_dados()
    encontrado = [m for m in medicamentos if m["nome"].lower() == nome.lower()]
    if not encontrado:
        raise ValueError(f"Medicamento '{nome}' não encontrado.")
    atualizados = [m for m in medicamentos if m["nome"].lower() != nome.lower()]
    salvar_dados(atualizados)
    return encontrado[0]


def buscar(nome):
    medicamentos = carregar_dados()
    resultado = [m for m in medicamentos if nome.lower() in m["nome"].lower()]
    return resultado
