lista_mutavel = [10, 20, 30]

print("Lista mutável (antes das alterações: ")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))

lista_mutavel.append(40)
lista_mutavel[0] = 0

print("Lista mutável (depois das alterações: ")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))