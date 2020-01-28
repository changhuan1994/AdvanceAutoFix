import json
from User import User
from Mechanic import Mechanic
from UserDataAccess import UserDataAccess
from flask import Flask, Response, redirect, request
import requests

app = Flask(__name__)

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_key'
)

db = UserDataAccess()

@app.route('/')
def hello_world():
    return json.dumps({'status': 'OK', 'response': 'Hello Minglun'})

@app.route("/login", methods = ["POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        print(username)
        print(id_token )
        user = get_user(username)
        if not verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        return json.dumps({'status': 'Found', 'response': 'username in the system'})

@app.route("/signup", methods = ["POST"])
def signup():
    if request.method == 'POST':
        user_name = request.form.get('user_name', None)
        full_name = request.form.get('full_name', None)
        address = request.form.get('address', None)
        bio = request.form.get('bio', None)
        ASECert_id = request.form.get('ASECert_id', None)
        ASECert_pic = request.form.get('ASECert_pic', None)
        paypal_info = request.form.get('paypal_info', None)
        licence = request.form.get('licence', None)
        id_token = request.form.get('id_token', None)
        if not verify_user(user_name, id_token):
            return json.dumps({'status': 'Failed', 'response': 'User not created because verification failed'})
        flag = db.AddUser( full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_pic) # None is for password. It is removed
        if flag == True:
            return json.dumps({'status': 'OK', 'response': 'User Created'})
    return json.dumps({'status': 'Failed', 'response': 'User not created becuase of database error'})

@app.route("/profile", methods = ["POST", "PUT"])
def display_profile():
    if request.method == 'POST':
        user_name = request.form.get('user_name', None)
        print (user_name)
        id_token = request.form.get('id_token', None)
        user = get_user(user_name)
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'No user found with given username'})
        if not verify_user(user_name, id_token):
            return json.dumps({'status': 'error', 'response': 'authentication error'})
        if user != None:
            return json.dumps({'status': 'OK',
                               'user_id': user.get_user_id(),
                               'full_name': user.get_full_name(),
                               'user_name': user.get_user_name(),
                               'ASECert_id': user.get_ASECert_id(),
                               'adress': user.get_address(),
                               'bio': user.get_bio(),
                               'paypal_info': user.get_paypal_info(),
                               'ASECert_pic': user.get_ASECert_HTTP()})
        return json.dumps({'status': 'Failed', 'response': "For Unknown Reason"})
    if request.method == 'PUT':
        user_id = request.form.get('user_id', None)
        user_name = request.form.get('user_name', None)
        full_name = request.form.get('full_name', None)
        ASECert_id = request.form.get('ASECert_id', None)
        ASECert_pic = request.form.get('ASECert_pic', None)
        address = request.form.get('address', None)
        bio = request.form.get('bio', None)
        paypal_info = request.form.get('paypal_info', None)
        id_token = request.form.get('id_token', None)
        print(user_name)
        user = get_user(user_name)
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'No user found with given username'})
        if not verify_user(user_name, id_token):
            return json.dumps({'status': 'error', 'response': 'authentication error'})
        db.UpdateUserByUserID( user_id, full_name, user_name, ASECert_id, address, bio, paypal_info, ASECert_pic) # None for password which has been removed
        # update user here
        return json.dumps({'status': 'OK', 'response': 'user updated'})

def get_user(username):
    raw_user = db.ReturnUserByUserName( username )
    if not isinstance(raw_user, int):
        if isinstance(raw_user[0], bytearray):
            user = Mechanic(raw_user[0].decode('utf-8'), raw_user[1].decode('utf-8'), raw_user[2].decode('utf-8'), raw_user[3].decode('utf-8'), raw_user[4].decode('utf-8'), raw_user[5].decode('utf-8'), raw_user[6].decode('utf-8'), raw_user[7].decode('utf-8'))
            return user
        user = Mechanic(raw_user[0], raw_user[1], raw_user[2], raw_user[3], raw_user[4], raw_user[5], raw_user[6], raw_user[7])
        print(user.get_user_name())
        return user
    else:
        return -1

def verify_user(username, token):
    URL = "https://oauth2.googleapis.com/tokeninfo"
    PARAMS = {'id_token': token}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    print("Google auth result: status: %d, %s with token %s" % (r.status_code, data, token))
    if r.status_code == 200 and data['email'] == username:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port = 5002)