
# A very simple Flask Hello World app for you to get started with...


from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime, date

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


def calculate_age(birthdate):
       today = date.today()
       years = today.year - birthdate.year
       months = today.month - birthdate.month


       if today.day < birthdate.day:
           months -= 1

           if months < 0:
               years -= 1
               months += 12

       return years, months


@app.route("/", methods=["GET"])
def home():
    return 
    render_template("login.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        first_name = request.form['first']
        last_name = request.form['last']
        dob_str = request.form['dob']

        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        years, months = calculate_age(dob)


        full_name = first_name + " " + last_name

        return redirect(url_for('success', full_name=full_name, years=str(years), months=str(months)))
    else:
        user = request.args.get('username')
        return redirect(url_for('fail', name=user))


@app.route('/success/<full_name>/<years>/<months>')
def success(full_name, years, months):
    return f"Hey, welcome {full_name}. Your age is {years} years and {months} months."


@app.route('/fail/<name>')
def fail(name):
    return 'Hey, this is failure case, you have used GET method %s' % name




@app.route('/step1')
def step1():
   return render_template('step2.html')



@app.route('/step3', methods=['POST', 'GET'])
def step3():
    if request.method == 'POST':
        user_first_name = request.form['firstname']
        user_last_name = request.form['lastname']
        print("step3 user first name: ",user_first_name)
        print("step3 user last name: ",user_last_name)
        full_name = user_first_name + " " + user_last_name
        print("step3 full name: ",full_name)
        return redirect(url_for('step4success', name=full_name))
    else:
        user_first_name = request.form['firstname']
        user_last_name = request.form['lastname']
        full_name = user_first_name + " " + user_last_name
        return redirect(url_for('step5failure', name=full_name))


@app.route('/step4success/<name>')
def step4success(name):
    return 'This message is from step4success, welcome  %s' % name



@app.route('/step5failure/<name>')
def step5failure(name):
    return 'This message is from,  welcome  %s' % name



