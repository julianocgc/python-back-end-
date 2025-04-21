# Aula 1 - strings
linguagem = "Python"
versao = "3.12"
teste = 'texto'
testando =  '''texto 2'''

print(linguagem, versao, teste, testando)

# Concatenação
print("Este é um curso de " + linguagem + ", ele é muito completo!" + teste)

repeticoes = "Olá" * 3

print(repeticoes)

# 1 = é atribuição
# 2 ='s é comparação

print(linguagem == "Python")

# qtd de caracteres

print(len("algum texto"))
print(len(linguagem))

# verificacao se texto está em outro texto
frase = "O curso de Python é muito bom!"

# STRING PROCURADA in STRING EM Q ESTOU PROCURANDO
print("Python" in frase)
print("PHP" in frase)

# Aula 2 - indexação -> começa no indice 0!
palavra = "Python"

print(palavra[0])
print(palavra[5])
print(palavra[-1])

try:
    print(palavra[11])
except IndexError:
    print("Indice inexistente")

# começa com e termina com
print(palavra.startswith("Py"))
print(palavra.startswith("on"))

print(palavra.endswith("on"))

texto = "Esta é uma frase muito grande"

# fatiamento de strings
nova_frase = texto[10:]

print(nova_frase)

# Aula 3- Fatiamento
frase = "Aprenda a programar em Python"

subfrase = frase[:7]

print(subfrase)

print(frase[-6:])

# fatiamento com passo
print(frase[::2])

# inveter string
print(frase[::-1])

# fatiamento alem do limite
print(frase[5:100])

# indice final exclusivo - no final sempre some 1
print(frase[:7])