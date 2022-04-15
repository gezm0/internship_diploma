#!/usr/bin/python

import psycopg2
import os
from datetime import datetime

# variables for connection passed through environment variables
this_db_user = os.environ["TF_VAR_db_user"]
this_db_password = os.environ["TF_VAR_db_password"]
this_db_name = os.environ["TF_VAR_db_name"]
this_db_host = os.environ["db_host"]

conn = psycopg2.connect(
  database=this_db_name, 
  user=this_db_user, 
  password=this_db_password, 
  host=this_db_host, 
  port="5432"
)

cursor = conn.cursor()

select_output = '''
    select persons_with_starships.name, persons_with_starships.gender, persons_with_starships.homeworld, starships.name, 
    starships.model, starships.cargo_capacity from persons_with_starships, starships 
    where persons_with_starships.ships_id=starships.ship_id 
    order by starships.cargo_capacity desc 
    limit 10;
    '''

cursor.execute(select_output)

rows = cursor.fetchall()
print("The number of parts: ", cursor.rowcount)
for row in rows:
    print(row)
cursor.close()

conn.close()
print(f"PostgreSQL connection is closed at {datetime.now()}")
print("")