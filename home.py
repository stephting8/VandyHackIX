from flask import Flask, render_template, request
from flask_mail import Mail
from mongodb import mongo
from bson import ObjectId


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["DEBUG"] = True

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
# app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/list_rides')
def rides():
    docs_unfilled = mongo.db.rides.find({"filled":False})
    return render_template('list_rides.html', docs_unfilled = docs_unfilled)

@app.route('/list_rides/requested', methods=['POST'])
def riderequested():
    if request.method == 'POST':

        id = request.form['id']
        mongo.db.rides.update_one({"_id":ObjectId(id)},{'$inc': {'requests_left': -1}})
    return


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
        
        insert=mongo.db.rides.insert_one({"destination":destination, 
                                            "time":time, 
                                            "num_seats":num_seats,
                                            "duration_hr":duration_hr,
                                            "duration_min":duration_min,
                                            "comments":comments, 
                                            "filled":False,
                                            "requests_left":10})
        print(insert)
    return ("")

@app.route('/profile')
def profile():
     return render_template('profile.html')

@app.route('/instructions')
def instructions():
     return render_template('instructions.html')