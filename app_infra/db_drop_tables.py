#!/usr/local/bin/python

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

list_tables = ['starships', 'persons_with_starships']
for table_to_drop in list_tables:

  drop_table = (f"DROP table {table_to_drop};")
  print(f"Table {table_to_drop} deleted successfully at {datetime.now()}")
  cursor.execute(drop_table)
  conn.commit()

cursor.close()
conn.close()
print(f"PostgreSQL connection is closed at {datetime.now()}")
print("")