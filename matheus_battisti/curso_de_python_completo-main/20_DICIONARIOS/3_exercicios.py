"""
EXERCÍCIO 1: Criando e manipulando um dicionário de alunos
DESCRIÇÃO: Crie um dicionário para armazenar nomes de alunos como chaves e suas notas como valores. 
Adicione três pares chave-valor ao dicionário, remova um aluno usando a chave e exiba o restante 
dos pares no dicionário formatados.

EXERCÍCIO 2: Acessando e filtrando valores em um dicionário
DESCRIÇÃO: Dado um dicionário com produtos e seus preços, filtre apenas os produtos com preço 
acima de R$50,00. Exiba o nome e o preço de cada produto que atenda a esse critério.

EXERCÍCIO 3: Iterando sobre dicionários para exibir informações
DESCRIÇÃO: Crie um dicionário com informações de um funcionário, incluindo nome, cargo e salário. 
Use um loop for para iterar sobre o dicionário e exibir as informações formatadas chave por valor.

EXERCÍCIO 4: Compreensão de dicionários com listas de números
DESCRIÇÃO: Usando uma lista de números, crie um dicionário onde a chave é o número e o valor 
é o quadrado do número. Exiba o dicionário completo ao final.

EXERCÍCIO 5: Trabalhando com dicionários aninhados para organização de dados
DESCRIÇÃO: Crie um dicionário aninhado para armazenar informações de clientes. Cada cliente deve 
ter um identificador único e conter informações como nome, idade e cidade. Exiba os dados de 
cada cliente formatados em linhas separadas.
"""

# Ex1

alunos = {"Ana": 9.0, "Matheus": 7.0, "Rodrigo": 8.0}

alunos["Daniela"] = 7.5

print(alunos)

alunos.pop("Matheus")

print(alunos)

# Ex 2
produtos = {"Computador": 3000.50, "Liquidificador": 80.44, "Mouse": 44.12, "Teclado": 122.10}

produtos_filtrados = {produto: preco for produto, preco in produtos.items() if preco > 50.0}

print(produtos_filtrados)

# Ex 3
func = {"nome": "Maria", "cargo": "Gerente", "salario": 5000.00}

for chave, valor in func.items():
    print(f"{chave.capitalize()}: {valor}")

# Ex 4
numeros = [1, 2, 3, 4, 5]

quadrados = {num: num ** 2 for num in numeros}

print(quadrados)

# Ex 5
clientes = {
    "cliente1": {"nome": "Carlos", "idade": 30, "cidade": "São Paulo"},
    "cliente2": {"nome": "Mariana", "idade": 25, "cidade": "Rio de Janeiro"},
    "cliente3": {"nome": "Pedro", "idade": 28, "cidade": "Belo Hrizonte"},
}

for cliente, dados in clientes.items():
    print(f"{cliente.capitalize()}")
    for chave, valor in dados.items():
        print(f"{chave.capitalize()} - {valor}")