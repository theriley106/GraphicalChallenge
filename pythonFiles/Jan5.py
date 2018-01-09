import glob
import csv

usernames = []
DATABASE = []

with open(glob.glob('static/Jan5.csv')[0], 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)


for val in your_list:
	usernames.append(val[1])

for user in list(set(usernames)):
	DATABASE.append({"User": user, "Count": usernames.count(user)})

DATABASE = sorted(DATABASE, key=lambda k: k['Count'], reverse=True)[:5]


def getDatabase():
	return DATABASE