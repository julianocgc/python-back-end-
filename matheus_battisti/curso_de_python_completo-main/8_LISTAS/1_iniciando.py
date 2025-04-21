# Aula 1
lista_vazia = []

print(lista_vazia)

print(len(lista_vazia))

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1)

print(len(lista1))

lista_concatenada = lista1 + lista2

print(lista_concatenada)

lista_repetida = lista1 * 3

print(lista_repetida)

# verificar se um el. está ou nao na lista (in e not in)
print(2 in lista1)
print(10 not in lista2)
print(5 in lista2)
print(10 in lista2)

# modificar valores da lista
lista1[0] = 10

print(lista1)

# indice na lista comeca de 0 (1o el.)
print(lista1[2])

# erro => print(lista1[10])

# Aula 2 - adicionando elementos
animais = ["cachorro", "gato"]

animais.append("pássaro")

print(animais)

animais.insert(1, "coelho")

print(animais)

numeros = []

numeros.append(5)
# indice 0 => inserindo no inicio da lista
numeros.insert(0, 10)

print(numeros)

# funciona, mas nao é legal
numeros.insert(999999999, 10)

print(numeros)

# Aula 3 - remocao de itens
print(animais)

animais.remove("gato")

print(animais)

primeiro_el = animais.pop(0)

print(animais)
print(primeiro_el)

animais.pop()

print(animais)

# indice e el. q nao existe, gera erro
# erro => animais.remove("algoqnaoexiste")
# erro => animais.pop(15)