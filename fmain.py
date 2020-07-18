from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator
from flask_sqlalchemy import SQLAlchemy
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell
import os
from flask_mail import Mail, Message


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SECRET_KEY'] = 'QASQAD'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#>test for($ python hello.py shell >>> from hello import db >>> db.create_all())

manager = Manager(app)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()
#<test
"""
def make_shell_context():
    return dict(app = app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context = make_shell_context()))

manager.add_command('db', MigrateCommand)
"""
if __name__ == '__main__':
        app.run(debug=True)
#>mail initialization
mail = Mail(app)
#<mail initialization
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
        #>call forwarding and sessions pr
        session['name'] = form.username.data
        #<
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            db.session.add(user)
            session['known'] = False
            #>send mail for admin
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
            #<send mail for admin
        else:
            session['known'] = True
        session['name'] = form.username.data
        form.username.data = ''
        return redirect(url_for('reg'))
    return render_template('reg.html', form=form, name=session.get('name'), known=session.get('known', False))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

class NameForm(FlaskForm):
    username = StringField('What is your name?', validators=[DataRequired()])
    usermail = StringField('Your email?', validators=[Email()])
    submit = SubmitField('Submit')

#>db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
#>mail
app.config['MAIL_SERVER'] = 'Henry513876@yandex.ru'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin Henry513876@yandex.ru'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAILSENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
#<mail


#<db

    #@app.route('/index')
    #def findex():
        #return render_template('index.html')
#except:
    #@app.route('/')
    #def index():
        #return '<h1> Error <h1>', 400


if __name__ == '__main__':
        app.run(debug=True)
