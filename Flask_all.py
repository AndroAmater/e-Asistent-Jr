#program za login, register, chat, 
import flask
from Flask_db import *
import sqlalchemy

app.debug = True

@app.route('/')
def chat():
	"""chat"""
	return 'Hello World!'

@app.route('/login')
def login(,username, password):
	"""Login"""
	user = User.query.filter_by(username = username).first()
	password = User.query.filter_by(password = password).first()
    if password == password and username == username:
       flask.redirect(url_for('chat')
       	loged = True
    else:
    	#gres na /login
@app.route('/register')
def add_user(username, password, email):
	"""Registracija"""
 	user = Flask_db.User(username, password, email)
 	Flask_db.db.session.add(user)
 	Flask_db.db.commit()
 	loged = True
	



