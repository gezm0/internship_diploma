import requests
import psycopg2
from datetime import datetime

starship_num = 1
starship_num_last = 80

data_starships = 'https://swapi.dev/api/starships/'

conn = psycopg2.connect(host='localhost', 
                        port="5432", 
                        dbname='test', 
                        user='test', 
                        password='test')

cursor = conn.cursor()

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
            print(starship_name, starship_model, starship_manufacturer, starship_cargo_capacity, starship_num)
            print(f"Ship record number {starship_num} inserted successfully")

        else:
            pass
    except:
        pass

    starship_num += 1

conn.commit()
print(f"Data to table 'starships' are successfully commited at {datetime.now()}")