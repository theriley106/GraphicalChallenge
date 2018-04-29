import glob
import csv
import re

ageDB = []
DATABASE = []

with open(glob.glob('static/aac_shelter_outcomes.csv')[0], 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

def convertToDays(age):
	try:
		if 'year' in str(age).lower():
			return int(re.findall("\d+", str(age))[0]) * 365
		if 'month' in str(age).lower():
			return int(re.findall("\d+", str(age))[0]) * 30
		else:
			return int(re.findall("\d+", str(age))[0])
	except:
		print("Exception detected")

def isAdopted(outcomeString):
	return ('adopt' in str(outcomeString).lower())

for val in your_list:
	age = val[0]
	outcome = val[10]

for category in list(set(categories)):
	DATABASE.append({"Label": category.replace('&', 'and'), "Value": categories.count(category)})


def getDatabase():
	return DATABASE
