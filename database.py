import json

database = 'list.json'
def find_in_list(id):
    try:
        db = open(database)
        users = json.loads(db.read())
        for user in users:
            if user['id'] == id:
                return user
    except Exception as e:
        print(e)

def add_to_list(data):
    try:
        db = open(database)
        db_infos = json.loads(db.read())
        db_infos.append(data)
        with open(database, 'w') as info:
            json.dump(db_infos, info, indent=2)
    except Exception as e:
        print(e)
        return "error"

def remove_from_list(req):
    try:
        db = open(database)
        db_infos = json.loads(db.read())
        db_infos.remove(req)
        with open(database, 'w') as info:
            json.dump(db_infos, info, indent=2)
    except Exception as e:
        print(e)
        return "error"

def getall():
    db = open(database)
    users = json.loads(db.read())
    if users:
        return users
