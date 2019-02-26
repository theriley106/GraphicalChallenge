import json

a = json.load(open("static/kaggle.json"))
print()

def getAll():
	vals = []
	for val in a['datasetListItems']:
		vals.append({"description": val['title'], "image": val['thumbnailImageUrl'], "link": "https://www.kaggle.com"+val['datasetUrl']})
	return vals