import json
import re

a = {}

companies = open("../static/listOfTechCompanies.txt").read().split("\n")

with open("/media/christopher/ssd/cscareerquestionds.json") as f:
	for i, line in enumerate(f):
		x = re.findall("\w+", json.loads(line)['body'].lower())
		for val in companies:
			if val.lower() in x:
				if val.lower() not in a:
					a[val.lower()] = 0
				a[val.lower()] += 1
		if i % 2000 == 0:
			print(i)

for key, value in a.iteritems():
	print("{} - {} Mentions".format(key, value))

with open('cscareerquestions.json', 'w') as fp:
	json.dump(a, fp)
