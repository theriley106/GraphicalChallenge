import glob
import csv

categories = []
DATABASE = []

with open(glob.glob('static/Jan8.csv')[0], 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)


for val in your_list:
	categories.append(val[2])

for category in list(set(categories)):
	DATABASE.append({"Label": category.replace('&', 'and'), "Value": categories.count(category)})


def getDatabase():
	return DATABASE
