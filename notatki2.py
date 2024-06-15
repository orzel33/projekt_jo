import requests
from bs4 import BeautifulSoup
import psycopg2

db_params = psycopg2.connect(
    user="postgres", database="postgres", host="localhost", port="5432", password="geoinformatyka"
)
def get_coordinates(phar_location)->None:

    url:str=f'https://www.openstreetmap.org/search?query={phar_location}'
    response=requests.get(url)
    print(response.text)
    response_html = BeautifulSoup(response.text, 'html.parser')
    response_html_lat: list = response_html.select('minlat')[1].text.replace(',', '.')
    response_html_lng: list = response_html.select('minlon')[1].text.replace(',', '.')
    print(response_html_lat)
    print(response_html_lng)
    return [response_html_lat, response_html_lng]

def create_phar(db_params)-> None:

    phar_name: str = input("Wprowadź nazwę apteki: ")
    phar_location: str = input("Wprowadź ulicę i kod pocztowy położenia apteki: ")
    new_phar: dict = {'Nazwa': phar_name,'location': phar_location}
    longitude,latitude=get_coordinates(phar_location)
    cursor=db_params.cursor()
    sql=f"INSERT INTO public.pharmacies(phar_name, phar_location , phar_coords) VALUES('{phar_name}','{phar_location}', 'SRID=4326;POINT({latitude} {longitude})');"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()
create_phar(db_params)

def read_phar(db_params, pharmacies=None)-> None:
    cursor=db_params.cursor()
    sql=f"SELECT * FROM public.pharmacies"
    cursor.execute(sql)
    users=cursor.fetchall()
    cursor.close()
    for phar in pharmacies:
        print(phar)