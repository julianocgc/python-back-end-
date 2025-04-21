# aula 1 - manip. de data e hora

from datetime import datetime, timedelta, date, time

print(f"Data e hora atual: {datetime.now()}")

data_inicio = datetime.now()

data_consulta = data_inicio + timedelta(days=7)

print(data_consulta)

# aula 2 - datetime

data = date(2024, 5, 12)

print(data)

tempo = time(13, 33, 12)

print(tempo)

data_com_horario = datetime(2020, 10, 20, 14, 30, 10)
data_com_horario_2 = datetime(2021, 12, 24, 14, 30, 10)

print(data_com_horario)

diferenca = data_com_horario_2 - data_com_horario

print(diferenca)

# aula 3 - extraindo info de datas

print(f"Dia: {data_inicio.day} Mês: {data_inicio.month} Ano: {data_inicio.year}")

print(f"Dia da semana: {data_inicio.weekday()}") # 0 = segunda-feira

print(f"Hora: {data_inicio.hour} Minuto: {data_inicio.minute} Segundos: {data_inicio.second}")

print(data_inicio.isoformat())
print(data_inicio)

# aula 4 - formatacao

print(data.strftime("%d/%m/%Y"))
print(data.strftime("%d/%m/%y"))

print(data_inicio.strftime("%d/%m/%Y %H:%M:%S"))
print(data_inicio.strftime("%d-%m-%Y"))

print(data_inicio.strftime("%A, %d de %B de %Y"))