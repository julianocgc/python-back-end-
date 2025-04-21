# aula 1- intro ao plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("pessoas.csv")

#fig = px.bar(df, x="Cargo", y="Salário", color="Departamento", title="Salário Médio por Cargo")
#fig.show()

# fig = px.scatter(df, x="Salário", y="Localização", color="Cargo", size="Salário", title="Dispersão Salários por Localização")
# fig.show()

# fig = px.pie(df, names="Departamento", values="Salário", title="Distribuição de Salário por departamento")
# fig.show()

# aula 2 - graficos avancados

# heatmap_data = df.pivot_table(index="Departamento", columns="Cargo", values="Salário", aggfunc="mean").fillna(0)

# fig = px.imshow(heatmap_data, title="Salários médios por departamento e cargo", color_continuous_scale="Viridis")

# fig.show()

fig = px.scatter_3d(df, x="Salário", y="Departamento", z="Localização", color="Cargo", title="Gráfico 3D")

fig.show()