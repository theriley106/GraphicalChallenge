import json
import datetime
DATABASE = {}
for i in range(7):
	DATABASE[i] = []
a = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DATA = [{'Score': 2.2638123763170563, 'Day': days[0]}, {'Score': 2.3354531001589827, 'Day': days[1]}, {'Score': 2.3465874924834638, 'Day': days[2]}, {'Score': 2.567317621681162, 'Day': days[3]}, {'Score': 2.3878993114346994, 'Day': days[4]}, {'Score': 2.906929142267234, 'Day': days[5]}, {'Score': 2.6537889364429086, 'Day': days[6]}]
def returnTime(timestamp):
	return (
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).weekday()
	)
def cleanData():
	with open('ALL_CC_Comments.json') as f:
	    for line in f:
	        j_content = json.loads(line)
	        e = int(returnTime(j_content["created_utc"]))
	        DATABASE[e].append(days[int(j_content['score'])])

	for e in range(7):
		DATA.append({"Day": e, "Score": sum(DATABASE[e]) / float(len(DATABASE[e]))})

	print DATA

def getDatabase():
	return DATA
