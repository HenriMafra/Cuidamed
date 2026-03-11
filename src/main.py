import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from medicamentos import adicionar, listar, remover, buscar

VERSAO = "1.0.0"

MENU = """
CuidaMed v{versao} - Gerenciador de Medicamentos

  1. Adicionar medicamento
  2. Listar medicamentos
  3. Remover medicamento
  4. Buscar medicamento
  0. Sair

"""


def exibir_menu():
    print(MENU.format(versao=VERSAO))


def cmd_adicionar():
    nome = input("Nome do medicamento: ").strip()
    horario = input("Horario (HH:MM): ").strip()
    try:
        doses = int(input("Doses por dia: ").strip())
    except ValueError:
        print("\nErro: doses por dia deve ser um numero inteiro.")
        return
    try:
        med = adicionar(nome, horario, doses)
        print(f"\n'{med['nome']}' adicionado com sucesso.")
        print(f"Horario: {med['horario']} | {med['doses_por_dia']}x ao dia")
    except ValueError as e:
        print(f"\nErro: {e}")


def cmd_listar():
    meds = listar()
    if not meds:
        print("\nNenhum medicamento cadastrado.")
        return
    print(f"\n{'#':<4} {'Nome':<25} {'Horario':<10} {'Doses/dia'}")
    print("-" * 50)
    for i, m in enumerate(meds, 1):
        print(f"{i:<4} {m['nome']:<25} {m['horario']:<10} {m['doses_por_dia']}x")


def cmd_remover():
    nome = input("Nome do medicamento a remover: ").strip()
    try:
        med = remover(nome)
        print(f"\n'{med['nome']}' removido com sucesso.")
    except ValueError as e:
        print(f"\nErro: {e}")


def cmd_buscar():
    termo = input("Digite o nome ou parte do nome: ").strip()
    resultado = buscar(termo)
    if not resultado:
        print(f"\nNenhum resultado para '{termo}'.")
        return
    print(f"\n{len(resultado)} resultado(s) encontrado(s):")
    print(f"{'Nome':<25} {'Horario':<10} {'Doses/dia'}")
    print("-" * 45)
    for m in resultado:
        print(f"{m['nome']:<25} {m['horario']:<10} {m['doses_por_dia']}x")


def main():
    acoes = {
        "1": cmd_adicionar,
        "2": cmd_listar,
        "3": cmd_remover,
        "4": cmd_buscar,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "0":
            print("\nAte logo.\n")
            break
        elif opcao in acoes:
            acoes[opcao]()
            input("\nPressione Enter para continuar...")
        else:
            print("\nOpcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
