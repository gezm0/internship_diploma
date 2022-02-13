from unicodedata import name
import psycopg2
import requests

# request data through AIP section

person_num = 1
data_people = f"https://swapi.dev/api/people/"
data_people_new = ''
people = '[]'

def get_raw_people():
    resp = requests.get(data_people_new)
    if resp.status_code == 200:
        people = resp.json()
    else:
        print('We have some issues')
    return people

def pre_people(raw_data):
    people_name = raw_data['name']
    people_gender = raw_data['gender']
    people_homeworld = raw_data['homeworld']
    people_starships = raw_data['starships']
    return people_name, people_gender, people_homeworld, people_starships

while person_num <= 50:
    data_people_new = data_people + str(person_num)
    person = pre_people(get_raw_people())
    p_name = person[0]
    p_gender = person[1]
    p_homeworld = person[2]
    p_starships = person[3]
    print(p_name, p_gender, p_homeworld, p_starships)
    person_num = person_num + 1

# work with data about starships
#def get_raw_sw_data_starships():
#    resp = requests.get(data_starships)
#    if resp.status_code == 200:
#        sw_data_starships = resp.json()
#    else:
#        print('We have some issues')
#    return sw_data_starships
#print(get_raw_sw_data_starships())

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
