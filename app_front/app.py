#!/usr/local/bin/python

import os
import psycopg2
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.environ["db_host"],
                            database=os.environ["TF_VAR_db_name"],
                            user=os.environ["TF_VAR_db_user"],
                            password=os.environ["TF_VAR_db_password"],
                            port="5432")
    return conn


def stress_test():
    prew = cur = 1
    element = 1750000
    
    for _ in range(int(element-2)):
        prew, cur = cur, prew + cur


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
    SELECT persons_with_starships.name, persons_with_starships.gender, persons_with_starships.homeworld, 
    starships.name, starships.model, starships.cargo_capacity 
    FROM persons_with_starships, starships 
    WHERE persons_with_starships.ships_id=starships.ship_id order by starships.cargo_capacity desc limit 10;
    ''')
    persons = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', persons=persons, datetime=datetime.now())


@app.route('/drop')
def drop():
    file_drop = open(r'drop.py', 'r').read()
    exec(file_drop)


@app.route('/recreate')
def recreate():
    file_create = open(r'create.py', 'r').read()
    exec(file_create)


@app.route('/stress')
def stress():
    stress_test()
    return render_template('stress.html', datetime=datetime.now())


if __name__ == "__main__":
    app.run(host='0.0.0.0')