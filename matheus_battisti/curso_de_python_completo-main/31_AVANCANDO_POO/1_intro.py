# aula 1- encapsulamento

# publico
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoa = Pessoa("Alice")

print(pessoa.nome)

# protegido
class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def exibir_func(self):
        print(f"Nome: {self._nome} Salário: {self._salario}")


func = Funcionario("Paulo", 5000)

func.exibir_func()

# privados
class ContaBancaria():
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def exibir_dados(self):
        print(f"Nome: {self.__nome} Saldo: {self.__saldo}")


conta = ContaBancaria("Pedro", 1000)

# print(conta.__nome) = erro

conta.exibir_dados()


# aula 2 - manipulacao de atributos com @property

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_preco(self):
        return f"R${self.__preco}"
    
    def set_preco(self, preco):
        if preco < 0:
            print("O preço não pode ser negativo!")
            return
        self.__preco = preco

produto = Produto("Notebook", 4000)

print(f"Preço atual do produto: {produto.get_preco()}")

produto.set_preco(1000)

print(f"Preço atual do produto: {produto.get_preco()}")

# @property
class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo
    

carro = Carro("Civic")

print(carro.modelo)

carro.modelo = "Civic 2010"

print(carro.modelo)

# aula 3 - heranca
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("Som genérico")


class Cachorro(Animal):
    def pular_em_pessoa(self):
        print("O cachorro pulou na visita...")

    def fazer_som(self):
        print("Latiu...")


cachorro = Cachorro("Turca")

cachorro.pular_em_pessoa()

print(cachorro.nome)

cachorro.fazer_som()


class Gato(Animal):
    def arranhar(self):
        print("O gato arranhou...")


gato = Gato("Luna")

print(gato.nome)

gato.arranhar()

gato.fazer_som()

# aula 4 - heranca multipla
class Caminhao:
    def carregar_caminhao(self):
        print("O caminhao foi carregado.")

class VeiculoEletrico:
    def carregar_bateria(self):
        print("A bateria foi carregada.")


class CaminhaoEletrico(Caminhao, VeiculoEletrico):
    def descarga_automatizada(self):
        print("O caminhão foi descarregado!")


caminhao_eletrico = CaminhaoEletrico()

caminhao_eletrico.carregar_caminhao()

caminhao_eletrico.carregar_bateria()

caminhao_eletrico.descarga_automatizada()

# conflitos
class ClassA:
    def acao(self):
        print("Acao classe A")

class ClassB:
    def acao(self):
        print("Acao classe B")

# MRO -> da mais importancia para as classes da esquerda
class ClassC(ClassB, ClassA):
    pass

obj = ClassC()

obj.acao()