import json

FILE_PATH = "data/skills.json"

def load_json():
    with open(FILE_PATH,"r") as file:
        data = json.load(file)
    return data

def store_json(data):
    with open(FILE_PATH,"w") as file:
        json.dump(data,file,indent = 4)

