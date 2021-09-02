from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def landing():
	return render_template('landing.html')

@app.route('/about')
def about():
	return render_template('about.html')

app.run(host='0.0.0.0')