from flask import Flask, render_template, request
from .mongodb import mongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/list_rides')
def rides():
    return render_template('list_rides.html')

@app.route('/create_rides', methods=['POST'])
def createrides():
    if request.method == 'POST':
        destination=request.form['destination']
        time = request.form['time']
        num_seats = request.form['num_seats']
        duration_start = request.form['duration_start']
        duration_end = request.form['duration_end']
        num_seats = request.form['num_seats']



    return render_template('create_rides.html')


@app.route('/profile')
def profile():
     return render_template('profile.html')

@app.route('/instructions')
def instructions():
     return render_template('instructions.html')