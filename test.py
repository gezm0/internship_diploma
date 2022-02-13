import json
import requests

person_num = 1
person_num_last = 90

data_people = f"https://swapi.dev/api/people/"

def get_raw_people():
    #people = ''
    resp = requests.get(data_people_new)
    if resp.status_code == 200:
        people = resp.json()
    else:
        print('')
    return people

def pre_people(raw_data):
    people_name = raw_data['name']
    people_gender = raw_data['gender']
    people_homeworld = raw_data['homeworld']
    people_starships = raw_data['starships']
    return people_name, people_gender, people_homeworld, people_starships

while person_num <= person_num_last:
    try:
        data_people_new = data_people + str(person_num)
        person = pre_people(get_raw_people())
        p_name = person[0]
        p_gender = person[1]
        p_homeworld = person[2]
        name_homeworld = requests.get(p_homeworld)
        name_homeworld = name_homeworld.text
        p_homeworld = json.loads(name_homeworld)
        p_homeworld = p_homeworld['name']
        p_starships = person[3]
        print(p_name, p_gender, p_homeworld, p_starships)
    except:
        pass
    person_num = person_num + 1
