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
def by_day(t):
    m, d, y = t['date'].split("-")
    return y, m, d

comments = []
for line in open(glob.glob('static/Feb1.json')[0], 'rb'):
	commentInfo = json.loads(line)
	commentInfo["Date"] = returnTime(commentInfo["created_utc"])
	comments.append(commentInfo)
comments = sorted(comments, key=lambda k: k['Date'])
listOfMentions = []
for comment in comments:
	listOfMentions.append(comment["Date"])
allInfo = []
for mention in list(set(listOfMentions)):
	info = {}
	info["date"] = mention
	info["mentions"] = listOfMentions.count(mention)
	allInfo.append(info)

#print allInfo
#print allInfo.sort(key=lambda item:item['date'], reverse=True)

def getDatabase():
	return sorted(allInfo, key=by_day, reverse=False)
