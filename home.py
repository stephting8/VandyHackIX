# from flask import Flask, render_template, request
# from flask_mail import Mail
# from mongodb import mongo
# from bson import ObjectId


# app = Flask(__name__)
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config["DEBUG"] = True

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# # app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
# # app.config['MAIL_PASSWORD'] = 'your_password'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/list_rides')
# def rides():
#     docs_unfilled = mongo.db.rides.find({"filled":False})
#     return render_template('list_rides.html', docs_unfilled = docs_unfilled)

# @app.route('/list_rides/requested', methods=['POST'])
# def riderequested():
#     if request.method == 'POST':

#         id = request.form['id']
#         mongo.db.rides.update_one({"_id":ObjectId(id)},{'$inc': {'requests_left': -1}})


#     return


# @app.route('/create_rides')
# def createrides():

#     return render_template('create_rides.html')


# @app.route('/insert_rides', methods=['POST'])
# def insertrides():
#     print("test")
#     if request.method == 'POST':
#         print("got POST")
#         destination=request.form['destination']
#         time = request.form['time']
#         num_seats = request.form['num_seats']
#         duration_hr = request.form['duration_hr']
#         duration_min = request.form['duration_min']
#         comments = request.form['comments']

#         print("here")
        
#         insert=mongo.db.rides.insert_one({"destination":destination, 
#                                             "time":time, 
#                                             "num_seats":num_seats,
#                                             "duration_hr":duration_hr,
#                                             "duration_min":duration_min,
#                                             "comments":comments, 
#                                             "filled":False,
#                                             "requests_left":10})
#         print(insert)
#     return ("")

# @app.route('/profile')
# def profile():
#      return render_template('profile.html')

# @app.route('/instructions')
# def instructions():
#      return render_template('instructions.html')






from flask import Flask, render_template, request, url_for, redirect, session
# from .mongodb import mongo
from authlib.integrations.flask_client import OAuth
 
app = Flask(__name__)
app.secret_key = 'rainbows'
 
# oauth config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='996812295199-8fj9vdhr48itim94uhosi3u5fh45c3up.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    # This is only needed if using openId to fetch user info
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)
 
app.config['TEMPLATES_AUTO_RELOAD'] = True
# @app.route('/')
# def home():
#     return render_template('home.html')
 
# @app.route('/login')
# def login():
#     return render_template('login.html')
 
 
@app.route('/')
def home():
    email = dict(session).get('email', None)
    return f'Hello, {email}!'
 
 
@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)
 
 
@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return redirect('/')
 
 
@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')
 
 
@app.route('/list_rides')
def rides():
    return render_template('list_rides.html')
 
 
@app.route('/create_rides', methods=['POST'])
def createrides():
    if request.method == 'POST':
        destination = request.form['destination']
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