#!/usr/bin/env python
#program za login, register, chat, 
from flask import * 
from flask.ext.login import LoginManager, login_required
from Flask_db import *
import sqlalchemy

app = Flask(__name__)

import sys
import os.path
def install_secret_key(app, filename='secret_key'):
	filename = os.path.join(app.instance_path, filename)
	app.config['SECRET_KEY'] = open(filename, 'key.txt').read()

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def chat():
	"""chat"""
	return render_template('chat.html')

def load_user(userid):
    return User.get(userid)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('chat'))
    return flask.render_template('login.html', form=form)

@app.route("/settings")
@login_required
def settings():
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

def unauthorized():
    # do stuff
    return a_response

@app.route('/register')
def add_user(username, password, email):
	"""Registracija"""
 	user = Flask_db.User(username, password, email)
 	Flask_db.db.session.add(user)
 	Flask_db.db.commit()
 	loged = True

if True == True:
	app.debug = True
	app.run()



