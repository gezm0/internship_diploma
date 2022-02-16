from unittest import skip
import requests
import psycopg2
from datetime import datetime

person_num = 1
person_num_last = 90
starship_num = 1
starship_num_last = 100

starship_name = ''
starship_model = ''
starship_manufacturer = ''
starship_cargo_capacity = ''

data_people = 'https://swapi.dev/api/people/'
data_starships = 'https://swapi.dev/api/starships/'

current_datetime = datetime.now()

conn = psycopg2.connect(host='localhost', 
                        port="5432", 
                        dbname='test', 
                        user='test', 
                        password='test')

cursor = conn.cursor()

while person_num <= person_num_last:
    try:
        data_people_new = data_people + str(person_num)

        resp = requests.get(data_people_new)
        if resp.status_code == 200:

            people = requests.get(data_people_new).json()
            person_name = people['name']
            person_gender = people['gender']
            person_homeworld = people['homeworld']
            person_homeworld = requests.get(person_homeworld).json()
            person_homeworld = person_homeworld['name']
            person_starships = people['starships']

            fill_table_people = f"INSERT INTO people (name, gender, homeworld) VALUES ('{person_name}', '{person_gender}', '{person_homeworld}');"
            cursor.execute(fill_table_people)
            print(f"Person record number {person_num} inserted successfully")

        else:
            pass

    except:
        pass

    person_num += 1

conn.commit()
print('Data to table "people" are successfully commited')

while starship_num <= starship_num_last:
    try:
        data_starships_new = data_starships + str(starship_num)

        resp = requests.get(data_starships_new)
        if resp.status_code == 200:

            ships = requests.get(data_starships_new).json()
            starship_name = ships['name']
            starship_model = ships['model']
            starship_manufacturer = ships['manufacturer']
            starship_cargo_capacity = ships['cargo_capacity']

            fill_table_starships = f"INSERT INTO starships (name, model, manufacturer, cargo_capacity, ship_id) VALUES ('{starship_name}', '{starship_model}', '{starship_manufacturer}', '{starship_cargo_capacity}', '{starship_num}');"
            cursor.execute(fill_table_starships)
            print(f"Ship record number {starship_num} inserted successfully")

        else:
            pass
    except:
        pass

    starship_num += 1

conn.commit()
print('Data to table "starships" are successfully commited')

if conn:
    cursor.close()
    conn.close()
    print(f"PostgreSQL connection is closed at {current_datetime}")
