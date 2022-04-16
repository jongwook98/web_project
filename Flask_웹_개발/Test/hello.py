import pathlib
from flask import Flask, render_template, session, redirect, url_for, flash
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField
#from wtforms.validators import InputRequired

from flask_bootstrap import Bootstrap

#class NameForm(FlaskForm):
#    name = StringField('What is your name?', validators=[InputRequired()])
#submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234125'
bootstrap = Bootstrap(app)
#moment = Moment(app)


@app.route('/')#, methods=['GET', 'POST'])
def index():
    '''
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        #form.name.data = ''
        return redirect(url_for('index'))
        name = form.name.data
        #form.name.data = ''
    '''
    #return render_template('index.html', form=form, name=name)
    return render_template('index.html')
   

'''
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
'''

'''
@app.route('/obstacle_detect/')
def obstacle():
    return render_template('obstacle.html', top=top, left=left)
'''

@app.route('/accident/')
def accident():
    accident_case = 0
    for path in pathlib.Path("static/img/accident_scene").iterdir():
        if path.is_file():
            accident_case += 1
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


if __name__=='__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000, debug=True)
