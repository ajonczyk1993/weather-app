

# def to_celsius(temp): # to samo co poniżej
#     return round( temp - 273.15 , 2)

to_celsius = lambda temp: round( temp - 273.15, 2) # konwersja temp z kelvinów na celsius

# 1. Utwórz funkcję, która przelicza m / s na km / h

to_kmh = lambda speed: speed * 3.6

# 2. Utwórz funkcję, która wyświetla aktualną datę w formacie y-m-d h-m-s

from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Zaimportuj obie funkcje i użyj ich w openweather_api