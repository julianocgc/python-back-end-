# aula 1 - multiplos decorators
def decorador1(func):
    def wrapper(*args, **kwargs):
        print("Executando decorator1")
        return func(*args, **kwargs)
    return wrapper

def decorador2(func):
    def wrapper(*args, **kwargs):
        print("Executando decorator2")
        return func(*args, **kwargs)
    return wrapper

@decorador2
@decorador1
def dizer_ola():
    print("Olá, tudo bem?")

dizer_ola()

# aula 2 - decoradores de classe

# adicionando metodos
def adicionar_metodo_novo(cls):
    def metodo_novo(self):
        return f"Este é um método novo na classe {cls.__name__}"
    cls.metodo_novo = metodo_novo
    return cls

@adicionar_metodo_novo
class MinhaClasse:
    def __init__(self, nome):
        self.nome = nome

obj = MinhaClasse("Nome do Objeto")

print(obj.metodo_novo())

# alterar o comportamento de inicializacao
def decorador_classe(cls):
    class NovaClasse(cls):
        def __init__(self, *args, **kwargs):
            print("Inicializando a classe com comportamento diferenciado.")
            super().__init__(*args, **kwargs)
    return NovaClasse

@decorador_classe
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p = Pessoa("Alice")

print(p.nome)

# aula 3 - decoradores do python

class Contador:
    total = 0

    @classmethod
    def incrementar(cls):
        cls.total +=1

    @classmethod
    def exibir_total(cls):
        return f"Total: {cls.total}"

Contador.incrementar()
Contador.incrementar()
Contador.incrementar()

print(Contador.exibir_total())

class Matematica:

    @staticmethod
    def soma(a, b):
        return a + b
    
    @staticmethod
    def subtracao(a, b):
        return a - b

print(Matematica.soma(10, 20))

print(Matematica.subtracao(50, 5))

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

ret = Retangulo(10, 20)

print(ret.area)


class Produto:
    imposto = 0.1

    def __init__(self, preco):
        self.preco = preco

    @classmethod
    def alterar_imposto(cls, novo_imposto):
        cls.imposto = novo_imposto

    def calcular_preco_final(self):
        return self.preco * (1 + Produto.imposto)


produto = Produto(100)

print(f"Preço final do Produto: {produto.calcular_preco_final()}")

Produto.alterar_imposto(.3)

print(f"Preço final do Produto: {produto.calcular_preco_final()}")