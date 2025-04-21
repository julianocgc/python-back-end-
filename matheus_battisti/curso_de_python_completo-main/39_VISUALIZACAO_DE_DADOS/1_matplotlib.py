# aula 1 - intro a visualizacao de dados
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

#plt.plot(x, y)
#plt.title("Gráfico de Linha")
#plt.show()

categorias = ["A", "B", "C"]
valores = [5, 7, 3]

#plt.bar(categorias, valores, color="blue")
#plt.title("Gráfico de Barras")
#plt.show()

x = [1, 2, 3, 4, 5, 7]
y = [10, 15, 30, 36, 50, 60]

#plt.scatter(x, y, color="red")
#plt.title("Gráfico de Dispersão")
#plt.show()

# aula 2 - fundamentos matplotlib

# plt.plot(x, y, label="Linha")
# plt.title("Gráfico de Linha com Título")
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")
# plt.legend()
# plt.show()

# plt.plot(x, y, color="purple", linestyle="--", marker="o")
# plt.title("Grafico 2")
# plt.grid()
# plt.show()

# aula 3 - personalizacao de graficos
# y2 = [1, 11, 22, 33, 44, 66]
# plt.plot(x, y, linewidth=6, label="Linha 1")
# plt.plot(x, y2, label="Linha 2", linestyle="dotted", color="green")
# plt.xlim(0, 6)
# plt.ylim(0, 65)
# plt.legend(loc="lower left")
# plt.show()

# aula 4 - subplot e layouts

# fig, axs = plt.subplots(2, 1)

# axs[0].plot(x, y, 'r')
# axs[0].set_title("Subplot 1")
# axs[1].bar(categorias, valores)
# axs[1].set_title("Subplot 2")
# plt.tight_layout()
# plt.show()

# fig, axs = plt.subplots(3, 2)

# axs[0, 0].plot(x, y, 'g')
# axs[0, 1].scatter(x, y, color='orange')

# axs[1, 0].bar(categorias, valores)
# axs[1, 1].plot(x, y, 'g', color="red")

# plt.tight_layout()
# plt.show()

# aual 5 - estilos e temas

# plt.style.use("ggplot")
# plt.plot(x, y, label="Dados com ggplot")
# plt.legend()
# plt.show()

plt.style.use("bmh")
plt.plot(x, y, label="Dados com dark_background", color="purple", linestyle="--", marker="o")
plt.legend()
plt.show()

print(plt.style.available)