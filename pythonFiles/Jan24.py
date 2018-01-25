import glob
import csv
import json
from uszipcode import ZipcodeSearchEngine
#search = ZipcodeSearchEngine()
primaryDataset = json.load(open(glob.glob('static/Jan24.json')[0], 'rb'))
def returnLongLatFromZIP(zipCode):
	a = search.by_zipcode(str(zipCode))
	print a["Latitude"]
	return {"Longitude": a["Longitude"], "Latitude": a["Latitude"]}

'''
primaryDataset = json.load(open(glob.glob('static/Jan24.json')[0], 'rb'))
for val in primaryDataset:
	try:
		data = returnLongLatFromZIP(val['zip'])
		if data["Longitude"] != None:
			val["Longitude"] = data["Longitude"]
			val["Latitude"] = data["Latitude"]
			DB.append(val)
	except:
		pass
'''



def genDatabase():
	return primaryDataset
