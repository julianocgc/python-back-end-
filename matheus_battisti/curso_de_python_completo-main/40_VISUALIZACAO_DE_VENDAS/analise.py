"""
Cenário - A Solicitação do Gestor
O gestor de uma rede de lojas, Carlos, está preocupado com a performance de vendas de diferentes produtos 
nas cinco regiões onde a empresa atua. 
Ele quer compreender melhor os dados de vendas para tomar decisões estratégicas. 

Carlos faz as seguintes solicitações:

Resumo Geral: 

"Preciso entender o desempenho geral das vendas ao longo do tempo. 
Por favor, gere um gráfico que mostre as quantidades vendidas ao longo dos dias para 
identificarmos tendências de vendas."

Vendas por Produto: 

"Gostaria de ver a quantidade total vendida por cada produto. 
Um gráfico de barras seria ótimo para visualizar isso."

Distribuição Regional: 

"Como estão as vendas por região? Um gráfico de pizza poderia mostrar qual região está contribuindo mais."

Detalhes por Categoria e Região: 

"Consigo ver a relação entre categorias de produtos e regiões? Um heatmap seria ideal para isso."

Acompanhamento de Produtos Populares: 

"Quais produtos têm um desempenho consistente ao longo do tempo? 
Um gráfico de linha detalhado por produto pode ajudar."

"""
import pandas as pd
import plotly.express as px

df = pd.read_csv("dados_vendas_dashboard.csv")

print(df.head())

# Resumo Geral
resumo_geral = df.groupby("Data_Venda").sum(numeric_only=True).reset_index()

fig1 = px.line(
    resumo_geral,
    x="Data_Venda",
    y="Quantidade",
    title="Resumo Geral: Vendas ao Longo do Tempo",
    labels={'Quantidade': 'Quantidade Vendida', 'Data_Venda': 'Data'}
)
#fig1.show()

# 2 Vendas Por produto: qtd total vendida por prod
vendas_por_produto = df.groupby("Produto").sum(numeric_only=True).reset_index()

fig2 = px.bar(
    vendas_por_produto,
    x="Produto",
    y="Quantidade",
    color="Produto",
    title="Vendas Por Produto"
)

#fig2.show()

# 3 Distribuicao regional
vendas_por_regiao = df.groupby("Região").sum(numeric_only=True).reset_index()

fig3 = px.pie(
    vendas_por_regiao,
    names="Região",
    values="Quantidade",
    title="Distribuição Regional"
)

#fig3.show()

# 4 Relacao entre categorias de produtos e regiões
heatmap_data = df.pivot_table(index="Região", columns="Categoria", values="Quantidade", aggfunc="sum").fillna(0)

fig4 = px.imshow(
    heatmap_data,
    title="Relação entre Categorias e Regiões"
)

#fig4.show()

# 5 Acompnhamento de produtos populares
produtos_populares = df.groupby(['Data_Venda', 'Produto']).sum(numeric_only=True).reset_index()

fig5 = px.line(
    produtos_populares,
    x="Data_Venda",
    y="Quantidade",
    color="Produto",
    title="Acompanhamento de Produtos Populares"
)

fig5.show()