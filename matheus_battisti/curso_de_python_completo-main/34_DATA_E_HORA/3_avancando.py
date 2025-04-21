# aula 1 - datas recorrentes

import calendar

calendario = calendar.monthcalendar(2025, 2)

domingos = [semana[calendar.SUNDAY] for semana in calendario if semana[calendar.SUNDAY] != 0]

print(f"Domingos de {calendar.month_name[2]} 2025: {domingos}")



calendario_mes = calendar.monthcalendar(2024, 6)

print(calendario_mes)

calendar.setfirstweekday(calendar.SUNDAY)

calendario_mes_2 = calendar.monthcalendar(2024, 6)

print(calendario_mes_2)


for ano in range(2010, 2040):
    if calendar.isleap(ano):
        print(f"{ano} é bissexto")

# aula 2 - pytz
import pytz
from datetime import datetime

zona_ny = pytz.timezone("America/New_York")
data_ny = datetime.now(zona_ny)

print(data_ny)

print(pytz.all_timezones[:100])

zona_br = pytz.timezone("America/Sao_Paulo")

data_br = datetime(2024, 2, 1, tzinfo=zona_br)

print(data_br)


# aula 2 - conversao de fusos horarios
data_sem_fuso = datetime(2024, 12, 25, 14, 0)

zona_paris = pytz.timezone("Europe/Paris")

data_paris = zona_paris.localize(data_sem_fuso)

print(data_sem_fuso)
print(data_paris)

zona_tokyo = pytz.timezone("Asia/Tokyo")

data_tokyo = data_paris.astimezone(zona_tokyo)

print(f"Data em Paris: {data_paris}, Data em Tóquio: {data_tokyo}")

# convreter UTC para local
zona_utc = pytz.UTC
data_utc = datetime.now(zona_utc)

print(data_utc)

zona_india = pytz.timezone("Asia/Kolkata")

data_india = data_utc.astimezone(zona_india)

print(f"Data em India: {data_india}, Data em UTC: {data_utc}")