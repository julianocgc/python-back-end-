# Calculadora
# Soma, divisão, subtração e multiplicação
# Cada uma das operações terá uma função

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por 0!"
    return a / b

def calculadora():
    print("Bem-vindo a calculadora")
    print("Selecione uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    while True:

        opcao = input("Digite o número da operação: ")

        if opcao == "5":
            print("Encerrando a calculadora...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro número da operação: "))
        num2 = float(input("Digite o segundo número da operação: "))

        # Operações da calculadora

        if opcao == "1":
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {divisao(num1, num2)}")

if __name__ == "__main__":
    calculadora()