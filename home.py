from flask import Flask, render_template
app = Flask(__name__)
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


@app.route('/profile')
def profile():
     return render_template('profile.html')

@app.route('/instructions')
def instructions():
     return render_template('instructions.html')