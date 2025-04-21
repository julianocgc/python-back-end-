# Aula 1 - metodos uteis
frutas = ["maçã", "banana", "Laranja", "Melancia", "morango", "banana"]

print(frutas.count("banana"))
print(frutas.count("maçã"))
print(frutas.count("kiwi"))

print(frutas.index("banana"))
print(frutas.index("Melancia"))
# el. n existe = erro => print(frutas.index("uva"))

teste = frutas.clear()

print(teste)

print(frutas)

# Aula 2 - listas aninhadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz)

print(matriz[0])

# primeiro index = lista, segundo index = el.
print(matriz[1][2])

nova_linha = [10, 11, 12]

matriz.append(nova_linha)

print(matriz)

# aula 3 - continuando listas aninhadas
print(matriz[2][0])

matriz[0][1] = 99

print(matriz)

matriz.pop(1)

print(matriz)

matriz[0].append(123)

print(matriz)

# acessando sublistas, podemos usar os metodos de lista normalmente

matriz.append([4, 4, 4])

print(matriz)

# aula 4 - iterando sobre listas
lista_nova = [1, 2, 3, 4, 5]

# for in
for numero in lista_nova:
    print("O numero da vez é ", numero)

# i => pode ser chamado de qlqr coisa (i, j,m, n)
for i, linha in enumerate(matriz):
    print(f"Linha {i + 1}: {linha}")

for linha in matriz:
    print(linha)
    for numero in linha:
        print("Valor: ", numero)

i = 0
while i < len(lista_nova):
    print("Numero: ", lista_nova[i])
    i += 1