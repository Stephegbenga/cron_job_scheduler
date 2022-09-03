import json
from time import sleep
database_list = 'list.json'
database_pause = 'trialcancelled.json'

def find_in_trialcancelled(id, date):
    try:
        db = open(database_pause)
        users = json.loads(db.read())
        for user in users:
            if user['id'] == id and user['date'] == date:
                return user
    except Exception as e:
        print(e)

def add_to_trialcancelled(data):
    try:
        db = open(database_pause)
        db_infos = json.loads(db.read())
        db_infos.append(data)
        with open(database_pause, 'w') as info:
            json.dump(db_infos, info, indent=2)
    except Exception as e:
        print(e)
        return "error"

def remove_from_trialcancelled(req):
    try:
        db = open(database_pause)
        db_infos = json.loads(db.read())
        db_infos.remove(req)
        with open(database_pause, 'w') as info:
            json.dump(db_infos, info, indent=2)
    except Exception as e:
        return "error"


def find_in_list(id):
    try:
        db = open(database_list)
        users = json.loads(db.read())
        for user in users:
            if user['id'] == id:
                return user
    except Exception as e:
        print(e)

def add_to_list(data):
    try:
        db = open(database_list)
        db_infos = json.loads(db.read())
        db_infos.append(data)
        with open(database_list, 'w') as info:
            json.dump(db_infos, info, indent=2)
    except Exception as e:
        print(e)
        return "error"


def remove_from_list(req):
    print(req)
    try:
        db = open(database_list)
        db_infos = json.loads(db.read())
        db_infos.remove(req)
        with open(database_list, 'w') as info:
            json.dump(db_infos, info, indent=2)
    except Exception as e:
        print(e)
        return "error"


def getall():
    db = open(database_list)
    users = json.loads(db.read())
    if users:
        return users
