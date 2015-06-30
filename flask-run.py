#!/usr/bin/env python
from flask import *
app = Flask(__name__)

app.debug = True

@app.route('/')
def hello():
	return render_template('layout.html')

if __name__ == "__main__":
	app.debug = True
	app.run()