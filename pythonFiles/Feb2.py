import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import operator
import glob
import json
import datetime

#N_DATASET = json.load()
def returnTime(timestamp):
	return (
	datetime.datetime.fromtimestamp(
		int(timestamp)
	).strftime('%m-%d-%Y')
	)
listOfSchoolInfo = json.load(open(glob.glob('static/Feb2.json')[0], 'rb'))

allInfo = []

for key, value in listOfSchoolInfo.items():
	allInfo.append({"School": key, "Mentions": value})


#print allInfo
#print allInfo.sort(key=lambda item:item['date'], reverse=True)

def getDatabase():
	return sorted(allInfo, key=lambda k: k['Mentions'], reverse=False)
print getDatabase()
