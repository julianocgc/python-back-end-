# Inventário
# 1 - Cadastrar novos produtos
# 2 - Atualizar  a quantidade
# 3 - Consultar o estoque

def exibir_menu():
    print("--- Sistema de Inventário ---")
    print("1. Adicionar um Produto")
    print("2. Autalizar a Quantidade de um Produto")
    print("3. Consultar o Estoque")
    print("4. Sair")
    
    return input("Escolha uma opção: ")

def adicionar_produto(inventario):
    produto = input("Digite o nome do Produto: ")

    if produto in inventario:
        print(f"O produto {produto} já está cadastrado...")
    else:
        quantidade = int(input("Digite a quantidade inicial do produto: "))

        inventario[produto] = quantidade

        print(f"O produto {produto} foi adicionado!")

def atualizar_quantidade(inventario):
    produto = input("Digite o nome do Produto para atualizar: ")

    if produto not in inventario:
        print(f"O produto {produto} não existe...")
    else:
        quantidade = int(input("Digite a quantidade atual do produto: "))

        inventario[produto] = quantidade

        print(f"O produto {produto} foi atualizado!")


def consultar_estoque(inventario):
    if not inventario:
        print("O estoque está vázio...")
    else:
        print("-- Estoque Atual ---")
        for produto, quantidade in inventario.items():
            print(f"{produto}: {quantidade} unidades")


def main():
    inventario = {}

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            print("Adicionar produto")
            adicionar_produto(inventario)
        elif opcao == "2":
            print("Atualizar Quantidade")
            atualizar_quantidade(inventario)
        elif opcao == "3":
            print("Verificar Estoque")
            consultar_estoque(inventario)
        elif opcao == "4":
            print("Encerrando Sistema de Inventário. Até Mais!")
            break
        else:
            print("Opção inválida. Escolha de 1 a 4.")

if __name__ == "__main__":
    main()