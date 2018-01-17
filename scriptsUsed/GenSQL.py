file = raw_input("Filename: ")
subreddit = raw_input("Subreddit (no /r/) : ")
saveFileName = raw_input("Save Filename: ")
listOfWords = open(file).read().split("\n")


if raw_input("Select Score (Y/N): ").lower() == 'y':
	query = '''SELECT
	  body, created_utc, score

	FROM [fh-bigquery:reddit_comments.all

	WHERE subreddit = "{}" 
	AND (LOWER(body) LIKE LOWER("% {} %")'''.format(subreddit, listOfWords[0])
else:
	query = '''SELECT
	  body, created_utc

	FROM [fh-bigquery:reddit_comments.all]

	WHERE subreddit = "{}" 
	AND (LOWER(body) LIKE LOWER("% {} %")'''.format(subreddit, listOfWords[0])

query = query.replace("\t", "")

for var in listOfWords[1:]:
	query = query + '\nOR LOWER(body) LIKE LOWER("% {} %")'.format(var)

query = query + ")"

f = open(saveFileName,'w')
f.write(query)
f.close()

