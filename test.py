from asyncio.windows_events import NULL
import requests
from datetime import datetime

person_num = 1
person_num_last = 10

data_people = 'https://swapi.dev/api/people/'

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
            ship_id_list = []

            for person_starship in person_starships:
                person_starship = requests.get(person_starship).json()
                ship_id = person_starship['url'].strip('/').split('/')[-1]
                person_starship_name = person_starship['name']
                ship_id_list.append(ship_id)

            print(person_name, person_gender, person_homeworld, ship_id_list)

        else:
            pass

    except:
        pass

    person_num += 1