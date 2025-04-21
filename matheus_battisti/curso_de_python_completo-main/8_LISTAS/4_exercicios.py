# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie uma lista com os números de 1 a 10. Use append() para adicionar o número 11
# e insert() para adicionar o número 0 no início da lista. Exiba a lista resultante.
# Descrição: O programa deve criar uma lista inicial, usar métodos para adicionar elementos no
# início e no final, e exibir a lista modificada.

# Exercício 2:
# Enunciado: Escreva um programa que receba uma lista de nomes e conte quantas vezes um nome
# específico aparece na lista usando count().
# Descrição: O programa deve receber uma lista de nomes e um nome de busca, calcular quantas
# vezes o nome aparece na lista usando count() e exibir o resultado.

# Exercício 3:
# Enunciado: Desenvolva um programa que organize uma lista de números em ordem crescente e
# depois inverta essa lista. Exiba os resultados em ambas as etapas.
# Descrição: O programa deve usar sort() para ordenar a lista e reverse() para inverter a
# ordem, exibindo os resultados após cada operação.

# Exercício 4:
# Enunciado: Crie uma lista aninhada que representa uma matriz 3x3. Acesse e modifique o valor
# do elemento da segunda linha, terceira coluna. Exiba a matriz antes e depois da modificação.
# Descrição: O programa deve criar uma lista aninhada para representar a matriz, modificar
# um valor específico usando índices e exibir as duas versões da matriz.

# Exercício 5:
# Enunciado: Escreva um programa que receba uma lista de números e exiba o menor valor, o
# maior valor, o número total de elementos e a soma de todos os valores.
# Descrição: O programa deve usar as funções len(), min(), max() e sum() para calcular os
# resultados e exibi-los de forma organizada.

# Ex 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros.append(11)
numeros.insert(0, 0)

print(numeros)

# Ex 2
nomes = ["Matheus", "Pedro", "João", "Matheus", "Henrique"]

nome_busca = "Matheus"

quantidade = nomes.count(nome_busca)

print(f"O nome buscado foi {nome_busca} e ele foi encontrado {quantidade} vezes.")

# Ex 3
nums = [4, 5, 1, 2, 8]

nums.sort()

print(nums)

nums.reverse()

print(nums)

# Ex 4
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 3, 2]
]

print(matriz)

matriz[1][2] = 100

print(matriz)

# EX 5
print("Menor valor: ", min(nums))
print("Maior valor: ", max(nums))
print("Quantidade: ", len(nums))
print("Soma: ", sum(nums))