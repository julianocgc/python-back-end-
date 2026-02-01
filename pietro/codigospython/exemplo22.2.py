def calcula_quadrados(lista):
    for elem in lista:
        quad = elem ** 2
        print(f"O quadrado de {elem} é {quad}")

lista_de_inteiros = [1, 2, 3, 4, 5]

calcula_quadrados(lista_de_inteiros)