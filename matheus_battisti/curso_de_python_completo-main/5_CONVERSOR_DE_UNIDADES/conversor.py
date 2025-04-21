# converter celsius para F
# conveter F para C

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahreinheit_para_celsius(fahreinheit):
    return (fahreinheit - 32) * 5/9

def menu():
    print("Bem-vindo ao Conversor")
    print("Escolha uma opção")
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    print("3 - Sair")

def conversor_temperaturas():
    menu()
    opcao = input("Digite a opção desejada (1/2/3):")

    if opcao == "1":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius:.2f}C é equivalente a {fahrenheit:.2f}F")
    elif opcao == "2":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahreinheit_para_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}F é equivalente a {celsius:.2f}C")
    elif opcao == "3":
        print("Obrigado por utilizar o conversor!")
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")

# Inicialização do sistema
if __name__ == "__main__":
    conversor_temperaturas()