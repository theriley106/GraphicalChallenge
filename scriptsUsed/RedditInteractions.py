import json
import glob
import re
#from bson import json_util
TEMPDATA = {}
DATABASE = []
print("This is going to find occurances of a LIST OF WORDS in a NEW-LINE DELIMETED JSON FILE and return NON-NEW LINE Delimited JSON\n\n")

def ldJsonToList(jsonFile):
	DATA = []
	for var in open(glob.glob(jsonFile)[0], 'rb').read().split('\n'):
		try:
			DATA.append(json.loads(var))
		except:
			pass
	return DATA

def convertWordList(wordListFile):
	listOfWords = open(wordListFile).read().split("\n")
	for word in listOfWords:
		TEMPDATA[word] = 0
		DATABASE.append({"Word": word, "Occurances": 0, "Sentiment": 0})
	return listOfWords

if __name__ == '__main__':
	'''a = ldJsonToList('../../NootropicsData.json')
	print a[:50]'''
	listOfWords = convertWordList(raw_input("List of Words Filename: "))
	listOfComments = ldJsonToList(raw_input("JSON Containing Comment Data Filename: "))
	print("Analyzing {} words and {} comments".format(len(listOfWords), len(listOfComments)))
	if raw_input("Return Comment Sentiment? (y/n) ").lower() == "y":
		getSentiment = True
	else:
		getSentiment = False
	if raw_input("Verbose (y/n): ") == 'y':
		verbose = True
	else:
		verbose = False
	saveFileName = raw_input("Save Filename: ")
	if getSentiment == False:
		for word in listOfWords:
			if verbose == True:
				print("Finding {}".format(word))
			TEMPDATA[word] = len(re.findall(word.lower(), str(listOfComments).lower()))
		for key, value in TEMPDATA.items():
			for data in DATABASE:
				if data['Word'] == key:
					data['Occurances'] = value

	with open(saveFileName, 'w') as outfile:
		json.dump(DATABASE, outfile)
