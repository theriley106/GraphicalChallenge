import glob
import json
DATABASE = []
airportList = json.load(open(glob.glob('static/airports.json')[0]))


def getDatabase():
	return airportList
