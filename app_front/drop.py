#!/usr/local/bin/python

import psycopg2
import os
from datetime import datetime

conn = psycopg2.connect(
  database=os.environ["TF_VAR_db_name"], 
  user=os.environ["TF_VAR_db_user"], 
  password=os.environ["TF_VAR_db_password"], 
  host=os.environ["db_host"], 
  port="5432")

cursor = conn.cursor()

drop_table_1 = (f"DELETE FROM persons_with_starships;")
print(f"Table persons_with_starships cleared successfully at {datetime.now()}")
cursor.execute(drop_table_1)
conn.commit()

drop_table_2 = (f"DELETE FROM starships;")
print(f"Table starships cleared successfully at {datetime.now()}")
cursor.execute(drop_table_2)
conn.commit()

cursor.close()
conn.close()
print(f"PostgreSQL connection is closed at {datetime.now()}")