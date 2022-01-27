# for work with database
import psycopg2
# for work with site through API
import requests

# request data through AIP section

# from where get data
data_people = f"https://swapi.dev/api/people/"
data_starships = f"https://swapi.dev/api/starships/"

# work with data about people
def get_raw_sw_data_people():
    resp = requests.get(data_people)
    if resp.status_code == 200:
        sw_data_people = resp.json()
    else:
        print('We have some issues')
    return sw_data_people
print(get_raw_sw_data_people())

# work with data about starships
def get_raw_sw_data_starships():
    resp = requests.get(data_starships)
    if resp.status_code == 200:
        sw_data_starships = resp.json()
    else:
        print('We have some issues')
    return sw_data_starships
print(get_raw_sw_data_starships())

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
