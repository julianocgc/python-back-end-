# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Escreva um programa que utilize um loop `while` para solicitar ao usuário números
# inteiros até que ele digite um número negativo. Ao final, exiba a soma de todos os números
# inseridos.
# Descrição: O programa deve utilizar um loop `while` para acumular valores em uma variável,
# interrompendo o loop quando um número negativo for inserido.

# Exercício 2:
# Enunciado: Desenvolva um programa que itere sobre uma string fornecida pelo usuário e conte
# quantas vogais estão presentes nela. Use um loop `for` e o comando `continue` para ignorar
# caracteres que não são vogais.
# Descrição: O programa deve iterar sobre a string, verificar se cada caractere é uma vogal e
# atualizar um contador para as vogais encontradas.

# Exercício 3:
# Enunciado: Crie um programa que percorra uma lista de números e interrompa a iteração ao encontrar
# o primeiro número maior que 100. Use o comando `break` para encerrar o loop.
# Descrição: O programa deve iterar sobre a lista de números, verificar se cada número é maior que
# 100 e encerrar o loop ao encontrar a primeira ocorrência.

# Exercício 4:
# Enunciado: Escreva um programa que utilize loops aninhados para criar uma tabela de multiplicação
# de 1 a 5. Formate a saída em forma de matriz para facilitar a leitura.
# Descrição: O programa deve usar loops `for` aninhados para calcular e exibir os resultados da
# multiplicação em formato tabular.

# SOLUÇÕES

# Ex 1
soma = 0

'''
while True:
    numero = int(input("Digite um numero inteiro ou negativo para sair do programa: "))

    if numero < 0:
        break

    soma += numero

print(f"A soma é: {soma}")
'''

# Ex 2
'''
string = input("Digite alguma coisa... ")

vogais = "aeiouAEIOU"

contador = 0

for char in string:
    if char not in vogais:
        continue
    contador += 1

print(f"A quantidade de vogais na string é: {contador}")
'''

# Ex 3
numeros = [10, 20, 30, 60, 120, 150]

for numero in numeros:
    if numero > 100:
        print(f"Primeiro numero encontrado acima de 100: {numero}")
        break
    print(numero)

# Ex 4
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j}", end=" ")
    print()