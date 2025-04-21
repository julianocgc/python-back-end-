# aula 1 - definicao de classes

# definindo a classe
class Animal:
    # criando a funcao construtora
    def __init__(self, especie):
        # atribuindo valores para as propriedades
        self.especie = especie


animal = Animal("Cachorro")

print(f"Espécie do animal: {animal.especie}")


# aula 2 - instancia

class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"O carro é do modelo {self.modelo} e foi fabricado em {self.ano}")

carro1 = Carro("Fusca", 1976)

carro2 = Carro("Civic", 2010)

print(carro1.modelo)

print(carro2.modelo)

carro1.detalhes()

# prop -> caracteristicas do obj, o nome obj.prop
# metodos -> acoes, o nome obj.metodo()

carro1.ano = 2000

print(carro1.ano)

carro1.detalhes()

# aula 3 - atributos (propriedades)

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


usuario = Usuario("João", "joao@email.com")
usuario2 = Usuario("Pedro", "pedro@email.com")

print(usuario.nome)
print(usuario.email)
print(usuario2.email)

usuario.nome = "João Silva"

print(usuario.nome)

class Retangulo:
    def __init__(self, altura, largura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
ret = Retangulo(10, 2)

print(f"O valor da area do retangulo é {ret.calcular_area()}")