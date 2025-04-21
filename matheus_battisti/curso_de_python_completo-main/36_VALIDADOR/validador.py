import re

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$"
    if re.match(padrao, email):
        return True
    return False

def validar_telefone(telefone):
    # 4899999999999 -> (48) 99999-9999 => mascára!
    padrao = r"^\(\d{2}\) \d{4,5}-\d{4}$"

    if re.match(padrao, telefone):
        return True
    return False

def validar_cpf(cpf):
    # criado com base numa formula != regex
    # regex valida o formato
    # 333.333.333-22
    padrao = r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"

    if re.match(padrao, cpf):
        return True
    return False

def menu():
    while True:
        print("=== Validador de Dados ===")
        print("1. Validar E-mail")
        print("2. Validar Telefone")
        print("3. Validar CPF")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            email = input("Digite o e-mail a ser validado: ")
            if validar_email(email):
                print("E-mail válido.")
            else:
                print("E-mail inválido.")
        elif opcao == "2":
            telefone = input("Digite o telefone a ser validado: ")
            if validar_telefone(telefone):
                print("Telefone válido.")
            else:
                print("Telefone inválido.")
        elif opcao == "3":
            cpf = input("Digite o CPF a ser validado: ")
            if validar_cpf(cpf):
                print("CPF válido.")
            else:
                print("CPF inválido.")
        elif opcao == "4":
            print("Saindo do Validador. Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()