import json
import glob
from datetime import datetime
import calendar

d = datetime.utcnow()
unixtime = calendar.timegm(d.utctimetuple())
print unixtime


def timeSince(utc):
	# Lower num means more recent
	d = datetime.utcnow()
	unixtime = calendar.timegm(d.utctimetuple())
	return int(unixtime) - int(utc)

'''allData = []
	tempData = {}
	for line in open("dataset.json", "rb"):
		info = json.loads(line)
		try:
			if "[deleted]" not in str(info['author']) and "author_flair_text" in info:
				try:
					info['author_flair_text'] = int(info['author_flair_text'])
					# This means the comment was deleted
					commentAuthor = info['author']
					if commentAuthor in tempData:
						if timeSince(info['created_utc']) < timeSince(tempData[commentAuthor]['created_utc']):
							# It's newer
							tempData[commentAuthor] = info
					else:
						tempData[commentAuthor] = info
				except:
					pass
		except:
			print 'error'
	for keys, vals, in tempData.items():
		allData.append(vals)

	with open("your_json_file", "w") as fp:
		json.dump(allData , fp)
	print len(tempData.keys())
'''

if __name__ == '__main__':
	a = json.load(open(glob.glob('static/rTDataset.json')[0], 'rb'))
	allNums = []
	tempData = []
	average = 0.0
	for val in a:
		if val['author_flair_text'] < 20 and val['author_flair_text'] > 10:
			average += val['author_flair_text']
			allNums.append(str(val['author_flair_text']))
		else:
			a.remove(val)
	average = float(average) / float(len(a))
	print average
	for val in list(set(allNums)):
		tempData.append({"Age": val, "Count": allNums.count(val)})
	with open("thisWorks.json", "w") as fp:
		json.dump(tempData , fp)
	print tempData

