from flask import Flask, render_template
from flask_wtf import Form #
from wtforms import StringField, SubmitField #
from wtforms.validators import Required #
app = Flask(__name__)


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

@app.route('/reg')
def reg():
    #return '<h1> smth <h1>'
    return render_template('reg.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
#>? work with reg.html
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
#<

    #@app.route('/index')
    #def findex():
        #return render_template('index.html')
#except:
    #@app.route('/')
    #def index():
        #return '<h1> Error <h1>', 400

if __name__ == '__main__':
    app.run(debug=True)
