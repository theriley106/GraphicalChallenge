def genQuery(subReddit):
	return '''SELECT
  body, created_utc

FROM [fh-bigquery:reddit_comments.all]

WHERE subreddit = "SUBREDDIT"'''.replace("SUBREDDIT", subReddit)

if __name__ == '__main__':
	print(genQuery(raw_input("Subreddit: ")))

