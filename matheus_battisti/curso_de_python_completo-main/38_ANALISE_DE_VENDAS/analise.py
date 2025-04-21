import pandas as pd

df = pd.read_csv('vendas_100.csv')

print("=== Dados de Vendas ===")
print(df.head())

# Criar uma nova coluna com o valor total de venda
df["Valor_Total"] = df["Quantidade"] * df["Preço_Unitário"] * (1 - df['Desconto'])

print("=== Dados com Valor Total ===")
print(df.head())

# Análise de vendas por cidade
vendas_por_cidade = df.groupby("Cidade")["Valor_Total"].sum()

print("=== Total de Vendas por Cidade ===")
print(vendas_por_cidade)

# Análise Produto mais vendido
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()

print("=== Produto Mais Vendido ===")
print(f"O produto mais vendido foi: {produto_mais_vendido}")

# Análise Receita total da empresa
receita = df["Valor_Total"].sum()
print("=== A Receita Total da Empresa ===")
print(f"A receita total foi de R${receita:.2f}")

# Análise Receita por Categoria
receita_por_categoria = df.groupby("Categoria")["Valor_Total"].sum()

print("=== Receita por Categoria ===")
print(receita_por_categoria)

# Salvar os resultados das análises em CSV
resultados_arquivo = "analise_vendas.csv"
df.to_csv(resultados_arquivo)
vendas_por_cidade.to_csv("vendas_por_cidade.csv", header=["Total_Vendas"])
receita_por_categoria.to_csv("receita_por_categoria.csv", header=["Receita_Total"])
print("Resultados salvos nos arquivos receita_por_categoria.csv e vendas_por_cidade.csv")