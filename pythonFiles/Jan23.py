import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import operator
import glob
import json
import math

DATABASE = []
DATABASE2 = []
#allData = json.load(open(glob.glob('static/Jan23/SAT_SCORE_INDIVIDUAL_ESTIMATES.json')[0], 'rb'))
redditData = json.load(open(glob.glob('static/Jan23/SATData.json')[0], 'rb'))
#rangeData = json.load(open(glob.glob('static/Jan23/SAT_SCORE_RANGE_SCORES.json')[0], 'rb'))
toSum = []
TOTAL_COMMENTS = len(redditData)

a = 0
for key, val in redditData.items():
	a += val
redditData["Total"] = a

for key, val in redditData.items():
	if key != "Total" and int(key) < 1601:
		DATABASE.append({"redditData": (float(val) / redditData['Total']) * 100, "Score": key})
'''for key, val in redditData.items():
	for value in rangeData:
		if key in tuple(value["Score"].split("-")):
			if 'redditData' not in ["Score"]:
				value["redditData"] = 0
			value["redditData"] += int(redditData[key])
			break
for val in rangeData:
	try:
		toSum.append(val['redditData'])
	except:
		rangeData.remove(val)

print a


e = []
for key, val in redditData.items():
	#print val
	e.append({"percent": ((float(val) / float(redditData['Total'])) * 100), "score": key})

e = sorted(e, key=lambda k: k['percent'], reverse=True)
for val in e[:12]:
	#print val['percent']
	print("- {} - {}%".format(val['score'], round(val['percent'],2)))

for value in rangeData:
	try:
		value["redditPercent"] = (float(value["redditData"]) / float(redditData['Total'])) * 100
	except:
		value["redditPercent"] = 0
	value["allPercent"] = (float(value["Students"]) / float(1715481)) * 100
	value['startRange'] = value['Score'].split('-')[0]

#print rangeData'''

'''for value in allData:
	#for key, val in value.items():
		try:
			info = {"Score": int(value["Score"]), "allAmount": (float(value["Students"]) / float(1715481)) * 100, "redditAmount": redditData[str(value["Score"])]}
			if redditData[str(value["Score"])] > 1:
				info['redditAmount'] = float(redditData[str(value["Score"])] / float(redditData["Total"])) * 100

			DATABASE.append(info)
		except:
			pass'''


def returnTime(timestamp):
	return (
	datetime.datetime.fromtimestamp(
		int(timestamp)
	).strftime('%m-%Y')
	)

def getDatabase():
	return DATABASE


if __name__ == '__main__':
	print DATABASE