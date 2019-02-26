import json

a = json.load(open("static/kaggle.json"))
print(a['datasetListItems'])