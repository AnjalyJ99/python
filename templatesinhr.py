from flask import Flask,render_template,url_for,request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
	message="This is home page"
	return render_template('layouts.html',message=message)

@app.route('/news')
def news():
	message='This is news page'
	return render_template('page.html',message=message)

@app.route('/about')
def about():
	message='This is about page'
	return render_template('page.html',message=message)