# aula 1 - intro seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("produtos.csv")

# sns.barplot(x="Categoria", y="Quantidade", data=df)
# plt.title("Quantidade Total por Categoria")
# plt.show()

# sns.scatterplot(x="Preço", y="Quantidade", hue="Categoria", data=df)
# plt.show()

# aula 2 - graficos avancados

# sns.boxplot(x="Categoria", y="Preço", data=df)
# plt.title("Boxplot de Preços e Categorias")
# plt.show()

# heatmap_data = df.pivot_table(index="Categoria", columns='Produto', values='Quantidade', aggfunc="sum").fillna(0)

# sns.heatmap(heatmap_data, annot=True, cmap="coolwarm")
# plt.title("Heatmap de Quantidades por Produto e Categoria")
# plt.show()

# sns.pairplot(df[['Preço', 'Quantidade']])
# plt.title("Pairplot")
# plt.show()

# aula 3 - estilizando seaborn
sns.set_theme(style="darkgrid", palette="pastel")
#sns.set_palette(sns.color_palette("coolwarm"))
sns.set_context("poster", font_scale=.9)
sns.barplot(x="Categoria", y="Quantidade", data=df)
plt.title("Quantidade Total por Categoria")
plt.show()