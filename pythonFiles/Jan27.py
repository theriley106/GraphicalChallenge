import os
import csv
import json
import glob
import datetime
import operator
counts = []
tempFile = []
DATASET = json.load(open(glob.glob('static/Jan27/grammyData.json')[0], 'rb'))
for var in DATASET:
	tempFile.append(var["annualGrammy"])

for var in list(set(tempFile)):
	counts.append({'awardNumber': tempFile.count(var), "grammyNumber": var})

print counts
'''count = sorted(count.items(), key=operator.itemgetter(0))
for key, value in count:
	WSBComments.append(value)'''


def getDatabase():
	return counts
