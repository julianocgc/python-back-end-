# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Escreva um programa que solicite dois números ao usuário e use operadores de comparação
# para verificar se o primeiro número é maior, menor ou igual ao segundo. Exiba os resultados.
# Descrição: O programa deve capturar dois números do usuário, realizar as comparações com operadores
# (<, >, ==) e exibir mensagens indicando a relação entre os números.

# Exercício 2:
# Enunciado: Desenvolva um programa que receba três números e determine se o primeiro é menor que o
# segundo e maior que o terceiro utilizando operadores combinados.
# Descrição: O programa deve capturar três números e verificar a relação combinada entre eles usando
# operadores (<, >) em uma única expressão.

# Exercício 3:
# Enunciado: Crie um programa que receba a idade de uma pessoa e verifique se ela está apta a votar
# (idade maior ou igual a 16) ou a dirigir (idade maior ou igual a 18) usando operadores lógicos.
# Descrição: O programa deve capturar a idade do usuário, aplicar condições com operadores (and, or)
# e exibir as mensagens correspondentes às permissões.

# Exercício 4:
# Enunciado: Escreva um programa que compare duas listas para verificar se elas ocupam o mesmo espaço
# na memória usando operadores de identidade (is) e verifique se um elemento específico está presente
# em ambas usando operadores de associação (in).
# Descrição: O programa deve criar duas listas, realizar a comparação de identidade com (is) e verificar
# a presença de um elemento em ambas as listas usando (in).

# Exercício 5:
# Enunciado: Implemente um sistema de validação de login que verifica se o nome de usuário e a senha
# inseridos estão corretos, combinando operadores lógicos, de associação e de comparação.
# Descrição: O programa deve verificar se as credenciais inseridas pelo usuário coincidem com as
# credenciais armazenadas e exibir mensagens de sucesso ou erro.

# Ex 1
'''
n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))

if n1 > n2:
    print("O N1 é maior que o N2")
elif n1 < n2:
    print("O N1 é menor que o N2")
else:
    print("Os valores são iguais")
'''

# Ex 2
'''
n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))
n3 = float(input("Digite o numero 3: "))

if n1 < n2 and n1 > n3:
    print("O n1 está entre o n2 e n3")
'''

# Ex 3
'''
idade = int(input("DIgite sua idade: "))

if idade >= 16 and idade < 18:
    print("Você pode votar.")
elif idade >= 18:
    print("Você pode votar e também dirigir.")
else:
    print("Você NÃO pode votar nem dirigir")
'''

# Ex 4
l1 = [1, 2, 3]
l2 = [1, 2, 3]

el = 3

print(l1 is l2)
print(el in l1 and el in l2)

# Ex 5
usuario_banco_de_dados = 'matheus@horadecodar.com.br'
senha_banco_de_dados = 'teste123'

usuario = input("Digite o seu e-mail: ")
senha = input("Digite a sua senha: ")

if usuario == usuario_banco_de_dados and senha == senha_banco_de_dados:
    print("Login efetuado com sucesso!")