# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie um programa que receba dois números inteiros e exiba a soma, subtração,
# multiplicação e divisão inteira entre eles.
# Descrição: O programa deve usar operações aritméticas básicas entre dois números inteiros,
# como soma, subtração, multiplicação e divisão inteira. Os resultados devem ser exibidos
# separadamente com mensagens explicativas.

# Exercício 2:
# Enunciado: Escreva um programa que receba um número de ponto flutuante, arredonde-o para duas
# casas decimais e exiba o resultado.
# Descrição: O programa deve solicitar um número float, usar a função round() para arredondá-lo
# para duas casas decimais e exibir o valor arredondado. O programa também deve informar o número
# original.

# Exercício 3:
# Enunciado: Desenvolva um programa que converta um número inteiro em float e vice-versa,
# exibindo o resultado das conversões.
# Descrição: O programa deve receber um número inteiro e convertê-lo em float, bem como receber
# um número float e convertê-lo em inteiro. Ambos os resultados das conversões devem ser exibidos.

# Exercício 4:
# Enunciado: Crie um programa que solicite três números ao usuário, aplique a fórmula de
# Bhaskara para calcular as raízes e exiba os resultados.
# Descrição: O programa deve solicitar os coeficientes `a`, `b` e `c` da equação quadrática.
# Usar o módulo math para calcular a raiz quadrada na fórmula de Bhaskara e exibir as raízes,
# se existirem. Deve incluir validação para o caso de raízes inexistentes.

# Exercício 5:
# Enunciado: Escreva um programa que use o módulo `math` para calcular a área de um círculo,
# solicitando o raio ao usuário.
# Descrição: O programa deve solicitar o raio como entrada, usar a fórmula da área de um
# círculo (A = πr²), com o módulo math para calcular π, e exibir o resultado com duas casas
# decimais.


# ex 1
'''
numero1 = int(input("Digite o n1: "))
numero2 = int(input("Digite o n2: "))

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
'''

# ex 2
'''
numero_float = float(input("Digite um número decimal: "))

numero_arredondado = round(numero_float, 2)

print(numero_float)
print(numero_arredondado)
'''

# ex 3
'''
numero_int = int(input("Digite um número inteiro: "))

numero_convertido_float = float(numero_int)

print(numero_convertido_float)

numero_float = float(input("Digite um número decimal: "))

numero_convertido_int = int(numero_float)

print(numero_convertido_float, numero_convertido_int)
'''

# ex 4

import math
'''

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
raiz2 = (-b - math.sqrt(delta)) / (2 * a)

print(raiz1, raiz2)
'''

# ex5
raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio**2)

print(area)