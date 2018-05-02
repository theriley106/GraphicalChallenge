import glob
import csv
import re
import json
ageDB = []
DATABASE = []
valueList = {}

listVal = json.load(open(glob.glob('static/messageWordCount.json')[0]))
print listVal
for val in your_list:
	try:
		age = val[0]
		outcome = val[10]
		if isAdopted(outcome) == True:
			ageDB.append(convertToDays(age))
	except:
		print("Error")

float(sum(ageDB))

for val in ageDB:
	try:
		valueList[str(val / 30)]
	except:
		valueList[str(val / 30)] = 0
	valueList[str(val / 30)] += 1

#print(float(sum(ageDB)) / len(ageDB))

def getDatabase():
	a = []
	for key, value in valueList.iteritems():
		a.append({"Age": key, "Count": value})
	return a
