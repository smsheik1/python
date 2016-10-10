from flask import Flask,render_template,redirect, session,request, flash

app=Flask(__name__)
app.secret_key= 'thebestsecretkeyever'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def showuser():
	print request.form
	if len(request.form['name']) < 1:
		print ['name']
		flash('name cannot be empty')
		return redirect('/')
	elif len(request.form['name']) > 120:
		flash('name can only contain 120 characters')
		return redirect('/')
	session['name']= request.form['name']
	session['location']= request.form['location']
	session['language']= request.form['language']
	return redirect('/result')


@app.route('/result')
def results():
	return render_template('results.html')


app.run(debug=True)