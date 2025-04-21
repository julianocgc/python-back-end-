# baseado no ano de nascimento do usuario
# calcular a idade dele
# 2024 ou 2025
from datetime import datetime

# datetime ->> varias funcionalidades para lidar com datas
ano_atual = datetime.now().year

ano_nascimento = int(input("Em que ano você nasceu?"))

idade = ano_atual - ano_nascimento

print("Você tem", idade, "anos")