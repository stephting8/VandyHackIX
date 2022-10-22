from flask import Flask, render_template, request
from mongodb import mongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/list_rides')
def rides():
    return render_template('list_rides.html')

@app.route('/create_rides')
def createrides():

    
    return render_template('create_rides.html')


@app.route('/insert_rides', methods=['POST'])
def insertrides():
    print("test")
    if request.method == 'POST':
        print("got POST")
        destination=request.form['destination']
        time = request.form['time']
        num_seats = request.form['num_seats']
        duration_hr = request.form['duration_hr']
        duration_min = request.form['duration_min']
        comments = request.form['comments']

        print("here")
        
        insert=mongo.db.rides.insert_one({"destination":destination, "time":time, "num_seats":num_seats,"duration_hr":duration_hr,"duration_min":duration_min,"comments":comments})
        print(insert)
    return ("")

@app.route('/profile')
def profile():
     return render_template('profile.html')

@app.route('/instructions')
def instructions():
     return render_template('instructions.html')