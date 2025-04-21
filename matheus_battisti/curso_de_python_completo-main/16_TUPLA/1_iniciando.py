# 1 - Criando tuplas
tupla = (1, 2, 3)

print(tupla)

tupla_lista = tuple([1, 2, 3])

print(tupla_lista)

tupla_1_el = (1,)

print(tupla_1_el)

tupla_vazia = ()

print(tupla_vazia)

# Aula 2- Imutabilidade
tupla = (1, 2, 3, 4)

# Erro
# tupla[0] = 10

print(tupla[0])

tupla_nova = tupla + (5, 6, 7, 3)

print(tupla_nova)

ocorrencias = tupla_nova.count(3)

print(ocorrencias)

print(tupla_nova.index(7))

# Aula 3 - operacoes com tuplas
print(tupla_nova[3])

subtupla = tupla_nova[2:5]

print(subtupla)

tupla = (10, 20)

# concatenação
tupla_maior = tupla_nova + tupla

print(tupla_maior)

tupla_repetida = tupla_nova * 3

print(tupla_repetida)

# 4 - desempacotamento

tupla_teste = ("a", "b", "c")

um, dois, tres = tupla_teste

print(um, dois, tres)

# erro - ha mais valores na tupla
# teste, testando = tupla_teste

a, *extras = tupla_repetida

print(a)

print(extras)

tuplas = [(1, 14), (22, 12), (44, 45)]

for x,y in tuplas:
    print("Coordenadas x e y: ", x, y)