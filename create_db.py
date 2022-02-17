import psycopg2
from psycopg2 import Error
from datetime import datetime

query_result = ()

try:
    conn = psycopg2.connect(host='localhost', 
                        port="5432", 
                        dbname='test', 
                        user='test', 
                        password='test')

    cursor = conn.cursor()
    
    create_table_people = ('''CREATE TABLE people (id SERIAL PRIMARY KEY NOT NULL, name VARCHAR (255) NOT NULL, 
                            gender VARCHAR (50), homeworld VARCHAR (100), ships_id VARCHAR);''')

    cursor.execute(create_table_people)

    create_table_starships = ('''CREATE TABLE starships (id SERIAL PRIMARY KEY NOT NULL, name VARCHAR (255) NOT NULL, model 
                            VARCHAR (255), manufacturer VARCHAR (255), cargo_capacity VARCHAR (255), ship_id VARCHAR (255));''')

    cursor.execute(create_table_starships)

    create_table_persons_with_starships = ('''CREATE TABLE persons_with_starships (id SERIAL PRIMARY KEY NOT NULL, 
                            person_name VARCHAR (255) NOT NULL, ship_id VARCHAR (255) NOT NULL);''')

    cursor.execute(create_table_persons_with_starships)

    conn.commit()

except (Exception, Error) as error:
    print("\nSomething wrong with connection\n\n", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print(f"PostgreSQL connection is closed at {datetime.now()}")