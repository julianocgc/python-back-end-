# aula 1 - iterador

iterador = iter([1, 2, 3])

print(iterador)
print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador)) StopIteration erro

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        raise StopIteration
    

contador = Contador(5)

for numero in contador:
    print(numero)


string = "Python"
string_iterador = iter(string)

print(next(string_iterador))
print(next(string_iterador))
print(next(string_iterador))

# verificar se algo é iteravel
from collections.abc import Iterable

print(isinstance([1,2 ,3], Iterable))
print(isinstance(123, Iterable))

# aula 2- geradores
def numeros():
    yield 1
    yield 2
    yield 3

for numero in numeros():
    print(numero)


def pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

print(list(pares(15)))


def contador_infinito():
    i = 1
    while True:
        yield i
        i += 1


cont = contador_infinito()

print(next(cont))
print(next(cont))
print(next(cont))
print(next(cont))
print(next(cont))
print(next(cont))

def mensagens():
    yield "Olá"
    yield "Bem-vindo"
    yield "Tudo bem?"
    yield "Tchau"

for msg in mensagens():
    print(msg)

# aula 3 - yield e return

def funcao_com_return():
    return 42

print(funcao_com_return())


def funcao_com_yield():
    yield 42

gen = funcao_com_yield()

print(next(gen))


def contador():
    yield 1
    print("Pausa")
    yield 2
    print("Continua")
    yield 3
    print("Finaliza")

for valor in contador():
    print(valor)


def quadrados_return(n):
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado


def quadrados_yield(n):
    for i in range(n):
        yield i ** 2

print(quadrados_return(5))
print(list(quadrados_yield(5)))

# aula 4 - aplicacoes praticas de geradores

def gerar_primos(limite):
    for num in range(2, limite + 1):
        if all(num % i != 0 for i in range(2, int(num ** .5) + 1)):
            yield num

print(list(gerar_primos(10)))

def somatorio(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
        yield soma

print(list(somatorio(10)))