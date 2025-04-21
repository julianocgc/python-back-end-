# aula 1 - definicao de funcao

# Criacao
def saudacao():
    print("Olá, tudo bem?")

# Invocação/chamar a funcao
saudacao()
saudacao()

def saudacao_completa(nome):
    print(f"Olá {nome}, tudo bem?")

saudacao_completa("Matheus")
saudacao_completa("Paulo")
saudacao_completa("Pedro")

# Aula 2 - parametros
def soma(a, b):
    print(a + b)

soma(4, 5)
soma(15, 20)

def multiplicacao(a, b):
    print(f"O resultado de {a} multiplicado por {b} é:")
    print(f"Resultado: {a * b}")

multiplicacao(10, 2)

def descricao_da_pessoa(nome, profissao, idade):
    print(f"O nome da pessoa é {nome}, ela atua como {profissao} e tem {idade} anos.")

    if idade > 18:
        print("Ela é maior de idade!")


descricao_da_pessoa("Matheus", "Programador", 33)


# Aula 3 - argumentos
def dados_pessoais(nome, idade):
    print(f"O nome é {nome} e a idade é {idade}")

dados_pessoais("Matheus", 33)

dados_pessoais(idade=50, nome="Pedro")

def exemplo_args(*numeros):
    print(numeros)
    for numero in numeros:
        print(numero)

exemplo_args(1, 2, 3)

exemplo_args(10, 20, 30, 40 , 50, 60)

# aula 4 - argumentos padrão
def cumprimentar(nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}")


cumprimentar("Pedro")
cumprimentar("Maria", "Bom dia")

def calcular_area(base, altura=10):
    print(base * altura)

calcular_area(10)

calcular_area(5, 5)

# Erro -> argumento default são os ultimos
# def calcular_area(base=5, altura):
#   print(base * altura)