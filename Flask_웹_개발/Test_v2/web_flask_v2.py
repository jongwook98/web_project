from flask import Flask, render_template
from flask_navigation import Navigation
from datetime import datetime
import sqlite3 as sql

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234125'
bootstrap = Bootstrap(app)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Accident Scene', 'accident'),
    nav.Item('Defective lane', 'defective_lane'),
    nav.Item('Over Speeding', 'over_speeding')
])

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/navpage/')
def navpage():
    return render_template('navpage.html')


@app.route('/accident/')
def accident():
    con = sql.connect('accident.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from Testcases')

    rows = cur.fetchall();
    return render_template('accident.html', rows=rows)
    

@app.route('/defective_lane/')
def defective_lane():
    con = sql.connect('defective.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from Testcases')

    rows = cur.fetchall();
    return render_template('defective_lane.html', rows=rows)


@app.route('/over_speeding/')
def over_speeding():
    con = sql.connect('over_speeding.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute('select * from Testcases')

    rows = cur.fetchall();
    return render_template('over_speeding.html', rows=rows)


if __name__=='__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=5000, debug=True)
