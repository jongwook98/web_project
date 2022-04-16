import pathlib
from flask import Flask, render_template, session, redirect, url_for, flash, request
from datetime import datetime
import sqlite3 as sql

from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234125'
bootstrap = Bootstrap(app)


@app.route('/')#, methods=['GET', 'POST'])
def index():
    return render_template('index.html')
   

'''
@app.route('/obstacle_detect/')
def obstacle():
    return render_template('obstacle.html', top=top, left=left)
'''

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


'''
@app.route('/accident/')#, methods = ['POST', 'GET'])
def accident():
    accident_case = 0
    for path in pathlib.Path("static/img/accident_scene").iterdir():
        if path.is_file():
            accident_case += 1
    
    
    if request.method == 'POST' :
        try:
            num = accident_case + 1
            path = "static/img/accident_scene_"+str(num)
            infor = "25, 30"
            time = datetime.now()

            with sql.connect('accident.db') as con :
                cur = con.cursor()

                cur.execute('INSERT INTO Testcases (case_, image_path, information, datetime) VALUES (?,?,?,?)', (num, path, infor, time))
                con.commit()
                msg = 'Record successfully added'
                accident_case += 1
        except:
            con.rollback()
            msg = 'Error in insert operation'
        finally:
            return render_template('accident.html', case=accident_case, msg=msg)
            con.close()
    else:
        return render_template('accident.html', case=accident_case)
    
    return render_template('accident.html', case=accident_case)
 

@app.route('/defective_lane/')
def defective_lane():
    defective_lane_case = 0
    for path in pathlib.Path("static/img/defective_lane").iterdir():
        if path.is_file():
            defective_lane_case += 1
    return render_template('defective_lane.html', case=defective_lane_case)


@app.route('/over_speeding/')
def over_speeding():
    over_speeding_case = 0
    for path in pathlib.Path("static/img/over_speeding").iterdir():
        if path.is_file():
            over_speeding_case += 1
    return render_template('over_speeding.html', case=over_speeding_case)
'''

if __name__=='__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000, debug=True)
