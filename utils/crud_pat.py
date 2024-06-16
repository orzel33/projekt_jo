import psycopg2

db_params = psycopg2.connect(
    user="postgres", database="postgres", host="localhost", port="5432", password="geoinformatyka"
)


def read_pat(db_params) -> None:
    cursor = db_params.cursor()
    sql = f"SELECT * FROM public.patients"
    cursor.execute(sql)
    patients = cursor.fetchall()
    cursor.close()
    for patient in patients:
        print(patient)


read_pat(db_params)


def create_pat(db_params) -> None:
    pat_name = input("Podaj imię i nazwisko pacjenta: ")
    pat_phar = input("Podaj nazwę apteki, która obsługuje pacjenta: ")
    pat_drug = input("Podaj nazwę leku przepisanego pacjentowi: ")
    cursor = db_params.cursor()
    cursor.execute("SELECT phar_location FROM public.pharmacies WHERE phar_name = %s", (pat_phar,))
    result = cursor.fetchone()
    if result:
        phar_location = result[0]
        cursor.execute(
            "INSERT INTO public.patients (pat_name, pat_phar, pat_drug)"
            "VALUES (%s, %s, %s)", (pat_name, pat_phar, pat_drug))
        db_params.commit()
        print("Pacjent został dodany do bazy danych.")
    else:
        print("Nie znaleziono apteki o podanej nazwie.")
    cursor.close()
    db_params.close()


create_pat(db_params)
