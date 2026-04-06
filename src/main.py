from medicamentos import GerenciadorMedicamentos


def menu():
    g = GerenciadorMedicamentos()
    while True:
        print("\nCuidaMed v1.0.0 - Gerenciador de Medicamentos")
        print("1. Adicionar medicamento")
        print("2. Listar medicamentos")
        print("3. Buscar medicamento")
        print("4. Remover medicamento")
        print("0. Sair")

        op = input("\nEscolha uma opção: ")

        if op == "1":
            n = input("Nome: ")
            h = input("Horário inicial (HH:MM): ")
            d = input("Doses por dia: ")
            try:
                g.adicionar(n, h, d)
                print("[+] Medicamento adicionado com sucesso!")
            except Exception as e:
                print(f"[-] Erro ao adicionar: {e}")

        elif op == "2":
            lista = g.listar()
            if not lista:
                print("Nenhum medicamento cadastrado.")
            for m in lista:
                print(f"- {m['nome']}: {m['horario']} ({m['doses_dia']}x ao dia)")

        elif op == "3":
            t = input("Digite o nome ou parte dele: ")
            resultados = g.buscar(t)
            for m in resultados:
                print(f"Encontrado: {m['nome']} as {m['horario']}")

        elif op == "4":
            n = input("Nome do medicamento para remover: ")
            if g.remover(n):
                print("[+] Removido com sucesso.")
            else:
                print("[-] Medicamento nao encontrado.")

        elif op == "0":
            print("Saindo... Cuide-se!")
            break


if __name__ == "__main__":
    menu()