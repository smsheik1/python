from flask import Flask,render_template,request,redirect,session,flash
import re
app=Flask(__name__)
app.secret_key='thebestsecretkeyever'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def user():
	return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
	valid = True

	if len(request.form['name']) < 1 :
		flash('name cannot be empty')
		valid = False
	elif len(request.form['name']) > 120:
		flash('name cannot be longer than 120 characters')
		valid = False
	elif request.form['name'].ixsalpha() == True:
		session['name'] = request.form['name']
	

	if len(request.form['email']) <1:
		flash('email cannot be empty')
		valid = False
	elif len(request.form['email']) >120:
		flash('email cannot be longer than 120 characters')
		valid = False
	else:
		session['email'] = request.form['email']

	if len(request.form['password']) <1:
		flash('password cannot be empty')
		valid = False
	elif len(request.form['password']) >120:
		flash('password cannot be longer than 120 characters')
		valid = False
	elif request.form['confirm_password'] != request.form['password']:
		flash('passwords do not match')
		valid = False
	else:
		session['password']=request.form['password']
	
	if valid:
		flash('success')
	return redirect('/')




app.run(debug=True)


