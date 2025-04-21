# Aula 1 - While
contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1

senha = ""

'''
while senha != "12345":
    senha = input("Digite a senha: ")

print("Bem vindo ao sistema")
'''

x = 10

while x > 0:
    print(x)
    x -= 1

numero = 0

'''
while True:
    numero = int(input("Digite um numero positivo"))

    if numero > 0:
        print("Numero positivo")
        break
'''

# Aula 2 - for

frutas = ["Maçã", "banana", "Limão"]

for fruta in frutas:
    print(f"Fruta: {fruta}")

# i => frutas[i]

for i, fruta in enumerate(frutas):
    print(f"Fruta: {fruta} referente ao indice {i}")


for numero in range(1, 6):
    print(numero)

for fruta in frutas:
    if "a" in fruta:
        print(f"Fruta {fruta} tem a letra 'a'")

# aula 3 - Range
for i in range(5):
    print(f"i = a {i}")

for i in range(3, 16, 3):
    print(f"I = {i}")

for i in range(10, 0, -1):
    print(f"i = {i}")

numeros = [10, 20, 30, 40]

for i in range(len(numeros)):
    print(f"i = {i}, acessando array {numeros[i]}")

# aula 4 - strings, listas e dicionarios

texto = "Python"

for letra in texto:
    print(f"Letra: {letra}")


dados = {
    "nome": "Matheus",
    "idade": 33,
    "esta_trabalhando": True
}

for chave in dados:
    print(f"Chave {chave} - Valor {dados[chave]}")

print(dados['nome'])

for chave, valor in dados.items():
    print(f"{chave} - {valor}")