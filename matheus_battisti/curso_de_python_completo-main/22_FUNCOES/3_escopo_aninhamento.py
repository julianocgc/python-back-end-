# aula 1 - funcao aninhada
def funcao_externa(mensagem):

    a = 10

    def funcao_interna():
        print(f"Mensagem recebida: " + mensagem)
        print(a)

    funcao_interna()

funcao_externa("testando")

def soma(a, b):
    resultado = a + b

    def exibir_resultado():
        print(f"O resultado da soma entre {a} e {b} é: {resultado}")

    exibir_resultado()

soma(10, 20)


# Aula 3 - closure
def criar_contador():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

# criar contador => 0 => incrementandor (incrementar) => nonlocal contador = SALVAR O VALOR ATUAL 0 + 1 = 2 + 1 = 3 + 1

contador = criar_contador()

print(contador()) # 1
print(contador()) # 2
print(contador()) # 3
print(contador()) # 4

def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

# Multiplicador -> nao tem valor
# Multiplicador -> fator = 10
# Multiplicador -> fator = 20, numero = 10 (20 * 10)
# 

multiplicar_por_2 = multiplicador(2)

print(multiplicar_por_2(10))
print(multiplicar_por_2(20))
print(multiplicar_por_2(30))

multiplicar_por_3 = multiplicador(3)

print(multiplicar_por_3(10))
print(multiplicar_por_3(20))
print(multiplicar_por_3(30))

# aula 4- documentacao de funcao

# [10, 6, 7] => 23 / 3 => media


def calcular_media(notas):
    """
        Calcula a média de uma lista de notas.

        Parâmetros:
            notas(list): Uma lista de números representado as notas.

        Retorno:
            float: A média das notas fornecidas    

        Exemplo:
            [10, 6, 7] => 23 / 3 => media
    
    """


    return sum(notas) / len(notas)

print(calcular_media([10, 6, 8]))