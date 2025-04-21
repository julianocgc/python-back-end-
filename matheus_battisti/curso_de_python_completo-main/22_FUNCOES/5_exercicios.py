# EXERCICIO 1:
# ENUNCIADO: Crie uma função chamada `saudacao` que aceite um nome como parâmetro e retorne
# uma mensagem de saudação personalizada.
# DESCRICAO: Esta função deve receber um nome como entrada, concatenar com a mensagem
# "Olá" e retornar o resultado. Por exemplo, se o nome for "Ana", a saída será "Olá, Ana!".

# EXERCICIO 2:
# ENUNCIADO: Escreva uma função chamada `calcular_media` que aceite uma lista de números
# como argumento e retorne a média dos números.
# DESCRICAO: A função deve calcular a soma dos elementos da lista e dividi-la pelo
# número de elementos na lista. Caso a lista esteja vazia, a função deve retornar `None`.

# EXERCICIO 3:
# ENUNCIADO: Implemente uma função chamada `imprimir_receita` que aceite ingredientes como
# argumentos nomeados arbitrários (`kwargs`) e imprima os ingredientes e suas quantidades.
# DESCRICAO: A função deve iterar sobre os argumentos nomeados fornecidos, exibindo
# cada ingrediente e sua quantidade. Por exemplo, `farinha=2` deve gerar a saída
# "Ingrediente: farinha, Quantidade: 2".

# EXERCICIO 4:
# ENUNCIADO: Crie uma função chamada `soma_recursiva` que use recursão para somar todos os
# números de 1 até um número fornecido como entrada.
# DESCRICAO: A função deve calcular a soma acumulativa de todos os números de 1 até
# o número fornecido. Certifique-se de que a entrada seja maior ou igual a 1 e trate
# casos inválidos com mensagens de erro.

# EXERCICIO 5:
# ENUNCIADO: Desenvolva uma função chamada `multiplicar_lambda` usando uma função lambda que
# aceite dois números como entrada e retorne o produto deles.
# DESCRICAO: A função deve ser implementada usando uma expressão lambda, sem usar `def`.
# Por exemplo, para as entradas 3 e 4, a saída deve ser 12.

# Ex 1

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Matheus")
saudacao("Pedro")

# Ex 2
def calcular_media(notas):
    if not notas:
        return None
    return sum(notas) / len(notas)

print(calcular_media([5, 10, 8]))
print(calcular_media([9, 9.5, 6]))

# Ex 3
def imprimir_receita(**kwargs):
    for ingrediente, quantidade in kwargs.items():
        print(f"Ingrediente: {ingrediente}, precisa de {quantidade} unidades")

ingredientes = {
    'uva': 10,
    'laranja': 3,
    'limao': 2,
    'pessego': 3
}

imprimir_receita(uva=10, laranja=3, limao=2, pessego=3)

# Ex 4
def soma_recursiva(n):
    if n < 1:
        return "O Número deve ser maior que 1..."
    elif n == 1:
        return 1
    
    return n + soma_recursiva(n - 1)

# 3 + 2 + 1 = 6
print(soma_recursiva(3))
print(soma_recursiva(-13))

# Ex 5
multiplicar_lambda = lambda a, b: a * b

print(multiplicar_lambda(2, 2))