import os
import psycopg2
from flask import Flask, render_template

select_output = '''
    select persons_with_starships.name, persons_with_starships.gender, persons_with_starships.homeworld, starships.name, 
    starships.model, starships.cargo_capacity from persons_with_starships, starships 
    where persons_with_starships.ships_id=starships.ship_id 
    order by starships.cargo_capacity desc 
    limit 10;
    '''

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.environ["db_host"],
                            database=os.environ["TF_VAR_db_name"],
                            user=os.environ["TF_VAR_db_user"],
                            password=os.environ["TF_VAR_db_password"],
                            port="5432")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(select_output)
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)