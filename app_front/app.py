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


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("select name, gender, homeworld, ship_model, ship_manufacturer, cargo_capacity from persons limit 10;")
    persons = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', persons=persons, datetime=datetime.now())


if __name__ == "__main__":
    app.run(host='0.0.0.0')