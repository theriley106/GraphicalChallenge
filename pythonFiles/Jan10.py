import os
import csv
import glob
import datetime
import operator
WSBComments = []
count = {}
for num in range(31):
	count['{0:02d}'.format(num+1)] = 0

def returnTime(timestamp):
	return (
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%d')
	)
with open(glob.glob('static/Jan10.csv')[0], 'rb') as f:
    reader = csv.reader(f)
    for var in list(reader):
    	if 'yolo' in str(var).lower():
    		count[str(returnTime(var[1]))] += str(var[0]).lower().count('yolo')
    		#WSBComments.append(var[1])

count = sorted(count.items(), key=operator.itemgetter(0))
for key, value in count:
	WSBComments.append(value)


def getDatabase():
	return WSBComments