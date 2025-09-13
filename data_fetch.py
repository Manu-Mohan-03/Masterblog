import json

def load_data(filepath):
    with open(filepath,"r") as handle:
        return json.load(handle)