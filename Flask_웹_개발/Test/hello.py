#from flask import Flask, redirect, url_for, render_template
#from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

from flask_bootstrap import Bootstrap

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[InputRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234125'
bootstrap = Bootstrap(app)
#bootstrap.config['SECRET_KEY']

#moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    #name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
        #name = form.name.data
        #form.name.data = ''
    #return render_template('index.html', form=form, name=name)
    return render_template('index.html', form=form, name=session.get('name'))

    #return render_template('index.html', current_time=datetime.now())
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

    #return '<h1>Hello, %s!</h1>' % name

@app.route('/accident/')
def acci():
    return render_template('accident.html')


@app.route('/showImg')
def showImg():
    return render_template('showImg.html')

if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
