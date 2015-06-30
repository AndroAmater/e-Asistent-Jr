#Flask add user to db
import Flask_db

def add_user(username, password, email):
 	user = Flask_db.User(username, password, email)
 	Flask_db.db.session.add(user)
 	Flask_db.db.commit()
 	