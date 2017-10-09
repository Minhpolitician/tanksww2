
import mongoengine
#mongodb://<dbuser>:<dbpassword>@ds113435.mlab.com:13435/tank_ww2

host = "ds113435.mlab.com"
port = 13435
db_name = "tank_ww2"
user_name = "Sherman_Jumbo"
password = "TriangulumM33"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
