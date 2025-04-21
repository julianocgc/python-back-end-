# EXERCICIO 1:
# ENUNCIADO: Crie uma classe `Produto` com atributos `nome` e `preco`. Instancie objetos e exiba suas
# informações.
# DESCRICAO: O programa deve criar uma classe chamada `Produto`, definir os atributos de instância
# `nome` e `preco`, e permitir a criação de objetos. Os objetos devem exibir suas informações de forma
# clara.

# EXERCICIO 2:
# ENUNCIADO: Defina uma classe `Funcionario` com um atributo de classe `salario_base` e um método para
# calcular o salário com bônus.
# DESCRICAO: A classe deve conter um atributo de classe `salario_base` e um método que aceite um
# percentual de bônus como argumento, retornando o salário ajustado.

# EXERCICIO 3:
# ENUNCIADO: Crie uma classe `Aluno` com um método para calcular a média de suas notas armazenadas em
# uma lista.
# DESCRICAO: O método deve calcular a média de uma lista de notas armazenadas como atributo da
# instância. A média deve ser exibida no formato numérico.

# EXERCICIO 4:
# ENUNCIADO: Implemente uma classe `Carro` com um construtor que inicializa modelo, ano e cor. Crie
# instâncias com valores diferentes.
# DESCRICAO: A classe deve usar o método `__init__` para inicializar os atributos `modelo`, `ano` e
# `cor`. Devem ser criados múltiplos objetos com diferentes valores e exibidos.

# EXERCICIO 5:
# ENUNCIADO: Altere o atributo `idade` de uma instância da classe `Pessoa` usando um método específico
# (setter).
# DESCRICAO: A classe deve usar um método setter para modificar o valor do atributo `idade`. O método
# deve validar se a idade é maior ou igual a 0 antes de alterar o valor.


# Ex 1

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def exibir_info(self):
        return f"Produto: {self.nome} custa R${self.preco}"
    
produto1 = Produto("Notebook", 3000)
produto2 = Produto("Mouse", 250)

print(produto1.exibir_info())
print(produto2.exibir_info())

# Ex 2
class Funcionario:
    salario_base = 2000

    def calcular_salario_com_bonus(self, bonus_percentual):
        return Funcionario.salario_base + (Funcionario.salario_base * (bonus_percentual / 100))
    
funcionario = Funcionario()

print(f"Salário com bônus de 15% é: R${funcionario.calcular_salario_com_bonus(15)}")

# Ex 3

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    

aluno = Aluno("Maria", [8, 9, 6])

print(f"A média do aluno {aluno.nome} é {aluno.calcular_media()}")

# Ex 4
class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def detalhes(self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}")

carro1 = Carro("Fusca", 1976, "Azul")
carro2 = Carro("Civic", 2022, "Preto")

carro1.detalhes()

carro2.detalhes()

# Ex 5
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa...")
        self.__idade = idade
    
    def get_idade(self):
        return self.__idade
    

pessoa = Pessoa("Carlos", 35)

print(f"A idade atual é {pessoa.get_idade()}")

# pessoa.set_idade(-10) erro

pessoa.set_idade(36)

print(f"A idade atual é {pessoa.get_idade()}")