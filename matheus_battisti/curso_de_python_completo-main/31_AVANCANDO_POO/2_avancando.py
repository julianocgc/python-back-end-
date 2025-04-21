# aula 1- MRO
class A:
    def acao(self):
        print("Acao A")

class B(A):
    def acao(self):
        print("Acao B")

class C(A):
    def acao(self):
        print("Acao C")

class D(B, C):
    pass


obj = D()

obj.acao()

print(D.mro())


# super

class X:
    def fazer_algo(self):
        print("Fazendo algo em X")


class Y(X):
    def fazer_algo(self):
        super().fazer_algo()
        print("Fazendo algo em Y")

obj2 = Y()

obj2.fazer_algo()

class Z(Y):
    def fazer_algo(self):
        super().fazer_algo()
        print("Fazendo algo em Z")

obj3 = Z()

obj3.fazer_algo()

# aula 2 - polimorfismo
class Gato:
    def fazer_som(self):
        print("Miau")

class Cachorro:
    def fazer_som(self):
        print("AU au")

# basico, com metodo comum
animais = [Gato(), Cachorro()]

for animal in animais:
    animal.fazer_som()

# funcao polimorfica
def executar_som(animal):
    print("Emitindo som do animal:")
    animal.fazer_som()

executar_som(Gato())

cachorro = Cachorro()

executar_som(cachorro)

# aula 3 - sobreposicao de metodos
class Veiculo:
    def mover(self):
        print("Movendo o veiculo...")

    def parar(self):
        print("O veículo foi parado.")

class Carro(Veiculo):
    def mover(self):
        print("Movendo o carro...")

    def parar(self):
        print("Freando o carro...")
        super().parar()

carro = Carro()

carro.mover()

carro.parar()