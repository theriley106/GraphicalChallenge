import glob
import csv
import json
from uszipcode import ZipcodeSearchEngine
search = ZipcodeSearchEngine()

def returnLongLatFromZIP(zipCode):
	a = search.by_zipcode(str(zipCode))[0]
	return {"Longitude": a["Longitude"], "Latitude": a["Latitude"]}


primaryDataset = json.load(open(glob.glob('static/Jan24.json')[0], 'rb'))
for val in primaryDataset:
	longitude, latitude = returnLongLatFromZIP(val['zip'])
	val["Longitude"] = longitude
	val["Latitude"] = latitude

with open('satScoreIndi.json', 'w') as fp:
    json.dump(primaryDataset, fp)

def readCSVs():
	DATABASE = []
	for csvFile in returnAllCSV(BUSNUM):
		with open(csvFile, 'rb') as f:
			reader = csv.reader(f)
			your_list = list(reader)
			for your_listz in your_list:
				try:
					DATABASE.append({"Lat": your_listz[2], "Long": your_listz[1]})
				except Exception as exp:
					print exp
					pass
	return DATABASE

def genDatabase():
	DATABASE = readCSVs()
	DATABASE = [dict(t) for t in set([tuple(d.items()) for d in DATABASE])]
	DATABASE = DATABASE[:500]
	return DATABASE

