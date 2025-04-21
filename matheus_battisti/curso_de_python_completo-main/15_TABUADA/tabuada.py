"""
    Gerar a tabuada de um número fornecido pelo usuário, exibindo os resultados de 1 a 10.
"""

def tabuada():
    print("Bem vindo a tabuada!")

    try:
        # Solicitar o número para o usuario
        numero = int(input("Digite o número da tabuada: "))

        print(f"Exibindo a tabuada do número {numero}")

        # Exibir a tabuada
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


if __name__ == "__main__":
    tabuada()

# try catch -> padrao da maioria das linguagens
# try except = try catch