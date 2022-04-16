#!/usr/local/bin/python

import requests
import psycopg2
import os
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d-%m-%Y, %H:%M:%S")

person_num = 1
person_num_last = 85
starship_num = 1
starship_num_last = 80

data_people = 'https://swapi.dev/api/people/'
data_starships = 'https://swapi.dev/api/starships/'

conn = psycopg2.connect(
  database=os.environ["TF_VAR_db_name"], 
  user=os.environ["TF_VAR_db_user"], 
  password=os.environ["TF_VAR_db_password"], 
  host=os.environ["db_host"], 
  port="5432")

cursor = conn.cursor()

print(f"Started at {date_time}")

while person_num <= person_num_last:
    try:
        data_people_new = data_people + str(person_num)

        resp = requests.get(data_people_new)
        if resp.status_code == 200:
            
            ship_id = ''
            people = requests.get(data_people_new).json()
            person_starships = people['starships']

            for person_starship in person_starships:
                person_starship = requests.get(person_starship).json()
                ship_id = person_starship['url'].strip('/').split('/')[-1]
                person_name = people['name']
                person_gender = people['gender']
                person_homeworld = people['homeworld']
                person_homeworld = requests.get(person_homeworld).json()
                person_homeworld = person_homeworld['name']
            
                fill_table_persons_with_starships = "INSERT INTO persons_with_starships (name, gender, homeworld, ships_id) VALUES (%s, %s, %s, %s)"
                vars_persons = [person_name, person_gender, person_homeworld, ship_id]
                cursor.execute(fill_table_persons_with_starships, vars_persons)

                print(f"Person {person_name} (id {person_num}) with starship id {ship_id} inserted successfully at {date_time}")

        else:
            pass

    except:
        pass

    person_num += 1

conn.commit()
print(f"Data to table 'persons_with_starships' are successfully commited at {date_time}")
print("")

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

            if starship_cargo_capacity == 'unknown':
                starship_cargo_capacity = '0'
            else:
                pass

            starship_cargo_capacity = int(starship_cargo_capacity)
            fill_table_starships = "INSERT INTO starships (name, model, manufacturer, cargo_capacity, ship_id) VALUES (%s, %s, %s, %s, %s)"
            vars_starships = [starship_name, starship_model, starship_manufacturer, starship_cargo_capacity, starship_num]
            cursor.execute(fill_table_starships, vars_starships)
            print(f"Ship {starship_name} - {starship_model} with id {starship_num} inserted successfully at {date_time}")

        else:
            pass
    except:
        pass

    starship_num += 1

conn.commit()
print(f"Data to table 'starships' are successfully commited at {date_time}")
print("")

persons_create_table = '''
    INSERT INTO persons (name, gender, homeworld, ship_model, ship_manufacturer, cargo_capacity)
    SELECT persons_with_starships.name, persons_with_starships.gender, persons_with_starships.homeworld, 
    starships.name, starships.model, starships.cargo_capacity 
    FROM persons_with_starships, starships 
    WHERE persons_with_starships.ships_id=starships.ship_id order by starships.cargo_capacity desc;
    '''
cursor.execute(persons_create_table)
conn.commit()
print(f"Table 'persons' was filled successfully at {date_time}")

if conn:
    cursor.close()
    conn.close()
    print(f"PostgreSQL connection is closed at {date_time}")
