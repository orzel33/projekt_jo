import requests
import psycopg2

db_params = psycopg2.connect(
    user="postgres", database="postgres", host="localhost", port="5432", password="geoinformatyka"
)
def remove_phar(db_params)-> None:
    cursor=db_params.cursor()
    sql=f"DELETE FROM public.pharmacies WHERE phar_name='{input('Którą apteke chcesz usunąćz systemu?')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()


def update_phar(db_params)-> None:
    new_name: str = input("Nowa nazwa: ")
    new_location: str = input("Nowy adres i kod pocztowy: ")
    longitude, latitude = get_coordinates(new_location)
    cursor=db_params.cursor()
    sql = f"UPDATE public.pharmacies SET phar_name='{new_name}',  phar_location='{new_location}', phar_cords='SRID=4326;POINT({latitude} {longitude})' WHERE name='{input('Dane której apteki edytować? ')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()