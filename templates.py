from flask import Flask,render_template,url_for,request

from markupsafe import escape


app=Flask(__name__)

@app.route('/')
def root():
	message = 'Flask server is running'
	return render_template('index.html',message=message)
@app.route('/users')
def show_users():
	users=[{"name":"User1","age":22},{"name":"user2","age":25}]
	return render_template('users.html',users=users)

@app.route('/create-user',methods=['GET','POST'])
def create_user():
	if request.method == 'POST':
		#accept data
		username=request.form['username']
		password=request.form['password']
		if username=='admin' and password=='test@123':
			message='login success'
			return render_template('create_user.html',message=message)
		else:
			message='Login failed,invalid credentials'
			return render_template('create_user.html',message=message)

		return username
	else:
		return render_template('create_user.html')
