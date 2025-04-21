# ENUNCIADOS E DESCRIÇÕES

# Exercício 1:
# Enunciado: Crie uma string com a frase "Python é incrível", substitua a palavra "incrível"
# por "fantástico" e exiba o resultado.
# Descrição: O programa deve criar uma string, usar o método replace() para substituir uma
# palavra específica e exibir o texto atualizado.

# Exercício 2:
# Enunciado: Escreva um programa que receba o nome completo de um usuário, divida o nome
# em partes e exiba o primeiro e o último nome separadamente.
# Descrição: O programa deve usar o método split() para dividir a string do nome em uma lista
# de palavras e acessar o primeiro e o último elementos da lista.

# Exercício 3:
# Enunciado: Desenvolva um programa que solicite uma lista de itens separados por vírgulas
# e os exiba em uma única string, com os itens separados por ponto e vírgula.
# Descrição: O programa deve receber uma entrada de texto, usar o método split() para criar
# uma lista e depois o método join() para concatenar os itens com o delimitador ";".

# Exercício 4:
# Enunciado: Crie uma string multilinha com uma mensagem de boas-vindas que inclua variáveis
# como o nome do usuário e a data atual, formatada com f-strings.
# Descrição: O programa deve usar uma string multilinha com aspas triplas e incluir variáveis
# formatadas dinamicamente com f-strings para exibir uma mensagem personalizada.

# Exercício 5:
# Enunciado: Escreva um programa que receba uma string, conte o número de vogais na string
# e exiba o total de vogais encontradas.
# Descrição: O programa deve iterar pela string, verificar se cada caractere é uma vogal e
# manter um contador que será exibido ao final.

# Exercicio 1
frase = "Python é incrivel"
nova_frase = frase.replace("incrivel", "fantástico")

print(nova_frase)

# Exercício 2
'''
nome_completo = input("Digite o seu nome completo: ")

partes = nome_completo.split()

primeiro_nome = partes[0]
ultimo_nome = partes[1]

print("Primeiro nome: ", primeiro_nome)
print("Último nome: ", ultimo_nome)
'''

# exercicio 3
'''
itens = input("Digite uma lista de itens separados por virgula: ")

lista = itens.split(",")

resultado = ";".join(lista)

print("Itens formatados: ", resultado)
'''

# exercicio 4
from datetime import date

nome_usuario = input("Digite o seu nome: ")
data_atual = date.today().strftime("%d/%m/%Y")

mensagem = f'''
    Bem-vindo {nome_usuario}!
    Hoje é {data_atual}
'''

print(mensagem)

# exercicio 5
texto = input("Digite uma string: ")

vogais = "aeiouAEIOU"

contador = sum(1 for char in texto if char in vogais)

print("Total de vogais: ", contador)