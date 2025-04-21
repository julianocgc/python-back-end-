# Aula 1 - criacao de dicionarios
dic = {"nome": "Matheus", "idade": 30}

dic2 = dict(cidade="São Paulo", estado="SP", populacao=4742743274)

print(dic)

print(dic2)

dic_vazio = {}

print(dic_vazio)

pares = [("a", 1), ("b", 2), ("c", 3)]

dic_tuplas = dict(pares)

print(dic_tuplas)

# Aula 2- Manipulacao de dicionarios
dic["profissao"] = "Programador"

print(dic)

dic["nome"] = "Matheus Battisti"

print(dic)

valor_excluido = dic.pop("idade")

print(valor_excluido)

print(dic)

del dic["nome"]

print(dic)

dic.clear()

print(dic)

# Erro chave n existente = del dic["teste"]

dic["cidade"] = "Rio de Janeiro"

print(dic)

# Aula 3 - acesso de valores
pessoa = {"nome": "Matheus", "idade": 30, "profissao": "Programador"}

print(pessoa["idade"])
print(pessoa['idade'])

# Erro -> chave inexistente print(pessoa["teste"])

print(pessoa.get("teste"))

if 'teste' in pessoa:
    print("chave existe")
else:
    print("chave NAO existe")

print(len(pessoa))

# Aula 4 - metodos de dicionario
chaves = pessoa.keys()
valores = pessoa.values()
itens = pessoa.items()

print(list(chaves))
print(list(valores))
print(list(itens)) # tuplas