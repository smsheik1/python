from flask import Flask,render_template,request,redirect,flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	query='SELECT * FROM users'
	users=mysql.query_db(query)
	print users
	return render_template('index.html', users = users)

@app.route('/success', methods=['POST'])
def users():
	user_email = request.form['email']
	insert_query= 'INSERT into users (email) values ("{}")'.format(user_email)
	mysql.query_db(insert_query)

	return redirect('/')




app.run(debug=True)


