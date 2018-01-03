import csv

def returnAllComments():
	with open('wsbcomments.csv', 'rb') as f:
		reader = csv.reader(f)
		return list(reader)