from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime, timedelta, timezone
import threading
from time import sleep
import requests
import json
from database import find_in_list, add_to_list, remove_from_list


def executejob(id):
    url = "http://127.0.0.1:2001/cronexecute?number={}".format(id)
    response = requests.request("GET", url)
    print(response.text)

def cron(cron_in_secs, id, date):
    if cron_in_secs > 30:
        for i in range(30):
            sleep(cron_in_secs/30)
    else:
        sleep(cron_in_secs)
    remove_from_list({"id": id, "date":date})
    executejob(id)


def process(date, id):
    org_date = date
    china_now = datetime.now(timezone(timedelta(hours=8)))
    china_now = china_now.strftime('%Y-%m-%d+%H:%M')
    china_now = f"{china_now}"
    date = datetime.strptime(date, '%Y-%m-%d+%H:%M')
    china_now = datetime.strptime(china_now, '%Y-%m-%d+%H:%M')

    if date > china_now:
        diff = date - china_now
        diff = diff.total_seconds()
        threading.Thread(target=cron, args=[diff, id, org_date]).start()
        data = {"status": "success"}
    else:
        data = {"status": "error", "reason": "date is in the past"}

    return data


class update(Resource):
    def get(self, date, id):
        req = {"date": date, "id": id}
        check = find_in_list(id)

        if check:
            data = {"status": "error", "reason": "Cron Job Already Scheduled"}
        else:
            data = process(date, id)
            if data['status'] == "success":
                add_to_list(req)

        return data




