# Aula 1 - Funcoes Lambda
dobrar = lambda x: x * 2

print(dobrar(5))
print(dobrar(15))
print(dobrar(52))

valores = [1, 2, 3, 4]


# map => funcao lambda, lista => modificar os valores
quadrados = list(map(lambda x: x ** 2, valores))

print(quadrados)

# filter => lambda, lista => os els. filtrados
filtrar_pares = list(filter(lambda x: x % 2 == 0, valores))

print(filtrar_pares)

# Aula 2 - def vs lambda
def soma(a, b):
    return a + b

soma2 = lambda a, b: a + b

print(soma(2, 4))

print(soma2(5, 5))

def soma_com_checagem(a, b):
    if a > b:
        print("A é maior que b")
        return 0
    
    return a + b

print(soma_com_checagem(5, 15))

print(soma_com_checagem(10, 5))

# Aula 3 - recursão

# 5 * 4 * 3 * 2 * 1 = x

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(15))

def fibonnacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonnacci(n - 1) + fibonnacci(n - 2)

print(fibonnacci(6))
print(fibonnacci(10))

# fibonacci -> 0, 1, 1, 2, 3, 5...