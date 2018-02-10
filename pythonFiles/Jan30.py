import json
import datetime
import glob
DATABASE = {}

DATASET = []
for line in open(glob.glob('static/Jan30.json')[0], 'rb'):
	try:
		DATASET.append(json.loads(line))
	except:
		pass

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
	return DATASET
