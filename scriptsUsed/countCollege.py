import json
DB = {"Total": 0}
finalList = {}
listOfSchools = open("listOfSchools.txt").read().split("\n")
for val in listOfSchools:
	schoolName = val.partition("|")[0].strip()
	for name in val.split("|"):
		finalList[name.lower().strip()] = schoolName.lower().strip()
print finalList
while True:
	print(finalList[raw_input("schoolName: ").lower()])
'''def getCollege(text):
	# input string of text and it returns colleges inside

for vals in json.load(open("SATFlair.json")):
	if vals['author_flair_text'] not in DB:
		DB[vals['author_flair_text']] = 0
	DB[vals['author_flair_text']] += 1
	DB["Total"] += 1

with open('SATData.json', 'w') as fout:
	json.dump(DB, fout)
'''
