import glob
import csv
import re
import os
import datetime
DATABASE = []
timeValues = []
Timestamps = open(glob.glob('static/Jan9/TS.txt')[0]).read().split("\n")
for time in Timestamps:
	if '2010' in str(time):
		timeValues.append('2017-' + time.partition("T")[0].partition('-')[2])

Timestamps = []

for var in timeValues:
	Timestamps.append(str(var))
print var

#for t in list(set(Timestamps)):
#	DATABASE[t] = Timestamps.count(t)

start = datetime.datetime.strptime("01-01-2017", "%m-%d-%Y")
end = datetime.datetime.strptime("12-31-2017", "%m-%d-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
print date_generated[0].strftime("%m-%d-%Y")
DATES = []
for i, d in enumerate(date_generated):
	i = i + 1
	DATABASE.append({d.strftime("%Y-%m-%d"): Timestamps.count(d.strftime("%Y-%m-%d"))})


with open(glob.glob('static/Jan9/DOW.csv')[0], 'rb') as f:
	reader = csv.reader(f)
	your_list = list(reader)

for var in your_list:
	try:
		DATES.append({"Y1": (float(Timestamps.count(str(var[0]))) / float(len(Timestamps))) * 100, "Y2": ((float(var[2]) - float(var[1])) / float(var[1])) * 100})
	except:
		pass



def getDatabase():
	return DATES