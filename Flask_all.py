#!/usr/bin/env python
#program za login, register, chat, 
from flask import *
from Flask_db import *
import sqlalchemy

app.debug = True
loged = False

@app.route('/')
def chat():
	"""chat"""
	if loged == True:
		return render_template('chat.html')
	else:
		return render_template('login.html')

@app.route('/login')
def login(username, password):
	"""Login"""
	user = User.query.filter_by(username = username).first()
	password = User.query.filter_by(password = password).first()
	if password == password and username == username:
		loged = True
		flask.redirect(url_for('chat'))
	else:
    	#gres na /login
		loged = False
		return "Login failed"
	return render_template('login.html')

@app.route('/register')
def add_user(username, password, email):
	"""Registracija"""
 	user = Flask_db.User(username, password, email)
 	Flask_db.db.session.add(user)
 	Flask_db.db.commit()
 	loged = True
	
if __name__ == "__main__":
	app.debug = True
	app.run()