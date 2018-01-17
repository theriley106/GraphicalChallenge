

print("This is going to find occurances of a LIST OF WORDS in a NEW-LINE DELIMETED JSON FILE and return NON-NEW LINE Delimited JSON\n\n")

listOfWords = open(raw_input("List of Words Filename: ")).read().split("\n")
listOfWords = open(raw_input("JSON Containing Comment Data Filename: ")).read().split("\n")
print("Analyzing {} words".format(len(listOfWords)))
if raw_input("Return Comment Sentiment? (y/n) ").lower() == "y":
	getSentiment = True
else:
	getSentiment = False

saveFileName = raw_input("Save Filename: ")