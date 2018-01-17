import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from textblob import TextBlob
import glob
import json
DATA = []
sentiments = []
positiveComments = 0
negativeComments = 0
def ldJsonToList(jsonFile):
	DATA = []
	for var in open(glob.glob(jsonFile)[0], 'rb').read().split('\n'):
		try:
			value = json.loads(var)
			DATA.append(value['body'])
		except Exception as exp:
			print exp
			pass
	return DATA

listOfComments = ldJsonToList(raw_input("JSON Containing Comment Data Filename: "))
for i, var in enumerate(listOfComments):
	if i % 1000 == 0:
		print("{} Sentiment".format(i))
	senValue = TextBlob(var).sentiment.polarity
	if senValue > 0:
		positiveComments += 1
	else:
		negativeComments += 1

print("Positive: {}\nNegative: {}".format(positiveComments, negativeComments))