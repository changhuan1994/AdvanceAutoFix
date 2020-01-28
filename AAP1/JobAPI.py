import json
from User import User
from Job import Job
from Mechanic import Mechanic
from JobDataAccess import JobDataAccess
from flask import Flask, Response, redirect, request
import UserAPI
import requests

app = Flask(__name__)

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_key'
)

db = JobDataAccess()

@app.route("/job/single", methods = ["POST"])
def getJobById():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        job_id = request.form.get('job_id', None)
        print("single:: username: %s, job_id: %s" % (username, job_id))
        user = UserAPI.get_user(username)
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        job = db.ReturnJobByID(int(job_id))
        if not isinstance(job, int):
            return json.dumps({'status': 'OK',
                               'job_id': job.get_job_id(),
                               'job_type_id': job.get_job_type_id(),
                               'address': job.get_address(),
                               'details': job.get_details(),
                               'cus_id': job.get_cus_id(),
                               'cus_name': job.get_customer_name(),
                               'job_type_name': job.get_job_type_name()})
        else:
            return json.dumps({'status': 'Failed', 'response': 'Job not found'})

@app.route("/job/whole", methods = ['POST'])
def getWholeJobList():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        user = UserAPI.get_user(username)
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        jobList = db.ReturnJobList()
        # print([job.__dict__ for job in jobList])
        return json.dumps([job.__dict__ for job in jobList])

@app.route("/job/distance", methods = ['POST'])
def getJobListByDistance():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        longitude = request.form.get('longitude', '0')
        latitude = request.form.get('latitude', '0')
        distance = request.form.get('distance', '100')
        preference = request.form.get('preference', None)
        print("distance:: username: %s, longitude: %s, latitude: %s, distance: %s, preference: %s" % (username, longitude, latitude, distance, preference))
        user = UserAPI.get_user(username)
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        pref_str = preference.split(' ')
        pref_int = [int(each) for each in pref_str]
        jobList = db.ReturnJobListUnderdistance(float(longitude), float(latitude), int(distance), user.get_user_id(), pref_int)
        return json.dumps([job.__dict__ for job in jobList])

@app.route("/job/book", methods = ['POST'])
def bookJob():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        job_id = request.form.get('job_id', None)
        store_id = request.form.get('store_id', None)
        print("book:: username: %s, job_id: %s, store_id: %s" % (username, job_id, store_id))
        user = UserAPI.get_user(username)
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        if db.BookJob(int(job_id), int(store_id), int(user.get_user_id())) == 1:
            return json.dumps({'status': 'OK', 'response': 'job booked'})
        else:
            return json.dumps({'status': 'Error', 'response': 'could not book job because of database problem'})

@app.route("/job/unbook", methods = ['POST'])
def unbookJob():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        job_id = request.form.get('job_id', None)
        print("unbook:: useranme: %s, job_id: %s" % (username, job_id))
        user = UserAPI.get_user(username)
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        status = db.ReturnJobHistoryOfJob(int(job_id)).pop()
        status_id = status[0]
        if (status_id in range(1,3)):
            db.UnBookJob(int(job_id))
            db.insertStatus(int(8), int(status[1]), 'pre-job cancel')
            return json.dumps({'status': 'OK', 'response': 'job pre-unbooked'})
        elif (status_id in range(3,5)):
            db.UnBookJob(int(job_id))
            db.insertStatus(int(9), int(status[1]), 'post-job cancel')
            db.insertStatus(int(10), int(status[1]), 'emergency job')
            return json.dumps({'status': 'OK', 'response': 'job post-unbooked'})
        else:
            return json.dumps({'status': 'Error', 'response': 'job cannot be unbooked'})

@app.route("/job/booked/mec", methods = ['POST'])
def getBookedJobsOfMechanic():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        print("booked/mec:: useranme: %s" % (username))
        user = UserAPI.get_user(username)
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        bookingList = db.ReturnBookedJobsWithMecID(user.get_user_id())
        jobList = []
        for each in bookingList:
            jobList.append(db.ReturnJobByID(each[0]))
        return json.dumps([job.__dict__ for job in jobList])

@app.route("/job/qualification", methods = ['POST'])
def getQualificationOfMechanic():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        user = UserAPI.get_user(username)
        print("qualification:: useranme: %s" % (username))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        result = db.ReturnQualificationsWithMecID(user.get_user_id())
        if result == -1:
            return json.dumps({'status': 'OK', 'response': 'User is not qualified to work'})
        else:
            return json.dumps([each for each in result])

