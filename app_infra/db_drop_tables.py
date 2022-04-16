#!/usr/local/bin/python

import psycopg2
import os
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d-%m-%Y, %H:%M:%S")

conn = psycopg2.connect(
  database=os.environ["TF_VAR_db_name"], 
  user=os.environ["TF_VAR_db_user"], 
  password=os.environ["TF_VAR_db_password"], 
  host=os.environ["db_host"], 
  port="5432")

cursor = conn.cursor()

list_tables = ['starships', 'persons_with_starships', 'persons']
for table_to_drop in list_tables:

  drop_table = (f"DROP table {table_to_drop};")
  print(f"Table {table_to_drop} deleted successfully at {date_time}")
  cursor.execute(drop_table)
  conn.commit()

cursor.close()
conn.close()
print(f"PostgreSQL connection is closed at {date_time}")
print("")