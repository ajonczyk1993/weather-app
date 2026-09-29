from services.openweather_api import get_weather
from services.files import create_excel, read_file
from services.dashboard import render
from services.mysql_db import create_weather_table, save_weather_record, get_weather_records
import time

# data = read_file()
# print(data)

create_weather_table() # tworzy tabelę danych w SQL zgodnie z funkcją w mysql_db.py

# x = get_weather_records() # uruchamia funkcję z mysql_db.py która pobiera dane z bazy SQL które wcześniej tam zapisaliśmy
# print(x)
# while True:
#     #1. Pobranie danych pogodowych
#     weather = get_weather()
#     #2. Wrzucenie danych do serwisu files - funkcji create_excel
#     # [weather] w liście bo pandas do DF oczekuje listy
#     create_excel([weather])
#     save_weather_record(weather)
#     print("Pobieram dane pogodowe")

    time.sleep(15) # co 15 sekund uruchamia funkcje od nowa, czyli pobiera dane pogodowe i zapisuje w SQL

# placeholder: threads

# if "__main__" == __name__:
#     render()