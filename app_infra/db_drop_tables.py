#!/usr/local/bin/python

import psycopg2
import requests
import os
from datetime import datetime

conn = psycopg2.connect(
  database=os.environ["TF_VAR_db_name"], 
  user=os.environ["TF_VAR_db_user"], 
  password=os.environ["TF_VAR_db_password"], 
  host=os.environ["db_host"], 
  port="5432")

cursor = conn.cursor()

list_tables = ['starships', 'persons_with_starships']
for table_to_drop in list_tables:

  drop_table = (f"DROP TABLE IF EXISTS {table_to_drop};")
  print(f"Table {table_to_drop} deleted successfully at {datetime.now()}")
  cursor.execute(drop_table)
  conn.commit()

cursor.close()
conn.close()
print(f"PostgreSQL connection is closed at {datetime.now()}")
print("")