from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime, timedelta, timezone
import threading
from time import sleep
import requests
import json
from database import find_in_list, add_to_list, remove_from_list, find_in_trialcancelled


def executejob(id, date):
    check_if_is_cancelled = find_in_trialcancelled(id, date)
    if check_if_is_cancelled:
        print("This Trial class has alredy been cancelled")
    else:
        url = "http://127.0.0.1:2001/cronexecute?number={}".format(id)
        response = requests.request("GET", url)
        print(response.text)


def cron(cron_in_secs, id, date):
    if cron_in_secs > 4294967:
            splitted_time = cron_in_secs / 200
            if splitted_time < 4294967:
                for i in range(200):
                    sleep(cron_in_secs/200)
                remove_from_list({"id": id, "date": date})
                executejob(id, date)
            else:
                sleep(3)
                remove_from_list({"id": id, "date": date})
    else:
        sleep(cron_in_secs)
        remove_from_list({"id": id, "date":date})
        executejob(id, date)


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
        print(req)
        check = find_in_list(id, date)
        if check:
            data = {"status": "error", "reason": "Cron Job Already Scheduled"}
        else:
            data = process(date, id)
            if data['status'] == "success":
                add_to_list(req)

        return data




