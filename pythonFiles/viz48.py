import json
import datetime
import glob
DATABASE = {}

DATASET = []
for line in open(glob.glob('static/formerPizzaHuts.json')[0], 'rb'):
	try:
		DATASET.append(json.loads(line))
	except:
		pass
for i in range(24):
	DATABASE[i] = []
DATA = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def returnTime(timestamp):
	return (
	datetime.datetime.fromtimestamp(
		int(timestamp)
	).hour
	)

def cleanData():
	for commentData in DATASET:
		e = int(returnTime(commentData["created_utc"]))
		DATABASE[e].append(int(commentData['score']))
	for e in range(len(DATABASE)):
		if e >= 12:
			v = int(e)-12
			if v == 0:
				v = 12
			timePeriod = "{}:00 PM".format(v)
		else:
			if int(e) == 0:
				e = 12
			timePeriod = "{}:00 AM".format(e)
		DATA.append({"Day": timePeriod, "Score": sum(DATABASE[e]) / float(len(DATABASE[e]))})
	return DATA

def getDatabase():
	return cleanData()
