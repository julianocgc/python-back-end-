# 1 - Tuplas em funcoes

def dividir(numerador, denominador):
    quociente = numerador // denominador
    resto = numerador % denominador
    return quociente, resto

resultado = dividir(10, 3)

print(resultado)

print(f"Quociente {resultado[0]} e Resto {resultado[1]}")

# envia os dados para funcao, faz as divisoes, retorna uma tupla, desempacota a tupla 2
quociente, resto = dividir(20, 2)

print(quociente, resto)


def calcular_area(dimensoes):
    largura, altura = dimensoes
    return largura * altura

area = calcular_area((5, 4))

print(area)

# 2 - conversoes entre listas e tuplas
lista = [4, 5, 6]

tupla = tuple(lista)

print(tupla)

lista_da_tupla = list(tupla)

print(lista_da_tupla)

# strings para listas ou tuplas
texto = "Python"

tupla_texto = tuple(texto)

lista_texto = list(texto)

# strings -> vao ser divididas pelas letras

print(tupla_texto)
print(lista_texto)

# tuple e list n modificam o dado original

# 3 - listas e tuplas
l = [1, 2, 3]

t = (1, 2, 3)

# t[0] = 1

l[0] = 2

import timeit

tempo_lista = timeit.timeit("[1, 2, 3, 4, 5]", number=1000000)
tempo_tupla = timeit.timeit("(1, 2, 3, 4, 5)", number=1000000)

print(f"Tempo lista: {tempo_lista} e Tempo tupla: {tempo_tupla}")