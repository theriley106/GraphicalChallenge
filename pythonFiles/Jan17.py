import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import operator
import glob
import json

DATABASE = []

N_DATASET = json.load(open(glob.glob('static/Jan17/Nootropics_Jan17.json')[0], 'rb'))
SA_DATASET = json.load(open(glob.glob('static/Jan17/StackAdvice_Jan17.json')[0], 'rb'))


for N_Value in N_DATASET:
	for SA_Value in SA_DATASET:
		if N_Value["Word"] == SA_Value["Word"]:
			tempData = {}
			tempData['Name'] = N_Value["Word"].split('/')[0].strip()
			tempData['Nootropics'] = N_Value
			tempData['StackAdvice'] = SA_Value
			DATABASE.append(tempData)

def returnTime(timestamp):
	return (
	datetime.datetime.fromtimestamp(
		int(timestamp)
	).strftime('%m-%Y')
	)

def getDatabase():
	return DATABASE


if __name__ == '__main__':
	print DATABASE