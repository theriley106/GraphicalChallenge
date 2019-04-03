import json

a = json.load(open("static/kaggle.json"))
print()

def getAll():
	vals = []
	for val in a['datasetListItems']:
		vals.append({"title": "", "description": val['overview'], "image": val['thumbnailImageUrl'], "link": "https://www.kaggle.com"+val['datasetUrl']})
	return vals