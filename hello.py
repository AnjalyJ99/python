from flask import Flask

app=Flask(__name__)

from markupsafe import escape

@app.route('/')
def root():
	return '<h1>Flask server is running</h1>'

@app.route('/user/<username>')
def show_user(username):
	return ' <h1>Username is %s</h1>' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'post id is %d' % post_id

@app.route('/path/<path:subpath>')
def show_path(subpath):
	return '<h1>subpath</h1> id is %s' % subpath