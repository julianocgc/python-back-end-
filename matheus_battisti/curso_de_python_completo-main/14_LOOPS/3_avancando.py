# Aula 1- Loops aninhados
matriz = [[1, 2, 3], [4, 5, 6], [9, 8, 7]]

for linha in matriz:
    print(linha)
    for elemento in linha:
        print(f"Elemento: {elemento}")


lista1 = [1, 2, 3]
lista2 = [2, 5, 7]

for a in lista1:
    for b in lista2:
        if a == b:
            print("Iguais")
        print(f"Comparando {a} e {b}")