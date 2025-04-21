# Aula 1 - Compreensao de listas

# lista com quadrados de numeros
quadrados = [x**2 for x in range(1, 11)]

print(quadrados)

# combinar listas
nomes = ["Alice", "Matheus", "João"]
idades = [18, 25, 44]

combinacao = [f"{nome} tem {idade} anos" for nome, idade in zip(nomes, idades)]

print(combinacao)

# Lista de caracteres de uma string
letras = [letra for letra in "Python"]

print(letras)

# strings e listas = acesso por indice, metodo len, percorrer com for in

# Aula 2- ordenacao de lista

numeros = [1, 10, 5, 6, 8, 2]

numeros.sort()

print(numeros)

numeros.sort(reverse=True)

print(numeros)

# utilizando key
palavras = ["ola mundo testando", "teste", "testando", "mais um teste"]

palavras.sort(key=len, reverse=True)

print(palavras)

# sorted -> n muda o dado original
numeros_2 = sorted(numeros)

print(numeros)

print(numeros_2)

# Aula 3- Revertendo listas
cidades = ["São Paulo", "Rio De Janeiro", "Florianópolis"]

cidades.reverse()

print(cidades)

cidades_p = list(reversed(cidades))

print(cidades)

print(cidades_p)

nums = [1, 2, 3, 4, 5]

nums.reverse()

print(nums)

# Aula 4 - len, min, max, sum

numeros = [10, 20, 30, 40, 50]

print(len(numeros))

print("Valor maximo: ", max(numeros))
print("Valor mínimo: ", min(numeros))

print("Soma dos valores: ", sum(numeros))

# key, trabalhar com tamanho de strings em min e max
print("Maior cidade: ", max(cidades, key=len))
print("Menor cidade: ", min(cidades, key=len))