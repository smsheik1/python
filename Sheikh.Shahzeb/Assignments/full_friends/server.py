from flask import Flask,render_template,request,redirect,session,flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'Full_Friends')


@app.route('/')
def index():
	query= 'SELECT * FROM users'
	users=mysql.query_db(query)
	print users
	return render_template('index.html', users = users)


@app.route('/friends', methods = ['POST'])
def create():
	add_friends= request.form['first_name']
	insert_query= 'INSERT into users (first_name) values ("{}")'.format(add_friends)
	mysql.query_db(insert_query)
	return redirect('/')


@app.route('/friends/<id>/edit')
def update(id):
	query='UPDATE users SET first_name=:first_name WHERE id =:id'


#@app.route('/friends/<id>')


#@app.route('friends/<id>/delete')






#@app.route('/friends/<id>/edit')
app.run(debug= True)