@app.route("/job/vediolink", methods = ['POST'])
def getVideoLink():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        user = UserAPI.get_user(username)
        print("link:: useranme: %s" % (username))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        result = db.ReturnJobTypesWithLink()
        if result == -1:
            return json.dumps({'status': 'Error', 'response': 'Faild retrieving data'})
        else:
            return json.dumps([each for each in result]) #[type_id, type_name, link]

@app.route("/job/history", methods = ['POST'])
def getJobHistory():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        user = UserAPI.get_user(username)
        print("history:: useranme: %s, id: %s" % (username, user.get_user_id()))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        result = db.ReturnJobHistoryOfMec(user.get_user_id())
        if result == -1:
            return json.dumps({'status': 'Error', 'response': 'Faild retrieving data'})
        else:
            return json.dumps([each for each in result]) #[job_id, status, time_stamp, customer, job_type]

@app.route("/job/store", methods = ['POST'])
def getNearbyStore():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        longitude = request.form.get('longitude', None)
        latitude = request.form.get('latitude', None)
        user = UserAPI.get_user(username)
        print("store:: useranme: %s, id: %s" % (username, user.get_user_id()))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        result = db.ReturnStoreListUnderDistance(float(longitude), float(latitude), int(6666)) # [id, address]
        if len(result) < 5:
            return json.dumps([each for each in result])
        else:
            return json.dumps([each for each in result[:5]]) # return first five elements

@app.route("/job/current", methods = ['POST'])
def checkCurrentJob():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        user = UserAPI.get_user(username)
        print("job/current:: useranme: %s, id: %s" % (username, user.get_user_id()))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        current_job = getCurrentJob(user.get_user_id())
        if isinstance(current_job, int):
            return json.dumps({'status': 'OK', 'response': 'No current job'})
        else:
            return json.dumps({'status': 'OK',
                               'job_id': current_job.get_job_id(),
                               'job_type_id': current_job.get_job_type_id(),
                               'address': current_job.get_address(),
                               'details': current_job.get_details(),
                               'cus_id': current_job.get_cus_id(),
                               'cus_name': current_job.get_customer_name(),
                               'job_type_name': current_job.get_job_type_name()})

@app.route("/job/status/current", methods = ['POST'])
def getCurrentStatusOfJob():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        job_id = request.form.get('job_id', None)
        user = UserAPI.get_user(username)
        print("job/current/status:: useranme: %s, id: %s, job_id: %s" % (username, user.get_user_id(), job_id))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        status_list = db.ReturnJobHistoryOfJob(int(job_id))
        if len(status_list) > 0:
            status = status_list.pop()
            if (status[0] < 8 or status[0] == 10):
                return json.dumps({'status': 'OK', 'current_status': status[0]})
        return json.dumps({'status': 'OK', 'current_status': '0'}) # no current status.

@app.route("/job/status/update", methods = ['POST'])
def updateStatusOfJob():
    if request.method == 'POST':
        username = request.form.get('user_name', None)
        id_token = request.form.get('id_token', None)
        job_id = request.form.get('job_id', None)
        description = request.form.get('description', None)
        user = UserAPI.get_user(username)
        print("job/status/update:: useranme: %s, id: %s, job_id: %s, description: %s" % (username, user.get_user_id(), job_id, description))
        if not UserAPI.verify_user(username, id_token):
            return json.dumps({'status': 'Error', 'response': 'authentication error'})
        if isinstance(user, int):
            return json.dumps({'status': 'Not_Found', 'response': 'Username not in database'})
        status_list = db.ReturnJobHistoryOfJob(int(job_id))
        if len(status_list) > 0:
            current_status = status_list.pop()
            if (current_status[0] in range(1, 7)) and (current_status[0] != 2):
                status_id = int(current_status[0]) + 1
                db.insertStatus(status_id, int(current_status[1]), description)
                return json.dumps({'status': 'OK', 'response': status_id})
            elif (current_status[0] == 2):
                current = getCurrentJob(user.get_user_id())
                if isinstance(current, int):
                    status_id = int(current_status[0]) + 1
                    db.insertStatus(status_id, int(current_status[1]), description)
                    return json.dumps({'status': 'OK', 'response': status_id})
                else:
                    return json.dumps({'status': 'Error', 'response': 'already have anothor job started'})
        return json.dumps({'status:': 'Error', 'response': 'status not able to update'})

def getCurrentJob(mec_id):
    bookings = db.ReturnBookedJobsWithMecID(mec_id)
    jobList = []
    for each in bookings:
        jobList.append(db.ReturnJobByID(each[0]))
    for each in jobList:
        status_list = db.ReturnJobHistoryOfJob(each.get_job_id())
        if len(status_list) > 0:
            status = status_list.pop()
            if (status[0] > 2 and status[0] < 7):
                return each
    return -1

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0', port = 5001)