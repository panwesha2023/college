# A very simple Flask Hello World app for you to get started with...


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Sneha, this is my first python web application college page'


@app.route('/college')
def college():
   return render_template('college.html')



@app.route('/loginentry')
def loginentry():
   return render_template('login.html')



@app.route('/faillogin')
def faillogin():
   return render_template('faillogin.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('fail', name=user))




@app.route('/success/<name>')
def success(name):
    return 'Hey, welcome %s' % name


@app.route('/fail/<name>')
def fail(name):
    return 'Hey, this is failure case, you have used GET method %s' % name
