#import json
import requests
import psycopg2
from psycopg2 import Error
from datetime import datetime

person_num = 1
person_num_last = 9
starship_num = 1
starship_num_last = 5

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
        people = requests.get(data_people_new).json()
        person_name = people['name']
        person_gender = people['gender']
        person_homeworld = people['homeworld']
        person_homeworld = requests.get(person_homeworld).json()
        person_homeworld = person_homeworld['name']
        person_starships = people['starships']
        fill_table_people = f"INSERT INTO people (name, gender, homeworld, starships) VALUES ({person_name}, {person_gender}, {person_homeworld}, {person_starships});"
        cursor.execute(fill_table_people)
        conn.commit()

    except:
        pass
  
    print(f"Person record number {person_num} inserted successfully")
    person_num += 1

while starship_num <= starship_num_last:
    try:
        data_starships_new = data_starships + str(starship_num)
        ships = requests.get(data_starships_new).json()
        starship_name = ships['name']
        starship_model = ships['model']
        starship_manufacturer = ships['manufacturer']
        starship_cargo_capacity = ships['cargo_capacity']
        fill_table_starships = f"INSERT INTO starships (name, model, manufacturer, cargo_capacity, ship_id) VALUES ({starship_name}, {starship_model}, {starship_manufacturer}, {starship_cargo_capacity}, {starship_num});"
        cursor.execute(fill_table_starships)
        conn.commit()
    except:
        pass

    print(f"Ship record number {starship_num} inserted successfully")
    starship_num += 1

if conn:
    cursor.close()
    conn.close()
    print(f"PostgreSQL connection is closed at {current_datetime}")