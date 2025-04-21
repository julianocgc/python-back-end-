# Aula 1 - Op. de identidade
x = None

print(x is None)
print(x == None)
print(x is not None)

a = 11
b = 10

print(a is b)
print(a == b)

lista = [1, 2, 3]
lista2 = [1, 2, 3]

print(lista is lista2)
print(lista == lista2)

s1 = "Python"
s2 = "Python"

print(s1 is s2)
print(s1 == s2)

d = {}
d2 = {}

print(d is d2)
print(d == d2)

t = ()
t2 = ()

print(t is t2)
print(t == t2)

# Aula 2 - Op. de associação
frutas = ["Maçã", "Banana", "Laranja"]

print("Maçã" in frutas)
print("Abacate" not in frutas)

frase = "Python é muito legal"

print("Python" in frase)
print("Java" not in frase)

# dicionarios = lista de dados com chave e valor
pessoa = {"nome": "Matheus", "idade": 33}

# Chave
print("profissao" in pessoa)
# Valor
print("Joaquim" in pessoa.values())

# tupla = lista imutavel
numeros = (1, 2, 3, 4, 5)

print(1 in numeros)
print(10 in numeros)

# Aula 3 - operadores com condições e calculos
'''
entrada = input("Digite um número: ")

numeros = [1, 2, 3, 4, 5]

if int(entrada) in numeros:
    print("Você acertou!")
'''

idade = 25
renda = 6000

if idade < 30 and renda > 5000:
    print("Você ganha bem!")


frase = "PHP e Python são linguagens de programação"

if "Python" in frase and "PHP" in frase:
    print("O texto fala sobre Python e PHP")