import psycopg2
from psycopg2 import Error
from datetime import datetime

current_datetime = datetime.now()
query_result = ()
conn = ()

db_host = '127.0.0.1'
db_port = 5432
db_dbname = 'test'
db_user = 'test'
db_password = 'test'

try:
    conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_dbname, user=db_user, password=db_password)
    cursor = conn.cursor()
    
    create_table_people_query = '''CREATE TABLE people (id INT SERIAL PRIMARY KEY NOT NULL, name VARCHAR (255) NOT NULL, 
                                gender VARCHAR (50) NOT NULL, homeworld VARCHAR (100) NOT NULL), starships VARCHAR (255) 
                                NOT NULL;'''
    cursor.execute(create_table_people_query)

    create_table_sharships_query = '''CREATE TABLE sharships (id INT SERIAL PRIMARY KEY NOT NULL, name VARCHAR (255) NOT NULL, 
                                model VARCHAR (255) NOT NULL, manufacturer VARCHAR (255) NOT NULL), cargo_capacity INT (20) 
                                NOT NULL, ship_id INT (10) NOT NULL;'''
    cursor.execute(create_table_sharships_query)

    create_table_persons_with_sharships_query = '''CREATE TABLE persons_with_sharships (id INT SERIAL PRIMARY KEY NOT NULL, 
                                person_name VARCHAR (255) NOT NULL, ship_id INT (10) NOT NULL;'''
    cursor.execute(create_table_persons_with_sharships_query)

    conn.commit()

except (Exception, Error) as error:
    print("\nSomething wrong with connection\n\n", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print(f"PostgreSQL connection is closed at {current_datetime}")