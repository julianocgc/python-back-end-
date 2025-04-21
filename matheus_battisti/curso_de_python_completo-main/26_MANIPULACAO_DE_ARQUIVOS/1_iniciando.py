# aula 1 - arquivos em python
# w = write
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Ola arquivo Python")

import csv

with open("dados.csv", "w") as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    # csv = linhas e colunas, comma separated values
    writer.writerow(["Nome", "Idade"])
    writer.writerow(["Matheus", 33])
    writer.writerow(["Maria", 44])

with open("imagem.jpg", "rb") as img:
    conteudo = img.read()

# aula 2 - open e close
arquivo = open("teste.txt", "w")
print(arquivo.closed)
arquivo.write("Escrevi e pronto...")
print(arquivo.closed)
arquivo.close()
print(arquivo.closed)

# open => abre o arquivo
# close => fecha o arquivo

# a gente realize operacoes com o with

# se nao utilizar ou se pegar codigo legado/antigo, checar se há o close

# aula 3 - modos de arquivos
with open("exemplo.txt", "r") as arquivo:
    print(arquivo.read())


with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Sobrescrevendo tudo!")

with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Isso está dps do que já foi escrito...")

with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Isso está dps do que já foi escrito... 2")

with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Sobrescrevendo tudo!")

# aula 4 - leitura
with open("exemplo2.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo) 

with open("exemplo2.txt", "r") as arquivo:
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()

    print("Linha 1:" + linha1)
    print("Linha 2:" + linha2)
    print("Linha 3:" + linha3)

with open("exemplo2.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    print(linhas)

with open("exemplo2.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha)