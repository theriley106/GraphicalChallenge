import json
from textblob import TextBlob
import re

def getLyricSentiment(lyrics):
	lyrics = re.sub('\s+',' ',lyrics)
	return TextBlob(lyrics).sentiment.polarity


with open('data.json') as json_data:
	d = json.load(json_data)
for e in d:
	e['Sentiment'] = getLyricSentiment(e["Lyrics"])

with open('dataWS.json', 'w') as outfile:
	json.dump(d, outfile)
