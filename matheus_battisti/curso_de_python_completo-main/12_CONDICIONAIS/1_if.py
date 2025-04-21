# Aula 1 - if
if True:
    print("Deu certo")
    print("Outra linha")

numero = 6

if numero % 2 == 0:
    print("O numero é par")

valor = 10
valor2 = 20

if valor < valor2:
    print("O valor 1 é menor que o valor 2")

lista = [1, 2, 3]

numero = 2

if numero in lista:
    print("O numero 2 está na lista")


# Aula 2 - else
numero = 11

if numero % 2 == 0:
    print("é par")
else:
    print("é impar")

idade = 27

if idade >= 18:
    print("Vc é maior de idade")
else:
    print("Vc é MENOR de idade")

'''
valor = int(input("Digite um numero positivo"))

if valor > 0:
    print(f"O valor {valor} é positivo!")
else:
    print("Vc digitou um numero negativo")
'''

# aula 3- Elif
idade = 11

if idade < 13:
    print("VOcê é uma criança")
elif idade < 18:
    print("Você é adolescente")
else:
    print("Vocé é adulto")


nota = 6.5

if nota >= 9:
    print("Você foi muito bem!")
elif nota >= 8:
    print("Você foi bem!")
elif nota >= 7:
    print("Você fico na média")
elif nota >= 6:
    print("Você está de recuperação")
else:
    print("Você foi muito mal, faça aulas de reforço")

# podemos ter só if
# nao podemos ter só else
# podemos ter if e elif, sem else
# podemos ter quantos elif's quisermos
# nem if e nem elif, requerem else