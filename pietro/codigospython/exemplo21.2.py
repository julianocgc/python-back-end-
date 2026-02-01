lista_pessoas = []

for _ in range(3):
    pessoa = {}
    pessoa["nome"] = input("Digite seu nome: ")
    pessoa["peso"] = float(input("Digite seu peso: "))
    pessoa["idade"] = int(input("Digite sua idade: "))
    lista_pessoas.append(pessoa)

print("Dados das pessoas: ")
for pessoa in lista_pessoas:
    print()
    print("Nome: ", pessoa["nome"])
    print("Peso: ", pessoa["peso"])
    print("Idade: ", pessoa["idade"])
