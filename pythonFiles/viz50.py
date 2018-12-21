import json

a = []

companies = open("../static/listOfTechCompanies.txt").read().split("\n")

with open("/media/christopher/ssd/cscareerquestionds.json") as f:
    for line in f:
        a.append(json.loads(line))

print len(a)
print len(companies)
