from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QASQAD'


#try:
@app.route('/')
def index():
    #return '<h1> smth <h1>'
    return render_template('index.html')

@app.route('/link1')
def link_1():
    #return '<h1> smth <h1>'
    return render_template('link_1.html')

@app.route('/link2')
def link_2():
    #return '<h1> smth <h1>'
    return render_template('link_2.html')

@app.route('/reg', methods = ['GET', 'POST'])
def reg():
    #name = None
    form = NameForm()
    if form.validate_on_submit():
        #name = form.username.data
        session['username'] = form.username.data
        return redirect(url_for('reg'))
        #form.username.data = ''
        #add usermail!
    #return '<h1> smth <h1>'
    return render_template('reg.html', form=form, name=session.get('username'))
"""
@app.route('/reg')
def reg():
    form = NameForm()
    #return '<h1> smth <h1>'
    return render_template('reg.html', form=form)"""

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

class NameForm(FlaskForm):
    username = StringField('What is your name?', validators=[DataRequired()])
    usermail = StringField('Your email?', validators=[Email()])
    submit = SubmitField('Submit')



    #@app.route('/index')
    #def findex():
        #return render_template('index.html')
#except:
    #@app.route('/')
    #def index():
        #return '<h1> Error <h1>', 400

if __name__ == '__main__':
    app.run(debug=True)
