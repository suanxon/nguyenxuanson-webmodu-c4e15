import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds157873.mlab.com:57873/xuanson

host = "ds157873.mlab.com"
port = 57873
db_name = "xuanson"
user_name = "admin1"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
