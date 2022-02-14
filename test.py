import json
import urllib.request as request
import requests

person_num = 1
person_num_last = 90

data_people = 'https://swapi.dev/api/people/'

def get_raw_people():
    #people = ''
    resp = requests.get(data_people_new)
    if resp.status_code == 200:
        people = resp.json()
    else:
        print('')
    return people

#def pre_people(raw_data):
#    people_name = raw_data['name']
#    people_gender = raw_data['gender']
#    people_homeworld = raw_data['homeworld']
#    people_starships = raw_data['starships']
#    return people_name, people_gender, people_homeworld, people_starships

while person_num <= person_num_last:
    try:
        data_people_new = data_people + str(person_num)
        people = requests.get(data_people_new).json()
        person_name = people['name']
        person_gender = people['gender']
        person_homeworld = people['homeworld']
        person_starships = people['starships']
        print(person_name, person_gender, person_homeworld, person_starships)
    except:
        pass
    person_num += 1
