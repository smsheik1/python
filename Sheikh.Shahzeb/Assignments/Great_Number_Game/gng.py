from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key='thebestsecretkeyever'

too_low="too low!"
too_high="too high!"
correct="Correct!"

@app.route('/')
def index():
	if not 'rand' in session:
		session['rand']= random.randrange(0,101)
	print session['rand']
	return render_template('gng_index.html')


@app.route('/test', methods=['POST'])
def test():
	print session['rand']

	if not 'guess' in session:
		session['guess']= request.form['guess']

	session['guess']= int(request.form['guess'])

	if session['guess'] > session['rand']:
		print session['guess'], 'You were too high!'
		session['p'] =too_high
	elif  session['guess'] < session['rand']:
		print session['guess'], 'You were too Low!'
		session['p'] =too_low
	elif session['guess'] == session['rand']:
		print session['rand'], 'You Got it!'
		session['p'] = correct
		session.clear()
	return redirect('/')







app.run(debug=True)