#flask_db

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///easistent.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=False)
    email = db.Column(db.String(255), unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email= email

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
            return True

    def is_active(self):
            return True
    
    def is_anonymous(self):
            return False
    
    def get_id(self):
            return unicode(self.id)
    
    