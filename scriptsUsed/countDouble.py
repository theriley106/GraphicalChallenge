import RedditInteractions
listOfComments = RedditInteractions.ldJsonToList(raw_input("JSON Containing Comment Data Filename: "))
count = 0

for comment in listOfComments:
	if 'theanine' in str(comment['body']).lower():
		if 'caffeine' in str(comment['body']).lower():
			count += 1

print count