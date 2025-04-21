# aula 1 - escrita em arquivos
with open("arquivo_write.txt", "w") as arquivo:
    arquivo.write("Testando a escrita \n")
    arquivo.write("Testando a escrita 2 \n")

linhas = ["Linha 1 \n", "Linha 2 \n", "Linha 3 \n"]

with open("arquivo_write.txt", "w") as arquivo:
    arquivo.writelines(linhas)

with open("arquivo_write.txt", "a") as arquivo:
    arquivo.write("Nova linha \n")

numeros = [1, 2, 3, 4]

# ú, é, ç => configurar
with open("arquivo_write.txt", "w") as arquivo:
    for numero in numeros:
        arquivo.write(f"Número: {numero} \n")

# aula 2 - binários
with open("imagem.jpg", "rb") as imagem:
    dados = imagem.read()
    print(f"Bytes lidos: {len(dados)}")

with open("copia_imagem.jpg", "wb") as nova_imagem:
    nova_imagem.write(dados)

with open("imagem.jpg", "rb") as imagem, open("imagem_append.jpg", "ab") as append_img:
    dados = imagem.read(1024)

    append_img.write(dados)

