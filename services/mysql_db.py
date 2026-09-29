import mysql.connector as sql # modul do połączenia Python z SQL
from config import AppConfig # pobiera wartości zapisane pod AppConfig z pliku config.py

# Funkcja tworząca połączenie z bazą danych
def get_connection():
    return sql.connect(
        host=AppConfig.DB_HOST, #lokalne IP bo baza jest na moim komputerze
        user=AppConfig.DB_USER, # nazwa którą używaliśmy w mysql server
        password=AppConfig.DB_PASSWORD, # hasło do bazy danych z mysql server
        database=AppConfig.DB_NAME # nazwa bazy danych na której pracuję w SQL i którą chcę zaimportować
)

# def create_weather_table(): # sprawdza czy mamy połączenie
#     connection = get_connection()
#     print(f"Connection: {connection.is_connected()}")

# W tej funkcji jest instrukcja SQL która zostanie wykonana po za pythonem w bazie SQL
def create_weather_table():

    query = """
    CREATE TABLE IF NOT EXISTS records (
        id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        miejsce VARCHAR(255) NOT NULL,
        temperatura FLOAT NOT NULL,
        temperatura_odczuwalna FLOAT NOT NULL,
        predkosc_wiatru FLOAT NOT NULL,
        cisnienie INT NOT NULL,
        wilgotnosc INT NOT NULL,
        zachmurzenie INT NOT NULL,
        godzina_pobrania_danych DATETIME NOT NULL
    )
    """

    try:
        connection = get_connection()
        cursor = connection.cursor() # pozwala wykonywać operacje na bazie danych w SQL
        cursor.execute(query) # cursor wykona kod powyżej
        connection.commit()  # ostateczne zatwierdzenie operacji
        print("Tabela została utworzona lub już istnieje")
    except Exception as e:
        print(e)


def save_weather_record(data):
    query = """
        INSERT INTO records 
        (miejsce, temperatura, temperatura_odczuwalna, 
        predkosc_wiatru, cisnienie, wilgotnosc, 
        zachmurzenie, godzina_pobrania_danych)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data['miejsce'],
        data['temperatura'],
        data['temperatura_odczuwalna'],
        data['predkosc_wiatru'],
        data['cisnienie'],
        data['wilgotnosc'],
        data['zachmurzenie'],
        data['godzina_pobrania_danych']
    )

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        print("Informacja zapisana w MySQL")
    except Exception as e:
        print(e)


def get_weather_records():
    query = """SELECT miejsce, temperatura, godzina_pobrania_danych 
    FROM records ORDER BY godzina_pobrania_danych DESC""" # do portfolio lepiej pisać konkretne kolumny a nie gwiazdkę

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print(e)