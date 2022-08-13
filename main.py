from scheduler import *
from flask_restful import Resource, Api
from database import getall
app = Flask(__name__)
api = Api(app)

cron_jobs = getall()
if cron_jobs:
    for cron_job in cron_jobs:
        date = cron_job["date"]
        id = cron_job["id"]
        data = process(date, id)
        if data['status'] == 'error':
            remove_from_list({"id": id, "date":date})


@app.route('/')
def homepage():
    return "Cron Task Scheduler"


api.add_resource(update, '/cronschedule/<string:date>/<string:id>')


if __name__ == '__main__':
    app.run()
