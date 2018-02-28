from textblob import TextBlob
import glob
femaleSentiment = []
maleSentiment = []

for comment in open(glob.glob("static/FemaleTwitterComments.txt")[0], 'rb').read().split('\n'):
	femaleSentiment.append(TextBlob(comment).sentiment.polarity)

for comment in open(glob.glob("static/MaleTwitterComments.txt")[0], 'rb').read().split('\n'):
	maleSentiment.append(TextBlob(comment).sentiment.polarity)


male = float(sum(maleSentiment)) / float(len(maleSentiment))
female = float(sum(femaleSentiment)) / float(len(femaleSentiment))


def getDatabase():
	return {"Male": male, "Female": female}

