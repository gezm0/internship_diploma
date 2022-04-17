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
print(f"PostgreSQL connection is closed at {current_datetime}")