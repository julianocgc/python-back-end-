# EXERCICIO 1:
# ENUNCIADO: Crie uma função lambda que aceite dois números e retorne o maior entre eles.
# DESCRICAO: A função lambda deve receber dois argumentos, comparar os valores e retornar o maior
# deles. Use uma única linha de código para a função.

# EXERCICIO 2:
# ENUNCIADO: Usando map(), transforme uma lista de strings em suas versões em maiúsculas.
# DESCRICAO: A função map() deve aplicar uma transformação a cada elemento de uma lista de strings,
# convertendo todas as letras para maiúsculas e retornando uma nova lista.

# EXERCICIO 3:
# ENUNCIADO: Utilize filter() para selecionar apenas os números positivos de uma lista.
# DESCRICAO: A função filter() deve iterar por uma lista de números e retornar apenas os
# valores maiores que zero, descartando os negativos e o zero.

# EXERCICIO 4:
# ENUNCIADO: Aplique reduce() para calcular o produto de todos os números em uma lista.
# DESCRICAO: A função reduce() deve multiplicar cumulativamente os números de uma lista
# e retornar o produto final. Use a biblioteca functools para importar reduce.

# EXERCICIO 5:
# ENUNCIADO: Combine map(), filter() e reduce() para somar os quadrados dos números pares em
# uma lista.
# DESCRICAO: A função filter() deve selecionar os números pares de uma lista, a função map()
# deve elevar cada número ao quadrado, e a função reduce() deve calcular a soma desses
# valores transformados.

# Ex 1
maior_valor = lambda a,b: a if a > b else b

print(maior_valor(10, 5))

# Ex 2
strings = ["abc", "def", "qwe"]

maiusculas = list(map(lambda x: x.upper(), strings))

print(maiusculas)

# Ex 3
numeros = [-2, -1, 0, 1, 2]

positivos = list(filter(lambda x: x >= 0, numeros))

print(positivos)

# Ex 4
from functools import reduce

lista = [10, 20, 30]

produto = reduce(lambda x, y: x * y, lista)

print(produto)

# Ex 5
nums = [1, 2, 3, 4, 5, 7, 8, 9, 11]

pares = filter(lambda x: x % 2 == 0, nums)

quadrados = map(lambda x: x ** 2, pares)

soma_qds = reduce(lambda x, y: x + y, quadrados)

print(soma_qds)