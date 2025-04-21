# Exibir contatos da agenda
def exibir_contatos(contatos):
    if not contatos:
        print("A agenda está vazia...")
    else:
        for i, contato in enumerate(contatos, start=1):
            nome, telefone, email = contato
            print(f"{i}. Nome: {nome}, Telefone: {telefone}, E-mail: {email}")

# Adicionar contatos a agenda
def adicionar_contatos(contatos):
    nome = input("Digite o seu nome: ")
    telefone = input("Digite o seu telefone: ")
    email = input("Digite o seu email: ")

    novo_contato = (nome, telefone, email)

    return contatos + (novo_contato, )


def main():

    contatos = ()

    while True:
        print("Menu de Agenda")
        print("1. Exibir contatos")
        print("2. Adicionar um contato")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        # Condicional para efetuar ação de cada uma das opções
        if opcao == "1":
            print("Exibindo contatos...")
            exibir_contatos(contatos)
            # Exibir de contatos
        elif opcao == "2":
            # Adicionar contato a agenda
            print("Adicionando novo registro...")
            contatos = adicionar_contatos(contatos)
        elif opcao == "3":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":
    main()