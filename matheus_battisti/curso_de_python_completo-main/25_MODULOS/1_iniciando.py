# aula 1 - O que sao modulos
import meu_modulo

print(meu_modulo.saudacao("Matheus"))

import math

print(math.sqrt(16))

# aula 2 - modulos padrão / core modules
print(math.pi)

print(math.cos(math.radians(60)))

import random

print(random.randint(1, 10))

lista = ["a", "b", "c", "d"]

print(random.choice(lista))

import datetime

print(datetime.datetime.now())

print(datetime.date.today())

import os # operational system

# print(os.getenv("PATH"))

# aula 3 - Alias
import numpy as np

array = np.array([1, 2, 3, 4])

print(array)

from math import sqrt, pi

print(sqrt(10))

print(pi)

from random import randint as ri

print(ri(10, 1000))

# from math import * <- má prática

# aula 4 - modulos internos
import calculadora

print(calculadora.somar(1, 1))
print(calculadora.subtrair(1, 1))

from utilitarios import saudacoes

saudacoes.saudacao()