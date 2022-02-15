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

print("Database opened successfully")

name='ilon'
gender='male'
homeworld='mars'
starships='BFR'

fill_table_people = (f"INSERT INTO people (name, gender, homeworld, starships) VALUES ('{name}', '{gender}', '{homeworld}', '{starships}');")
cursor.execute(fill_table_people)
conn.commit()

cursor.close()
conn.close()
print(f"PostgreSQL connection is closed at {current_datetime}")