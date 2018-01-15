import requests
import bs4
import glob
import csv
import json


with open(glob.glob('static/Jan13.json')[0], 'rb') as json_data:
    DATABASE = json.load(json_data)

NEW_DATABASE = []
for key, value in DATABASE.items():
    NEW_DATABASE.append({"Drug": key, "Occurances": value})

def getDatabase():
    return NEW_DATABASE