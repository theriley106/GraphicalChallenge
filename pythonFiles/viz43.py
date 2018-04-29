import glob
import csv
import re

ageDB = []
DATABASE = []

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

print(sum(ageDB))

def getDatabase():
	return DATABASE
