import json

a = []

with open("/media/christopher/ssd/cscareerquestionds.json") as f:
    for line in f:
        a.append(json.loads(line))

print len(a)
