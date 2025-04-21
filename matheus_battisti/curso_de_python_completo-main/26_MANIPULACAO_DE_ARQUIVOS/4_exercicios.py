# EXERCICIO 1:
# ENUNCIADO: Crie um programa que leia um arquivo de texto linha por linha e exiba todas as linhas em
# ordem inversa.
# DESCRICAO: O programa deve abrir um arquivo de texto existente, ler todas as suas linhas, e exibi-las
# no terminal em ordem inversa. Utilize os métodos readlines() e reverse().

# EXERCICIO 2:
# ENUNCIADO: Escreva um programa que converta um arquivo CSV de produtos em um arquivo JSON formatado.
# DESCRICAO: O programa deve usar o csv.reader para ler o arquivo CSV e json.dump para gravar os dados
# como uma lista de dicionários em um arquivo JSON com indentação para melhor visualização.

# EXERCICIO 3:
# ENUNCIADO: Crie uma função que grave em um arquivo binário uma lista de números inteiros e leia os
# números de volta.
# DESCRICAO: A função deve abrir um arquivo em modo binário, gravar a lista de números convertida em
# bytes, e em seguida, abrir o arquivo novamente para ler os dados e exibi-los no terminal.

# EXERCICIO 4:
# ENUNCIADO: Leia um arquivo JSON com informações de usuários e exiba o nome e a idade de cada usuário.
# DESCRICAO: O programa deve usar json.load para carregar os dados do arquivo JSON e iterar pela lista
# de usuários, exibindo no terminal o nome e a idade de cada um.

# EXERCICIO 5:
# ENUNCIADO: Implemente um programa que tente abrir um arquivo inexistente e trate o erro, exibindo uma
# mensagem personalizada.
# DESCRICAO: O programa deve usar um bloco try-except para capturar o erro FileNotFoundError e exibir
# uma mensagem personalizada informando que o arquivo não foi encontrado.

# Ex 1
with open("arquivo_write.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    linhas.reverse()
    for linha in linhas:
        print(linha)

# Ex 2
import csv
import json

with open("exemplo_csv.csv", "r") as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv)
    dados = list(leitor)

with open("produtos_exercicio.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)

# Ex 3
import struct

def gravar_e_ler_binario(lista_numeros):
    with open("numeros.bin", "wb") as arquivo_bin:
        for numero in lista_numeros:
            arquivo_bin.write(struct.pack("i", numero))

    with open("numeros.bin", "rb") as arquivo_bin:
        while True:
            dado = arquivo_bin.read(4)
            if not dado:
                break
            print(struct.unpack("i", dado)[0])

gravar_e_ler_binario([10, 20, 30, 40])

# Ex 4
with open("dados_convertidos.json", "r") as arquivo_json:
    usuarios = json.load(arquivo_json)
    for usuario in usuarios:
        print(f"Nome: {usuario['Nome']} - Idade: {usuario['Idade']}")


# Ex 5
try:
    with open("arquivoquenaoexiste.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo nao foi encontrado!")