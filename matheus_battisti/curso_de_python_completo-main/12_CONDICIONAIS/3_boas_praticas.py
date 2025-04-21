# Aula 1 - condicionais em processamento de dados
dados = [10, -5, 8, 0, -1]

dados_validos = [x for x in dados if x > 0]

# percorrer todos os numeros
# vai incluir no array novo somente quem for maior q 0
print(dados_validos)

idades = [10, 15, 20, 23, 12, 18, 44, 60]

categorias = [
    "Criança" if idade < 13 else "Adolescente" if idade < 18 else "Adulto" for idade in idades
]

print(categorias)


# Aula 2

idade = 20

maioridade = 18

maior_de_idade = idade >= maioridade

print(maior_de_idade)

# hard coded = quando o dado é escrito pelo dev, nao vem de uma variável ou Banco de dados

