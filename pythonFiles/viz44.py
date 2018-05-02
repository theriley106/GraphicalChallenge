import glob
import json
DATABASE = []

for key, value in json.load(open(glob.glob('static/messageWordCount.json')[0])):
	DATABASE.append({"Words": key, "Count": value})


def getDatabase():
	return DATABASE
