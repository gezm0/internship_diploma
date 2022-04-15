#!/usr/local/bin/python

import psycopg2
import os
from psycopg2 import Error
from datetime import datetime

query_result = ()

try:
    conn = psycopg2.connect(
        database=os.environ["TF_VAR_db_name"], 
        user=os.environ["TF_VAR_db_user"], 
        password=os.environ["TF_VAR_db_password"], 
        host=os.environ["db_host"], 
        port="5432")

    cursor = conn.cursor()
    
    create_table_starships = ('''CREATE TABLE starships (id SERIAL PRIMARY KEY NOT NULL, name VARCHAR (255) NOT NULL, model 
                            VARCHAR (255), manufacturer VARCHAR (255), cargo_capacity bigint, ship_id INT);''')

    cursor.execute(create_table_starships)
    print(f"Table 'starships' created successfully at {datetime.now()}")

    create_table_persons_with_starships = ('''CREATE TABLE persons_with_starships (id SERIAL PRIMARY KEY NOT NULL, 
                            name VARCHAR (255) NOT NULL, gender VARCHAR (50), homeworld VARCHAR (100), ships_id INT);''')

    cursor.execute(create_table_persons_with_starships)
    print(f"Table 'persons_with_starships' created successfully at {datetime.now()}")

    conn.commit()

except (Exception, Error) as error:
    print("\nSomething wrong with connection\n\n", error)

finally:
    if conn:
        cursor.close()
        conn.close()
        print(f"PostgreSQL connection is closed at {datetime.now()}")
        print("")