# aula 1 - tratamento de erro
try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida")

dados = {"nome":"Maria", "idade": 30}

try:
    dados['altura']
except KeyError:
    print("A chave informada nao existe")

try:
    dados['altura']
except Exception as e:
    print(f"Erro, por favor tente novamente mais tarde.")


# aula 2 - try e except
# try:
#     numero = int(input("Digite um número: "))
#     print(numero)
# except ValueError:
#     print("Valor inválido!")

# 1 -> ok
# @, asd -> nao ok

# try:
#     numero1 = int(input("Digite o primeiro numero: "))
#     numero2 = int(input("Digite o segundo numero: "))

#     resultado = numero1 / numero2

#     print(resultado)
# except ValueError:
#     print("O valor precisa ser um numero...")
# except ZeroDivisionError:
#     print("Divisão por zero não é possível...")

# aula 3 - else com try

# try:
#     numero = int(input("Digite um número: "))
# except ValueError:
#     print("Vc precisa digitar um número inteiro")
# else:
#     print(f"Parabéns por digitar o numero {numero}")


try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo nao existe.")
else:
    print("Arquivo lido com sucesso...")
    print(conteudo)