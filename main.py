from scheduler import *
from flask_restful import Resource, Api, request
from database import getall, find_in_trialcancelled, add_to_trialcancelled, add_to_list
app = Flask(__name__)
api = Api(app)

cron_jobs = getall()
if cron_jobs:
    for cron_job in cron_jobs:
        print(cron_job)
        date = cron_job["date"]
        id = cron_job["id"]
        try:
            callback = cron_job["callback"]
        except:
            callback = "https://asanafinder.com/cronexecute"
        data = process(date, id, callback)
        print(data)
        if data['status'] == 'error':
            remove_from_list({"id": id, "date":date})


@app.route('/')
def homepage():
    return "Cron Task Scheduler"

@app.route('/cancel_trialclass', methods=['POST'])
def cancel_trialclass():
    req = request.get_json()
    id = req["id"]
    date = req["date"]
    check = find_in_trialcancelled(id, date)

    if check:
        message = "leads trial already cancelled"
    else:
        add_to_trialcancelled(req)
        message = "Leads trial cancelled successfully"
    return message


@app.route('/cronschedule', methods=['POST'])
def cronschedule():
    req = request.get_json()
    print(req)
    if not req or "id" not in req or "date" not in req:
        return {"status": "error", "reason": "id or date not in request"}
    id = req["id"]
    date = req["date"]
    callback = req["callback"]
    data = process(date, id, callback)
    if data['status'] == 'success':
        add_to_list(req)
    return data


if __name__ == '__main__':
    app.run(port=6001)
