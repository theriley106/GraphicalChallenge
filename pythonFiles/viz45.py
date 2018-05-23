import json
import glob
DATASET = json.load(open(glob.glob('static/45.json')[0], 'rb'))



def getDatabase():
	return DATASET
