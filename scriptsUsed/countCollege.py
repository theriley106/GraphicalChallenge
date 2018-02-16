import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import json
import glob
DB = {"Total": 0}
finalList = {}
listF = []
listOfSchools = open("listOfSchools.txt").read().split("\n")
for val in listOfSchools:
	schoolName = val.partition("|")[0].strip()
	for name in val.split("|"):
		if len(name) > 1:
			finalList[name.lower().strip()] = schoolName.lower().strip()

def getCollege(text):
	info = []
	# input string of text and it returns colleges inside
	for college in finalList.keys():
		if college in str(text):
			for i in range(str(text).count(college)):
				info.append(finalList[college])
	return info

def ldJsonToList(jsonFile):
	DATA = []
	for var in open(glob.glob(jsonFile)[0], 'rb').read().split('\n'):
		try:
			DATA.append(json.loads(var))
		except:
			pass
	return DATA

for comment in ldJsonToList("SchoolList.json"):
	try:
		for val in getCollege(comment['body']):
			listF.append(val)
	except:
		pass
DATA = {}

for val in list(set(listF)):
	DATA[val] = listF.count(val)


print DATA
'''
for vals in json.load(open("SATFlair.json")):
	if vals['author_flair_text'] not in DB:
		DB[vals['author_flair_text']] = 0
	DB[vals['author_flair_text']] += 1
	DB["Total"] += 1

with open('SATData.json', 'w') as fout:
	json.dump(DB, fout)
'''
