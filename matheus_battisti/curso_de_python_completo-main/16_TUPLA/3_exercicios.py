# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie uma tupla que armazene os nomes de 5 cidades. Imprima cada nome individualmente
# utilizando um loop.
# Descrição: O programa deve criar uma tupla com 5 nomes de cidades e usar um loop `for` para exibir
# cada cidade.

# Exercício 2:
# Enunciado: Defina uma função que receba dois números como parâmetros e retorne uma tupla contendo
# a soma, a diferença e o produto dos números. Mostre como acessar cada valor retornado separadamente.
# Descrição: A função deve calcular e retornar os valores como uma tupla. O programa deve usar
# desempacotamento para acessar os valores.

# Exercício 3:
# Enunciado: Converta a lista `[10, 20, 30, 40, 50]` em uma tupla. Em seguida, exiba o maior e o
# menor valor da tupla.
# Descrição: O programa deve usar a função `tuple()` para a conversão e as funções `max()` e `min()`
# para encontrar os valores máximo e mínimo.

# Exercício 4:
# Enunciado: Crie um programa que itere sobre uma tupla de números e calcule a soma apenas dos
# números pares presentes nela.
# Descrição: O programa deve iterar sobre a tupla, verificar se cada número é par e somar os pares.

# Exercício 5:
# Enunciado: Escreva um programa que compare o desempenho de listas e tuplas na iteração de
# 1 milhão de elementos, exibindo o tempo de execução de cada uma.
# Descrição: O programa deve usar a biblioteca `timeit` para medir o tempo de execução de um loop
# iterando sobre uma lista e uma tupla.

# Ex1

cidades = ("São Paulo", "Floripa", "Belo Horizonte", "Curitiba", "Porto Alegre")

for cidade in cidades:
    print(f"Cidade: {cidade}")

# Ex 2
def operacoes(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2

resultado = operacoes(10, 5)

print(f"Soma: {resultado[0]}, Subtração: {resultado[1]}, Multiplicação: {resultado[2]}")

# Ex3
lista = [10, 20, 30, 40, 50]

tupla = tuple(lista)

print(f"O maior valor é {max(tupla)} e o menor {min(tupla)}")


# Ex 4
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero

print(f"A soma foi: {soma_pares}")

# Ex 5
lista = list(range(1_000_000))
tupla = tuple(range(1_000_000))

import timeit

tempo_lista = timeit.timeit(stmt="for x in lista: pass", setup="lista = list(range(1_000_000))", number=1000)
tempo_tupla = timeit.timeit(stmt="for x in tupla: pass", setup="tupla = tuple(range(1_000_000))", number=1000)


print(f"Tempo de execução lista {tempo_lista:.5f} segundos")
print(f"Tempo de execução tupla {tempo_tupla:.5f} segundos")

