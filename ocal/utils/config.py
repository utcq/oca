import json

try:
    CONFIG = json.load(open("config.json", "rb"))
except:
    raise EnvironmentError("Missing config.json file")