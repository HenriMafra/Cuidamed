import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from medicamentos import (
    carregar_medicamentos,
    salvar_medicamentos,
    adicionar_medicamento,
    listar_medicamentos,
    remover_medicamento,
    buscar_medicamento,
)
from api import buscar_info_medicamento, formatar_info


def menu():
    print("\n" + "=" * 45)
    print("  CuidaMed v1.1.0 - Gerenciador de Medicamentos")
    print("=" * 45)
    print("  1. Adicionar medicamento")
    print("  2. Listar medicamentos")
    print("  3. Remover medicamento")
    print("  4. Buscar medicamento")
    print("  5. Consultar informações do medicamento (API)")
    print("  0. Sair")
    print("=" * 45)


def main():
    medicamentos = carregar_medicamentos()

    while True:
        menu()
        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("  Nome do medicamento: ").strip()
            horario = input("  Horário (ex: 08:00): ").strip()
            while True:
                try:
                    doses = int(input("  Doses por dia: ").strip())
                    break
                except ValueError:
                    print("  Digite um número válido.")
            medicamentos = adicionar_medicamento(medicamentos, nome, horario, doses)
            salvar_medicamentos(medicamentos)
            print(f"\n  '{nome}' adicionado com sucesso!")

        elif opcao == "2":
            resultado = listar_medicamentos(medicamentos)
            print("\n" + resultado)

        elif opcao == "3":
            nome = input("  Nome do medicamento a remover: ").strip()
            medicamentos, removido = remover_medicamento(medicamentos, nome)
            if removido:
                salvar_medicamentos(medicamentos)
                print(f"\n  '{nome}' removido com sucesso!")
            else:
                print(f"\n  '{nome}' não encontrado.")

        elif opcao == "4":
            termo = input("  Buscar por nome: ").strip()
            encontrados = buscar_medicamento(medicamentos, termo)
            if encontrados:
                print(f"\n  {len(encontrados)} resultado(s) encontrado(s):")
                for m in encontrados:
                    print(f"  - {m['nome']} | {m['horario']} | {m['doses_por_dia']}x/dia")
            else:
                print("\n  Nenhum medicamento encontrado.")

        elif opcao == "5":
            nome = input("  Nome do medicamento para consultar: ").strip()
            print("\n  Consultando OpenFDA...")
            info = buscar_info_medicamento(nome)
            if info:
                print(formatar_info(info))
            else:
                print(f"\n  Nenhuma informação encontrada para '{nome}' na base OpenFDA.")

        elif opcao == "0":
            print("\n  Encerrando CuidaMed. Até logo!\n")
            break

        else:
            print("\n  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
