import glob
import json
DATABASE = []
lngLatList = open(glob.glob('static/listOfLongLat.txt')[0]).read().split("\n")


def getDatabase():
	DATABASE = []
	for val in lngLatList:
		splitList = val.split(",")
		info = {"Latitude": splitList[1].strip(), "Longitude": splitList[0].strip()}
		DATABASE.append(info)
	return DATABASE
