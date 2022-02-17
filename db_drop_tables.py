import psycopg2
from datetime import datetime

current_datetime = datetime.now()

conn = psycopg2.connect(
  database="test", 
  user="test", 
  password="test", 
  host="127.0.0.1", 
  port="5432"
)

cursor = conn.cursor()

list_tables = ['people', 'starships', 'persons_with_starships']
for table_to_drop in list_tables:

  drop_table = (f"DROP table {table_to_drop};")
  cursor.execute(drop_table)
  conn.commit()

cursor.close()
conn.close()
print(f"PostgreSQL connection is closed at {current_datetime}")