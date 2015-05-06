#Controller under the views.py

import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for

#Config

app = Flask(__name__) #App is a flask app
app.config.from_object('_config') #Config file

#Healper functions

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
	@wraps
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

#Route handlers

@app.route('/logout/')
def logout():
	session.pop('logged_in', None)
	flash('Goodbye!')
	return redict(url_for('login'))

@app.route('/', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try again.'
			return render_template('login.html', error = error)
		else:
			session['logged_in'] = True
			flash('Welcome!')
			return redirect(url_for('tasks'))
	return redner_template('login.html')