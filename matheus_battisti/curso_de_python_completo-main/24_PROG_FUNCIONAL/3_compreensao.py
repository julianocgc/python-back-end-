# Aula 1 - Compreensao de listas
numeros = [1, 2, 3, 4]

triplicar = [x * 3 for x in numeros]

print(triplicar)

triplicar_lambda = [(lambda x: x * 3)(x) for x in numeros]

print(triplicar_lambda)

palavras = ["x", "y", "z"]

maiusculas = [x.upper() for x in palavras]

print(maiusculas)

# aula 2- compreensão em dicionarios
quadrados_dict = {x: x**2 for x in numeros}

print(quadrados_dict)

original = {"a": 1, "b": 2, "c": 3}

invertido = {v: k for k, v in original.items()}

print(invertido)

pares_quadrado = {x: x**2 for x in numeros if x % 2 == 0}

print(pares_quadrado)

# Aula 3 - expressoes geradores
quadrados_gen = list((x**2 for x in numeros))

print(quadrados_gen)

pares_gen = list((x for x in numeros if x % 2 == 0))

print(pares_gen)

# aula 4 - comparacao
import sys

# compreensao = [], gerador = ()
lista = [x**2 for x in range(1000)]
gerador = (x**2 for x in range(1000))

print("Memoria compreensao: ", sys.getsizeof(lista))
print("Memoria gerador: ", sys.getsizeof(gerador))

print(lista[5])
print(list(gerador)[5])