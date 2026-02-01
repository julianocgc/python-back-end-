class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fala():
        return f"{self.nome} é um(a) {self.especie}"

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca

    def fala(self):
        return f"{super().fala()} late"

    class Gato(Animal):
        def __init__(self, nome, cor):
            super().__init__(nome, "Gato")
            self.cor = cor

            def fala():
                return f"{super().fala()} mia"

dog = Cachorro("Bilu", "Caramelo")
cat = Gato("Pipoca", "Rajado")

print("Atributos do Cachorro:")
print(f"Nome: {dog.nome}")
print(f"Raça: {dog.raca}")
print(f"Especie: {dog.especie}")
print()
print(dog.fala())
print()
print()

print("Atributos do Gato:")
print(f"Nome: {cat.nome}")
print(f"Raça: {cat.cor}")
print(f"Especie: {cat.especie}")
print()
print(cat.fala())