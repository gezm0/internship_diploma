import json
import requests

person_num = 1
person_num_last = 90
starship_num = 1
starship_num_last = 50

data_people = 'https://swapi.dev/api/people/'
data_starships = 'https://swapi.dev/api/starships/'

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
        print(person_name, person_gender, person_homeworld, person_starships)
    except:
        pass
    person_num += 1

while starship_num <= starship_num_last:
    try:
        data_starships_new = data_starships + str(starship_num)
        ships = requests.get(data_starships_new).json()
        starship_name = ships['name']
        starship_model = ships['model']
        starship_manufacturer = ships['manufacturer']
        starship_cargo_capacity = ships['cargo_capacity']
        print(starship_name, starship_model, starship_manufacturer, starship_cargo_capacity)
    except:
        pass
    starship_num += 1