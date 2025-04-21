# aula 1 - numeros complexos
numero1 = 3 + 4j
numero2 = 2 - 1j

print(numero1)
print(numero2)

numero3 = complex(5, -3)

print(numero3)

print(numero1.real)
print(numero1.imag)

# aula 2 - conversoes de tipos numericos
numero_int = 10

numero_float = float(numero_int)

print(numero_float)

numero_complex = complex(numero_float)

print(numero_complex)

print(10 + 10.4)

print(int(10.44))

# aula 3 operacoes aritmeticas
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) # divisao normal

print(a // b) # divisao inteira

print(a ** b)

print(a % b) # modulo

# 10 / 3 = 3 inteiro, 1

# aula 4 - precedencia
resultado = 3 + 4 * 5

print(resultado)

resultado2 = (3 + 4) * 5

print(resultado2)

exp = 2 ** 3 ** 2 # 2 ** (3 ** 2) => 2 ** 9

print(exp)

op_complexas = (10 + 5) * 2 - (33 + 4 / 2)

print(op_complexas)

# aula 5 - funcoes matematicas
numero = -15

numero_abs = abs(numero)

print(numero_abs)

numero_quebrado = 1.4235437534

print(round(numero_quebrado, 2))

base = 2
expoente = 5
modulo = 3

resultado = pow(base, expoente)

print(resultado)


quociente, resto = divmod(20, 6) # 3 x 6, 20 - 18 = 2

print(quociente, resto)

# aula 6 - modulo math

import math

numero = 16

raiz_qd = math.sqrt(numero)

print(raiz_qd)

numero = 5

fatorial = math.factorial(5)

print(fatorial)

numero = 100

# objeto math -> metodo/funcao log10
logaritmo = math.log10(numero)

print(logaritmo)

# objeto math -> propriedade pi
print(math.pi)

seno = math.sin(10)

print(seno)

# aula 7

num_grande = 1.5e6 # 1500000
num_peq = 2.5e-3 # 0.0025

print(num_grande)
print(num_peq)

resultado = num_grande + num_peq

print(resultado)

print(f"O numero é {num_grande:.4e}")