# Aula 1 - Métodos de string

# formataçao
texto = "pythoN é muito leGal"

print(texto.upper())
print(texto.lower())
print(texto.capitalize())

# remocao de espaco
espacos = " teste aqui de python               "

espacos_limpos = espacos.strip()

print(espacos)
print(espacos_limpos)

# substituicao de caracteres
print(espacos.replace("python", "php"))

dados = "nome,telefone,endereco"

dados_separados = dados.split(",")

print(dados_separados)

# Aula 2 split
frase = "Python é muito divertido"

lista_frase = frase.split()

print(lista_frase)

# indices de lista tb comecam com 0 (primeiro el.)
print(lista_frase[1])

string_caracteres = "teste-testando-testou"

print(string_caracteres.split("-"))

# maxsplit = funciona por numero de indices
print(frase.split(" ", 1))


# Aula 3 join
palavras = ["Python", "é", "Incrível"]

print(" ".join(palavras))

print(",".join(palavras))

numeros = [1, 2, 3]

# map -> percorrer uma lista, e modificar eles

print(" ".join(map(str, numeros)))

# Aula 4 Replace
texto = "Python é ótimo"

print(texto.replace("ótimo", "perfeito"))

palavras = "maçã laranja maçã banana maçã"

# terceiro arg: qtd de substituicoes
print(palavras.replace("maçã", "teste", 2))

# limpar caracteres
texto = "sei lá @ teste !" 

print(texto.replace("@", "").replace("!", ""))

print(texto)