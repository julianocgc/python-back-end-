# aula 1 - manip. de dados
dados = [1, 2, 3, 4, 5]

dados_quadrados = [x**2 for x in dados]

print(dados_quadrados)

import numpy as np

dados_np = np.array([1, 2, 3, 4, 5])

dados_quadrados_np = dados_np ** 2

print(dados_quadrados_np)

import pandas as pd

# dados = pd.read_csv("dados.csv")

# print(dados.head())

# dados["coluna_existente"] = dados["coluna_existente"] * 2

# print(dados.head())

# aula 2 - introducao ao numpy
array = np.array([1, 2, 3, 4, 5])

print(array)

print(array * 2)

matriz = np.array([[1, 2, 3], [4, 5, 6]])

print(matriz)

print(np.mean(matriz))

print(np.mean(array))

# aula 3 - arrays com numpy

arr = [10, 20, 30]

array = np.array(arr)

print(array)

zeros = np.zeros((4, 4))

print(zeros)

uns = np.ones((3, 7))

print(uns)

aleatorios = np.random.rand(3, 5)

print(aleatorios)

# inicial, final, num. els
espacados = np.linspace(0, 20, 3)

print(espacados)

# aula 4 - propriedades dos arrays

array = np.array([[10, 20 , 30], [1, 5, 10], [2, 4, 6]])

print(array.ndim)

array2 = np.zeros((2, 3, 4))

print(array2)

print(array2.ndim)

print(array.shape)
print(array2.shape)

print(array.dtype)
print(array2.dtype)

print(array.size)
print(array2.size)