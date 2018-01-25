import json
SAT_2017_TAKERS = 1715481

def inverse():
	for key, value in satListz.items():
		value = int(value)
		key = int(key)
		if value not in flipped:
			flipped[value] = [key]
		else:
			flipped[value].append(key)
	newList = []
	for key, value in flipped.items():
		if len(value) > 1:
			newKey = "{}-{}".format(int(min(float(s) for s in value)), int(max(float(s) for s in value)))
		else:
			newKey = "{}-{}".format(value[0], value[0])
		newList.append({"Score": newKey, "Percentile": key})
	return newList

DB = []
listOfRanges = sorted(json.load(open("rangeSAT.json")), key=lambda k: k['Percentile'], reverse=True)
#Json dict containing format: {"Percentile": 98, "Score": "1420-1440"} - sorted by the percentile
highValue = {"Percentile": 100, "Score": "1700-1700"}
while True:
	if len(listOfRanges) == 0:
		lowValue = {"Percentile": 0, "Score": "0-0"}
	else:
		lowValue = listOfRanges[0]	
	#print("{} Difference between {} and {}".format(, highValue['Score'], lowValue['Score']))
	lowEnd, highEnd = highValue['Score'].split('-')
	percentDiff = float(highValue['Percentile'] - lowValue["Percentile"])
	print percentDiff
	#DB.append({"Score": highValue['Score'], "Students": (SAT_2017_TAKERS * percentDiff) * .01})
	totalScores = ((int(highEnd)-int(lowEnd)) / 10) + 1
	percentReceived = percentDiff / float(totalScores)

	for val in range(int(lowEnd), int(highEnd)+10, 10):
		totalTestTakers = SAT_2017_TAKERS * ((percentDiff / float(totalScores))*.01)
		DB.append({"Score": int(val), "Students": int(totalTestTakers)})
	if len(listOfRanges) == 0:
		break
	highValue = listOfRanges[0]
	listOfRanges.remove(highValue)

with open('satScoreIndi.json', 'w') as fp:
    json.dump(DB, fp)