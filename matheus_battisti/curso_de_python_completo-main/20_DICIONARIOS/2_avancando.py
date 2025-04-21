# Aula 1 - iterando em dicionarios
produto = {"nome": "Camisa", "preço": 21, "cor": "Preta"}

for chave in produto:
    print(chave)
    print(produto[chave])
    if chave == "nome":
        print("O nome do produto é " + produto[chave])

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f"{chave} - {valor}")


# Aula 2 - Compreensão de dicionários
numeros = [1, 2, 3, 4]

quadrados = {num: num ** 2 for num in numeros}

print(quadrados)

filtrar = {chave: valor for chave, valor in produto.items() if isinstance(valor, int)}

print(filtrar)

# Aula 3 - Dicionarios aninhados
usuarios = {
    "user1": {"nome": "Matheus", "email": "matheus@gmail.com"},
    "user2": {"nome": "Maria", "email": "maria@gmail.com"},
}

print(usuarios["user1"]["email"])
print(usuarios["user2"]["nome"])

for user, info in usuarios.items():
    print(f"Dados do usuario: {user}")
    for key, value in info.items():
        print(f"{key} - {value}")

usuarios2 = [
    {"nome": "Matheus", "email": "matheus@gmail.com"},
    {"nome": "Maria", "email": "maria@gmail.com"},
]

for user in usuarios2:
    print(f"Dados do usuario: {user}")
    for key, value in user.items():
        print(f"{key} - {value}")


# aula 4 - boas praticas
id_produto = produto.get("id")

print(id_produto)

config = dict.fromkeys(["tema", "volume", "brilho"], "Padrão")

print(config)

produto_copia = produto.copy()

produto_copia['preço'] = 50

print(produto)
print(produto_copia)