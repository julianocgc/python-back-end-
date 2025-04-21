# aula 1 - metodos estáticos

class Validator:
    @staticmethod
    def validar_idade(idade):
        return idade > 0
    
print(Validator.validar_idade(10))
print(Validator.validar_idade(-5))

class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b
    
    @staticmethod
    def calcular_area_retangulo(base, altura):
        return base * altura
    
    def soma2(self, a, b):
        return a + b
    

print(Matematica.soma(10, 2))

print(Matematica.calcular_area_retangulo(12, 5))

# print(Matematica.soma2(10, 2)) -> erro, precisa de objeto

# aula 2 - class methods

class ContaBancaria:
    total_contas = 0

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

        ContaBancaria.total_contas += 1

    @classmethod
    def obter_total_de_contas(cls):
        return cls.total_contas
    

print(f"Nós temos {ContaBancaria.obter_total_de_contas()} contas no banco!")

c1 = ContaBancaria("Matheus", 1000)
c2 = ContaBancaria("Pedro", 2000)
c3 = ContaBancaria("João", 3000)

print(f"Nós temos {ContaBancaria.obter_total_de_contas()} contas no banco!")

# aula 3  - dunder methods
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome} Preço: {self.preco}"
    
    def __repr__(self):
        return f"Produto(nome={self.nome}, preco={self.preco})"


prod1 = Produto("Notebook", 2000)

print(prod1)
print(str(prod1))
print(repr(prod1))

# aula 4- outros dunder methods
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outro):
        return self.nome == outro.nome and self.idade == outro.idade
    
    def __lt__(self, outro):
        return self.idade < outro.idade
    

p1 = Pessoa("Marcos", 30)
p2 = Pessoa("Marcos", 30)
p3 = Pessoa("Maria", 40)

print(p1 == p2)
print(p1 == p3)


print(p1 < p2)
print(p1 < p3)