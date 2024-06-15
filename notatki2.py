import requests
from bs4 import BeautifulSoup
import psycopg2

db_params = psycopg2.connect(
    user="postgres", database="postgres", host="localhost", port="5432", password="geoinformatyka"
)


def get_coordinates(phar_location):
        url = f'https://nominatim.openstreetmap.org/search?format=json&q={phar_location}'
        response = requests.get(url)
        data = response.json()
        if data and len(data) > 0:
            first_result = data[0]
            lat = float(first_result['lat'])
            lon = float(first_result['lon'])
            print(f"Latitude: {lat}")
            print(f"Longitude: {lon}")
            return [lat, lon]
        else:
            print("Nie udało się znaleźć współrzędnych dla podanej lokalizacji.")
            return None

def create_phar(db_params) -> None:
    phar_name: str = input("Wprowadź nazwę apteki: ")
    phar_location: str = input("Wprowadź ulicę i kod pocztowy położenia apteki: ")
    new_phar: dict = {'Nazwa': phar_name, 'location': phar_location}
    longitude, latitude = get_coordinates(phar_location)
    cursor = db_params.cursor()
    sql = f"INSERT INTO public.pharmacies(phar_name, phar_location, phar_coords) VALUES('{phar_name}', '{phar_location}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()
create_phar(db_params)


def read_phar(db_params) -> None:
    cursor = db_params.cursor()
    sql = f"SELECT * FROM public.pharmacies"
    cursor.execute(sql)
    users = cursor.fetchall()
    cursor.close()
