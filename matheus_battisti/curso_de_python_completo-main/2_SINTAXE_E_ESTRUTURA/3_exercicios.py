# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.
# Descrição: O programa deve utilizar a função print() para exibir a mensagem
# "Olá, Mundo!" no console. Este exercício reforça o uso básico da função
# print() e a estrutura simples de um programa Python.

# Exercício 2:
# Enunciado: Escreva um programa que solicite o nome do usuário e exiba uma
# saudação personalizada.
# Descrição: O programa deve usar a função input() para receber o nome do
# usuário e armazená-lo em uma variável. Em seguida, deve exibir uma mensagem
# de saudação que inclua o nome fornecido, utilizando a função print().

# Exercício 3:
# Enunciado: Desenvolva um programa que demonstra o uso correto da indentação
# em uma estrutura condicional.
# Descrição: O programa deve solicitar um número ao usuário e verificar se ele
# é positivo, negativo ou zero. Utilize estruturas condicionais com a
# indentação adequada para determinar e exibir o resultado.

# Exercício 4:
# Enunciado: Crie um programa que solicita dois números ao usuário e exibe a
# soma deles.
# Descrição: O programa deve utilizar a função input() para receber dois
# números, converter as entradas para o tipo numérico apropriado float(), calcular a
# soma e exibir o resultado utilizando print().

# Exercício 5:
# Enunciado: Escreva um programa que calcula a idade do usuário com base no ano
# de nascimento fornecido.
# Descrição: O programa deve solicitar o ano de nascimento do usuário, converter
# a entrada para inteiro, calcular a idade atual considerando o ano atual e
# exibir a idade utilizando print(). Utilize comentários para explicar cada
# etapa do código.

# EX1
print("Olá, Mundo!")

# EX2
nome = input("Digite o seu nome: ")

print("Olá " + nome + ", tudo bem?")

# EX3
if 10 > 5:
    print("10 é maior que 5")

# EX4
n1 = input("Digite o numero 1: ")
n2 = input("Digite o numero 2: ")

#converti os numeros 'em texto', para pontos flutuantes => 15.2
# 15.2 => int => 15
# 10 => float => 10.0
soma = float(n1) + float(n2)

print("A soma dos números é ", soma)

