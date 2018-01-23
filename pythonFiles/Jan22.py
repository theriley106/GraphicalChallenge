import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import operator
import glob
import json
import math

DATABASE = []
DATABASE2 = []
allData = json.load(open(glob.glob('static/Jan22/allACTData.json')[0], 'rb'))
redditData = json.load(open(glob.glob('static/Jan22/actData.json')[0], 'rb'))


for key, val in allData.items():
	try:
		info = {"Score": int(key), "allAmount": float(val) / float(allData['Total']) * 100, "redditAmount": 0}
		if redditData[str(key)] > 1:
			info['redditAmount'] = float(redditData[str(key)] / float(redditData["Total"])) * 100

		DATABASE.append(info)
	except:
		pass


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