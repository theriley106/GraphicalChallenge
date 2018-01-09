import csv
import datetime
import operator
import glob


DATABASE = [0]

count = {}
for num in range(31):
	count['{0:02d}'.format(num+1)] = 0

#print count

def returnTime(timestamp):
	return (
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%d')
	)

def returnAllComments():
	with open(glob.glob('static/Jan2.csv')[0], 'rb') as f:
		reader = csv.reader(f)
		for value in list(reader)[1:]:
			if 'tesla' in str(value[0]).lower() or 'tsla' in str(value[0]).lower() or '$tsla' in str(value[0]).lower():
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('$tsla')
				count[str(returnTime(value[1]))] += str(value[0]).lower().count('tesla')
returnAllComments()
count = sorted(count.items(), key=operator.itemgetter(0))
for key, value in count:
	DATABASE.append(value)

def returnDatabase():
	return DATABASE