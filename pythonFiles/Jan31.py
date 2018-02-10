import json
import datetime
import glob
DATABASE = {}

DATASET = json.load(open(glob.glob('static/Jan31.json')[0]))

def returnTime(timestamp):
	return (
	datetime.datetime.fromtimestamp(
		int(timestamp)
	).weekday()
	)

def cleanData():
	for commentData in DATASET:
		e = int(returnTime(commentData["created_utc"]))
		DATABASE[e].append(int(commentData['score']))
	for e in range(7):
		DATA.append({"Day": days[e], "Score": sum(DATABASE[e]) / float(len(DATABASE[e]))})
	return DATA

def getDatabase():
	DATA = []
	for value in DATASET:
		value['Sentiment'] = float(value["Sentiment"])
		DATA.append(value)
	return DATA
