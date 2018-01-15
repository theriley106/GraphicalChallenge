import csv
import re
import json
#"([a-zA-Z0-9_ -)\-\n]*?)"
listOfDrugNames = []
allComments = str(open("dnmComments.txt").read()).split("\n")
database = {}
mentionCount = {}
with open('drugNames.json') as json_data:
    #drugNamesJson = 
    for mainName, streetNames in json.load(json_data, strict=False).items():
    	listOfDrugNames.append(mainName)
    	mentionCount[mainName] = 0
    	database[mainName] = mainName
    	for name in streetNames:
    		listOfDrugNames.append(name)
    		database[name] = mainName

for i, comment in enumerate(allComments):
	try:
		for drug in listOfDrugNames:
			if drug in list(set(comment.split(' '))):
				mentionCount[database[str(drug)]] += 1
				break
	except:
		print("comment error {}".format(i))
print mentionCount
with open('drugmentions.txt','w') as f:
	f.write(str(mentionCount))