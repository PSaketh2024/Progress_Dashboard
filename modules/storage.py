import json

def load_json():
    with open("data/goals.json","r") as file:
        data = json.load(file)
    return data

def store_json(data):
    with open("data/goals.json","w") as file:
        json.dump(data,file)

