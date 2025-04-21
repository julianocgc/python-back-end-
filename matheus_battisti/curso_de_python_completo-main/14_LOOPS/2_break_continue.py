# aula 1 - break
for numero in range(1, 50):
    print("Numero: ", numero)

    if numero % 7 == 0:
        print("Encontramos o numero ", numero)

        break

'''
while True:
    comando = input("Digite 'sair' para encerrar: ")
    if comando.lower() == 'sair':
        print("Encerrando programa...")
        break

    print(comando)
'''

frutas = ['maçã', 'banana', 'uva', 'laranja']

for fruta in frutas:
    print(fruta)

    if fruta == 'uva':
        print("Encontramos a uva...")
        break


# aula 2- continue
numeros = [1, -3, 4, -5, 9, -2]

for numero in numeros:
    if numero < 0:
        continue
    print("O numero é ", numero)

texto = "Python3.12348"

for letra in texto:
    if not letra.isalpha():
        continue
    print("Letra: ", letra)

for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)

# break encerra o loop
# continue pula para a prox. execução


print("aula 3")

# Aula 3 - combinacao de break e continue
for numero in range(1, 20):
    if numero % 2 != 0:
        continue
    if numero % 5 == 0:
        print(f"Primeiro numero divisivel por 5: {numero}")
        break
    print(numero)

for numero in numeros:
    if numero < 0:
        continue
    
    elif numero > 5:
        print("Numero maior que o previsto, parando loop...")
        break

    print(numero)