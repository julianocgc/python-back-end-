# aula 1 - parsing de strings para datas
from datetime import datetime, timedelta

data = datetime.strptime("25/12/2024", "%d/%m/%Y")

print(data)

data_hora = datetime.strptime("25/10/2015 14:30", "%d/%m/%Y %H:%M")

print(data_hora)

try:
    data_invalida = datetime.strptime("200/10/24", "%d/%m/%Y")
except ValueError as e:
    print(f"Erro ao converter data: {e}")

# aula 2- calculo com datas

data1 = datetime(2024, 12, 25)
data2 = datetime(2025, 9, 12)

diferenca = data2 - data1

print(diferenca.days)

nova_data = data1 + timedelta(days=5)
nova_data_semanas = data1 - timedelta(weeks=3)

print(nova_data)
print(nova_data_semanas)

periodo = timedelta(days=3, hours=3)

data_evento = data1 + periodo

print(data_evento)

# aula 3 - time
import time

timestamps = time.time()

print(timestamps)

# converter timestamp para data legivel
data_legivel = time.ctime(timestamps)

print(data_legivel)

print("Parando")
# #time.sleep(2)
print("Continuando")

# medir o tempo de execucao de um codigo

inicio = time.time()

# for _ in range(100000000):
#    pass

fim = time.time()

print(f"Tempo de execução em segundos: {fim - inicio}")

# aula 4 -modulo calendar

import calendar

print(calendar.month(2024, 12))

print(calendar.calendar(2025))

print(calendar.isleap(2024))
print(calendar.isleap(2025))
print(calendar.isleap(2026))
print(calendar.isleap(2027))
print(calendar.isleap(2028))

dias = calendar.monthcalendar(2024, 11)

print(dias)