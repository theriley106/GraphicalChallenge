import json
DB = {"Total": 0}
for vals in json.load(open("SATFlair.json")):
	if vals['author_flair_text'] not in DB:
		DB[vals['author_flair_text']] = 0
	DB[vals['author_flair_text']] += 1
	DB["Total"] += 1

with open('SATData.json', 'w') as fout:
	json.dump(DB, fout)