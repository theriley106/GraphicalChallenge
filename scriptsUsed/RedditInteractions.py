import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from textblob import TextBlob
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
		TEMPDATA[word] = {"Count": 0, "Sentiments": []}
		DATABASE.append({"Word": word, "Occurances": 0, "Sentiment": 0})
	return listOfWords

if __name__ == '__main__':
	'''a = ldJsonToList('../../NootropicsData.json')
	print a[:50]'''
	listOfWords = convertWordList(raw_input("List of Words Filename: "))
	listOfComments = ldJsonToList(raw_input("JSON Containing Comment Data Filename: "))
	print("Analyzing {} words and {} comments".format(len(listOfWords), len(listOfComments)))
	if raw_input("Return Comment Sentiment? (y/n) ").lower() == "y":
		for i, var in enumerate(listOfComments):
			try:
				if i % 1000 == 0:
					print("{} Sentiment".format(i))
				for word in listOfWords:
					for keyword in str(word).split("/"):
						if str(keyword).strip().lower() in str(var).lower():
							TEMPDATA[word]["Sentiments"].append(TextBlob(var["body"]).sentiment.polarity)
			except Exception as exp:
				print exp

	else:
		getSentiment = False
	if raw_input("Verbose (y/n): ") == 'y':
		verbose = True
	else:
		verbose = False
	saveFileName = raw_input("Save Filename: ")
	for word in listOfWords:
		wordCount = 0
		if verbose == True:
			print("Finding {}".format(word))
		for keyword in str(word).split("/"):
			wordCount = wordCount + len(re.findall(str(keyword).lower().strip(), str(listOfComments).lower()))
		TEMPDATA[word]["Count"] = wordCount
	for key, value in TEMPDATA.items():
		for data in DATABASE:
			if data['Word'] == key:
				data['Occurances'] = value['Count']
				if len(value['Sentiments']) > 0:
					data['Sentiment'] = sum(value['Sentiments']) / float(len(value['Sentiments']))
				else:
					data['Sentiment'] = 0

	with open(saveFileName, 'w') as outfile:
		json.dump(DATABASE, outfile)
