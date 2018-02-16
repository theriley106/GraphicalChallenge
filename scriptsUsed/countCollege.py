import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
import json
import glob
import traceback
DB = {"Total": 0}
finalList = {}
listF = []
listOfSchools = open("listOfSchools.txt").read().split("\n")
for val in listOfSchools:
	schoolName = val.partition("|")[0].strip()
	for name in val.split("|"):
		if len(name) > 1:
			finalList[name.lower().strip()] = schoolName.lower().strip()

def checkWords(word, text):
	word = word.split(" ")
	text = text.split(" ")
	if len(word) > 2:
		totalCount = 0
		if word[0] in text and word[1] in text:
			count1 = text.count(word[0])
			count2 = text.count(word[1])
			if count1 < count2:
				totalCount += count1
			else:
				totalCount += count2
	else:
		totalCount += text.count(word[0])
	return totalCount




def getCollege(text):
	info = []
	# input string of text and it returns colleges inside
	for college in finalList.keys():
		for i in range(len(college.split(" "))):
			if '"{}'.format(college.split(" ")[i]) in str(list(text.split(" "))):
				for i in range(str(text).count('"{}'.format(college.split(" ")[i]))):
					info.append(finalList[college])
					break

	return info

def ldJsonToList(jsonFile):
	DATA = []
	for var in open(glob.glob(jsonFile)[0], 'rb').read().split('\n'):
		try:
			DATA.append(json.loads(var))
		except:
			pass
	return DATA
listOfAllSchoolNames = ldJsonToList("SchoolList.json")
for i, comment in enumerate(listOfAllSchoolNames):
	print("{} / {}".format(i, len(listOfAllSchoolNames)))
	try:
		for val in getCollege(comment['body']):
			listF.append(val)
	except Exception as exp:
		traceback.print_exc()
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
