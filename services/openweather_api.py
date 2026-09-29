import requests
from config import AppConfig
from common.functions import to_celsius
from common.functions import to_kmh
from common.functions import timestamp
from datetime import datetime

API_KEY = AppConfig.API_KEY # Importujemy klucz z pliku config
API_CITY = AppConfig.API_CITY

def get_weather(): #funkcja która ma służyć do pobierania danych pogodowych
    url = f"https://api.openweathermap.org/data/2.5/weather?q={API_CITY}&appid={API_KEY}"

    try: # powinniśmy zabezpieczyć się przed wyjątkami za pomocą try except
        response = requests.get(url)
        data = response.json()
        weather = {
            "miejsce": data.get("name"),
            "temperatura": to_celsius(data.get("main").get("temp")), # konwersja temp z kelvinów na celsius
            "temperatura_odczuwalna": to_celsius(data.get("main").get("feels_like")), # konwersja temp z kelvinów na celsius
            "predkosc_wiatru": to_kmh(data.get("wind").get("speed")),
            "cisnienie": data.get("main").get("pressure"),
            "wilgotnosc": data.get("main").get("humidity"),
            "zachmurzenie": data.get("clouds").get("all"),
            "godzina_pobrania_danych": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return weather
    except Exception as e:
        print("Error", e)

