# Aula 1 - inteiros
numero1 = 41
numero2 = -12

print("Numeros: ", numero1, numero2)

print(type(numero1))

valor_absoluto = abs(numero2)

print(valor_absoluto)

print(pow(numero1, 2))

print(numero1 + numero2)

# Aula 2 - Operacoes aritmeticas

a = 20
b = 7

# 7 + 7 = 14 => 6 (para dar 20)

soma = a + b
multiplicacao = a * b
divisao = a // b # divisão inteira
divisao_normal = a / b
subtracao = a - b

print("S: ", soma)
print("M: ", multiplicacao)
print("D sem resto, divisão inteira: ", divisao)
print("D normal: ", divisao_normal)
print("Sub: ", subtracao)

resto = a % b

print(resto)

print(2 % 2)

contador = 10

contador = contador + 10

contador += 10

print(contador)

contador *= 5

print(contador)

contador -= 10

print(contador)

# Aula 3 - float
temperatura = 32.1
pi = 3.14747574
altura  = 1.82

# no exterior, estados unidos => , -> .

print("Temperatura: ", temperatura)

print(type(temperatura))

c = 1.8
d = 1.344854385353

print(c + d)
print(c * d)

numero_grande = 1.5e6 # 1.5 X 10^6 = 1500000

print(numero_grande)

print(a + c)

# Aula 4
numero = 2.6535

num_arredondado = round(numero, 2)

print(num_arredondado)

# biblioteca math
import math

valor = 7.9

valor_cima = math.ceil(valor)
valor_baixo = math.floor(valor)

print(valor_cima, valor_baixo)

resultado = 0.1 + 0.2

print(resultado)

print(f"O resultado é {resultado:.1f}")

# f => format

