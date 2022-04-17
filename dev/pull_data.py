import json
#from unicodedata import name
import psycopg2
import requests

# request data through AIP section

person_num = 1
person_num_last = 90
starship_num = 1
starship_num_last = 50

data_people = f"https://swapi.dev/api/people/"
data_starships = f"https://swapi.dev/api/starships/"

def get_raw_people():
    #people = ''
    resp = requests.get(data_people_new)
    if resp.status_code == 200:
        people = resp.json()
    else:
        print('')
    return people

def get_raw_starships():
    #starships = ''
    resp = requests.get(data_starships_new)
    if resp.status_code == 200:
        starships = resp.json()
    else:
        print('')
    return starships

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
    person_num += 1

def pre_starships(raw_data):
    starship_name = raw_data['name']
    starship_model = raw_data['model']
    starship_manufacturer = raw_data['manufacturer']
    starship_cargo_capacity = raw_data['cargo_capacity']
    return starship_name, starship_model, starship_manufacturer, starship_cargo_capacity

while starship_num <= starship_num_last:
    try:
        data_starships_new = data_starships + str(starship_num)
        starship = pre_starships(get_raw_starships())
        s_name = starship[0]
        s_model = starship[1]
        s_manufacturer = starship[2]
        s_cargo_capacity = starship[3]
        print(s_name, s_model, s_manufacturer, s_cargo_capacity)
    except:
        pass
    starship_num += 1

# todo
# work with raw data

# database section
# define connection method
#conn = psycopg2.connect(host='127.0.0.1', 
#                        port="5432", 
#                        dbname='test', 
#                        user='test', 
#                        password='test')

# checking the connection status and displaying the result
#if conn:
#        print('All OK')
#else:
#        print('Something wrong with connection')
#        breakpoint

#cursor = conn.cursor()                  # need for working with database
