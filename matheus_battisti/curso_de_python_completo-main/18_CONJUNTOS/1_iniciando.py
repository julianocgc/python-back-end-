# 1 - criando conjuntos - set
conjunto = {1, 2, 3, 4}

print(conjunto)

conjunto_de_lista = set([1, 2, 3, 3])

print(conjunto_de_lista)

print(len(conjunto_de_lista))

print(4 in conjunto_de_lista)
print(1 in conjunto_de_lista)

# 2 - op. matematicas
conj1 = {1, 2, 3}
conj2 = {2, 3, 4, 5}

uniao = conj1 | conj2

print(uniao)

interseccao = conj1 & conj2

print(interseccao)

diferenca = conj1 - conj2

print(diferenca)

diferenca2 = conj2 - conj1

print(diferenca2)

# msms resultados, só que através de métodos
print(conj1.union(conj2))
print(conj1.intersection(conj2))
print(conj1.difference(conj2))
print(conj2.difference(conj1))

# 3 - operações avançadas

# diferença simetrica
sim = conj1 ^ conj2

print(sim)

sim2 = conj1.symmetric_difference(conj2)

print(sim2)

subconjunto = {1, 2}
subconj2 = {99, 101}

# issubset -> SUBCONJUNTO -> CONJUNTO
print(subconjunto.issubset(conj1))
print(subconj2.issubset(conj1))

# 4 - metodos de conjunto
conj3 = {1, 2, 3, 4, 5, 6, 7, 8}

conj3.add(5)
conj3.add(10)

print(conj3)

# remove -> pelo valor do el.
conj3.remove(3)

# discard -> remocao sem erro
conj3.discard(99)
# Erro: conj3.remove(99)

print(conj3)

conj3.clear()

print(conj3)