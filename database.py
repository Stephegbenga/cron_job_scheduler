import json
from time import sleep

from pymongo import MongoClient

config = {
    'db_url':'mongodb+srv://yoga:aqqSvjd5ACywhiby@cluster0.iia2mvf.mongodb.net/?retryWrites=true&w=majority',
    'db_name':'CronScheduler'
}

dburl = config['db_url']
conn = MongoClient(dburl)

db = conn.get_database(config['db_name'])

database_list = db.get_collection('list')
database_pause = db.get_collection('trialcancelled')

def find_in_trialcancelled(id, date):
    dataa = database_pause.find_one({"id": id, "date": date})
    return dataa


def add_to_trialcancelled(data):
    try:
        data.pop('_id', None)
        dataa = database_pause.insert_one(data)
        print(dataa)
        return dataa
    except Exception as e:
        print(e)


def remove_from_trialcancelled(req):
    try:
        dataa = database_pause.delete_one({"id": req['id'], "date": req['date']})
        print(dataa)
        return (dataa)
    except Exception as e:
        print(e)


def find_in_list(id):
    dataa = database_list.find_one({"id": id})
    return dataa


def add_to_list(data):
    try:
        data.pop('_id', None)
        dataa = database_list.insert_one(data)
        print(dataa)
        return dataa
    except Exception as e:
        print(e)


def remove_from_list(req):
    try:
        dataa = database_list.delete_one({"id": req['id'], "date": req['date']})
        print(dataa)
        return (dataa)
    except Exception as e:
        print(e)


def getall():
    dataa = database_list.find({})
    templates_array = []
    for data in dataa:
        data.pop('_id', None)
        templates_array.append(data)

    return templates_array