"""
    Lista de compras funções:

    Adicionar um item a uma lista
    Remover item
    Visualizar Lista
    Limpar lista

"""

def exibir_menu():
    print("Gerenciador Lista de Compras")
    print("1 - Adicionar item")
    print("2 - Remover um item")
    print("3 - Visualizar a lista")
    print("4 - Limpar a lista")
    print("5 - Sair")

# Adiciona item a lista
def adicionar_item(lista):
    item = input("Digite o nome do item: ")

    lista.append(item)

    print(f"'{item}' foi adicionado a sua lista.")

# Visualiza todos os itens da lista
def visualizar_lista(lista):
    if len(lista) == 0:
        print("A lista está vazia")
    else:
        print("Lista de Compras: ")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")

# Remover um item
def remover(lista):
    if len(lista) == 0:
        print("A lista está vazia")
        return
    
    item = input("Digite o item que você quer remover: ")

    if item in lista:
        lista.remove(item)
        print(f"O item {item} foi removido da lista.")
    else:
        print(f"O item {item} não está na lista.")

# limpar a lista
def limpar_lista(lista):
    lista.clear()
    print("A lista agora está vazia.")

def gerenciador_lista_de_compras():

    lista_compras = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        # um if e 4 elis => para se tornar uma unica operacao
        if opcao == "1":
            adicionar_item(lista_compras)
        elif opcao == "2":
            remover(lista_compras)
        elif opcao == "3":
            visualizar_lista(lista_compras)
        elif opcao == "4":
            limpar_lista(lista_compras)
        elif opcao == "5":
            print("Obrigado por utilizado o Gerenciador!")
            break
        else:
            print("Operação invália. Digite outro número.")



# Iniciar programa
if __name__ == "__main__":
    gerenciador_lista_de_compras()