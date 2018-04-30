import glob
import csv
import re

ageDB = []
DATABASE = []
valueList = {}

with open(glob.glob('static/aac_shelter_outcomes.csv')[0], 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

def convertToDays(age):
	if 'year' in str(age).lower():
		return int(re.findall("\d+", str(age))[0]) * 365
	if 'month' in str(age).lower():
		return int(re.findall("\d+", str(age))[0]) * 30
	else:
		return int(re.findall("\d+", str(age))[0])

def isAdopted(outcomeString):
	return ('adopt' in str(outcomeString).lower())

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
print valueList

def getDatabase():
	return DATABASE
