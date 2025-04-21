# aula 1 - expressoes geradoras

exp_geradora = (x ** 2 for x in range(10))

print(list(exp_geradora))

print(sum(x ** 2 for x in range(6)))

lista = [i ** 2 for i in range(1000)]
gerador = (i ** 2 for i in range(1000))

import sys

print(f"Tamanho em bytes gerador: {sys.getsizeof(lista)} ")
print(f"Tamanho em bytes gerador: {sys.getsizeof(gerador)} ")

# aula 2 - func. geradoras x expressoes geradoras

# num pares => x % 2 == 0
pares = (x for x in range(10) if x % 2 == 0)

print(list(pares))

# fibonacci -> n consigo em uma linha = funcoes
def numero_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a + b

print(list(numero_fibonacci(15)))


# aual 3 - iterador personalizado
class SequenciaPares:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual <= self.limite:
            resultado = self.atual
            self.atual += 2
            return resultado
        raise StopIteration
    
pares = SequenciaPares(20)

for num in pares:
    print(num)

class Ciclo:
    def __init__(self, valores):
        self.valores = valores
        self.indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.valores):
            self.indice = 0
        valor = self.valores[self.indice]
        self.indice += 1
        return valor
    

ciclo = Ciclo([1, 2, 3, 4])

for _ in range(20):
    print(next(ciclo))